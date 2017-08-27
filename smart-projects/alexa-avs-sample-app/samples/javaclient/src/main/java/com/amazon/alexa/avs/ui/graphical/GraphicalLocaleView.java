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
package com.amazon.alexa.avs.ui.graphical;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.config.DeviceConfig;

import java.awt.FlowLayout;
import java.util.Locale;

import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;

import com.amazon.alexa.avs.ui.LocaleUIHandler;
import com.amazon.alexa.avs.ui.controllers.LocaleViewController;

public class GraphicalLocaleView extends JPanel implements LocaleUIHandler {

    private static final String LOCALE_LABEL = "Locale:";
    private static final String LOCALE_NAME = "Locale";

    private LocaleViewController localeViewController;

    GraphicalLocaleView(DeviceConfig config, AVSController controller) {
        super(new FlowLayout(FlowLayout.LEFT, 0, 0));
        localeViewController = new LocaleViewController(config, controller);
        JLabel localeLabel = new JLabel(LOCALE_LABEL);
        this.add(localeLabel);
        localeLabel.setName(LOCALE_NAME);
        JComboBox<Object> localeSelector =
                new JComboBox<>(config.getSupportedLocalesLanguageTag().toArray());
        localeSelector.setSelectedItem(config.getLocale().toLanguageTag());
        localeSelector.addActionListener(e -> {
            Locale locale = Locale.forLanguageTag(localeSelector.getSelectedItem().toString());
            handleLocaleChange(locale);
        });
        this.add(localeSelector);
    }

    @Override
    public void handleLocaleChange(Locale locale) {
        localeViewController.handleLocaleChange(locale);
    }
}
