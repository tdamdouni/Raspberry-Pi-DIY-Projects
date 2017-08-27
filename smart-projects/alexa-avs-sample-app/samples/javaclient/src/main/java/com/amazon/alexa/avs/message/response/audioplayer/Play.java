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
package com.amazon.alexa.avs.message.response.audioplayer;

import com.amazon.alexa.avs.message.Payload;
import com.amazon.alexa.avs.message.response.AttachedContentPayload;

import org.codehaus.jackson.annotate.JsonIgnore;

import java.io.InputStream;

public final class Play extends Payload implements AttachedContentPayload {

    public enum PlayBehavior {
        REPLACE_ALL,
        ENQUEUE,
        REPLACE_ENQUEUED;
    }

    private PlayBehavior playBehavior;
    private AudioItem audioItem;

    public PlayBehavior getPlayBehavior() {
        return playBehavior;
    }

    public AudioItem getAudioItem() {
        return audioItem;
    }

    public void setPlayBehavior(String playBehavior) {
        this.playBehavior = PlayBehavior.valueOf(playBehavior);
    }

    public void setAudioItem(AudioItem audioItem) {
        this.audioItem = audioItem;
    }

    @Override
    public boolean requiresAttachedContent() {
        return audioItem.getStream().requiresAttachedContent();
    }

    @Override
    public boolean hasAttachedContent() {
        return audioItem.getStream().hasAttachedContent();
    }

    @Override
    public String getAttachedContentId() {
        if (requiresAttachedContent()) {
            return audioItem.getStream().getUrl();
        } else {
            return null;
        }
    }

    @JsonIgnore
    @Override
    public InputStream getAttachedContent() {
        return audioItem.getStream().getAttachedContent();
    }

    @Override
    public void setAttachedContent(String cid, InputStream content) {
        if (getAttachedContentId().equals(cid)) {
            audioItem.getStream().setAttachedContent(content);
        } else {
            throw new IllegalArgumentException(
                    "Tried to add the wrong audio content to a Play directive. This cid: "
                            + getAttachedContentId() + " other cid: " + cid);
        }
    }
}
