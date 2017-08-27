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

#include "WakeWordEngineFactory.h"
#include "Logger.h"
#include "WakeWordUtils.h"
#include "KittAiSnowboyWakeWordEngine.h"
#include "SensoryWakeWordEngine.h"
#include "GPIOWakeWordEngine.h"

using namespace AlexaWakeWord::Logger;

namespace AlexaWakeWord {

namespace WakeWordEngineFactory {

std::unique_ptr<WakeWordEngine> createEngine(
        WakeWordDetectedInterface* interface,
        EngineType engineType) {

  switch(engineType) {
    case EngineType::KITT_AI_SNOWBOY_ENGINE:
      log(Logger::DEBUG, "WakeWordEngineFactory: creating Kitt-Ai Engine");
      return make_unique<KittAiSnowboyWakeWordEngine>(interface);
    case EngineType::SENSORY_ENGINE:
      log(Logger::DEBUG, "WakeWordEngineFactory: creating Sensory Engine");
      return make_unique<SensoryWakeWordEngine>(interface);
    case EngineType::GPIO_ENGINE:
      log(Logger::DEBUG, "WakeWordEngineFactory: creating GPIO Engine");
      return make_unique<GPIOWakeWordEngine>(interface);
    default:
      log(Logger::ERROR, "WakeWordEngineFactory: unhandled switch case");
      return nullptr;
  }
}

std::string engineTypeToString(const EngineType type) {

  switch (type) {
    case EngineType::KITT_AI_SNOWBOY_ENGINE:
      return "KITT_AI_SNOWBOY_ENGINE";
    case EngineType::SENSORY_ENGINE:
      return "SENSORY_ENGINE";
    case EngineType::GPIO_ENGINE:
      return "GPIO_ENGINE";
    default:
      return "UNKNOWN";
  }
}

} // namespace WakeWordEngineFactory

} // namespace AlexaWakeWord
