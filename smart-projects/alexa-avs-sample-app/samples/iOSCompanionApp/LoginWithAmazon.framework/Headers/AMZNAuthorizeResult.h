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

NS_ASSUME_NONNULL_BEGIN

@class AMZNUser;

/**
 This class defines the result object of the authorize:handler method defined in AMZNAuthorizationManager. The result object is passed into
 the AMZNAuthorizationRequestHandler block callback.
 
 @since 3.0
 */
@interface AMZNAuthorizeResult : NSObject

/**
 A valid access token contains permissions to requested scopes in previous authorize:handler API call.
 
 @since 3.0
 */
@property (nonatomic, strong) NSString *token;

/**
 A valid authorization code along with code verifier can be exchanged for an access token pair that
 contains permissions to requested scopes in authorize:withHandler API call.
 
 @since 3.0
 */

@property (nonatomic, strong) NSString *authorizationCode;

/**
The client id is needed as one of the parameter while exchanging authorization code for token pair
 
 @since 3.0
 */

@property (nonatomic, strong) NSString *clientId;

/**
 The redirect uri is needed as one of the parameter while exchanging the authorization code for token pair
 
 @since 3.0
 */

@property (nonatomic, strong) NSString *redirectUri;

/**
 An AMZNUser object contains user's profile information. This object is only available if the app requested scopes that contain permissions
 to customer's profile data. Refer to AMZNProfileScope to find a list of scopes in such type.
 
 @since 3.0
*/
@property (nonatomic, strong, nullable) AMZNUser *user;

@end
NS_ASSUME_NONNULL_END
