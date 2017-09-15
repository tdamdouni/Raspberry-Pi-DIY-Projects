#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#          10_led_running_lights_3.py
#
# Light up 10 LEDs in different sequences. Can be called with two
# optional command line options. One to specify the number of loops
# per sequence and one to specify the delay in seconds.
# Works with Python 2 and 3.
#
# Example usage :
# python 10_led_running_lights_3 5 0.2
# would run each sequence for 5 loops with a 0.2 second delay between each LED.
#
# Author : Matt Hawkins
# Date   : 02/05/2017
#
# http://www.raspberrypi-spy.co.uk/2012/06/knight-rider-cylon-lights-for-the-raspberry-pi/
#
#--------------------------------------

# Import required libraries
import RPi.GPIO as GPIO
import sys
import time

def populateSeq(index):
  # Take a number and return sequence list
  Seq = []
  if index==1:
    # One LED
    StepCount = 10
    Seq = list(range(0,StepCount))
    Seq[0] =[1,0,0,0,0,0,0,0,0,0]
    Seq[1] =[0,1,0,0,0,0,0,0,0,0]
    Seq[2] =[0,0,1,0,0,0,0,0,0,0]
    Seq[3] =[0,0,0,1,0,0,0,0,0,0]
    Seq[4] =[0,0,0,0,1,0,0,0,0,0]
    Seq[5] =[0,0,0,0,0,1,0,0,0,0]
    Seq[6] =[0,0,0,0,0,0,1,0,0,0]
    Seq[7] =[0,0,0,0,0,0,0,1,0,0]
    Seq[8] =[0,0,0,0,0,0,0,0,1,0]
    Seq[9] =[0,0,0,0,0,0,0,0,0,1]
  elif index==2:
    # Double LEDs
    StepCount = 11
    Seq = list(range(0,StepCount))
    Seq[0] =[1,0,0,0,0,0,0,0,0,0]
    Seq[1] =[1,1,0,0,0,0,0,0,0,0]
    Seq[2] =[0,1,1,0,0,0,0,0,0,0]
    Seq[3] =[0,0,1,1,0,0,0,0,0,0]
    Seq[4] =[0,0,0,1,1,0,0,0,0,0]
    Seq[5] =[0,0,0,0,1,1,0,0,0,0]
    Seq[6] =[0,0,0,0,0,1,1,0,0,0]
    Seq[7] =[0,0,0,0,0,0,1,1,0,0]
    Seq[8] =[0,0,0,0,0,0,0,1,1,0]
    Seq[9] =[0,0,0,0,0,0,0,0,1,1]
    Seq[10]=[0,0,0,0,0,0,0,0,0,1]
  elif index==3:
    # Two LEDs from opposite ends
    StepCount = 9
    Seq = list(range(0,StepCount))
    Seq[0] =[1,0,0,0,0,0,0,0,0,1]
    Seq[1] =[0,1,0,0,0,0,0,0,1,0]
    Seq[2] =[0,0,1,0,0,0,0,1,0,0]
    Seq[3] =[0,0,0,1,0,0,1,0,0,0]
    Seq[4] =[0,0,0,0,1,1,0,0,0,0]
    Seq[5] =[0,0,0,1,0,0,1,0,0,0]
    Seq[6] =[0,0,1,0,0,0,0,1,0,0]
    Seq[7] =[0,1,0,0,0,0,0,0,1,0]
    Seq[8] =[1,0,0,0,0,0,0,0,0,1]
  else:
    # One LED
    StepCount = 10
    Seq = list(range(0,StepCount1))
    Seq[0] =[1,0,0,0,0,0,0,0,0,0]
    Seq[1] =[0,1,0,0,0,0,0,0,0,0]
    Seq[2] =[0,0,1,0,0,0,0,0,0,0]
    Seq[3] =[0,0,0,1,0,0,0,0,0,0]
    Seq[4] =[0,0,0,0,1,0,0,0,0,0]
    Seq[5] =[0,0,0,0,0,1,0,0,0,0]
    Seq[6] =[0,0,0,0,0,0,1,0,0,0]
    Seq[7] =[0,0,0,0,0,0,0,1,0,0]
    Seq[8] =[0,0,0,0,0,0,0,0,1,0]
    Seq[9] =[0,0,0,0,0,0,0,0,0,1]
  return Seq

# Use GPIO references
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# that are connected to 10 LEDs
# Pins 7,11,15,21,23,16,18,22,24,26
# GPIO4,GPIO17,GPIO22,GPIO9,GPIO11
# GPIO23,GPIO24,GPIO25,GPIO8,GPIO7
RpiGPIO = [4,17,22,9,11,23,24,25,8,7]

# Set all pins as output
for pin in RpiGPIO:
  print("Setup GPIO"+str(pin)+" as output")
  GPIO.setup(pin,GPIO.OUT)

# Handle command line arguments
if len(sys.argv)==3:
  try:
    SeqLoops = int(sys.argv[1])
    WaitTime = float(sys.argv[2])
  except:
    SeqLoops = 10
    WaitTime = 0.1
else:
  SeqLoops = 10
  WaitTime = 0.1

SeqCount = 0
  
# Start main loop
while True:

  SeqCount=SeqCount+1
  if SeqCount>3:
    SeqCount=1

  # Populae list with sequence
  Seq = populateSeq(SeqCount)
  StepCount = len(Seq)
  StepCounter = 0
  StepDir = 1

  for loop in range(SeqLoops*StepCount):

    print("-- Step : "+ str(StepCounter) +" --")

    for pin in range(0, 10):
      xpin = RpiGPIO[pin]
      if Seq[StepCounter][pin]!=0:
        print(" Enable " + str(xpin))
        GPIO.output(xpin, True)
      else:
        print(" Disable "+ str(xpin))
        GPIO.output(xpin, False)

    StepCounter += StepDir

    # If we reach the end of the sequence reverse
    # the direction and step the other way
    if (StepCounter==StepCount) or (StepCounter<0):
      StepDir = StepDir * -1
      StepCounter = StepCounter + StepDir + StepDir

    # Wait before moving on
    time.sleep(WaitTime)
