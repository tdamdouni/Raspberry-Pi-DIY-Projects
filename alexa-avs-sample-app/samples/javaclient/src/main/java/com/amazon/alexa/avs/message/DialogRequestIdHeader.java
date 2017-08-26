/** 
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Amazon Software License (the "License"). You may not use this file 
 * except in compliance with the License. A copy of the License is located at
 *
 *   http://aws.amazon.com/asl/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, 
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the 
 * specific language governing permissions and limitations under the License.
 */
package com.amazon.alexa.avs.message;

public class DialogRequestIdHeader extends MessageIdHeader {

    private String dialogRequestId;

    public DialogRequestIdHeader() {
        // For Jackson
    }

    public DialogRequestIdHeader(String namespace, String name, String dialogRequestId) {
        super(namespace, name);
        this.dialogRequestId = dialogRequestId;
    }

    public final void setDialogRequestId(String dialogRequestId) {
        this.dialogRequestId = dialogRequestId;
    }

    public final String getDialogRequestId() {
        return dialogRequestId;
    }

    @Override
    public String toString() {
        return String.format("%1$s dialogRequestId:%2$s", super.toString(), dialogRequestId);
    }
}
