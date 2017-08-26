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
import com.amazon.alexa.avs.auth.AuthSetup;
import com.amazon.alexa.avs.config.DeviceConfig;
import com.amazon.alexa.avs.config.DeviceConfig.ProvisioningMethod;
import com.amazon.alexa.avs.ui.LoginLogoutUIHandler;
import com.amazon.alexa.avs.ui.controllers.LoginLogoutViewController;

import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

public class GraphicalLoginLogoutView extends JPanel implements LoginLogoutUIHandler {

    private JButton loginButton;
    private JButton logoutButton;

    private final AVSController controller;
    private final AuthSetup authSetup;
    private final GraphicalUI graphicalUI;

    private LoginLogoutViewController loginLogoutController;

    public GraphicalLoginLogoutView(DeviceConfig config, AVSController controller,
            AuthSetup authSetup, GraphicalUI graphicalUI) {
        super(new FlowLayout(FlowLayout.LEFT, 0, 0));

        this.controller = controller;
        this.authSetup = authSetup;
        this.graphicalUI = graphicalUI;

        if (config.getProvisioningMethod() == ProvisioningMethod.COMPANION_SERVICE) {
            loginButton = new JButton(LoginLogoutViewController.LOGIN_LABEL);
            loginButton.setEnabled(true);
            loginButton.addActionListener(e -> startLogin());
            this.add(loginButton);

            logoutButton = new JButton(LoginLogoutViewController.LOGOUT_LABEL);
            logoutButton.setEnabled(false);
            logoutButton.addActionListener(e -> startLogout());
            this.add(logoutButton);
        }
    }

    private void createLoginLogoutControllerIfMissing() {
        if (loginLogoutController == null) {
            this.loginLogoutController = new LoginLogoutViewController(controller, authSetup,
                    graphicalUI.getRegCodeDisplayHandler());
        }
    }

    @Override
    public void startLogin() {
        createLoginLogoutControllerIfMissing();
        loginLogoutController.startLogin();
    }

    @Override
    public void startLogout() {
        createLoginLogoutControllerIfMissing();
        loginLogoutController.startLogout();
    }

    private void afterLogin() {
        if (loginButton != null) {
            loginButton.setEnabled(false);
        }
        if (logoutButton != null) {
            logoutButton.setEnabled(true);
        }
    }

    private void afterLogout() {
        if (loginButton != null) {
            loginButton.setEnabled(true);
        }
        if (logoutButton != null) {
            logoutButton.setEnabled(false);
        }
    }

    @Override
    public synchronized void onAccessTokenReceived(String accessToken) {
        SwingUtilities.invokeLater(() -> afterLogin());
    }

    @Override
    public synchronized void onAccessTokenRevoked() {
        SwingUtilities.invokeLater(() -> afterLogout());
    }
}