#!/usr/bin/env python

import time
import scrollphathd
from scrollphathd.fonts import font3x5

print("Press Ctrl+C to exit")

# Try to use Python 2s safe `raw_input`,
# otherwise assume Python 3 `input`.
def safe_input(message):
    try:
        return raw_input(message)
    except NameError:
        return input(message)

minutes = 0
seconds = 0

# Loop until the user has entered a valid time
while True:
    cd_time = safe_input('Enter a countdown time in MM:SS, e.g. "00:30" for 30 seconds: ')

    try:
        # Very crudely parse out the minutes and seconds by splitting
        # on the ":" and casting the two parts to ints.
        minutes, seconds = [int(x) for x in cd_time.strip('"').split(":")]
        break
    except ValueError:
        # Any error parsing the users chosen time is ignored,
        # and we ask them to input a value again
        pass

# Calculate how long we need to count down for in seconds
start_time = time.time()
end_time = start_time + (minutes * 60) + seconds
run_time = end_time - start_time
curr_time = start_time

print("Counting down {minutes} minutes and {seconds} seconds...".format(minutes=minutes, seconds=seconds))

while curr_time < end_time:
    curr_time = time.time()
    remaining = end_time - curr_time
    hundredths = int(remaining * 100)

    # If greater than 59 seconds are left, display minutes + seconds
    if int(remaining) > 59:
        curr_minutes = int(remaining / 60.0)
        curr_seconds = int(remaining % 60)
        padded_str = str("{0:02d}".format(curr_minutes)) + str("{0:02d}".format(curr_seconds))

    # Otherwise display seconds
    else:
        curr_seconds = int(remaining)
        curr_hundredths = int(remaining * 100 % 100)
        padded_str = str("{0:02d}".format(curr_seconds))

    scrollphathd.clear()
    scrollphathd.write_string(padded_str, x=0, y=1, font=font3x5, brightness=0.5)
    scrollphathd.show()

scrollphathd.clear()

print("Done!")
