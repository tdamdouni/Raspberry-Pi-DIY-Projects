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

#include "WakeWordIPCFactory.h"
#include "Logger.h"
#include "WakeWordIPCSocket.h"
#include "WakeWordUtils.h"

using namespace AlexaWakeWord::Logger;

namespace AlexaWakeWord {

namespace WakeWordIPCFactory {

std::unique_ptr<WakeWordIPC> createIPCHandler(IPCInterface* interface,
                                              IPCType ipcType) {

  switch(ipcType) {
    case IPCType::TCP_PROTOCOL:
      log(Logger::DEBUG, "createIPCHandler: Creating TCP handler");
      return make_unique<WakeWordIPCSocket>(interface);
    default:
      log(Logger::ERROR, "createIPCHandler: Unhandled switch case");
      return nullptr;
  }
}

std::string IPCTypeToString(const IPCType type) {

  switch(type) {
    case IPCType::TCP_PROTOCOL:
      return "TCP_PROTOCOL";
    default:
      log(Logger::ERROR, "IPCTypeToString: Unhandled switch case");
      return "UNKNOWN";
  }
}

} // WakeWordIPCFactory

} // namespace AlexaWakeWord
