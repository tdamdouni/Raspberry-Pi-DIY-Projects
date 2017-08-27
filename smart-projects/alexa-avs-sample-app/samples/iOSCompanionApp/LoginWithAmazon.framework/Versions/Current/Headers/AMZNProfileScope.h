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

/**
 This interface implements AMZNScope protocol and is used to define 'scopes' owned by Login with Amazon.
 
 @since 3.0
 */
@interface AMZNProfileScope : NSObject <AMZNScope>

/**
 This method returns an object of 'profile' scope.
 
 @since 3.0
 */
+ (id<AMZNScope>)profile;

/**
 This method returns an object of 'postal_code' scope.
 
 @since 3.0
 */
+ (id<AMZNScope>)postalCode;

/**
 This method returns an object of 'profile:user_id' scope.
 
 @since 3.0
 */
+ (id<AMZNScope>)userID;

@end
NS_ASSUME_NONNULL_END
