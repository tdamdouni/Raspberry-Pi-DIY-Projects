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

#ifndef ALEXA_VS_WAKE_WORD_WAKEWORDIPC_H_
#define ALEXA_VS_WAKE_WORD_WAKEWORDIPC_H_

#include "IPCInterface.h"

namespace AlexaWakeWord {

// Base class for handling IPC communication.  Handles the sending and
// receiving of commands.
class WakeWordIPC {
public:
  WakeWordIPC(IPCInterface* interface);
  virtual ~WakeWordIPC() = default;

  // Allows a command to be sent
  virtual void sendCommand(const IPCInterface::Command command) = 0;

protected:

  // Sub-classes should call this function when a command is received
  void ipcCommandReceived(const IPCInterface::Command command);

private:

  // The object which needs to know when a command is received
  IPCInterface* m_interface;
};

}/* namespace AlexaWakeWord*/

#endif /* ALEXA_VS_WAKE_WORD_WAKEWORDIPC_H_ */
