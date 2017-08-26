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

#ifndef ALEXA_VS_WAKE_WORD_WAKE_WORD_ENGINE_FACTORY_H_
#define ALEXA_VS_WAKE_WORD_WAKE_WORD_ENGINE_FACTORY_H_

#include "WakeWordEngine.h"

#include <memory>

namespace AlexaWakeWord {

// A namespace, not a class.  We don't need more at this time, and it's
// simpler to implement, use, and extend.
namespace WakeWordEngineFactory {

// Currently supported wake-word audio engines
enum class EngineType {
  KITT_AI_SNOWBOY_ENGINE = 1,
  SENSORY_ENGINE = 2,
  GPIO_ENGINE = 3
};

// Creation function
std::unique_ptr<WakeWordEngine> createEngine(
        WakeWordDetectedInterface* interface, EngineType engineType);

// Utility function
std::string engineTypeToString(const EngineType type);

} // namespace WakeWordEngineFactory

} // namespace AlexaWakeWord

#endif // ALEXA_VS_WAKE_WORD_WAKE_WORD_ENGINE_FACTORY_H_
