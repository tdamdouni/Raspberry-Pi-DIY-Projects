/**
 * Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
package com.amazon.alexa.avs.http;

import com.amazon.alexa.avs.DirectiveEnqueuer;
import com.amazon.alexa.avs.ResultListener;
import com.amazon.alexa.avs.config.DeviceConfig;

import org.eclipse.jetty.util.ssl.SslContextFactory;

public class AVSClientFactory {
    private DeviceConfig config;

    public AVSClientFactory(DeviceConfig config) {
        this.config = config;
    }

    public AVSClient getAVSClient(DirectiveEnqueuer directiveEnqueuer,
            ParsingFailedHandler parsingFailedHandler, ResultListener resultListener)
            throws Exception {
        return new AVSClient(config.getAvsHost(), directiveEnqueuer, new SslContextFactory(),
                parsingFailedHandler, resultListener);
    }
}
