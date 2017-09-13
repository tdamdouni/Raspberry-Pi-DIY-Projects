#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____          
#   / _ \/ _ \(_) __/__  __ __ 
#  / , _/ ___/ /\ \/ _ \/ // / 
# /_/|_/_/  /_/___/ .__/\_, /  
#                /_/   /___/   
#
#  HogCam - Wildlife Camera
#
# hogcam.py
# Detect movement using a PIR module and
# take a sequences of photos
#
# Author : Matt Hawkins
# Date   : 19/07/2014
#
# http://www.raspberrypi-spy.co.uk/
#
# Uses the picamera Python library
# http://picamera.readthedocs.org/
#
#--------------------------------------

# Import required Python libraries
import os
import time
import picamera
import RPi.GPIO as GPIO

#======================================
# User Configurable Settings
PHOTO_SIZE_H  = 1280
PHOTO_SIZE_V  = 720
PHOTO_COUNT   = 20
PHOTO_DELAY   = 1
PHOTO_DIR     = '/media/usb/'
AUTO_SHUTDOWN = True
#======================================

# Setup GPIO pins
print "Configuring GPIO ..."
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_LED1 = 4
GPIO_LED2 = 17
GPIO_LED3 = 22
GPIO_LED4 = 10
GPIO_LED5 = 9
GPIO_LED6 = 11
GPIO_BUZZ = 8
GPIO_SWT1 = 7
GPIO_SWT2 = 25
GPIO_PIR  = 18

GPIO.setwarnings(False)

# Set PIR and Switch pins as inputs
GPIO.setup(GPIO_SWT1,GPIO.IN)  # Switch 1
GPIO.setup(GPIO_SWT2,GPIO.IN)  # Switch 2
GPIO.setup(GPIO_PIR,GPIO.IN)   # Echo

# Set LED pins as outputs
GPIO.setup(GPIO_LED1,GPIO.OUT) # LED 1
GPIO.setup(GPIO_LED2,GPIO.OUT) # LED 2
GPIO.setup(GPIO_LED3,GPIO.OUT) # LED 3
GPIO.setup(GPIO_LED4,GPIO.OUT) # LED 4
GPIO.setup(GPIO_LED5,GPIO.OUT) # LED 5
GPIO.setup(GPIO_LED6,GPIO.OUT) # LED 6

photo_counter = 0
switch2_state = GPIO.input(GPIO_SWT2)

try:
  
  GPIO.output(GPIO_LED1,True)
  GPIO.output(GPIO_LED2,False)

  print "Waiting for PIR to settle ..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    time.sleep(0.2)
    GPIO.output(GPIO_LED1,not GPIO.input(GPIO_LED1))
    GPIO.output(GPIO_LED2,not GPIO.input(GPIO_LED2))
  GPIO.output(GPIO_LED1,False)
  GPIO.output(GPIO_LED2,False)

  GPIO.output(GPIO_LED6,True)

  # Loop until users quits with CTRL-C
  while switch2_state==0 :

    print "Waiting for motion :"

    while GPIO.input(GPIO_PIR)==0 and switch2_state==0:
      time.sleep(0.1)
      switch2_state = GPIO.input(GPIO_SWT2)

    if switch2_state==0:

      # Take photos
      print "Fire-up camera ..."
      camera = picamera.PiCamera()
      camera.led = False
      camera.resolution = (PHOTO_SIZE_H, PHOTO_SIZE_V)
      for i in range(PHOTO_COUNT):
        filename='img_'+"{0:0>4}".format(photo_counter)+'_'+"{0:0>2}".format(i)+'.jpg'
        camera.capture(PHOTO_DIR+filename)
        print('  Captured %s' % filename)
        GPIO.output(GPIO_LED3,True)
        time.sleep(PHOTO_DELAY)
        GPIO.output(GPIO_LED3,False)
      camera.close()
      photo_counter=photo_counter+1
      GPIO.output(GPIO_LED4,True)

  print "Switch pressed"
 
  # Blink Red LED
  GPIO.output(GPIO_LED1,True)
  time.sleep(1)
  GPIO.output(GPIO_LED1,False)

  # Turn off LEDs
  GPIO.output(GPIO_LED3,False)
  GPIO.output(GPIO_LED4,False)  
  GPIO.output(GPIO_LED6,False)
  
  if AUTO_SHUTDOWN==True:
    print "Auto Shutdown"
    os.system('shutdown -h now')   

except KeyboardInterrupt:
  print "User quit"
  GPIO.output(GPIO_LED6,False)
  GPIO.cleanup() # Reset GPIO