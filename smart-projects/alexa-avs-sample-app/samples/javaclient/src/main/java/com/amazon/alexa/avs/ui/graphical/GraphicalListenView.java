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

import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.RecordingRMSListener;
import com.amazon.alexa.avs.RequestListener;
import com.amazon.alexa.avs.auth.AccessTokenListener;
import com.amazon.alexa.avs.ui.ListenUIHandler;
import com.amazon.alexa.avs.ui.SpeechStateChangeListener;
import com.amazon.alexa.avs.ui.controllers.ListenViewController;

public class GraphicalListenView extends JPanel implements ListenUIHandler {

    private static final String NOT_LISTENING_LABEL = "Tap to speak to Alexa";
    private static final String LISTENING_LABEL = "Listening";
    private static final String PROCESSING_LABEL = " ";
    private static final String ERROR_DIALOG_TITLE = "Error";

    private ImageIcon notListeningIcon;
    private ImageIcon listeningIcon;
    private JLabel actionButtonLabel;
    private JButton actionButton;
    private ListenViewController listenViewController;

    GraphicalListenView(RecordingRMSListener rmsListener, AVSController controller) {
        super();
        ClassLoader resLoader = Thread.currentThread().getContextClassLoader();
        notListeningIcon = new ImageIcon(resLoader.getResource("res/avs-mic-icon.png"));
        listeningIcon = new ImageIcon(resLoader.getResource("res/avs-blue-mic-icon.png"));
        listenViewController =
                new ListenViewController(rmsListener, controller, new SpeechRequestListener(this));

        this.setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        actionButtonLabel = new JLabel(NOT_LISTENING_LABEL);
        actionButtonLabel.setAlignmentX(CENTER_ALIGNMENT);
        this.add(actionButtonLabel);

        actionButton = new JButton(notListeningIcon);
        actionButton.setAlignmentX(CENTER_ALIGNMENT);

        actionButton.setEnabled(false);
        actionButton.addActionListener(e -> listenButtonPressed());

        this.add(actionButton);
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
        SwingUtilities.invokeLater(() -> {
            actionButton.setEnabled(false);
            actionButtonLabel.setText(PROCESSING_LABEL);
        });
    }

    @Override
    public void onListening() {
        listenViewController.onListening();
        SwingUtilities.invokeLater(() -> {
            actionButtonLabel.setText(LISTENING_LABEL);
            actionButton.setIcon(listeningIcon);
        });
    }

    @Override
    public void onProcessingFinished() {
        listenViewController.onProcessingFinished();
        SwingUtilities.invokeLater(() -> {
            actionButton.setEnabled(true);
            actionButtonLabel.setText(NOT_LISTENING_LABEL);
            actionButton.setIcon(notListeningIcon);
        });
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

        private GraphicalListenView parentComponent;

        SpeechRequestListener(GraphicalListenView listenView) {
            parentComponent = listenView;
        }

        @Override
        public void onRequestFinished() {
        }

        @Override
        public void onRequestError(Throwable e) {
            JOptionPane.showMessageDialog(parentComponent, e.getMessage(), ERROR_DIALOG_TITLE,
                    JOptionPane.ERROR_MESSAGE
            );
        }
    }

    @Override
    public synchronized void onAccessTokenReceived(String accessToken) {
        SwingUtilities.invokeLater(() -> actionButton.setEnabled(true));
    }

    @Override
    public synchronized void onAccessTokenRevoked() {
        SwingUtilities.invokeLater(() -> actionButton.setEnabled(false));
    }
}
