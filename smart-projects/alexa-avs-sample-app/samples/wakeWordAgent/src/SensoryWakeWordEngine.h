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

#ifndef SENSORY_WAKE_WORD_ENGINE_H
#define SENSORY_WAKE_WORD_ENGINE_H

#include "WakeWordEngine.h"
#include "snsr.h"

#include <memory>
#include <string>
#include <thread>
#include <atomic>

namespace AlexaWakeWord {

class SensoryWakeWordEngine: public WakeWordEngine {
public:
  SensoryWakeWordEngine(WakeWordDetectedInterface* interface);
  ~SensoryWakeWordEngine();
  void pause();
  void resume();
  bool isRunning();
  void callWakeWordDetected();

private:

  // Utility functions controlling the sensory library
  void init();
  void start();
  void stop();
  void mainLoop();

  // audio is acquired and processed in this thread
  std::unique_ptr<std::thread> m_thread;
  std::atomic<bool> m_isRunning;

  // A handle on the sensory engine session.
  // This is typedef'd as a pointer to a struct within snsr.h.
  SnsrSession m_session;
};

}
#endif // SENSORY_WAKE_WORD_ENGINE_H
