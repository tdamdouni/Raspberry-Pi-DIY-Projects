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

#include "WakeWordAgent.h"
#include "WakeWordUtils.h"
#include "Logger.h"

#include <string>
#include <unistd.h>

using namespace AlexaWakeWord::Logger;

namespace AlexaWakeWord {

WakeWordAgent::WakeWordAgent(WakeWordEngineFactory::EngineType engineType,
                             WakeWordIPCFactory::IPCType ipcType) :
        m_isRunning{false}, m_currentState{State::UNINITIALIZED} {

  setState(State::IDLE);

  try {

    log(Logger::DEBUG, std::string("WakeWordAgent: initalizing") +
            " | wake word engine of type:" +
            WakeWordEngineFactory::engineTypeToString(engineType) +
            " | IPC handler of type:" +
            WakeWordIPCFactory::IPCTypeToString(ipcType));

    m_wakeWordEngine = WakeWordEngineFactory::createEngine(this, engineType);
    m_IPCHandler = WakeWordIPCFactory::createIPCHandler(this, ipcType);

    m_isRunning = true;

    m_thread = make_unique<std::thread>(&WakeWordAgent::mainLoop, this);

  } catch(std::bad_alloc& e) {
    log(Logger::ERROR, "WakeWordAgent: could not allocate memory");
    throw;
  } catch (WakeWordException& e) {
      log(Logger::ERROR,
          std::string("WakeWordAgent: exception in constructor: ") + e.what());
    throw;
  }
}

WakeWordAgent::~WakeWordAgent() {
  log(Logger::DEBUG, "WakeWordAgent: Joining on thread");
  m_isRunning = false;
  m_thread->join();
}

// A fairly simple state machine.  On each state we care about, the
// transition should be self-explanatory.
void WakeWordAgent::mainLoop() {

  log(Logger::INFO, "WakeWordAgent: thread started");

  std::unique_lock<std::mutex> lck(m_mtx);

  auto checkState = [this] {
    return m_currentState == State::WAKE_WORD_DETECTED
    || m_currentState == State::WAKE_WORD_PAUSE_REQUESTED
    || m_currentState == State::WAKE_WORD_RESUME_REQUESTED;
  };

  while (m_isRunning) {

    // Wait for a state where an action is required
    m_cvStateChange.wait(lck, checkState);

    try {

      switch (m_currentState) {
        case State::WAKE_WORD_DETECTED:
          m_IPCHandler->sendCommand(Command::WAKE_WORD_DETECTED);
          setState(State::SENT_WAKE_WORD_DETECTED);
          break;

        case State::WAKE_WORD_PAUSE_REQUESTED:
          m_wakeWordEngine->pause();
          m_IPCHandler->sendCommand(Command::CONFIRM);
          setState(State::WAKE_WORD_PAUSED);
          break;

        case State::WAKE_WORD_RESUME_REQUESTED:
          m_wakeWordEngine->resume();
          setState(State::IDLE);
          break;

        default:
          // no-op
          break;
      }

    } catch (WakeWordException &e) {
     log(Logger::ERROR, std::string("WakeWordAgent::mainLoop - exception:") +
                        e.what());
      setState(State::IDLE);
    }
  }

  log(Logger::INFO, "WakeWordAgent: thread ended");
}

// Besides setting the state, prints some pretty cool trace!
void WakeWordAgent::onWakeWordDetected() {

  log(Logger::INFO, "===> WakeWordAgent: wake word detected <===");

  if(State::IDLE == m_currentState ||
      State::SENT_WAKE_WORD_DETECTED == m_currentState) {
    std::lock_guard<std::mutex> lock(m_mtx);
    setState(State::WAKE_WORD_DETECTED);
    m_cvStateChange.notify_one();
  }
}

// Called by our IPC handling object when a command is received.
// Updates our state machine accordingly.
// Note that the mainLoop() function above is where this change of
// state results in any action.
void WakeWordAgent::onIPCCommandReceived(IPCInterface::Command command) {

  log(Logger::INFO, "WakeWordAgent: IPC Command received:" +
                   std::to_string(command));

  switch(m_currentState) {
    case State::IDLE:
    case State::SENT_WAKE_WORD_DETECTED:
      if (IPCInterface::PAUSE_WAKE_WORD_ENGINE == command) {
        std::lock_guard<std::mutex> lock(m_mtx);
        setState(State::WAKE_WORD_PAUSE_REQUESTED);
        m_cvStateChange.notify_one();
      }
      break;
    case State::WAKE_WORD_PAUSED:
      if(IPCInterface::Command::RESUME_WAKE_WORD_ENGINE == command) {
        std::lock_guard<std::mutex> lock(m_mtx);
        setState(State::WAKE_WORD_RESUME_REQUESTED);
        m_cvStateChange.notify_one();
      }
      break;
    default:
      // no-op
      break;
  }
}

// utility function
std::string WakeWordAgent::stateToString(State state) {

  switch(state) {
    case State::UNINITIALIZED:
      return "UNINITIALIZED";
    case State::IDLE:
      return "IDLE";
    case State::WAKE_WORD_DETECTED:
      return "WAKE_WORD_DETECTED";
    case State::SENT_WAKE_WORD_DETECTED:
      return "SENT_WAKE_WORD_DETECTED";
    case State::WAKE_WORD_PAUSE_REQUESTED:
      return "WAKE_WORD_PAUSE_REQUESTED";
    case State::WAKE_WORD_PAUSED:
      return "WAKE_WORD_PAUSED";
    case State::WAKE_WORD_RESUME_REQUESTED:
      return "WAKE_WORD_RESUME_REQUESTED";
    default:
      log(Logger::ERROR, "WakeWordAgent::stateToString: unhandled switch case");
      return "UNKNOWN";
  }
}

// Utility function.  Encapsulates tracing to aid debugging.
void WakeWordAgent::setState(State state) {

  m_currentState = state;

  log(Logger::INFO, "WakeWordAgent: State set to " +
          stateToString(state) + "(" + std::to_string(static_cast<int>(state)) + ")");
}

} // namespace AlexaWakeWord
