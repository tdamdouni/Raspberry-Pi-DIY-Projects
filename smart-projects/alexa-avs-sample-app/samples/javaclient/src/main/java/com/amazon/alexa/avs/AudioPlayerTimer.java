/**
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */
package com.amazon.alexa.avs;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.TimeUnit;

/**
 * Since VLC's offsets are not accurate, this class manages calculating the correct offset using
 * System.nanoTime().
 */
public class AudioPlayerTimer {
    private static final Logger log = LoggerFactory.getLogger(AudioPlayerTimer.class);

    private long startNano;
    private long elapsedTimeMs;
    private long totalStreamLength;
    private boolean isPlaying = false;

    public synchronized void start() {
        log.debug("Starting AudioPlayerTimer");
        startNano = System.nanoTime();
        isPlaying = true;
    }

    public synchronized void stop() {
        log.debug("Stopping AudioPlayerTimer");
        if (isPlaying) {
            elapsedTimeMs += getCurrentOffsetInMilliseconds();
            isPlaying = false;
        }
    }

    public synchronized long getOffsetInMilliseconds() {
        long offset = elapsedTimeMs + (isPlaying ? getCurrentOffsetInMilliseconds() : 0);
        if (totalStreamLength > 0) {
            // If we know the length of the song, we don't want to send offsets that are beyond the
            // length. This is to correct the minor discrepancies between what VLC thinks is the end
            // of the song and what Java's internal timer thinks is the end of the song.
            offset = Math.min(totalStreamLength, offset);
        }
        log.debug("Getting offset. Offset: " + offset);
        return offset;
    }

    public void reset() {
        reset(0);
    }

    public void reset(long startPosition) {
        reset(startPosition, -1);
    }

    public synchronized void reset(long startPosition, long maxPosition) {
        log.debug("Resetting AudioPlayerTimer");
        elapsedTimeMs = startPosition;
        isPlaying = false;
        startNano = System.nanoTime();
        totalStreamLength = maxPosition;
    }

    private long getCurrentOffsetInMilliseconds() {
        return TimeUnit.MILLISECONDS.convert(System.nanoTime() - startNano, TimeUnit.NANOSECONDS);
    }
}
