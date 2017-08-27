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
package com.amazon.alexa.avs.ui.headless;

import com.amazon.alexa.avs.AVSController;
import com.amazon.alexa.avs.auth.AuthSetup;
import com.amazon.alexa.avs.auth.companionservice.RegCodeDisplayHandler;
import com.amazon.alexa.avs.config.DeviceConfig;
import com.amazon.alexa.avs.config.DeviceConfig.ProvisioningMethod;
import com.amazon.alexa.avs.ui.LoginLogoutUIHandler;
import com.amazon.alexa.avs.ui.controllers.LoginLogoutViewController;

public class HeadlessLoginLogoutView implements LoginLogoutUIHandler {

    private final LoginLogoutViewController loginLogoutController;
    private final DeviceConfig config;

    public HeadlessLoginLogoutView(DeviceConfig config, AVSController controller,
            AuthSetup authSetup, RegCodeDisplayHandler regCodeDisplayHandler) {
        this.config = config;
        this.loginLogoutController = new LoginLogoutViewController(controller, authSetup,
                regCodeDisplayHandler);
    }

    @Override
    public synchronized void onAccessTokenReceived(String accessToken) {
        System.out.println("Logged in.");
    }

    @Override
    public synchronized void onAccessTokenRevoked() {
        System.out.println("Logged out.");
    }

    @Override
    public void startLogin() {
        if (config.getProvisioningMethod() == ProvisioningMethod.COMPANION_SERVICE) {
            loginLogoutController.startLogin();
        } else {
            System.out.println("Can only login using the companion service.");
        }
    }

    @Override
    public void startLogout() {
        if (config.getProvisioningMethod() == ProvisioningMethod.COMPANION_SERVICE) {
            loginLogoutController.startLogout();
        } else {
            System.out.println("Can only logout of the companion service.");
        }
    }
}