#!/usr/bin/python3
import RPi.GPIO as GPIO

pin = 6
count = 0

def spin(channel):
    global count
    count = count + 1
    print count

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped)

input("Press enter to stop logging\n")
