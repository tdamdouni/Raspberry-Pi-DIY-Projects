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
package com.amazon.alexa.avs.auth.companionservice;

import com.amazon.alexa.avs.auth.AccessTokenListener;
import com.amazon.alexa.avs.auth.OAuth2AccessToken;
import com.amazon.alexa.avs.auth.companionservice.CompanionServiceClient.RemoteServiceException;
import com.amazon.alexa.avs.config.DeviceConfig;
import com.amazon.alexa.avs.config.DeviceConfig.CompanionServiceInformation;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class CompanionServiceAuthManager {
    /**
     * How long in seconds before trying again to exchange refreshToken for an accessToken.
     */
    private static final int COMPANION_SERVICE_RETRY_INTERVAL_IN_SECONDS = 2;
    private static final Logger log = LoggerFactory.getLogger(CompanionServiceAuthManager.class);
    private final DeviceConfig deviceConfig;
    private final CompanionServiceClient companionServiceClient;
    private final RegCodeDisplayHandler regCodeDisplayHandler;
    private final AccessTokenListener accessTokenListener;
    private final Timer refreshTimer;
    private OAuth2AccessToken token;

    public CompanionServiceAuthManager(DeviceConfig deviceConfig,
            CompanionServiceClient remoteProvisioningClient,
            RegCodeDisplayHandler regCodeDisplayHandler, AccessTokenListener accessTokenListener) {
        this.deviceConfig = deviceConfig;
        this.companionServiceClient = remoteProvisioningClient;
        this.regCodeDisplayHandler = regCodeDisplayHandler;
        this.accessTokenListener = accessTokenListener;
        this.refreshTimer = new Timer();
    }

    public void startRemoteProvisioning() {
        if (deviceConfig.getCompanionServiceInfo() != null
                && deviceConfig.getCompanionServiceInfo().getSessionId() != null) {
            try {
                refreshTokens();
            } catch (RemoteServiceException e) {
                startNewProvisioningRequest();
            }
        } else {
            startNewProvisioningRequest();
        }
    }

    private void startNewProvisioningRequest() {
        CompanionServiceRegCodeResponse response = requestRegistrationCode();
        requestAccessToken(response.getSessionId());
    }

    public CompanionServiceRegCodeResponse requestRegistrationCode() {
        while (true) {
            try {
                CompanionServiceRegCodeResponse regCodeResponse =
                        companionServiceClient.getRegistrationCode();

                String regCode = regCodeResponse.getRegCode();

                regCodeDisplayHandler.displayRegCode(regCode);
                return regCodeResponse;
            } catch (IOException e) {
                try {
                    log.error("There was a problem connecting to the Companion Service. Trying again in "
                                    + COMPANION_SERVICE_RETRY_INTERVAL_IN_SECONDS
                                    + " seconds. Please make sure it is up and running.");
                    Thread.sleep(COMPANION_SERVICE_RETRY_INTERVAL_IN_SECONDS * 1000);
                } catch (InterruptedException ie) {
                }
            }
        }
    }

    public void requestAccessToken(String sessionId) {
        if (deviceConfig.getCompanionServiceInfo() != null) {
            while (true) {
                try {
                    token = companionServiceClient.getAccessToken(sessionId);

                    CompanionServiceInformation info = deviceConfig.getCompanionServiceInfo();
                    info.setSessionId(sessionId);
                    deviceConfig.saveConfig();

                    refreshTimer.schedule(new RefreshTokenTimerTask(),
                            new Date(token.getExpiresTime()));

                    accessTokenListener.onAccessTokenReceived(token.getAccessToken());
                    break;
                } catch (IOException e) {
                    try {
                        log.error("There was a problem connecting to the Companion Service. Trying again in "
                                        + COMPANION_SERVICE_RETRY_INTERVAL_IN_SECONDS
                                        + " seconds. Please make sure it is up and running.");
                        Thread.sleep(COMPANION_SERVICE_RETRY_INTERVAL_IN_SECONDS * 1000);
                    } catch (InterruptedException ie) {
                    }
                }
            }
        }
    }

    private void refreshTokens() {
        if (deviceConfig.getCompanionServiceInfo() != null) {
            requestAccessToken(deviceConfig.getCompanionServiceInfo().getSessionId());
        }
    }

    public void revokeToken() {
        if ((deviceConfig.getCompanionServiceInfo() != null) && (deviceConfig.getCompanionServiceInfo().getSessionId() != null)) {
            while (true) {
                try {
                    if (companionServiceClient.revokeAccessToken(deviceConfig.getCompanionServiceInfo().getSessionId())) {
                        accessTokenListener.onAccessTokenRevoked();
                    } else {
                        log.error("There was a problem deleting the tokens in the Companion Service.");
                    }
                    break;
                } catch (IOException e) {
                    try {
                        log.error("There was a problem connecting to the Companion Service. Trying again in "
                                        + COMPANION_SERVICE_RETRY_INTERVAL_IN_SECONDS
                                        + " seconds. Please make sure it is up and running.");
                        Thread.sleep(COMPANION_SERVICE_RETRY_INTERVAL_IN_SECONDS * 1000);
                    } catch (InterruptedException ie) {
                    }
                }
            }
        }
    }

    /**
     * TimerTask for refreshing accessTokens every hour.
     */
    private class RefreshTokenTimerTask extends TimerTask {
        @Override
        public void run() {
            refreshTokens();
        }
    }
}
