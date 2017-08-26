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

import static com.amazon.alexa.avs.ui.controllers.AccessTokenViewController.ACCESS_TOKEN_LABEL;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.auth.AuthSetup;

import java.awt.GridLayout;

import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

import com.amazon.alexa.avs.ui.AccessTokenUIHandler;

public class GraphicalAccessTokenView extends JPanel implements AccessTokenUIHandler {

    private static final int TEXT_FIELD_COLUMNS = 50;

    private JTextField tokenTextField;

    GraphicalAccessTokenView(AuthSetup authSetup, AVSController controller) {
        super(new GridLayout(0, 1));
        this.add(new JLabel(ACCESS_TOKEN_LABEL));

        tokenTextField = new JTextField(TEXT_FIELD_COLUMNS);
        tokenTextField.addActionListener(e -> {
            controller.onUserActivity();
            authSetup.onAccessTokenReceived(tokenTextField.getText());
        });
        this.add(tokenTextField);
    }

    @Override
    public synchronized void onAccessTokenReceived(String accessToken) {
        SwingUtilities.invokeLater(() -> tokenTextField.setText(accessToken));
    }

    @Override
    public synchronized void onAccessTokenRevoked() {
        SwingUtilities.invokeLater(() -> tokenTextField.setText(""));
    }
}
