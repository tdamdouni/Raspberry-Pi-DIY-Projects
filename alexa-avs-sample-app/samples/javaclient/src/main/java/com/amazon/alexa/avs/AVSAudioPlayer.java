/** 
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Amazon Software License (the "License"). You may not use this file 
 * except in compliance with the License. A copy of the License is located at
 *
 *   http://aws.amazon.com/asl/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, 
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the 
 * specific language governing permissions and limitations under the License.
 */
package com.amazon.alexa.avs;

import com.amazon.alexa.avs.AudioPlayerStateMachine.AudioPlayerState;
import com.amazon.alexa.avs.exception.DirectiveHandlingException;
import com.amazon.alexa.avs.exception.DirectiveHandlingException.ExceptionType;
import com.amazon.alexa.avs.message.request.RequestFactory;
import com.amazon.alexa.avs.message.request.context.PlaybackStatePayload;
import com.amazon.alexa.avs.message.request.context.SpeechStatePayload;
import com.amazon.alexa.avs.message.request.context.VolumeStatePayload;
import com.amazon.alexa.avs.message.response.audioplayer.AudioItem;
import com.amazon.alexa.avs.message.response.audioplayer.ClearQueue;
import com.amazon.alexa.avs.message.response.audioplayer.Play;
import com.amazon.alexa.avs.message.response.audioplayer.Stream;
import com.amazon.alexa.avs.message.response.speaker.SetMute;
import com.amazon.alexa.avs.message.response.speaker.VolumePayload;
import com.amazon.alexa.avs.message.response.speechsynthesizer.Speak;

import org.apache.commons.io.IOUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.UUID;

import javazoom.jl.player.Player;
import uk.co.caprica.vlcj.component.AudioMediaPlayerComponent;
import uk.co.caprica.vlcj.player.MediaPlayer;
import uk.co.caprica.vlcj.player.MediaPlayerEventAdapter;

public class AVSAudioPlayer {

    private static final Logger log = LoggerFactory.getLogger(AVSAudioPlayer.class);

    // callback to send audio events
    private final AVSController controller;
    // vlc instance to play media
    private AudioMediaPlayerComponent audioPlayer;
    // queue of listen directive media
    private final Queue<Stream> playQueue;
    // queue of speak directive media
    private final Queue<SpeakItem> speakQueue;
    // Cache of URLs associated with the current AVSPlayItem/stream
    private Set<String> streamUrls;
    // Urls associated with the current stream that we've already tried to play
    private Set<String> attemptedUrls;
    // Map of VLC-centric urls to file urls - we use this map to delete local files after playing
    private Map<String, String> cachedAudioFiles;
    // Alarm thread
    private Thread alarmThread;
    // Speaker thread
    private Thread playThread;
    // Object on which to lock
    private Object playLock = new Object();
    // How long the thread should block on waiting for audio to finish playing
    private static final int TIMEOUT_IN_MS = 3000;

    // VLCJ volumes are between 0-200. Alexa volumes are from 0-100. These constants are used to
    // convert and limit volume values.
    private static final long VLCJ_VOLUME_SCALAR = 2;
    private static final int VLCJ_MIN_VOLUME = 0;
    private static final int VLCJ_DEFAULT_VOLUME = 100;
    private static final int VLCJ_MAX_VOLUME = 200;

    // VLC's elapsed time doesn't work correctly. So we're using System.nanoTime() to get accurate
    // timestamps
    private AudioPlayerTimer timer;
    // track the last progressReport sent time
    private boolean waitForPlaybackFinished;
    // used for speak directives and earcons
    private Player speaker = null;
    private final ClassLoader resLoader; // used to load resource files

    private String latestStreamToken = "";

    private String latestToken = "";

    /*
     * The AudioPlayerStateMachine is used to keep track of local audio playback state changes,
     * ensuring the PlaybackEvents are sent at the right time, in the correct order, and only once.
     */
    private final AudioPlayerStateMachine audioPlayerStateMachine;

    private int currentVolume;

    private long playbackStutterStartedOffsetInMilliseconds;

    private final Set<AlexaSpeechListener> listeners;

    private final AudioPlayerProgressReporter progressReporter;

    private enum SpeechState {
        PLAYING,
        FINISHED;
    }

    private enum AlertState {
        PLAYING,
        INTERRUPTED,
        FINISHED;
    }

    private volatile AlertState alertState = AlertState.FINISHED;

    private volatile SpeechState speechState = SpeechState.FINISHED;

    private boolean isInterrupted = false;

    private boolean currentlyMuted;

    public AVSAudioPlayer(AVSController controller) {
        this.controller = controller;
        resLoader = Thread.currentThread().getContextClassLoader();
        timer = new AudioPlayerTimer();
        waitForPlaybackFinished = false;
        playQueue = new LinkedList<Stream>();
        speakQueue = new LinkedList<SpeakItem>();
        streamUrls = new HashSet<String>();
        attemptedUrls = new HashSet<String>();
        cachedAudioFiles = new HashMap<String, String>();
        setupAudioPlayer();

        currentVolume = audioPlayer.getMediaPlayer().getVolume();
        if (currentVolume == VLCJ_MIN_VOLUME) {
            currentVolume = VLCJ_DEFAULT_VOLUME;
        }
        currentlyMuted = audioPlayer.getMediaPlayer().isMute();

        audioPlayerStateMachine = new AudioPlayerStateMachine(this, controller);

        progressReporter = new AudioPlayerProgressReporter(
                new ProgressReportDelayEventRunnable(audioPlayerStateMachine),
                new ProgressReportIntervalEventRunnable(audioPlayerStateMachine), timer);

        listeners = new HashSet<>();
    }

    public void registerAlexaSpeechListener(AlexaSpeechListener listener) {
        listeners.add(listener);
    }

    public void handleSpeak(Speak speak) {
        SpeakItem speakItem = new SpeakItem(speak.getToken(), speak.getAttachedContent());

        speakQueue.add(speakItem);
        // if not already speaking, start speech
        if (speakQueue.size() == 1) {
            startSpeech();
        }
    }

    public void handlePlay(Play play) throws DirectiveHandlingException {
        AudioItem item = play.getAudioItem();
        if (play.getPlayBehavior() == Play.PlayBehavior.REPLACE_ALL) {
            clearAll();
            // if already playing, transition to stopped and send PlaybackStopped event
            audioPlayerStateMachine.playReplaceAll();
        } else if (play.getPlayBehavior() == Play.PlayBehavior.REPLACE_ENQUEUED) {
            clearEnqueued();
        }

        Stream stream = item.getStream();
        String streamUrl = stream.getUrl();
        String streamId = stream.getToken();
        long offset = stream.getOffsetInMilliseconds();
        log.info("URL: {}", streamUrl);
        log.info("StreamId: {}", streamId);
        log.info("Offset: {}", offset);

        if (stream.hasAttachedContent()) {
            try {
                File tmp = File.createTempFile(UUID.randomUUID().toString(), ".mp3");
                tmp.deleteOnExit();
                Files.copy(stream.getAttachedContent(), tmp.toPath(),
                        StandardCopyOption.REPLACE_EXISTING);

                stream.setUrl(tmp.getAbsolutePath());
                add(stream);
            } catch (IOException e) {
                log.error("Error while saving audio to a file", e);
                throw new DirectiveHandlingException(ExceptionType.INTERNAL_ERROR,
                        "Error saving attached content to disk, unable to handle Play directive.");
            }
        } else {
            add(stream);
        }
    }

    public void handleStop() {
        synchronized (audioPlayer.getMediaPlayer()) {
            stop();
            audioPlayerStateMachine.playbackStopped();
        }
    }

    public void handleClearQueue(ClearQueue clearQueue) {
        if (clearQueue.getClearBehavior() == ClearQueue.ClearBehavior.CLEAR_ALL) {
            clearAll();
            audioPlayerStateMachine.clearQueueAll();
        } else {
            clearEnqueued();
            audioPlayerStateMachine.clearQueueEnqueued();
        }
    }

    public void handleSetVolume(VolumePayload volumePayload) {
        currentVolume = (int) (volumePayload.getVolume() * VLCJ_VOLUME_SCALAR);
        audioPlayer.getMediaPlayer().setVolume(currentVolume);
        controller.sendRequest(
                RequestFactory.createSpeakerVolumeChangedEvent(getVolume(), isMuted()));
    }

    public void handleAdjustVolume(VolumePayload volumePayload) {
        int adjustVolumeBy = (int) (volumePayload.getVolume() * VLCJ_VOLUME_SCALAR);
        currentVolume = Math.min(VLCJ_MAX_VOLUME,
                Math.max(VLCJ_MIN_VOLUME, currentVolume + adjustVolumeBy));
        audioPlayer.getMediaPlayer().setVolume(currentVolume);
        controller.sendRequest(
                RequestFactory.createSpeakerVolumeChangedEvent(getVolume(), isMuted()));
    }

    public void handleSetMute(SetMute setMutePayload) {
        currentlyMuted = setMutePayload.getMute();
        audioPlayer.getMediaPlayer().mute(currentlyMuted);
        controller
                .sendRequest(RequestFactory.createSpeakerMuteChangedEvent(getVolume(), isMuted()));
    }

    private void setupAudioPlayer() {
        audioPlayer = new AudioMediaPlayerComponent();

        audioPlayer.getMediaPlayer().addMediaPlayerEventListener(new MediaPlayerEventAdapter() {

            private boolean playbackStartedSuccessfully;

            private boolean bufferUnderrunInProgress;

            private boolean isPaused;

            @Override
            public void newMedia(MediaPlayer mediaPlayer) {
                log.debug("newMedia: {}", mediaPlayer.mrl());
                playbackStartedSuccessfully = false;
                bufferUnderrunInProgress = false;
            }

            @Override
            public void stopped(MediaPlayer mediaPlayer) {
                log.debug("stopped: {}", mediaPlayer.mrl());
            }

            @Override
            public void playing(MediaPlayer mediaPlayer) {
                log.debug("playing: {}", mediaPlayer.mrl());
                long length = audioPlayer.getMediaPlayer().getLength();
                log.debug("    length: {}", length);

                if (isPaused && playbackStartedSuccessfully) {
                    audioPlayerStateMachine.playbackResumed();
                    isPaused = false;
                }

                startTimerAndProgressReporter();
            }

            @Override
            public void buffering(MediaPlayer mediaPlayer, float newCache) {
                Stream stream = playQueue.peek();
                if (stream == null) {
                    return;
                }
                if (playbackStartedSuccessfully && !bufferUnderrunInProgress) {
                    // We started buffering mid playback
                    bufferUnderrunInProgress = true;
                    long startOffset = 0;
                    startOffset = stream.getOffsetInMilliseconds();
                    playbackStutterStartedOffsetInMilliseconds =
                            Math.max(startOffset, getCurrentOffsetInMilliseconds());
                    stopTimerAndProgressReporter();
                    audioPlayerStateMachine.playbackStutterStarted();
                }

                if (bufferUnderrunInProgress && newCache >= 100.0f) {
                    // We are fully buffered after a buffer underrun event
                    bufferUnderrunInProgress = false;
                    audioPlayerStateMachine.playbackStutterFinished();
                    startTimerAndProgressReporter();
                }

                if (!playbackStartedSuccessfully && newCache >= 100.0f) {
                    // We have successfully buffered the first time and started playback
                    playbackStartedSuccessfully = true;

                    long offset = stream.getOffsetInMilliseconds();

                    timer.reset(offset, audioPlayer.getMediaPlayer().getLength());
                    progressReporter.disable();
                    if (stream.getProgressReportRequired()) {
                        progressReporter.setup(stream.getProgressReport());
                    }

                    audioPlayerStateMachine.playbackStarted();
                    startTimerAndProgressReporter();

                    if (isInterrupted) {
                        interruptContent();
                    }

                    if (isPaused) {
                        audioPlayerStateMachine.playbackPaused();
                    }
                }
            }

            @Override
            public void paused(MediaPlayer mediaPlayer) {
                log.debug("paused: {}", mediaPlayer.mrl());
                stopTimerAndProgressReporter();
                if (playbackStartedSuccessfully) {
                    audioPlayerStateMachine.playbackPaused();
                }
                isPaused = true;
            }

            @Override
            public void finished(MediaPlayer mediaPlayer) {
                log.info("Finished playing {}", mediaPlayer.mrl());
                List<String> items = mediaPlayer.subItems();
                // Remember the url we just tried
                attemptedUrls.add(mediaPlayer.mrl());

                if (cachedAudioFiles.containsKey(mediaPlayer.mrl())) {
                    String key = mediaPlayer.mrl();
                    String cachedUrl = cachedAudioFiles.get(key);
                    deleteCachedFile(cachedUrl);
                    cachedAudioFiles.remove(key);
                }

                if ((items.size() > 0) || (streamUrls.size() > 0)) {
                    // Add to the set of URLs to attempt playback
                    streamUrls.addAll(items);

                    // Play any url associated with this play item that
                    // we haven't already tried
                    for (String mrl : streamUrls) {
                        if (!attemptedUrls.contains(mrl)) {
                            log.info("Playing {}", mrl);
                            mediaPlayer.playMedia(mrl);
                            return;
                        }
                    }
                }

                // wait for any pending events to finish(playbackStarted/progressReport)
                while (controller.eventRunning()) {
                    try {
                        Thread.sleep(100);
                    } catch (Exception e) {
                    }
                }

                // remove the item from the queue since it has finished playing
                playQueue.poll();

                stopTimerAndProgressReporter();
                audioPlayerStateMachine.playbackNearlyFinished();
                audioPlayerStateMachine.playbackFinished();

                // unblock playback now that playbackFinished has been sent
                waitForPlaybackFinished = false;
                if (!playQueue.isEmpty()) {
                    // start playback if it wasn't the last item
                    startPlayback();
                }
            }

            @Override
            public void error(MediaPlayer mediaPlayer) {
                log.error("Error playing: {}", mediaPlayer.mrl());

                attemptedUrls.add(mediaPlayer.mrl());
                // If there are any urls left to try, don't throw an error
                for (String mrl : streamUrls) {
                    if (!attemptedUrls.contains(mrl)) {
                        mediaPlayer.playMedia(mrl);
                        return;
                    }
                }

                // wait for any pending events to finish(playbackStarted/progressReport)
                while (controller.eventRunning()) {
                    try {
                        Thread.sleep(100);
                    } catch (Exception e) {
                    }
                }
                playQueue.clear();
                stopTimerAndProgressReporter();
                audioPlayerStateMachine.playbackFailed();
            }
        });
    }

    /**
     * Returns true if Alexa is currently speaking
     */
    public boolean isSpeaking() {
        return speechState == SpeechState.PLAYING;
    }

    /**
     * Returns true if Alexa is currently playing media
     */
    public boolean isPlayingOrPaused() {
        return isPlaying() || audioPlayerStateMachine.getState() == AudioPlayerState.PAUSED;
    }

    private boolean isPlaying() {
        return (audioPlayerStateMachine.getState() == AudioPlayerState.PLAYING
                || audioPlayerStateMachine.getState() == AudioPlayerState.BUFFER_UNDERRUN);
    }

    /**
     * Returns true if Alexa is currently playing an alarm sound
     */
    public boolean isAlarming() {
        return alertState == AlertState.PLAYING;
    }

    /**
     * Interrupt all audio - Alarms, speech, and media
     */
    public void interruptAllAlexaOutput() {
        log.debug("Interrupting all Alexa output");
        if (isSpeaking()) {
            // Then we are interrupting some speech
            interruptCurrentlyPlaying();
        }
        speakQueue.clear();

        interruptAlertsAndContent();
    }

    /**
     * Interrupt only alerts and content
     */
    private void interruptAlertsAndContent() {
        if (isAlarming()) {
            alertState = AlertState.INTERRUPTED;
        }

        interruptContent();
    }

    /**
     * Interrupt only content
     */
    private void interruptContent() {
        isInterrupted = true;

        synchronized (audioPlayer.getMediaPlayer()) {
            if (!playQueue.isEmpty() && isPlaying() && audioPlayer.getMediaPlayer().isPlaying()) {
                log.debug("AudioPlayer content interrupted");
                audioPlayer.getMediaPlayer().pause();
            }
        }
    }

    /**
     * Resume all audio from interrupted state. Since the speech queue is cleared when interrupted,
     * resuming speech is not necessary
     */
    public void resumeAllAlexaOutput() {
        log.debug("Resuming all Alexa output");
        if (speakQueue.isEmpty() && !resumeAlerts()) {
            resumeContent();
        }
    }

    /**
     * Resume alert audio
     */
    private boolean resumeAlerts() {
        if (alertState == AlertState.INTERRUPTED) {
            startAlert();
            return true;
        }
        return false;
    }

    /**
     * Resume any content
     */
    private void resumeContent() {
        isInterrupted = false;

        synchronized (audioPlayer.getMediaPlayer()) {
            if (!playQueue.isEmpty() && isPlayingOrPaused()
                    && !audioPlayer.getMediaPlayer().isPlaying()) {
                // Pause toggles the pause state of the media player, if it was previously paused it
                // will be resumed.
                log.debug("AudioPlayer content resumed");
                audioPlayer.getMediaPlayer().pause();
            }
        }
    }

    /**
     * Add audio to be played by the media player. This is triggered by the play directive
     *
     * @param stream
     *            Stream to add to the play queue
     */
    private void add(Stream stream) {
        String expectedPreviousToken = stream.getExpectedPreviousToken();

        boolean startPlaying = playQueue.isEmpty();

        if (expectedPreviousToken == null || latestStreamToken.isEmpty()
                || latestStreamToken.equals(expectedPreviousToken)) {
            playQueue.add(stream);
        }

        if (startPlaying) {
            startPlayback();
        }
    }

    /**
     * Play media in the play queue
     */
    private void startPlayback() {
        if (playQueue.isEmpty()) {
            return;
        }

        Thread thread = new Thread() {

            @Override
            public void run() {
                // wait for any speech to complete before starting playback
                // also wait for playbackFinished to be called after getNextItem
                while (!speakQueue.isEmpty() || waitForPlaybackFinished) {
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        log.error("Interupted while waiting to start playback", e);
                    }
                }

                Stream stream = playQueue.peek();

                if (stream == null) {
                    // if a stop/clearQueue came down before we started
                    return;
                }

                latestStreamToken = stream.getToken();

                if (!playItem(stream)) {
                    // an error will be reported from the vlcj listener
                    return;
                }

                if (isSpeaking() || isAlarming()) {
                    // pause if Alexa is speaking or there is an active alert.
                    interruptContent();
                }
            }
        };
        thread.start();
    }

    /**
     * Play the media from the given url, at the given offset
     *
     * @param stream
     *            The Stream object we will be playing
     * @return true if played successfully, false otherwise
     */
    private boolean playItem(Stream stream) {
        synchronized (audioPlayer.getMediaPlayer()) {

            // Reset url caches and state information
            streamUrls = new HashSet<String>();
            attemptedUrls = new HashSet<String>();

            // Resetting the audio player is necessary to prevent hanging behavior
            // when listening to some long-running music tracks
            setupAudioPlayer();

            String url = stream.getUrl();
            long offset = stream.getOffsetInMilliseconds();

            log.debug("playing {}", url);

            timer.reset(); // Clear the old values

            if (audioPlayer.getMediaPlayer().startMedia(url)) {
                audioPlayer.getMediaPlayer().setVolume(currentVolume);
                audioPlayer.getMediaPlayer().mute(currentlyMuted);
                if (offset > 0) {
                    audioPlayer.getMediaPlayer().setTime(offset);
                }

                if (stream.hasAttachedContent()) {
                    cachedAudioFiles.put(audioPlayer.getMediaPlayer().mrl(), url);
                }

                return true;
            }
            return false;
        }
    }

    /**
     * Stop all media playback
     */
    public void stop() {
        synchronized (audioPlayer.getMediaPlayer()) {
            if (!playQueue.isEmpty() && isPlayingOrPaused()) {

                // Stop keeping track of the offset and sending reporting events
                stopTimerAndProgressReporter();

                audioPlayer.getMediaPlayer().stop();
            }
        }
    }

    /**
     * Play items from the speech play queue
     */
    private void startSpeech() {

        final SpeakItem speak = speakQueue.peek();

        // This addresses the possibility of the queue being cleared
        // between the time of this function call and this line of code.
        if (speak == null) {
            return;
        }

        notifyAlexaSpeechStarted();

        speechState = SpeechState.PLAYING;
        latestToken = speak.getToken();

        controller
                .sendRequest(RequestFactory.createSpeechSynthesizerSpeechStartedEvent(latestToken));

        Thread thread = new Thread() {
            @Override
            public void run() {
                synchronized (playLock) {
                    try {
                        InputStream inpStream = speak.getAudio();
                        interruptAlertsAndContent();
                        play(inpStream);
                        while (inpStream.available() > 0) {
                            playLock.wait(TIMEOUT_IN_MS);
                        }
                    } catch (InterruptedException | IOException e) {
                    }

                    finishedSpeechItem();
                }
            }
        };
        thread.start();
    }

    /**
     * When a speech item is finished, perform the necessary actions
     */
    private void finishedSpeechItem() {
        // remove the finished item
        speakQueue.poll();

        if (speakQueue.isEmpty()) {
            speechState = SpeechState.FINISHED;
            controller.sendRequest(
                    RequestFactory.createSpeechSynthesizerSpeechFinishedEvent(latestToken));

            notifyAlexaSpeechFinished();
        } else {
            // if not done start the next speech
            startSpeech();
        }
    }

    /**
     * Clear the queue of items to play, but keep the most recent item.
     */
    public void clearEnqueued() {
        // save the top item
        Stream top = playQueue.poll();
        // clear the queue and re-add the top item
        playQueue.clear();
        if (top != null) {
            playQueue.add(top);
        }
    }

    /**
     * Clear all media scheduled to play, including items currently playing
     */
    public void clearAll() {
        // stop playback and clear all
        stop();
        playQueue.clear();
    }

    /**
     * Get the position of the currently playing media item
     *
     * @return The position in milliseconds of the stream
     */
    private long getProgress() {
        synchronized (audioPlayer.getMediaPlayer()) {
            return timer.getOffsetInMilliseconds();
        }
    }

    /**
     * Start/resume the AudioPlayer Timer and ProgressReporter
     */
    private void startTimerAndProgressReporter() {
        timer.start();
        if (progressReporter.isSetup()) {
            progressReporter.start();
        }
    }

    /**
     * Stop/pause the AudioPlayer Timer and ProgressReporter
     */
    private void stopTimerAndProgressReporter() {
        timer.stop();
        progressReporter.stop();
    }

    /**
     * Get the playback state of the media player
     */
    public PlaybackStatePayload getPlaybackState() {
        AudioPlayerState playerState = audioPlayerStateMachine.getState();

        long offset = getCurrentOffsetInMilliseconds();

        return new PlaybackStatePayload(latestStreamToken, offset, playerState.toString());
    }

    public String getCurrentStreamToken() {
        return latestStreamToken;
    }

    public long getPlaybackStutterStartedOffsetInMilliseconds() {
        return playbackStutterStartedOffsetInMilliseconds;
    }

    public long getCurrentOffsetInMilliseconds() {
        AudioPlayerState playerActivity = audioPlayerStateMachine.getState();

        long offset;
        switch (playerActivity) {
            case PLAYING:
            case PAUSED:
            case BUFFER_UNDERRUN:
            case STOPPED:
            case FINISHED:
                offset = getProgress();
                break;
            case IDLE:
            default:
                offset = 0;
        }

        return offset;
    }

    /**
     * Get the speech state
     */
    public SpeechStatePayload getSpeechState() {
        String contentId = latestToken;
        return new SpeechStatePayload(contentId, getPlayerPosition(), speechState.name());
    }

    public VolumeStatePayload getVolumeState() {
        return new VolumeStatePayload(getVolume(), isMuted());
    }

    public long getVolume() {
        return currentVolume / VLCJ_VOLUME_SCALAR;
    }

    public boolean isMuted() {
        return currentlyMuted;
    }

    /**
     * Returns the offset in milliseconds of the default audio player. If there is no player
     * position, this function defaults to 0
     *
     * @return Player offset in milliseconds
     */
    private synchronized long getPlayerPosition() {
        long offsetInMilliseconds = 0;
        if (speaker != null) {
            offsetInMilliseconds = speaker.getPosition();
        }
        return offsetInMilliseconds;
    }

    /**
     * plays MP3 data from a resource asynchronously. will stop any previous playback and start the
     * new audio
     */
    public synchronized void playMp3FromResource(String resource) {
        final InputStream inpStream = resLoader.getResourceAsStream(resource);
        play(inpStream);
    }

    /**
     * Play the alarm sound
     */
    public void startAlert() {
        if (!isAlarming()) {
            interruptContent();
            if (isSpeaking()) {
                // alerts are in the background when Alexa is speaking
                alertState = AlertState.INTERRUPTED;
            } else {
                alertState = AlertState.PLAYING;

                alarmThread = new Thread() {
                    @Override
                    public void run() {
                        while (isAlarming() && !isSpeaking()) {
                            if (Thread.interrupted()) {
                                break;
                            }
                            InputStream inpStream = resLoader.getResourceAsStream("res/alarm.mp3");
                            synchronized (playLock) {
                                try {
                                    play(inpStream);
                                    while (inpStream.available() > 0) {
                                        playLock.wait(TIMEOUT_IN_MS);
                                    }
                                } catch (InterruptedException | IOException e) {
                                }
                            }
                        }
                    }
                };
                alarmThread.start();
            }
        }
    }

    /**
     * Stop the alarm
     */
    public void stopAlert() {
        interruptCurrentlyPlaying();
        alertState = AlertState.FINISHED;
    }

    /**
     * Interrupt whatever audio is currently playing through the default audio player
     */
    private synchronized void interruptCurrentlyPlaying() {
        if (playThread != null) {
            playThread.interrupt();
        }
        stopPlayer();
    }

    /**
     * Ends playback of the default audio player
     */
    private synchronized void stopPlayer() {
        if (speaker != null) {
            speaker.close();
            speaker = null;
            if (isSpeaking()) {
                speechState = SpeechState.FINISHED;
                notifyAlexaSpeechFinished();
            }
        }
    }

    /**
     * Play a generic input stream through the default audio player without blocking
     */
    private synchronized void play(final InputStream inpStream) {
        play(inpStream, false);
    }

    /**
     * Play a generic input stream through the default audio player
     */
    private synchronized void play(final InputStream inpStream, boolean block) {
        playThread = new Thread() {
            @Override
            public void run() {
                synchronized (playLock) {
                    try {
                        speaker = new Player(inpStream);
                        speaker.play();
                    } catch (Exception e) {
                        log.error("An error occurred while trying to play audio", e);
                    } finally {
                        IOUtils.closeQuietly(inpStream);
                    }
                    playLock.notifyAll();
                }
            }
        };
        playThread.start();
    }

    private void notifyAlexaSpeechStarted() {
        for (AlexaSpeechListener listener : listeners) {
            listener.onAlexaSpeechStarted();
        }
    }

    private void notifyAlexaSpeechFinished() {
        for (AlexaSpeechListener listener : listeners) {
            listener.onAlexaSpeechFinished();
        }
    }

    private static class ProgressReportDelayEventRunnable implements Runnable {

        private final AudioPlayerStateMachine playbackStateMachine;

        public ProgressReportDelayEventRunnable(AudioPlayerStateMachine playbackStateMachine) {
            this.playbackStateMachine = playbackStateMachine;
        }

        @Override
        public void run() {
            playbackStateMachine.reportProgressDelay();
        }
    };

    private static class ProgressReportIntervalEventRunnable implements Runnable {

        private final AudioPlayerStateMachine playbackStateMachine;

        public ProgressReportIntervalEventRunnable(AudioPlayerStateMachine playbackStateMachine) {
            this.playbackStateMachine = playbackStateMachine;
        }

        @Override
        public void run() {
            playbackStateMachine.reportProgressInterval();
        }
    }

    public interface AlexaSpeechListener {
        void onAlexaSpeechStarted();

        void onAlexaSpeechFinished();
    }

    private void deleteCachedFile(final String uri) {
        File file = new File(uri);
        file.delete();
    }
}
