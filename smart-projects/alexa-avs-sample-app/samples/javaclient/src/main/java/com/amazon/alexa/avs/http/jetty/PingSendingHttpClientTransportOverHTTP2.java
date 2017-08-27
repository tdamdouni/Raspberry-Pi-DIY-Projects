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
package com.amazon.alexa.avs.http.jetty;

import org.eclipse.jetty.client.HttpClient;
import org.eclipse.jetty.client.HttpDestination;
import org.eclipse.jetty.client.Origin;
import org.eclipse.jetty.client.api.Connection;
import org.eclipse.jetty.http2.api.Session;
import org.eclipse.jetty.http2.client.HTTP2Client;
import org.eclipse.jetty.http2.client.http.HttpClientTransportOverHTTP2;
import org.eclipse.jetty.http2.client.http.HttpConnectionOverHTTP2;
import org.eclipse.jetty.http2.client.http.HttpDestinationOverHTTP2;
import org.eclipse.jetty.http2.frames.PingFrame;
import org.eclipse.jetty.util.Callback;

import java.util.Optional;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

/**
 * Sends an HTTP/2 PING frame every 5 minutes after a connection is opened.
 */
public class PingSendingHttpClientTransportOverHTTP2 extends HttpClientTransportOverHTTP2 {
    private static final int PING_INTERVAL_IN_MINUTES = 5;
    private static final int INITIAL_PING_DELAY_IN_MINUTES = PING_INTERVAL_IN_MINUTES;
    private final ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
    private Optional<ConnectionListener> connectionListener = Optional.empty();
    private HttpClient httpClient;

    public PingSendingHttpClientTransportOverHTTP2(HTTP2Client client, ConnectionListener connectionListener) {
        super(client);
        this.connectionListener = Optional.ofNullable(connectionListener);
    }

    @Override
    public void setHttpClient(HttpClient client) {
        super.setHttpClient(client);
        httpClient = client;
    }

    @Override
    protected HttpConnectionOverHTTP2 newHttpConnection(HttpDestination destination, Session session) {
        scheduler.scheduleAtFixedRate(new ServerPing(session), INITIAL_PING_DELAY_IN_MINUTES,
                PING_INTERVAL_IN_MINUTES, TimeUnit.MINUTES);
        return super.newHttpConnection(destination, session);
    }

    @Override
    public HttpDestination newHttpDestination(Origin origin) {
        return new ConnectionStatusHttpDestinationOverHTTP2(httpClient, origin);
    }

    /**
     * A {@link HttpDestinationOverHTTP2} to let the listener know when the connection is opened or closed.
     */
    public class ConnectionStatusHttpDestinationOverHTTP2 extends HttpDestinationOverHTTP2 {
        public ConnectionStatusHttpDestinationOverHTTP2(HttpClient client, Origin origin) {
            super(client, origin);
        }

        @Override
        public void close(Connection connection) {
            super.close(connection);
            connectionListener.ifPresent(l -> l.onDisconnected());
        }

        @Override
        public void succeeded(Connection connection) {
            super.succeeded(connection);
            connectionListener.ifPresent(l -> l.onConnected());
        }
    }

    /**
     * Task to send a PING frame over an open HTTP/2 Session.
     */
    private static class ServerPing implements Runnable {
        private Session session;

        private ServerPing(Session session) {
            this.session = session;
        }

        @Override
        public void run() {
            if (!session.isClosed()) {
                PingFrame frame = new PingFrame(false);
                session.ping(frame, Callback.NOOP);
            }
        }
    }

    /**
     * Listener to inform others of the connection being opened or closed.
     */
    public interface ConnectionListener {
        void onConnected();
        void onDisconnected();
    }
}
