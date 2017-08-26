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
package com.amazon.alexa.avs;

import com.amazon.alexa.avs.config.ObjectMapperFactory;

import org.codehaus.jackson.map.ObjectReader;
import org.codehaus.jackson.type.TypeReference;

import java.util.List;

/**
 * A file-backed data store for AVS Alerts
 */
public class AlertsFileDataStore extends FileDataStore<List<Alert>> {
    private static final String ALARM_FILE = "alarms.json";
    private static AlertsFileDataStore sInstance = new AlertsFileDataStore();

    private AlertsFileDataStore() {
        super(ALARM_FILE);
    }

    public synchronized static AlertsFileDataStore getInstance() {
        return sInstance;
    }

    @Override
    public ObjectReader getObjectReader() {
        return ObjectMapperFactory.getObjectReader().withType(new TypeReference<List<Alert>>() {
        });
    }
}
