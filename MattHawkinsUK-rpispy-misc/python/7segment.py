#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____          
#   / _ \/ _ \(_) __/__  __ __ 
#  / , _/ ___/ /\ \/ _ \/ // / 
# /_/|_/_/  /_/___/ .__/\_, /  
#                /_/   /___/   
#
#  MAX7219 Seven Segment Display Model
#
# Author : Matt Hawkins
# Date   : 27/02/2016
#
# http://www.raspberrypi-spy.co.uk/
#
# This script is a simplified version of the sevensegment example script
# provided by Richard Hull with his MAX7219 driver.
# https://github.com/rm-hull/max7219
# Those files are available under the following licence terms :
#
#  The MIT License (MIT)
#  Copyright (c) 2015 Richard Hull
#  Permission is hereby granted, free of charge,
#  to any person obtaining a copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation the rights to use,
#  copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#  The above copyright notice and this permission notice shall be included in all copies
#  or substantial portions of the Software.
#
#--------------------------------------
import max7219.led as led
import time
import random
from datetime import datetime

def date(device, deviceId):
    now   = datetime.now()
    day   = now.day
    month = now.month
    year  = now.year - 2000

    # Set day
    device.letter(deviceId, 8, int(day / 10))     # Tens
    device.letter(deviceId, 7, day % 10)          # Ones
    device.letter(deviceId, 6, '-')               # dash
    # Set day
    device.letter(deviceId, 5, int(month / 10))   # Tens
    device.letter(deviceId, 4, month % 10)        # Ones
    device.letter(deviceId, 3, '-')               # dash
    # Set day
    device.letter(deviceId, 2, int(year / 10))    # Tens
    device.letter(deviceId, 1, year % 10)         # Ones

device = led.sevensegment()

# Write date
date(device, 0)

# Adjust Brightness
for x in xrange(5):
    for intensity in xrange(16):
        device.brightness(intensity)
        time.sleep(0.1)

device.brightness(7)

# Scroll Text
for i in xrange(8):
  device.scroll_right()
  time.sleep(0.1)

device.clear()
time.sleep(1)

# Random Numbers
while True:
  # Random float
  num = random.uniform(0,99999)
  device.write_number(deviceId=0, value=num, zeroPad=True, decimalPlaces=3)
  time.sleep(0.5)