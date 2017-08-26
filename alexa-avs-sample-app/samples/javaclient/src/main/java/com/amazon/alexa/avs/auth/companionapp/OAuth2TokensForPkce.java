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
import com.amazon.alexa.avs.auth.OAuth2AccessToken;

/**
 * Container for information regarding accessTokens and refreshTokens.
 */
public class OAuth2TokensForPkce extends OAuth2AccessToken {

    private final String clientId;
    private final String refreshToken;

    /**
     * Creates an {@link OAuth2TokensForPkce} object.
     *
     * @param clientId The clientId of the companion app/service that initiated the workflow.
     * @param accessToken The accessToken returned from LWA.
     * @param refreshToken The refreshToken returned from LWA.
     * @param expiresIn Time in seconds that the accessToken expires in.
     */
    public OAuth2TokensForPkce(String clientId, String accessToken, String refreshToken, int expiresIn) {
        super(accessToken, expiresIn);

        if (StringUtils.isBlank(clientId)) {
            throw new IllegalArgumentException("Missing or empty " + AuthConstants.OAuth2.CLIENT_ID + " parameter");
        }

        if (StringUtils.isBlank(refreshToken)) {
            throw new IllegalArgumentException("Missing " + AuthConstants.OAuth2.REFRESH_TOKEN + " parameter");
        }

        this.clientId = clientId;
        this.refreshToken = refreshToken;
    }

    /**
     * @return clientId.
     */
    public String getClientId() {
        return clientId;
    }

    /**
     * @return refreshToken.
     */
    public String getRefreshToken() {
        return refreshToken;
    }
}
