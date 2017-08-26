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

#include "PortAudioWrapper.h"
#include "Logger.h"
#include "WakeWordException.h"

#include "pa_util.h"

#include <functional>
#include <memory>

namespace AlexaWakeWord {

// Ring buffer size is almost 1 s worth of samples (sampling rate 16kHz)
// approximated to the nearest power of 2
const int RING_BUFFER_SIZE          = 16384;

// In this codebase, portAudio expects 16-bit input
const int EXPECTED_BYTES_PER_SAMPLE = 2;

// Called directly by portAudio code.  userData is populated internally
// as the PortAudioWrapper object that will in turn handle the callback.
// That's why the class callback function is public.
int portAudioCallback(const void* input,
                      void* output,
                      unsigned long numSamplesToWrite,
                      const PaStreamCallbackTimeInfo* timeInfo,
                      PaStreamCallbackFlags statusFlags,
                      void* userData) {

  auto paWrapper = static_cast<PortAudioWrapper*>(userData);
  paWrapper->paCallback(input, numSamplesToWrite);

  // Returning this portAudio-defined enum from this callback
  // is expected to allow portAudio to continue processing.
  return paContinue;
}

PortAudioWrapper::PortAudioWrapper(int sampleRate,
                                   int numChannels,
                                   int bitsPerSample) :
        m_paStream{nullptr}, m_numLostSamples{0} {

  init(bitsPerSample, numChannels, sampleRate);
}

PortAudioWrapper::~PortAudioWrapper() {
  Pa_StopStream(m_paStream);
  Pa_CloseStream(m_paStream);
  Pa_Terminate();
}

void PortAudioWrapper::readData(std::vector<int16_t>* paSamples) {

  if(m_numLostSamples > 0) {
    log(Logger::INFO, "RingBuffer overflow, number of lost samples:" +
            std::to_string(m_numLostSamples));
    m_numLostSamples = 0;
  }

  auto numAvailableSamples =
          PaUtil_GetRingBufferReadAvailable(&m_paRingBuffer);

  // There may be no work to do
  if(0 == numAvailableSamples) {
    return;
  }

  // Get the data out the ringbuffer and into the vector
  paSamples->resize(numAvailableSamples);
  auto numReadSamples = PaUtil_ReadRingBuffer(&m_paRingBuffer,
                                              paSamples->data(),
                                              numAvailableSamples);

  // Confirm we read the amount of data we expected
  if(numReadSamples != numAvailableSamples) {
    log(Logger::ERROR, std::string("Error reading from PortAudio") +
            " | available samples:" + std::to_string(numAvailableSamples) +
            " | read samples:" + std::to_string(numReadSamples));
  }
}

// The class-level callback.  Propagates the data from portAudio into the
// ringbuffer.
void PortAudioWrapper::paCallback(const void* input,
                                  unsigned long numSamplesToWrite) {

  // Write PortAudio's input to the ring buffer where we can access it later
  auto numWrittenSamples = PaUtil_WriteRingBuffer(&m_paRingBuffer,
                                                  input,
                                                  numSamplesToWrite);

  // If the ring buffer does not have enough space for numSamplesToWrite,
  // keep track of the number of samples lost
  if(numWrittenSamples < numSamplesToWrite) {
    log(Logger::INFO, "sample size mismatch");
    m_numLostSamples += (numSamplesToWrite - numWrittenSamples);
  }
}

void PortAudioWrapper::init(int bitsPerSample, int numChannels,
                            int sampleRate) {

  log(Logger::DEBUG, "PortAudioWrapper: initializing ring buffer");

  // Initialize the ring buffer

  int bytesPerSample = bitsPerSample / 8;

  // Create the actual memory for the ring buffer, using portAudio functions
  // to create & release the memory needed.
  m_ringBufferMemory = std::unique_ptr<char, std::function<void(char*)>>(
    (char*)PaUtil_AllocateMemory(bytesPerSample * RING_BUFFER_SIZE),
    [](char* b) { PaUtil_FreeMemory(b); });

  PaUtil_InitializeRingBuffer(&m_paRingBuffer,
                              bytesPerSample,
                              RING_BUFFER_SIZE,
                              m_ringBufferMemory.get());

  log(Logger::DEBUG, "PortAudioWrapper: Initializing PortAudio");

  PaError paStatus = Pa_Initialize();
  if (paStatus != paNoError) {
    std::string errorMsg = std::string("Failed to initialize PortAudio. ") +
            Pa_GetErrorText(paStatus);
    log(Logger::ERROR, errorMsg);
    throw WakeWordException(errorMsg);
  }

  // Ok, open the stream

  paStatus = paNotInitialized;
  switch(bytesPerSample) {
    case EXPECTED_BYTES_PER_SAMPLE:
      paStatus = Pa_OpenDefaultStream(&m_paStream,
                                      numChannels,
                                      0,
                                      paInt16,
                                      sampleRate,
                                      paFramesPerBufferUnspecified,
                                      portAudioCallback,
                                      this);
      break;
    default:
      std::string errorMsg = std::string("Failed to open Port Audio stream") +
          " | invalid bytes per sample:" + std::to_string(bytesPerSample) +
          " | expected bytes per sample:" +
              std::to_string(EXPECTED_BYTES_PER_SAMPLE);
      log(Logger::ERROR, errorMsg);
      throw WakeWordException(errorMsg);
  }

  if (paStatus != paNoError) {
    std::string errorMsg = "Failed to open PortAudio stream.";
    log(Logger::ERROR, errorMsg + Pa_GetErrorText(paStatus));
    throw WakeWordException(errorMsg);
  }

  // Start the stream

  paStatus = Pa_StartStream(m_paStream);

  if(paStatus != paNoError) {
    std::string errorMsg = std::string("Failed to start PortAudio stream.") +
            Pa_GetErrorText(paStatus);
    log(Logger::ERROR, errorMsg);
    throw WakeWordException(errorMsg);
  }
}

} // namespace AlexaWakeWord
