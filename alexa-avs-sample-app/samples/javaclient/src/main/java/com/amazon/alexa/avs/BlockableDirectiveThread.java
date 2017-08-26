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

import com.amazon.alexa.avs.message.response.Directive;

import java.util.concurrent.BlockingQueue;

/**
 * This thread takes a queue which will be filled with directives and dispatches them to the given
 * {@link DirectiveDispatcher} as they are added to the queue. This thread also supports blocking
 * the dispatching of directives.
 */
public class BlockableDirectiveThread extends Thread {
    private final BlockingQueue<Directive> directiveQueue;
    private final DirectiveDispatcher directiveDispatcher;
    private volatile boolean block;

    public BlockableDirectiveThread(BlockingQueue<Directive> directiveQueue,
            DirectiveDispatcher directiveDispatcher) {
        this(directiveQueue, directiveDispatcher, BlockableDirectiveThread.class.getSimpleName());
    }

    public BlockableDirectiveThread(BlockingQueue<Directive> directiveQueue,
            DirectiveDispatcher directiveDispatcher, String name) {
        this.directiveQueue = directiveQueue;
        this.directiveDispatcher = directiveDispatcher;
        setName(name);
    }

    public synchronized void block() {
        block = true;
    }

    public synchronized void unblock() {
        block = false;
        notify();
    }

    public synchronized void clear() {
        directiveQueue.clear();
    }

    @Override
    public void run() {
        while (true) {
            try {
                synchronized (this) {
                    if (block) {
                        wait();
                    }
                }
                Directive directive = directiveQueue.take();
                directiveDispatcher.dispatch(directive);
            } catch (InterruptedException e) {
            }
        }
    }
}
