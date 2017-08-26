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
package com.amazon.alexa.avs.exception;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * This exception is only for exceptions returned from the Server as a System.Exception message
 */
@SuppressWarnings("serial")
public class AlexaSystemException extends AVSException {
    private static final Logger log = LoggerFactory.getLogger(AlexaSystemException.class);
    // Parsed exception code from raw string
    private AlexaSystemExceptionCode exceptionCode;
    // Raw string for the exception code
    private final String rawCode;

    public AlexaSystemException(String code, String description) {
        super(description);
        rawCode = code;
        try {
            this.exceptionCode = AlexaSystemExceptionCode.valueOf(code);
        } catch (IllegalArgumentException e) {
            log.warn(String
                    .format("Received AlexaSystemException with unrecognized code %s.", code));
        }
    }

    @Override
    public String toString() {
        return "" + rawCode + ": " + getMessage();
    }

    public String getDescription() {
        return getMessage();
    }

    public AlexaSystemExceptionCode getExceptionCode() {
        return exceptionCode;
    }
}
