var flotilla = require("pimoroni-flotilla");

/*
 * Flotilla Node-RED Node
 * 
 * - Should support multiple docks
 * - Each dock has up to 8 connected modules
 * - Each module may have one or more inputs or outputs;
 *    - Like temperature/pressure as inputs on Weather
 *    - Or time/temperature as outputs on Number
 *
 * UX
 * 
 * A drop down list should display a list of Docks. Ideally any connected dock would be queried for its particulars
 * so that this list could use the dock friendly-name if its set.
 *
 * Once a Dock is selected, an asyncronous connection is established and maintained, and the connected modules enumerated.
 *
 * The list of connected modules populates a second drop down list (or a nice grid of icons if we're feeling sassy)
 *
 * Selecting/clicking a connected module would prompt a third UI widget for selecting a particular module output/input stream and configuring options.
 *
 * Internally
 *
 * The Flotilla onUpdate hook would be used to collect updates from connected modules and dispatch them to the nodes concerned.
 *
 * The relationship between nodes and Docks should be keyed upon comPort
 *
*/

var docks = {};
var inputNodes = [];
var outputNodes = [];

function findDock(module, serial, callback, err) {
    for(var comName in docks){
        if(typeof comName === "undefined") continue;

        var dock = docks[comName];

        if(dock.dockSerial === serial){
            callback(dock);
            return;
        }
    }
    err("Unable to find Dock: " + serial);
}

function getDock(module, comName, callback, err) {

    if(typeof comName === "undefined" || comName === null || comName === "null") {
        err("Invalid com port");
        return;
    }

    if(docks[comName]) {
        callback(docks[comName]);
        return;
    }

    docks[comName] = new flotilla({
        portName: comName,
        onOpen: function(flotilla, args){
            module.REDvInfo(comName + " opened!");

            if(typeof callback === "function") {
                callback(flotilla);
                err = null;
                callback = null;
            }            
        },
        onUpdate: function(flotilla, args){
            inputNodes.forEach(function(node, index){
                if(node.serial == flotilla.dockSerial
                && node.channel == args.channel 
                && typeof node.onUpdate === "function"){
                    node.onUpdate(args);
                }
            });
        },
        onLost: function(flotilla, args){
            inputNodes.forEach(function(node, index){
                if(node.serial == flotilla.dockSerial
                && node.channel == args.channel
                && typeof node.onLost === "function"){
                    node.onLost(args);
                }
            });
        },
        onFound: function(flotilla, args){
            inputNodes.forEach(function(node, index){
                if(node.serial == flotilla.dockSerial
                && node.channel == args.channel
                && typeof node.onFound === "function"){
                    node.onFound(args);       
                }
            });
        },
        onInfo: function(flotilla, message){
            module.REDvInfo(message);
        },
        onError: function(flotilla, message){
            module.REDWarn(message);

            if(typeof err === "function") {
                err(message);
                err = null;
                callback = null;
            }
            docks[comName] = null;
        },
    });

};

module.exports = function(RED) {
    "use strict";

    var module = (function(RED){
        return {
            REDWarn: function(message){
                RED.log.warn("Flotilla: " + message);
            },
            REDvWarn: function(message){
                if( RED.settings.verbose ) RED.log.warn("Flotilla: " + message);
            },
            REDvInfo: function(message){
                if( RED.settings.verbose ) RED.log.info("Flotilla: " + message);
            }
        }
    })(RED);

    var RefreshDocksFrequency = 4000; // Run Refresh Docks every n/1000 seconds

    function RefreshDocks() {
        module.REDvInfo("Polling for new Docks...");

        flotilla.listDocks(function(docks){
            docks.forEach(function(dock, index){
                getDock(module,dock.comName,function(){},function(){});
            });
        });
    }

    var PollDocks = setInterval(RefreshDocks,RefreshDocksFrequency);

    function FlotillaInput(config) {
        RED.nodes.createNode(this,config);

        this.serial = config.flotillaSerial;
        this.channel = parseInt(config.flotillaChannel);
        this.input = config.flotillaInput;

        var node = this;

        this.onUpdate = function(args){
            if(node.input === "all"){
                node.send({topic:"flotilla/" + args.channel + "/" + args.module, payload: args.input});
            }
            else if(typeof args.input[node.input] !== "undefined"){
                node.send({topic:"flotilla/" + args.channel + "/" + args.module + "/" + node.input, payload: args.input[node.input]});
            }   
        };

        inputNodes.push(node);

        node.on("close", function(done) {
            inputNodes.splice(inputNodes.indexOf(node),1);
            done();
        });
    }
    RED.nodes.registerType("node-flotilla in", FlotillaInput);

    function FlotillaOutput(config) {
        RED.nodes.createNode(this,config);

        this.serial = config.flotillaSerial;
        this.channel = parseInt(config.flotillaChannel) - 1;
        this.output = config.flotillaOutput;

        var node = this;

        node.on("input", function(msg) {

                findDock(module, node.serial, function(dock){
                    if(dock.modules[node.channel]){
                        if(typeof dock.modules[node.channel].output[node.output] === "function"){
                            // Handle single numerical value, for outputs which take just one argument (number, motor, etc)
                            if (typeof msg.payload === "number"){
                                dock.modules[node.channel].output[node.output](msg.payload);

                                // If the module has a "show" method, then call it automatiacally.
                                // It's clunky to have to do so explicitly in Node-RED!
                                if(typeof dock.modules[node.channel].output["show"] === "function"){
                                    dock.modules[node.channel].output["show"]();
                                }
                                return;
                            }
                            // Handle array with multiple sets of function arguments
                            if (typeof msg.payload === "object" && typeof msg.payload[0] === "object" && msg.payload.length > 0){
                                for(var x = 0; x < msg.payload.length; x++){
                                    dock.modules[node.channel].output[node.output].apply(this, msg.payload[x]);
                                }

                                // If the module has a "show" method, then call it automatiacally.
                                // It's clunky to have to do so explicitly in Node-RED!
                                if(typeof dock.modules[node.channel].output["show"] === "function"){
                                    dock.modules[node.channel].output["show"]();
                                }
                                return;
                            }
                            // Handle single set of function arguments
                            if (typeof msg.payload === "object"){
                                dock.modules[node.channel].output[node.output].apply(this, msg.payload);

                                // If the module has a "show" method, then call it automatiacally.
                                // It's clunky to have to do so explicitly in Node-RED!
                                if(typeof dock.modules[node.channel].output["show"] === "function"){
                                    dock.modules[node.channel].output["show"]();
                                }
                                return;
                            }
                        }
                    }
                }, function(err){});           

        });

        outputNodes.push(node);

        node.on("close", function(done) {
            outputNodes.splice(outputNodes.indexOf(node),1);
            done();
        });
    }
    RED.nodes.registerType("node-flotilla out", FlotillaOutput);

    function FlotillaModify(config) {
        RED.nodes.createNode(this,config);
    }
    RED.nodes.registerType("node-flotilla modify", FlotillaModify);

    RED.httpAdmin.get("/flotilla/docks", RED.auth.needsPermission("serial.read"), function(req,res) {
        res.json(docks);
    });

    RED.httpAdmin.get("/flotilla/module", RED.auth.needsPermission("serial.read"), function(req,res) {
        var serial = req.query.serial;
        var channel = parseInt(req.query.channel) - 1;
        findDock(module, serial, function(dock){
            res.send(JSON.stringify(dock.modules[channel], function(k,v){
                // Include functions in the JSON by setting their value to the text string "function"
                // exclude any "show" functions, since we call those internally
                if(typeof v === "function" && k !== "show"){
                    return "function";
                }
                return v;
            }));
        },
        function(message){
            res.json({error:message});
        });
    });

    RED.httpAdmin.get("/flotilla/dock", RED.auth.needsPermission("serial.read"), function(req,res) {
        var serial = req.query.serial;
        findDock(module, serial, function(dock){
            res.json(dock.modules);     
        },
        function(message){
            res.json({error:message});
        });
    });

};
