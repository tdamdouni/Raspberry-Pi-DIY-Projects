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
package com.amazon.alexa.avs.http;

import com.amazon.alexa.avs.config.ObjectMapperFactory;
import com.amazon.alexa.avs.exception.AVSJsonProcessingException;
import com.amazon.alexa.avs.message.Message;

import org.codehaus.jackson.JsonProcessingException;
import org.codehaus.jackson.map.ObjectReader;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;

public class MessageParser {
    private static final Logger log = LoggerFactory.getLogger(MessageParser.class);

    /**
     * Parses a single valid Message in the given byte array
     *
     * @return Message if the bytes composed a valid Message
     * @throws IOException
     *             Directive parsing failed
     */
    protected Message parseServerMessage(byte[] bytes) throws IOException {
        return parse(bytes, Message.class);
    }

    protected <T> T parse(byte[] bytes, Class<T> clazz) throws IOException {
        try {
            ObjectReader reader = ObjectMapperFactory.getObjectReader();
            Object logBody = reader.withType(Object.class).readValue(bytes);
            log.info("Response metadata: \n{}", ObjectMapperFactory
                    .getObjectWriter()
                    .withDefaultPrettyPrinter()
                    .writeValueAsString(logBody));
            return reader.withType(clazz).readValue(bytes);
        } catch (JsonProcessingException e) {
            String unparseable = new String(bytes, "UTF-8");
            throw new AVSJsonProcessingException(
                    String.format("Failed to parse a %1$s", clazz.getSimpleName()), e, unparseable);
        }
    }
}
