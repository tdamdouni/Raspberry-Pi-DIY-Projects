#!/bin/python 
# Simple script for shutting down the raspberry Pi at the press of a button. 
# by Inderpreet Singh https://www.element14.com/community/docs/DOC-78055/l/adding-a-shutdown-button-to-the-raspberry-pi-b
 
import RPi.GPIO as GPIO  
import time  
import os  
 
# Use the Broadcom SOC Pin numbers 
# Setup the Pin with Internal pullups enabled and PIN in reading mode. 
GPIO.setmode(GPIO.BCM)  
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
# Our function on what to do when the button is pressed 
def Shutdown(channel):  
   os.system("sudo shutdown -h now")  
def Restart(channel):
   os.system("sudo shutdown -r now")
 
# Add our function to execute when the button pressed event happens 
GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  
GPIO.add_event_detect(23, GPIO.FALLING, callback = Restart, bouncetime = 2000) 
 
# Now wait! 
while 1:  
   time.sleep(1) 