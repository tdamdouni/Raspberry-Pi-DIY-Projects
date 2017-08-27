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

import java.util.concurrent.Callable;

/**
 * A policy for describing how an action should be retried.
 */
public interface RetryPolicy {
    /**
     * Attempt to execute the {@link Callable}, and retry using the logic of the concrete
     * implementation of this interface if we receive an Exception of type exception.
     *
     * @param callable
     *            The {@link Callable} to call on each attempt.
     * @param exception
     *            The type of {@link Exception} to cause a retry.
     * @throws Exception
     */
    void tryCall(Callable<Void> callable, Class<? extends Throwable> exception) throws Exception;
}
