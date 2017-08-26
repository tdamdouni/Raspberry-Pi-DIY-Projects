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
package com.amazon.alexa.avs;

import com.amazon.alexa.avs.http.AVSClient.Resource;
import com.amazon.alexa.avs.http.MultipartParser;
import com.amazon.alexa.avs.http.RetryPolicy;

import org.eclipse.jetty.client.api.ContentProvider;

import java.util.Optional;

public class AVSRequest {
    private final Resource resource;
    private final ContentProvider contentProvider;
    private final RetryPolicy retryPolicy;
    private final MultipartParser multipartParser;
    private final RequestListener requestListener;

    public AVSRequest(Resource resource, ContentProvider contentProvider, RetryPolicy retryPolicy, MultipartParser multipartParser, RequestListener requestListener) {
        this.resource = resource;
        this.contentProvider = contentProvider;
        this.retryPolicy = retryPolicy;
        this.multipartParser = multipartParser;
        this.requestListener = requestListener;
    }

    public AVSRequest(Resource resource, ContentProvider contentProvider, RetryPolicy retryPolicy, MultipartParser multipartParser) {
        this(resource, contentProvider, retryPolicy, multipartParser, null);
    }

    public Resource getResource() {
        return resource;
    }

    public ContentProvider getContentProvider() {
        return contentProvider;
    }

    public RetryPolicy getRetryPolicy() {
        return retryPolicy;
    }

    public MultipartParser getMultipartParser() {
        return multipartParser;
    }

    public Optional<RequestListener> getRequestListener() {
        return Optional.ofNullable(requestListener);
    }
}
