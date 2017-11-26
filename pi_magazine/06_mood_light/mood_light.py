#!/usr/bin/env python

import time
from neopixel import *
import RPi.GPIO as GPIO
import datetime


# LED strip
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = True    # True to invert the signal (when using NPN transistor level shift)


# Colors
NO_COLOR = Color(0, 0, 0)
MORNING_COLOR = Color(190, 190, 255)
DAY_COLOR = Color(255, 255, 255)
NIGHT_COLOR = Color(255, 190, 100)
YELLOW = Color(255, 255, 0)
DIM = Color(10, 10, 10)
LONG_PRESS_THRESHOLD = 0.5

colors = [NO_COLOR, MORNING_COLOR, DAY_COLOR, NIGHT_COLOR, YELLOW, DIM]
color_index = 0


# GPIO 
SWITCH_PIN = 23
GPIO.setmode(GPIO.BCM) # Configure the Pi to use the BCM (Broadcom) pin names
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set all the LEDs to the color specified
def set_all(strip, color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()

# Set the color based on the time of day        
def set_color_index_from_time():
    global color_index
    now = datetime.datetime.now()
    if now.hour < 10:
        color_index = 1
    elif now.hour < 21:
        color_index = 2
    else:
        color_index = 3

# Initialize the display        
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()
set_all(strip, colors[0])
strip.show()

print 'Press Ctrl-C to quit.'

while True:
    if GPIO.input(SWITCH_PIN) == False: # button pressed
        down_time = time.time()
        time.sleep(0.2) # debounce
        # Wait for switch release or long press timeout
        while GPIO.input(SWITCH_PIN) == False and time.time() - down_time <= LONG_PRESS_THRESHOLD :
            time.sleep(0.1)
        press_duration = time.time() - down_time
        if press_duration > LONG_PRESS_THRESHOLD:
            set_color_index_from_time()
        else:
            color_index += 1
            if color_index > len(colors)-1:
                color_index = 0
        
        set_all(strip, colors[color_index])
        strip.show()
        while GPIO.input(SWITCH_PIN) == False:
            time.sleep(0.1)

