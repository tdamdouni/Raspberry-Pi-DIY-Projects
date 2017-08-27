#!/usr/bin/env python

# http://forums.pimoroni.com/t/blinkt-retropie-auto-stop-script-help/4450

import colorsys
import time

from blinkt import set_clear_on_exit, set_brightness, set_pixel, show

import signal
import sys

# This catches the SIGINT signal which is sent by kill and cleans up the Blinkt!. In theory anyway!
def signal_handler(signal, frame):
    blinkt.clear()
    blinkt.show()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

spacing = 360.0 / 16.0
hue = 0

set_clear_on_exit()
set_brightness(0.1)

while True:
    hue = int(time.time() * 100) % 360
    for x in range(8):
        offset = x * spacing
h        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        set_pixel(x,r,g,b)
    show()
    time.sleep(0.001)