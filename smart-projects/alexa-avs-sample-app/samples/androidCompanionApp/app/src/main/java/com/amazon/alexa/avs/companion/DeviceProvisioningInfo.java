/**
 * Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */
package com.amazon.alexa.avs.companion;

import org.apache.commons.lang3.StringUtils;

import java.util.ArrayList;
import java.util.List;

public class DeviceProvisioningInfo {
    private final String productId;
    private final String dsn;
    private final String sessionId;
    private final String codeChallenge;
    private final String codeChallengeMethod;

    public DeviceProvisioningInfo(String productId, String dsn, String sessionId, String codeChallenge, String codeChallengeMethod) {
        List<String> missingParameters = new ArrayList<String>();
        if (StringUtils.isBlank(productId)) {
            missingParameters.add(AuthConstants.PRODUCT_ID);
        }

        if (StringUtils.isBlank(dsn)) {
            missingParameters.add(AuthConstants.DSN);
        }

        if (StringUtils.isBlank(sessionId)) {
            missingParameters.add(AuthConstants.SESSION_ID);
        }

        if (StringUtils.isBlank(codeChallenge)) {
            missingParameters.add(AuthConstants.CODE_CHALLENGE);
        }

        if (StringUtils.isBlank(codeChallengeMethod)) {
            missingParameters.add(AuthConstants.CODE_CHALLENGE_METHOD);
        }

        if (missingParameters.size() != 0) {
            throw new MissingParametersException(missingParameters);
        }

        this.productId = productId;
        this.dsn = dsn;
        this.sessionId = sessionId;
        this.codeChallenge = codeChallenge;
        this.codeChallengeMethod = codeChallengeMethod;
    }

    public String getProductId() {
        return productId;
    }

    public String getDsn() {
        return dsn;
    }

    public String getSessionId() {
        return sessionId;
    }

    public String getCodeChallenge() {
        return codeChallenge;
    }

    public String getCodeChallengeMethod() {
        return codeChallengeMethod;
    }

    public static class MissingParametersException extends IllegalArgumentException {
        private static final long serialVersionUID = 1L;
        private final List<String> missingParameters;

        public MissingParametersException(List<String> missingParameters) {
            super();
            this.missingParameters = missingParameters;
        }

        @Override
        public String getMessage() {
            return "The following parameters were missing or empty strings: "
                    + StringUtils.join(missingParameters.toArray(), ", ");
        }

        public List<String> getMissingParameters() {
            return missingParameters;
        }
    }
}