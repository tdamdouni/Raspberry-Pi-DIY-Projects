#!/usr/bin/env python

import colorsys
import math
import time

import pantilthat


pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)

r, g, b, w = 0, 0, 0, 50

while True:
    for x in range(18):
        pantilthat.set_pixel(x, r, g, b, w)

    pantilthat.show()

    p = int(math.sin(time.time()) * 90)
    t = int(math.sin(time.time()) * 90)

    pantilthat.pan(p)
    pantilthat.tilt(t)
