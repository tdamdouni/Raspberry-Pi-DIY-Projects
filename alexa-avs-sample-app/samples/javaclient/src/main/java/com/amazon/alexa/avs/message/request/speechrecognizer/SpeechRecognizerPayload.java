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
package com.amazon.alexa.avs.message.request.speechrecognizer;

import com.amazon.alexa.avs.SpeechProfile;
import com.amazon.alexa.avs.message.Payload;

public final class SpeechRecognizerPayload extends Payload {
    private final String profile;
    private final String format;

    public SpeechRecognizerPayload(SpeechProfile profile, String format) {
        this.profile = profile.toString();
        this.format = format;
    }

    public String getProfile() {
        return profile;
    }

    public String getFormat() {
        return format;
    }
}
