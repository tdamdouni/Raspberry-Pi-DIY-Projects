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

#include "KittAiSnowboyWakeWordEngine.h"
#include "Logger.h"
#include "WakeWordUtils.h"
#include "WakeWordException.h"

#include <unistd.h>

using namespace snowboy;
using namespace AlexaWakeWord::Logger;

namespace AlexaWakeWord {

static const std::string  RESOURCE_FILE  = "../ext/resources/common.res";
static const std::string  MODEL_FILE     = "../ext/resources/alexa.umdl";
static const float        AUDIO_GAIN     = 1.0;
static const bool         APPLY_FRONTEND = true;
static const int          MICROSECONDS_BETWEEN_SAMPLES = 100000;

KittAiSnowboyWakeWordEngine::KittAiSnowboyWakeWordEngine(
        WakeWordDetectedInterface* interface) : WakeWordEngine(interface),
        m_isRunning{false},
        m_isDetectorSetup{false},
        m_isPortAudioSetup{false} {

  try {
    init();
  } catch(std::bad_alloc& e) {
    log(Logger::ERROR,
      "KittAiSnowboyWakeWordEngine: Failed to allocate memory");
    throw;
  } catch(WakeWordException& e) {
    log(Logger::ERROR, std::string(
      "KittAiSnowboyWakeWordEngine: Initialization error:") + e.what());
    throw;
  }
}

KittAiSnowboyWakeWordEngine::~KittAiSnowboyWakeWordEngine() {

  log(Logger::INFO, " *** THREAD JOINING: KITT-AI ***");
  m_isRunning = false;
  m_thread->join();
}

void KittAiSnowboyWakeWordEngine::pause() {

  log(Logger::INFO, "KittAiSnowboyWakeWordEngine: handling pause");

  // Pause means we want to release the microphone input stream.
  // This will allow the AVS client to acquire it.

  std::lock_guard<std::mutex> lock(m_portAudioMutex);

  if(m_isPortAudioSetup) {
    log(Logger::INFO, "KittAiSnowboyWakeWordEngine: releasing portAudio");

    // Invoke destructor to release the microphone
    m_portAudioWrapper.reset();
    m_isPortAudioSetup = false;
  } else {
    log(Logger::INFO, "KittAiSnowboyWakeWordEngine: portAudio already released");
  }
}

void KittAiSnowboyWakeWordEngine::resume() {

  log(Logger::INFO, "KittAiSnowboyWakeWordEngine: handling resume");

  initPortAudio();
}

void KittAiSnowboyWakeWordEngine::init() {

  log(Logger::DEBUG, "KittAiSnowboyWakeWordEngine: initializing");

  initDetector();
  initPortAudio();

  log(Logger::DEBUG, "Starting Kitt-Ai engine thread");
  m_isRunning = true;
  m_thread = make_unique<std::thread>(&KittAiSnowboyWakeWordEngine::mainLoop,
            this);
}

void KittAiSnowboyWakeWordEngine::initDetector() {

  log(Logger::DEBUG,
      std::string("Initializing Kitt-Ai Snowboy library ") +
      " | resource file:" + RESOURCE_FILE +
      " | model file: " + MODEL_FILE +
      " | audio gain: " + std::to_string(AUDIO_GAIN));

  m_detector = make_unique<SnowboyDetect>(RESOURCE_FILE, MODEL_FILE);
  m_detector->SetAudioGain(AUDIO_GAIN);
  m_detector->ApplyFrontend(APPLY_FRONTEND);
  m_isDetectorSetup = true;
}

void KittAiSnowboyWakeWordEngine::initPortAudio() {

  int sampleRate = m_detector->SampleRate();
  int bitsPerSample = m_detector->BitsPerSample();
  int numChannels = m_detector->NumChannels();

  log(Logger::DEBUG,
      std::string("KittAiSnowboyWakeWordEngine: Creating PortAudio library") +
      " | sample rate " + std::to_string(sampleRate) +
      " | sample size " + std::to_string(bitsPerSample) +
      " | number of channels " + std::to_string(numChannels));

  std::lock_guard<std::mutex> lock(m_portAudioMutex);

  m_portAudioWrapper = make_unique<PortAudioWrapper>(sampleRate,
                                                     numChannels,
                                                     bitsPerSample);
  m_isPortAudioSetup = true;
}

void KittAiSnowboyWakeWordEngine::getPortAudioInput(std::vector<int16_t>* data) {

  std::lock_guard<std::mutex> lock(m_portAudioMutex);

  if (!m_isDetectorSetup || !m_isPortAudioSetup) {
    return;
  }

  m_portAudioWrapper->readData(data);
}

void KittAiSnowboyWakeWordEngine::mainLoop() {

  log(Logger::INFO, "KittAiSnowboyWakeWordEngine: thread started");

  while(m_isRunning) {

    std::vector<int16_t> paSamples;
    getPortAudioInput(&paSamples);

    if( (!paSamples.empty()) &&
        m_detector->RunDetection(paSamples.data(), paSamples.size()) > 0) {

      log(Logger::INFO, "KittAiSnowboyWakeWordEngine: Wake Word Detected");
      wakeWordDetected();
    }
    usleep(MICROSECONDS_BETWEEN_SAMPLES);
  }

  log(Logger::INFO, "KittAiSnowboyWakeWordEngine: thread ended");
}

} // namespace AlexaWakeWord
