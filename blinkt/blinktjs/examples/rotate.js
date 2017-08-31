const Blinkt = require('../src/index.js');
const blinkt = new Blinkt({defaultBrightness: 0.2});

let timer;

setTimeout(() => {
	blinkt.setAll(255, 0, 0);
	blinkt.draw();
	console.log('red');
}, 10);

setTimeout(() => {
	blinkt.setPixel(3, 200, 255, 0);
	blinkt.draw();
	console.log('yellow dot');

	timer = setInterval(() => {
		blinkt.rotateLeft();
		blinkt.draw();
	}, 100);
}, 1000);

setTimeout(() => {
	clearInterval(timer);
	console.log('end');
}, 5000);