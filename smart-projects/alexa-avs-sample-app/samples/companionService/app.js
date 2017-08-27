var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var auth = require('./authentication.js');

var app = express();
app.use(bodyParser.json());

/**
 * The endpoint for the device to request a registration code to then show to the user.
 */
app.get('/provision/regCode', function (req, res) {
    if (!req.client.authorized) {
        console.error("User is not authorized to access this URL. Make sure the client certificate is set up properly");
        res.status(401);
        res.send({ error: "Unauthorized", message: "You are not authorized to access this URL. Make sure your client certificate is set up properly." });
        return;
    }

    auth.getRegCode(req.query.productId, req.query.dsn, function (err, reply) {
        if (err) {
            console.error("Error retrieving registration code: " + err.name + ", " + err.message);
            res.status(err.status);
            res.send({ error: err.name, message: err.message });
        } else {
            console.log("Successfully retrieved registration code for " + req.query.productId + " / " + req.query.dsn);
            res.send(reply);
        }
    });
});

/**
 * The endpoint for the device to request a new accessToken when the previous one expires.
 */
app.get('/provision/accessToken', function (req, res) {
    if (!req.client.authorized) {
        console.error("User is not authorized to access this URL. Make sure the client certificate is set up properly");
        res.status(401);
        res.send({ error: "Unauthorized", message: "You are not authorized to access this URL. Make sure your client certificate is set up properly." });
        return;
    }

    auth.getAccessToken(req.query.sessionId, function (err, reply) {
        if (err) {
            console.error("Error retrieving access token: " + err.name + ", " + err.message);
            res.status(err.status);
            res.send({ error: err.name, message: err.message });
        } else {
            console.log("Successfully retrieved access token for session id: " + req.query.sessionId);
            res.send(reply);
        }
    });
});

/**
 * The endpoint for the device to revoke a token.
 */
app.get('/provision/revokeToken', function (req, res) {
    if (!req.client.authorized) {
        console.error("User is not authorized to access this URL. Make sure the client certificate is set up properly");
        res.status(401);
        res.send({ error: "Unauthorized", message: "You are not authorized to access this URL. Make sure your client certificate is set up properly." });
        return;
    }

    auth.revokeToken(req.query.sessionId, function (err, reply) {
        if (err) {
            console.error("Error revoking token: " + err.name + ", " + err.message);
            res.status(err.status);
            res.send({ error: err.name, message: err.message });
        } else {
            console.log("Successfully revoked token for session id: " + req.query.sessionId);
            res.send(reply);
        }
    });
});

/**
 * The endpoint for the customer to visit and get redirected to LWA to login.
 */
app.get('/provision/:regCode', function (req, res, next) {
    auth.register(req.params.regCode, res, function (err) {
        // on success gets redirect so wont return to a callback.
        res.status(err.status);
        res.send({ error: err.name, message: err.message });
        next(err);
    });
});

/**
 * The endpoint that LWA will redirect to to include the authorization code and state code.
 */
app.get('/authresponse', function (req, res) {
    auth.authresponse(req.query.code, req.query.state, function (err, reply) {
        if (err) {
            res.status(err.status);
            res.send({ error: err.name, message: err.message });
        } else {
            res.send(reply);
        }
    });
});

// standard error handling functions.
app.use(function (req, res, next) {
    // Suppress /favicon.ico errors
    var favicon = "favicon.ico";
    if (req.url.slice(-favicon.length) != favicon) {
        var err = new Error('Not Found: ' + req.url);
        err.status = 404;
        next(err);
    } else {
        next();
    }
});

app.use(function (err, req, res, next) {
    console.log("error: ", err);
    res.status(err.status || 500);
    res.send('error: ' + err.message);
});

module.exports = app;
