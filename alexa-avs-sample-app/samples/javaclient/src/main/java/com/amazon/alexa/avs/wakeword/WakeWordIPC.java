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
package com.amazon.alexa.avs.wakeword;

import java.io.IOException;

public abstract class WakeWordIPC {

    public enum IPCCommand {

        IPC_DISCONNECT(1), IPC_WAKE_WORD_DETECTED(2), IPC_PAUSE_WAKE_WORD_ENGINE(3),
        IPC_RESUME_WAKE_WORD_ENGINE(4), IPC_CONFIRM(5);

        private final int value;

        IPCCommand(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }
    }

    private WakeWordDetectedHandler handler = null;

    public WakeWordIPC(WakeWordDetectedHandler handler) {
        this.handler = handler;
    }

    protected void wakeWordDetected() {
        if (handler != null) {
            handler.onWakeWordDetected();
        }
    }

    public abstract void sendCommand(IPCCommand command) throws IOException;

    public abstract void init();
}
