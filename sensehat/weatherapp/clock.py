#!/usr/bin/env python

from sense_hat import SenseHat
import time

sense = SenseHat()

number = [
0,1,1,1, #zero
0,1,0,1,
0,1,0,1,
0,1,1,1,
0,0,1,0, #one
0,1,1,0,
0,0,1,0,
0,1,1,1,
0,1,1,1, #two
0,0,1,1,
0,1,1,0,
0,1,1,1,
0,1,1,1, #three
0,0,1,1,
0,0,1,1,
0,1,1,1,
0,1,0,1, #four
0,1,1,1,
0,0,0,1,
0,0,0,1,
0,1,1,1, #five
0,1,1,0,
0,0,1,1,
0,1,1,1,
0,1,0,0, #six
0,1,1,1,
0,1,0,1,
0,1,1,1,
0,1,1,1, #seven
0,0,0,1,
0,0,1,0,
0,1,0,0,
0,1,1,1, #eight
0,1,1,1,
0,1,1,1,
0,1,1,1,
0,1,1,1, #nine
0,1,0,1,
0,1,1,1,
0,0,0,1
]

hourColour   = [255,0,0] # red
minuteColour = [0,255,255] # cyan
empty        = [0,0,0] # off / black

clockImage = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]

hour = time.localtime().tm_hour
minute = time.localtime().tm_min

# Map digits to clockImage array

pixelOffset = 0
index = 0
for indexLoop in range(0, 4):
	for counterLoop in range(0, 4):
		if (hour >= 10):
			clockImage[index] = number[int(hour/10)*16+pixelOffset]
		clockImage[index+4] = number[int(hour%10)*16+pixelOffset]
		clockImage[index+32] = number[int(minute/10)*16+pixelOffset]
		clockImage[index+36] = number[int(minute%10)*16+pixelOffset]
		pixelOffset = pixelOffset + 1
		index = index + 1
	index = index + 4

# Colour the hours and minutes

for index in range(0, 64):
	if (clockImage[index]):
		if index < 32:
			clockImage[index] = hourColour
		else:
			clockImage[index] = minuteColour
	else:
		clockImage[index] = empty

# Display the time

sense.set_rotation(90) # Optional
sense.low_light = True # Optional
sense.set_pixels(clockImage)
