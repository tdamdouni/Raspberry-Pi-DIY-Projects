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

import static com.amazon.alexa.avs.PlaybackAction.PAUSE;
import static com.amazon.alexa.avs.PlaybackAction.PLAY;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.PlaybackAction;
import com.amazon.alexa.avs.ui.PlaybackControlsUIHandler;

public class PlaybackViewController implements PlaybackControlsUIHandler {

    private final AVSController controller;
    private boolean playbackControlsEnabled;

    public PlaybackViewController(AVSController controller) {
        this.controller = controller;
        this.playbackControlsEnabled = true;
    }

    @Override
    public void buttonPressed(PlaybackAction action) {
        if (playbackControlsEnabled) {
            controller.onUserActivity();
            switch (action) {
                case PAUSE:
                case PLAY:
                    controller.handlePlaybackAction(controller.isPlaying() ? PAUSE : PLAY);
                    break;
                default:
                    controller.handlePlaybackAction(action);
            }
        }
    }

    @Override
    public void onProcessing() {
        // No-op
    }

    @Override
    public void onListening() {
        this.playbackControlsEnabled = false;
    }

    @Override
    public void onProcessingFinished() {
        this.playbackControlsEnabled = true;
    }

    @Override
    public void onAccessTokenReceived(String accessToken) {
    }

    @Override
    public void onAccessTokenRevoked() {
    }
}
