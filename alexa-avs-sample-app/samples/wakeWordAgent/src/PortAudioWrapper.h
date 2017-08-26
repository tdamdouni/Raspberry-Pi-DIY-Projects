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

#ifndef ALEXA_VS_WAKE_WORD_PORT_AUDIO_WRAPPER_H_
#define ALEXA_VS_WAKE_WORD_PORT_AUDIO_WRAPPER_H_

#include "pa_ringbuffer.h"
#include "portaudio.h"

#include <stdint.h>
#include <vector>
#include <memory>
#include <functional>

namespace AlexaWakeWord {

// Our portAudio logic.  It self-initializes, and manages its own
// callbacks internally.  After construction, the ringbuffer will be
// continually populated with microphone data.  Call readData to access this
// data.
class PortAudioWrapper {

public:
  PortAudioWrapper(int sampleRate, int numChannels, int bitsPerSample);
  virtual ~PortAudioWrapper();

  // Copies the data acquired from PortAudio into the passed vector
  void readData(std::vector<int16_t>* paSamples);

  // We integrate with PortAudio via a low-level C callback.
  // This public member function is provided to be called in turn.
  // Don't call this function from outside this class.
  void paCallback(const void* input, unsigned long numSamplesToWrite);

private:

  // Initialize
  void init(int bitsPerSample, int numChannels, int sampleRate);

  // Pointer to the memory for the ring buffer we will use
  std::unique_ptr<char, std::function<void(char*)>> m_ringBufferMemory;

  // The actual ring buffer object, which will be initialized with the
  // memory allocated by m_ringBufferMemory
  PaUtilRingBuffer m_paRingBuffer;

  // Pointer to PortAudio stream
  PaStream* m_paStream;

  // Number of lost samples lost during callback processing
  int m_numLostSamples;
};

} // namespace AlexaWakeWord

#endif // ALEXA_VS_WAKE_WORD_PORT_AUDIO_WRAPPER_H_
