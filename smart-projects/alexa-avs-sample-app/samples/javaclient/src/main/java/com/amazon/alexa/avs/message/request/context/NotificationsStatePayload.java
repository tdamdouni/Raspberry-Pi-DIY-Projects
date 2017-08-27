/**
 * Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */
package com.amazon.alexa.avs.message.request.context;

import com.amazon.alexa.avs.message.Payload;

public class NotificationsStatePayload extends Payload {
    private boolean isEnabled;
    private boolean isVisualIndicatorPersisted;

    public NotificationsStatePayload() {
    }

    public NotificationsStatePayload(boolean enabled, boolean persisted) {
        this.isEnabled = enabled;
        this.isVisualIndicatorPersisted = persisted;
    }

    public void setIsEnabled(boolean enabled) {
        this.isEnabled = enabled;
    }

    public boolean getIsEnabled() {
        return isEnabled;
    }

    public void setIsVisualIndicatorPersisted(boolean persisted) {
        this.isVisualIndicatorPersisted = persisted;
    }

    public boolean getIsVisualIndicatorPersisted() {
        return isVisualIndicatorPersisted;
    }
}
