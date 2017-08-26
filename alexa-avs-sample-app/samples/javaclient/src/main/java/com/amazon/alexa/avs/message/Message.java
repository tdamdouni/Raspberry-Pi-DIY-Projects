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
package com.amazon.alexa.avs.message;

import com.amazon.alexa.avs.AVSAPIConstants;
import com.amazon.alexa.avs.config.ObjectMapperFactory;
import com.amazon.alexa.avs.message.Message.MessageDeserializer;
import com.amazon.alexa.avs.message.response.AlexaExceptionResponse;
import com.amazon.alexa.avs.message.response.Directive;

import org.codehaus.jackson.JsonNode;
import org.codehaus.jackson.JsonParseException;
import org.codehaus.jackson.JsonParser;
import org.codehaus.jackson.JsonProcessingException;
import org.codehaus.jackson.annotate.JsonIgnore;
import org.codehaus.jackson.map.DeserializationContext;
import org.codehaus.jackson.map.JsonDeserializer;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectReader;
import org.codehaus.jackson.map.annotate.JsonDeserialize;
import org.codehaus.jackson.node.ObjectNode;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.util.Iterator;
import java.util.Map.Entry;

/**
 * A message from the server. Can be an
 * {@link com.amazon.alexa.avs.message.response.system.Exception Exception},
 * {@link com.amazon.alexa.avs.message.request.Event Event} , or {@link Directive}
 */
@JsonDeserialize(using = MessageDeserializer.class)
public abstract class Message {
    protected Header header;
    protected Payload payload;

    @JsonIgnore
    private String rawMessage;

    protected Message(Header header, JsonNode payload, String rawMessage)
            throws JsonParseException, JsonMappingException, IOException {

        this.header = header;
        try {
            ObjectReader reader = ObjectMapperFactory.getObjectReader();
            Class<?> type = Class.forName(getClass().getPackage().getName() + "."
                    + header.getNamespace().toLowerCase() + "." + header.getName());
            this.payload = (Payload) reader.withType(type).readValue(payload);
        } catch (ClassNotFoundException e) {
            // Default to empty payload
            this.payload = new Payload();
        }

        this.rawMessage = rawMessage;
    }

    protected Message(Header header, Payload payload, String rawMessage) {
        this.header = header;
        this.payload = payload;
        this.rawMessage = rawMessage;
    }

    @JsonIgnore
    public String getName() {
        return header.getName();
    }

    @JsonIgnore
    public String getNamespace() {
        return header.getNamespace();
    }

    public void setHeader(Header header) {
        this.header = header;
    }

    public Header getHeader() {
        return header;
    }

    public void setPayload(Payload payload) {
        this.payload = payload;
    }

    public Payload getPayload() {
        return payload;
    }

    public String getRawMessage() {
        return rawMessage;
    }

    @Override
    public String toString() {
        return header.toString();
    }

    public static class MessageDeserializer extends JsonDeserializer<Message> {
        private static final Logger log = LoggerFactory.getLogger(MessageDeserializer.class);

        @Override
        public Message deserialize(JsonParser jp, DeserializationContext ctx)
                throws IOException, JsonProcessingException {
            ObjectReader reader = ObjectMapperFactory.getObjectReader();
            ObjectNode obj = (ObjectNode) reader.readTree(jp);
            Iterator<Entry<String, JsonNode>> elementsIterator = obj.getFields();

            String rawMessage = obj.toString();

            DialogRequestIdHeader header = null;
            JsonNode payloadNode = null;
            ObjectReader headerReader =
                    ObjectMapperFactory.getObjectReader(DialogRequestIdHeader.class);
            while (elementsIterator.hasNext()) {
                Entry<String, JsonNode> element = elementsIterator.next();
                if (element.getKey().equals("header")) {
                    header = headerReader.readValue(element.getValue());
                }
                if (element.getKey().equals("payload")) {
                    payloadNode = element.getValue();
                }
            }
            if (header == null) {
                throw ctx.mappingException("Missing header");
            }
            if (payloadNode == null) {
                throw ctx.mappingException("Missing payload");
            }

            return createMessage(header, payloadNode, rawMessage);
        }

        private Message createMessage(Header header, JsonNode payload, String rawMessage)
                throws JsonParseException, JsonMappingException, IOException {
            if (AVSAPIConstants.System.NAMESPACE.equals(header.getNamespace())
                    && AVSAPIConstants.System.Exception.NAME.equals(header.getName())) {
                return new AlexaExceptionResponse(header, payload, rawMessage);
            } else {
                return new Directive(header, payload, rawMessage);
            }
        }

    }
}
