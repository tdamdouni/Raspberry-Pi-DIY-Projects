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
package com.amazon.alexa.avs;

import java.util.UUID;

/**
 * DialogRequestIdAuthority creates and keeps track of the active dialogRequestId.
 */
public class DialogRequestIdAuthority {

    private static final DialogRequestIdAuthority instance;

    static {
        instance = new DialogRequestIdAuthority();
    }

    private String currentDialogRequestId;

    private DialogRequestIdAuthority() {
    }

    public static DialogRequestIdAuthority getInstance() {
        return instance;
    }

    public String createNewDialogRequestId() {
        currentDialogRequestId = UUID.randomUUID().toString();
        return currentDialogRequestId;
    }

    public boolean isCurrentDialogRequestId(String candidateRequestId) {
        return currentDialogRequestId != null && currentDialogRequestId.equals(candidateRequestId);
    }
}
