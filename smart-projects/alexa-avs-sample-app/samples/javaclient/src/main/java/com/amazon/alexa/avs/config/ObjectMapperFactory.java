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

import org.codehaus.jackson.map.DeserializationConfig;
import org.codehaus.jackson.map.ObjectMapper;
import org.codehaus.jackson.map.ObjectReader;
import org.codehaus.jackson.map.ObjectWriter;

public class ObjectMapperFactory {
    private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper()
            .configure(DeserializationConfig.Feature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    private static final ObjectWriter OBJECT_WRITER = OBJECT_MAPPER.writer();
    private static final ObjectReader OBJECT_READER = OBJECT_MAPPER.reader();

    private ObjectMapperFactory() {
    }

    /**
     *
     * @return A generic object reader
     */
    public static ObjectReader getObjectReader() {
        return OBJECT_READER;
    }

    /**
     * Get an ObjectReader that can parse JSON to type clazz
     *
     * @param clazz
     *            Type of class to parse the JSON into
     * @return
     */
    public static ObjectReader getObjectReader(Class<?> clazz) {
        return OBJECT_READER.withType(clazz);
    }

    public static ObjectWriter getObjectWriter() {
        return OBJECT_WRITER;
    }
}
