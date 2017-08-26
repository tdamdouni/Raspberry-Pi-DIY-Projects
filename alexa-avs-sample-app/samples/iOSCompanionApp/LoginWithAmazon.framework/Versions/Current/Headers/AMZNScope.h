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

/**
 This protocol is used to define Scopes used in calling 'authorize' methods defined AMZNAuthorizationManager class. Scope classes that implements
 this protocol represent the concept of 'scope' in OAuth 2.0 protocol.
 */

NS_ASSUME_NONNULL_BEGIN
@protocol AMZNScope<NSObject>
@required

/**
 The name of a scope.
 
 @since 3.0
 */
@property (nonatomic, readonly) NSString *name;

@optional

/**
 The scope data for a given scope.
 
 @since 3.0
 */
@property (nonatomic, readonly) NSDictionary *scopeData;

@end
NS_ASSUME_NONNULL_END
