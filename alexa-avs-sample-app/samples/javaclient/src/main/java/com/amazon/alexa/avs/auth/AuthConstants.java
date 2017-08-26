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

/**
 * Constants related to authentication and device provisioning.
 */
@SuppressWarnings("javadoc")
public class AuthConstants {
    public static final String SESSION_ID = "sessionId";

    public static final String CLIENT_ID = "clientId";
    public static final String REDIRECT_URI = "redirectUri";
    public static final String AUTH_CODE = "authCode";

    public static final String CODE_CHALLENGE = "codeChallenge";
    public static final String CODE_CHALLENGE_METHOD = "codeChallengeMethod";
    public static final String DSN = "dsn";
    public static final String PRODUCT_ID = "productId";

    public static final String REG_CODE = "regCode";
    public static final String LOGOUT_SUCCESS = "logoutSuccess";

    // ERRORS
    public static final String ERROR = "error";
    public static final String MESSAGE = "message";
    public static final String INVALID_PARAM_ERROR = "INVALID_PARAM";
    public static final String INCORRECT_SESSION_ID_ERROR = "INCORRECT_SESSION_ID";
    public static final String LWA_ERROR = "LWA_ERROR";

    /**
     * Constants related specifically to OAuth 2.0 (http://tools.ietf.org/html/rfc6749) and draft 10
     * of Proof Key for Code Exchange by OAuth (https://tools.ietf.org/html/draft-ietf-oauth-spop-10).
     */
    public static class OAuth2 {
        public static final String AUTHORIZATION_CODE = "authorization_code";
        public static final String GRANT_TYPE = "grant_type";
        public static final String REDIRECT_URI = "redirect_uri";
        public static final String CODE = "code";
        public static final String CLIENT_ID = "client_id";
        public static final String CODE_VERIFIER = "code_verifier";
        public static final String ACCESS_TOKEN = "access_token";
        public static final String REFRESH_TOKEN = "refresh_token";
        public static final String EXPIRES_IN = "expires_in";
    }
}
