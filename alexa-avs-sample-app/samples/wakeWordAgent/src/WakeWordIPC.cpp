/**
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Amazon Software License (the "License"). You may not use this file 
 * except in compliance with the License. A copy of the License is located at
 *
 *   http://aws.amazon.com/asl/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" 
 * BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License 
 * for the specific language governing permissions and limitations under the License.
 */

#include "WakeWordIPC.h"
#include "Logger.h"

using namespace AlexaWakeWord::Logger;

namespace AlexaWakeWord {

WakeWordIPC::WakeWordIPC(IPCInterface* interface) :
        m_interface{interface} {
}

void WakeWordIPC::ipcCommandReceived(IPCInterface::Command command) {

  if(!m_interface) {
    return;
  }

  log(Logger::DEBUG, "WakeWordIPC: received command");
  m_interface->onIPCCommandReceived(command);
}

} // namespace AlexaWakeWord
