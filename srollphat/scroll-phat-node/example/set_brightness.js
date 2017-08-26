var i2c = require('i2c-bus')

var i2c1 = i2c.openSync(1);

var i2c_address = 0x60;
var cmd_set_mode = 0x00;
var cmd_set_brightness = 0x19;
var cmd_set_pixels = 0x01;

var mode_5x11 = "00000011";

var max_brightness = 8;
var brightness = 0;
i2c1.writeByteSync(i2c_address, cmd_set_brightness, brightness);


i2c1.writeByteSync(i2c_address, cmd_set_brightness, parseInt(mode_5x11, 2));

var buffer = 2;
i2c1.writeByteSync(i2c_address, cmd_set_pixels, buffer);


var intv = setInterval(function() {
  i2c1.writeByteSync(i2c_address, cmd_set_brightness, brightness++);
  if(brightness >= max_brightness) {
     i2c1.closeSync();
     clearTimeout(intv)
  }
}, 200);

