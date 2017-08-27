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

import javax.sound.sampled.AudioFormat;

public enum AudioInputFormat {
    LPCM(Constants.LPCM_CHUNK_SIZE_BYTES, Constants.LPCM_CHUNK_SIZE_MS, Constants.LPCM_AUDIO_FORMAT, Constants.LPCM_CONTENT_TYPE);

    private final int chunkSizeBytes;
    private final int chunkSizeMs;
    private final AudioFormat audioFormat;
    private final String contentType;

    private AudioInputFormat(final int chunkSizeBytes, final int chunkSizeMs, AudioFormat audioFormat, final String contentType) {
        this.chunkSizeBytes = chunkSizeBytes;
        this.chunkSizeMs = chunkSizeMs;
        this.audioFormat = audioFormat;
        this.contentType = contentType;
    }

    public int getChunkSizeBytes() {
        return chunkSizeBytes;
    }

    public int getChunkSizeMs() {
        return chunkSizeMs;
    }

    public AudioFormat getAudioFormat() {
        return audioFormat;
    }

    public String getContentType() {
        return contentType;
    }

    private static final class Constants {
        private static final int LPCM_CHUNK_SIZE_BYTES = 320;
        private static final int LPCM_CHUNK_SIZE_MS = 10;
        private static final AudioFormat LPCM_AUDIO_FORMAT = new AudioFormat(16000f, 16, 1, true, false);
        private static final String LPCM_CONTENT_TYPE = "audio/L16; rate=16000; channels=1";
    }
}
