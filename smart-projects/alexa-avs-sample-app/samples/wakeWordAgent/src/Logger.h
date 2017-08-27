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

#ifndef ALEXA_VS_WAKE_WORD_LOGGER_H_
#define ALEXA_VS_WAKE_WORD_LOGGER_H_

#include <string>

namespace AlexaWakeWord {

// Our mini-logger code.  Currently this supports levels of logging,
// and prints log trace to std::out.  To minimize code intrusion, the exposed
// interface is a namespace with a simple log() function.
// The .cpp file contains a class with the implementation.
// Both the namespace functions, and underlying class, may be extended to
// allow more complex things.
namespace Logger {

  // Not an enum class, to allow trivial < operator
  enum Level {
    DEBUG = 1,
    INFO,
    WARNING,
    ERROR
  };

  // Log at the specific level.
  void log(const Level level, const std::string& msg);

  // Set the level.  Future log messages below that level will be suppressed.
  void setDefaultLogLevel(const Level level);

} // namespace logger

} // namespace AlexaWakeWord

#endif // ALEXA_VS_WAKE_WORD_LOGGER_H_
