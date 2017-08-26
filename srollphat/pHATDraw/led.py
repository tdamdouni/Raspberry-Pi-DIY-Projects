#!/usr/bin/env python

import sys
import json
import time

import scrollphat

if len(sys.argv) != 3:
	print("\nProblem")
	sys.exit(0)

data = json.loads(sys.argv[1])
brightness = int(sys.argv[2])

scrollphat.set_brightness(brightness)
for d in data:
	print data[d]
	scrollphat.set_pixel(data[d][0], data[d][1], True)

scrollphat.update()

sys.exit(0)

