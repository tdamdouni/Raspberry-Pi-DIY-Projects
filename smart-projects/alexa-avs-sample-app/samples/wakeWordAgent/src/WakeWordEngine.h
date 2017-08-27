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

#ifndef ALEXA_VS_WAKE_WORD_WAKE_WORD_ENGINE_H_
#define ALEXA_VS_WAKE_WORD_WAKE_WORD_ENGINE_H_

#include "WakeWordDetectedInterface.h"

namespace AlexaWakeWord {

// Interface for a WakeWordEngine.  This encapsulates the logic needed for
// detecting a wake-word (ie. 'Alexa') from audio input.
class WakeWordEngine {

public:

  WakeWordEngine(WakeWordDetectedInterface* passedInterface);
  virtual ~WakeWordEngine() = default;

  // When paused, the microphone is released.
  virtual void pause() = 0;
  virtual void resume() = 0;

protected:

  // This will be called by subclasses of WakeWordEngine to notify that
  // a wake-word was detected.
  void wakeWordDetected();

private:

  // The object that needs to know when the wakeword is detected.
  WakeWordDetectedInterface* m_interface;
};

} /* namespace AlexaWakeWord*/

#endif /* ALEXA_VS_WAKE_WORD_WAKE_WORD_ENGINE_H_ */
