/**
 * Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */

#import <UIKit/UIKit.h>
#import <Foundation/Foundation.h>
#import "AVSDeviceResponse.h"
#import <LoginWithAmazon/LoginWithAmazon.h>
#import "ProvisioningClient.h"

@interface LoginController : UIViewController<ProvisioningClientDelegate>

// Properties for UI Controls
@property (weak, nonatomic) IBOutlet UIButton *loginButton;
@property (weak, nonatomic) IBOutlet UIButton *connectToDeviceButton;
@property (weak, nonatomic) IBOutlet UILabel *provisionSuccessText;
@property (weak, nonatomic) IBOutlet UITextField *deviceAddress;
@property (weak, nonatomic) IBOutlet UIActivityIndicatorView *deviceSearchProgress;

- (void) deviceDiscovered : (AVSDeviceResponse *) response;
- (void) deviceSuccessfulyProvisioned; 
- (void) userSuccessfullySignedIn;
- (void) errorSearchingForDevice: (NSError*) error;
- (void) errorProvisioningDevice: (NSError*) error;

@end
