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

#include "testLogger.h"
#include "../src/Logger.h"

#include <string>

using namespace AlexaWakeWord;

using namespace Logger;

bool testLogger() {

  std::string testString = "test trace";

  // set to each possible value
  setDefaultLogLevel(Logger::DEBUG);
  setDefaultLogLevel(Logger::INFO);
  setDefaultLogLevel(Logger::WARNING);
  setDefaultLogLevel(Logger::ERROR);

  // ensure logging to all levels works
  log(Logger::DEBUG, testString);
  log(Logger::INFO, testString);
  log(Logger::WARNING, testString);
  log(Logger::ERROR, testString);

  return true;
}

