/**
 * Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */

#import <Foundation/Foundation.h>
#import "AVSDeviceResponse.h"

@protocol ProvisioningClientDelegate

@required

- (void) errorSearchingForDevice: (NSError *) error;

- (void) errorProvisioningDevice: (NSError *) error;

- (void) deviceDiscovered : (AVSDeviceResponse *) response;

- (void) deviceSuccessfulyProvisioned;

@end

/*!
 * @discussion A client to asynchronously handle communication and provisioning with an Alexa enbaled device on the 
 * current network. The client can be used to request metadata from the device that will be used to provision the device.
 * The client can also be used to send post provisioning info to the device.
 */
@interface ProvisioningClient : NSObject

-(id) initWithDelegate:(NSObject<ProvisioningClientDelegate> *) delegate;

/*!
 * @discussion Open an HTTP connection to the Alexa enabled device. Sends a GET request to the device and
 * returns the response. The response contains relevant information that should be used by the Alexa enabled device to
 * get the authorization code.
 */
- (void) getDeviceProvisioningInfo : (NSString *) deviceAddress;

/*!
 * @discussion Open an HTTP connection to the Alexa enabled device. Sends a POST request to the device that contains
 * the information for the Alexa enabled device to get an access token. In particular the post request should
 * contain the authorization code.
 */
- (void) postCompanionProvisioningInfo: (NSString *) deviceAddress : (NSString *) authCode : (NSString *) sessionId;

@end

