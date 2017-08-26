#!/usr/bin/env python
import time
import sys

import scrollphathd
from scrollphathd.fonts import font5x7

scrollphathd.rotate(180)

if len(sys.argv) != 2:
    print("\nusage: python echo.py \"message\" \npress CTRL-C to exit\n")
    sys.exit(0)

string = sys.argv[1]
length = len(string)
width = 17
buffer = (length * 6) + width

#snip

string = sys.argv[1] + '      '
buffer = scrollphathd.write_string(string, x=17, y=0, font=font5x7, brightness=0.5)

for i in range(buffer):
    scrollphathd.show()
    scrollphathd.scroll(1)
    time.sleep(0.05)
    
scrollphathd.write_string(string + "      ", x=width, y=0, font=font5x7, brightness=0.5)

for i in range(buffer):
    scrollphathd.show()
    scrollphathd.scroll(1)
    time.sleep(0.05)