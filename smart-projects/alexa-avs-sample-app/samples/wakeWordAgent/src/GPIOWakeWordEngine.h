
#ifndef GPIO_WAKE_WORD_ENGINE_H
#define GPIO_WAKE_WORD_ENGINE_H

#include "WakeWordEngine.h"
#include <thread>
#include <memory>
#include <atomic>

namespace AlexaWakeWord {

// A specialization of a WakeWordEngine, where a trigger comes from GPIO
class GPIOWakeWordEngine: public WakeWordEngine {
public:
  GPIOWakeWordEngine(WakeWordDetectedInterface* interface);
  ~GPIOWakeWordEngine() = default;
  void pause();
  void resume();

private:

  void init();
  void mainLoop();

  // GPIO is monitored in this thread
  std::unique_ptr<std::thread> m_thread;
  std::atomic<bool> m_isRunning;

};

}
#endif // GPIO_WAKE_WORD_ENGINE_H
