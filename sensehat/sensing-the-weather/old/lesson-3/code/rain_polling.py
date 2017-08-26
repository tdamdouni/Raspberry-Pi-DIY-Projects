#!/usr/bin/python

import RPi.GPIO as GPIO
import time

pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

current_state = 0
previous_state = 0
count = 0

while True: 
    current_state = GPIO.input(pin)

    if previous_state == GPIO.HIGH and current_state == GPIO.LOW:
        count=count + 1
        print (count * 0.2794)

    previous_state = current_state
    time.sleep(0.01)
