__author__ = 'Charles Gantt'
# This code is part of the Foginator 2000 project developed for the Halloween15 Raspberry Pi Project event at Element14.com and can be found at http://bit.ly/foginator2000

import RPi.GPIO as GPIO
import time
import sys
from sense_hat import SenseHat
from ISStreamer.Streamer import Streamer

logger = Streamer(bucket_name="Foginator2000_Data_10/23/2015", access_key="zLahwAUqKbNKv6YvuT5JuO58EiUOavDa")

sense = SenseHat()
sense.clear()
sensing = True
fog_Armed = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(21, GPIO.OUT)

O = (0, 255, 0) # Green
X = (0, 0, 0) # Black

creeper_pixels = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, X, X, O, O, X, X, O,
    O, X, X, O, O, X, X, O,
    O, O, O, X, X, O, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, O, O, X, O, O
]

black_pixels = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X
]

def is_integration():
   while sensing == True:
        print "IS Start"
        temp = sense.get_temperature()
        temp = round(temp, 1)
        logger.log("Teperature C",temp)
        print "T1"
        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        logger.log("Humidity :",humidity)
        print "H1"
        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        logger.log("Pressure:",pressure)
        print "P1"
        sense.set_pixels(creeper_pixels)
        time.sleep(2)
        sense.set_pixels(black_pixels)
        sense.clear()
        print "IS Done"
        break

def fire_fog():
    while fog_Armed == True:
        print "Fog Start"
        print "Lights Start"
        GPIO.output(21,True)
        time.sleep(2)
        print "Relay Triggered"
        GPIO.output(4,True)
        time.sleep(10)
        print "Relay Disabled"
        GPIO.output(4,False)
        time.sleep(20)
        print "Lights Disabled"
        GPIO.output(21,False)
        is_integration()
        print "Fog Done"
        time.sleep(10)
        print "Watching For Motion"
        break

while True:
    time.sleep(3)
    if GPIO.input(17)==True:
        print "Motion Detected"
        fire_fog()
