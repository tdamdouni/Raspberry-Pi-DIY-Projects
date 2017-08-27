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

import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

/**
 * A timer used to trigger AVS alerts on schedule
 */
public class AlertScheduler extends Timer {
    private final Alert alert;
    private final AlertHandler handler;
    private boolean active = false;

    public AlertScheduler(final Alert alert, final AlertHandler handler) {
        super();
        schedule(new TimerTask() {
            @Override
            public void run() {
                setActive(true);
                handler.startAlert(alert.getToken());
            }
        }, Date.from(alert.getScheduledTime().toInstant()));
        this.alert = alert;
        this.handler = handler;
    }

    public synchronized boolean isActive() {
        return active;
    }

    public synchronized void setActive(boolean active) {
        this.active = active;
    }

    @Override
    public void cancel() {
        super.cancel();
        if (isActive()) {
            handler.stopAlert(alert.getToken());
            setActive(false);
        }
    }

    public Alert getAlert() {
        return alert;
    }
}
