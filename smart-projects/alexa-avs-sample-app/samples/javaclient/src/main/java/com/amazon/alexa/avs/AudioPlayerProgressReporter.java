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
package com.amazon.alexa.avs;

import com.amazon.alexa.avs.message.response.ProgressReport;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

public class AudioPlayerProgressReporter {
    private final ScheduledExecutorService eventScheduler = Executors.newScheduledThreadPool(1);
    private static final Logger log = LoggerFactory.getLogger(AudioPlayerProgressReporter.class);

    private ScheduledFuture<?> progressReportDelayFuture;
    private ScheduledFuture<?> progressReportIntervalFuture;

    private final Runnable progressReportDelayRunnable;
    private final Runnable progressReportIntervalRunnable;

    private final AudioPlayerTimer audioPlayerTimer;

    private long progressReportDelay;
    private long progressReportInterval;
    private boolean isSetup;

    public AudioPlayerProgressReporter(Runnable progressReportDelayRunnable,
            Runnable progressReportIntervalRunnable,
            AudioPlayerTimer audioPlayerTimer) {
        if (progressReportDelayRunnable == null ||
                progressReportIntervalRunnable == null ||
                audioPlayerTimer == null) {
            throw new IllegalArgumentException("All arguments must be provided.");
        }

        this.progressReportDelayRunnable = progressReportDelayRunnable;
        this.progressReportIntervalRunnable = progressReportIntervalRunnable;
        this.audioPlayerTimer = audioPlayerTimer;
        this.isSetup = false;
    }

    /**
     * Setup the AudioPlayerProgressReporter to send progress report events for the given
     * ProgressReport object. This method should be called before start().
     *
     * @param progressReport
     *            Object containing how long to wait for both the delay and interval reports
     * @throws IllegalArgumentException
     *            Is thrown if the required ProgressReport param is not given
     * @throws IllegalStateException
     *            Is thrown if the AudioPlayerProgressReporter is already setup
     */
    public synchronized void setup(ProgressReport progressReport) {
        if (progressReport == null) {
            String errorMessage = "ProgressReport must not be null.";
            log.error(errorMessage);
            throw new IllegalArgumentException(errorMessage);
        }
        if (isSetup) {
            String errorMessage = "AudioPlayerProgressReporter has already been setup. Please disable it before setting it up again.";
            log.error(errorMessage);
            throw new IllegalStateException(errorMessage);
        }

        cancelEvents();
        progressReportDelay = progressReport.getProgressReportDelayInMilliseconds();
        progressReportInterval = progressReport.getProgressReportIntervalInMilliseconds();
        isSetup = true;
    }

    /**
     * Disable the AudioPlayerProgressReporter so that it won't send any more events until
     * it is reset by a call to setup(progressReport).
     */
    public synchronized void disable() {
        isSetup = false;
        cancelEvents();
        progressReportDelay = 0;
        progressReportInterval = 0;
    }

    /**
     * Start (or resume) sending progress report events. This method takes into account
     * the current position within the audio track to determine when to report events.
     *
     * Since the ProgressReportDelayElapsed event should only be sent once per track,
     * if the ProgressReportDelay has already passed it should not be sent again.
     *
     * ProgressReportIntervalElapsed should be sent on a periodic interval based on
     * how long the track has been playing.
     *
     * This method can only be called after setup(progressReport). An IllegalStateException
     * will be thrown if this is not the case.
     *
     * @throws IllegalStateException
     *            Is thrown if the AudioPlayerProgressReporter has not previously been setup
     */
    public synchronized void start() {
        // If the reporter is being started again, we need to cancel any existing report threads
        // to ensure there are no duplicates
        cancelEvents();

        if (!isSetup) {
            String errorMessage = "AudioPlayerProgressReporter cannot be started because it has not been setup yet.";
            log.error(errorMessage);
            throw new IllegalStateException(errorMessage);
        }

        long currentOffsetIntoTrack = audioPlayerTimer.getOffsetInMilliseconds();

        long timeUntilDelayReport = progressReportDelay - currentOffsetIntoTrack;
        if (timeUntilDelayReport > 0) {
            scheduleDelayEvent(timeUntilDelayReport);
        }

        long timeUntilIntervalReport = progressReportInterval == 0 ? 0 :
                progressReportInterval - (currentOffsetIntoTrack % progressReportInterval);
        if (timeUntilIntervalReport > 0) {
            scheduleIntervalEvent(timeUntilIntervalReport, progressReportInterval);
        }
    }

    /**
     * Stop (or pause) sending progress report events.
     */
    public synchronized void stop() {
        cancelEvents();
    }

    /**
     * Determine whether the AudioPlayerProgressReporter is currently setup and ready to send
     * progress report events.
     *
     * @return true if the reporter is setup and ready to send reports, false otherwise
     */
    public synchronized boolean isSetup() {
        return isSetup;
    }

    /**
     * Schedules the ProgressReportDelayElapsed event.
     * @param delay
     *            Delay in ms until the event should fire.
     */
    private void scheduleDelayEvent(long delay) {
        log.debug("Scheduling ProgressReportDelayElapsed event in {} ms", String.valueOf(delay));
        progressReportDelayFuture = eventScheduler.schedule(progressReportDelayRunnable, delay,
                TimeUnit.MILLISECONDS);
    }

    /**
     * Schedules the ProgressReportIntervalElapsed event.
     * @param delay
     *            Delay in ms until the event should first fire.
     * @param interval
     *            Period in ms between firing of the event.
     */
    private void scheduleIntervalEvent(long delay, long interval) {
        log.debug("Scheduling ProgressReportIntervalElapsed event in {} ms that will repeat every {} ms",
                String.valueOf(delay), String.valueOf(interval));
        progressReportIntervalFuture = eventScheduler.scheduleAtFixedRate(
                progressReportIntervalRunnable, delay, interval, TimeUnit.MILLISECONDS);
    }

    private void cancelEvents() {
        if (progressReportDelayFuture != null && !progressReportDelayFuture.isDone()) {
            progressReportDelayFuture.cancel(false);
        }

        if (progressReportIntervalFuture != null && !progressReportIntervalFuture.isDone()) {
            progressReportIntervalFuture.cancel(false);
        }
    }
}
