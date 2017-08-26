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
package com.amazon.alexa.avs.message.request.settings;

import java.util.List;

import com.amazon.alexa.avs.message.Payload;

public class SettingsUpdatedPayload extends Payload {
    private final List<Setting> settings;

    public SettingsUpdatedPayload(List<Setting> settings) {
        this.settings = settings;
    }

    public List<Setting> getSettings() {
        return settings;
    }
}
