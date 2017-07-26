import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)


def fire_fog():
    GPIO.output(4,True)
    time.sleep(3)
    GPIO.output(4,False)
    GPIO.cleanup()
    sys.exit()

while 1:
    time.sleep(3)
    if GPIO.input(17)==True:
        fire_fog()
