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
package com.amazon.alexa.avs.message.request.context;

import com.amazon.alexa.avs.message.Payload;

public final class SpeechStatePayload extends Payload {
    private final String token;
    private final long offsetInMilliseconds;
    private final String playerActivity;

    public SpeechStatePayload(String token, long offsetInMilliseconds, String playerActivity) {
        this.token = token;
        this.offsetInMilliseconds = offsetInMilliseconds;
        this.playerActivity = playerActivity;
    }

    public String getToken() {
        return this.token;
    }

    public long getOffsetInMilliseconds() {
        return this.offsetInMilliseconds;
    }

    public String getPlayerActivity() {
        return this.playerActivity;
    }

}
