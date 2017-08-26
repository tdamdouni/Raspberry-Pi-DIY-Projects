#!/usr/bin/env python
#Original code by alexellis, updated to run on scroll-phat-hd by alexmburns.

import math
import sys
import time

import scrollphathd


i = 0
buf = [0] * 17
scrollphathd.set_brightness(0.5)

while True:
    try:
        for x in range(0, 17):
            y = (math.sin((i + (x * 10)) / 10.0) + 1) # Produces range from 0 to 2
            y *= 2.5 # Scale to 0 to 5
            buf[x] = 1 << int(y)

        scrollphathd.write_string(buf)
        scrollphathd.show()
	scrollphathd.scroll()
	scrollphathd.clear()
        time.sleep(0.005)

        i += 1
    except KeyboardInterrupt:
        scrollphathd.clear()
        sys.exit(-1)
