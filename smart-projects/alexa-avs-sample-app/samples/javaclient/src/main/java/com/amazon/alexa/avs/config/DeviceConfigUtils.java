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
package com.amazon.alexa.avs.config;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.StringWriter;
import java.util.HashMap;
import java.util.Map;

import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonReader;
import javax.json.JsonWriter;
import javax.json.JsonWriterFactory;
import javax.json.stream.JsonGenerator;

import org.apache.commons.io.IOUtils;

import com.amazon.alexa.avs.config.DeviceConfig.CompanionAppInformation;
import com.amazon.alexa.avs.config.DeviceConfig.CompanionServiceInformation;

/**
 * A utility class for interacting with the config file. This class is used for creating
 * {@link DeviceConfig}, and also for persisting changes.
 *
 * @see DeviceConfig
 */
public final class DeviceConfigUtils {
    private static String deviceConfigName = DeviceConfig.FILE_NAME;

    /**
     * Reads the {@link DeviceConfig} from disk.
     *
     * @return The configuration.
     */
    public static DeviceConfig readConfigFile() {
        return readConfigFile(DeviceConfig.FILE_NAME);
    }

    /**
     * Reads the {@link DeviceConfig} from disk. Pass in the name of the config file
     *
     * @return The configuration.
     */
    public static DeviceConfig readConfigFile(String filename) {
        FileInputStream file = null;
        try {
            deviceConfigName = filename.trim();
            file = new FileInputStream(deviceConfigName);
            JsonReader json = Json.createReader(file);
            JsonObject configObject = json.readObject();

            JsonObject companionServiceObject =
                    configObject.getJsonObject(DeviceConfig.COMPANION_SERVICE);
            CompanionServiceInformation companionServiceInfo = null;
            if (companionServiceObject != null) {
                String serviceUrl = companionServiceObject
                        .getString(DeviceConfig.CompanionServiceInformation.SERVICE_URL, null);
                String sessionId = companionServiceObject
                        .getString(DeviceConfig.CompanionServiceInformation.SESSION_ID, null);
                String sslClientKeyStore = companionServiceObject.getString(
                        DeviceConfig.CompanionServiceInformation.SSL_CLIENT_KEYSTORE, null);
                String sslClientKeyStorePassphrase = companionServiceObject.getString(
                        DeviceConfig.CompanionServiceInformation.SSL_CLIENT_KEYSTORE_PASSPHRASE,
                        null);
                String sslCaCert = companionServiceObject
                        .getString(DeviceConfig.CompanionServiceInformation.SSL_CA_CERT, null);

                companionServiceInfo = new CompanionServiceInformation(serviceUrl,
                        sslClientKeyStore, sslClientKeyStorePassphrase, sslCaCert);
                companionServiceInfo.setSessionId(sessionId);
            }

            JsonObject companionAppObject = configObject.getJsonObject(DeviceConfig.COMPANION_APP);
            CompanionAppInformation companionAppInfo = null;
            if (companionAppObject != null) {
                int localPort = companionAppObject
                        .getInt(DeviceConfig.CompanionAppInformation.LOCAL_PORT, -1);
                String lwaUrl = companionAppObject
                        .getString(DeviceConfig.CompanionAppInformation.LWA_URL, null);
                String clientId = companionAppObject
                        .getString(DeviceConfig.CompanionAppInformation.CLIENT_ID, null);
                String refreshToken = companionAppObject
                        .getString(DeviceConfig.CompanionAppInformation.REFRESH_TOKEN, null);
                String sslKeyStore = companionAppObject
                        .getString(DeviceConfig.CompanionAppInformation.SSL_KEYSTORE, null);
                String sslKeyStorePassphrase = companionAppObject.getString(
                        DeviceConfig.CompanionAppInformation.SSL_KEYSTORE_PASSPHRASE, null);

                companionAppInfo = new CompanionAppInformation(localPort, lwaUrl, sslKeyStore,
                        sslKeyStorePassphrase);
                companionAppInfo.setClientId(clientId);
                companionAppInfo.setRefreshToken(refreshToken);
            }

            String productId = configObject.getString(DeviceConfig.PRODUCT_ID, null);
            String dsn = configObject.getString(DeviceConfig.DSN, null);
            String provisioningMethod =
                    configObject.getString(DeviceConfig.PROVISIONING_METHOD, null);
            String avsHost = configObject.getString(DeviceConfig.AVS_HOST, null);
            boolean wakeWordAgentEnabled = configObject.getBoolean(DeviceConfig.WAKE_WORD_AGENT_ENABLED, false);
            boolean headlessModeEnabled = configObject.getBoolean(DeviceConfig.HEADLESS, false);
            String locale = configObject.getString(DeviceConfig.LOCALE, null);

            DeviceConfig deviceConfig = new DeviceConfig(productId, dsn, provisioningMethod,
                    wakeWordAgentEnabled, headlessModeEnabled, locale, companionAppInfo,
                    companionServiceInfo, avsHost);

            return deviceConfig;
        } catch (FileNotFoundException e) {
            throw new RuntimeException(
                    "The required file " + deviceConfigName + " could not be opened.", e);
        } finally {
            IOUtils.closeQuietly(file);
        }
    }

    /**
     * Writes the {@link DeviceConfig} back to disk.
     *
     * @param config
     */
    public static void updateConfigFile(DeviceConfig config) {
        FileOutputStream file = null;
        try {
            file = new FileOutputStream(deviceConfigName);
            StringWriter stringWriter = new StringWriter();

            Map<String, Object> properties = new HashMap<String, Object>(1);
            properties.put(JsonGenerator.PRETTY_PRINTING, true);

            JsonWriterFactory writerFactory = Json.createWriterFactory(properties);
            JsonWriter jsonWriter = writerFactory.createWriter(stringWriter);
            jsonWriter.writeObject(config.toJson());
            jsonWriter.close();

            // We have to write to a separate StringWriter and trim() it because the pretty-printing
            // generator adds a newline at the beginning of the file.
            file.write(stringWriter.toString().trim().getBytes());
        } catch (FileNotFoundException e) {
            throw new RuntimeException(
                    "The required file " + deviceConfigName + " could not be updated.", e);
        } catch (IOException e) {
            throw new RuntimeException(
                    "The required file " + deviceConfigName + " could not be updated.", e);
        } finally {
            IOUtils.closeQuietly(file);
        }
    }

}
