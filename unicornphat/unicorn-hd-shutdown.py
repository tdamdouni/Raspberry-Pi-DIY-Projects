#!/usr/bin/env python

# #!/usr/bin/env python

import colorsys
import math
import time
import signal
import sys

import unicornhat as unicorn

def Shutdown(Code, Frame):
    unicorn.off()
    sys.exit(0)

signal.signal(signal.SIGTERM, Shutdown)

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

i = 0.0
offset = 30
try:
	while True:
		i = i + 0.3
		for y in range(height):
			for x in range(width):
				r = 0#x * 32
				g = 0#y * 32
				xy = x + y / 4
				r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
				g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
				b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
				r = max(0, min(255, r + offset))
				g = max(0, min(255, g + offset))
				b = max(0, min(255, b + offset))
				unicorn.set_pixel(x,y,int(r),int(g),int(b))
		unicorn.show()
		time.sleep(0.01)
except KeyboardInterrupt:
	unicorn.off()

import colorsys
import math
import time
import signal
import sys

import unicornhat as unicorn

def Shutdown(Code, Frame):
    unicorn.off()
    sys.exit(0)

signal.signal(signal.SIGTERM, Shutdown)

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

i = 0.0
offset = 30
try:
	while True:
		i = i + 0.3
		for y in range(height):
			for x in range(width):
				r = 0#x * 32
				g = 0#y * 32
				xy = x + y / 4
				r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
				g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
				b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
				r = max(0, min(255, r + offset))
				g = max(0, min(255, g + offset))
				b = max(0, min(255, b + offset))
				unicorn.set_pixel(x,y,int(r),int(g),int(b))
		unicorn.show()
		time.sleep(0.01)
except KeyboardInterrupt:
	unicorn.off()