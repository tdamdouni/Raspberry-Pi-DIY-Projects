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

import com.amazon.alexa.avs.message.request.RequestBody;
import com.amazon.alexa.avs.message.request.RequestFactory;
import com.amazon.alexa.avs.message.request.audioplayer.PlaybackFailedPayload.ErrorType;
import com.amazon.alexa.avs.message.request.context.PlaybackStatePayload;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.EnumSet;
import java.util.Set;

/**
 * The AudioPlayerStateMachine enforces the correct ordering and number of PlaybackEvents sent
 * during audio playback, and keeps track of the audio player state. The audio player state has four
 * supported states.
 *
 * <ul>
 * <li>Idle, the state which the machine starts out in (no media playback has happened).</li>
 * <li>Playing, state corresponding to the client handle a media item and playing it</li>
 * <li>Stopped, state corresponding to the client previously playing a media item and was stopped
 * <li>Finished, state corresponding to when the client has finished playing a media item</li>
 * </ul>
 *
 * AudioPlayerStateMachine provides all the transitions between these states, and sends any playback
 * events required.
 */
public class AudioPlayerStateMachine {

    private static final Logger log = LoggerFactory.getLogger(AudioPlayerStateMachine.class);

    // Current State
    private State<AudioPlayerState> state;

    // State Transitions
    private final PlaybackStarted playbackStarted;
    private final DelayProgressReport delayReport;
    private final IntervalProgressReport intervalReport;
    private final PlaybackFailed playbackFailed;
    private final PlaybackNearlyFinished playbackNearlyFinished;
    private final PlaybackStutterStarted playbackStutterStarted;
    private final PlaybackStutterFinished playbackStutterFinished;
    private final PlaybackFinished playbackFinished;
    private final PlaybackStopped playbackStopped;
    private final ClearQueueEnqueued clearQueueEnqueued;
    private final ClearQueueAll clearQueueAll;
    private final PlayReplaceAll playReplaceAll;
    private final PlaybackPaused playbackPaused;
    private final PlaybackResumed playbackResumed;

    public AudioPlayerStateMachine(AVSAudioPlayer audioPlayer, AVSController controller) {
        state = new State<AudioPlayerState>(AudioPlayerState.IDLE);

        playbackFinished =
                new PlaybackFinished(EnumSet.of(AudioPlayerState.PLAYING), audioPlayer, controller);
        clearQueueEnqueued = new ClearQueueEnqueued(EnumSet.allOf(AudioPlayerState.class),
                audioPlayer, controller);
        clearQueueAll =
                new ClearQueueAll(EnumSet.allOf(AudioPlayerState.class), audioPlayer, controller);
        playReplaceAll =
                new PlayReplaceAll(EnumSet.allOf(AudioPlayerState.class), audioPlayer, controller);
        playbackStarted = new PlaybackStarted(
                EnumSet.of(AudioPlayerState.STOPPED, AudioPlayerState.FINISHED,
                        AudioPlayerState.IDLE, AudioPlayerState.PAUSED, AudioPlayerState.PLAYING),
                audioPlayer, controller);
        delayReport = new DelayProgressReport(EnumSet.of(AudioPlayerState.PLAYING), audioPlayer,
                controller);
        intervalReport = new IntervalProgressReport(EnumSet.of(AudioPlayerState.PLAYING),
                audioPlayer, controller);
        playbackFailed =
                new PlaybackFailed(EnumSet.allOf(AudioPlayerState.class), audioPlayer, controller);
        playbackNearlyFinished = new PlaybackNearlyFinished(EnumSet.allOf(AudioPlayerState.class),
                audioPlayer, controller);
        playbackStopped =
                new PlaybackStopped(EnumSet.allOf(AudioPlayerState.class), audioPlayer, controller);
        playbackStutterStarted = new PlaybackStutterStarted(EnumSet.of(AudioPlayerState.PLAYING),
                audioPlayer, controller);
        playbackStutterFinished = new PlaybackStutterFinished(
                EnumSet.of(AudioPlayerState.BUFFER_UNDERRUN), audioPlayer, controller);
        playbackPaused = new PlaybackPaused(
                EnumSet.of(AudioPlayerState.PLAYING, AudioPlayerState.STOPPED,
                        AudioPlayerState.IDLE, AudioPlayerState.BUFFER_UNDERRUN),
                audioPlayer, controller);
        playbackResumed =
                new PlaybackResumed(EnumSet.of(AudioPlayerState.PAUSED), audioPlayer, controller);
    }

    /**
     * Transitions into the playing state sending playback started events
     */
    public synchronized void playbackStarted() {
        log.debug(PlaybackStarted.class.getSimpleName());
        playbackStarted.transition(state);
    }

    /**
     * Transitions into the buffer underrun state sending playback stutter started events
     */
    public synchronized void playbackStutterStarted() {
        log.debug(PlaybackStutterStarted.class.getSimpleName());
        playbackStutterStarted.transition(state);
    }

    /**
     * Transitions into the playing state sending playback stutter finished events
     */
    public synchronized void playbackStutterFinished() {
        log.debug(PlaybackStutterFinished.class.getSimpleName());
        playbackStutterFinished.transition(state);
    }

    /**
     * Transitions from playing state into the stopped state sending playback stopped events.
     * Alternatively if the player is in IDLE, it will remain in idle
     */
    public synchronized void playbackStopped() {
        log.debug(PlaybackStopped.class.getSimpleName());
        playbackStopped.transition(state);
    }

    /**
     * Transitions to the appropriate state, sending playback queue cleared events.
     */
    public synchronized void clearQueueEnqueued() {
        log.debug(ClearQueueEnqueued.class.getSimpleName());
        clearQueueEnqueued.transition(state);
    }

    /**
     * Transitions to the appropriate state, sending playback queue cleared events.
     */
    public synchronized void clearQueueAll() {
        log.debug(ClearQueueAll.class.getSimpleName());
        clearQueueAll.transition(state);
    }

    /**
     * Transitions to stopped if currently playing, sending playback stopped event.
     */
    public synchronized void playReplaceAll() {
        log.debug(PlayReplaceAll.class.getSimpleName());
        playReplaceAll.transition(state);
    }

    /**
     * Transitions from playing to playing, sending playback error events.
     */
    public synchronized void playbackFailed() {
        log.debug(PlaybackFailed.class.getSimpleName());
        playbackFailed.transition(state);
    }

    /**
     * Transitions from playing to playing, sending playback progress delay report events.
     */
    public synchronized void reportProgressDelay() {
        log.debug(DelayProgressReport.class.getSimpleName());
        delayReport.transition(state);
    }

    /**
     * Transitions from playing to playing, sending playback progress interval report events.
     */
    public synchronized void reportProgressInterval() {
        log.debug(IntervalProgressReport.class.getSimpleName());
        intervalReport.transition(state);
    }

    /**
     * Transitions from current state to current state sending playback nearly finished events.
     */
    public synchronized void playbackNearlyFinished() {
        log.debug(PlaybackNearlyFinished.class.getSimpleName());
        playbackNearlyFinished.transition(state);
    }

    /**
     * Transitions from playing to finished, sending playback finished events.
     */
    public synchronized void playbackFinished() {
        log.debug(PlaybackFinished.class.getSimpleName());
        playbackFinished.transition(state);
    }

    /**
     * Transitions from playing to paused.
     */
    public synchronized void playbackPaused() {
        log.debug(PlaybackPaused.class.getSimpleName());
        playbackPaused.transition(state);
    }

    /**
     * Transitions from paused to playing.
     */
    public synchronized void playbackResumed() {
        log.debug(PlaybackResumed.class.getSimpleName());
        playbackResumed.transition(state);
    }

    public AudioPlayerState getState() {
        return state.get();
    }

    public enum AudioPlayerState {
        IDLE,
        PLAYING,
        PAUSED,
        FINISHED,
        STOPPED,
        BUFFER_UNDERRUN;
    }

    private static abstract class AudioPlayerStateTransition
            extends StateTransition<AudioPlayerState> {

        private final AVSAudioPlayer audioPlayer;
        private final AVSController controller;

        public AudioPlayerStateTransition(Set<AudioPlayerState> validStartStates,
                AVSAudioPlayer audioPlayer, AVSController controller) {
            super(validStartStates);
            this.audioPlayer = audioPlayer;
            this.controller = controller;
        }

        protected final void sendRequest(RequestBody requestBody) {
            controller.sendRequest(requestBody);
        }

        protected final PlaybackStatePayload getCurrentPlaybackState() {
            return audioPlayer.getPlaybackState();
        }

        protected final String getCurrentStreamToken() {
            return audioPlayer.getCurrentStreamToken();
        }

        protected final long getCurrentOffsetInMilliseconds() {
            return audioPlayer.getCurrentOffsetInMilliseconds();
        }

        protected final long getPlaybackStutterStartedTimestampMs() {
            return audioPlayer.getPlaybackStutterStartedOffsetInMilliseconds();
        }

        @Override
        protected void onInvalidStartState(State<AudioPlayerState> startState) {
            log.error("Invalid {} from {}.", this.getClass().getSimpleName(), startState.get());
        }
    }

    private static class PlaybackStarted extends AudioPlayerStateTransition {

        public PlaybackStarted(Set<AudioPlayerState> validStartStates, AVSAudioPlayer audioPlayer,
                AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            state.set(AudioPlayerState.PLAYING);
            sendRequest(RequestFactory.createAudioPlayerPlaybackStartedEvent(
                    getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
        }
    }

    private static class PlaybackStopped extends AudioPlayerStateTransition {

        public PlaybackStopped(Set<AudioPlayerState> validStartStates, AVSAudioPlayer audioPlayer,
                AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            if (state.get() != AudioPlayerState.IDLE) {
                state.set(AudioPlayerState.STOPPED);
                sendRequest(RequestFactory.createAudioPlayerPlaybackStoppedEvent(
                        getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
            }
        }
    }

    private static class DelayProgressReport extends AudioPlayerStateTransition {

        public DelayProgressReport(Set<AudioPlayerState> validStartStates,
                AVSAudioPlayer audioPlayer, AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            state.set(AudioPlayerState.PLAYING);
            sendRequest(RequestFactory.createAudioPlayerProgressReportDelayElapsedEvent(
                    getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
        }
    }

    private static class IntervalProgressReport extends AudioPlayerStateTransition {

        public IntervalProgressReport(Set<AudioPlayerState> validStartStates,
                AVSAudioPlayer audioPlayer, AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            state.set(AudioPlayerState.PLAYING);
            sendRequest(RequestFactory.createAudioPlayerProgressReportIntervalElapsedEvent(
                    getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
        }
    }

    private static class PlaybackFailed extends AudioPlayerStateTransition {

        public PlaybackFailed(Set<AudioPlayerState> validStartStates, AVSAudioPlayer audioPlayer,
                AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            state.set(AudioPlayerState.STOPPED);
            sendRequest(RequestFactory.createAudioPlayerPlaybackFailedEvent(getCurrentStreamToken(),
                    getCurrentPlaybackState(), ErrorType.MEDIA_ERROR_UNKNOWN));
        }
    }

    private static class PlaybackNearlyFinished extends AudioPlayerStateTransition {

        public PlaybackNearlyFinished(Set<AudioPlayerState> validStartStates,
                AVSAudioPlayer audioPlayer, AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            sendRequest(RequestFactory.createAudioPlayerPlaybackNearlyFinishedEvent(
                    getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
        }
    }

    private static class PlaybackFinished extends AudioPlayerStateTransition {

        public PlaybackFinished(Set<AudioPlayerState> validStartStates, AVSAudioPlayer audioPlayer,
                AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            state.set(AudioPlayerState.FINISHED);
            sendRequest(RequestFactory.createAudioPlayerPlaybackFinishedEvent(
                    getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
        }
    }

    private static class ClearQueueEnqueued extends AudioPlayerStateTransition {

        public ClearQueueEnqueued(Set<AudioPlayerState> validStartStates,
                AVSAudioPlayer audioPlayer, AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            sendRequest(RequestFactory.createAudioPlayerPlaybackQueueClearedEvent());
        }
    }

    private static class ClearQueueAll extends AudioPlayerStateTransition {

        public ClearQueueAll(Set<AudioPlayerState> validStartStates, AVSAudioPlayer audioPlayer,
                AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            sendRequest(RequestFactory.createAudioPlayerPlaybackQueueClearedEvent());

            AudioPlayerState currentState = state.get();
            if (currentState == AudioPlayerState.PLAYING || currentState == AudioPlayerState.PAUSED
                    || currentState == AudioPlayerState.BUFFER_UNDERRUN) {
                state.set(AudioPlayerState.STOPPED);
                sendRequest(RequestFactory.createAudioPlayerPlaybackStoppedEvent(
                        getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
            }

        }
    }

    private static class PlayReplaceAll extends AudioPlayerStateTransition {

        public PlayReplaceAll(Set<AudioPlayerState> validStartStates, AVSAudioPlayer audioPlayer,
                              AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            AudioPlayerState currentState = state.get();
            if (currentState == AudioPlayerState.PLAYING || currentState == AudioPlayerState.PAUSED
                    || currentState == AudioPlayerState.BUFFER_UNDERRUN) {
                state.set(AudioPlayerState.STOPPED);
                sendRequest(RequestFactory.createAudioPlayerPlaybackStoppedEvent(
                        getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
            }
        }
    }

    private static class PlaybackStutterStarted extends AudioPlayerStateTransition {

        public PlaybackStutterStarted(Set<AudioPlayerState> validStartStates,
                AVSAudioPlayer audioPlayer, AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            state.set(AudioPlayerState.BUFFER_UNDERRUN);
            sendRequest(RequestFactory.createAudioPlayerPlaybackStutterStartedEvent(
                    getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
        }
    }

    private static class PlaybackStutterFinished extends AudioPlayerStateTransition {

        public PlaybackStutterFinished(Set<AudioPlayerState> validStartStates,
                AVSAudioPlayer audioPlayer, AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            state.set(AudioPlayerState.PLAYING);
            sendRequest(RequestFactory.createAudioPlayerPlaybackStutterFinishedEvent(
                    getCurrentStreamToken(), getCurrentOffsetInMilliseconds(),
                    getCurrentOffsetInMilliseconds() - getPlaybackStutterStartedTimestampMs()));
        }
    }

    private static class PlaybackPaused extends AudioPlayerStateTransition {

        public PlaybackPaused(Set<AudioPlayerState> validStartStates, AVSAudioPlayer audioPlayer,
                AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            state.set(AudioPlayerState.PAUSED);
            sendRequest(RequestFactory.createAudioPlayerPlaybackPausedEvent(getCurrentStreamToken(),
                    getCurrentOffsetInMilliseconds()));
        }
    }

    private static class PlaybackResumed extends AudioPlayerStateTransition {

        public PlaybackResumed(Set<AudioPlayerState> validStartStates, AVSAudioPlayer audioPlayer,
                AVSController controller) {
            super(validStartStates, audioPlayer, controller);
        }

        @Override
        protected void onTransition(State<AudioPlayerState> state) {
            state.set(AudioPlayerState.PLAYING);
            sendRequest(RequestFactory.createAudioPlayerPlaybackResumedEvent(
                    getCurrentStreamToken(), getCurrentOffsetInMilliseconds()));
        }
    }
}
