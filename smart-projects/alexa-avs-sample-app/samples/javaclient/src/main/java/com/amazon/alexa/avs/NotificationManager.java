/**
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */
package com.amazon.alexa.avs;

import com.amazon.alexa.avs.DataStore.ResultListener;
import com.amazon.alexa.avs.audio.SimpleAudioPlayer;
import com.amazon.alexa.avs.config.ObjectMapperFactory;
import com.amazon.alexa.avs.http.BasicHttpClient;
import com.amazon.alexa.avs.message.request.context.NotificationsStatePayload;
import com.amazon.alexa.avs.message.response.notifications.SetIndicator;
import com.amazon.alexa.avs.message.response.notifications.SetIndicator.Asset;

import org.apache.commons.io.IOUtils;
import org.codehaus.jackson.map.ObjectReader;
import org.codehaus.jackson.type.TypeReference;
import org.eclipse.jetty.util.ssl.SslContextFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.UUID;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicReference;

public class NotificationManager {
    private static final Logger log = LoggerFactory.getLogger(NotificationManager.class);
    private static final String NOTIFICATION_STATUS_FILENAME = "notificationIndicator.json";
    private static final long ASSET_DOWNLOAD_TIMEOUT =
            TimeUnit.MILLISECONDS.convert(3, TimeUnit.SECONDS);

    private final ClassLoader resLoader; // used to load resource files
    private final NotificationIndicator notificationIndicator;
    private final SimpleAudioPlayer player;
    private final BasicHttpClient httpClient;

    private ExecutorService indicatorExecutor;
    private ExecutorService assetDownloader;
    private Map<String, File> assets;
    private Set<Future<?>> indicatorFutures;
    private FileDataStore<NotificationsStatePayload> dataStore;
    private AtomicBoolean allowPersistentIndicator;
    private Status indicatorStatus;
    private AtomicBoolean isSetIndicatorPersisted;
    private AtomicReference<String> activeAudioAsset;

    /**
     *
     * @param indicator
     *            Notification indicator for providing visual information to the user about
     *            notification state.
     * @param audioPlayer
     *            Audio player responsible for playing the audio asset that accompanies each
     *            SetIndicator directive
     */
    public NotificationManager(NotificationIndicator indicator, SimpleAudioPlayer audioPlayer) {
        this(indicator, audioPlayer, new BasicHttpClient(new SslContextFactory()),
                new NotificationsFileDataStore(NOTIFICATION_STATUS_FILENAME));
    }

    NotificationManager(NotificationIndicator indicator, SimpleAudioPlayer audioPlayer,
            BasicHttpClient httpClient, FileDataStore<NotificationsStatePayload> dataStore) {
        this.notificationIndicator = indicator;
        this.player = audioPlayer;
        this.assets = Collections.synchronizedMap(new HashMap<String, File>());
        this.indicatorExecutor = Executors.newSingleThreadExecutor();
        this.assetDownloader = Executors.newCachedThreadPool();
        this.allowPersistentIndicator = new AtomicBoolean(true);
        this.httpClient = httpClient;
        this.isSetIndicatorPersisted = new AtomicBoolean(false);
        this.indicatorStatus = Status.NONE;
        this.dataStore = dataStore;
        this.indicatorFutures = Collections.synchronizedSet(new HashSet<Future<?>>());
        this.activeAudioAsset = new AtomicReference<String>("");
        this.resLoader = Thread.currentThread().getContextClassLoader();
    }

    private Optional<Future<?>> cacheAudioIndicators(SetIndicator setIndicator) {
        if (setIndicator.shouldPlayAudioIndicator()) {
            SetIndicator.Asset asset = setIndicator.getAsset();
            if (asset != null) {
                String assetId = asset.getAssetId();
                boolean assetAlreadyDownloaded = assets.containsKey(assetId);
                if (!assetAlreadyDownloaded) {
                    return Optional.of(this.assetDownloader.submit(new Runnable() {
                        @Override
                        public void run() {
                            File temp;
                            try {
                                InputStream input =
                                        httpClient.downloadResourceAtUrl(asset.getUrl());
                                temp = File.createTempFile(UUID.randomUUID().toString(), ".mp3");
                                log.debug("Created asset file: {}", temp.getAbsolutePath());
                                temp.deleteOnExit();
                                IOUtils.copy(input, new FileOutputStream(temp));
                                assets.put(assetId, temp);
                            } catch (IOException e) {
                                log.error("Temporary file could not be created.");
                            } catch (Exception e) {
                                log.error("Unrecoverable exception downloading file", e);
                            }
                        }
                    }));
                }
            }
        }
        return Optional.empty();
    }

    private boolean waitForAsset(Asset asset, Optional<Future<?>> audioAssetDownloadFuture) {
        if (asset != null && audioAssetDownloadFuture.isPresent()) {
            Future<?> audioAsset = audioAssetDownloadFuture.get();
            try {
                audioAsset.get(ASSET_DOWNLOAD_TIMEOUT, TimeUnit.MILLISECONDS);
                if (assets.containsKey(asset.getAssetId())) {
                    return true;
                }
            } catch (TimeoutException e) {
                log.error("Timout expired before notification asset downloaded", e);
            } catch (InterruptedException | ExecutionException e) {
                log.error("Asset download thread interrupted before notification asset downloaded",
                        e);
            }
        }
        return false;
    }

    private void setIndicatorStatus(Status status) {
        switch (status) {
            case NEW:
                this.notificationIndicator.onNewNotification();
                break;
            case QUEUED:
                this.notificationIndicator.onQueuedNotifications();
                break;
            default:
                this.notificationIndicator.onClearNotifications();
        }
        this.indicatorStatus = status;
        this.dataStore.writeToDisk(getState(), new ResultListener<NotificationsStatePayload>() {

            @Override
            public void onSuccess(NotificationsStatePayload p) {
                log.debug("Persisted notification status to disk: {}", p);
            }

            @Override
            public void onFailure() {
                log.error("Failed to persist notification status to disk");
            }

        });
    }

    public void handleSetIndicator(final SetIndicator setIndicator) {
        isSetIndicatorPersisted.set(setIndicator.shouldPersistVisualIndicator());
        final Optional<Future<?>> audioAssetDownloadFuture = cacheAudioIndicators(setIndicator);
        allowPersistentIndicator.set(true);
        // If we're already playing this notification, don't queue it up a second time.
        String assetId = setIndicator.getAsset().getAssetId();
        if (!activeAudioAsset.get().equals(assetId)) {
            if (activeAudioAsset.get().equals("")) {
                activeAudioAsset.set(assetId == null ? "" : assetId);
            }
            indicatorFutures.add(indicatorExecutor.submit(new Runnable() {
                @Override
                public void run() {
                    log.debug("Handling SetIndicator");
                    Asset asset = setIndicator.getAsset();
                    String assetId = asset.getAssetId();
                    activeAudioAsset.set(assetId == null ? "" : assetId);
                    if (setIndicator.shouldPlayAudioIndicator()) {
                        boolean downloadSuccess = waitForAsset(asset, audioAssetDownloadFuture);
                        setIndicatorStatus(Status.NEW);
                        playAudioIndicator(asset, downloadSuccess);
                    }
                    // Should transition to "unheard notifications" indicator?
                    if (setIndicator.shouldPersistVisualIndicator()) {
                        if (allowPersistentIndicator.get()) {
                            setIndicatorStatus(Status.QUEUED);
                        }
                    } else {
                        setIndicatorStatus(Status.NONE);
                    }
                    activeAudioAsset.set("");
                    log.debug("Done handling SetIndicator");
                }
            }));
        }
        cleanUpIndicatorFutures();
    }

    private void playAudioIndicator(Asset asset, boolean downloadSuccess) {
        InputStream inputStream = null;
        try {
            if (downloadSuccess) {
                File assetFile = assets.get(asset.getAssetId());
                inputStream = new FileInputStream(assetFile);
                log.debug("Successfully downloaded notification sound.");
            } else {
                log.debug("Could not download notification sound. Falling back to default.");
                inputStream = resLoader.getResourceAsStream("res/default_notification_sound.mp3");
            }
            player.play(inputStream);
        } catch (FileNotFoundException e) {
            log.error("Could not play notification sound", e);
        } finally {
            IOUtils.closeQuietly(inputStream);
        }
    }

    private void cleanUpIndicatorFutures() {
        synchronized (indicatorFutures) {
            Iterator<Future<?>> it = indicatorFutures.iterator();
            while (it.hasNext()) {
                Future<?> f = it.next();
                if (f.isDone() || f.isCancelled()) {
                    it.remove();
                }
            }
        }
    }

    public void handleClearIndicator() {
        allowPersistentIndicator.set(false);
        synchronized (indicatorFutures) {
            for (Future<?> f : indicatorFutures) {
                f.cancel(true);
            }
        }
        indicatorFutures.clear();
        setIndicatorStatus(Status.NONE);
    }

    public NotificationsStatePayload getState() {
        return new NotificationsStatePayload(this.indicatorStatus.isEnabled,
                isSetIndicatorPersisted.get());
    }

    public void loadFromDisk(com.amazon.alexa.avs.ResultListener listener) {
        dataStore.loadFromDisk(new ResultListener<NotificationsStatePayload>() {

            @Override
            public void onSuccess(NotificationsStatePayload payload) {
                log.debug("Loaded notification indicator state from disk");
                if (payload != null) {
                    isSetIndicatorPersisted.set(payload.getIsVisualIndicatorPersisted());
                    if (payload.getIsEnabled()) {
                        setIndicatorStatus(Status.QUEUED);
                    }
                }
                listener.onSuccess();
            }

            @Override
            public void onFailure() {
                listener.onFailure();
            }

        });
    }

    static enum Status {
        NEW(true),
        QUEUED(true),
        NONE(false);

        // True if this status indicates that the indicator is "on" in some form
        private boolean isEnabled;

        Status(boolean hasNotifications) {
            this.isEnabled = hasNotifications;
        }
    }

    private static class NotificationsFileDataStore
            extends FileDataStore<NotificationsStatePayload> {

        public NotificationsFileDataStore(String filename) {
            super(filename);
        }

        protected ObjectReader getObjectReader() {
            return ObjectMapperFactory
                    .getObjectReader()
                    .withType(new TypeReference<NotificationsStatePayload>() {
                    });
        }
    }
}
