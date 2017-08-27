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

#ifndef ALEXA_VS_WAKE_WORD_IPC_INTERFACE_H_
#define ALEXA_VS_WAKE_WORD_IPC_INTERFACE_H_

#include <string>

namespace AlexaWakeWord {

// This class provides the interface for interacting with the Alexa Sample App
// over IPC.  In this project, this is required to communicate to the Sample App
// that the WakeWordAgent has detected the keyword ('Alexa').  The Sample App
// responds in turn to the Agent when the user has completed their interaction
// with Alexa.
class IPCInterface {

public:
  enum Command : uint32_t {
    DISCONNECT                = 1,  // OUTGOING : Ask the AVS client to disconnect from us
    WAKE_WORD_DETECTED        = 2,  // OUTGOING : sent to AVS client when a wake word is detected
    PAUSE_WAKE_WORD_ENGINE    = 3,  // INCOMING : request to pause the engine and yield the Mic
    RESUME_WAKE_WORD_ENGINE   = 4,  // INCOMING : request to resume the engine
    CONFIRM                   = 5,  // OUTGOING : sent to AVS client to confirm the engine has stopped
    UNKNOWN                   = 6   // n/a : for error & default cases
  };

  virtual ~IPCInterface() = default;

  // This will be called by the IPC handling code when an actual command
  // comes in over IPC from a wake-word agent - the implementation
  // of this function will handle it.
  virtual void onIPCCommandReceived(Command command) = 0;

  // Utility function
  static Command intToCommand(int intCommand);

private:

  // Utility function
  std::string commandToString(const Command command);
};

} // namespace AlexaWakeWord

#endif // ALEXA_VS_WAKE_WORD_IPC_INTERFACE_H_
