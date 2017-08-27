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
package com.amazon.alexa.avs.ui;

import java.util.Locale;

/**
 * Controls behavior for changing Locale dynamically.
 */
public interface LocaleUIHandler {

    /**
     * When the locale is updated, call this method with the new locale.
     *
     * @param locale
     *         Updated locale.
     */
    void handleLocaleChange(Locale locale);
}
