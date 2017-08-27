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
package com.amazon.alexa.avs;

public enum SpeechProfile {

    // For a hold-to-talk/push-to-talk device
    CLOSE_TALK("CLOSE_TALK"),
    
    // For a tap-to-talk device that relies on Alexa's end-of-speech detection.
    NEAR_FIELD("NEAR_FIELD");

    private final String profileName;

    SpeechProfile(String profileName) {
        this.profileName = profileName;
    }

    @Override
    public String toString() {
        return this.profileName;
    }
}
