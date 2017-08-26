/**
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */
package com.amazon.alexa.avs.audio;

import org.apache.commons.io.IOUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.InputStream;

import javazoom.jl.player.Player;

public class AudioPlayer {
    private static final Logger log = LoggerFactory.getLogger(AudioPlayer.class);

    public AudioPlayer() {
    }

    /**
     * Play the given input stream. Note: This method blocks.
     *
     * @param inputStream
     *            MP3 Audio bytes to play
     */
    public void play(InputStream inputStream) {
        try {
            Player player = new Player(inputStream);
            player.play();
        } catch (Exception e) {
            log.error("An error occurred while trying to play audio", e);
        } finally {
            IOUtils.closeQuietly(inputStream);
        }
    }
}
