var scroll = require('./scroll');

var scroller = new scroll();
scroller.initialize(function(openErr) {
	if(openErr) {
		return console.error("Can't open i2c.");
	}

	scroller.setBrightness(3, function () {
		scroller.clearPixels();
		scroller.setPixel(1,2,true);
		scroller.refresh();
	});
});
