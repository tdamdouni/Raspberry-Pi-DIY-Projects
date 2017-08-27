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

import java.util.concurrent.BlockingQueue;

import javax.swing.JOptionPane;

import com.amazon.alexa.avs.ui.DialogFactory;

public class HeadlessDialogFactory implements DialogFactory {

    private BlockingQueue<String> userInputs;

    public HeadlessDialogFactory(BlockingQueue<String> userInputs) {
        this.userInputs = userInputs;
    }

    @Override
    public void showInformationalDialog(String title, String message) {
        System.out.println(title.toUpperCase() + ": " + message);
        String input;
        try {
            while ((input = userInputs.take()) != null) {
                switch (input) {
                    case "enter":
                        System.out.println("OK");
                        return;
                    case "exit":
                    case "quit":
                        System.exit(0);
                    default:
                        System.out.println("Invalid input. Please just press enter to continue");
                }
            }
        } catch (InterruptedException e) {
            System.exit(0);
        }
    }

    @Override
    public int showYesNoDialog(String title, String message) {
        System.out.println(title.toUpperCase() + ": " + message + " [y/n/exit]");
        String input;
        try {
            while ((input = userInputs.take()) != null) {
                switch (input) {
                    case "y":
                        return JOptionPane.YES_OPTION;
                    case "n":
                        return JOptionPane.NO_OPTION;
                    case "exit":
                    case "quit":
                        System.exit(0);
                    default:
                        System.out.println("Invalid option. Please type y, n, or exit");
                }
            }
        } catch (InterruptedException e) {
            System.exit(0);
        }
        return -1;
    }
}
