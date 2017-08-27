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

#include <iostream>

#include "testLogger.h"
#include "testKittAi.h"
#include "testSensory.h"
#include "testIPCFactory.h"
#include "testGPIO.h"
#include "unistd.h"

using namespace std;

// runs the test-suite
int main() {

  // logging
  if(!testLogger()) {
    std::cout << "ERROR testing log functionality" << std::endl;
    return 0;
  }

  std::cout << " **** Logging tests passed ok ****" << std::endl;

  // kitt-ai
  if(!testKittAi()) {
    std::cout << "ERROR testing kitt-ai functionality" << std::endl;
    return 0;
  }

  std::cout << " **** Kitt-ai tests passed ok ****" << std::endl;

  // sensory
  if(!testSensory()) {
    std::cout << "ERROR testing sensory functionality" << std::endl;
    return 0;
  }

  std::cout << " **** Sensory tests passed ok ****" << std::endl;

  // GPIO
  if(!testGPIO()) {
    std::cout << "ERROR testing GPIO functionality" << std::endl;
    return 0;
  }

  std::cout << " **** GPIO tests passed ok ****" << std::endl;

  // ipc factory
  if(!testIPCFactory()) {
    std::cout << "ERROR testing ipc factory functionality" << std::endl;
    return 0;
  }

  std::cout << " **** ipc factory tests passed ok ****" << std::endl;

  std::cout << " *****************************" << std::endl;
  std::cout << " **** ALL TESTS PASSED OK ****" << std::endl;
  std::cout << " *****************************" << std::endl;

  return 0;
}

