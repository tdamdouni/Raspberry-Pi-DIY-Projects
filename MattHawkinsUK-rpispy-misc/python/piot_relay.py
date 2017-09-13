#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           piot.py
#  Test sequence for ModMyPi PiOT Relay board
#
#  Official Wiki here :
#  https://github.com/modmypi/PiOT-Relay-Board/wiki
#
# Author : Matt Hawkins
# Date   : 14/09/2016
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import time
import RPi.GPIO as GPIO

# Define GPIO used for each relay
relay1=5
relay2=6
relay3=13
relay4=19

def Handshake():
  # Send connect/disconnect
  # pulse train to GPIO2
  for x in range(4):
    GPIO.output(2,1)
    time.sleep(0.05)
    GPIO.output(2,0)
    time.sleep(0.05)

#Turn off GPIO warnings
GPIO.setwarnings(False)

#Set the GPIO numbering to be GPIO numbers
GPIO.setmode(GPIO.BCM)    

# Configure GPIOs as outputs
GPIO.setup(2,GPIO.OUT)
GPIO.setup(relay1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(relay2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(relay3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(relay4,GPIO.OUT,initial=GPIO.LOW)

# Send handshake to enable board
Handshake()

print("Board active")

time.sleep(1)

# Toggle relays and loop
for x in range(6):
  GPIO.output(relay1, not GPIO.input(relay1))
  time.sleep(0.5)
  GPIO.output(relay2, not GPIO.input(relay2))
  time.sleep(0.5)
  GPIO.output(relay3, not GPIO.input(relay3))
  time.sleep(0.5)
  GPIO.output(relay4, not GPIO.input(relay4))
  time.sleep(0.5)

# Send handshake to disable board
Handshake()

print("Board inactive")