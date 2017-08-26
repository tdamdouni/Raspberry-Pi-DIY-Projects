#!/usr/bin/env python

# Script is unchanged from Pimoroni's advancedscrolling.py example, apart from the data import/parsing.

import time
import scrollphathd
import urllib2
import json
from scrollphathd.fonts import font5x7

print("""
every thing every tiny
""")

# Uncomment to rotate 180 degrees
scrollphathd.rotate(180)

# Dial down the brightness
scrollphathd.set_brightness(0.2)

# If rewind is True the scroll effect will rapidly rewind after the last line
rewind = False

# Delay is the time (in seconds) between each pixel scrolled
delay = 0.02

# Add a data source
url = 'https://everythingeverytime.herokuapp.com/poem'

def refreshPoem():
    httpreq = urllib2.urlopen(url)
    response = httpreq.read()
    poem = json.loads(response)
    poem_line = poem['poem']
    return poem_line

poem_line = refreshPoem()

# Print first poem to the console
for i in range(10):
    print poem_line[i]

# Change the lines below to your own message
lines = [poem_line[0],
         poem_line[1],
         poem_line[2],
         poem_line[3],
         poem_line[4],
         poem_line[5],
         poem_line[6],
         poem_line[7],
         poem_line[8],
         poem_line[9]]

# Determine how far apart each line should be spaced vertically
line_height = scrollphathd.DISPLAY_HEIGHT + 2

# Store the left offset for each subsequent line (starts at the end of the last line)
offset_left = 0

# Draw each line in lines to the Scroll pHAT HD buffer
# scrollphathd.write_string returns the length of the written string in pixels
# we can use this length to calculate the offset of the next line
# and will also use it later for the scrolling effect.
lengths = [0] * len(lines)

for line, text in enumerate(lines):
    lengths[line] = scrollphathd.write_string(text, x=offset_left, y=line_height * line, font=font5x7)
    offset_left += lengths[line]

# Draw each line in lines to the Scroll pHAT HD buffer
scrollphathd.set_pixel(offset_left - 1, (len(lines) * line_height) - 1, 0)

while True:
    # Reset the animation
    scrollphathd.scroll_to(0, 0)
    scrollphathd.show()

    # Keep track of the X and Y position for the rewind effect
    pos_x = 0
    pos_y = 0

    for current_line, line_length in enumerate(lengths):
        # Delay a slightly longer time at the start of each line
        time.sleep(delay*10)

        # Scroll to the end of the current line
        for y in range(line_length):
            scrollphathd.scroll(1, 0)
            pos_x += 1
            time.sleep(delay)
            scrollphathd.show()

        # If we're currently on the very last line and rewind is True
        # We should rapidly scroll back to the first line.
        if current_line == len(lines) - 1 and rewind:
            for y in range(pos_y):
                scrollphathd.scroll(-int(pos_x/pos_y), -1)
                scrollphathd.show()
                time.sleep(delay)

         # Clear the current lines, refresh data and print to console
            lines.clear()
            poem_line = refreshPoem()
            for i in range(10):
                print poem_line[i]

        # Otherwise, progress to the next line by scrolling upwards
        else:
            for x in range(line_height):
                scrollphathd.scroll(0, 1)
                pos_y += 1
                scrollphathd.show()
                time.sleep(delay)
