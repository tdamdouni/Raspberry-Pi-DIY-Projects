'use strict';

const wpi = require('wiring-pi');
const convert = require('./colorConvert');

class Blinkt {
	constructor(options) {
		options = options || {};

		// pins - give defaults
		this.pinDAT = options.DAT || 23;
		this.pinCLK = options.CLK || 24;

		// WiringPi setup
		wpi.setup('gpio');
		wpi.pinMode(this.pinDAT, wpi.OUTPUT);
		wpi.pinMode(this.pinCLK, wpi.OUTPUT);

		this.clearOnExit = options.clearOnExit === false ? false : true;
		this.format = options.colorFormat || 'RGB';
		this.pixelCount = options.pixelCount || 8;
		this.brightness = options.defaultBrightness || 0.5;
		this.pixels = [];

		// init pixels
		for (let i = 0; i < this.pixelCount; i++) {
			this.pixels.push([0, 0, 0, this.brightness]);
		}

		// register listener to turn off lights on exit
		if (this.clearOnExit) {
			process.on('exit', () => {
				this.off();
			});
		}
	}

	_clocker(count) {
		wpi.digitalWrite(this.pinDAT, 0);
		for (var i = 0; i < count; i++) {
			wpi.digitalWrite(this.pinCLK, 1);
			wpi.digitalWrite(this.pinCLK, 0);
		}
	}

	_writeByte(byte) {
		let bit;

		this.pixels.forEach((pixel, i, arr) => {
			bit = ((byte & (1 << (7 - i))) > 0) === true ? wpi.HIGH : wpi.LOW;

			wpi.digitalWrite(this.pinDAT, bit);
			wpi.digitalWrite(this.pinCLK, 1);
			wpi.digitalWrite(this.pinCLK, 0);
		});
	}

	setPixel(i, r, g, b, a) {
		if (typeof i === 'number' && i >= 0 && i < this.pixelCount) {
			if (this.format === 'HSL') { [r,g,b] = convert.hsl2rgb(r, g, b); }
			if (this.format === 'HSV') { [r,g,b] = convert.hsv2rgb(r, g, b); }
			if (a === undefined) { a = this.brightness; }

			this.pixels[i] = [
				parseInt(r, 10) & 255,
				parseInt(g, 10) & 255,
				parseInt(b, 10) & 255,
				parseInt((31.0 * a), 10) & 0b11111
			];
		}
	}

	setAll(r, g, b, a) {
		this.pixels.forEach((pixel, i, arr) => {
			this.setPixel(i, r, g, b, a);
		});
	}

	rotateLeft() {
		this.pixels.push(this.pixels.shift());
	}

	rotateRight() {
		this.pixels.unshift(this.pixels.pop());
	}

	off() {
		this.setAll(0,0,0,0);
		this.draw();
	}

	draw() {
		this._clocker(32);

		this.pixels.forEach((pixel, i, arr) => {
			this._writeByte(0b11100000 | pixel[3]); // Brightness
			this._writeByte(pixel[2]); // Blue
			this._writeByte(pixel[1]); // Green
			this._writeByte(pixel[0]); // Red
		});

		this._clocker(36);
	}
}

module.exports = Blinkt;