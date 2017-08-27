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
package com.amazon.alexa.avs.message.response;

public class ProgressReport {
    private long progressReportDelayInMilliseconds;
    private long progressReportIntervalInMilliseconds;

    public long getProgressReportDelayInMilliseconds() {
        return progressReportDelayInMilliseconds;
    }

    public long getProgressReportIntervalInMilliseconds() {
        return progressReportIntervalInMilliseconds;
    }

    public void setProgressReportDelayInMilliseconds(long progressReportDelayInMilliseconds) {
        this.progressReportDelayInMilliseconds = progressReportDelayInMilliseconds;
    }

    public void setProgressReportIntervalInMilliseconds(long progressReportIntervalInMilliseconds) {
        this.progressReportIntervalInMilliseconds = progressReportIntervalInMilliseconds;
    }

    public boolean isRequired() {
        return progressReportDelayInMilliseconds > 0 || progressReportIntervalInMilliseconds > 0;
    }
}
