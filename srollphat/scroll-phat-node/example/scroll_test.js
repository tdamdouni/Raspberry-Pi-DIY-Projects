var scroll = require('../src/scroll');

var scroller = new scroll();
scroller.initialize(function(openErr) {
	if(openErr) {
		return console.error("Can't open i2c.");
	}

	scroller.setBrightness(3, function () {
		var x = 0;
		var interval = setInterval(function() {
			console.log("Row: " +x);
			
			for(var i = 0; i < 11; i++) {
				scroller.setPixel(i, x, true);
			}
			scroller.refresh(function done () {

			});

			x++;
			if(x >= 5) {
				scroller.clearPixels();
				scroller.refresh(function () {
					scroller.close();
					clearTimeout(interval);
				});

			} 
		}, 1500); 
	});
});
