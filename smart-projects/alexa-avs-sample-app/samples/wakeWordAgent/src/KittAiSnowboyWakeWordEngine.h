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

#ifndef ALEXA_VS_WAKE_WORD_KITT_AI_SNOWBOY_WAKE_WORD_ENGINE_H_
#define ALEXA_VS_WAKE_WORD_KITT_AI_SNOWBOY_WAKE_WORD_ENGINE_H_

#include "WakeWordEngine.h"
#include "snowboy-detect.h"
#include "PortAudioWrapper.h"

#include <thread>
#include <memory>
#include <mutex>
#include <atomic>

namespace AlexaWakeWord {

// A specialization of a WakeWordEngine, integrating Kitt-ai.
// Take note of the two main pieces:
//  * portAudio - acquires input from the microphone
//  * kitt-ai   - processes this input, and indicates if the keyword has
//                been spoken
// The kitt-ai & portAudio code is run on its own thread.
class KittAiSnowboyWakeWordEngine: public WakeWordEngine {

public:

  KittAiSnowboyWakeWordEngine(WakeWordDetectedInterface* passedInterface);
  ~KittAiSnowboyWakeWordEngine();

  void pause();
  void resume();

private:

  void init();
  void initDetector();
  void initPortAudio();
  void getPortAudioInput(std::vector<int16_t>* data);
  void mainLoop();

  // Audio is acquired and processed in this thread
  std::unique_ptr<std::thread> m_thread;
  std::atomic<bool> m_isRunning;

  // Our kitt.ai detector
  std::unique_ptr<snowboy::SnowboyDetect> m_detector;
  std::atomic<bool> m_isDetectorSetup;

  // portAudio integration to acquire sound from the speaker
  std::unique_ptr<PortAudioWrapper> m_portAudioWrapper;
  std::atomic<bool> m_isPortAudioSetup;
  std::mutex m_portAudioMutex;
};

} // namespace AlexaWakeWord

#endif // ALEXA_VS_WAKE_WORD_KITT_AI_SNOWBOY_WAKE_WORD_ENGINE_H_
