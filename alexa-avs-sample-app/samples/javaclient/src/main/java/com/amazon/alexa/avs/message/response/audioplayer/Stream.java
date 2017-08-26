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
package com.amazon.alexa.avs.message.response.audioplayer;

import com.amazon.alexa.avs.message.response.ProgressReport;

import org.codehaus.jackson.annotate.JsonIgnore;

import java.io.InputStream;

public final class Stream {
    private String url;
    private String token;
    private String expiryTime;
    private long offsetInMilliseconds;
    private ProgressReport progressReport;
    private boolean urlIsAContentId;
    private String expectedPreviousToken;

    @JsonIgnore
    private InputStream attachedContent;

    public String getUrl() {
        return url;
    }

    public String getToken() {
        return token;
    }

    public String getExpiryTime() {
        return expiryTime;
    }

    public long getOffsetInMilliseconds() {
        return offsetInMilliseconds;
    }

    public boolean getProgressReportRequired() {
        return progressReport != null && progressReport.isRequired();
    }

    public ProgressReport getProgressReport() {
        return progressReport;
    }

    public String getExpectedPreviousToken() {
        return expectedPreviousToken;
    }

    public void setUrl(String url) {
        urlIsAContentId = url.startsWith("cid");
        if (urlIsAContentId) {
            this.url = url.substring(4);
        } else {
            this.url = url;
        }
    }

    public void setToken(String token) {
        this.token = token;
    }

    public void setExpiryTime(String expiryTime) {
        this.expiryTime = expiryTime;
    }

    public void setOffsetInMilliseconds(long offsetInMilliseconds) {
        this.offsetInMilliseconds = offsetInMilliseconds;
    }

    public void setProgressReport(ProgressReport progressReport) {
        this.progressReport = progressReport;
    }

    public void setExpectedPreviousToken(String expectedPreviousToken) {
        this.expectedPreviousToken = expectedPreviousToken;
    }

    public boolean requiresAttachedContent() {
        return urlIsAContentId && !hasAttachedContent();
    }

    public boolean hasAttachedContent() {
        return attachedContent != null;
    }

    public void setAttachedContent(InputStream attachedContent) {
        this.attachedContent = attachedContent;
    }

    @JsonIgnore
    public InputStream getAttachedContent() {
        return attachedContent;
    }
}
