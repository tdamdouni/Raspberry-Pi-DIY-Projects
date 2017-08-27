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
package com.amazon.alexa.avs.message.response.system;

import com.amazon.alexa.avs.message.Payload;

/**
 * A directive representing an instruction for the client to change the
 * endpoint it uses for making request to Alexa Voice Service.
 */
public class SetEndpoint extends Payload {

    private String endpoint;

    /**
     * Set the endpoint on the payload.
     * 
     * @param endpoint
     *            The string to set as the endpoint on the payload.
     */
    public void setEndpoint(String endpoint) {
        this.endpoint = endpoint;
    }

    /**
     * Get the new Alexa Voice Service endpoint.
     * 
     * @return A string for the new AVS endpoint.
     */
    public String getEndpoint() {
        return endpoint;
    }

}
