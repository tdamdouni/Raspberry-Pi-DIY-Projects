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
package com.amazon.alexa.avs.http;

import com.amazon.alexa.avs.AVSRequest;
import com.amazon.alexa.avs.AudioInputFormat;
import com.amazon.alexa.avs.RequestListener;
import com.amazon.alexa.avs.ResultListener;
import com.amazon.alexa.avs.config.ObjectMapperFactory;
import com.amazon.alexa.avs.exception.AVSException;
import com.amazon.alexa.avs.exception.AVSJsonProcessingException;
import com.amazon.alexa.avs.exception.AlexaSystemException;
import com.amazon.alexa.avs.exception.AlexaSystemExceptionCode;
import com.amazon.alexa.avs.http.MultipartParser.MultipartParserConsumer;
import com.amazon.alexa.avs.http.jetty.InputStreamResponseListener;
import com.amazon.alexa.avs.http.jetty.PingSendingHttpClientTransportOverHTTP2;
import com.amazon.alexa.avs.http.jetty.PingSendingHttpClientTransportOverHTTP2.ConnectionListener;
import com.amazon.alexa.avs.message.Message;
import com.amazon.alexa.avs.message.request.RequestBody;
import com.amazon.alexa.avs.message.response.AlexaExceptionResponse;

import org.apache.commons.fileupload.MultipartStream;
import org.apache.commons.fileupload.MultipartStream.MalformedStreamException;
import org.apache.commons.io.IOUtils;
import org.apache.commons.lang3.StringUtils;
import org.codehaus.jackson.JsonGenerationException;
import org.codehaus.jackson.JsonProcessingException;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectWriter;
import org.eclipse.jetty.client.HttpClient;
import org.eclipse.jetty.client.api.ContentProvider;
import org.eclipse.jetty.client.api.Request;
import org.eclipse.jetty.client.api.Response;
import org.eclipse.jetty.client.util.StringContentProvider;
import org.eclipse.jetty.http.HttpHeader;
import org.eclipse.jetty.http.HttpMethod;
import org.eclipse.jetty.http.HttpStatus;
import org.eclipse.jetty.http2.client.HTTP2Client;
import org.eclipse.jetty.util.component.LifeCycle;
import org.eclipse.jetty.util.component.LifeCycle.Listener;
import org.eclipse.jetty.util.ssl.SslContextFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Optional;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Callable;
import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.TimeUnit;

public class AVSClient implements ConnectionListener {
    private static final Logger log = LoggerFactory.getLogger(AVSClient.class);

    private static final int REQUEST_TIMEOUT_IN_S = 15;
    private static final int REQUEST_ATTEMPTS = 3;
    private static final long REQUEST_RETRY_DELAY_MS = 1000;

    private static final String EVENTS_ENDPOINT = "/v20160207/events";
    private static final String DIRECTIVES_ENDPOINT = "/v20160207/directives";
    private final BlockingQueue<AVSRequest> requestQueue;

    static final String METADATA_NAME = "metadata";
    static final String AUDIO_NAME = "audio";

    public enum Resource {
        EVENTS(EVENTS_ENDPOINT, HttpMethod.POST),
        DIRECTIVES(DIRECTIVES_ENDPOINT, HttpMethod.GET);

        private final String path;
        private final HttpMethod method;

        Resource(String path, HttpMethod method) {
            this.path = path;
            this.method = method;
        }

        public String getPath() {
            return path;
        }

        public HttpMethod getMethod() {
            return method;
        }
    }

    private HttpClient httpClient;
    private URL host;

    private SslContextFactory sslContextFactory;
    private static String accessToken = "";
    private DownchannelRequestThread downchannelThread;
    private RequestThread requestThread;
    private MultipartParser requestResponseParser;
    private MultipartParser downchannelParser;
    private HTTP2Client http2Client;
    private ParsingFailedHandler parsingFailedHandler;
    private ResultListener resultListener;

    /**
     * Constructor that takes a host, a {@link MultipartParserConsumer}, and a {@link SslContextFactory} .
     * The provided {@link SslContextFactory} may allow bypassing server certificates, or handling
     * TLS/SSL in different ways.
     *
     * @param host
     *            The URL of the AVS host.
     * @param multipartParserConsumer
     *            The {@link MultipartParserConsumer} for executing the directives from the
     *            multipartParser.
     * @param sslContextFactory
     *            The {@link SslContextFactory} to use for validating certificates.
     * @param parsingFailedHandler
     *            The handler for handling parse failures.
     * @param resultListener
     *            The listener for checking that the downchannel has been set up
     * @throws Exception
     */
    public AVSClient(URL host, MultipartParserConsumer multipartParserConsumer,
            SslContextFactory sslContextFactory, ParsingFailedHandler parsingFailedHandler,
            ResultListener resultListener) throws Exception {
        http2Client = new HTTP2Client();
        this.host = host;
        this.sslContextFactory = sslContextFactory;
        requestQueue = new LinkedBlockingDeque<>();
        requestResponseParser = new MultipartParser(multipartParserConsumer);
        downchannelParser = new MultipartParser(multipartParserConsumer);

        this.parsingFailedHandler = parsingFailedHandler;

        this.resultListener = resultListener;

        createNewHttpClient();

        requestThread = new RequestThread(requestQueue);

        if (StringUtils.isNotBlank(accessToken)) {
            startRequestThread();
            startDownchannelThread();
        }
    }

    private void createNewHttpClient() throws Exception {

        if ((httpClient != null) && httpClient.isStarted()) {
            try {
                httpClient.stop();
            } catch (Exception e) {
                log.error("There was a problem stopping the HTTP client", e);
                throw e;
            }
        }

        // Sets up an HttpClient that sends HTTP/1.1 requests over an HTTP/2 transport
        httpClient = new HttpClient(new PingSendingHttpClientTransportOverHTTP2(http2Client, this),
                sslContextFactory);
        httpClient.addLifeCycleListener(new Listener() {

            @Override
            public void lifeCycleFailure(LifeCycle arg0, Throwable arg1) {
                log.error("HttpClient failed", arg1);
                StackTraceElement st[] = Thread.currentThread().getStackTrace();
                log.info(String.join(System.lineSeparator(), Arrays.toString(st)));
            }

            @Override
            public void lifeCycleStarted(LifeCycle arg0) {
                log.info("HttpClient started");
            }

            @Override
            public void lifeCycleStarting(LifeCycle arg0) {
                log.info("HttpClient starting");
            }

            @Override
            public void lifeCycleStopped(LifeCycle arg0) {
                log.info("HttpClient stopped");
            }

            @Override
            public void lifeCycleStopping(LifeCycle arg0) {
                log.info("HttpClient stopping");
                StackTraceElement st[] = Thread.currentThread().getStackTrace();
                log.info(String.join(System.lineSeparator(), Arrays.toString(st)));
            }

        });
        httpClient.start();

    }

    private Request createRequest(Resource resource, ContentProvider content) throws Exception {
        if (!httpClient.isStarted()) {
            log.error("HttpClient is stopped when it should be started");
            createNewHttpClient();
        }
        Request request = httpClient
                .newRequest(host.toString() + resource.getPath())
                .method(resource.getMethod());

        if (content != null) {
            request = request.content(content);
        }

        return request;
    }

    /**
     * Execute a request.
     *
     * @param avsRequest
     */
    private void doRequest(AVSRequest avsRequest) {

        Callable<Void> task = new Callable<Void>() {
            @Override
            public Void call() throws Exception {
                Request request =
                        createRequest(avsRequest.getResource(), avsRequest.getContentProvider());
                doRequestActual(request, avsRequest.getRequestListener(),
                        avsRequest.getMultipartParser());
                return null;
            }
        };

        try {
            avsRequest.getRetryPolicy().tryCall(task, RequestException.class);
        } catch (MultipartStream.MalformedStreamException e) {
            if (!e.getMessage().equals("Stream ended unexpectedly")) {
                log.error("Malformed stream exception", e);
            }
        } catch (Exception e) {
            log.error("There was a problem with the request.", e);
            avsRequest.getRequestListener().ifPresent(l -> l.onRequestError(e));
        }
    }

    /**
     * Execute the actual request to the server, wait for the response, and handle it.
     *
     * @param request
     *            The request to make.
     * @param requestListener
     *            The request listener to check request status.
     * @param multipartParser
     *            The {@link MultipartParser} to use for parsing the response to this request.
     * @throws AVSException
     *             is thrown when we get a non-2xx HTTP status code.
     * @throws IOException
     *             is thrown when parsing the multipart stream, and reading from the
     *             {@link InputStreamResponseListener}.
     */
    private void doRequestActual(Request request, Optional<RequestListener> requestListener,
            MultipartParser multipartParser) throws AVSException, IOException {
        request.header(HttpHeaders.AUTHORIZATION, "Bearer " + accessToken);

        InputStreamResponseListener responseListener = new InputStreamResponseListener();
        Response response;
        InputStream inputStream = null;

        try {
            // We have a request queue that maintains correct sequencing of events to appease the
            // server needing no events to happen in parallel. However, Downchannel requests don't
            // happen on that queue, they happen separately. By synchronizing here we can ensure
            // that no requests on the request queue will happen in parallel with the downchannel
            // requests.
            synchronized (this) {
                request.send(responseListener);
                response = responseListener.get(REQUEST_TIMEOUT_IN_S, TimeUnit.SECONDS);
            }
            inputStream = responseListener.getInputStream();
        } catch (Exception e) {
            IOUtils.closeQuietly(inputStream);
            throw new RequestException(e);
        }

        int statusCode = response.getStatus();
        log.info("Response code: {}", statusCode);
        log.info("Response headers: {}", response.getHeaders());

        // If 200 or 204, trigger the result listener
        if (statusCode == HttpStatus.OK_200) {
            requestListener.ifPresent(l -> l.onRequestSuccess());
        }

        if (statusCode == HttpStatus.NO_CONTENT_204) {
            requestListener.ifPresent(l -> l.onRequestSuccess());
            log.info("This response successfully had no content.");
            return;
        }

        String contentType = response.getHeaders().get(HttpHeader.CONTENT_TYPE);
        Optional<String> boundary =
                getHeaderParameter(contentType, HttpHeaders.Parameters.BOUNDARY);

        try {
            if (!boundary.isPresent()) {
                // This code assumes that System.Exception is only sent as a non-multipart response
                // This should throw an exception
                parseException(inputStream, multipartParser);

                // If the above doesn't throw the expected exception,
                // throw this exception instead
                throw new MalformedStreamException(
                        "A boundary is missing from the response headers. "
                                + "Unable to parse multipart stream.");
            }

            multipartParser.parseStream(inputStream, boundary.get());
        } catch (AVSJsonProcessingException e) {
            parsingFailedHandler.onParsingFailed(e.getUnparseable());
        } catch (JsonProcessingException e) {
            String unparseable = IOUtils.toString(inputStream);
            parsingFailedHandler.onParsingFailed(unparseable);
        } finally {
            IOUtils.closeQuietly(inputStream);
        }
    }

    /**
     * Parses an exception in the given byte array
     *
     * @throws AlexaSystemException
     *             Special case when the server message is itself an Exception.
     */
    public void parseException(InputStream inputStream, MessageParser parser)
            throws IOException, AlexaSystemException {
        ByteArrayOutputStream data = new ByteArrayOutputStream();
        IOUtils.copy(inputStream, data);
        Message message = parser.parseServerMessage(data.toByteArray());
        if (message instanceof AlexaExceptionResponse) {
            ((AlexaExceptionResponse) message).throwException();
        }
    }

    /**
     * Send an event with a {@link RequestBody}.
     *
     * @param body
     * @throws JsonMappingException
     * @throws JsonGenerationException
     * @throws IOException
     */
    public void sendEvent(RequestBody body)
            throws JsonGenerationException, JsonMappingException, IOException {
        sendEvent(body, null);
    }

    /**
     * Send an event with a {@link RequestBody}.
     *
     * @param body
     * @param listener
     * @throws JsonMappingException
     * @throws JsonGenerationException
     * @throws IOException
     */
    public void sendEvent(RequestBody body, RequestListener listener)
            throws JsonGenerationException, JsonMappingException, IOException {
        MultipartContentProvider multipartContent = new MultipartContentProvider();
        multipartContent.addPart(METADATA_NAME, createMetadataContent(body));

        enqueueRequest(new AVSRequest(Resource.EVENTS, multipartContent,
                new LinearRetryPolicy(REQUEST_RETRY_DELAY_MS, REQUEST_ATTEMPTS),
                requestResponseParser, listener));
    }

    /**
     * Send a speech recognition event with a {@link RequestBody}.
     *
     * @param body
     * @param inputStream
     * @param listener
     * @param audiotype
     * @throws IOException
     */
    public void sendEvent(RequestBody body, InputStream inputStream, RequestListener listener,
            AudioInputFormat audiotype)
            throws JsonGenerationException, JsonMappingException, IOException {

        AudioInputStreamContentProvider audioContent =
                new AudioInputStreamContentProvider(audiotype, inputStream);

        CachingContentProvider cachableContent = new CachingContentProvider(audioContent);

        MultipartContentProvider multipartContent = new MultipartContentProvider();
        multipartContent.addPart(METADATA_NAME, createMetadataContent(body));
        multipartContent.addPart(AUDIO_NAME, cachableContent);

        enqueueRequest(new AVSRequest(Resource.EVENTS, multipartContent,
                new LinearRetryPolicy(REQUEST_RETRY_DELAY_MS, REQUEST_ATTEMPTS),
                requestResponseParser, listener));
    }

    public void closeDownchannel() {
        if (downchannelThread != null) {
            downchannelThread.shutdownGracefully();
        }
    }

    /**
     * Get the Alexa Voice Service URL.
     *
     * @return URL the client is using for requests to Alexa Voice Service.
     */
    public URL getHost() {
        return host;
    }

    private StringContentProvider createMetadataContent(RequestBody body)
            throws JsonGenerationException, JsonMappingException, IOException {
        ObjectWriter writer = ObjectMapperFactory.getObjectWriter();
        log.info("Request metadata: \n{}",
                writer.withDefaultPrettyPrinter().writeValueAsString(body));
        String metadata = writer.writeValueAsString(body);
        StringContentProvider metadataContent =
                new StringContentProvider(ContentTypes.JSON, metadata, StandardCharsets.UTF_8);
        return metadataContent;
    }

    private void enqueueRequest(AVSRequest request) {
        if (!requestQueue.offer(request)) {
            log.error("Failed to enqueue request");
        }
    }

    private static Optional<String> getHeaderParameter(final String headerValue, final String key) {
        if ((headerValue == null) || (key == null)) {
            return Optional.ofNullable(null);
        }

        String[] parts = headerValue.split(";");
        for (String part : parts) {
            part = part.trim();
            if (part.startsWith(key)) {
                return Optional
                        .of(part.substring(key.length() + 1).replaceAll("(^\")|(\"$)", "").trim());
            }
        }

        return Optional.ofNullable(null);
    }

    /**
     * Set the access token to use for all requests to AVS.
     *
     * @param accessToken
     */

    private static void setAccessTokenValue(String accessToken){
        AVSClient.accessToken = accessToken;
    }

    public void setAccessToken(String accessToken) {
        setAccessTokenValue(accessToken);
        startRequestThread();
        startDownchannelThread();
    }

    public void revokeAccessToken() {
        setAccessTokenValue("");
        stopDownchannelThread();
    }

    private static void cacheAccessToken(String accessToken) {
        AVSClient.accessToken = accessToken;
    }

    void startRequestThread() {
        if (!requestThread.isAlive()) {
            requestThread.start();
        }
    }

    void startDownchannelThread() {
        stopDownchannelThread();
        downchannelThread = new DownchannelRequestThread();
        downchannelThread.start();
    }

    void stopDownchannelThread() {
        if (downchannelThread != null) {
            downchannelThread.shutdownGracefully();
        }
    }

    /**
     * When the application shuts down make sure to clean up the HTTPClient
     */
    public void shutdown() {
        try {
            downchannelThread.shutdownGracefully();
            httpClient.stop();
        } catch (Exception e) {
        }
    }

    /**
     * Thread for handling the long-lived response from the server for the downchannel communication
     * of directives.
     */
    private class DownchannelRequestThread extends Thread {
        private boolean running = true;

        public DownchannelRequestThread() {
            setName(this.getClass().getSimpleName());
        }

        public void shutdownGracefully() {
            downchannelParser.shutdownGracefully();
            running = false;
        }

        @Override
        public void run() {
            openConnection();
        }

        private void openConnection() {
            while (running) {
                log.info("Establishing downchannel");
                AVSRequest avsRequest = new AVSRequest(Resource.DIRECTIVES, null,
                        new ExponentialRetryPolicy(REQUEST_RETRY_DELAY_MS, REQUEST_ATTEMPTS),
                        downchannelParser, new RequestListener() {
                            @Override
                            public void onRequestError(Throwable e) {
                                if (shouldExceptionCauseShutdown(e)) {
                                    shutdownGracefully();
                                }
                                resultListener.onFailure();
                            }

                            @Override
                            public void onRequestSuccess() {
                                resultListener.onSuccess();
                            }

                            /**
                             * Determines if the encountered error is one that should cause the
                             * downchannel to shutdown.
                             *
                             * @param e
                             *            the encountered error
                             * @return true if the downchannel should be shutdown, false otherwise
                             */
                            private boolean shouldExceptionCauseShutdown(Throwable e) {
                                return (e instanceof AlexaSystemException)
                                        && (AlexaSystemExceptionCode.UNAUTHORIZED_REQUEST_EXCEPTION == ((AlexaSystemException) e)
                                                .getExceptionCode());
                            }

                        });

                doRequest(avsRequest);

                log.info("Finishing downchannel");
            }
        }
    }

    private class RequestThread extends Thread {
        private BlockingQueue<AVSRequest> queue;

        public RequestThread(BlockingQueue<AVSRequest> queue) {
            this.queue = queue;
            setName(this.getClass().getSimpleName());
        }

        @Override
        public void run() {
            while (true) {
                try {
                    AVSRequest request = queue.take();
                    doRequest(request);

                    request.getRequestListener().ifPresent(l -> l.onRequestFinished());
                } catch (InterruptedException e) {
                    log.error("Exception in the request thread", e);
                }
            }
        }
    }

    static class RequestException extends RuntimeException {
        private static final long serialVersionUID = 1L;

        public RequestException(Throwable cause) {
            super(cause);
        }
    }

    public static class MalformedResponseException extends RuntimeException {
        private static final long serialVersionUID = 1L;

        public MalformedResponseException(String message, Throwable cause) {
            super(message, cause);
        }

        public MalformedResponseException(String message) {
            super(message);
        }

        public MalformedResponseException(Throwable cause) {
            super(cause);
        }
    }

    @Override
    public void onConnected() {
        downchannelParser.onConnected();
    }

    @Override
    public void onDisconnected() {
        downchannelParser.onDisconnected();
    }
}
