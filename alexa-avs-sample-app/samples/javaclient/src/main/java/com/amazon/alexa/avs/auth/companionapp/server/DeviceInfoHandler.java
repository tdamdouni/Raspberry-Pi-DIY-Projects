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
package com.amazon.alexa.avs.auth.companionapp.server;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.handler.AbstractHandler;

import com.amazon.alexa.avs.auth.companionapp.CompanionAppAuthManager;
import com.amazon.alexa.avs.auth.companionapp.DeviceProvisioningInfo;

/**
 * A Jetty Handler for sending {@link DeviceProvisioningInfo} to companion applications.
 */
public class DeviceInfoHandler extends AbstractHandler {
    private final CompanionAppAuthManager authManager;

    /**
     * Creates a {@link DeviceInfoHandler} object.
     * @param authManager
     */
    public DeviceInfoHandler(CompanionAppAuthManager authManager) {
        this.authManager = authManager;
    }

    /**
     * Handle sending the necessary device information to the companion application to start provisioning.
     *
     * {@inheritDoc}
     */
    @Override
    public void handle(String target, Request baseRequest, HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {
        // Only handle this as a GET request.
        if (!request.getMethod().equals("GET")) {
            baseRequest.setHandled(false);
            return;
        }

        // Setup the response. We'll always return JSON.
        baseRequest.setHandled(true);
        response.setContentType("application/json");

        DeviceProvisioningInfo deviceProvisioningInfo = authManager.getDeviceProvisioningInfo();

        response.setStatus(HttpServletResponse.SC_OK);
        response.getWriter().print(deviceProvisioningInfo.toJson().toString());
        return;
    }
}
