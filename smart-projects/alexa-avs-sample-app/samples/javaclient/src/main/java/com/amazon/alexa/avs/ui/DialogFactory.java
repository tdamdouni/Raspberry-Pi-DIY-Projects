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

/**
 * Factory providing prompts to the user telling them information or asking a Yes/No question.
 */
public interface DialogFactory {

    /**
     * Tell the user some information. The user must acknowledge this information before continuing.
     *
     * @param title
     *         Description of the type of message.
     * @param message
     *         Content of the message.
     */
    void showInformationalDialog(String title, String message);

    /**
     * Ask the user a Yes/No question.
     *
     * @param title
     *         Description of the type of message.
     * @param message
     *         Question text.
     * @return 0 if the user pressed yes, 1 if the user pressed no. Matches JOptionPane results.
     */
    int showYesNoDialog(String title, String message);
}
