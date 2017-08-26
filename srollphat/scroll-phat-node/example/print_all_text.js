var scroll = require('../src/scroll');

var text = "OMG";
if(process.argv.length > 2) {
	text = process.argv.slice(2).join(" ");
}

var scroller = new scroll();
scroller.initialize(function(openErr) {
	if(openErr) {
		return console.error("Can't open i2c.");
	}

	scroller.setBrightness(3, function () {
		scroller.clearPixels();
		scroller.refresh();
		setTimeout(function() {

			scroller.setText(text);
			scroller.refresh();
		}, 300);

	});
});
