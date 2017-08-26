/**
 * Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */
package com.amazon.alexa.avs.companion;

import android.app.Dialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v4.app.DialogFragment;
import android.support.v4.app.FragmentManager;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.amazon.identity.auth.device.AuthError;
import com.amazon.identity.auth.device.api.authorization.AuthCancellation;
import com.amazon.identity.auth.device.api.authorization.AuthorizationManager;
import com.amazon.identity.auth.device.api.authorization.AuthorizeListener;
import com.amazon.identity.auth.device.api.authorization.AuthorizeRequest;
import com.amazon.identity.auth.device.api.authorization.AuthorizeResult;
import com.amazon.identity.auth.device.api.authorization.ScopeFactory;
import com.amazon.identity.auth.device.api.workflow.RequestContext;

import org.json.JSONException;
import org.json.JSONObject;

public class LoginWithAmazonActivity extends AppCompatActivity {

    private static final String TAG = LoginWithAmazonActivity.class.getName();
    private static final String ALEXA_ALL_SCOPE = "alexa:all";
    private static final String DEVICE_SERIAL_NUMBER = "deviceSerialNumber";
    private static final String PRODUCT_INSTANCE_ATTRIBUTES = "productInstanceAttributes";
    private static final String PRODUCT_ID = "productID";

    private static final String BUNDLE_KEY_EXCEPTION = "exception";

    private static final int MIN_CONNECT_PROGRESS_TIME_MS = 1*1000;

    private ProvisioningClient mProvisioningClient;
    private DeviceProvisioningInfo mDeviceProvisioningInfo;
    private RequestContext mRequestContext;

    private EditText mAddressTextView;
    private Button mConnectButton;
    private ProgressBar mConnectProgress;
    private ProgressBar mLoginProgress;
    private ImageButton mLoginButton;
    private TextView mLoginMessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mRequestContext = RequestContext.create(this);
        mRequestContext.registerListener(new AuthorizeListenerImpl());

        setContentView(R.layout.lwa_activity);

        mAddressTextView = (EditText) findViewById(R.id.addressTextView);

        mConnectButton = (Button) findViewById(R.id.connectButton);
        mConnectProgress = (ProgressBar) findViewById(R.id.connectProgressBar);

        mLoginButton = (ImageButton) findViewById(R.id.loginButton);
        mLoginProgress = (ProgressBar) findViewById(R.id.loginProgressBar);
        mLoginMessage = (TextView) findViewById(R.id.loginMessage);

        connectCleanState();

        try {
            mProvisioningClient = new ProvisioningClient(this);
        } catch(Exception e) {
            connectErrorState();
            showAlertDialog(e);
            Log.e(TAG, "Unable to use Provisioning Client. CA Certificate is incorrect or does not exist.", e);
        }

        String savedDeviceAddress = getPreferences(Context.MODE_PRIVATE).getString(getString(R.string.saved_device_address), null);
        if (savedDeviceAddress != null) {
            mAddressTextView.setText(savedDeviceAddress);
        }

        mConnectButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View view) {
                final String address = mAddressTextView.getText().toString();
                mProvisioningClient.setEndpoint(address);

                new AsyncTask<Void, Void, DeviceProvisioningInfo>() {
                    private Exception errorInBackground;

                    @Override
                    protected void onPreExecute() {
                        super.onPreExecute();
                        connectInProgressState();
                    }

                    @Override
                    protected DeviceProvisioningInfo doInBackground(Void... voids) {
                        try {
                            long startTime = System.currentTimeMillis();
                            DeviceProvisioningInfo response = mProvisioningClient.getDeviceProvisioningInfo();
                            long duration = System.currentTimeMillis() - startTime;

                            if (duration < MIN_CONNECT_PROGRESS_TIME_MS) {
                                try {
                                    Thread.sleep(MIN_CONNECT_PROGRESS_TIME_MS - duration);
                                } catch (InterruptedException e) {
                                    e.printStackTrace();
                                }
                            }

                            return response;
                        } catch (Exception e) {
                            errorInBackground = e;
                        }
                        return null;
                    }

                    @Override
                    protected void onPostExecute(DeviceProvisioningInfo deviceProvisioningInfo) {
                        super.onPostExecute(deviceProvisioningInfo);
                        if (deviceProvisioningInfo != null) {
                            mDeviceProvisioningInfo = deviceProvisioningInfo;

                            SharedPreferences.Editor editor = getPreferences(Context.MODE_PRIVATE).edit();
                            editor.putString(getString(R.string.saved_device_address), address);
                            editor.commit();

                            connectSuccessState();
                        } else {
                            connectCleanState();
                            showAlertDialog(errorInBackground);
                        }
                    }
                }.execute();
            }
        });

        mLoginButton.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                loginInProgressState();

                final JSONObject scopeData = new JSONObject();
                final JSONObject productInstanceAttributes = new JSONObject();
                final String codeChallenge = mDeviceProvisioningInfo.getCodeChallenge();
                final String codeChallengeMethod = mDeviceProvisioningInfo.getCodeChallengeMethod();

                try {
                    productInstanceAttributes.put(DEVICE_SERIAL_NUMBER, mDeviceProvisioningInfo.getDsn());
                    scopeData.put(PRODUCT_INSTANCE_ATTRIBUTES, productInstanceAttributes);
                    scopeData.put(PRODUCT_ID, mDeviceProvisioningInfo.getProductId());

                    AuthorizationManager.authorize(new AuthorizeRequest.Builder(mRequestContext)
                            .addScope(ScopeFactory.scopeNamed(ALEXA_ALL_SCOPE, scopeData))
                            .forGrantType(AuthorizeRequest.GrantType.AUTHORIZATION_CODE)
                            .withProofKeyParameters(codeChallenge, codeChallengeMethod)
                            .build());
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        });
    }

    @Override
    protected void onResume() {
        super.onResume();
        mRequestContext.onResume();
    }

    private void connectCleanState() {
        mConnectButton.setVisibility(View.VISIBLE);
        mConnectProgress.setVisibility(View.GONE);

        mLoginButton.setVisibility(View.GONE);
        mLoginProgress.setVisibility(View.GONE);
        mLoginMessage.setVisibility(View.GONE);
    }

    private void connectInProgressState() {
        mConnectButton.setVisibility(View.GONE);
        mConnectProgress.setVisibility(View.VISIBLE);
        mConnectProgress.setIndeterminate(true);

        mLoginButton.setVisibility(View.GONE);
        mLoginProgress.setVisibility(View.GONE);
        mLoginMessage.setVisibility(View.GONE);
    }

    private void connectSuccessState() {
        mConnectButton.setVisibility(View.VISIBLE);
        mConnectProgress.setVisibility(View.GONE);

        mLoginButton.setVisibility(View.VISIBLE);
        mLoginProgress.setVisibility(View.GONE);
        mLoginMessage.setVisibility(View.GONE);
    }

    private void connectErrorState() {
        mConnectButton.setVisibility(View.GONE);
        mConnectProgress.setVisibility(View.GONE);

        mLoginButton.setVisibility(View.GONE);
        mLoginProgress.setVisibility(View.GONE);
        mLoginMessage.setVisibility(View.GONE);
    }

    private void loginInProgressState() {
        mConnectButton.setVisibility(View.VISIBLE);
        mConnectProgress.setVisibility(View.GONE);

        mLoginButton.setVisibility(View.GONE);
        mLoginProgress.setVisibility(View.VISIBLE);
        mLoginMessage.setVisibility(View.GONE);
    }

    private void loginSuccessState() {
        mConnectButton.setVisibility(View.VISIBLE);
        mConnectProgress.setVisibility(View.GONE);

        mLoginButton.setVisibility(View.GONE);
        mLoginProgress.setVisibility(View.GONE);
        mLoginMessage.setVisibility(View.VISIBLE);
        mLoginMessage.setText(R.string.success_message);
    }

    protected void showAlertDialog(Exception exception) {
        exception.printStackTrace();
        ErrorDialogFragment dialogFragment = new ErrorDialogFragment();
        Bundle args = new Bundle();
        args.putSerializable(BUNDLE_KEY_EXCEPTION, exception);
        dialogFragment.setArguments(args);
        FragmentManager fm = getSupportFragmentManager();
        dialogFragment.show(fm, "error_dialog");
    }

    private class AuthorizeListenerImpl extends AuthorizeListener {
        @Override
        public void onSuccess(final AuthorizeResult authorizeResult) {
            final String authorizationCode = authorizeResult.getAuthorizationCode();
            final String redirectUri = authorizeResult.getRedirectURI();
            final String clientId = authorizeResult.getClientId();
            final String sessionId = mDeviceProvisioningInfo.getSessionId();

            final CompanionProvisioningInfo companionProvisioningInfo = new CompanionProvisioningInfo(sessionId, clientId, redirectUri, authorizationCode);

            new AsyncTask<Void, Void, Void>() {
                private Exception errorInBackground;

                @Override
                protected void onPreExecute() {
                    super.onPreExecute();
                    loginInProgressState();
                }

                @Override
                protected Void doInBackground(Void... voids) {
                    try {
                        mProvisioningClient.postCompanionProvisioningInfo(companionProvisioningInfo);
                    } catch (Exception e) {
                        errorInBackground = e;
                    }
                    return null;
                }

                @Override
                protected void onPostExecute(Void result) {
                    super.onPostExecute(result);
                    if (errorInBackground != null) {
                        connectCleanState();
                        showAlertDialog(errorInBackground);
                    } else {
                        loginSuccessState();
                    }
                }
            }.execute();
        }

        @Override
        public void onError(final AuthError authError) {
            Log.e(TAG, "AuthError during authorization", authError);
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    showAlertDialog(authError);
                }
            });
        }

        @Override
        public void onCancel(final AuthCancellation authCancellation) {
            Log.e(TAG, "User cancelled authorization");
        }
    }

    public static class ErrorDialogFragment extends DialogFragment {
        @Override
        public Dialog onCreateDialog(Bundle savedInstanceState) {
            Bundle args = getArguments();
            Exception exception = (Exception) args.getSerializable(BUNDLE_KEY_EXCEPTION);
            String message = exception.getMessage();

            return new AlertDialog.Builder(getActivity())
                    .setTitle(R.string.error)
                    .setMessage(message)
                    .setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialogInterface, int i) {
                            dismiss();
                        }
                    })
                    .create();
        }
    }
}