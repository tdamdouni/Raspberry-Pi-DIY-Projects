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
package com.amazon.alexa.avs;

import com.amazon.alexa.avs.auth.AuthSetup;
import com.amazon.alexa.avs.config.DeviceConfig;
import com.amazon.alexa.avs.config.DeviceConfigUtils;
import com.amazon.alexa.avs.http.AVSClientFactory;
import com.amazon.alexa.avs.ui.graphical.GraphicalUI;
import com.amazon.alexa.avs.ui.headless.HeadlessUI;
import com.amazon.alexa.avs.wakeword.WakeWordIPCFactory;

public class App {

    private AVSController controller;

    public static void main(String[] args) throws Exception {
        if (args.length == 1) {
            new App(args[0]);
        } else {
            new App();
        }
    }

    public App() throws Exception {
        this(DeviceConfigUtils.readConfigFile());
    }

    public App(String configName) throws Exception {
        this(DeviceConfigUtils.readConfigFile(configName));
    }

    public App(DeviceConfig config) throws Exception {
        AuthSetup authSetup = new AuthSetup(config);
        controller =
                new AVSController(new AVSAudioPlayerFactory(), new AlertManagerFactory(),
                        getAVSClientFactory(config), DialogRequestIdAuthority.getInstance(),
                        new WakeWordIPCFactory(), config);
        if (config.getHeadlessModeEnabled()) {
            new HeadlessUI(controller, authSetup, config);
        } else {
            new GraphicalUI(controller, authSetup, config);
        }
    }

    protected AVSClientFactory getAVSClientFactory(DeviceConfig config) {
        return new AVSClientFactory(config);
    }

    protected AVSController getController() {
        return controller;
    }
}
