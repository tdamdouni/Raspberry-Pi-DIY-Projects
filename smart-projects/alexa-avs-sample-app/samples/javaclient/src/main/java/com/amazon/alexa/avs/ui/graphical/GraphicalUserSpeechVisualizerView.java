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
package com.amazon.alexa.avs.ui.graphical;

import javax.swing.JProgressBar;
import javax.swing.SwingUtilities;

import com.amazon.alexa.avs.ui.UserSpeechVisualizerUIHandler;

public class GraphicalUserSpeechVisualizerView extends JProgressBar
        implements UserSpeechVisualizerUIHandler {

    GraphicalUserSpeechVisualizerView() {
        super(0, 100);
    }

    @Override
    public void onProcessing() {
        SwingUtilities.invokeLater(() -> setIndeterminate(true));
    }

    @Override
    public void onListening() {
        // No-op
    }

    @Override
    public void onProcessingFinished() {
        SwingUtilities.invokeLater(() -> setIndeterminate(false));
    }

    @Override
    public void rmsChanged(int rms) { // AudioRMSListener callback
        // update the visualizer
        SwingUtilities.invokeLater(() -> setValue(rms));
    }
}
