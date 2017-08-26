# scroll-phat-node
Work-in-progress node.js library for Pimorani's scrollPhat. Partial re-write in Node with some re-use of Python library.

Features:

```
[x] Set brightness
[x] Set mode 5x11
[x] Set pixels on/off
[x] Load font into bitmaps
[x] Print single character onto screen
[x] Print multiple characters onto screen
```

Todo:

> These remaining items will probably not be finished since animations and timing in asynchronous JavaScript are necessarily hard and complex. 

```
[ ] Scroll text across screen
[ ] Flip output of screen i.e. upside down.
[ ] Scroll-phat HD support
```

### Installation:

#### Required:
* Node.js v4.2.3
* Raspberry PI or device with I2c support
* I2c correctly set up and functioning

Install node.js via [binary distribution](https://nodejs.org/en/download/), apt-get/pacman or nvm etc. This has been developed/tested on Arch Linux but will also work on other distributions.
The i2c-bus library will also require a full make/gcc tool-chain to be installed.

Use Node's `npm` package manager to install dependencies:

```
npm install
```

#### Demos

* node scroll_test.js
* node app.js

#### Use in your code

The library aims to be largely compatible with the original Python version, but Node.js is an asynchronous environment, meaning you can quickly get into a deep callback chain. I would suggest looking into the `async` library control-flow or a *Promise* library. 

```
var scrollPhat = require('scroll-phat-node');

var scroller = new scroll();
scroller.initialize(function(openErr) {
	if(openErr) {
		return console.error("Can't open i2c.");
	}

	var brightness = 3;
	scroller.setBrightness(brightness, function () {
		scroller.clearPixels();
		scroller.setPixel(1, 1, true);
		scroller.setPixel(1, 2, true);
		scroller.setPixel(1, 3, true);
		scroller.setPixel(1, 4, true);
		scroller.setPixel(1, 5, true);

		scroller.refresh(function () {
			setTimeout(function() {
				scroller.clearPixels();
				scroller.refresh(function () {
					scroller.close();
				});
			}, 1000);
		});
	});
});
```

### Details

Each of the 11 columns can be written to with binary value between 0 and 31, where 0 is off and 31 is fully on. If you need several pixels to be on at once then you need to work out what this would look like in binary. *I.e. top and bottom = 10001 = 17*

