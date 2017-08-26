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

import com.amazon.alexa.avs.auth.AuthConstants;
import com.amazon.alexa.avs.auth.OAuth2AccessToken;
import com.amazon.alexa.avs.auth.companionapp.CompanionAppProvisioningInfo;
import com.amazon.alexa.avs.config.DeviceConfig;

import org.apache.commons.io.IOUtils;
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.ByteArrayInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.security.KeyManagementException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.UnrecoverableKeyException;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;
import java.util.HashMap;
import java.util.Map;

import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonReader;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.KeyManagerFactory;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSocketFactory;
import javax.net.ssl.TrustManagerFactory;

/**
 * Client for communicating with the companion service and exchanging information for provisioning.
 */
public class CompanionServiceClient {

    private final DeviceConfig deviceConfig;
    private SSLSocketFactory pinnedSSLSocketFactory;

    private static final Logger log = LoggerFactory.getLogger(CompanionServiceClient.class);

    /**
     * Creates an {@link CompanionServiceClient} object.
     *
     * @param deviceConfig
     */
    public CompanionServiceClient(DeviceConfig deviceConfig) {
        this.deviceConfig = deviceConfig;
        this.pinnedSSLSocketFactory = getPinnedSSLSocketFactory();
    }

    /**
     * Creates an {@link CompanionServiceClient} object.
     *
     * @param deviceConfig
     * @param sslSocketFactory
     */
    protected CompanionServiceClient(DeviceConfig deviceConfig, SSLSocketFactory sslSocketFactory) {
        this.deviceConfig = deviceConfig;
        this.pinnedSSLSocketFactory = sslSocketFactory;
    }

    /**
     * Loads the CA certificate into an in-memory keystore and creates an {@link SSLSocketFactory}.
     *
     * @return SSLSocketFactory
     */
    public SSLSocketFactory getPinnedSSLSocketFactory() {
        InputStream caCertInputStream = null;
        InputStream clientKeyPair = null;
        try {
            // Load the CA certificate into memory
            CertificateFactory cf = CertificateFactory.getInstance("X.509");
            caCertInputStream =
                    new FileInputStream(deviceConfig.getCompanionServiceInfo().getSslCaCert());
            Certificate caCert = cf.generateCertificate(caCertInputStream);

            // Load the CA certificate into the trusted KeyStore
            KeyStore trustStore = KeyStore.getInstance(KeyStore.getDefaultType());
            trustStore.load(null, null);
            trustStore.setCertificateEntry("myca", caCert);

            // Create a TrustManagerFactory with the trusted KeyStore
            TrustManagerFactory trustManagerFactory =
                    TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
            trustManagerFactory.init(trustStore);

            // Load the client certificate and private key into another KeyStore
            KeyStore keyStore = KeyStore.getInstance("PKCS12");
            clientKeyPair = new FileInputStream(
                    deviceConfig.getCompanionServiceInfo().getSslClientKeyStore());
            keyStore.load(clientKeyPair, deviceConfig
                    .getCompanionServiceInfo()
                    .getSslClientKeyStorePassphrase()
                    .toCharArray());

            // Create a TrustManagerFactory with the client key pair KeyStore
            KeyManagerFactory keyManagerFactory =
                    KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm());
            keyManagerFactory.init(keyStore, deviceConfig
                    .getCompanionServiceInfo()
                    .getSslClientKeyStorePassphrase()
                    .toCharArray());

            // Initialize the SSLContext and return an SSLSocketFactory;
            SSLContext sc = SSLContext.getInstance("TLS");
            sc.init(keyManagerFactory.getKeyManagers(), trustManagerFactory.getTrustManagers(),
                    null);

            return sc.getSocketFactory();
        } catch (CertificateException | KeyStoreException | UnrecoverableKeyException
                | NoSuchAlgorithmException | IOException | KeyManagementException e) {
            throw new RuntimeException(
                    "The KeyStore for contacting the Companion Service could not be loaded.", e);
        } finally {
            IOUtils.closeQuietly(caCertInputStream);
            IOUtils.closeQuietly(clientKeyPair);
        }
    }

    /**
     * Send the device's provisioning information to the companion service, and receive back
     * {@link CompanionServiceRegCodeResponse} which has a regCode to display to the user.
     *
     * @return Information from the companion service to begin the provisioning process.
     * @throws IOException
     *             If an I/O exception occurs.
     */
    public CompanionServiceRegCodeResponse getRegistrationCode() throws IOException {
        Map<String, String> queryParameters = new HashMap<>();
        queryParameters.put(AuthConstants.PRODUCT_ID, deviceConfig.getProductId());
        queryParameters.put(AuthConstants.DSN, deviceConfig.getDsn());

        JsonObject response = callService("/provision/regCode", queryParameters);

        // The sessionId created from the 3pService
        String sessionId = response.getString(AuthConstants.SESSION_ID, null);
        String regCode = response.getString(AuthConstants.REG_CODE, null);

        return new CompanionServiceRegCodeResponse(sessionId, regCode);
    }

    /**
     * Request the companion service's information once the user has registered. Once the user has
     * registered and we've received the {@link CompanionAppProvisioningInfo} we can then exchange
     * that information for tokens.
     *
     * @param sessionId
     * @return accessToken
     * @throws IOException
     *             If an I/O exception occurs.
     */
    public OAuth2AccessToken getAccessToken(String sessionId) throws IOException {
        Map<String, String> queryParameters = new HashMap<>();
        queryParameters.put(AuthConstants.SESSION_ID, sessionId);

        JsonObject response = callService("/provision/accessToken", queryParameters);

        String accessToken = response.getString(AuthConstants.OAuth2.ACCESS_TOKEN, null);
        int expiresIn = response.getInt(AuthConstants.OAuth2.EXPIRES_IN, -1);

        return new OAuth2AccessToken(accessToken, expiresIn);
    }

    public boolean revokeAccessToken(String sessionId) throws IOException {
        Map<String, String> queryParameters = new HashMap<>();
        queryParameters.put(AuthConstants.SESSION_ID, sessionId);

        JsonObject response = callService("/provision/revokeToken", queryParameters);

        return response.getBoolean(AuthConstants.LOGOUT_SUCCESS, false);
    }

    JsonObject callService(String path, Map<String, String> parameters) throws IOException {
        HttpURLConnection con = null;
        InputStream response = null;
        try {
            String queryString = mapToQueryString(parameters);
            URL obj = new URL(deviceConfig.getCompanionServiceInfo().getServiceUrl(),
                    path + queryString);
            con = (HttpURLConnection) obj.openConnection();

            if (con instanceof HttpsURLConnection) {
                ((HttpsURLConnection) con).setSSLSocketFactory(pinnedSSLSocketFactory);
            }

            con.setRequestProperty("Content-Type", "application/json");
            con.setRequestMethod("GET");

            if ((con.getResponseCode() >= 200) || (con.getResponseCode() < 300)) {
                response = con.getInputStream();
            }

            if (response != null) {
                String responsestring = IOUtils.toString(response);
                JsonReader reader = Json
                        .createReader(new ByteArrayInputStream(responsestring.getBytes(StandardCharsets.UTF_8)));
                IOUtils.closeQuietly(response);
                return reader.readObject();
            }
            return Json.createObjectBuilder().build();
        } catch (IOException e) {
            if (con != null) {
                response = con.getErrorStream();

                if (response != null) {
                    String responsestring = IOUtils.toString(response);
                    JsonReader reader = Json.createReader(
                            new ByteArrayInputStream(responsestring.getBytes(StandardCharsets.UTF_8)));
                    JsonObject error = reader.readObject();

                    String errorName = error.getString("error", null);
                    String errorMessage = error.getString("message", null);

                    if (!StringUtils.isBlank(errorName) && !StringUtils.isBlank(errorMessage)) {
                        throw new RemoteServiceException(errorName + ": " + errorMessage);
                    }
                }
            }
            throw e;
        } finally {
            if (response != null) {
                IOUtils.closeQuietly(response);
            }
        }
    }

    private String mapToQueryString(Map<String, String> parameters)
            throws UnsupportedEncodingException {
        StringBuilder queryBuilder = new StringBuilder();
        if ((parameters != null) && (parameters.size() > 0)) {
            queryBuilder.append("?");
            for (Map.Entry<String, String> entry : parameters.entrySet()) {
                if (queryBuilder.length() > 1) {
                    queryBuilder.append("&");
                }
                queryBuilder.append(URLEncoder.encode(entry.getKey().toString(),
                        StandardCharsets.UTF_8.name()));
                queryBuilder.append("=");
                queryBuilder.append(URLEncoder.encode(entry.getValue().toString(),
                        StandardCharsets.UTF_8.name()));
            }
        }
        return queryBuilder.toString();
    }

    @SuppressWarnings("javadoc")
    public static class RemoteServiceException extends RuntimeException {
        private static final long serialVersionUID = 1L;

        public RemoteServiceException(String s) {
            super(s);
        }
    }

}
