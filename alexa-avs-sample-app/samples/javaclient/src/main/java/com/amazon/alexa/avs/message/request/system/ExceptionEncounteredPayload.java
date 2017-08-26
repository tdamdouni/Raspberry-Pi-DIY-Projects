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
package com.amazon.alexa.avs.message.request.system;

import com.amazon.alexa.avs.exception.DirectiveHandlingException.ExceptionType;
import com.amazon.alexa.avs.message.Payload;

public class ExceptionEncounteredPayload extends Payload {

    private String unparsedDirective;
    private ErrorStructure error;

    public ExceptionEncounteredPayload(String unparsedDirective, ExceptionType type, String message) {
        this.unparsedDirective = unparsedDirective;
        error = new ErrorStructure(type, message);
    }

    public String getUnparsedDirective() {
        return unparsedDirective;
    }

    public ErrorStructure getError() {
        return error;
    }

    private static class ErrorStructure {
        private ExceptionType type;
        private String message;

        public ErrorStructure(ExceptionType type, String message) {
            this.type = type;
            this.message = message;
        }

        public ExceptionType getType() {
            return type;
        }

        public String getMessage() {
            return message;
        }
    }
}
