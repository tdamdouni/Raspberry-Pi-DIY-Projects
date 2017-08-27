var mqtt = require('mqttjs');
var readline = require('readline');
var port = 1883;

var rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
    });

mqtt.createServer(function(client) {
	var self = this;

	process.stdin.resume();
	process.stdin.setEncoding('utf8');

	if (!self.clients) self.clients = {};

	client.on('connect', function(packet) {
		console.log('connection from '+packet.client);
		client.connack({returnCode: 0});
		client.id = packet.client;
		self.clients[client.id] = client;
	    });

	client.on('publish', function(packet) {
		console.log('got ['+packet.topic+' | '+packet.payload+']');
	    });

	client.on('subscribe', function(packet) {
		console.log('subscribe '+packet.subscriptions);
		var granted = [];
		for (var i = 0; i < packet.subscriptions.length; i++) {
		    granted.push(packet.subscriptions[i].qos);
		}

		client.suback({granted: granted});
	    });

	client.on('pingreq', function(packet) {
		console.log('pingreq');
		client.pingresp();
	    });

	client.on('disconnect', function(packet) {
		console.log('disconnect');
		delete self.clients[client.id];
		client.stream.end();
	    });

	client.on('close', function(err) {
		console.log('close');
		delete self.clients[client.id];
	    });

	client.on('error', function(err) {
		console.log('error');
		client.stream.end();
		util.log('error!');
	    });

	rl.on('line', function (cmd) {
		console.log('sending ['+cmd+']');
		for (var k in self.clients) {
		    self.clients[k].publish({topic: "msg", payload: cmd});
		}
	    });

    }).listen(port);
