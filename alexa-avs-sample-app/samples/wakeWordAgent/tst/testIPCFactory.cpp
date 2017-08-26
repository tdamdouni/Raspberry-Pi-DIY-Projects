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

#include "testIPCFactory.h"
#include "../src/WakeWordIPCFactory.h"
#include "../src/WakeWordAgent.h"
#include "../src/Logger.h"

#include <unistd.h>
#include <string>

using namespace AlexaWakeWord;

using namespace Logger;

// dummy class for passing in for ipc object creation
class DummyWakeWordAgent: public WakeWordDetectedInterface, public IPCInterface {

  void onWakeWordDetected() { }

  void onIPCCommandReceived(Command command) { }
};

void createTempIPCFactory() {

  auto dummyAgent = std::make_shared<DummyWakeWordAgent>();

  auto ipc = WakeWordIPCFactory::createIPCHandler(dummyAgent.get(),
                                                  WakeWordIPCFactory::IPCType::TCP_PROTOCOL);
}

bool testIPCFactory() {

  createTempIPCFactory();

  // if we got here, no issues creating & destroying the IPC object
  return true;
}

