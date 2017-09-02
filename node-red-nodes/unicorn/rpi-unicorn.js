/**
 * Copyright 2016 Pimoroni Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 **/

module.exports = function(RED) {
    "use strict";

    function REDvWarn(message){
        if( RED.settings.verbose ) RED.log.warn("Unicorn: " + message);
    }
    
    function REDvInfo(message){
        if( RED.settings.verbose ) RED.log.info("Unicorn: " + message);
    }

    var HAT = (function(){

        var fs = require("fs");
        var spawn = require("child_process").spawn;

        var cmd = __dirname+"/unicornlink";
        var hat = null;
        var allowExit = false;
        var reconnectTimer = null;
        var disconnectTimeout = null;
        var users = [];

        if ( !(fs.statSync(cmd).mode & 1) ) {
            throw "Error: '" + cmd + "' must be executable (755)";
        }

        process.env.PYTHONBUFFERED = 1;

        var connect = function() {
            if( reconnectTimer ) clearTimeout(reconnectTimer);

            reconnectTimer = null;
            allowExit = false;

            hat = spawn(cmd);

            users.forEach(function(node){
                node.status({fill:"green",shape:"dot",text:"Connected"});
            });

            function handleMessage(data){
                data = data.trim();
                if (data.length == 0) return;

                if (data.substring(0,5) == "ERROR"){
                    REDvWarn(data);
                    return;
                }

                if (data.substring(0,5) == "FATAL"){
                    throw "Error: " + data;
                }
            }

            hat.stdout.on('data', function(data) {
                data = data.toString().trim();
                if (data.length == 0) return;

                var messages = data.split("\n");
                messages.forEach(function(message){
                    handleMessage(message);
                });
                REDvInfo("Got Data: " + data + " :");

            });

            hat.stderr.on('data', function(data) {
                REDvWarn("Process Error: "+data+" :");

                hat.stdin.write("stop");
                hat.kill("SIGKILL");
            });

            hat.on('close', function(code) {
                REDvWarn("Process Exit: "+code+" :");

                hat = null;
                users.forEach(function(node){
                    node.status({fill:"red",shape:"circle",text:"Disconnected"});
                });

                if (!allowExit && !reconnectTimer){
                    REDvInfo("Attempting Reconnect");

                    reconnectTimer = setTimeout(function(){
                        connect();
                    },5000);
                }

            });

        }

        var disconnect = function(){
            disconnectTimeout = setTimeout(function(){
                if (hat !== null) {
                    allowExit = true;
                    hat.stdin.write("stop\n");
                    hat.kill("SIGKILL");
                }
            },3000);
            if (reconnectTimer) {
                clearTimeout(reconnedTimer);
            }

        }

        return {
            open: function(node){
                if (disconnectTimeout) clearTimeout(disconnectTimeout);
                if (!hat) connect();

                if(!reconnectTimer){
                    node.status({fill:"green",shape:"dot",text:"Connected"});
                }

                users.push(node);

                REDvInfo("Adding node, count: " + users.length.toString());
            },
            close: function(node,done){
                users.splice(users.indexOf(node),1);
                
                REDvInfo("Removing node, count: " + users.length.toString());

                if(users.length === 0){
                    disconnect();
                }
            },
            send: function(msg){
                if(hat) hat.stdin.write(msg+"\n");
            }
        }


    })();

    function UnicornOut(config) {
        RED.nodes.createNode(this,config);
 
        var node = this;

        HAT.open(this);

        node.on("input", function(msg) {
            if ( typeof msg.payload === "string" ){
                HAT.send(msg.topic + ":" + msg.payload.toString());
                REDvInfo("Sending Command: " + msg.topic + ":" + msg.payload.toString());
            }
        });

        node.on("close", function(done) {
            done();
        });
    }

    RED.nodes.registerType("rpi-unicorn out",UnicornOut);
}
