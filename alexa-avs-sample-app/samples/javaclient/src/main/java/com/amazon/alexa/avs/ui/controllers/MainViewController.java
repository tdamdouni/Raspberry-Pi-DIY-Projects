/**
 * Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Amazon Software License (the "License"). You may not use this file
 * except in compliance with the License. A copy of the License is located at
 *
 * http://aws.amazon.com/asl/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
 */
package com.amazon.alexa.avs.ui.controllers;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.amazon.alexa.avs.ui.MainUIHandler;

public class MainViewController implements MainUIHandler {
    private static final Logger log = LoggerFactory.getLogger(MainViewController.class);

    private static final String APP_TITLE = "Alexa Voice Service";
    private static final String VERSION_PROPERTIES_FILE = "/res/version.properties";
    private static final String VERSION_KEY = "version";

    @Override
    public String getAppTitle() {
        String version = getAppVersion();
        String title = APP_TITLE;
        if (version != null) {
            title += " - v" + version;
        }
        return title;
    }

    private String getAppVersion() {
        final Properties properties = new Properties();
        try (final InputStream stream = getClass().getResourceAsStream(VERSION_PROPERTIES_FILE)) {
            properties.load(stream);
            if (properties.containsKey(VERSION_KEY)) {
                return properties.getProperty(VERSION_KEY);
            }
        } catch (IOException e) {
            log.warn("version.properties file not found on classpath");
        }
        return null;
    }
}
