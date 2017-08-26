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
package com.amazon.alexa.avs.ui;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.auth.AuthSetup;
import com.amazon.alexa.avs.config.DeviceConfig;

/**
 * The base class that encompasses all UI behavior.
 */
public abstract class BaseUI {

    // Set by this base class
    protected DeviceConfig config;
    protected AVSController controller;
    protected AuthSetup authSetup;

    // Should be set by subclasses
    protected LocaleUIHandler localeView;
    protected DeviceNameUIHandler deviceNameView;
    protected CardUIHandler cardView;
    protected AccessTokenUIHandler bearerTokenView;
    protected NotificationsUIHandler notificationsView;
    protected ListenUIHandler listenView;
    protected PlaybackControlsUIHandler playbackControlsView;
    protected UserSpeechVisualizerUIHandler visualizerView;
    protected LoginLogoutUIHandler loginLogoutView;
    protected MainUIHandler mainView;

    protected BaseUI(AVSController controller, AuthSetup authSetup, DeviceConfig config)
            throws Exception {
        this.authSetup = authSetup;
        this.controller = controller;
        this.config = config;
        createViews(config);
        addListeners();
        init(config);
        startAuthentication();
    }

    /**
     * Make sure required components are registered with each other before initialization.
     */
    private void addListeners() {
        listenView.addSpeechStateChangeListener(playbackControlsView);
        listenView.addSpeechStateChangeListener(visualizerView);
        listenView.addSpeechStateChangeListener(cardView);
        authSetup.addAccessTokenListener(listenView);
        authSetup.addAccessTokenListener(playbackControlsView);
        authSetup.addAccessTokenListener(loginLogoutView);
        authSetup.addAccessTokenListener(bearerTokenView);
        authSetup.addAccessTokenListener(controller);
    }

    /**
     * Initializes the controller, and any other initialization tasks that subclasses require.
     */
    private void init(DeviceConfig config) {
        initialize(config);
        controller.init(listenView, notificationsView, cardView);
        controller.startHandlingDirectives();
    }

    /**
     * Triggers the authentication flow for the specific UI.
     */
    protected abstract void startAuthentication();

    /**
     * Any views for interacting/displaying UI elements should be created here. As a result of
     * calling this method, all UIHandlers within BaseUI should be non-null.
     */
    protected abstract void createViews(DeviceConfig config);

    /**
     * Any initialization logic that a subclass needs to do should be done here. This occurs
     * after views are created, but before authentication.
     */
    protected abstract void initialize(DeviceConfig config);
}
