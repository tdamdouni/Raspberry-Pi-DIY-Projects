#!/usr/bin/env python

import time
import math
import ast

import scrollphathd

# Open and read the array file
fh = open( "candle_example.js", "r" )
x = fh.read()
fh.close()

# Evaluate the string as an array
y = ast.literal_eval(x)

# Break the contained newlines into separate array components
list = []
for s in y:
	list.append(s.splitlines())

# Function that returns the brightness value nnn as a float, from the array at position i,j, for frame "step" 
def candle(i , j, step):
    r = float(list[step][i][j*3:j*3+3])
    return r

# Set maximal brightness of LED Matrix
scrollphathd.set_brightness(0.5)

# Start rendering loop
timestep = 0
while True:
    if timestep == 332: # the file has 333 frames
      timestep = 0
 
    timestep = timestep + 1
	
    # Render each pixel column by column based on array contents
    for x in range(0, scrollphathd.DISPLAY_WIDTH):
        for y in range(0, scrollphathd.DISPLAY_HEIGHT):
            v = candle(x, y, timestep)
            scrollphathd.pixel(x, y, max(0,v/255))

    # Wait a little before the next frame		
    time.sleep(0.001)
	
    # Show the frame buffer	
    scrollphathd.show()

