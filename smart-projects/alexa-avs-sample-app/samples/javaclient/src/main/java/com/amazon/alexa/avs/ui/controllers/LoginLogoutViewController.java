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
package com.amazon.alexa.avs.ui.controllers;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.auth.AuthSetup;
import com.amazon.alexa.avs.auth.companionservice.RegCodeDisplayHandler;
import com.amazon.alexa.avs.ui.LoginLogoutUIHandler;

public class LoginLogoutViewController implements LoginLogoutUIHandler {
    public static final String LOGIN_LABEL = "Login";
    public static final String LOGOUT_LABEL = "Logout";

    private final AVSController controller;
    private final AuthSetup authSetup;
    private final RegCodeDisplayHandler regCodeDisplayHandler;

    public LoginLogoutViewController(
            final AVSController controller,
            final AuthSetup authSetup,
            final RegCodeDisplayHandler regCodeDisplayHandler) {
        this.controller = controller;
        this.authSetup = authSetup;
        this.regCodeDisplayHandler = regCodeDisplayHandler;
    }

    @Override
    public void startLogin() {
        controller.onUserActivity();
        authSetup.startProvisioningThread(regCodeDisplayHandler);
    }

    @Override
    public void startLogout() {
        controller.onUserActivity();
        authSetup.startLogoutThread(regCodeDisplayHandler);
    }

    @Override
    public void onAccessTokenReceived(String accessToken) {
    }

    @Override
    public void onAccessTokenRevoked() {
    }
}