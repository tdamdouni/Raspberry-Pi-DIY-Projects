/**
 * Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */
package com.amazon.alexa.avs.companion;

import org.json.JSONException;
import org.json.JSONObject;

public class CompanionProvisioningInfo {
    private final String sessionId;
    private final String clientId;
    private final String redirectUri;
    private final String authCode;

    public CompanionProvisioningInfo(String sessionId, String clientId, String redirectUri, String authCode) {
        this.sessionId = sessionId;
        this.clientId = clientId;
        this.redirectUri = redirectUri;
        this.authCode = authCode;
    }

    public String getSessionId() {
        return sessionId;
    }

    public String getClientId() {
        return clientId;
    }

    public String getRedirectUri() {
        return redirectUri;
    }

    public String getAuthCode() {
        return authCode;
    }

    public JSONObject toJson() {
        try {
            JSONObject jsonObject = new JSONObject();
            jsonObject.put(AuthConstants.AUTH_CODE, authCode);
            jsonObject.put(AuthConstants.CLIENT_ID, clientId);
            jsonObject.put(AuthConstants.REDIRECT_URI, redirectUri);
            jsonObject.put(AuthConstants.SESSION_ID, sessionId);
            return jsonObject;
        } catch (JSONException e) {
            return null;
        }
    }
}
