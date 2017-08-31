# node-blinkt
A Node.js Library to Interact with [Blinkt](https://shop.pimoroni.com/products/blinkt)

# Install

```bash
npm install node-blinkt
```

# Usage

```js
var Blinkt = require('./Blinkt'),
	leds = new Blinkt();

leds.setup();
leds.clearAll();
leds.setAllPixels(0, 156, 0, 0.1);
leds.sendUpdate();
```

# Methods

## setup()
Connects to the GPIO and sets the GPIO pin modes. Must be called before any other commands.

## clearAll()
Sets all pixels to white.

## setPixel(pixelNum, red, green, blue, brightness)
Sets the specififed pixel to the passed rgb and brightness level. The pixelNum is
an integer between 0 and 7 to indicate the pixel to change.

## setBrightness(pixelNum, brightness)
Sets the brightness level between 0.0 (off) and 1.0 (full brightness) for the specified pixelNum.
The pixelNum is an integer between 0 and 7 to indicate the pixel to change.

## setAllPixels(red, green, blue, brightness)
Sets all pixels to the passed rgb and brightness level.

## sendUpdate()
This method is the most important. You can set pixels colours as much as you want but they
will not update until you call this method.

# Copyright and License
All works are copyright Irrelon Software Limited. You may use this project under any open-source
license that you wish e.g. (MIT, GPL etc).