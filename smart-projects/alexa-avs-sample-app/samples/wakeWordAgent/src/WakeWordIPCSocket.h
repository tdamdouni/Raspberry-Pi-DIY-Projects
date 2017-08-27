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

#ifndef ALEXA_VS_WAKE_WORD_WAKE_WORD_IPC_SOCKET_H_
#define ALEXA_VS_WAKE_WORD_WAKE_WORD_IPC_SOCKET_H_

#include "WakeWordIPC.h"

#include <stdint.h>
#include <thread>
#include <atomic>
#include <arpa/inet.h>

namespace AlexaWakeWord {

// an implementation of the IPC class, which uses sockets.
class WakeWordIPCSocket: public WakeWordIPC {

public:

  WakeWordIPCSocket(IPCInterface* interface);
  virtual ~WakeWordIPCSocket();
  void sendCommand(const IPCInterface::Command command);

private:

  // Utility functions
  void clearSocketMembers();
  void init();
  bool initializeSocket();
  bool makeConnection();
  bool receiveCommand();

  // The main thread loop
  void mainLoop();

  // Thread management variables
  std::atomic<bool> m_isRunning;
  std::unique_ptr<std::thread> m_thread;

  // Socket variables
  int m_socketHandle;
  bool m_socketConnected;
  struct sockaddr_in m_socketAddr;
};

} // namespace AlexaWakeWord

#endif // ALEXA_VS_WAKE_WORD_WAKE_WORD_IPC_SOCKET_H_
