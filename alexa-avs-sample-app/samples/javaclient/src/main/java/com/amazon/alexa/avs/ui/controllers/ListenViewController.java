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
package com.amazon.alexa.avs.ui.controllers;

import java.util.LinkedList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.RecordingRMSListener;
import com.amazon.alexa.avs.RequestListener;
import com.amazon.alexa.avs.ui.ListenUIHandler;
import com.amazon.alexa.avs.ui.SpeechStateChangeListener;

public class ListenViewController implements ListenUIHandler {
    private static final Logger log = LoggerFactory.getLogger(ListenViewController.class);

    private volatile ButtonState buttonState;
    private AVSController controller;
    private RecordingRMSListener rmsListener;
    private List<SpeechStateChangeListener> listeners;
    private RequestListener requestListener;
    private boolean buttonEnabled;

    public ListenViewController(RecordingRMSListener rmsListener, AVSController controller,
            RequestListener requestListener) {
        this.controller = controller;
        this.rmsListener = rmsListener;
        listeners = new LinkedList<>();
        this.requestListener = requestListener;

        buttonState = ButtonState.START;
        buttonEnabled = true;
    }

    @Override
    public void listenButtonPressed() {
        if (buttonEnabled) {
            controller.onUserActivity();

            if (buttonState == ButtonState.START) { // if in idle mode
                buttonState = ButtonState.STOP;
                controller.startRecording(rmsListener, new SpeechRequestListener());
                onListening();
            } else { // else we must already be in listening
                buttonState = ButtonState.PROCESSING;
                controller.stopRecording(); // stop the recording so the request can complete
                onProcessing();
            }
        }
    }

    private class SpeechRequestListener extends RequestListener {

        @Override
        public void onRequestFinished() {
            // In case we get a response from the server without
            // terminating the stream ourselves.
            if (buttonState == ButtonState.STOP) {
                listenButtonPressed();
            }
            finishProcessing();
            if (requestListener != null) {
                requestListener.onRequestFinished();
            }
        }

        @Override
        public void onRequestError(Throwable e) {
            log.error("An error occured creating speech request", e);
            listenButtonPressed();
            finishProcessing();
            if (requestListener != null) {
                requestListener.onRequestFinished();
            }
        }
    }

    /**
     * Handles functional logic to wrap up a speech request
     */
    private void finishProcessing() {
        buttonState = ButtonState.START;
        controller.processingFinished();
        // Now update the UI
        onProcessingFinished();
    }

    @Override
    public void addSpeechStateChangeListener(SpeechStateChangeListener listener) {
        if (listener != null) {
            listeners.add(listener);
        }
    }

    @Override
    public void onStopCaptureDirective() {
        if (buttonState == ButtonState.STOP) {
            listenButtonPressed();
        }
    }

    @Override
    public void onProcessing() {
        buttonEnabled = false;
        for (SpeechStateChangeListener listener : listeners) {
            listener.onProcessing();
        }
    }

    @Override
    public void onListening() {
        for (SpeechStateChangeListener listener : listeners) {
            listener.onListening();
        }
    }

    @Override
    public void onProcessingFinished() {
        buttonEnabled = true;
        for (SpeechStateChangeListener listener : listeners) {
            listener.onProcessingFinished();
        }
    }

    @Override
    public void onExpectSpeechDirective() {
        Thread thread = new Thread(() -> {
            while (!buttonEnabled || buttonState != ButtonState.START || controller.isSpeaking()) {
                try {
                    Thread.sleep(500);
                } catch (Exception e) {
                }
            }
            listenButtonPressed();
        });
        thread.start();
    }

    @Override
    public synchronized void onWakeWordDetected() {
        if (buttonState == ButtonState.START) { // if in idle mode
            log.info("Wake Word was detected");
            listenButtonPressed();
        }
    }

    private enum ButtonState {
        START,
        STOP,
        PROCESSING;
    }

    @Override
    public void onAccessTokenReceived(String accessToken) {
    }

    @Override
    public void onAccessTokenRevoked() {
    }
}
