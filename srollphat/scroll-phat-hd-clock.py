#!/usr/bin/env python

# http://forums.pimoroni.com/t/keeping-an-eye-on-a-website-with-rpi0-and-scroll-phat-hd/4487

import os
import time
import signal
import math
import scrollphathd
from scrollphathd.fonts import font3x5

def warning():
        speed_factor = 10
        scale = (math.sin(time.time() * speed_factor) + 1) / 2
        offset = 0
        for x in range(scrollphathd.width):
            for y in range(scrollphathd.height):
                offset += 1
                color = 0.85 * scale * (offset % 2)
                scrollphathd.pixel(x, y, color)
        scrollphathd.show()

def clock():
        scrollphathd.rotate(180)
        scrollphathd.clear()
        str1 = time.strftime("%H%M") 
        scrollphathd.write_string(str1, x=1, y=1, font=font3x5, brightness=0.01)
        scrollphathd.show()
        time.sleep(0.1)

while True:
        web = os.popen("curl -s https://example.com | grep .css").read()
        t_end = time.time() + 60 * 1
        if "hot.css" in web:
                while time.time() < t_end:
                        warning()
        else:
                while time.time() < t_end:
                        clock()