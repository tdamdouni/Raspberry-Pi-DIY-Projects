var mqtt = require('mqttjs'),
    Gpio = require('onoff').Gpio,
    button = new Gpio(14, 'in', 'both'),
    led1 = new Gpio(23, 'out'),
    led2 = new Gpio(24, 'out'),
    state = 1;

var serverIP = '192.168.1.245';

mqtt.createClient(2883, serverIP, function(err, client) {
	if (err) process.exit(1);

	function setLight() {
	    console.log('switch ' + state);
	    led1.writeSync(state % 2 ? 0 : 1);
	    led2.writeSync(state % 3 ? 0 : 1);
	    client.publish({topic: 'switch state', payload: JSON.stringify(state)} );
	    button.watch(function (err, value) {
		    if (err) throw err;
		    state++;
		    if (state > 3)
			state = 0;
		    setLight();
		});
	}

	client.connect({keepalive: 3000});
	console.log('connect');

	client.on('connack', function(packet) {
		if (packet.returnCode === 0) {
		    console.log('connected '+JSON.stringify(packet));
		}
		else {
		    console.log('connack error %d', packet.returnCode);
		    process.exit(-1);
		}
	    });

	client.on('close', function() {
		process.exit(0);
	    });

	client.on('error', function(e) {
		console.log('error %s', e);
		process.exit(-1);
	    });

	setLight();
    });
