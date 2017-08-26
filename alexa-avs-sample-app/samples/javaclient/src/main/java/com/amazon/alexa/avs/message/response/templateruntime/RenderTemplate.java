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
package com.amazon.alexa.avs.message.response.templateruntime;

import com.amazon.alexa.avs.message.Payload;

public class RenderTemplate extends Payload {
    private String type;
    private Title title;
    private String textField;

    public final void setType(String type) {
        this.type = type;
    }

    public final void setTitle(Title title) {
        this.title = title;
    }

    public final void setTextField(String textField) {
        this.textField = textField;
    }

    public final Title getTitle() {
        return title;
    }

    public final String getType() {
        return type;
    }

    public final String getTextField() {
        return textField;
    }
}
