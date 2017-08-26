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

import com.amazon.alexa.avs.ui.UserSpeechVisualizerUIHandler;

public class HeadlessUserSpeechVisualizerView implements UserSpeechVisualizerUIHandler {

    @Override
    public void onProcessing() {
        System.out.println("Processing");
    }

    @Override
    public void onListening() {
        System.out.println("Listening");
    }

    @Override
    public void onProcessingFinished() {
        System.out.println("Done");
    }

    @Override
    public void rmsChanged(int rms) {
    }
}
