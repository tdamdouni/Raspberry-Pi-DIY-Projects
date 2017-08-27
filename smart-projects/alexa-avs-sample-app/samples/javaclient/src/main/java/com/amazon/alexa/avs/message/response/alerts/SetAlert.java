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
package com.amazon.alexa.avs.message.response.alerts;

import com.amazon.alexa.avs.DateUtils;
import com.amazon.alexa.avs.message.Payload;

import org.codehaus.jackson.annotate.JsonProperty;

import java.time.ZonedDateTime;

public final class SetAlert extends Payload {

    public enum AlertType {
        ALARM,
        TIMER;
    }

    // Opaque identifier of the alert
    private String token;

    private AlertType type;

    // Time when the alarm or timer is scheduled
    private ZonedDateTime scheduledTime;

    public void setToken(String token) {
        this.token = token;
    }

    public String getToken() {
        return token;
    }

    public void setType(String type) {
        this.type = AlertType.valueOf(type.toUpperCase());
    }

    public AlertType getType() {
        return type;
    }

    @JsonProperty("scheduledTime")
    public void setScheduledTime(String dateTime) {
        scheduledTime = ZonedDateTime.parse(dateTime, DateUtils.AVS_ISO_OFFSET_DATE_TIME);
    }

    public void setScheduledTime(ZonedDateTime dateTime) {
        scheduledTime = dateTime;
    }

    public ZonedDateTime getScheduledTime() {
        return scheduledTime;
    }
}
