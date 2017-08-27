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

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;

import com.amazon.alexa.avs.ui.DialogFactory;

public class GraphicalDialogFactory implements DialogFactory {

    private JFrame contentPane;

    GraphicalDialogFactory(JFrame contentPane) {
        this.contentPane = contentPane;
    }

    @Override
    public void showInformationalDialog(String title, String message) {
        JTextArea textMessage = new JTextArea(message);
        textMessage.setEditable(false);
        JOptionPane.showMessageDialog(contentPane, textMessage, title,
                JOptionPane.INFORMATION_MESSAGE
        );
    }

    @Override
    public int showYesNoDialog(String title, String message) {
        JTextArea textMessage = new JTextArea(message);
        textMessage.setEditable(false);
        return JOptionPane.showConfirmDialog(contentPane, textMessage, title,
                JOptionPane.YES_NO_OPTION
        );
    }
}
