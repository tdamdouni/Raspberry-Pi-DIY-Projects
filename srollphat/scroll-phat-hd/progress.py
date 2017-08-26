#!/usr/bin/env python
#Original code by alexellis, updated to run on scroll-phat-hd by alexmburns.

import math
import sys
import time

import scrollphathd


def millis():
    return int(round(time.time() * 1000))

scrollphathd.set_brightness(0.5)

def clear(pause):
    for y in range(7):
        for x in range(17):
            scrollphathd.set_pixel(x,y,0)
            scrollphathd.show()
            time.sleep(pause)

def paint(pause):
    for y in range(7):
        for x in range(17):
            scrollphathd.set_pixel(x,y,1)
            scrollphathd.show()
            time.sleep(pause)

while(True):
    try:
        pause_time = 0.06
        paint(pause_time)
        clear(pause_time)
    except KeyboardInterrupt:
        scrollphathd.clear()
        sys.exit(-1)
