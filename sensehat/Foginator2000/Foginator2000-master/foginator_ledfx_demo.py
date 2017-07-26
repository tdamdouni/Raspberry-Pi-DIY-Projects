import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(21, GPIO.OUT)


def fire_fog():
    GPIO.output(21,True)
    time.sleep(2)
    GPIO.output(4,True)
    time.sleep(10)
    GPIO.output(4,False)
    time.sleep(20)
    GPIO.output(21,False)
    GPIO.cleanup()
    sys.exit()

while 1:
    time.sleep(3)
    if GPIO.input(17)==True:
        fire_fog()
