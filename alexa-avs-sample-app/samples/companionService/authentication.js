var crypto = require('crypto');
var https = require('https');
var uuid = require('node-uuid');
var config = require("./config");
var storage = require('node-storage');

var auth = {};

var sessionIds = [];
var sessionIdToDeviceInfo = {};
var regCodeToSessionId = {};
var pendingStateToRegCode = {};
var refreshTokenStorage = new storage('./refresh_tokens');

var REG_NUM_BYTES = 12;
var PRODUCT_MAX_LENGTH = 384;
var PRODUCT_MIN_LENGTH = 1;
var DSN_MIN_LENGTH = 1;

var UUID_REGEX = /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/;

var oAuthServer = 'https://' + config.lwaRedirectHost + '/ap/oa';
var lwaProdAuthUrl = oAuthServer + '?client_id=' + config.clientId + '&response_type=code&redirect_uri=' + config.redirectUrl;

/**
 * Create an error object to return to the user.
 *
 * @param name The name of the error.
 * @param msg The message associated with the error.
 * @param status The HTTP status code for the error.
 * @returns The error.
 */
function error(name, msg, status) {
    var err = new Error();
    err.name = name;
    err.message = msg;
    err.status = status;
    return err;
}

/**
 * Create an object of relevant LWA HTTP request information.
 *
 * @param urlPath The LWA host.
 * @returns LWA HTTP request information.
 */
function getLwaPostOptions(urlPath) {
    return {
        host: config.lwaApiHost,
        path: urlPath,
        method: 'POST',
        port: 443,
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        },
        rejectUnauthorized: config.validateCertChain
    };
}

/**
 * Redirect the user to the LWA page to authenticate.
 *
 * @param deviceInfo Device information including productId and dsn.
 * @param regCode The regCode passed in from the user.
 * @param res The HTTP response object.
 */
function redirectToDeviceAuthenticate(deviceInfo, regCode, res) {
    res.statusCode = 302;

    var state = uuid.v4();
    var productScope = {productID:deviceInfo.productId, productInstanceAttributes:{deviceSerialNumber:deviceInfo.dsn}};
    var scopeData = {};
    scopeData['alexa:all'] = productScope;

    var scopeDataStr = '&scope=' + encodeURIComponent('alexa:all') + '&state=' + encodeURIComponent(state) + '&scope_data=' + encodeURIComponent(JSON.stringify(scopeData));
    var authUrl = lwaProdAuthUrl + scopeDataStr;

    pendingStateToRegCode[state] = regCode;

    res.setHeader("Location", authUrl);
    res.end();
}

/**
 * Determine if the user provided productId and dsn match the known map.
 *
 * @param productId The productId.
 * @param dsn The dsn.
 * @returns {Boolean}
 */
function isValidDevice(productId, dsn) {
    if (productId.length >= PRODUCT_MIN_LENGTH &&
        productId.length <= PRODUCT_MAX_LENGTH &&
        dsn.length >= DSN_MIN_LENGTH &&
        config.products[productId] &&
        config.products[productId].indexOf(dsn) >= 0) {
        return true;
    }

    return false;
}

/**
 * Generate a registration code for a device, and map it to the device.
 *
 * The registration code is used by the user as a key to know what device to associate tokens with.
 *
 * @param productId The productId.
 * @param dsn The dsn.
 * @param callback The callback(err, json) to return data to the user.
 */
auth.getRegCode = function(productId, dsn, callback) {
    var missingProperties = [];
    if (!productId) {
        missingProperties.push("productId");
    }

    if (!dsn) {
        missingProperties.push("dsn");
    }

    if (missingProperties.length > 0) {
        callback(error("MissingParams", "The following parameters were missing or empty strings: " + missingProperties.join(", "), 400));
        return;
    }

    if (!isValidDevice(productId, dsn)) {
        callback(error("BadRequest", "The provided product and dsn do not match valid values", 400));
        return;
    }

    crypto.randomBytes(REG_NUM_BYTES, function(err, regCodeBuffer) {
        if (err) {
            console.log("failed on generate bytes", err);
            callback(error("InternalError", "Failure generating code", 500));
            return;
        } else {
            var regCode = regCodeBuffer.toString('hex');
            var sessionId = uuid.v4();
            sessionIds.push(sessionId);
            regCodeToSessionId[regCode] = sessionId;
            sessionIdToDeviceInfo[sessionId] = {
                productId: productId,
                dsn: dsn,
            };

            reply = {
                regCode: regCode,
                sessionId: sessionId,
            };

            callback(null, reply);
        }
    });
};

/**
 * Get an accessToken associated with the sessionId.
 *
 * Makes a request to LWA to get accessToken given the stored refreshToken.
 *
 * @param sessionId The sessionId for this device.
 * @param callback The callback(err, json) to return data to the user.
 */
auth.getAccessToken = function(sessionId, callback) {
    var missingProperties = [];
    if (!sessionId) {
        missingProperties.push("sessionId");
    }

    if (missingProperties.length > 0) {
        callback(error("MissingParams", "The following parameters were missing or empty strings: " + missingProperties.join(", "), 400));
        return;
    }

    var refreshToken = refreshTokenStorage.get(sessionId);

    if ((refreshToken === null) || (refreshToken === undefined) || (refreshToken === "")) {
        if (sessionIds.indexOf(sessionId) == -1 || !/^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/.test(sessionId)) {
            callback(error('InvalidSessionId', 'The provided sessionId was invalid.', 401));
            return;
        }
        callback(error('InvalidSessionId', "No refresh tokens stored for this session id: " + sessionId, 401));
        return;
    }

    var options = getLwaPostOptions('/auth/o2/token');
    var reqGrant = 'grant_type=refresh_token' +
        '&refresh_token=' + refreshToken +
        '&client_id=' + config.clientId +
        '&client_secret=' + config.clientSecret;

    var req = https.request(options, function (res) {
        var resultBuffer = null;

        res.on('end', function () {
            if (res.statusCode === 200 && resultBuffer !== null) {
                var result = JSON.parse(resultBuffer);
                // Update the refresh token in the storage
                refreshTokenStorage.put(sessionId, result.refresh_token);
                // Craft the response to the device
                var reply = {
                    access_token: result.access_token,
                    expires_in: result.expires_in
                };
                callback(null, reply);
            } else {
                callback(error('TokenRetrievalFailure', 'Unexpected failure while retrieving tokens.', res.statusCode));
            }
        });

        res.on('data', function (data) {
            if (res.statusCode === 200) {
                if (resultBuffer === null) {
                    resultBuffer = data;
                } else {
                    resultBuffer = Buffer.concat([resultBuffer, data]);
                }
            } else {
                callback(error('TokenRetrievalFailure', 'Unexpected failure while retrieving tokens.', res.statusCode));
            }
        });
    });

    req.on('error', function (e) {
        callback(error('TokenRetrievalFailure', 'Unexpected failure while retrieving tokens.', 500));
    });

    req.write(reqGrant);
    req.end();
};

/**
 * Revokes token associated with the sessionId.
 *
 * @param sessionId The sessionId for this device.
 * @param callback The callback(err, json) to return data to the user.
 */
auth.revokeToken = function(sessionId, callback) {
    var missingProperties = [];
    if (!sessionId) {
        missingProperties.push("sessionId");
    }

    if (missingProperties.length > 0) {
        callback(error("MissingParams", "The following parameters were missing or empty strings: " + missingProperties.join(", "), 400));
        return;
    }

    refreshTokenStorage.remove(sessionId);

    var reply = {
        logoutSuccess: true
     };
    callback(null, reply);
};

/**
 * Redirects the user to the LWA login page to enter their username and password.
 *
 * @param regCode The registration code that was presented to the user and maps their request to the device that generated the registration code.
 * @param res The HTTP response object.
 * @param callback The callback(err, json) to return data to the user.
 */
auth.register = function (regCode, res, callback) {
    if (regCode.length != REG_NUM_BYTES*2 || !(regCode in regCodeToSessionId)) {
        callback(error('InvalidRegistrationCode', 'The provided registration code was invalid.', 401));
        return;
    } else {
        var sessionId = regCodeToSessionId[regCode];
        var prodInfo = sessionIdToDeviceInfo[sessionId];
        redirectToDeviceAuthenticate(prodInfo, regCode, res);
    }
};

/**
 * Performs the initial request for refreshToken and saves the refreshToken in disk after the user has logged in and redirected to /authresponse.
 *
 * @param authCode The authorization code that was included in the redirect from LWA.
 * @param stateCode The state code that we use to map a redirect from LWA back to device information.
 * @param callback The callback(err, json) to return data to the user.
 */
auth.authresponse = function (authCode, stateCode, callback) {
    var missingProperties = [];
    if (!authCode) {
        missingProperties.push("code");
    }

    if (!stateCode) {
        missingProperties.push("state");
    }

    if (missingProperties.length > 0) {
        callback(error("MissingParams", "The following parameters were missing or empty strings: " + missingProperties.join(", "), 400));
        return;
    }

    if (!(stateCode in pendingStateToRegCode) || !UUID_REGEX.test(stateCode)) {
        callback(error('InvalidStateCode', 'The provided state code was invalid.', 401));
        return;
    }

    var regCode = pendingStateToRegCode[stateCode];
    var sessionId = regCodeToSessionId[regCode];

    var options = getLwaPostOptions('/auth/o2/token');
    var reqGrant = 'grant_type=authorization_code' +
        '&code=' + authCode +
        '&redirect_uri=' + config.redirectUrl +
        '&client_id=' + config.clientId +
        '&client_secret=' + config.clientSecret;

    var req = https.request(options, function (res) {
        var resultBuffer = null;

        res.on('end', function () {
            if (res.statusCode === 200 && resultBuffer !== null) {
                var result = JSON.parse(resultBuffer);
                refreshTokenStorage.put(sessionId, result.refresh_token);
                callback(null, "device tokens ready");
            } else {
                callback(error('TokenRetrievalFailure', 'Unexpected failure while retrieving tokens.', res.statusCode));
            }
        });

        res.on('data', function (data) {
            if (res.statusCode === 200) {
                if (resultBuffer === null) {
                    resultBuffer = data;
                } else {
                    resultBuffer = Buffer.concat([resultBuffer, data]);
                }
            } else {
                callback(error('TokenRetrievalFailure', 'Unexpected failure while retrieving tokens.', res.statusCode));
            }
        });
    });

    req.on('error', function (e) {
        console.error('Failed to post request: ' + e.message);
    });

    req.write(reqGrant);
    req.end();
};

module.exports = auth;
