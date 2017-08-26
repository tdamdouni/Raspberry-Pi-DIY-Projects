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

typedef void (^AMZNUserFetchRequestHandler)(AMZNUser * _Nullable user, NSError * _Nullable error);

/** 
 This interface is used to define an 'user' object that represents the currently logged in Amazon customer. The interface also defines class
 methods used to retrieve stored user information if there is any.
 
 @since 3.0
 */
@interface AMZNUser : NSObject

extern NSString *const AMZNUserIDKey;
extern NSString *const AMZNUserNameKey;
extern NSString *const AMZNUserEmailKey;
extern NSString *const AMZNUserPostalCodeKey;

/**
 The ID of an authorized user.
 
 @since 3.0
 */
@property(nonatomic, readonly, strong, nullable) NSString *userID;

/**
 The name of an authorized user.
 
 @since 3.0
 */
@property(nonatomic, readonly, strong, nullable) NSString *name;

/**
 The email of an authorized user.
 
 @since 3.0
 */
@property(nonatomic, readonly, strong, nullable) NSString *email;

/**
 The postal code of an authorized user.
 
 @since 3.0
 */
@property(nonatomic, readonly, strong, nullable) NSString *postalCode;

/**
 All available profile data of an authorized user.
 
 @since 3.0
 */
@property(nonatomic, readonly, strong) NSDictionary *profileData;

/**
 Use this method to get the profile of the currently authorized user.
 
 This method returns an AMZNUser object that contains profile data of the authorized user on this app. Before calling this method, the app should make sure that it is authorized for scopes with permissions to customer's profile data. Please refer to AMZNProfileScope to find a list of scopes in such type. The profile information is first locally cached. Once the cache expires, LWA SDK will call authorization server to fetch most up-to-date profile data.
 
 The result of this API is sent to the AMZNUserFetchRequestHandler block call back. On success, the callback will return an AMZNUser object that contains previously authorized profile information. On failure, the callback will return an NSError object.
 
 @since 3.0
 */
+ (void)fetch:(AMZNUserFetchRequestHandler)handler;

@end
NS_ASSUME_NONNULL_END
