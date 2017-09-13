#!/usr/bin/python
#--------------------------------------
#
#            Raspberry Pi
#       GPIO Xmas Tree Add-on
#
# Randomly lights LEDs and shutdowns Pi
# when switch on GPIO25 is pressed.
#
# Author      : Andrew Gale
# Modified By : Matt Hawkins
# Date        : 20/12/2014
# Based on Xmas tree "example_5.py" from
# http://www.pocketmoneytronics.co.uk/
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import os
import tree
import random
import RPi.GPIO as GPIO

# Some constants to identify each LED
L0 = 1
L1 = 2
L2 = 4
L3 = 8
L4 = 16
L5 = 32
L6 = 64
ALL = 1+2+4+8+16+32+64
NO_LEDS = 0

DELAY = 0.2

# Configure switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

tree.setup() # you must always call setup() first!

# Two ways of randomly illuminating LEDs (they do the
# same thing but Way 1 is easier to understand whilst
# Way 2 is a shorter piece of code).

# Loop until switch is pressed
while GPIO.input(25)==0:
  random_led = random.randint(0, 6)
  if (random_led == 0):   tree.leds_on_and_wait(L0, DELAY) # D0 on
  elif (random_led == 1): tree.leds_on_and_wait(L1, DELAY) # D1 on
  elif (random_led == 2): tree.leds_on_and_wait(L2, DELAY) # D2 on
  elif (random_led == 3): tree.leds_on_and_wait(L3, DELAY) # D3 on
  elif (random_led == 4): tree.leds_on_and_wait(L4, DELAY) # D4 on
  elif (random_led == 5): tree.leds_on_and_wait(L5, DELAY) # D5 on
  elif (random_led == 6): tree.leds_on_and_wait(L6, DELAY) # D6 on

tree.all_leds_off() # extinguish all LEDs

# All done!
tree.cleanup() # call cleanup() at the end

# Shutdown Pi
os.system('sudo halt')