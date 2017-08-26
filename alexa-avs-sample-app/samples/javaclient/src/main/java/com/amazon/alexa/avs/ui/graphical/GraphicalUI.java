package com.amazon.alexa.avs.ui.graphical;

import javax.swing.JFrame;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.auth.AuthSetup;
import com.amazon.alexa.avs.auth.companionservice.RegCodeDisplayHandler;
import com.amazon.alexa.avs.config.DeviceConfig;
import com.amazon.alexa.avs.ui.BaseUI;

public class GraphicalUI extends BaseUI {

    private RegCodeDisplayHandler regCodeDisplayHandler;

    public GraphicalUI(AVSController controller, AuthSetup authSetup, DeviceConfig config)
            throws Exception {
        super(controller, authSetup, config);
    }

    @Override
    protected void startAuthentication() {
        regCodeDisplayHandler =
                new RegCodeDisplayHandler(new GraphicalDialogFactory((JFrame) mainView), config);
        authSetup.startProvisioningThread(regCodeDisplayHandler);
    }

    @Override
    protected void createViews(DeviceConfig config) {
        GraphicalAccessTokenView bearerTokenView =
                new GraphicalAccessTokenView(authSetup, controller);
        GraphicalNotificationsView notificationsView = new GraphicalNotificationsView();
        GraphicalDeviceNameView deviceNameView =
                new GraphicalDeviceNameView(config.getProductId(), config.getDsn());
        GraphicalLocaleView localeView = new GraphicalLocaleView(config, controller);
        GraphicalUserSpeechVisualizerView visualizerView = new GraphicalUserSpeechVisualizerView();
        GraphicalListenView listenView = new GraphicalListenView(visualizerView, controller);
        GraphicalPlaybackControlsView playbackControlsView =
                new GraphicalPlaybackControlsView(visualizerView, controller);
        GraphicalCardView cardView = new GraphicalCardView();
        GraphicalLoginLogoutView loginLogoutView = new GraphicalLoginLogoutView(config,
                controller, authSetup, this);

        // Assign the views to the base UI members for future reference
        this.bearerTokenView = bearerTokenView;
        this.notificationsView = notificationsView;
        this.deviceNameView = deviceNameView;
        this.localeView = localeView;
        this.visualizerView = visualizerView;
        this.listenView = listenView;
        this.playbackControlsView = playbackControlsView;
        this.cardView = cardView;
        this.loginLogoutView = loginLogoutView;

        mainView = new GraphicalMainView(deviceNameView, localeView, bearerTokenView,
                notificationsView, visualizerView, listenView, playbackControlsView, cardView,
                loginLogoutView);
    }

    RegCodeDisplayHandler getRegCodeDisplayHandler() {
        return regCodeDisplayHandler;
    }

    @Override
    protected void initialize(DeviceConfig config) {
        ((GraphicalMainView) mainView).setVisible(true);
    }

}
