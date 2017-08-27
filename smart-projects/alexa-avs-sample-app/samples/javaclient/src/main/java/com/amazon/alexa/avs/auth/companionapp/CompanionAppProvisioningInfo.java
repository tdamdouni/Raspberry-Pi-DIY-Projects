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
package com.amazon.alexa.avs.auth.companionapp;

import org.apache.commons.lang3.StringUtils;

import com.amazon.alexa.avs.auth.AuthConstants;
import com.amazon.alexa.avs.auth.MissingParameterException;

/**
 * A container for the necessary provisioning information from the companion app/service.
 */
public class CompanionAppProvisioningInfo {
    private final String sessionId;
    private final String clientId;
    private final String redirectUri;
    private final String authCode;

    /**
     * Creates a {@link CompanionAppProvisioningInfo} object.
     *
     * @param sessionId The sessionId used to initiate this information.
     * @param clientId The clientId of the companion.
     * @param redirectUri The redirectUri used by the companion.
     * @param authCode The authCode from the companion.
     */
    public CompanionAppProvisioningInfo(String sessionId, String clientId, String redirectUri, String authCode) {
        super();

        if (StringUtils.isBlank(sessionId)) {
            throw new MissingParameterException(AuthConstants.SESSION_ID);
        }

        if (StringUtils.isBlank(clientId)) {
            throw new MissingParameterException(AuthConstants.CLIENT_ID);
        }

        if (StringUtils.isBlank(redirectUri)) {
            throw new MissingParameterException(AuthConstants.REDIRECT_URI);
        }

        if (StringUtils.isBlank(authCode)) {
            throw new MissingParameterException(AuthConstants.AUTH_CODE);
        }

        this.sessionId = sessionId;
        this.clientId = clientId;
        this.redirectUri = redirectUri;
        this.authCode = authCode;
    }

    /**
     * @return sessionId.
     */
    public String getSessionId() {
        return sessionId;
    }

    /**
     * @return clientId.
     */
    public String getClientId() {
        return clientId;
    }

    /**
     * @return redirectUri.
     */
    public String getRedirectUri() {
        return redirectUri;
    }

    /**
     * @return authCode.
     */
    public String getAuthCode() {
        return authCode;
    }

}
