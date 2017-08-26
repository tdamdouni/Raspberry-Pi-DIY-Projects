#!/usr/bin/env python

import colorsys
import phatbeat
import time


print("""
pHAT BEAT: Rainbow

Displays a glorious rainbow on pHAT BEAT!

Press Ctrl+C to exit!

""")



SPEED = 50
BRIGHTNESS = 64
SPREAD = 20

while True:
    for x in range(phatbeat.CHANNEL_PIXELS):
        h = (time.time() * SPEED + (x * SPREAD)) % 360 / 360.0
        r, g, b = [int(c*BRIGHTNESS) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        phatbeat.set_pixel(x, r, g, b, channel=0)
        phatbeat.set_pixel(x, r, g, b, channel=1)

    phatbeat.show()
    time.sleep(0.001)
