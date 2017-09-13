#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____          
#   / _ \/ _ \(_) __/__  __ __ 
#  / , _/ ___/ /\ \/ _ \/ // / 
# /_/|_/_/  /_/___/ .__/\_, /  
#                /_/   /___/   
#
#  MAX7219 Seven Segment Display
#  Boba Fett Chestplate Display
#
# By default it will display random characters
# on all segments. Pass "random" or "seq" on
# the command line to change mode.
# e.g. python 7segmentboba.py seq
#
# The predefined sequence is based on information
# posted by "RafalFett" on TheDentedHelmet.com
# http://www.thedentedhelmet.com/f20/esb-chest-display-sequence-43686/
#
# Author : Matt Hawkins
# Date   : 27/02/2016
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import max7219.led as led
import sys
import time
import random

def getRandomChar():
  # Get a random character 
  charset = '0123456789abcdefghijklmnopqrstuvwxyz-'
  val = random.randint(0,len(charset)-1)
  return charset[val]

if len(sys.argv)>1:
  mode=sys.argv[1]
  mode=mode.lower()
else:
  mode='random'
  
# Setup display
device = led.sevensegment()
device.brightness(2)
device.clear()

interval = 1.2

starttext = 'B0BAFETT'

sequence = [' dmeug  ',
            ' 88888  ',
            ' dmeug  ',
            ' sexyn  ',
            ' kiqho  ',
            ' dmeug  ',
            ' njvwh  ',
            ' kiqho  ',
            ' dmeug  ',
            ' ntvzp  ',
            ' dmeug  ',
            ' sexyn  '
]

# Display text
for index, char in enumerate(starttext):
  device.letter(0, 8-index, char)   

time.sleep(1)

try:

  # Display random symbols
  print("Random sequence")
  while mode=='random':
    for index in range(1,9):
      device.letter(0, index, getRandomChar())  
    time.sleep(interval)

  # Display sequence
  print("Predefined sequence")  
  while mode=='seq':
    for item in sequence:
      for index, char in enumerate(item):
        device.letter(0, 8-index, char)      
      time.sleep(interval)
    
except KeyboardInterrupt:
  print("Stop")