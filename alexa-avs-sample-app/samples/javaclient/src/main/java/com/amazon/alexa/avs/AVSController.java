/**
 * Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Amazon Software License (the "License"). You may not use this file
 * except in compliance with the License. A copy of the License is located at
 *
 * http://aws.amazon.com/asl/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
 */
package com.amazon.alexa.avs;

import com.amazon.alexa.avs.AVSAudioPlayer.AlexaSpeechListener;
import com.amazon.alexa.avs.audio.SimpleAudioPlayer;
import com.amazon.alexa.avs.auth.AccessTokenListener;
import com.amazon.alexa.avs.config.DeviceConfig;
import com.amazon.alexa.avs.exception.DirectiveHandlingException;
import com.amazon.alexa.avs.exception.DirectiveHandlingException.ExceptionType;
import com.amazon.alexa.avs.http.AVSClient;
import com.amazon.alexa.avs.http.AVSClientFactory;
import com.amazon.alexa.avs.http.LinearRetryPolicy;
import com.amazon.alexa.avs.http.ParsingFailedHandler;
import com.amazon.alexa.avs.message.request.RequestBody;
import com.amazon.alexa.avs.message.request.RequestFactory;
import com.amazon.alexa.avs.message.request.settings.LocaleSetting;
import com.amazon.alexa.avs.message.request.settings.Setting;
import com.amazon.alexa.avs.message.response.Directive;
import com.amazon.alexa.avs.message.response.alerts.DeleteAlert;
import com.amazon.alexa.avs.message.response.alerts.SetAlert;
import com.amazon.alexa.avs.message.response.alerts.SetAlert.AlertType;
import com.amazon.alexa.avs.message.response.audioplayer.ClearQueue;
import com.amazon.alexa.avs.message.response.audioplayer.Play;
import com.amazon.alexa.avs.message.response.notifications.SetIndicator;
import com.amazon.alexa.avs.message.response.speaker.SetMute;
import com.amazon.alexa.avs.message.response.speaker.VolumePayload;
import com.amazon.alexa.avs.message.response.speechsynthesizer.Speak;
import com.amazon.alexa.avs.message.response.system.SetEndpoint;
import com.amazon.alexa.avs.message.response.templateruntime.CardHandler;
import com.amazon.alexa.avs.message.response.templateruntime.RenderTemplate;
import com.amazon.alexa.avs.ui.NotificationsUIHandler;
import com.amazon.alexa.avs.wakeword.WakeWordDetectedHandler;
import com.amazon.alexa.avs.wakeword.WakeWordIPC;
import com.amazon.alexa.avs.wakeword.WakeWordIPC.IPCCommand;
import com.amazon.alexa.avs.wakeword.WakeWordIPCFactory;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.Executors;
import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicLong;

import javax.sound.sampled.LineUnavailableException;

public class AVSController implements RecordingStateListener, AlertHandler, AlertEventListener,
        AccessTokenListener, DirectiveDispatcher, AlexaSpeechListener, ParsingFailedHandler,
        UserActivityListener, WakeWordDetectedHandler {

    private AudioCapture microphone;
    private AudioCapture audioFileCapture;
    private AVSClient avsClient;

    private final DialogRequestIdAuthority dialogRequestIdAuthority;
    private AlertManager alertManager;
    private boolean eventRunning = false; // is an event currently being sent

    private static final AudioInputFormat AUDIO_TYPE = AudioInputFormat.LPCM;
    private static final String START_SOUND = "res/start.mp3";
    private static final String END_SOUND = "res/stop.mp3";
    private static final String ERROR_SOUND = "res/error.mp3";
    private static final SpeechProfile PROFILE = SpeechProfile.NEAR_FIELD;
    private static final String FORMAT = "AUDIO_L16_RATE_16000_CHANNELS_1";

    private static final Logger log = LoggerFactory.getLogger(AVSController.class);
    private static final long MILLISECONDS_PER_SECOND = 1000;
    private static final long USER_INACTIVITY_REPORT_PERIOD_HOURS = 1;

    private final AVSAudioPlayer player;
    private BlockableDirectiveThread dependentDirectiveThread;
    private BlockableDirectiveThread independentDirectiveThread;
    private BlockingQueue<Directive> dependentQueue;
    private BlockingQueue<Directive> independentQueue;
    public SpeechRequestAudioPlayerPauseController speechRequestAudioPlayerPauseController;
    private ScheduledExecutorService scheduledExecutor = Executors.newScheduledThreadPool(1);

    private AtomicLong lastUserInteractionTimestampSeconds;

    private Set<ExpectSpeechListener> expectSpeechListeners;
    private ExpectStopCaptureListener stopCaptureHandler;

    private boolean wakeWordAgentEnabled = false;

    private WakeWordIPC wakeWordIPC = null;
    private boolean acceptWakeWordEvents = true; // to ensure we only process one event at a time
    private WakeWordDetectedHandler wakeWordDetectedHandler;
    private final int WAKE_WORD_AGENT_PORT_NUMBER = 5123;
    private final int WAKE_WORD_RELEASE_TRIES = 5;
    private final int WAKE_WORD_RELEASE_RETRY_DELAY_MS = 1000;
    private final AVSClientFactory avsClientFactory;
    private final DirectiveEnqueuer directiveEnqueuer;
    private final DeviceConfig config;
    private NotificationManager notificationManager;
    private CardHandler cardHandler;
    private ResultListener listener;

    public AVSController(AVSAudioPlayerFactory audioFactory, AlertManagerFactory alarmFactory,
            AVSClientFactory avsClientFactory, DialogRequestIdAuthority dialogRequestIdAuthority,
            WakeWordIPCFactory wakewordIPCFactory, DeviceConfig config) throws Exception {

        this.avsClientFactory = avsClientFactory;
        this.wakeWordAgentEnabled = config.getWakeWordAgentEnabled();

        this.config = config;

        if (this.wakeWordAgentEnabled) {
            try {
                log.info("Creating Wake Word IPC | port number: " + WAKE_WORD_AGENT_PORT_NUMBER);
                this.wakeWordIPC =
                        wakewordIPCFactory.createWakeWordIPC(this, WAKE_WORD_AGENT_PORT_NUMBER);
                this.wakeWordIPC.init();
                Thread.sleep(1000);
                log.info("Created Wake Word IPC ok.");
            } catch (IOException e) {
                log.error("Error creating Wake Word IPC ok.", e);
            }
        }

        initializeMicrophone();

        // Ensure that we have attempted to finish loading all relevant data from file and the
        // downchannel has been successfully set up before sending synchronize state
        CountDownLatch loadBeforeSync = new CountDownLatch(3);
        listener = new ResultListener() {
            private boolean setLocaleCalled;

            @Override
            public void onSuccess() {
                loadBeforeSync.countDown();
                sendSyncAndLocale();
            }

            @Override
            public void onFailure() {
                loadBeforeSync.countDown();
                sendSyncAndLocale();
            }

            private void sendSyncAndLocale() {
                // Send synchronize state and set location once the file operations have finished.
                if (loadBeforeSync.getCount() <= 0) {
                    try {
                        log.info("Start sending SynchronizeStateEvent");
                        sendSynchronizeStateEvent();
                        if (!setLocaleCalled) {
                            setLocale(config.getLocale());
                            setLocaleCalled = true;
                        }
                    } catch (InterruptedException e) {
                        log.error("Could not send SynchronizeState event", e);
                    }
                }
            }
        };

        this.player = audioFactory.getAudioPlayer(this);
        this.player.registerAlexaSpeechListener(this);
        this.dialogRequestIdAuthority = dialogRequestIdAuthority;
        speechRequestAudioPlayerPauseController =
                new SpeechRequestAudioPlayerPauseController(player);

        dependentQueue = new LinkedBlockingDeque<>();

        independentQueue = new LinkedBlockingDeque<>();

        directiveEnqueuer = new DirectiveEnqueuer(dialogRequestIdAuthority, dependentQueue,
                independentQueue, this);

        avsClient = avsClientFactory.getAVSClient(directiveEnqueuer, this, listener);

        alertManager = alarmFactory.getAlertManager(this, this, AlertsFileDataStore.getInstance());

        // ensure we notify AVS of playbackStopped on app exit
        Runtime.getRuntime().addShutdownHook(new Thread() {
            @Override
            public void run() {
                player.stop();
                avsClient.shutdown();
            }
        });

        dependentDirectiveThread =
                new BlockableDirectiveThread(dependentQueue, this, "DependentDirectiveThread");
        independentDirectiveThread =
                new BlockableDirectiveThread(independentQueue, this, "IndependentDirectiveThread");

        lastUserInteractionTimestampSeconds =
                new AtomicLong(System.currentTimeMillis() / MILLISECONDS_PER_SECOND);
        scheduledExecutor.scheduleAtFixedRate(new UserInactivityReport(),
                USER_INACTIVITY_REPORT_PERIOD_HOURS, USER_INACTIVITY_REPORT_PERIOD_HOURS,
                TimeUnit.HOURS);
    }

    public void init(ListenHandler listenHandler, NotificationIndicator notificationIndicator,
            CardHandler cardHandler) {
        // Initialize all GUI-related handlers
        this.stopCaptureHandler = listenHandler;
        this.expectSpeechListeners = new HashSet<>(
                Arrays.asList(listenHandler, speechRequestAudioPlayerPauseController));
        this.wakeWordDetectedHandler = listenHandler;
        this.cardHandler = cardHandler;
        this.notificationManager =
                new NotificationManager(notificationIndicator, new SimpleAudioPlayer());

        alertManager.loadFromDisk(listener);
        notificationManager.loadFromDisk(listener);
    }

    private void getMicrophone(AVSController controller) throws LineUnavailableException {
        controller.microphone = AudioCapture.getAudioHardware(AUDIO_TYPE.getAudioFormat(),
                new MicrophoneLineFactory());
    }

    private void initializeMicrophone() {

        if (this.wakeWordAgentEnabled) {
            AVSController controller = this;
            Callable<Void> task = new Callable<Void>() {
                @Override
                public Void call() throws Exception {
                    try {
                        wakeWordIPC.sendCommand(IPCCommand.IPC_PAUSE_WAKE_WORD_ENGINE);
                        getMicrophone(controller);
                    } catch (LineUnavailableException e) {
                        log.warn("Could not open microphone line");
                    }
                    wakeWordIPC.sendCommand(IPCCommand.IPC_RESUME_WAKE_WORD_ENGINE);
                    return null;
                }
            };

            try {
                LinearRetryPolicy retryPolicy = new LinearRetryPolicy(
                        WAKE_WORD_RELEASE_RETRY_DELAY_MS, WAKE_WORD_RELEASE_TRIES);
                retryPolicy.tryCall(task, Exception.class);
            } catch (Exception e) {
                log.error("There was a problem connecting to the wake word engine.", e);
            }
        }

        // if either the wake-word agent is not configured for this platform, or we were not
        // able to connect to it, let's get the microphone directly
        if (microphone == null) {
            try {
                getMicrophone(this);
            } catch (LineUnavailableException e) {
                log.warn("Could not open the microphone line.");
            }
        }
    }

    public void startHandlingDirectives() {
        dependentDirectiveThread.start();
        independentDirectiveThread.start();
    }

    public void sendSynchronizeStateEvent() throws InterruptedException {
        sendRequest(RequestFactory.createSystemSynchronizeStateEvent(player.getPlaybackState(),
                player.getSpeechState(), alertManager.getState(), player.getVolumeState(),
                notificationManager.getState()));
    }

    @Override
    public void onAccessTokenReceived(String accessToken) {
        avsClient.setAccessToken(accessToken);
    }

    @Override
    public void onAccessTokenRevoked() {
        avsClient.revokeAccessToken();
    }

    // start the recording process and send to server
    // takes an optional RMS callback and an optional request callback
    public void startRecording(RecordingRMSListener rmsListener, RequestListener requestListener) {

        if (this.wakeWordAgentEnabled) {

            acceptWakeWordEvents = false;

            try {
                wakeWordIPC.sendCommand(IPCCommand.IPC_PAUSE_WAKE_WORD_ENGINE);
            } catch (IOException e) {
                log.warn("Could not send the IPC_PAUSE_WAKE_WORD_ENGINE command");
            }
        }

        try {
            String dialogRequestId = dialogRequestIdAuthority.createNewDialogRequestId();

            RequestBody body = RequestFactory.createSpeechRecognizerRecognizeRequest(
                    dialogRequestId, PROFILE, FORMAT, player.getPlaybackState(),
                    player.getSpeechState(), alertManager.getState(), player.getVolumeState());

            dependentQueue.clear();
            InputStream inputStream;
            if (audioFileCapture != null) {
                inputStream = audioFileCapture.getAudioInputStream(this, rmsListener);
            } else {
                inputStream = getMicrophoneInputStream(this, rmsListener);
            }

            avsClient.sendEvent(body, inputStream, requestListener, AUDIO_TYPE);

            speechRequestAudioPlayerPauseController.startSpeechRequest();
        } catch (Exception e) {
            player.playMp3FromResource(ERROR_SOUND);
            requestListener.onRequestError(e);
        }
    }

    private InputStream getMicrophoneInputStream(AVSController controller,
            RecordingRMSListener rmsListener) throws LineUnavailableException, IOException {

        int numberRetries = 1;

        if (this.wakeWordAgentEnabled) {
            numberRetries = WAKE_WORD_RELEASE_TRIES;
        }

        for (; numberRetries > 0; numberRetries--) {
            try {
                return microphone.getAudioInputStream(controller, rmsListener);
            } catch (LineUnavailableException | IOException e) {
                if (numberRetries == 1) {
                    throw e;
                }
                log.warn("Could not open the microphone line.");
                try {
                    Thread.sleep(WAKE_WORD_RELEASE_RETRY_DELAY_MS);
                } catch (InterruptedException e1) {
                    log.error("exception:", e1);
                }
            }
        }

        throw new LineUnavailableException();
    }

    public void handlePlaybackAction(PlaybackAction action) {
        switch (action) {
            case PLAY:
                if (alertManager.hasActiveAlerts()) {
                    alertManager.stopActiveAlert();
                } else {
                    sendRequest(RequestFactory.createPlaybackControllerPlayEvent(
                            player.getPlaybackState(), player.getSpeechState(),
                            alertManager.getState(), player.getVolumeState()));
                }
                break;
            case PAUSE:
                if (alertManager.hasActiveAlerts()) {
                    alertManager.stopActiveAlert();
                } else {
                    sendRequest(RequestFactory.createPlaybackControllerPauseEvent(
                            player.getPlaybackState(), player.getSpeechState(),
                            alertManager.getState(), player.getVolumeState()));
                }
                break;
            case PREVIOUS:
                sendRequest(RequestFactory.createPlaybackControllerPreviousEvent(
                        player.getPlaybackState(), player.getSpeechState(), alertManager.getState(),
                        player.getVolumeState()));
                break;
            case NEXT:
                sendRequest(RequestFactory.createPlaybackControllerNextEvent(
                        player.getPlaybackState(), player.getSpeechState(), alertManager.getState(),
                        player.getVolumeState()));
                break;
            default:
                log.error("Failed to handle playback action");
        }
    }

    public void sendRequest(RequestBody body) {
        eventRunning = true;
        try {
            avsClient.sendEvent(body);
        } catch (Exception e) {
            log.error("Failed to send request", e);
        }
        eventRunning = false;
    }

    /**
     * Set this device account's locale to the given locale by sending a SettingsUpdated event to
     * AlexaService.
     *
     * @param locale
     */
    public void setLocale(Locale locale) {
        List<Setting> settings = new ArrayList<>();
        settings.add(new LocaleSetting(locale.toLanguageTag()));
        sendRequest(RequestFactory.createSettingsUpdatedEvent(settings));
    }

    public boolean eventRunning() {
        return eventRunning;
    }

    @Override
    public synchronized void dispatch(Directive directive) {
        String directiveNamespace = directive.getNamespace();

        String directiveName = directive.getName();
        log.info("Handling directive: {}.{}", directiveNamespace, directiveName);
        if (dialogRequestIdAuthority.isCurrentDialogRequestId(directive.getDialogRequestId())) {
            speechRequestAudioPlayerPauseController.dispatchDirective();
        }
        try {
            if (AVSAPIConstants.SpeechRecognizer.NAMESPACE.equals(directiveNamespace)) {
                handleSpeechRecognizerDirective(directive);
            } else if (AVSAPIConstants.SpeechSynthesizer.NAMESPACE.equals(directiveNamespace)) {
                handleSpeechSynthesizerDirective(directive);
            } else if (AVSAPIConstants.AudioPlayer.NAMESPACE.equals(directiveNamespace)) {
                handleAudioPlayerDirective(directive);
            } else if (AVSAPIConstants.Alerts.NAMESPACE.equals(directiveNamespace)) {
                handleAlertsDirective(directive);
            } else if (AVSAPIConstants.Notifications.NAMESPACE.equals(directiveNamespace)) {
                handleNotificationsDirective(directive);
            } else if (AVSAPIConstants.Speaker.NAMESPACE.equals(directiveNamespace)) {
                handleSpeakerDirective(directive);
            } else if (AVSAPIConstants.System.NAMESPACE.equals(directiveNamespace)) {
                handleSystemDirective(directive);
            } else if (AVSAPIConstants.TemplateRuntime.NAMESPACE.equals(directiveNamespace)) {
                handleTemplateRuntimeDirective(directive);
            } else {
                throw new DirectiveHandlingException(ExceptionType.UNSUPPORTED_OPERATION,
                        "No device side component to handle the directive.");
            }
        } catch (DirectiveHandlingException e) {
            sendExceptionEncounteredEvent(directive.getRawMessage(), e.getType(), e);
        } catch (Exception e) {
            sendExceptionEncounteredEvent(directive.getRawMessage(), ExceptionType.INTERNAL_ERROR,
                    e);
            throw e;
        }
    }

    private void sendExceptionEncounteredEvent(String directiveJson, ExceptionType type,
            Exception e) {
        sendRequest(RequestFactory.createSystemExceptionEncounteredEvent(directiveJson, type,
                e.getMessage(), player.getPlaybackState(), player.getSpeechState(),
                alertManager.getState(), player.getVolumeState()));
        log.error("{} error handling directive: {}", type, directiveJson, e);
    }

    private void handleAudioPlayerDirective(Directive directive) throws DirectiveHandlingException {
        String directiveName = directive.getName();
        if (AVSAPIConstants.AudioPlayer.Directives.Play.NAME.equals(directiveName)) {
            player.handlePlay((Play) directive.getPayload());
        } else if (AVSAPIConstants.AudioPlayer.Directives.Stop.NAME.equals(directiveName)) {
            player.handleStop();
        } else if (AVSAPIConstants.AudioPlayer.Directives.ClearQueue.NAME.equals(directiveName)) {
            player.handleClearQueue((ClearQueue) directive.getPayload());
        } else {
            throwUnsupportedOperationException(directive);
        }
    }

    private void handleSystemDirective(Directive directive) throws DirectiveHandlingException {
        String directiveName = directive.getName();
        if (AVSAPIConstants.System.Directives.ResetUserInactivity.NAME.equals(directiveName)) {
            onUserActivity();
        } else if (AVSAPIConstants.System.Directives.SetEndpoint.NAME.equals(directiveName)) {
            handleSetEndpoint((SetEndpoint) directive.getPayload());
        } else {
            throwUnsupportedOperationException(directive);
        }
    }

    private void handleSpeechSynthesizerDirective(Directive directive)
            throws DirectiveHandlingException {
        if (AVSAPIConstants.SpeechSynthesizer.Directives.Speak.NAME.equals(directive.getName())) {
            player.handleSpeak((Speak) directive.getPayload());
        } else {
            throw new DirectiveHandlingException(ExceptionType.UNSUPPORTED_OPERATION,
                    "The device's speech synthesizer component cannot handle this directive.");
        }
    }

    private void handleSpeechRecognizerDirective(Directive directive)
            throws DirectiveHandlingException {
        String directiveName = directive.getName();
        if (AVSAPIConstants.SpeechRecognizer.Directives.ExpectSpeech.NAME.equals(directiveName)) {
            // If your device cannot handle automatically starting to listen, you must
            // implement a listen timeout event, as described here:
            // https://developer.amazon.com/public/solutions/alexa/alexa-voice-service/rest/speechrecognizer-listentimeout-request
            notifyExpectSpeechDirective();
        } else if (AVSAPIConstants.SpeechRecognizer.Directives.StopCapture.NAME
                .equals(directiveName)) {
            stopCaptureHandler.onStopCaptureDirective();
        } else {
            throwUnsupportedOperationException(directive);
        }
    }

    private void handleAlertsDirective(Directive directive) throws DirectiveHandlingException {
        String directiveName = directive.getName();
        if (AVSAPIConstants.Alerts.Directives.SetAlert.NAME.equals(directiveName)) {
            SetAlert payload = (SetAlert) directive.getPayload();
            String alertToken = payload.getToken();
            ZonedDateTime scheduledTime = payload.getScheduledTime();
            AlertType type = payload.getType();

            if (alertManager.hasAlert(alertToken)) {
                AlertScheduler scheduler = alertManager.getScheduler(alertToken);
                if (scheduler.getAlert().getScheduledTime().equals(scheduledTime)) {
                    return;
                } else {
                    scheduler.cancel();
                }
            }

            Alert alert = new Alert(alertToken, type, scheduledTime);
            alertManager.add(alert);
        } else if (AVSAPIConstants.Alerts.Directives.DeleteAlert.NAME.equals(directiveName)) {
            DeleteAlert payload = (DeleteAlert) directive.getPayload();
            alertManager.delete(payload.getToken());
        } else {
            throwUnsupportedOperationException(directive);
        }
    }

    private void handleNotificationsDirective(Directive directive)
            throws DirectiveHandlingException {
        String directiveName = directive.getName();
        if (AVSAPIConstants.Notifications.Directives.SetIndicator.NAME.equals(directiveName)) {
            SetIndicator payload = (SetIndicator) directive.getPayload();
            notificationManager.handleSetIndicator(payload);
        } else if (AVSAPIConstants.Notifications.Directives.ClearIndicator.NAME
                .equals(directiveName)) {
            notificationManager.handleClearIndicator();
        } else {
            throwUnsupportedOperationException(directive);
        }
    }

    private void handleSpeakerDirective(Directive directive) throws DirectiveHandlingException {
        String directiveName = directive.getName();
        if (AVSAPIConstants.Speaker.Directives.SetVolume.NAME.equals(directiveName)) {
            player.handleSetVolume((VolumePayload) directive.getPayload());
        } else if (AVSAPIConstants.Speaker.Directives.AdjustVolume.NAME.equals(directiveName)) {
            player.handleAdjustVolume((VolumePayload) directive.getPayload());
        } else if (AVSAPIConstants.Speaker.Directives.SetMute.NAME.equals(directiveName)) {
            player.handleSetMute((SetMute) directive.getPayload());
        } else {
            throwUnsupportedOperationException(directive);
        }
    }

    private void handleTemplateRuntimeDirective(Directive directive)
            throws DirectiveHandlingException {
        String directiveName = directive.getName();
        if (cardHandler == null) {
            throwUnsupportedOperationException(directive);
        }
        if (AVSAPIConstants.TemplateRuntime.Directives.RenderTemplate.NAME.equals(directiveName)) {
            cardHandler.renderCard((RenderTemplate) directive.getPayload(),
                    directive.getRawMessage());
        } else if (AVSAPIConstants.TemplateRuntime.Directives.RenderPlayerInfo.NAME
                .equals(directiveName)) {
            cardHandler.renderPlayerInfo(directive.getRawMessage());
        } else {
            throwUnsupportedOperationException(directive);
        }
    }

    private void throwUnsupportedOperationException(Directive directive)
            throws DirectiveHandlingException {
        throw new DirectiveHandlingException(ExceptionType.UNSUPPORTED_OPERATION,
                String.format("The device's %s component cannot handle the %s directive",
                        directive.getNamespace(), directive.getName()));
    }

    private void handleSetEndpoint(SetEndpoint setEndpoint) throws DirectiveHandlingException {
        try {
            URL endpoint = new URL(setEndpoint.getEndpoint());
            if (endpoint.equals(avsClient.getHost())) {
                return;
            }
            config.setAvsHost(endpoint);
            config.saveConfig();

            avsClient.closeDownchannel();
            avsClient = avsClientFactory.getAVSClient(directiveEnqueuer, this, listener);
        } catch (MalformedURLException e) {
            log.error("The SetEndpoint payload had a malformed URL");
            throw new DirectiveHandlingException(ExceptionType.UNEXPECTED_INFORMATION_RECEIVED,
                    "Received SetEndpoint directive with malformed url");
        } catch (Exception e) {
            log.error("Failed to set a new avs client.");
            throw new DirectiveHandlingException(ExceptionType.INTERNAL_ERROR,
                    "Error while creating avsClient");
        }
    }

    private void notifyExpectSpeechDirective() {
        for (ExpectSpeechListener listener : expectSpeechListeners) {
            listener.onExpectSpeechDirective();
        }
    }

    public void stopRecording() {
        speechRequestAudioPlayerPauseController.finishedListening();
        microphone.stopCapture();

        if (this.wakeWordAgentEnabled) {
            try {
                wakeWordIPC.sendCommand(IPCCommand.IPC_RESUME_WAKE_WORD_ENGINE);
            } catch (IOException e) {
                log.warn("could not send resume wake word engine command", e);
            }
            acceptWakeWordEvents = true;
        }
    }

    // audio state callback for when recording has started
    @Override
    public void recordingStarted() {
        player.playMp3FromResource(START_SOUND);
    }

    // audio state callback for when recording has completed
    @Override
    public void recordingCompleted() {
        player.playMp3FromResource(END_SOUND);
    }

    public boolean isSpeaking() {
        return player.isSpeaking();
    }

    public boolean isPlaying() {
        return player.isPlayingOrPaused();
    }

    @Override
    public void onAlertStarted(String alertToken) {
        sendRequest(RequestFactory.createAlertsAlertStartedEvent(alertToken));

        if (player.isSpeaking()) {
            sendRequest(RequestFactory.createAlertsAlertEnteredBackgroundEvent(alertToken));
        } else {
            sendRequest(RequestFactory.createAlertsAlertEnteredForegroundEvent(alertToken));
        }
    }

    @Override
    public void onAlertStopped(String alertToken) {
        sendRequest(RequestFactory.createAlertsAlertStoppedEvent(alertToken));
    }

    @Override
    public void onAlertSet(String alertToken, boolean success) {
        sendRequest(RequestFactory.createAlertsSetAlertEvent(alertToken, success));
    }

    @Override
    public void onAlertDelete(String alertToken, boolean success) {
        sendRequest(RequestFactory.createAlertsDeleteAlertEvent(alertToken, success));
    }

    @Override
    public void startAlert(String alertToken) {
        player.startAlert();
    }

    @Override
    public void stopAlert(String alertToken) {
        if (!alertManager.hasActiveAlerts()) {
            player.stopAlert();
        }
    }

    public void processingFinished() {
        log.debug("Speech processing finished. Dependent queue size: {}", dependentQueue.size());
        speechRequestAudioPlayerPauseController
                .speechRequestProcessingFinished(dependentQueue.size());
    }

    @Override
    public void onAlexaSpeechStarted() {
        dependentDirectiveThread.block();

        if (alertManager.hasActiveAlerts()) {
            for (String alertToken : alertManager.getActiveAlerts()) {
                sendRequest(RequestFactory.createAlertsAlertEnteredBackgroundEvent(alertToken));
            }
        }
    }

    @Override
    public void onAlexaSpeechFinished() {
        dependentDirectiveThread.unblock();

        if (alertManager.hasActiveAlerts()) {
            for (String alertToken : alertManager.getActiveAlerts()) {
                sendRequest(RequestFactory.createAlertsAlertEnteredForegroundEvent(alertToken));
            }
        }
    }

    @Override
    public void onParsingFailed(String unparseable) {
        String message = "Failed to parse message from AVS";
        sendRequest(RequestFactory.createSystemExceptionEncounteredEvent(unparseable,
                ExceptionType.UNEXPECTED_INFORMATION_RECEIVED, message, player.getPlaybackState(),
                player.getSpeechState(), alertManager.getState(), player.getVolumeState()));
    }

    @Override
    public void onUserActivity() {
        lastUserInteractionTimestampSeconds
                .set(System.currentTimeMillis() / MILLISECONDS_PER_SECOND);
    }

    private class UserInactivityReport implements Runnable {

        @Override
        public void run() {
            sendRequest(RequestFactory.createSystemUserInactivityReportEvent(
                    (System.currentTimeMillis() / MILLISECONDS_PER_SECOND)
                            - lastUserInteractionTimestampSeconds.get()));
        }
    }

    @Override
    public synchronized void onWakeWordDetected() {
        if (acceptWakeWordEvents) {
            wakeWordDetectedHandler.onWakeWordDetected();
        }
    }

    public void setAudioFileCapture(AudioCapture audioFileCapture) {
        this.audioFileCapture = audioFileCapture;
    }
}
