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

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.StandardCharsets;

import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonReader;

import org.apache.commons.io.IOUtils;

import com.amazon.alexa.avs.auth.AuthConstants;
import com.amazon.alexa.avs.auth.OAuth2AccessToken;

/**
 * Device side implementation of http://tools.ietf.org/html/draft-ietf-oauth-spop-10#section-4.4.1.
 * Uses the Login With Amazon OAuth2 API to facilitate the exchange of an authCode for access/refresh
 * tokens.
 */
public class OAuth2ClientForPkce {
    private static final String TOKEN_PATH = "/auth/o2/token";

    private final URL tokenEndpoint;

    /**
     * Creates an {@link OAuth2ClientForPkce} given an endpoint.
     * @param endpoint
     */
    public OAuth2ClientForPkce(URL endpoint) {
        try {
            this.tokenEndpoint = new URL(endpoint, TOKEN_PATH);
        } catch (MalformedURLException e) {
            // Convert to a RuntimeException because we've already validated that endpoint is correct when reading in
            // DeviceConfig
            throw new RuntimeException(e);
        }
    }

    /**
     * Uses the LWA service to fetch an access token and refresh token in exchange for a refresh token and clientId.
     * Expected use case of this method: refreshing tokens once the initial provisioning is complete and normal
     * usage of the device is ready to commence.
     *
     * @param refreshToken received from the initial provisioning request
     * @param clientId of the security profile associated with the companion app
     * @return {@link OAuth2AccessToken} object containing the access token and refresh token
     * @throws IOException
     */
    public OAuth2TokensForPkce exchangeRefreshTokenForTokens(String refreshToken, String clientId) throws IOException {
        HttpURLConnection connection = (HttpURLConnection) tokenEndpoint.openConnection();

        JsonObject data = prepareExchangeRefreshTokenForTokensData(refreshToken, clientId);

        JsonObject jsonObject = postRequest(connection, data.toString());

        String newAccessToken = jsonObject.getString(AuthConstants.OAuth2.ACCESS_TOKEN);
        String newRefreshToken = jsonObject.getString(AuthConstants.OAuth2.REFRESH_TOKEN);
        int expiresIn = jsonObject.getInt(AuthConstants.OAuth2.EXPIRES_IN);

        return new OAuth2TokensForPkce(clientId, newAccessToken, newRefreshToken, expiresIn);
    }

    /**
     * Uses the LWA service to fetch an access token and refresh token in exchange for an auth code
     * (and a few other relevant parameter). Expected use case of this method: once we receive a
     * message/notification from the companion app with the authCode, this method will be used to
     * hit LWA and return tokens. These tokens can then be used to access AVS.
     *
     * @param authCode provided by the companion application
     * @param redirectUri corresponding to the companion application
     * @param clientId of the security profile associated with the companion app
     * @param codeVerifier unique value known to the device
     * @return {@link OAuth2AccessToken} object containing the access token and refresh token
     * @throws IOException
     */
    public OAuth2TokensForPkce exchangeAuthCodeForTokens(String authCode, String redirectUri, String clientId,
            String codeVerifier) throws IOException {
        HttpURLConnection connection = (HttpURLConnection) tokenEndpoint.openConnection();

        JsonObject data = prepareExchangeAuthCodeForTokensData(authCode, redirectUri, clientId, codeVerifier);

        JsonObject jsonObject = postRequest(connection, data.toString());

        String newAccessToken = jsonObject.getString(AuthConstants.OAuth2.ACCESS_TOKEN);
        String newRefreshToken = jsonObject.getString(AuthConstants.OAuth2.REFRESH_TOKEN);
        int expiresIn = jsonObject.getInt(AuthConstants.OAuth2.EXPIRES_IN);

        return new OAuth2TokensForPkce(clientId, newAccessToken, newRefreshToken, expiresIn);
    }

    // Helper method used by the class to make HTTP request to LWA service
    JsonObject postRequest(HttpURLConnection connection, String data) throws IOException {
        int responseCode = -1;
        InputStream error = null;
        InputStream response = null;
        DataOutputStream outputStream = null;
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "application/json");
        connection.setDoOutput(true);

        outputStream = new DataOutputStream(connection.getOutputStream());
        outputStream.write(data.getBytes(StandardCharsets.UTF_8));
        outputStream.flush();
        outputStream.close();
        responseCode = connection.getResponseCode();

        try {
            response = connection.getInputStream();
            JsonReader reader = Json.createReader(new InputStreamReader(response, StandardCharsets.UTF_8));
            return reader.readObject();

        } catch (IOException ioException) {
            error = connection.getErrorStream();
            if (error != null) {
                LWAException lwaException = new LWAException(IOUtils.toString(error), responseCode);
                throw lwaException;
            } else {
                throw ioException;
            }
        } finally {
            IOUtils.closeQuietly(error);
            IOUtils.closeQuietly(outputStream);
            IOUtils.closeQuietly(response);
        }
    }

    // Helper method used by this class to prepare string representation of JSON request data
    JsonObject prepareExchangeAuthCodeForTokensData(String authCode, String redirectUri, String clientId,
            String codeVerifier) {
        return Json
                .createObjectBuilder()
                        .add(AuthConstants.OAuth2.GRANT_TYPE, AuthConstants.OAuth2.AUTHORIZATION_CODE)
                        .add(AuthConstants.OAuth2.CODE, authCode)
                        .add(AuthConstants.OAuth2.REDIRECT_URI, redirectUri)
                        .add(AuthConstants.OAuth2.CLIENT_ID, clientId)
                        .add(AuthConstants.OAuth2.CODE_VERIFIER, codeVerifier)
                        .build();
    }

    // Helper method used by this class to prepare string representation of JSON request data
    JsonObject prepareExchangeRefreshTokenForTokensData(String refreshToken, String clientId) {
        return Json
                .createObjectBuilder()
                        .add(AuthConstants.OAuth2.GRANT_TYPE, AuthConstants.OAuth2.REFRESH_TOKEN)
                        .add(AuthConstants.OAuth2.CLIENT_ID, clientId)
                        .add(AuthConstants.OAuth2.REFRESH_TOKEN, refreshToken)
                        .build();
    }

}
