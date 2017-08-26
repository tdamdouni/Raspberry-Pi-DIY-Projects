/**
 * Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */

/*!
 * @discussion A non-mutable class representing a response from the Alexa enabled  
 */
@interface  AVSDeviceResponse : NSObject

@property (readonly, nonnull) NSString *productId;
@property (readonly, nonnull) NSString *dsn;
@property (readonly, nonnull) NSString *sessionId;
@property (readonly, nonnull) NSString *codeChallenge;
@property (readonly, nonnull) NSString *codeChallengeMethod;

- (nonnull id)initWithValues: (nonnull NSString* ) productId : (nonnull NSString* ) dsn : (nonnull NSString* ) sessionId : (nonnull NSString* ) codeChallenge : (nonnull NSString* ) codeChallengeMethod;

@end
