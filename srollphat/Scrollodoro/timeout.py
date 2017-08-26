#!/usr/bin/env python

# Pomodoro timeout countdown timer for Raspberry Pi and Pimoroni Scroll pHAT
# Counts down over 5 minutes, then flashes
# Usage: ./timeout.py [# minutes]

import sys
import time
import scrollphat

minutes = 5

if len(sys.argv) > 1:
    minutes = (int)(sys.argv[1])

# print "Timing " + (str)minutes + " minutes"

def flash():
    scrollphat.set_pixels(lambda x, y: 1, True)
    time.sleep(0.1)
    scrollphat.clear()
    time.sleep(0.1)

total_time = (minutes * 60)
popov = total_time / 5.0

start = time.time()

scrollphat.clear()
scrollphat.set_rotate(True)
scrollphat.set_brightness(1)

blinkstate = False
elapsed = 0

while total_time > elapsed:
    try:
	elapsed = time.time() - start
	# print elapsed

	blinkstate = not blinkstate
	blinker_line = (int)(elapsed / popov)
	# print blinker_line
        scrollphat.clear_buffer()

	for x in range(0, 11, 1):
	    for y in range(0, 11, 1):
		loc_line = ((y * 11) + x)/11
                if loc_line == blinker_line:
                    scrollphat.set_pixel(x, y, blinkstate)
                if loc_line > blinker_line:
                    scrollphat.set_pixel(x, y, True)

	scrollphat.update()

        time.sleep(0.5)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)

scrollphat.set_brightness(50)

for t in range(0, 3, 1):
    for s in range(0, 5, 1):
        flash()
    time.sleep(0.5)

scrollphat.clear()
