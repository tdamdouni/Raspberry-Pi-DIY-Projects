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

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.RecordingRMSListener;
import com.amazon.alexa.avs.RequestListener;
import com.amazon.alexa.avs.ui.ListenUIHandler;
import com.amazon.alexa.avs.ui.SpeechStateChangeListener;
import com.amazon.alexa.avs.ui.controllers.ListenViewController;

public class HeadlessListenView implements ListenUIHandler {
    private ListenViewController listenViewController;

    public HeadlessListenView(RecordingRMSListener rmsListener, AVSController controller) {
        listenViewController =
                new ListenViewController(rmsListener, controller, new SpeechRequestListener());
    }

    @Override
    public void listenButtonPressed() {
        listenViewController.listenButtonPressed();
    }

    @Override
    public void addSpeechStateChangeListener(SpeechStateChangeListener listener) {
        listenViewController.addSpeechStateChangeListener(listener);
    }

    @Override
    public void onStopCaptureDirective() {
        listenViewController.onStopCaptureDirective();
    }

    @Override
    public void onProcessing() {
        listenViewController.onProcessing();
    }

    @Override
    public void onListening() {
        listenViewController.onListening();
    }

    @Override
    public void onProcessingFinished() {
        listenViewController.onProcessingFinished();
    }

    @Override
    public void onExpectSpeechDirective() {
        listenViewController.onExpectSpeechDirective();
    }

    @Override
    public synchronized void onWakeWordDetected() {
        listenViewController.onWakeWordDetected();
    }

    private static class SpeechRequestListener extends RequestListener {

        @Override
        public void onRequestFinished() {
        }

        @Override
        public void onRequestError(Throwable e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    @Override
    public void onAccessTokenReceived(String accessToken) {
        listenViewController.onAccessTokenReceived(accessToken);
    }

    @Override
    public void onAccessTokenRevoked() {
        listenViewController.onAccessTokenRevoked();
    }
}
