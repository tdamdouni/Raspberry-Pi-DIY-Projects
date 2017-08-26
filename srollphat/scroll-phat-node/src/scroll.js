var i2c = require('i2c-bus');
var fs = require('fs');
var path = require('path');

var i2c_address = 0x60;
var cmd_set_mode = 0x00;
var cmd_set_brightness = 0x19;
var cmd_set_pixels = 0x01;
var mode_5x11 = "00000011";
var total_lines = 11;
var line_length = 5;

// Terminate the block with 0xff.
var end_marker = 255;

function scroll() {
	this.buffer = new Uint8Array(total_lines + 1);
	for(var n = 0;n<total_lines; n++) {
		this.buffer[n] = 0;
	}
	this.buffer[this.buffer.length] = end_marker;
	this.font = {};
}

scroll.prototype.initialize = function(done) {
	var that = this;
	fs.readFile(path.join(__dirname, './font.json'), 'utf8', function(err, text) {
		if(err) { 
			return done(err);
		}

		that.font = JSON.parse(text);

		that.wire = i2c.open(1, function(err) {
			that.wire.writeByte(i2c_address, cmd_set_mode, parseInt(mode_5x11, 2), function(){
				done(err);
			});
		});
	});
};

scroll.prototype.setBrightness=function(val, done) {
	var that = this;

	that.wire.writeByte(i2c_address, cmd_set_brightness, Number(val), function(err) {
		done(err);
	});
};

scroll.prototype.refresh = function(done) {
	var that = this;

	var buffer = that.buffer;
//	console.log(buffer)
	var callback = done ? done : that.refreshDone;

	that.wire.writeI2cBlock(i2c_address, cmd_set_pixels, buffer.length, buffer, callback);
};

scroll.prototype.refreshDone = function() {

}

scroll.prototype.clearPixels = function() {
	var that = this;
	for (var i = 0; i < this.buffer.length; i++) {
		this.buffer[i] = 0;
	};
};

var toAsciiCode = function(character) {
   return character.toCharCode(0);
}


scroll.prototype.setText = function(text) {
    var that = this;

	var columnOffset=0;

    for(var i = 0; i < text.length; i++) {
       var ascii = text.charCodeAt(i);
       console.log("Printing " + ascii);

       var ch = that.font[ascii];
       for(var j=0;j<ch.length;j++) {
//	       	console.log((columnOffset+j)+ "x"+ch[j] +" on");
	        this.setPixels(columnOffset, ch[j], true);
	        columnOffset++;
       }
       columnOffset++;
    }
}; 

scroll.prototype.setPixels = function(x, total, value) {
	var that = this;
	that.setColumn(x, total, value);
};

scroll.prototype.setPixel = function(x, y, value) {
	var that = this;
	if(value) {
 	   that.buffer[x] |= (1 << y)
	} else {
 	   that.buffer[x] &= ~(1 << y)
	}
};

scroll.prototype.setColumn = function(x, y, value) {
	var that = this;
	that.buffer[x] =y
};

scroll.prototype.close = function() {
	var that = this;
	that.wire.closeSync();
};

module.exports = scroll;
