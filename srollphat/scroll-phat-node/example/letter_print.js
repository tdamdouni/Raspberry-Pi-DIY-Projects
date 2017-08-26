var async = require('async');

var scroll = require('../src/scroll');
var scroller = new scroll();
scroller.initialize(function(openErr) {
	if(openErr) {
		return console.error("Can't open i2c.");
	}

	var letterBuffer = ["S", "C", "R", "O", "L", "L", "."];
	scroller.setBrightness(3, function () {
		var interval = setInterval(function() {
			if(!letterBuffer.length) {
				return clearInterval(interval);
			}
			scroller.clearPixels();
			scroller.refresh();
			scroller.setText(letterBuffer[0]);
			scroller.refresh();
			letterBuffer=letterBuffer.slice(1);
		}, 500);

	});
});