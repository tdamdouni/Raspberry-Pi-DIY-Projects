"use strict"

var mqtt    = require('mqtt');

let main  = (done) => {
  let counter = 0;
  var ops = {
    port: 1883,
    host: "iot.eclipse.org"
  };

  var client  = mqtt.connect(ops);
  client.on('message', (topic, msg)=> {
    console.log(topic,msg.toString());
    if(msg.toString() != "query-temp") {
//       console.log("Received reply.. OK.");
       let json = JSON.parse(msg.toString());
//       console.log(json.temp.toFixed(2) + " degrees C");

       client.end();
       done(null, json.temp.toFixed(1));
    }
  });

  client.on('connect', () => {
      console.log("Connected");
      console.log("Publishing message");
      client.subscribe("755560112c589693968780500472f141eb13b8c9", {qos:1}, (err)=> {
        client.publish("755560112c589693968780500472f141eb13b8c9", "query-temp", {qos:1}, (err)=> {
          console.log("Subscribing", err);
        });
          console.log("We're listening.", err)
      });
 });
};

module.exports = main;