#!/usr/bin/env python

import colorsys
import math
import time

import pantilthat


pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)

while True:
    t = time.time()
    b = (math.sin(t * 2) + 1) / 2
    b = int(b * 255.0)
    t = round(time.time() * 1000) / 1000
    a = round(math.sin(t) * 90)
    pantilthat.pan(int(a))
    pantilthat.tilt(int(a))
    r, g, b = [int(x*255) for x in  colorsys.hsv_to_rgb(((t*100) % 360) / 360.0, 1.0, 1.0)]
    pantilthat.set_all(r, g, b)
    pantilthat.show()
    print(a)
    time.sleep(0.04)
