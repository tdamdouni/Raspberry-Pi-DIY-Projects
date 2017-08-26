/** 
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Amazon Software License (the "License"). You may not use this file 
 * except in compliance with the License. A copy of the License is located at
 *
 *   http://aws.amazon.com/asl/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, 
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the 
 * specific language governing permissions and limitations under the License.
 */
package com.amazon.alexa.avs.wakeword;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashSet;
import java.util.Set;

public class WakeWordIPCSocket extends WakeWordIPC implements Runnable {

    private ServerSocket serverSocket = null;
    private Thread ipcThread = null;
    private final Set<WakeWordIPCConnectedClient> connectedClients = new HashSet<>();
    private static final Logger log = LoggerFactory.getLogger(WakeWordIPCSocket.class);

    public WakeWordIPCSocket(WakeWordDetectedHandler handler, int portNumber) throws IOException {
        super(handler);
        serverSocket = new ServerSocket(portNumber, 0, InetAddress.getByName(null));
    }

    public void init() {
        if (ipcThread == null) {
            ipcThread = new Thread(this);
            ipcThread.start();
        }
    }

    @Override
    public void run() {
        while (true) {
            try {
                Socket clientSocket = serverSocket.accept();
                WakeWordIPCConnectedClient newConnectedClient =
                        new WakeWordIPCConnectedClient(clientSocket, this);
                newConnectedClient.init();
                registerClient(newConnectedClient);
            } catch (Exception e) {
                log.warn("Could not accept/connect IPC client", e);
            }
        }
    }

    public synchronized void registerClient(WakeWordIPCConnectedClient newClient) {
        connectedClients.add(newClient);
        log.info("New IPC client was accepted, current of current clients is "
                + connectedClients.size());
    }

    public synchronized void unregisterClient(WakeWordIPCConnectedClient oldClient) {
        connectedClients.remove(oldClient);
        log.info(
                "IPC client was removed, current of current clients is " + connectedClients.size());
    }

    @Override
    public synchronized void sendCommand(IPCCommand command) throws IOException {
        log.debug("Sending command " + command + " to all connected clients");
        for (WakeWordIPCConnectedClient client : connectedClients) {
            client.send(command);
        }
    }

    public void processWakeWordDetected() {
        log.info("Wake Word Detected ......");
        (new Thread() {
            @Override
            public void run() {
                wakeWordDetected();
            }
        }).start();
    }
}
