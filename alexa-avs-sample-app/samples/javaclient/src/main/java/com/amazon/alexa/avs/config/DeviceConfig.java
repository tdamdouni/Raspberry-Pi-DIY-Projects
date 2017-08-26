/**
 * Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
package com.amazon.alexa.avs.config;

import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonObjectBuilder;

import org.apache.commons.lang3.StringUtils;

/**
 * Container that encapsulates all the information that exists in the config file.
 */
public class DeviceConfig {
    private static final String DEFAULT_HOST = "https://avs-alexa-na.amazon.com";
    public static final String FILE_NAME = "config.json";
    private static final List<Locale> SUPPORTED_LOCALES = new ArrayList<>();
    static {
        SUPPORTED_LOCALES.add(Locale.US);
        SUPPORTED_LOCALES.add(Locale.UK);
        SUPPORTED_LOCALES.add(Locale.GERMANY);
    }

    public static final String PRODUCT_ID = "productId";
    public static final String DSN = "dsn";
    public static final String COMPANION_APP = "companionApp";
    public static final String COMPANION_SERVICE = "companionService";
    public static final String PROVISIONING_METHOD = "provisioningMethod";
    public static final String AVS_HOST = "avsHost";
    public static final String WAKE_WORD_AGENT_ENABLED = "wakeWordAgentEnabled";
    public static final String LOCALE = "locale";
    public static final String HEADLESS = "headless";

    /*
     * Required parameters from the config file.
     */
    private final String productId;
    private final String dsn;
    private final ProvisioningMethod provisioningMethod;
    private URL avsHost;
    private Locale locale;

    /*
     * Optional parameters from the config file.
     */
    private CompanionAppInformation companionAppInfo;
    private CompanionServiceInformation companionServiceInfo;
    private boolean wakeWordAgentEnabled;
    private boolean headlessModeEnabled;

    @SuppressWarnings("javadoc")
    public enum ProvisioningMethod {
        COMPANION_APP(DeviceConfig.COMPANION_APP),
        COMPANION_SERVICE(DeviceConfig.COMPANION_SERVICE);

        private String name;

        ProvisioningMethod(String name) {
            this.name = name;
        }

        @Override
        public String toString() {
            return name;
        }

        public static ProvisioningMethod fromString(String method) {
            if (ProvisioningMethod.COMPANION_APP.toString().equals(method)) {
                return COMPANION_APP;
            } else if (ProvisioningMethod.COMPANION_SERVICE.toString().equals(method)) {
                return COMPANION_SERVICE;
            }
            throw new IllegalArgumentException("Invalid provisioning method");
        }
    }

    /**
     * Creates a {@link DeviceConfig} object.
     *
     * @param productId
     *            The productId of this device.
     * @param dsn
     *            The dsn of this device.
     * @param provisioningMethod
     *            The provisioningMethod to use. One of: {@value #COMPANION_APP},
     *            {@value #COMPANION_SERVICE}
     * @param wakeWordAgentEnabled
     *            Whether the wake word agent functionality is enabled.
     * @param headlessModeEnabled
     *            Whether to launch the app in the terminal or as a GUI application.
     * @param languageTag
     *            The language tag representing the locale to initialize the app with.
     * @param companionAppInfo
     *            The information necessary for the Companion App method of provisioning.
     * @param companionServiceInfo
     *            The information necessary for the Companion Service method of provisioning.
     * @param avsHost
     *            (optional) AVS host override
     */
    public DeviceConfig(String productId, String dsn, String provisioningMethod,
            boolean wakeWordAgentEnabled, boolean headlessModeEnabled, String languageTag,
            CompanionAppInformation companionAppInfo,
            CompanionServiceInformation companionServiceInfo, String avsHost) {

        if (StringUtils.isBlank(productId)) {
            throw new MalformedConfigException(PRODUCT_ID + " is blank in your config file.");
        }

        if (StringUtils.isBlank(dsn)) {
            throw new MalformedConfigException(DSN + " is blank in your config file.");
        }

        if (StringUtils.isBlank(languageTag)) {
            throw new MalformedConfigException(
                    LOCALE + " is blank in your config file. Supported locales are: "
                            + getSupportedLocalesLanguageTag());
        }

        Locale locale = Locale.forLanguageTag(languageTag);
        if (!SUPPORTED_LOCALES.contains(locale)) {
            throw new MalformedConfigException(LOCALE + ": " + languageTag
                    + " is not a supported locale. Supported locales are: "
                    + getSupportedLocalesLanguageTag());
        }

        ProvisioningMethod method;
        try {
            method = ProvisioningMethod.fromString(provisioningMethod);
        } catch (IllegalArgumentException e) {
            throw new MalformedConfigException(PROVISIONING_METHOD + " should be either \""
                    + COMPANION_APP + "\" or \"" + COMPANION_SERVICE + "\".");
        }

        if (method == ProvisioningMethod.COMPANION_APP
                && (companionAppInfo == null || !companionAppInfo.isValid())) {
            throw new MalformedConfigException("Your " + PROVISIONING_METHOD + " is set to \""
                    + COMPANION_APP + "\" but you do not have a valid \"" + COMPANION_APP
                    + "\" section in your config file.");
        } else if (method == ProvisioningMethod.COMPANION_SERVICE
                && (companionServiceInfo == null || !companionServiceInfo.isValid())) {
            throw new MalformedConfigException("Your " + PROVISIONING_METHOD + " is set to \""
                    + COMPANION_SERVICE + "\" but you do not have a valid \"" + COMPANION_SERVICE
                    + "\" section in your config file.");
        }

        this.provisioningMethod = method;
        this.productId = productId;
        this.dsn = dsn;
        this.locale = locale;
        this.companionServiceInfo = companionServiceInfo;
        this.companionAppInfo = companionAppInfo;
        avsHost = StringUtils.isBlank(avsHost) ? DEFAULT_HOST : avsHost;
        try {
            this.avsHost = new URL(avsHost);
        } catch (MalformedURLException e) {
            throw new MalformedConfigException(AVS_HOST + " is malformed in your config file.", e);
        }

        this.wakeWordAgentEnabled = wakeWordAgentEnabled;
        this.headlessModeEnabled = headlessModeEnabled;
    }

    public DeviceConfig(String productId, String dsn, String provisioningMethod,
            boolean wakeWordAgentEnabled, boolean headlessModeEnabled, String languageTag,
            CompanionAppInformation companionAppInfo,
            CompanionServiceInformation companionServiceInfo) {
        this(productId, dsn, provisioningMethod, wakeWordAgentEnabled, headlessModeEnabled,
                languageTag, companionAppInfo, companionServiceInfo, DEFAULT_HOST);
    }

    /**
     * Get the Alexa Voice Service URL.
     *
     * @return URL for making requests to Alexa Voice Service.
     */
    public URL getAvsHost() {
        return avsHost;
    }

    /**
     * Set the Alexa Voice Service URL.
     *
     * @param url
     *            the base URL to be used for making requests to Alexa Voice Service.
     */
    public void setAvsHost(URL url) {
        avsHost = url;
    }

    /**
     * @return productId.
     */
    public String getProductId() {
        return productId;
    }

    /**
     * @return dsn.
     */
    public String getDsn() {
        return dsn;
    }

    /**
     * @return provisioningMethod.
     */
    public ProvisioningMethod getProvisioningMethod() {
        return provisioningMethod;
    }

    /**
     * @return companionAppInfo.
     */
    public CompanionAppInformation getCompanionAppInfo() {
        return companionAppInfo;
    }

    /**
     * @return wakeWordAgentEnabled.
     */
    public boolean getWakeWordAgentEnabled() {
        return wakeWordAgentEnabled;
    }

    /**
     * @return headlessModeEnabled.
     */
    public boolean getHeadlessModeEnabled() {
        return headlessModeEnabled;
    }

    /**
     * @return locale
     */
    public Locale getLocale() {
        return locale;
    }

    /**
     * Set the locale.
     *
     * @param locale
     */
    public void setLocale(Locale locale) {
        if (!SUPPORTED_LOCALES.contains(locale)) {
            throw new IllegalArgumentException(
                    "Locale " + locale + " is not supported. Supported locales are: "
                            + getSupportedLocalesLanguageTag());
        }
        this.locale = locale;
    }

    /**
     * Get the Supported Locales as a language tag
     *
     * @return List of LanguageTags
     */
    public List<String> getSupportedLocalesLanguageTag() {
        return SUPPORTED_LOCALES.stream().map(Locale::toLanguageTag).collect(Collectors.toList());
    }

    /**
     * @param companionAppInfo
     */
    public void setCompanionAppInfo(CompanionAppInformation companionAppInfo) {
        this.companionAppInfo = companionAppInfo;
    }

    /**
     * @return companionServiceInfo.
     */
    public CompanionServiceInformation getCompanionServiceInfo() {
        return companionServiceInfo;
    }

    /**
     * @param companionServiceInfo
     */
    public void setCompanionServiceInfo(CompanionServiceInformation companionServiceInfo) {
        this.companionServiceInfo = companionServiceInfo;
    }

    /**
     * Save this file back to disk.
     */
    public void saveConfig() {
        DeviceConfigUtils.updateConfigFile(this);
    }

    /**
     * Serialize this object to JSON.
     *
     * @return A JSON representation of this object.
     */
    public JsonObject toJson() {

        JsonObjectBuilder builder = Json
                .createObjectBuilder()
                .add(PRODUCT_ID, productId)
                .add(DSN, dsn)
                .add(PROVISIONING_METHOD, provisioningMethod.toString())
                .add(WAKE_WORD_AGENT_ENABLED, wakeWordAgentEnabled)
                .add(HEADLESS, headlessModeEnabled)
                .add(LOCALE, locale.toLanguageTag())
                .add(AVS_HOST, avsHost.toString());

        if (companionAppInfo != null) {
            builder.add(COMPANION_APP, companionAppInfo.toJson());
        }

        if (companionServiceInfo != null) {
            builder.add(COMPANION_SERVICE, companionServiceInfo.toJson());
        }

        return builder.build();
    }

    /**
     * Describes the information necessary for the Companion App method of provisioning.
     */
    public static class CompanionAppInformation {
        public static final String LOCAL_PORT = "localPort";
        public static final String LWA_URL = "lwaUrl";
        public static final String SSL_KEYSTORE = "sslKeyStore";
        public static final String SSL_KEYSTORE_PASSPHRASE = "sslKeyStorePassphrase";
        public static final String REFRESH_TOKEN = "refreshToken";
        public static final String CLIENT_ID = "clientId";

        private final int localPort;
        private final String lwaUrl;
        private final String sslKeyStore;
        private final String sslKeyStorePassphrase;

        private URL loginWithAmazonUrl;
        private String clientId;

        /**
         * This is a field that represents the OAuth refresh token. Please note that this token
         * represents persistent authorization on the client side, and should be treated with care.
         * This implementation will store this value on disk. For a production deployment of this
         * code, a more secure method of storing this data is strongly recommended.
         */
        private String refreshToken;

        /**
         * Creates a {@link CompanionAppInformation} object.
         *
         * @param localPort
         * @param lwaUrl
         */
        public CompanionAppInformation(int localPort, String lwaUrl, String sslKeyStore,
                String sslKeyStorePassphrase) {
            this.localPort = localPort;
            this.sslKeyStore = sslKeyStore;
            this.sslKeyStorePassphrase = sslKeyStorePassphrase;
            this.lwaUrl = lwaUrl;
        }

        /**
         * @return clientId.
         */
        public String getClientId() {
            return clientId;
        }

        /**
         * @param clientId
         */
        public void setClientId(String clientId) {
            this.clientId = clientId;
        }

        /**
         * This is an accessor for the OAuth refresh token. Please note that this token represents
         * persistent authorization on the client side, and should be treated with care. This
         * implementation will store this value on disk. For a production deployment of this code, a
         * more secure method of storing this data is strongly recommended.
         *
         * @return refreshToken.
         */
        public String getRefreshToken() {
            return refreshToken;
        }

        /**
         * @param refreshToken
         */
        public void setRefreshToken(String refreshToken) {
            this.refreshToken = refreshToken;
        }

        /**
         * @return localPort.
         */
        public int getLocalPort() {
            return localPort;
        }

        /**
         * @return lwaUrl.
         */
        public URL getLwaUrl() {
            if (loginWithAmazonUrl == null) {
                if (StringUtils.isBlank(lwaUrl)) {
                    throw new MalformedConfigException(LWA_URL + " is blank in your config file.");
                } else {
                    try {
                        loginWithAmazonUrl = new URL(lwaUrl);
                    } catch (MalformedURLException e) {
                        throw new MalformedConfigException(
                                LWA_URL + " is malformed in your config file.", e);
                    }
                }
            }
            return loginWithAmazonUrl;
        }

        /**
         * @return sslKeyStore.
         */
        public String getSslKeyStore() {
            return sslKeyStore;
        }

        /**
         * @return sslKeyStorePassphrase.
         */
        public String getSslKeyStorePassphrase() {
            return sslKeyStorePassphrase;
        }

        /**
         * Serialize this object to JSON.
         *
         * @return A JSON representation of this object.
         */
        public JsonObject toJson() {
            JsonObjectBuilder builder = Json
                    .createObjectBuilder()
                    .add(LOCAL_PORT, localPort)
                    .add(LWA_URL, getLwaUrl().toString())
                    .add(SSL_KEYSTORE, sslKeyStore)
                    .add(SSL_KEYSTORE_PASSPHRASE, sslKeyStorePassphrase);

            if ((clientId != null) && (refreshToken != null)) {
                builder.add(CLIENT_ID, clientId);
                builder.add(REFRESH_TOKEN, refreshToken);
            }

            return builder.build();
        }

        public boolean isValid() {
            if (localPort < 1 || localPort > 65535) {
                throw new MalformedConfigException(
                        LOCAL_PORT + " is invalid. Value port values are 1-65535.");
            }

            getLwaUrl(); // Verifies that the url is valid
            if (StringUtils.isBlank(sslKeyStore)) {
                throw new MalformedConfigException(SSL_KEYSTORE + " is blank in your config file.");
            } else {
                File sslKeyStoreFile = new File(sslKeyStore);
                if (!sslKeyStoreFile.exists()) {
                    throw new MalformedConfigException(
                            sslKeyStore + " " + SSL_KEYSTORE + " does not exist.");
                }
            }
            return true;
        }
    }

    /**
     * Describes the information necessary for the Companion Service method of provisioning.
     */
    public static class CompanionServiceInformation {
        public static final String SESSION_ID = "sessionId";
        public static final String SERVICE_URL = "serviceUrl";
        public static final String SSL_CLIENT_KEYSTORE = "sslClientKeyStore";
        public static final String SSL_CLIENT_KEYSTORE_PASSPHRASE = "sslClientKeyStorePassphrase";
        public static final String SSL_CA_CERT = "sslCaCert";

        private final String serviceUrlString;
        private final String sslClientKeyStore;
        private final String sslClientKeyStorePassphrase;
        private final String sslCaCert;

        private URL serviceUrl;
        private String sessionId;

        /**
         * Creates a {@link CompanionServiceInformation} object.
         *
         * @param serviceUrl
         */
        public CompanionServiceInformation(String serviceUrl, String sslClientKeyStore,
                String sslClientKeyStorePassphrase, String sslCaCert) {
            this.serviceUrlString = serviceUrl;
            this.sslClientKeyStore = sslClientKeyStore;
            this.sslClientKeyStorePassphrase = sslClientKeyStorePassphrase;
            this.sslCaCert = sslCaCert;
        }

        /**
         * @return serviceUrl.
         */
        public URL getServiceUrl() {
            if (serviceUrl == null) {
                if (StringUtils.isBlank(serviceUrlString)) {
                    throw new MalformedConfigException(
                            SERVICE_URL + " is blank in your config file.");
                } else {
                    try {
                        this.serviceUrl = new URL(serviceUrlString);
                    } catch (MalformedURLException e) {
                        throw new MalformedConfigException(
                                SERVICE_URL + " is malformed in your config file.", e);
                    }
                }
            }
            return serviceUrl;
        }

        /**
         * @param sessionId
         */
        public void setSessionId(String sessionId) {
            this.sessionId = sessionId;
        }

        /**
         * @return sessionId.
         */
        public String getSessionId() {
            return sessionId;
        }

        /**
         * @return sslClientKeyStore.
         */
        public String getSslClientKeyStore() {
            return sslClientKeyStore;
        }

        /**
         * @return sslClientKeyStorePassphrase.
         */
        public String getSslClientKeyStorePassphrase() {
            return sslClientKeyStorePassphrase;
        }

        /**
         * @return sslCaCert.
         */
        public String getSslCaCert() {
            return sslCaCert;
        }

        /**
         * Serialize this object to JSON.
         *
         * @return A JSON representation of this object.
         */
        public JsonObject toJson() {
            JsonObjectBuilder builder = Json
                    .createObjectBuilder()
                    .add(SERVICE_URL, getServiceUrl().toString())
                    .add(SSL_CLIENT_KEYSTORE, sslClientKeyStore)
                    .add(SSL_CLIENT_KEYSTORE_PASSPHRASE, sslClientKeyStorePassphrase)
                    .add(SSL_CA_CERT, sslCaCert);

            if (sessionId != null) {
                builder.add(SESSION_ID, sessionId);
            }

            return builder.build();
        }

        public boolean isValid() {
            getServiceUrl(); // Verifies that the URL is valid
            if (StringUtils.isBlank(sslClientKeyStore)) {
                throw new MalformedConfigException(
                        SSL_CLIENT_KEYSTORE + " is blank in your config file.");
            } else {
                File sslClientKeyStoreFile = new File(sslClientKeyStore);
                if (!sslClientKeyStoreFile.exists()) {
                    throw new MalformedConfigException(
                            sslClientKeyStore + " " + SSL_CLIENT_KEYSTORE + " does not exist.");
                }
            }

            if (StringUtils.isBlank(sslCaCert)) {
                throw new MalformedConfigException(SSL_CA_CERT + " is blank in your config file.");
            } else {
                File sslCaCertFile = new File(sslCaCert);
                if (!sslCaCertFile.exists()) {
                    throw new MalformedConfigException(
                            sslCaCertFile + " " + SSL_CA_CERT + " does not exist.");
                }
            }
            return true;
        }
    }

    @SuppressWarnings("javadoc")
    public static class MalformedConfigException extends RuntimeException {
        private static final long serialVersionUID = 1L;

        public MalformedConfigException(String message, Throwable cause) {
            super(message, cause);
        }

        public MalformedConfigException(String s) {
            super(s);
        }
    }
}

