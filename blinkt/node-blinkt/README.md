    888888b.   888 d8b          888      888    888
    888  "88b  888 Y8P          888      888    888
    888  .88P  888              888      888    888
    8888888K.  888 888 88888b.  888  888 888888 888
    888  "Y88b 888 888 888 "88b 888 .88P 888    888
    888    888 888 888 888  888 888888K  888    Y8P
    888   d88P 888 888 888  888 888 "88b Y88b.   "
    8888888P"  888 888 888  888 888  888  "Y888 888

[Blinkt](https://github.com/NotNinja/node-blinkt) is Node.js library that allows you to interact with your Blinkt
hardware:

https://shop.pimoroni.com/products/blinkt

[![Dependency Status](https://img.shields.io/david/NotNinja/node-blinkt.svg?style=flat-square)](https://david-dm.org/NotNinja/node-blinkt)
[![License](https://img.shields.io/npm/l/blinkt.svg?style=flat-square)](https://github.com/NotNinja/blinkt/blob/master/LICENSE.md)
[![Release](https://img.shields.io/npm/v/blinkt.svg?style=flat-square)](https://www.npmjs.com/package/blinkt)

* [Install](#install)
* [API](#api)
* [Bugs](#bugs)
* [Contributors](#contributors)
* [License](#license)

## Install

Install using `npm`:

``` bash
$ npm install --save blinkt
```

## API

### Set A Single Pixel

The bread and butter of Blintk! is setting pixels. You can set any of the 8 pixels on your Blinkt! to one of around 16
million colors!

The `brightness` argument is completely optional. Omit it to keep the last brightness value set for that particular
pixel.

``` javascript
blinkt.setPixel(index, red, green, blue, brightness)
```

| Parameter  | Description                                                        | Required |
| ---------- | ------------------------------------------------------------------ | -------- |
| index      | The horizontal position of the pixel (between 0 and 7 - inclusive) | Yes      |
| red        | The amount of red to be set (between 0 and 255 - inclusive)        | Yes      |
| green      | The amount of green to be set (between 0 and 255 - inclusive)      | Yes      |
| blue       | The amount of blue to be set (between 0 and 255 - inclusive)       | Yes      |
| brightness | The brightness to be set (between 0 and 1 - inclusive)             | No       |

### Set All Pixels

Sometimes you need to set all the pixels to the same color. This convenience method does just that!

The `brightness` argument is completely optional. Omit it to keep the last brightness values set for each pixel.

``` javascript
blinkt.setPixels(red, green, blue, brightness)
```

| Parameter  | Description                                                   | Required |
| ---------- | ------------------------------------------------------------- | -------- |
| red        | The amount of red to be set (between 0 and 255 - inclusive)   | Yes      |
| green      | The amount of green to be set (between 0 and 255 - inclusive) | Yes      |
| blue       | The amount of blue to be set (between 0 and 255 - inclusive)  | Yes      |
| brightness | The brightness to be set (between 0 and 1 - inclusive)        | No       |

### Show

None of your pixels will appear on Blinkt! until you `show()` them. This method writes all the pixel data out to your
device.

``` javascript
blinkt.show()
```

### Clear

Exactly the same as calling `setAll(0,0,0)`, clear sets all the pixels to black.

You must also call `show()` if you want to turn Blinkt! off.

``` javascript
blinkt.clear()
```

### Enable/Disable Clear On Exit

Sometimes you want a script that runs and quits, leaving a pattern up on Blinkt!

``` javascript
blinkt.setClearOnExit(value)
```

| Parameter | Description                                       | Required |
| --------- | ------------------------------------------------- | -------- |
| value     | `true` to clear pixels on exit; otherwise `false` | No       |

### Get A Single Pixel

Returns the colors and brightness for a particular pixel.

``` javascript
blinkt.getPixel(index)
```

| Parameter | Description                                                        | Required |
| --------- | ------------------------------------------------------------------ | -------- |
| index     | The horizontal position of the pixel (between 0 and 7 - inclusive) | Yes      |

### Constants

Blinkt! has 8 pixels. Simple. Use the constant `NUM_PIXELS` when you’re iterating over pixels, so you can avoid a *magic
number* in your code.

``` javascript
blinkt.NUM_PIXELS
```

## Bugs

If you have any problems with using this library or would like to see changes currently in development you can do so
[here](https://github.com/NotNinja/node-blinkt/issues).

If you believe that you are experiencing issues with your Blinkt hardware, then you
[get help](http://forums.pimoroni.com/c/support).

## Contributors

If you want to contribute, you're a legend! Information on how you can do so can be found in
[CONTRIBUTING.md](https://github.com/NotNinja/node-blinkt/blob/master/CONTRIBUTING.md). We want your suggestions and
pull requests!

A list of Blinkt contributors can be found in
[AUTHORS.md](https://github.com/NotNinja/node-blinkt/blob/master/AUTHORS.md).

## License

See [LICENSE.md](https://github.com/NotNinja/node-blinkt/raw/master/LICENSE.md) for more information on our MIT license.

[![Copyright !ninja](https://cdn.rawgit.com/NotNinja/branding/master/assets/copyright/base/not-ninja-copyright-186x25.png)](https://not.ninja)
