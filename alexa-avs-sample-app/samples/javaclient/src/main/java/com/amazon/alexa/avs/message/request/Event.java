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
package com.amazon.alexa.avs.message.request;

import com.amazon.alexa.avs.message.Header;
import com.amazon.alexa.avs.message.Message;
import com.amazon.alexa.avs.message.Payload;

import org.apache.commons.lang3.StringUtils;

/**
 * A message from the client to the server
 */
public class Event extends Message {

    public Event(Header header, Payload payload) {
        super(header, payload, StringUtils.EMPTY);
    }
}
