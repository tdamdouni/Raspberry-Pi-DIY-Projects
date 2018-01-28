# Raspberry Pi Park Sensor

_Captured: 2017-11-18 at 11:36 from [www.instructables.com](http://www.instructables.com/id/Raspberry-Pi-Park-Sensor/)_

![](https://cdn.instructables.com/F72/J0F4/J9OWHMH0/F72J0F4J9OWHMH0.MEDIUM.jpg)

In this instructable we're gonna be building a park sensor. The idea of this park sensor is to show green when you have plenty of room to pull your car forward in parking lot, and then turn yellow as you approach the fully forward position, and then red when you should stop. We're going to build this system with our Raspberry Pi, and use some distances that we can easily test.

## Step 1: Things You Will Need

![](https://cdn.instructables.com/F8X/JCCH/J9OWHKQL/F8XJCCHJ9OWHKQL.MEDIUM.jpg)

You will need the following components other than Raspberry Pi setup.

  1. HC-SR04 Ultrasonic Distance Sensor 
  2. Led (X3) 
  3. 330Ω Resistor (X3) 
  4. 10KΩ Resistor (x2) 
  5. Male-Male / Male-Female Jumper Wires 
  6. Breadboard

## Step 2: Do the Wiring

![](https://cdn.instructables.com/F5M/LNW2/J9SVLAR5/F5MLNW2J9SVLAR5.MEDIUM.jpg)

![](https://cdn.instructables.com/FO5/ACWG/J9SVLAVQ/FO5ACWGJ9SVLAVQ.SMALL.jpg)

![](https://cdn.instructables.com/F5H/MXEC/J9SVLAVX/F5HMXECJ9SVLAVX.SMALL.jpg)

![](https://cdn.instructables.com/FOH/XT6A/J9SVLAW7/FOHXT6AJ9SVLAW7.SMALL.jpg)

![](https://cdn.instructables.com/FV6/9D0N/J9SVLAWS/FV69D0NJ9SVLAWS.SMALL.jpg)

  1. Trigger for the distance sensor is GPIO 4, echo is GPIO 18, the green light is 17, the yellow light is 27 and the red light is 22.
  2. 330 ohm resistors are for the leds and they are connecting to the positive leg of the leds and then GPIO.
  3. 10K ohm resistors are for the echo pin of the distance sensor and connect to the GPIO. 

## Step 3: Code

import RPi.GPIO as GPIO  
import time

GPIO.setwarnings(False)

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

TRIG = 4

ECHO = 18

GREEN = 17

YELLOW = 27

RED = 22

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(GREEN,GPIO.OUT)

GPIO.setup(YELLOW,GPIO.OUT)

GPIO.setup(RED,GPIO.OUT)

def green_light():

GPIO.output(GREEN, GPIO.HIGH)

GPIO.output(YELLOW, GPIO.LOW)

GPIO.output(RED, GPIO.LOW)

def yellow_light():

GPIO.output(GREEN, GPIO.LOW)

GPIO.output(YELLOW, GPIO.HIGH)

GPIO.output(RED, GPIO.LOW)

def red_light(): GPIO.output(GREEN, GPIO.LOW)

GPIO.output(YELLOW, GPIO.LOW)

GPIO.output(RED, GPIO.HIGH)

def get_distance():

GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)

while GPIO.input(ECHO) == False: start = time.time()

while GPIO.input(ECHO) == True: end = time.time()

signal_time = end-start

distance = signal_time / 0.000058

return distance

while True:

distance = get_distance()

time.sleep(0.05)

print(distance)

if distance >= 25:

green_light()

elif 25 > distance > 10:

yellow_light()

elif distance <= 5:

red_light()

If the distance is greater than or equal to 25 cm, we show a green light. If it's between 10 and 25 cm, we'll turn yellow, and then we'll turn red for less than or equal to 10 cm.
