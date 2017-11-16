#!/usr/bin/env python
# coding: Latin-1

# some of the code in this program is from the example code by PiBorg.
# more imformation can be found here.
# https://github.com/piborg/zeroborg/
#
# the joy of open source code :-D

# import libraries required

import ZeroBorg
import RPi.GPIO as GPIO
import time


# define pins for the line following sensor

leftPin = 10
middlePin = 9
rightPin = 11




# Setup pins for line following sensor

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(leftPin, GPIO.IN)
GPIO.setup(middlePin, GPIO.IN)
GPIO.setup(rightPin, GPIO.IN)


# Setup the ZeroBorg


ZB = ZeroBorg.ZeroBorg()
ZB.Init()
ZB.ResetEpo()

# Power settings
voltageIn = 8.4                         # Total battery voltage to the ZeroBorg (change to 9V if using a non-rechargeable battery)
voltageOut = 6.0                        # Maximum motor voltage

# Setup the power limits
if voltageOut > voltageIn:
    maxPower = 1
else:
    maxPower = voltageOut / float(voltageIn)

# kill power to motors

ZB.MotorsOff()

# funtions

def readInputs():
    left = 0
    middle = 0
    right = 0

    if GPIO.input(leftPin) == False:
        print("left\n")
        left = 1

    if GPIO.input(middlePin) == False:
        print("middle\n")
        middle = 1

    if GPIO.input(rightPin) == False:
        print("right\n")
        right = 1

    returnValues = [left, middle, right]
    return returnValues

# define motor speed values and set to 0.0

driveLeft = 0.0
driveRight = 0.0
oldDriveLeft = 0.0
oldDriveRight = 0.0

# control loop

while True:


    line = readInputs() # call the read line following sensor function
    # print line # remove hash for debuging
    time.sleep(0.01) # adjust if 100 per second reads if too fast or slow
	
	# if line is on left turn right

    if (line == [0, 1, 1]):
         driveLeft = -0.6
         driveRight = 0.6
		 
    # if line is central, power both motors

    if (line == [1, 0, 1]):
         driveLeft = 0.5
         driveRight = 0.5
		 
    # if line is right turn left

    if (line == [1, 1, 0]):
         driveLeft = 0.6
         driveRight =-0.6
		 
	# if can't see line, repeat last move

    if (line == [1, 1, 1]):
        driveLeft = oldDriveLeft
        driveRight = oldDriveRight
		
	# save driveLeft and driveRight to oldDriveLeft and oldDriveRight

    oldDriveLeft = driveLeft
    oldDriveRight = driveRight
	
	# update motor values

    ZB.SetMotor2(-driveLeft * maxPower)
    ZB.SetMotor3(-driveLeft * maxPower)
    ZB.SetMotor1(-driveRight * maxPower)
    ZB.SetMotor4(-driveRight * maxPower)

