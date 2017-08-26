"use strict"

var APP_ID = undefined;

var intentHandler = require("./intentHandler");
var AlexaSkill = require('./AlexaSkill');

var Envirophat = function () {
    AlexaSkill.call(this, APP_ID);
};

// Extend AlexaSkill
Envirophat.prototype = Object.create(AlexaSkill.prototype);
Envirophat.prototype.constructor = Envirophat;

Envirophat.prototype.eventHandlers.onSessionStarted = function (sessionStartedRequest, session) {
    console.log("Envirophat onSessionStarted requestId: " + sessionStartedRequest.requestId
        + ", sessionId: " + session.sessionId);
    // any initialization logic goes here
};

Envirophat.prototype.eventHandlers.onLaunch = function (launchRequest, session, response) {
    console.log("Envirophat onLaunch requestId: " + launchRequest.requestId + ", sessionId: " + session.sessionId);
    response.ask("Welcome to Envirophat", "Ask me the temperature");
};

Envirophat.prototype.eventHandlers.onSessionEnded = function (sessionEndedRequest, session) {
    console.log("Envirophat onSessionEnded requestId: " + sessionEndedRequest.requestId
        + ", sessionId: " + session.sessionId);
};

Envirophat.prototype.intentHandlers = {
    // register custom intent handlers
    "EnvirophatTemperatureIntent": function (intent, session, response) {
        intentHandler((err, result) => {
            var speechOutput = "The ambient temperature is " + result + " degrees celcius.";
            response.tellWithCard(speechOutput, "Envirophat update", speechOutput);
        });
   },
   "AMAZON.HelpIntent": function (intent, session, response) {
        response.ask("You can ask me the temperature", "You can ask me the temperature");
    }
};

// Create the handler that responds to the Alexa Request.
exports.handler = function (event, context) {
    // Create an instance of the Envirophat skill.
    var helloWorld = new Envirophat();
    helloWorld.execute(event, context);
};
