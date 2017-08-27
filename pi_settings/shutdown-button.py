#!/usr/bin/python

# http://forums.pimoroni.com/t/blinkt-retropie-auto-stop-script-help/4450

import RPi.GPIO as GPIO
import time
import subprocess


GPIO.setmode(GPIO.BOARD)  


GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)  

oldButtonState1 = True

while True:
    #grab the current button state
    buttonState1 = GPIO.input(5)

    # check to see if button has been pushed
    if buttonState1 != oldButtonState1 and buttonState1 == False:
      subprocess.call("shutdown -h now", shell=True, 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      oldButtonState1 = buttonState1

    time.sleep(.1)