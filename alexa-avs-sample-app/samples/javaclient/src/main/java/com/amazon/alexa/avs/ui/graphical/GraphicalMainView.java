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
package com.amazon.alexa.avs.ui.graphical;

import java.awt.FlowLayout;

import javax.swing.BoxLayout;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.WindowConstants;
import javax.swing.border.EmptyBorder;

import com.amazon.alexa.avs.ui.MainUIHandler;
import com.amazon.alexa.avs.ui.controllers.MainViewController;

public class GraphicalMainView extends JFrame implements MainUIHandler {

    private static final int APP_WIDTH = 570;
    private static final int APP_HEIGHT = 620;

    private MainViewController mainViewController;

    GraphicalMainView(GraphicalDeviceNameView deviceNameView, GraphicalLocaleView localeView,
            GraphicalAccessTokenView bearerTokenView, GraphicalNotificationsView notificationsView,
            GraphicalUserSpeechVisualizerView userSpeechVisualizerView,
            GraphicalListenView listenView, GraphicalPlaybackControlsView playbackControlsView,
            GraphicalCardView cardView, GraphicalLoginLogoutView loginLogoutView) {
        super();
        mainViewController = new MainViewController();
        getContentPane().setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));
        getRootPane().setBorder(new EmptyBorder(10, 10, 10, 10));

        addTopPanel(deviceNameView, notificationsView);
        getContentPane().add(localeView);
        getContentPane().add(loginLogoutView);
        getContentPane().add(bearerTokenView);
        getContentPane().add(userSpeechVisualizerView);
        getContentPane().add(listenView);
        getContentPane().add(playbackControlsView);
        getContentPane().add(cardView);

        setTitle(getAppTitle());
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setSize(APP_WIDTH, APP_HEIGHT);
    }

    @Override
    public String getAppTitle() {
        return mainViewController.getAppTitle();
    }

    private void addTopPanel(GraphicalDeviceNameView deviceNameView,
            GraphicalNotificationsView notificationsView) {
        FlowLayout flowLayout = new FlowLayout(FlowLayout.LEFT, 0, 0);
        JPanel topPanel = new JPanel(flowLayout);
        topPanel.add(deviceNameView);
        topPanel.add(notificationsView);
        getContentPane().add(topPanel);
    }
}
