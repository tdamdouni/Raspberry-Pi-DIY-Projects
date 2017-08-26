#!/usr/bin/env python
#Original code by jon-root, updated to run on scroll-phat-hd by alexmburns.

# simple binary clock
# bcd for hours, minutes and seconds
# chart for time past the hour (one light per whole ten minutes)
# please see disclaimer at bottom of file

import sys
import time

import scrollphathd

scrollphathd.set_brightness(0.5)

def string_to_bcd(digit):

    bcd_digit = bin(int(digit))[2:]
    return ('00000' + bcd_digit)[-5:]


def plot_digit(digit, position):

    bcd_digit = string_to_bcd(digit)
    for y in range(0, 5, 1):
        scrollphathd.set_pixel(position, y, int(bcd_digit[y]) == 1)

while True:
    try:
        current = time.strftime('%H0%M0%S')
        for x in range(0, 8):
            plot_digit(current[x], x)
        for i in range(0, 5):
            scrollphathd.set_pixel(10, i, (5 - i) <= ((int(current[3:5])) / 10))
	scrollphathd.show()
        time.sleep(0.5)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)

