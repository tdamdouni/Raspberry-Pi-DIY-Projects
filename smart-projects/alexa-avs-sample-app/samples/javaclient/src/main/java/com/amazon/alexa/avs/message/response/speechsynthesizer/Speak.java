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
package com.amazon.alexa.avs.message.response.speechsynthesizer;

import com.amazon.alexa.avs.message.Payload;
import com.amazon.alexa.avs.message.response.AttachedContentPayload;

import org.codehaus.jackson.annotate.JsonIgnore;

import java.io.InputStream;

public class Speak extends Payload implements AttachedContentPayload {
    private String url;
    private String format;
    private String token;

    @JsonIgnore
    private InputStream attachedContent;

    /**
     * Get the Content-ID that this {@link Speak} references.
     */
    public String getUrl() {
        return url;
    }

    public String getFormat() {
        return format;
    }

    public String getToken() {
        return token;
    }

    public void setUrl(String url) {
        // The format we get from the server has the audioContentId as "cid:%CONTENT_ID%" whereas
        // the actual Content-ID HTTP Header value is "%CONTENT_ID%".
        // This normalizes that
        this.url = url.substring(4);
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public void setToken(String token) {
        this.token = token;
    }

    @Override
    public boolean requiresAttachedContent() {
        return !hasAttachedContent();
    }

    @Override
    public boolean hasAttachedContent() {
        return attachedContent != null;
    }

    @JsonIgnore
    @Override
    public String getAttachedContentId() {
        return url;
    }

    @JsonIgnore
    @Override
    public InputStream getAttachedContent() {
        return attachedContent;
    }

    @Override
    public void setAttachedContent(String cid, InputStream content) {
        if (getAttachedContentId().equals(cid)) {
            this.attachedContent = content;
        } else {
            throw new IllegalArgumentException(
                    "Tried to add the wrong audio content to a Speak directive. This cid: "
                            + getAttachedContentId() + " other cid: " + cid);
        }
    }
}
