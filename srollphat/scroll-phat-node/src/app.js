var i2c = require('i2c-bus')

var i2c_address = 0x60;
var cmd_set_mode = 0x00;
var cmd_set_brightness = 0x19;
var cmd_set_pixels = 0x01;

var mode_5x11 = "00000011";

var max_brightness = 8;
var brightness = 3;

function init(brightnessValue) {
	var wire = i2c.openSync(1);
	wire.writeByteSync(i2c_address, cmd_set_mode, parseInt(mode_5x11, 2));
	wire.writeByteSync(i2c_address, cmd_set_brightness, Number(brightnessValue));
	return wire;
}

function write(wireInstance, val) {
	var buffer = [];
	var size = 11;

	for (var n=0; n< size; n++) {
	    buffer.push(0);
	}

	var uint = new Uint8Array(buffer.length+1);
	for (var i = 0 ; i < uint.length; i++) {
	    buffer[i]=val;
	    uint[i] = buffer[i];
	}
	uint[uint.length] = 255;

	wireInstance.writeI2cBlockSync(i2c_address, cmd_set_pixels, buffer.length, uint);
}

var printValuesTo = function(maxValue, delayMs, doneCallback) {
	var i = 0;
	var val = setInterval(function() {
		console.log("Printing: " + i);
		write(wire, i);
		if(i>=maxValue) {
			doneCallback();
			clearTimeout(val);
		}
		i++;
	}, delayMs);
}

var wire = init(brightness);

printValuesTo(31, 200, function () {

	write(wire, 0);
	wire.closeSync();
});
