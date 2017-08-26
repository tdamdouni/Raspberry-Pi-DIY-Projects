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

import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonReader;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.handler.AbstractHandler;

import com.amazon.alexa.avs.auth.AuthConstants;
import com.amazon.alexa.avs.auth.MissingParameterException;
import com.amazon.alexa.avs.auth.companionapp.CompanionAppAuthManager;
import com.amazon.alexa.avs.auth.companionapp.CompanionAppAuthManager.InvalidSessionIdException;
import com.amazon.alexa.avs.auth.companionapp.CompanionAppProvisioningInfo;
import com.amazon.alexa.avs.auth.companionapp.LWAException;

/**
 * A Jetty Handler for receiving {@link CompanionAppProvisioningInfo} from companion applications.
 */
public class CompanionInfoHandler extends AbstractHandler {
    private final CompanionAppAuthManager authManager;

    /**
     * Creates a {@link CompanionInfoHandler} object.
     * @param authManager
     */
    public CompanionInfoHandler(CompanionAppAuthManager authManager) {
        this.authManager = authManager;
    }

    /**
     * Writes an error message to the response.
     *
     * @param response The response object to write to.
     * @param error The error type to write.
     * @param message The error message to write.
     * @param statusCode The HTTP status code to use.
     * @throws IOException If an I/O exception occurs.
     */
    public void errorMessage(HttpServletResponse response, String error, String message, int statusCode)
            throws IOException {
        JsonObject object =
                Json.createObjectBuilder().add(AuthConstants.ERROR, error).add(AuthConstants.MESSAGE, message).build();

        response.setStatus(statusCode);
        response.getWriter().println(object.toString());
    }

    /**
     * Handle receiving the necessary information from the companion application to finish provisioning.
     *
     * {@inheritDoc}
     */
    @Override
    public void handle(String target, Request baseRequest, HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // Only handle this as a POST request.
        if (!request.getMethod().equals("POST")) {
            baseRequest.setHandled(false);
            return;
        }

        // Setup the response. We'll always return JSON.
        baseRequest.setHandled(true);
        response.setContentType("application/json");

        // Read in the JSON and parse it.
        JsonReader reader = Json.createReader(request.getInputStream());
        JsonObject jsonRequest = reader.readObject();

        String sessionId = jsonRequest.getString(AuthConstants.SESSION_ID, null);
        String clientId = jsonRequest.getString(AuthConstants.CLIENT_ID, null);
        String redirectUri = jsonRequest.getString(AuthConstants.REDIRECT_URI, null);
        String authCode = jsonRequest.getString(AuthConstants.AUTH_CODE, null);

        try {
            CompanionAppProvisioningInfo companionProvisioningInfo =
                    new CompanionAppProvisioningInfo(sessionId, clientId, redirectUri, authCode);
            authManager.exchangeCompanionInfoForTokens(companionProvisioningInfo);

            response.setStatus(HttpServletResponse.SC_NO_CONTENT);
        } catch (MissingParameterException e) {
            errorMessage(response, AuthConstants.INVALID_PARAM_ERROR, e.getMessage(), HttpServletResponse.SC_BAD_REQUEST);
            return;
        } catch (InvalidSessionIdException e) {
            errorMessage(response, AuthConstants.INCORRECT_SESSION_ID_ERROR, e.getMessage(),
                    HttpServletResponse.SC_BAD_REQUEST);
            return;
        } catch (LWAException e) {
            errorMessage(response, AuthConstants.LWA_ERROR, e.getMessage(), e.getResponseCode());
            return;
        }

        return;
    }
}
