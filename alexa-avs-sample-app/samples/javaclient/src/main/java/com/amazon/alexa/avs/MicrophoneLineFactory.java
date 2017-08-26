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

import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Line;
import javax.sound.sampled.Mixer;
import javax.sound.sampled.TargetDataLine;

public class MicrophoneLineFactory {
    // get the system default microphone
    public TargetDataLine getMicrophone() {
        Mixer.Info[] mixers = AudioSystem.getMixerInfo();
        for (Mixer.Info mixerInfo : mixers) {
            Mixer m = AudioSystem.getMixer(mixerInfo);
            try {
                m.open();
                m.close();
            } catch (Exception e) {
                continue;
            }

            Line.Info[] lines = m.getTargetLineInfo();
            for (Line.Info li : lines) {
                try {
                    TargetDataLine temp = (TargetDataLine) AudioSystem.getLine(li);
                    if (temp != null) {
                        return temp;
                    }
                } catch (Exception e) {
                }
            }
        }
        return null;
    }
}
