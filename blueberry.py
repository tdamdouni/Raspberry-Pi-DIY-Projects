#!/usr/bin/env python

import math
import time

import unicornhat as unicorn


unicorn.set_layout(unicorn.PHAT)
unicorn.rotation(0)
unicorn.brightness(0.3)
width, height = unicorn.get_shape()


for x in range(width):
    for y in range(height):
        unicorn.set_pixel(x, y, 49, 125, 212)
    unicorn.show()
    time.sleep(0.12)

time.sleep(0.8)

for x in range(width):
    for y in range(height):
        unicorn.set_pixel(x, y, 49, 212, 71)

unicorn.show()
time.sleep(0.5)
