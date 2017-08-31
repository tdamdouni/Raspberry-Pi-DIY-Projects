Blinkt! class (ES6) for node.js

Control your Pimoroni Blinkt! in javascript. 8 APA102 LEDs for your Raspberry Pi https://shop.pimoroni.com/products/blinkt. Original python libraries available https://github.com/pimoroni/blinkt.

## Usage

Set the pixels with `setPixel()` or `setAll()` and call `draw()` to write the pixels to the device.

* `setPixel(0, 255, 255, 255, 0.5);` - setPixel takes the pixel number (0-7), rgb values and optionally brightness
* `setAll(255,255,255, 0.3)` - sets all pixels to a color, with an optional brightness value
* `off()` - turn off all lights. This calls `draw()` internally, as it's meant to be a single call to turn everything off.
* `rotateLeft()` - shift leds to the left
* `rotateRight()` - shift leds to the right
* `draw()` - always call draw to write the pixel data to blinkt

Additionally, there are some startup options

* defaultBrightness - the brightness value to use if none provided. 0.5 by default.
* CLK - clock pin, 24 by default
* DAT - data pin, 23 by default
* pixelCount - number of pixels, 8 by default
* colorFormat - `'RGB'` by default, you can also use `'HSL'` and `'HSV'`. HSL works, but isn't connected to led brightness, so not completely usable.
* clearOnExit - whether to call `off()` when the process exits. `true` by default.

## Examples

```
const Blinkt = require('blinktjs');
const blinkt = new Blinkt({defaultBrightness: 0.2});

blinkt.setAll(255, 0, 0);
blinkt.draw();
```

See the examples folder for a few basic examples.
