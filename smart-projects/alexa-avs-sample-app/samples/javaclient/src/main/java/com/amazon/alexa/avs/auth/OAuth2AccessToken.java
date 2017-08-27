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
package com.amazon.alexa.avs.auth;

import java.util.Calendar;
import java.util.Date;

import org.apache.commons.lang3.StringUtils;

/**
 * Holds relevent accessToken information from LWA.
 */
public class OAuth2AccessToken {

    private final String accessToken;
    private final long expiresTime;

    /**
     * Creates an {@link OAuth2AccessToken} object.
     *
     * @param accessToken The accessToken returned from LWA.
     * @param expiresIn Time in seconds that the accessToken expires in.
     */
    public OAuth2AccessToken(String accessToken, int expiresIn) {
        if (StringUtils.isBlank(accessToken)) {
            throw new IllegalArgumentException("Missing " + AuthConstants.OAuth2.ACCESS_TOKEN + " parameter");
        }

        if (expiresIn < 0) {
            throw new IllegalArgumentException("Invalid " + AuthConstants.OAuth2.EXPIRES_IN
                    + " value. Must be a positive number.");
        }

        Date currentDate = new Date();
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(currentDate);
        calendar.add(Calendar.SECOND, expiresIn);

        this.accessToken = accessToken;
        this.expiresTime = calendar.getTime().getTime();
    }

    /**
     * @return accessToken
     */
    public String getAccessToken() {
        return accessToken;
    }

    /**
     * The time in milliseconds that the accessToken expires.
     * @return time in milliseconds that the accessToken expires.
     */
    public long getExpiresTime() {
        return expiresTime;
    }
}
