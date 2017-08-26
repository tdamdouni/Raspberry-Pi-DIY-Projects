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
package com.amazon.alexa.avs.auth.companionservice;

import org.apache.commons.lang3.StringUtils;

import com.amazon.alexa.avs.auth.AuthConstants;

/**
 * A container for the necessary provisioning information from the companion service to start the provisioning process.
 */
public class CompanionServiceRegCodeResponse {
    private final String sessionId;
    private final String regCode;

    /**
     * Creates a {@link CompanionServiceRegCodeResponse} object.
     *
     * @param sessionId The sessionId from the companion service.
     * @param regCode The registration code to be shown to the user to register on the companion service.
     */
    public CompanionServiceRegCodeResponse(String sessionId, String regCode) {
        if (StringUtils.isBlank(sessionId)) {
            throw new IllegalArgumentException("Missing " + AuthConstants.SESSION_ID + " parameter");
        }

        if (StringUtils.isBlank(regCode)) {
            throw new IllegalArgumentException("Missing " + AuthConstants.REG_CODE + " parameter");
        }

        this.sessionId = sessionId;
        this.regCode = regCode;
    }

    /**
     * @return sessionId.
     */
    public String getSessionId() {
        return sessionId;
    }

    /**
     * @return regCode.
     */
    public String getRegCode() {
        return regCode;
    }
}
