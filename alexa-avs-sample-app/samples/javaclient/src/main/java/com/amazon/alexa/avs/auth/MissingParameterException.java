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
package com.amazon.alexa.avs.auth;

@SuppressWarnings("javadoc")
public class MissingParameterException extends IllegalArgumentException {
    private static final long serialVersionUID = 1L;
    private final String missingParameter;

    public MissingParameterException(String missingParameter) {
        super();
        this.missingParameter = missingParameter;
    }

    @Override
    public String getMessage() {
        return "The following parameter was missing or an empty string: " + this.missingParameter;
    }

    public String getMissingParameter() {
        return this.missingParameter;
    }
}
