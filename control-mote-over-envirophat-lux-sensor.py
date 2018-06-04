#!/usr/bin/env python

# https://forums.pimoroni.com/t/help-with-enviro-phat-related-project/7201/4

# Import the necessary modules, including the Enviro pHAT module
import os
import time
from envirophat import light

# Variables used defined below

state = 0       # Logic to tell whether the light is on or off.
period = 15     # Time (in seconds) between checks. Default is 15 seconds.

def lights_on():
    global state
    state = 1
    os.system('curl -s "http://username:password@PI-IP-ADD-RESS/api-all-on/" > /dev/null')
    print('Lights on! Room luminence is {0:.0f} lux.'.format(light.light()))

def lights_off():
    global state
    state = 0
    os.system('curl -s "http://username:password@PI-IP-ADD-RESS/api-all-off/" > /dev/null')
    print('Lights off! Room luminence is {0:.0f} lux.'.format(light.light()))

# Defines when the lights will come on or off.
lower_lux = 240
upper_lux = 260       

while True:
    if state == 0:
        # if lights are off, turn them on when the lower level is reached
        if light.light() < lower_lux:
            lights_on()
    else:
        # the lights are on, turn them off if the level reaches the upper level
        if light.light() > upper_lux:
            lights_off()

    time.sleep(period)