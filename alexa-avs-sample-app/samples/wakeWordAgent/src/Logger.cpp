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

#include "Logger.h"

#include <iostream>

namespace AlexaWakeWord {

namespace Logger {

// File-local utility function
std::string logLevelToString(Logger::Level level) {

  switch (level) {
    case Logger::DEBUG:
      return "DEBUG";
    case Logger::INFO:
      return "INFO";
    case Logger::WARNING:
      return "WARNING";
    case Logger::ERROR:
      return "ERROR";
    default:
      return "UNKNOWN";
  }
}

/////////////////////////////////////////////////////////
// Implementation class - only visible in this file
class LoggerImpl {

public:

  static void log(const Level level, const std::string& msg) {

    if(level < m_defaultLevel) {
      return;
    }

    std::cout << logLevelToString(level) << ":" << msg << std::endl;
  }

  void setDefaultLogLevel(const Level level) {
    m_defaultLevel = level;
  }

private:

  static Level m_defaultLevel;
};

Level LoggerImpl::m_defaultLevel = Level::WARNING;

/////////////////////////////////////////////////////////
// File-local utility function
LoggerImpl getLogger() {
  static LoggerImpl logger;
  return logger;
}

/////////////////////////////////////////////////////////
// Implementation of namespace-visible functions to outside callers
//
void log(const Level level, const std::string& msg) {
  getLogger().log(level, msg);
}

void setDefaultLogLevel(const Level level) {
  getLogger().setDefaultLogLevel(level);
}

} // namespace Logger

} // namespace AlexaWakeWord
