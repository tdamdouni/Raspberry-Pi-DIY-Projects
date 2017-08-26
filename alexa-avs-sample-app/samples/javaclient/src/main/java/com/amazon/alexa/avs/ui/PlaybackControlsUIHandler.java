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

import com.amazon.alexa.avs.PlaybackAction;
import com.amazon.alexa.avs.auth.AccessTokenListener;

/**
 * Handles playback events (Play/Pause/Next/Previous).
 */
public interface PlaybackControlsUIHandler extends SpeechStateChangeListener, AccessTokenListener {

    /**
     * Handler for button events. When a playback button is pressed, call this method with the
     * appropriate action (Play, Paused, Next, Previous).
     *
     * @param action
     *         Action that occurred.
     */
    void buttonPressed(PlaybackAction action);
}
