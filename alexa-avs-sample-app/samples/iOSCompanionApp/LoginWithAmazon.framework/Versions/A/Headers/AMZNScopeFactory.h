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
#import "AIError.h"

NS_ASSUME_NONNULL_BEGIN

/**
 This interface defines faction methods to create a scope object that can be used as properties in a LWAAuthorizeRequest object.
 
 @since 3.0
 */
@interface AMZNScopeFactory : NSObject

/**
 This method returns a scope object with input name.
 
 @since 3.0
 */
+ (id<AMZNScope>)scopeWithName:(NSString *)scopeName;

/**
 This method returns a scope object with input name and scope data.
 
 @since 3.0
 */
+ (id<AMZNScope>)scopeWithName:(NSString *)scopeName data:(NSDictionary *)scopeData;

/**
 This method returns scope name and scope data in a json format.
 
 @since 3.0
 */
+ (NSString *)getScopeDataAsJsonString:(NSArray *)scopes withErrorObject:(AIError *)errorObject;

@end

NS_ASSUME_NONNULL_END
