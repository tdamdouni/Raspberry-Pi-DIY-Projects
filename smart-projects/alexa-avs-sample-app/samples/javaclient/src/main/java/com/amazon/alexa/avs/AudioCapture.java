/**
 * Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Amazon Software License (the "License"). You may not use this file
 * except in compliance with the License. A copy of the License is located at
 *
 * http://aws.amazon.com/asl/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
 */
package com.amazon.alexa.avs;

import java.io.IOException;
import java.io.InputStream;
import java.io.PipedInputStream;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.TargetDataLine;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class AudioCapture {
    private static AudioCapture sAudioCapture;
    private TargetDataLine microphoneLine;
    private AudioFormat audioFormat;
    private AudioBufferThread thread;

    private static final int BUFFER_SIZE_IN_SECONDS = 6;

    private int BUFFER_SIZE_IN_BYTES;

    private static final Logger log = LoggerFactory.getLogger(AudioCapture.class);

    public static AudioCapture getAudioHardware(final AudioFormat audioFormat,
                                                MicrophoneLineFactory microphoneLineFactory) throws LineUnavailableException {
        if (sAudioCapture == null) {
            sAudioCapture = new AudioCapture(audioFormat, microphoneLineFactory);
        }
        return sAudioCapture;
    }

    protected AudioCapture() {}

    private AudioCapture(final AudioFormat audioFormat, MicrophoneLineFactory microphoneLineFactory)
            throws LineUnavailableException {
        super();
        this.audioFormat = audioFormat;
        microphoneLine = microphoneLineFactory.getMicrophone();
        if (microphoneLine == null) {
            throw new LineUnavailableException();
        }
        BUFFER_SIZE_IN_BYTES = (int) ((audioFormat.getSampleSizeInBits() * audioFormat.getSampleRate()) / 8
                * BUFFER_SIZE_IN_SECONDS);
    }

    public InputStream getAudioInputStream(final RecordingStateListener stateListener,
                                           final RecordingRMSListener rmsListener) throws LineUnavailableException, IOException {
        try {
            startCapture();
            PipedInputStream inputStream = new PipedInputStream(BUFFER_SIZE_IN_BYTES);
            thread = new AudioBufferThread(inputStream, stateListener, rmsListener);
            thread.start();
            return inputStream;
        } catch (LineUnavailableException | IOException e) {
            stopCapture();
            throw e;
        }
    }

    public void stopCapture() {
        microphoneLine.stop();
        microphoneLine.close();

    }

    private void startCapture() throws LineUnavailableException {
        microphoneLine.open(audioFormat);
        microphoneLine.start();
    }

    public int getAudioBufferSizeInBytes() {
        return BUFFER_SIZE_IN_BYTES;
    }

    private class AudioBufferThread extends Thread {

        private final AudioStateOutputStream audioStateOutputStream;

        public AudioBufferThread(PipedInputStream inputStream,
                                 RecordingStateListener recordingStateListener, RecordingRMSListener rmsListener)
                throws IOException {
            audioStateOutputStream =
                    new AudioStateOutputStream(inputStream, recordingStateListener, rmsListener);
        }

        @Override
        public void run() {
            while (microphoneLine.isOpen()) {
                copyAudioBytesFromInputToOutput();
            }
            closePipedOutputStream();
        }

        private void copyAudioBytesFromInputToOutput() {
            byte[] data = new byte[microphoneLine.getBufferSize() / 5];
            int numBytesRead = microphoneLine.read(data, 0, data.length);
            try {
                audioStateOutputStream.write(data, 0, numBytesRead);
            } catch (IOException e) {
                stopCapture();
            }
        }

        private void closePipedOutputStream() {
            try {
                audioStateOutputStream.close();
            } catch (IOException e) {
                log.error("Failed to close audio stream ", e);
            }
        }
    }

}
