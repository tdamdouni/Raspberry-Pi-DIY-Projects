/**
 * Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * You may not use this file except in compliance with the License. A copy of the License is located the "LICENSE.txt"
 * file accompanying this source. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the specific language governing permissions and limitations
 * under the License.
 */

#import <Foundation/Foundation.h>
#import <LoginWithAmazon/LoginWithAmazon.h>
#import "AVSDeviceResponse.h"
#import "ProvisioningClient.h"

enum Path {
    DEVICE_INFO,
    COMPANION_INFO,
};

@interface ProvisioningClient() <NSURLConnectionDataDelegate>
@property (weak, nonatomic) NSObject<ProvisioningClientDelegate> *delegate;
@property (strong, nonatomic) NSURLConnection *connection;
@property (strong, nonatomic) NSMutableData *data;
@property (assign, nonatomic) enum Path path;
@property (assign, nonatomic) NSInteger statusCode;
@property (strong, nonatomic) NSArray *caChainArray;
@end

@implementation ProvisioningClient

-(id) initWithDelegate : (NSObject<ProvisioningClientDelegate> *) delegate {
    self = [super init];
    if (self) {
        self.delegate = delegate;

        NSString *cerPath = [[NSBundle mainBundle] pathForResource:@"ca" ofType:@"der"];
        NSData *derCA = [NSData dataWithContentsOfFile:cerPath];
        SecCertificateRef caRef = SecCertificateCreateWithData(NULL, (__bridge CFDataRef)derCA);
        self.caChainArray = [NSArray arrayWithObject:(__bridge id)(caRef)];
        CFRelease(caRef);
    }

    return self;
}

- (void) getDeviceProvisioningInfo : (NSString *) deviceAddress {
    self.path = DEVICE_INFO;

    NSURL *url = [NSURL URLWithString:[NSString stringWithFormat:@"%@/provision/deviceInfo", deviceAddress]];
    NSMutableURLRequest* request = [[NSMutableURLRequest alloc] initWithURL:url];
    [request setHTTPMethod:@"GET"];
    self.connection = [NSURLConnection connectionWithRequest:request delegate:self];
    [self.connection start];
}

- (void) postCompanionProvisioningInfo: (NSString * ) deviceAddress : (NSString *) authCode : (NSString *) sessionId {
    self.path = COMPANION_INFO;

    NSURL *url = [NSURL URLWithString:[NSString stringWithFormat:@"%@/provision/companionInfo", deviceAddress]];

    NSDictionary *requestBodyDictionary = @{@"authCode":authCode,
                                            @"clientId":[AIMobileLib getClientId],
                                            @"redirectUri":[AIMobileLib getRedirectUri],
                                            @"sessionId":sessionId};

    NSData *jsonData = [NSJSONSerialization dataWithJSONObject:requestBodyDictionary
                                                       options:kNilOptions error:nil];

    NSMutableURLRequest* request = [[NSMutableURLRequest alloc] initWithURL:url];
    [request setHTTPMethod:@"POST"];
    [request setHTTPBody:jsonData];
    self.connection = [NSURLConnection connectionWithRequest:request delegate:self];
    [self.connection start];
}

- (void) handleDeviceProvisioningInfo {
    NSError *error = nil;
    NSDictionary *json = [NSJSONSerialization JSONObjectWithData:self.data options:kNilOptions error:& error];

    if (error) {
        [self.delegate errorSearchingForDevice: error];
        return;
    }

    if(([json objectForKey:@"productId"] == nil) || ([json objectForKey:@"dsn"] == nil) ||
       ([json objectForKey:@"sessionId"] == nil) || ([json objectForKey:@"codeChallenge"] == nil) ||
       ([json objectForKey:@"codeChallengeMethod"] == nil)) {
        NSDictionary *userInfo = @{NSLocalizedDescriptionKey: @"Response from server didn't contain required parameters"};
        NSError *error = [[NSError alloc] initWithDomain:[[NSBundle mainBundle] bundleIdentifier] code:400 userInfo:userInfo];
        [self.delegate errorSearchingForDevice:error];
        return;
    }

    AVSDeviceResponse * responseFromDevice = [[AVSDeviceResponse alloc] initWithValues:[json objectForKey:@"productId"]:
                                              [json objectForKey:@"dsn"]:
                                              [json objectForKey:@"sessionId"]:
                                              [json objectForKey:@"codeChallenge"]:
                                              [json objectForKey:@"codeChallengeMethod"]];
    [self.delegate deviceDiscovered : responseFromDevice];
}

- (void) handleCompanionProvisioningInfo {
    [self.delegate deviceSuccessfulyProvisioned];
}

- (void) handleServiceError {
    if (self.data == nil) {
        return;
    }
    
    NSError *error = nil;
    NSDictionary *json = [NSJSONSerialization JSONObjectWithData:self.data options:kNilOptions error:& error];
    if (json != nil) {
        NSString* errorDescription = [NSString stringWithFormat:@"An issue occured while provisioning your device. %@: %@", [json objectForKey:@"error"], [json objectForKey:@"message"]];
        NSDictionary *userInfo = @{NSLocalizedDescriptionKey: errorDescription};
        error = [[NSError alloc] initWithDomain:[[NSBundle mainBundle] bundleIdentifier] code:self.statusCode userInfo:userInfo];
    }

    [self.delegate errorProvisioningDevice:error];
}


- (void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error {
    self.connection = nil;
    self.data = nil;
    self.statusCode = 0;
    
    [self.delegate errorSearchingForDevice:error];
}

- (void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response {
    [self.data setLength:0];
    self.statusCode = [(NSHTTPURLResponse*) response statusCode];
}

- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data {
    if (self.data == nil) {
        self.data = [NSMutableData data];
    }
    
    [self.data appendData:data];
}

- (void)connectionDidFinishLoading:(NSURLConnection *)connection {
    if (self.statusCode < 200 || self.statusCode >= 300) {
        [self handleServiceError];
        return;
    }
    
    if (self.path == DEVICE_INFO) {
        [self handleDeviceProvisioningInfo];
    } else if (self.path == COMPANION_INFO) {
        [self handleCompanionProvisioningInfo];
    }
}

- (void)connection:(NSURLConnection *)connection willSendRequestForAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge {
    SecTrustRef serverTrust = challenge.protectionSpace.serverTrust;
    SecTrustResultType result;
    OSStatus error = errSecSuccess;
    if (error == errSecSuccess) {
        error = SecTrustSetAnchorCertificates(serverTrust, (__bridge CFArrayRef)self.caChainArray);
    }

    if (error == errSecSuccess) {
        error = SecTrustSetAnchorCertificatesOnly(serverTrust, YES);
    }

    if (error == errSecSuccess) {
        error = SecTrustEvaluate(serverTrust, &result);
    }

    if (error == errSecSuccess) {
        if (result == kSecTrustResultProceed || result == kSecTrustResultUnspecified) {
            [challenge.sender useCredential:[NSURLCredential credentialForTrust:serverTrust]
                 forAuthenticationChallenge:challenge];
            return;
        }
    };

    [[challenge sender] cancelAuthenticationChallenge:challenge];
}

@end
