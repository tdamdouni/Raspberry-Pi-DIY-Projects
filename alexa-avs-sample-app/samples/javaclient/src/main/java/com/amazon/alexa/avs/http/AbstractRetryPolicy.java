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

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.Callable;

public abstract class AbstractRetryPolicy implements RetryPolicy {
    private int maxAttempts;

    private static final Logger log = LoggerFactory.getLogger(AbstractRetryPolicy.class);

    public AbstractRetryPolicy(int maxAttempts) {
        this.maxAttempts = maxAttempts;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public void tryCall(Callable<Void> callable, Class<? extends Throwable> exception)
            throws Exception {
        int attempts = 0;
        while (attempts < maxAttempts) {
            try {
                callable.call();
                break;
            } catch (Exception e) {
                attempts++;
                if ((exception != null) && (exception.isAssignableFrom(e.getClass()))
                        && !(attempts >= maxAttempts)) {
                    log.warn("Error occured while making call. This call will retry.", e);
                    Thread.sleep(getDelay(attempts));
                } else {
                    throw e;
                }
            }
        }
    }

    /**
     * Get the expected delay in milliseconds.
     *
     * @param attempts
     * @return
     */
    protected abstract long getDelay(int attempts);
}
