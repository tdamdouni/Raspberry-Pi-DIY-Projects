#!/usr/bin/env python

# https://forums.pimoroni.com/t/help-with-enviro-phat-related-project/7201/11

import requests
import time
import datetime
import os
from envirophat import light

# Get the current time
def whats_the_time():
    now = datetime.datetime.now()
    return (now.strftime("%H:%M:%S"))

# The function to turn off the lights. Sends a webhook to IFTTT which
# triggers Hue.

def turn_off():
    requests.post("https://maker.ifttt.com/trigger/{TRIGGER_WORD}/with/key/{TOKEN_GOES_HERE}")
    print("Lights off!")

# The function to turn on the lights. Sends a webhook to IFTTT which                   
# triggers Hue.

def turn_on():
    requests.post("https://maker.ifttt.com/trigger/{TRIGGER_WORD}/with/key/{TOKEN_GOES_HERE}")
    print("Lights on!")

# Check the light level and determine whether the lights need to 
# be turned on or off.

def average_lux():
    # Variables for calculating the average lux levels
    start_time = time.time()
    curr_time = time.time()
    collect_light_time = 15 # Maybe use 60?
    collect_light_data = []

    # Calculate the average lux level over 15 seconds
    print("Calculating average light level...")
    while curr_time - start_time < collect_light_time:
	    curr_time = time.time()
	    avg = light.light()
	    collect_light_data.append(avg)
	    time.sleep(1)
    average_light = sum(collect_light_data[-10:]) / 10.0
    now = whats_the_time()
    print("{} {} {} {} {} {} {} {}.".format("Average over", collect_light_time, "seconds", "is:", average_light, "lux.", "Last checked at", now))
    print("{} {} {} {}.".format("Waiting", "45", "seconds", "before trying again"))
    return average_light

try:
    # Local variables.
    state = 0	# Sets the state for the lights.
    low = 260	# Low value for light level (lux).
    high = 300	# High value for light level (lux).
    period = 45	# Delay, in seconds, between calls.
    while True:
	# Get the average lux level first,
	room_light = average_lux()
	# Now check if the room is dark enough then turn on the lights.
	if room_light < low and state != 1:
	    turn_on()
	    state = 1
	# Or if it is bright enough, turn off the lights.
	elif room_light > high and state == 1:
	    turn_off()
	    state = 0
	time.sleep(period)
except KeyboardInterrupt:
    pass