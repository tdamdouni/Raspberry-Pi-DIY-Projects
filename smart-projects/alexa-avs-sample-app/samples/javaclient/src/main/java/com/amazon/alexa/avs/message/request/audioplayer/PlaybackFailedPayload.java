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
package com.amazon.alexa.avs.message.request.audioplayer;

import com.amazon.alexa.avs.message.Payload;
import com.amazon.alexa.avs.message.request.context.PlaybackStatePayload;

public final class PlaybackFailedPayload extends Payload {

    private final String token;
    private final PlaybackStatePayload currentPlaybackState;
    private final ErrorStructure error;

    public PlaybackFailedPayload(String token, PlaybackStatePayload playbackState,
            ErrorType errorType) {
        this.token = token;
        this.currentPlaybackState = playbackState;
        error = new ErrorStructure(errorType);

    }

    public String getToken() {
        return token;
    }

    public PlaybackStatePayload getCurrentPlaybackState() {
        return currentPlaybackState;
    }

    public ErrorStructure getError() {
        return error;
    }

    private final static class ErrorStructure {
        private final ErrorType type;
        private final String message;

        public ErrorStructure(ErrorType type) {
            this.type = type;
            this.message = type.getMessage();
        }

        public ErrorType getType() {
            return type;
        }

        public String getMessage() {
            return message;
        }
    }

    public enum ErrorType {
        MEDIA_ERROR_UNKNOWN("An unknown error occurred"),
        MEDIA_ERROR_INVALID_REQUEST(
                "The server recognized the request as being malformed (bad request, unauthorized, forbidden, not found, etc)"),
        MEDIA_ERROR_SERVICE_UNAVAILABLE("The device was unavailable to reach the service"),
        MEDIA_ERROR_INTERNAL_SERVER_ERROR(
                "The server accepted the request, but was unable to process it as expected"),
        MEDIA_ERROR_INTERNAL_DEVICE_ERROR("There was an internal error on the device");

        private final String message;

        private ErrorType(String message) {
            this.message = message;
        }

        public String getMessage() {
            return message;
        }
    }
}
