#!/usr/bin/env python
#Original code by alexellis, updated to run on scroll-phat-hd by alexmburns.

#To execute script type python count.py [5]... excluding brackets... any number will work.

import sys
import time

import scrollphathd

if(len(sys.argv) == 1):
    print("Type a number in under 999 as an argument.")
    sys.exit(-1)
val = int(sys.argv[1])

if(val > 999):
    print("Number must be under 999 to fit on screen")
    sys.exit(-1)

scrollphathd.set_brightness(0.5)

for x in range(1, val+1):
    try:
        scrollphathd.write_string(str(x))
	scrollphathd.show()
	scrollphathd.clear()
        time.sleep(1.00)
    except KeyboardInterrupt:
        scrollphathd.clear()
        sys.exit(-1)
