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
package com.amazon.alexa.avs.ui.headless;

import static com.amazon.alexa.avs.ui.controllers.NotificationsViewController.NEW_NOTIFICATION;
import static com.amazon.alexa.avs.ui.controllers.NotificationsViewController.NO_NOTIFICATIONS;
import static com.amazon.alexa.avs.ui.controllers.NotificationsViewController.QUEUED_NOTIFICATIONS;

import com.amazon.alexa.avs.ui.NotificationsUIHandler;

public class HeadlessNotificationsView implements NotificationsUIHandler {

    @Override
    public void onNewNotification() {
        System.out.println(NEW_NOTIFICATION);
    }

    @Override
    public void onQueuedNotifications() {
        System.out.println(QUEUED_NOTIFICATIONS);
    }

    @Override
    public void onClearNotifications() {
        System.out.println(NO_NOTIFICATIONS);
    }
}
