/**
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.Rectangle;
import java.io.IOException;

import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.Scrollable;
import javax.swing.border.EmptyBorder;

import org.codehaus.jackson.JsonNode;
import org.codehaus.jackson.map.ObjectMapper;
import org.codehaus.jackson.map.SerializationConfig;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.amazon.alexa.avs.message.response.templateruntime.RenderTemplate;
import com.amazon.alexa.avs.message.response.templateruntime.Title;

public class CardPanel extends JPanel implements Scrollable {
    private static final Logger log = LoggerFactory.getLogger(CardPanel.class);
    private static final String BODY_TEMPLATE_1 = "bodyTemplate1";
    private Font defaultFont;

    private static final int SCROLLABLE_INCREMENT = 16;
    private static final float FONT_SCALE = 1.2f;
    private static final int BORDER_TOP = 10;
    private static final int BORDER_LEFT = 20;
    private static final int BORDER_BOTTOM = 10;
    private static final int BORDER_RIGHT = 20;
    private static final int TITLE_BOTTOM_PADDING = 15;

    /**
     * Generated Serial Version UID.
     */
    private static final long serialVersionUID = 2069388985473311409L;

    public CardPanel() {
        defaultFont = getFont();
        setBorder(new EmptyBorder(BORDER_TOP, BORDER_LEFT, BORDER_BOTTOM, BORDER_RIGHT));
        setBackground(Color.WHITE);
        setLayout(new BorderLayout());
    }

    public void generateCard(RenderTemplate payload, String rawMessage) {
        clearCard();
        if (payload.getType().equals(BODY_TEMPLATE_1)) {
            generateBodyTemplate1(payload.getTitle(), payload.getTextField());
        } else {
            createJsonTemplate(rawMessage);
        }

        revalidate();
        repaint();
    }

    public void generatePlayerInfo(String rawMessage) {
        clearCard();
        createJsonTemplate(rawMessage);
        revalidate();
        repaint();
    }

    public void clearCard() {
        removeAll();
    }

    private void generateBodyTemplate1(Title title, String content) {
        JPanel titlePanel = new JPanel(new GridLayout(0, 1));
        titlePanel.setBackground(Color.WHITE);
        titlePanel.setBorder(new EmptyBorder(0, 0, TITLE_BOTTOM_PADDING, 0));

        JTextArea mainTitle = new JTextArea(title.getMainTitle());
        mainTitle.setEditable(false);
        mainTitle.setFont(new Font(defaultFont.getFamily(), Font.BOLD, defaultFont.getSize()));
        JTextArea subTitle = new JTextArea(title.getSubTitle());
        subTitle.setForeground(Color.GRAY);
        subTitle.setEditable(false);

        titlePanel.add(mainTitle);
        titlePanel.add(subTitle);

        JTextArea textField = new JTextArea(content);
        textField.setLineWrap(true);
        textField.setWrapStyleWord(true);
        textField.setFont(new Font(defaultFont.getFamily(), Font.PLAIN,
                Math.round(defaultFont.getSize() * FONT_SCALE)));
        textField.setEditable(false);

        add(titlePanel, BorderLayout.PAGE_START);
        add(textField, BorderLayout.PAGE_END);
    }

    private void createJsonTemplate(String rawMessage) {

        String rawPayload;
        try {
            ObjectMapper mapper = new ObjectMapper();
            JsonNode message = mapper.readTree(rawMessage);
            JsonNode payload = message.get("payload");
            mapper.enable(SerializationConfig.Feature.INDENT_OUTPUT);
            rawPayload = mapper.writeValueAsString(payload);
        } catch (IOException e) {
            log.warn("Error parsing raw payload from JsonNode.");
            return;
        }

        JTextArea card = new JTextArea(rawPayload);
        card.setLineWrap(true);
        card.setWrapStyleWord(true);
        card.setEditable(false);
        add(card);
    }

    @Override
    public Dimension getPreferredScrollableViewportSize() {
        return super.getPreferredSize();
    }

    @Override
    public int getScrollableUnitIncrement(Rectangle visibleRect, int orientation, int direction) {
        return SCROLLABLE_INCREMENT;
    }

    @Override
    public int getScrollableBlockIncrement(Rectangle visibleRect, int orientation, int direction) {
        return SCROLLABLE_INCREMENT;
    }

    @Override
    public boolean getScrollableTracksViewportWidth() {
        return true;
    }

    @Override
    public boolean getScrollableTracksViewportHeight() {
        return false;
    }
}
