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

import com.amazon.alexa.avs.ExpectSpeechListener;
import com.amazon.alexa.avs.ExpectStopCaptureListener;
import com.amazon.alexa.avs.ListenHandler;
import com.amazon.alexa.avs.auth.AccessTokenListener;
import com.amazon.alexa.avs.wakeword.WakeWordDetectedHandler;

/**
 * Controls behavior related to the user indicating a desire to speak to AVS.
 */
public interface ListenUIHandler
        extends SpeechStateChangeListener, ExpectStopCaptureListener, ExpectSpeechListener,
        WakeWordDetectedHandler, ListenHandler, AccessTokenListener {

    /**
     * Triggered when the user indicated a desire to listen. Note: This method may also be triggered
     * while the user is already listening, in which case it should trigger an end to listening.
     */
    void listenButtonPressed();

    /**
     * Registers listeners that care about various speech state changes.
     */
    void addSpeechStateChangeListener(SpeechStateChangeListener listener);
}
