let rpio = require("rpio"), stream = require("stream"), util = require("util");

let DATA_PIN = 16;
let CLOCK_PIN = 18;
let BFF_PIN = 29;
let BPP_PIN = 31;
let BRW_PIN = 33;
let BUP_PIN = 36;
let BDN_PIN = 37;
let BOF_PIN = 32;
let ledCount = 16;
let ledPerChannel = 8;
let defaultBrightness = 7;
let leds = [];

util.inherits(ButtonStream, stream.Readable);
var buttonProto = ButtonStream.prototype;

function ButtonStream(pin) {
	if (!(this instanceof ButtonStream)) {
		return new ButtonStream(pin);
	}

	stream.Readable.call(this);
	rpio.open(pin, rpio.INPUT, rpio.PULL_UP);
	this.monitorPin = pin;
	this.monitor();
}

buttonProto.monitorPin;
buttonProto.monitoring = false;
buttonProto.buffer = [];
buttonProto.lastPress = 0;
buttonProto.closeTimeout = 5000;
buttonProto.shouldClose = false;

buttonProto.monitor = function () {
	rpio.poll(this.monitorPin, function () {
		let state = rpio.read(this.monitorPin) === 1 ? 0 : 1;
		this.buffer.push(state);
		this.emit("pinChange", this.monitorPin, state);
		if (state === 1) {
			this.lastPress = new Date().getTime();
		} else {
			if (this.lastPress > 0 && (new Date().getTime() - this.lastPress) > this.closeTimeout) {
				this.shouldClose = true;
				rpio.close(this.monitorPin);
				this.emit("end", this.monitorPin);
			}
			this.lastPress = 0;
		}
	}.bind(this));

	this.monitoring = true;
	setTimeout(function () { this.emit("monitoring", this.monitorPin) }.bind(this), 100);
}

buttonProto._read = function () {
	if (this.shouldClose) {
		return this.push(null);
	}

	if (!this.monitoring) {
		return this.once('monitoring', function () {
			this._read();
		});
	}

	if (this.buffer.length === 0) {
		return this.once('pinChange', function () {
			this._read();
		});
	}

	this.push(this.monitorPin + "," + this.buffer.shift().toString() + '\n');
};

let _start = function () {
	rpio.write(DATA_PIN, 0);
	for (let i = 0; i < 32; i++) {
		rpio.write(CLOCK_PIN, 1);
		rpio.write(CLOCK_PIN, 0);
	}
};

let _end = function () {
	rpio.write(DATA_PIN, 0);
	for (let i = 0; i < 36; i++) {
		rpio.write(CLOCK_PIN, 1);
		rpio.write(CLOCK_PIN, 0);
	}
};

let _writeByte = function (byte) {
	for (let x = 0; x < 8; x++) {
		rpio.write(DATA_PIN, byte & 0b10000000);
		rpio.write(CLOCK_PIN, 1);
		byte <<= 1;
		rpio.write(CLOCK_PIN, 0);
	}
};

let _closeButtons = function () {
	rpio.close(BFF_PIN);
	rpio.close(BPP_PIN);
	rpio.close(BRW_PIN);
	rpio.close(BUP_PIN);
	rpio.close(BDN_PIN);
	rpio.close(BOF_PIN);
};

let _close = function () {
	rpio.close(DATA_PIN);
	rpio.close(CLOCK_PIN);
	_closeButtons();
};

let _getBrightness = function (brightness) {
	return Number(31.0 * brightness) & 0b111111;
};

let _validateBrightness = function (brightness) {
	if (brightness > 1.0 || brightness < 0.1) {
		throw 'Brightness must be between 0.1 and 1.0, provided was ' + brightness;
	}
};

function init_led(customBrightness) {
	let brightnessToUse = defaultBrightness;

	if (customBrightness) {
		_validateBrightness(customBrightness);
		brightnessToUse = _getBrightness(customBrightness);
	}

	for (let led = 0; led < ledCount; led++) {
		leds.push({
			red: 0,
			green: 0,
			blue: 0,
			brightness: brightnessToUse
		});
	}

	rpio.open(DATA_PIN, rpio.OUTPUT);
	rpio.open(CLOCK_PIN, rpio.OUTPUT);
}

function changeSingleLED(arrayIndex, red, green, blue, redraw, changeBrightness) {
	let newBrightness = null;

	if (arrayIndex > ledCount - 1 || arrayIndex < 0) {
		throw arrayIndex + " is not valid within the array";
	}

	if (changeBrightness) {
		_validateBrightness(changeBrightness);
		newBrightness = _getBrightness(changeBrightness);
	}

	leds[arrayIndex].red = red;
	leds[arrayIndex].green = green;
	leds[arrayIndex].blue = blue;
	leds[arrayIndex].brightness = newBrightness || leds[arrayIndex].brightness;

	if (redraw) {
		this.redraw();
	}
}

function changeAllChannelLEDs(red, green, blue, channel, redraw, changeBrightness) {
	let validChannels = [0, 1];
	let newBrightness = null;

	if (validChannels.indexOf(Number(channel)) === -1) {
		throw 'Provided channel (' + channel + ') was invalid. Please provide either 0 or 1';
	}

	if (changeBrightness) {
		_validateBrightness(changeBrightness);
		newBrightness = _getBrightness(changeBrightness);
	}

	let startingPosition = channel === 0 ? channel : ledPerChannel;
	let endingPosition = channel === 0 ? channel + (ledPerChannel - 1) : (ledPerChannel * 2) - 1;

	for (let i = startingPosition; i <= endingPosition; i++) {
		leds[i].red = red;
		leds[i].green = green;
		leds[i].blue = blue;
		leds[i].brightness = newBrightness || leds[i].brightness;
	}

	if (redraw) {
		this.redraw();
	}
}

function getButtonPins() {
	let buttons = [];

	buttons.push({
		pin: BFF_PIN,
		name: "FAST_FORWARD"
	});

	buttons.push({
		pin: BPP_PIN,
		name: "PLAY_PAUSE"
	});

	buttons.push({
		pin: BRW_PIN,
		name: "REWIND"
	});

	buttons.push({
		pin: BUP_PIN,
		name: "VOL_UP"
	});

	buttons.push({
		pin: BDN_PIN,
		name: "VOL_DOWN"
	});

	buttons.push({
		pin: BOF_PIN,
		name: "POWER"
	});

	return buttons;
}

function changeAllLEDs(red, green, blue, redraw, changeBrightness) {
	let newBrightness = null;
	if (changeBrightness) {
		_validateBrightness(changeBrightness);
		newBrightness = _getBrightness(changeBrightness);
	}

	for (let led = 0; led < ledCount; led++) {
		leds[led].red = red;
		leds[led].green = green;
		leds[led].blue = blue;
		leds[led].brightness = newBrightness || leds[led].brightness;
	}

	if (redraw) {
		this.redraw();
	}
}


function redraw() {
	_start();
	for (let i = 0; i < leds.length; i++) {
		_writeByte(0b11100000 | leds[i].brightness);
		_writeByte(Number(leds[i].blue) & 0xff);
		_writeByte(Number(leds[i].green) & 0xff);
		_writeByte(Number(leds[i].red) & 0xff);
	}
	_end();
}

function turnOffAllLEDs(redraw) {
	changeAllLEDs(0, 0, 0);
	if (redraw) {
		this.redraw();
	}
}

function teardown(turnOff) {
	if (turnOff) {
		this.turnOffAllLEDs(true);
	}
	_close();
}

module.exports.init_led = init_led;
module.exports.changeAllLEDs = changeAllLEDs;
module.exports.changeSingleLED = changeSingleLED;
module.exports.changeAllChannelLEDs = changeAllChannelLEDs;
module.exports.redraw = redraw;
module.exports.turnOffAllLEDs = turnOffAllLEDs;
module.exports.teardown = teardown;
module.exports.getButtonPins = getButtonPins;
module.exports.buttonStream = ButtonStream;

module.exports.VERSION = "1.0.0";
module.exports.LEDCOUNT = ledCount;
module.exports.CHANNEL_LEDS = ledPerChannel;