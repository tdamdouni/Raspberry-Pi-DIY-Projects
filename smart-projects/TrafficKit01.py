#!/usr/bin/env python
# Traffic Lights Demo Sequence
# Runs until Ctrl/C is pressed

# Must be run as root - sudo python TrafficKit01.py 

import time, random, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_RED = 7
LED_AMBER = 11
LED_GREEN = 13

LEDOFF = 0
LEDON = 1

def setupgpio():
  GPIO.setup(LED_RED, GPIO.OUT)
  GPIO.setup(LED_AMBER, GPIO.OUT)
  GPIO.setup(LED_GREEN, GPIO.OUT)
        
def alloff (val):
    GPIO.output (LED_RED, LEDOFF)
    GPIO.output (LED_AMBER, LEDOFF)
    GPIO.output (LED_GREEN, LEDOFF)
    time.sleep(val)
    
def allon (val):
    GPIO.output (LED_RED, LEDON)
    GPIO.output (LED_AMBER, LEDON)
    GPIO.output (LED_GREEN, LEDON)
    time.sleep(val)

def red (val):
    GPIO.output (LED_RED, LEDON)
    GPIO.output (LED_AMBER, LEDOFF)
    GPIO.output (LED_GREEN, LEDOFF)
    time.sleep(val)

def redamber (val):
    GPIO.output (LED_RED, LEDON)
    GPIO.output (LED_AMBER, LEDON)
    GPIO.output (LED_GREEN, LEDOFF)
    time.sleep(val)

def amber (val):
    GPIO.output (LED_RED, LEDOFF)
    GPIO.output (LED_AMBER, LEDON)
    GPIO.output (LED_GREEN, LEDOFF)
    time.sleep(val)

def green (val):
    GPIO.output (LED_RED, LEDOFF)
    GPIO.output (LED_AMBER, LEDOFF)
    GPIO.output (LED_GREEN, LEDON)
    time.sleep(val)

def flashall (val):
    count = 0
    while count < val:
        allon(0.1)
        alloff(0.1)
        count += 1

def basicSequence (val):
    count = 0
    while count < val:
        red (3)
        redamber (1)
        green (3)
        amber (1)
        red (0)
        count += 1

try:   
  while True:
    setupgpio()
    alloff(0)
    flashall(5)
    basicSequence (5)

except KeyboardInterrupt:
  GPIO.cleanup()
  exit()
