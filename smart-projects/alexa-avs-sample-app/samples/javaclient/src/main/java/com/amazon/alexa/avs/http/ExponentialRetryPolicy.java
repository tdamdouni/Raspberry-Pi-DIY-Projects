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
package com.amazon.alexa.avs.http;

/**
 * Implements a {@link RetryPolicy} with an exponential backoff.
 */
public class ExponentialRetryPolicy extends AbstractRetryPolicy {
    private long mulitiplier;

    public ExponentialRetryPolicy(long mulitiplier, int maxAttempts) {
        super(maxAttempts);
        this.mulitiplier = mulitiplier;
    }

    @Override
    protected long getDelay(int attempts) {
        if (attempts == 0) {
            return 0;
        }

        attempts = Math.max(0, attempts - 1);
        double exp = Math.pow(2, attempts);
        return Math.round(exp * mulitiplier);
    }
}
