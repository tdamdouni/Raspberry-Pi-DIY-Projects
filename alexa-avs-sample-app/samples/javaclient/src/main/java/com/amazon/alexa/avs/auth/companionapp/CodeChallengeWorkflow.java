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

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

import org.apache.commons.codec.binary.Base64;

@SuppressWarnings("javadoc")
public class CodeChallengeWorkflow {
    private static final String SHA_256 = "S256";
    private static final String ALORITHM_SHA_256 = "SHA-256";

    private String codeVerifier;
    private String codeChallengeMethod;
    private String codeChallenge;
    private static CodeChallengeWorkflow instance = new CodeChallengeWorkflow();

    private CodeChallengeWorkflow() {
    }

    /**
     * @return the {@link CodeChallengeWorkflow} instance
     */
    public static CodeChallengeWorkflow getInstance() {
        return instance;
    }

    /**
     * CodeChallenge parameter generation logic goes here. We are implementing version 10 of the specification.
     * Design doc: https://w.amazon.com/index.php/IdentityServices/LWA/Projects/LWA_3P_SSO_Launch
     * SPOP Protocol specification version 10: https://tools.ietf.org/html/draft-ietf-oauth-spop-02
     */
    public void generateProofKeyParameters() {
        try {
            codeVerifier = generateCodeVerifier();
            codeChallengeMethod = SHA_256;
            codeChallenge = generateCodeChallenge(codeVerifier, codeChallengeMethod);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Your JRE does not support the required "
                    + CodeChallengeWorkflow.ALORITHM_SHA_256 + " algorithm.", e);
        }
    }

    /**
     * @return the codeVerifier generated.
     */
    public String getCodeVerifier() {
        return this.codeVerifier;
    }

    /**
     * @return the codeChallenge generated.
     */
    public String getCodeChallenge() {
        return this.codeChallenge;
    }

    /**
     * @return the codeChallengeMethod used. Defaults to {@value #SHA_256}
     */
    public String getCodeChallengeMethod() {
        return this.codeChallengeMethod;
    }

    private String generateCodeChallenge(String codeVerifier, String codeChallengeMethod)
            throws NoSuchAlgorithmException {
        String codeChallenge =
                base64UrlEncode(MessageDigest.getInstance(ALORITHM_SHA_256).digest(codeVerifier.getBytes()));
        return codeChallenge;
    }

    private String generateCodeVerifier() {
        byte[] randomOctetSequence = generateRandomOctetSequence();
        String codeVerifier = base64UrlEncode(randomOctetSequence);
        return codeVerifier;
    }

    /**
     * As per Proof Key/SPOP protocol Version 10
     * @return a random 32 sized octet sequence from allowed range
     */
    private byte[] generateRandomOctetSequence() {
        SecureRandom random = new SecureRandom();
        byte[] octetSequence = new byte[32];
        random.nextBytes(octetSequence);

        return octetSequence;
    }

    /**
     * This method is borrowed from the SPOP protocol spec version 10 here : http://datatracker.ietf.org/doc/draft-ietf-oauth-spop/?include_text=1
     * @param arg the string to convert
     * @return base64 URL encoded string value as specified by spec.
     */
    private String base64UrlEncode(byte[] arg) {
        return Base64.encodeBase64URLSafeString(arg);
    }
}
