package com.amazon.alexa.avs.ui.headless;

import java.util.Locale;
import java.util.Scanner;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.LinkedBlockingQueue;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.PlaybackAction;
import com.amazon.alexa.avs.auth.AccessTokenListener;
import com.amazon.alexa.avs.auth.AuthSetup;
import com.amazon.alexa.avs.auth.companionservice.RegCodeDisplayHandler;
import com.amazon.alexa.avs.config.DeviceConfig;
import com.amazon.alexa.avs.ui.BaseUI;

public class HeadlessUI extends BaseUI implements AccessTokenListener {

    private BlockingQueue<String> userInputs;
    private ExecutorService userInputParser;
    private Future<?> parseThread;
    private boolean helpTextPrinted;

    private RegCodeDisplayHandler regCodeDisplayHandler;

    public HeadlessUI(AVSController controller, AuthSetup authSetup, DeviceConfig config)
            throws Exception {
        super(controller, authSetup, config);
        userInputParser = Executors.newFixedThreadPool(1);
        helpTextPrinted = false;
    }

    private void init() {
        userInputs = new LinkedBlockingQueue<>();
        regCodeDisplayHandler =
                new RegCodeDisplayHandler(new HeadlessDialogFactory(userInputs), config);
    }

    @Override
    protected void startAuthentication() {
        authSetup.addAccessTokenListener(this);
        authSetup.startProvisioningThread(regCodeDisplayHandler);
    }

    @Override
    protected void createViews(DeviceConfig config) {
        init();
        bearerTokenView = new HeadlessAccessTokenView();
        notificationsView = new HeadlessNotificationsView();
        visualizerView = new HeadlessUserSpeechVisualizerView();
        localeView = new HeadlessLocaleView(config, controller);
        listenView = new HeadlessListenView(visualizerView, controller);
        playbackControlsView = new HeadlessPlaybackControlsView(controller);
        loginLogoutView = new HeadlessLoginLogoutView(config, controller, authSetup,
                regCodeDisplayHandler);

        new HeadlessDeviceNameView(config.getProductId(), config.getDsn());
        mainView = new HeadlessMainView();
    }

    @Override
    protected void initialize(DeviceConfig config) {
        Executor userEventExecutor = Executors.newFixedThreadPool(1);
        userEventExecutor.execute(() -> readUserInput());
    }

    private void readUserInput() {
        Scanner scanner = new Scanner(System.in);
        String readString = scanner.nextLine();
        while (readString != null) {
            if (readString.isEmpty()) {
                // Enter key was pressed
                userInputs.add("enter");
            } else {
                userInputs.add(readString);
            }

            if (scanner.hasNextLine()) {
                readString = scanner.nextLine();
            } else {
                readString = null;
            }
        }
    }

    private void parseUserInput() throws InterruptedException {
        String userInput;
        while ((userInput = userInputs.take()) != null) {
            parseUserInput(userInput);
        }
    }

    public void onAccessTokenReceived(String accessToken) {
        if (!helpTextPrinted) {
            printHelpText();
            helpTextPrinted = true;
        }
        if (parseThread != null) {
            parseThread.cancel(true);
        }
        parseThread = userInputParser.submit(() -> {
            try {
                parseUserInput();
            } catch (InterruptedException e) {
                return;
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
                System.exit(1);
            }
        });

    }

    @Override
    public void onAccessTokenRevoked() {
    }

    private void printHelpText() {
        System.out.println();
        System.out.println("Welcome to AVS! To interact with this app, type one of the following "
                + "commands, followed by <enter>");
        System.out.println("Login/Logout: login or logout");
        System.out.println("To listen: <space>/l/listen, or just press enter!");
        System.out.println("Next song: n/next");
        System.out.println("Play/Pause: p/play/pause");
        System.out.println("Previous song: b/back");
        System.out.println("Switch locale: en-US/en-GB/de-DE");
        System.out.println("Quit: q/quit/exit");
        System.out.println("Display this help text again: h/help");
        System.out.println();
    }

    private void parseUserInput(String input) {
        switch (input) {
            case " ":
            case "l":
            case "enter":
            case "listen":
                System.out.println("Listen button pressed");
                listenView.listenButtonPressed();
                break;
            case "n":
            case "next":
                System.out.println("Next button pressed");
                playbackControlsView.buttonPressed(PlaybackAction.NEXT);
                break;
            case "b":
            case "back":
                System.out.println("Back button pressed");
                playbackControlsView.buttonPressed(PlaybackAction.PREVIOUS);
                break;
            case "p":
            case "play":
            case "pause":
                System.out.println("Play/Pause button pressed");
                playbackControlsView.buttonPressed(PlaybackAction.PLAY);
                break;
            case "en-US":
            case "en-GB":
            case "de-DE":
                System.out.println("Switching locale to: " + input);
                localeView.handleLocaleChange(Locale.forLanguageTag(input));
                break;
            case "q":
            case "quit":
            case "exit":
                System.out.println("Exiting");
                System.exit(0);
                break;
            case "login":
                // We're starting a login flow which has it's own built in parsing. Once the
                // login flow is complete the parsing thread will be restarted.
                parseThread.cancel(true);
                System.out.println("Logging in");
                loginLogoutView.startLogin();
                break;
            case "logout":
                System.out.println("Logging out");
                loginLogoutView.startLogout();
                break;
            case "h":
            case "help":
                printHelpText();
                break;
            default:
                System.out.println("Unknown input: \"" + input + "\"");
        }
    }

}
