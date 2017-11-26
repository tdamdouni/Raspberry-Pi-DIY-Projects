#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import urllib2

LIGHT_PIN = 18   # photoresistor pin
EVENT = 'fridge_alert'
BASE_URL = 'https://maker.ifttt.com/trigger/'
KEY = 'cyR3vPNFlP9K32W4NZB9cd'

# Configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_event():
    response = urllib2.urlopen(BASE_URL + EVENT + '/with/key/' + KEY)
    print(response.read())

try:
    while True:
        if GPIO.input(LIGHT_PIN) == 0:
            # Its light (door open)
            send_event()
            # Do nothing until the doior is closed again
            while GPIO.input(LIGHT_PIN) == 0:
                time.sleep(0.1)
            # Do nothing for a further minute anyway
            print("Wait a minute")
            time.sleep(60)
            print("Monitoring again")

finally:
    print('Cleaning up GPIO')
    GPIO.cleanup()
