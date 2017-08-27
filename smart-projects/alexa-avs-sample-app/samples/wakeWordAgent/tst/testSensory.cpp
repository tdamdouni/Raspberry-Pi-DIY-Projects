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

#include "testSensory.h"
#include "../src/SensoryWakeWordEngine.h"
#include "../src/WakeWordAgent.h"
#include "../src/Logger.h"

#include <unistd.h>
#include <string>

using namespace AlexaWakeWord;

using namespace Logger;

// dummy class for passing in for kittAi creation
class DummyWakeWordAgent: public WakeWordDetectedInterface, public IPCInterface {

  void onWakeWordDetected() { }

  void onIPCCommandReceived(Command command) { }
};

void createTempSensory() {

  auto wwAgent = std::make_shared<DummyWakeWordAgent>();

  auto sensory = std::make_shared<SensoryWakeWordEngine>(wwAgent.get());
}

bool testSensory() {

  // This function will create a sensory object, wake-word agent,
  // and call various member functions.  After the end of the function,
  // the objects will be destroyed.
  // This function call will verify that the object's threads are being
  // correctly ended, and that the destructors are running without issue.
  createTempSensory();

  // if we got here, it went well.
  return true;
}

