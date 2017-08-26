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
package com.amazon.alexa.avs.message.response;

import com.amazon.alexa.avs.message.Payload;

import java.io.InputStream;

/**
 * Specify a type of {@link Payload} that references attached audio content via a Content-ID HTTP
 * Header value.
 */
public interface AttachedContentPayload {

    /**
     * Returns whether or not this payload requires content to be attached. False means either it
     * never required content, or that it has content.
     */
    boolean requiresAttachedContent();

    /**
     * Returns whether or not this payload has content attached.
     */
    boolean hasAttachedContent();

    /**
     * Returns the content id for the required attached content.
     */
    String getAttachedContentId();

    /**
     * Returns the attached content.
     */
    InputStream getAttachedContent();

    /**
     * Attaches the given attachment content if the given content id matches the required content
     * id.
     *
     * @param contentId
     *            - content id of attachementContent
     * @param attachmentContent
     *            - content to attach
     */
    void setAttachedContent(String contentId, InputStream attachmentContent);
}
