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

/**
 These constants define interactive stratgies used in executing an authorization reuest.
 Interactive strategy defnies whether to switch UI for re-authentication when calling for authorize:handler API. LWA SDK for iOS supports fllowing three types of interactive strategyes:
 
 @since v3.0
 */
typedef NS_ENUM(NSUInteger, AMZNInteractiveStrategy) {
    
    /**
     AMZNInteractiveStrategyAuto: The SDK first looks up for locally stored authorization grant. If those stored authorization grant contains all requested scopes (or any
     remaining scopes are implicitly authorized), then the SDK will then try to return currently cached access token. If the token has expired, the SDK will try to refresh and return a new
     access token. If there is no previously authorized user, or some of the requested scopes are not authorized, or the token refresh call failed, the SDK will redirect end user to SignIn flow.
     AMZNAuthorizeRequest will default to use AMZNInteractiveStrategyAuto if no interactive strategy is specified by caller.
     
     @since 3.0
     */
    AMZNInteractiveStrategyAuto = 0,
    
    /**
     AMZNInteractiveStrategyNever: In this case, the SDK only try to use locally cached authorized grant. If those stored authorization grant contains all requested scopes (or any
     remaining scopes are implicitly authorized), then the SDK will then try to return currently cached access token. If the token has expired, the SDK will try to refresh and return a new
     access token. If there is no previously authorized user, or some of the requested scopes are not authorized, or the token refresh call failed, the SDK will return error.
     
     @since 3.0
     */
    AMZNInteractiveStrategyNever = 1,
    
    /**
     AMZNInteractiveStrategyAlways: In this case, the SDK will not look up for locally stored authorization grant, instead, it will always force to redirect end user to SignIn whenever an
     authorization request is being executed.
     
     @since 3.0
     */
    AMZNInteractiveStrategyAlways = 2
};

/*
 These constants define different kinds of authorization grants that can be requested from Login With Amazon SDK. An authorization
 grant is a credential representing the access to resources that the user has granted.
 
 @since v3.0
 */
typedef NS_ENUM(NSUInteger, AMZNAuthorizationGrantType) {
    
    /**
     AMZNAuthorizationGrantTypeToken: An OAuth 2.0 access token. When requesting an access token, Login With Amazon SDK will persist this token and
     refresh it when necessary on your behalf.
     AMZNAuthorizeRequest will default to use AMZNAuthorizationGrantTypeToken if no interactive strategy is specified by caller.
     
     @since 3.0
     */
    AMZNAuthorizationGrantTypeToken = 0,
    
    /**
     AMZNAuthorizationGrantTypeCode: An OAuth 2.0 authorization code grant. Login With Amazon SDK does not persist this grant and does not allow
     access to use Login With Amazon-enabled APIs that require authorization.
     
     @since 3.0
     */
    AMZNAuthorizationGrantTypeCode = 1
};


/**
 This class is used to define an input request object when calling authorize:handler method in AMZNAuthorizationHandler
 class.
 
 @since 3.0
 */
@interface AMZNAuthorizeRequest : NSObject

/**
 This property represents a list of scopes object that request authorization. Each scope object in the scopes array
 should be in AMZNScope type.
 
 @since 3.0
 */
@property (nonatomic, strong) NSArray *scopes;

/**
 This property represents desired interactive strategy of an authorization request. See detailed usage in
 AMZNInteractiveStrategy type.
 
 @since 3.0
 */
@property (nonatomic) AMZNInteractiveStrategy interactiveStrategy;

/**
 This property represents which grant type to use during authorization. See detailed usage in
 AMZNAuthorizationGrantType type
 
 @since 3.0
 */
@property (nonatomic) AMZNAuthorizationGrantType grantType;

/**
 This property let you pass a code challenge when you request grant type as AMZNAuthorizationGrantTypeCode
 
 @since 3.0
 */
@property (nonatomic, strong) NSString *codeChallenge;

/**
 This property let you pass a code challenge when you request grant type as AMZNAuthorizationGrantTypeCode
 
 @since 3.0
 */
@property (nonatomic, strong) NSString *codeChallengeMethod;

@end
NS_ASSUME_NONNULL_END
