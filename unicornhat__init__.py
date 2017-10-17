#!/usr/bin/env python

# NOTE! This file replaces __init__.py in the Unicorn HAT HD library and allows it to drive two displays side-by-side,
# in this configuration: https://twitter.com/Gadgetoid/status/883259931478155264

# Both HATs are connected to Mini Black HAT Hack3r boards- the right board is connected directly to the Pi, and the left
# board is wired to the GPIO outputs of the right using the standard UHHD pinout: https://pinout.xyz/pinout/unicorn_hat_hd

# MISO is not needed, and the chip-select pin is jumped from BCM7 on the right header to BCM8 on the left.

# Rotation is *NOT* supported but it's possible to implement 0 and 180 degree options.
# It would be possible to re-implement 90 degree rotation support for 2:2 ratios using 4, 9 or 16 HATs.

import colorsys
import time

try:
    import spidev
except ImportError:
    sys.exit("This library requires the spidev module\nInstall with: sudo pip install spidev")

try:
    import numpy
except ImportError:
    exit("This library requires the numpy module\nInstall with: sudo pip install numpy")


__version__ = '0.0.2'

_spi = spidev.SpiDev()
_spi.open(0, 0)
_spi.max_speed_hz = 9000000

_spi2 = spidev.SpiDev()
_spi2.open(0, 1)
_spi2.max_speed_hz = 9000000

_SOF = 0x72
_DELAY = 1.0/120

WIDTH = 32
HEIGHT = 16

PHAT = None
HAT = None
PHAT_VERTICAL = None
AUTO = None

_rotation = 0
_brightness = 0.5
_buf = numpy.zeros((WIDTH,HEIGHT,3), dtype=int)

def brightness(b):
    """Set the display brightness between 0.0 and 1.0.

    :param b: Brightness from 0.0 to 1.0 (default 0.5)

    """

    global _brightness

    _brightness = b

def rotation(r):
    """Set the display rotation in degrees.

    Actual rotation will be snapped to the nearest 90 degrees.

    """
    global _rotation

    _rotation = int(round(r/90.0))

def get_rotation():
    """Returns the display rotation in degrees."""
    return _rotation * 90

def set_layout(pixel_map=None):
    """Does nothing, for library compatibility with Unicorn HAT."""
    pass

def set_all(r, g, b):
    _buf[:] = r, g, b

def set_pixel(x, y, r, g, b):
    """Set a single pixel to RGB colour.

    :param x: Horizontal position from 0 to 15
    :param y: Veritcal position from 0 to 15
    :param r: Amount of red from 0 to 255
    :param g: Amount of green from 0 to 255
    :param b: Amount of blue from 0 to 255

    """
    _buf[x][y] = r, g, b

def set_pixel_hsv(x, y, h, s=1.0, v=1.0):
    """set a single pixel to a colour using HSV.

     :param x: Horizontal position from 0 to 15
     :param y: Veritcal position from 0 to 15
     :param h: Hue from 0.0 to 1.0 ( IE: degrees around hue wheel/360.0 )
     :param s: Saturation from 0.0 to 1.0
     :param v: Value (also known as brightness) from 0.0 to 1.0

    """

    r, g, b = [int(n*255) for n in colorsys.hsv_to_rgb(h, s, v)]
    set_pixel(x, y, r, g, b)

def get_pixel(x, y):
    return tuple(_buf[x][y])

def shade_pixels(shader):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            r, g, b = shader(x, y)
            set_pixel(x, y, r, g, b)

def get_pixels():
    return _buf

def get_shape():
    """Return the shape (width, height) of the display."""

    return WIDTH, HEIGHT

def clear():
    """Clear the buffer."""
    _buf.fill(0)

def off():
    """Clear the buffer and immediately update Unicorn HAT HD.

    Turns off all pixels.

    """
    clear()
    show()

def show():
    """Output the contents of the buffer to Unicorn HAT HD."""
    _buf1 = numpy.rot90(_buf[:WIDTH/2,:HEIGHT],1)
    _buf2 = numpy.rot90(_buf[WIDTH/2:WIDTH,:HEIGHT],1)
    _spi.xfer2([_SOF] + (_buf1.reshape(768) * _brightness).astype(numpy.uint8).tolist())
    _spi2.xfer2([_SOF] + (_buf2.reshape(768) * _brightness).astype(numpy.uint8).tolist())
    time.sleep(_DELAY)