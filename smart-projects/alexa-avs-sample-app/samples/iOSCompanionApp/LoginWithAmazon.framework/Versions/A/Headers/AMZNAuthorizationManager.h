/**
 * Copyright 2012-2015 Amazon.com, Inc. or its affiliates. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy
 * of the License is located at
 *
 * http://aws.amazon.com/apache2.0/
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
 */

#import <Foundation/Foundation.h>

#import "AMZNScope.h"

NS_ASSUME_NONNULL_BEGIN

@class AMZNAuthorizeResult;
@class AMZNAuthorizeRequest;

typedef void (^AMZNAuthorizationRequestHandler)(AMZNAuthorizeResult * _Nullable result, BOOL userDidCancel, NSError * _Nullable error);
typedef void (^AMZNSignOutRequestHandler)(NSError * _Nullable error);


/**
 These constants will be used to identify what global end-points the SDK connects to. Set the `region` property to one of the following values
 
 @since 3.0
 */
typedef NS_ENUM(NSUInteger, AMZNRegion) {
    /** Setting region property to this value causes the SDK to determine the best end-points to connect to. This will be the default value in case you don't set region property explicitly */
    AMZNRegionAuto = 0,
     /** Setting region property to this value causes the SDK to connect to end-points in North America. */
    AMZNRegionNA = 1,
     /** Setting region property to this value causes the SDK to connect to end-points in Europe. */
    AMZNRegionEU = 2,
    /** Setting region property to this value causes the SDK to connect to end-points in far East. */
    AMZNRegionFE = 3
    
};

/**
 AMZNAuthorizationManager defines methods used to get authorization from a user and clean authorization state.
 
 @since 3.0
 */
@interface AMZNAuthorizationManager : NSObject

/**
 This property is used to decide whether to enable sandbox mode
 
 @since 3.0
 */
@property (nonatomic, getter=isSandboxMode) BOOL sandboxMode;

/**
 This property is used to decide which region to use.
 Set this value to one of the constants defined as part of the enum `AMZNRegion`.
 
  @since 3.0
 */
@property (nonatomic) AMZNRegion region;

+ (instancetype)sharedManager;

/**
 This method is used to get authorization from an user. The method accepts input in AMZNAuthorizeRequest type.
 
 The result is passed into the AMZNAuthorizationRequestHandler block callback. If success, the result object will
 contain a valid access token with permissions to requested scopes.
 
 If failed, the block callback will return an NSError object with corresponding error code and error domain.
 
 @since 3.0
 */
- (void)authorize:(AMZNAuthorizeRequest *)request withHandler:(AMZNAuthorizationRequestHandler)handler;

/**
 Deletes cached user tokens and other data.  Use this method to logout a user.
 
 This method removes the authorization tokens from the Keychain. It also clears the cookies from the local cookie
 storage and the server side authentication state to clear the authorization state of the users who checked the "Keep me signed in" checkbox.
 
 The result is passed into the AMZNSignOutRequestHandler block callback. If failed. the block callback will return an
 NSError object with corresponding error code and error domain.
 
 @since 3.0
 */
- (void)signOut:(AMZNSignOutRequestHandler)handler;

/**
 Helper function for `authorize:withHandler:`.
 
 Call this function from your implementation of the
 `[UIApplicationDelegate application:openURL:sourceApplication:annotation]` delegate. This method handles the
 `[UIApplicationDelegate application:openURL:sourceApplication:annotation]` call from the Safari web browser. The app
 should be calling this function when it receives a call to
 `[UIApplicationDelegate application:openURL:sourceApplication:annotation]`, passing in the `url` and the
 `sourceApplication`. If app fails to do so, the SDK will not be able to complete the login flow.
 
 The SDK validates the `url` parameter to see if it is valid for the SDK. It is possible the app may want to handle the
 `url` as well, in which case the app should first call the SDK to see if this `url` is a callback from Safari and if
 the SDK wants to process it. After processing, the SDK will return its preference and the app can then process the
 `url` if it chooses. Any error arising from this API is reported through the failure delegate used for the
 `authorizeUserForScopes:delegate:` call.
 
 @param url The url received in the `[UIApplicationDelegate application:openURL:sourceApplication:annotation]` delegate
 method.
 @param sourceApplication The sourceApplication received in the
 `[UIApplicationDelegate application:openURL:sourceApplication:annotation]` delegate method.
 @return Returns YES if the url passed in was a valid url for the SDK and NO if the url was not valid.
 @see See `authorizeUserForScopes:delegate:` for more discussion on how to work with this API to complement the login
 work flow.
 
 @since 3.0
 */
+ (BOOL)handleOpenURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication;

@end
NS_ASSUME_NONNULL_END

