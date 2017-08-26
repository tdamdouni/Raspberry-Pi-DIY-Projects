/**
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is
 * located the "LICENSE.txt" file accompanying this source. This file is distributed on an "AS
 * IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under the License.
 */
package com.amazon.alexa.avs;

public interface NotificationIndicator {

    void onNewNotification();

    void onQueuedNotifications();

    void onClearNotifications();
}
