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

@implementation AVSDeviceResponse

- (id)initWithValues: (NSString*) productId : (NSString*) dsn : (NSString*) sessionId : (NSString*) codeChallenge : (nonnull NSString* ) codeChallengeMethod {
    if( self = [super init]) {
        _productId = productId;
        _dsn = dsn;
        _sessionId = sessionId;
        _codeChallenge = codeChallenge;
        _codeChallengeMethod = codeChallengeMethod;
    }
    return self;
}

@end
