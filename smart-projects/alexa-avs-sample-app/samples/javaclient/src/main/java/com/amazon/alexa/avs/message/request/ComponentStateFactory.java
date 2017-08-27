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
package com.amazon.alexa.avs.message.request;

import com.amazon.alexa.avs.AVSAPIConstants;
import com.amazon.alexa.avs.message.Header;
import com.amazon.alexa.avs.message.Payload;
import com.amazon.alexa.avs.message.request.context.AlertsStatePayload;
import com.amazon.alexa.avs.message.request.context.ComponentState;
import com.amazon.alexa.avs.message.request.context.NotificationsStatePayload;
import com.amazon.alexa.avs.message.request.context.PlaybackStatePayload;
import com.amazon.alexa.avs.message.request.context.SpeechStatePayload;
import com.amazon.alexa.avs.message.request.context.VolumeStatePayload;

public class ComponentStateFactory {

    public static ComponentState createPlaybackState(PlaybackStatePayload playerState) {
        return new ComponentState(new Header(AVSAPIConstants.AudioPlayer.NAMESPACE,
                AVSAPIConstants.AudioPlayer.Events.PlaybackState.NAME), playerState);
    }

    public static ComponentState createSpeechState(SpeechStatePayload speechState) {
        return new ComponentState(new Header(AVSAPIConstants.SpeechSynthesizer.NAMESPACE,
                AVSAPIConstants.SpeechSynthesizer.Events.SpeechState.NAME), speechState);
    }

    public static ComponentState createAlertState(AlertsStatePayload alertState) {
        return new ComponentState(new Header(AVSAPIConstants.Alerts.NAMESPACE,
                AVSAPIConstants.Alerts.Events.AlertsState.NAME), alertState);
    }

    public static ComponentState createVolumeState(VolumeStatePayload volumeState) {
        return new ComponentState(new Header(AVSAPIConstants.Speaker.NAMESPACE,
                AVSAPIConstants.Speaker.Events.VolumeState.NAME), volumeState);
    }

    public static ComponentState createNotificationsState(
            NotificationsStatePayload notificationsState) {
        return new ComponentState(
                new Header(AVSAPIConstants.Notifications.NAMESPACE,
                        AVSAPIConstants.Notifications.Events.IndicatorState.NAME),
                notificationsState);
    }

    public static ComponentState createComponentState(Payload payload) {
        ComponentState component;
        if (payload instanceof PlaybackStatePayload) {
            component = ComponentStateFactory.createPlaybackState((PlaybackStatePayload) payload);
        } else if (payload instanceof SpeechStatePayload) {
            component = ComponentStateFactory.createSpeechState((SpeechStatePayload) payload);
        } else if (payload instanceof AlertsStatePayload) {
            component = ComponentStateFactory.createAlertState((AlertsStatePayload) payload);
        } else if (payload instanceof VolumeStatePayload) {
            component = ComponentStateFactory.createVolumeState((VolumeStatePayload) payload);
        } else if (payload instanceof NotificationsStatePayload) {
            component = ComponentStateFactory
                    .createNotificationsState((NotificationsStatePayload) payload);
        } else {
            throw new IllegalArgumentException("Unknown payload type");
        }
        return component;
    }
}
