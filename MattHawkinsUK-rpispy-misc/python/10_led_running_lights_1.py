#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#          10_led_running_lights_1.py
# Lights up 10 LEDs in sequence. Works with Python 2 and 3.
#
# Author : Matt Hawkins
# Date   : 01/05/2017
#
# http://www.raspberrypi-spy.co.uk/2012/06/knight-rider-cylon-lights-for-the-raspberry-pi/
#
#--------------------------------------

# Import required libraries
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# that are connected to 10 LEDs
# Pins 7,11,15,21,23,16,18,22,24,26
# GPIO4,GPIO17,GPIO22,GPIO9,GPIO11
# GPIO23,GPIO24,GPIO25,GPIO8,GPIO7
RpiGPIO = [4,17,22,9,11,23,24,25,8,7]
 
# Set all pins as output
for pinref in RpiGPIO:
  print("Setup pins")
  GPIO.setup(pinref,GPIO.OUT)
 
# Define some settings
StepCounter = 0
StepDir = 1
WaitTime = 0.2
 
# Define some sequences
 
# One LED
StepCount1 = 10
Seq1 = []
Seq1 = list(range(0,StepCount1))
Seq1[0] =[1,0,0,0,0,0,0,0,0,0]
Seq1[1] =[0,1,0,0,0,0,0,0,0,0]
Seq1[2] =[0,0,1,0,0,0,0,0,0,0]
Seq1[3] =[0,0,0,1,0,0,0,0,0,0]
Seq1[4] =[0,0,0,0,1,0,0,0,0,0]
Seq1[5] =[0,0,0,0,0,1,0,0,0,0]
Seq1[6] =[0,0,0,0,0,0,1,0,0,0]
Seq1[7] =[0,0,0,0,0,0,0,1,0,0]
Seq1[8] =[0,0,0,0,0,0,0,0,1,0]
Seq1[9] =[0,0,0,0,0,0,0,0,0,1]
 
# Double LEDs
StepCount2 = 11
Seq2 = []
Seq2 = list(range(0,StepCount2))
Seq2[0] =[1,0,0,0,0,0,0,0,0,0]
Seq2[1] =[1,1,0,0,0,0,0,0,0,0]
Seq2[2] =[0,1,1,0,0,0,0,0,0,0]
Seq2[3] =[0,0,1,1,0,0,0,0,0,0]
Seq2[4] =[0,0,0,1,1,0,0,0,0,0]
Seq2[5] =[0,0,0,0,1,1,0,0,0,0]
Seq2[6] =[0,0,0,0,0,1,1,0,0,0]
Seq2[7] =[0,0,0,0,0,0,1,1,0,0]
Seq2[8] =[0,0,0,0,0,0,0,1,1,0]
Seq2[9] =[0,0,0,0,0,0,0,0,1,1]
Seq2[10]=[0,0,0,0,0,0,0,0,0,1]
 
# Two LEDs from opposite ends
StepCount3 = 9
Seq3 = []
Seq3 = list(range(0,StepCount3))
Seq3[0] =[1,0,0,0,0,0,0,0,0,1]
Seq3[1] =[0,1,0,0,0,0,0,0,1,0]
Seq3[2] =[0,0,1,0,0,0,0,1,0,0]
Seq3[3] =[0,0,0,1,0,0,1,0,0,0]
Seq3[4] =[0,0,0,0,1,1,0,0,0,0]
Seq3[5] =[0,0,0,1,0,0,1,0,0,0]
Seq3[6] =[0,0,1,0,0,0,0,1,0,0]
Seq3[7] =[0,1,0,0,0,0,0,0,1,0]
Seq3[8] =[1,0,0,0,0,0,0,0,0,1]
 
# Choose a sequence to use
Seq = Seq3
StepCount = StepCount3
 
# Start main loop
while True:
  print("-- Step : "+ str(StepCounter) +" --")
  for pinref in range(0, 10):
    xpin=RpiGPIO[pinref]#
    # Check if LED should be on or off
    if Seq[StepCounter][pinref]!=0:
      print(" Enable " + str(xpin))
      GPIO.output(xpin, True)
    else:
      print(" Disable " + str(xpin))
      GPIO.output(xpin, False)
 
  StepCounter += StepDir
 
  # If we reach the end of the sequence reverse
  # the direction and step the other way
  if (StepCounter==StepCount) or (StepCounter<0):
    StepDir = StepDir * -1
    StepCounter = StepCounter + StepDir + StepDir
 
  # Wait before moving on
  time.sleep(WaitTime)