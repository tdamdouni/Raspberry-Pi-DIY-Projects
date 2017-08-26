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

import com.amazon.alexa.avs.message.response.templateruntime.RenderTemplate;

import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.SwingUtilities;
import javax.swing.border.LineBorder;

import com.amazon.alexa.avs.ui.CardUIHandler;

public class GraphicalCardView extends JPanel implements CardUIHandler {

    private static final int CARD_WIDTH = 400;
    private static final int CARD_HEIGHT = 300;
    private static final String CARD_PANEL_NAME = "cardpanel";

    private CardPanel cardPanel;

    GraphicalCardView() {
        super();
        this.cardPanel = new CardPanel();
        JScrollPane cardContainer = new JScrollPane(this.cardPanel);
        cardContainer.setBorder(new LineBorder(Color.BLACK));
        cardContainer.setPreferredSize(new Dimension(CARD_WIDTH, CARD_HEIGHT));
        this.add(cardContainer);
        this.cardPanel.setName(CARD_PANEL_NAME);
    }

    @Override
    public void onProcessing() {
    }

    @Override
    public void onListening() {
        SwingUtilities.invokeLater(() -> cardPanel.clearCard());
    }

    @Override
    public void onProcessingFinished() {
    }

    @Override
    public void renderCard(RenderTemplate payload, String rawMessage) {
        SwingUtilities.invokeLater(() -> cardPanel.generateCard(payload, rawMessage));
    }

    @Override
    public void renderPlayerInfo(String rawMessage) {
        SwingUtilities.invokeLater(() -> cardPanel.generatePlayerInfo(rawMessage));
    }

}
