#!/bin/python
# https://medium.com/@aallan/hands-on-with-the-aiy-projects-voice-kit-7c810856faaf
# Script for shutting down the Raspberry Pi by pressing a button.
# by Inderpreet Singh (30 May 2017)
# http://hackaday.com/2017/05/30/diy-google-aiy/

import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(02, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def Shutdown(channel):
 os.system("sudo shutdown -h now")

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(02, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

# Now wait!
while 1:
 time.sleep(1)
