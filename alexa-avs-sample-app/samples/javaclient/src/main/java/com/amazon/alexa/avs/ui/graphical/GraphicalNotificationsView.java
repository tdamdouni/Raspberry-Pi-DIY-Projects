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

import static com.amazon.alexa.avs.ui.controllers.NotificationsViewController.NEW_NOTIFICATION;
import static com.amazon.alexa.avs.ui.controllers.NotificationsViewController.NO_NOTIFICATIONS;
import static com.amazon.alexa.avs.ui.controllers.NotificationsViewController.QUEUED_NOTIFICATIONS;

import java.awt.Color;

import javax.swing.BorderFactory;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

import com.amazon.alexa.avs.ui.NotificationsUIHandler;

public class GraphicalNotificationsView extends JPanel implements NotificationsUIHandler {

    private static final String NOTIFICATION_NAME = "notification";

    private JLabel notificationStatus;

    GraphicalNotificationsView() {
        super();
        notificationStatus = new JLabel(NO_NOTIFICATIONS);
        notificationStatus.setName(NOTIFICATION_NAME);
        this.add(notificationStatus);
        this.setSize(150, 50);
        this.setBorder(BorderFactory.createLineBorder(Color.BLACK));
    }

    @Override
    public void onNewNotification() {
        SwingUtilities.invokeLater(() -> {
            setBackground(Color.YELLOW);
            notificationStatus.setText(NEW_NOTIFICATION);
        });
    }

    @Override
    public void onQueuedNotifications() {
        SwingUtilities.invokeLater(() -> {
            setBackground(Color.YELLOW);
            notificationStatus.setText(QUEUED_NOTIFICATIONS);
        });
    }

    @Override
    public void onClearNotifications() {
        SwingUtilities.invokeLater(() -> {
            setBackground(null);
            notificationStatus.setText(NO_NOTIFICATIONS);
        });
    }
}
