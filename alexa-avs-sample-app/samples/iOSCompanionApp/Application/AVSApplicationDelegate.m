/**
 * Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */

#import <LoginWithAmazon/LoginWithAmazon.h>
#import "AVSApplicationDelegate.h"

@implementation AVSApplicationDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{    
    self.viewController = [[[([UIApplication sharedApplication].delegate).window rootViewController] storyboard]
                                instantiateViewControllerWithIdentifier:@"loginController"];
    
    self.window.rootViewController = self.viewController;
    
    // Override point for customization after application launch.
    return YES;
}

- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation {
    // Pass on the url to the SDK to parse authorization code from the url.
    BOOL isValidRedirectLogInURL = [AIMobileLib handleOpenURL:url sourceApplication:sourceApplication];
    
    if(!isValidRedirectLogInURL) {
        return NO;
    }
    
    // App may also want to handle url
    return YES;
}

@end
