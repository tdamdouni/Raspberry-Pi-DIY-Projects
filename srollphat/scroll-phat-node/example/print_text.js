var scroll = require('../src/scroll');

var scroller = new scroll();
scroller.initialize(function(openErr) {
	if(openErr) {
		return console.error("Can't open i2c.", openErr);
	}

	scroller.setBrightness(3, function () {
		scroller.refresh();
		scroller.setText("O");
		scroller.refresh();
		setTimeout(function() {
			scroller.clearPixels();
			scroller.refresh();
			scroller.setText("M");
			scroller.refresh();
			setTimeout(function() {
				scroller.clearPixels();
				scroller.refresh();
				scroller.setText("G");
				scroller.refresh();
				setTimeout(function() {
					scroller.clearPixels();
					scroller.refresh();
					scroller.setText("!");
					scroller.refresh();
				}, 1500);

			}, 1500);

		}, 1500);
	});
});
