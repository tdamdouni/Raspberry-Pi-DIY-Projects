#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
while True:
    pin_value = GPIO.input(pin)
        if pin_value == True:
            print ("HIGH")
        else:
            print ("LOW")
        time.sleep(0.5)
