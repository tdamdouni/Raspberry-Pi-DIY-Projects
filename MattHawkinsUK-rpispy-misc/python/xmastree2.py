#!/usr/bin/python
#--------------------------------------
#
#            Raspberry Pi
#        RGB Xmas Tree Add-on
#
# Randomly lights LEDs with a colour
#
# Author      : Andrew Gale
# Modified By : Matt Hawkins
# Date        : 19/12/2016
# Based on example "rgb_tree_example.py" from
# http://www.pocketmoneytronics.co.uk/
#
# Requires installation of Unicorn HAT librares.
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

from neopixel import *
from time import sleep
from random import randint

# set-up the tree
MASTER_BRIGHTNESS = 100 # 0=minimum 255=maximum
tree = Adafruit_NeoPixel(17, 18, 800000, 5, False, MASTER_BRIGHTNESS)
tree.begin()

# useful functions

def set_led_rgb(led_number, red, green, blue):
    # change the colour of an LED by specifying the amount of
    # red, green and blue light to display.
    colour = (green & 255)<<16 | (red & 255) << 8 | (blue & 255) # n.b. GRB not RGB
    tree.setPixelColor(led_number, colour)
    tree.show() # n.b. update immediately

def all_leds_off():
    # set all 6 LEDs to black (i.e. off).
    for i in range(6):
        set_led_rgb(i, 0, 0, 0)
    tree.show()                               
    
##
## Randomly set leds to random colours.
##

all_leds_off()

# start off in a random state
for led_number in range(6):
    red = randint(60, 255)
    green = randint(60, 255)
    blue = randint(60, 255)
    set_led_rgb(led_number, red, green, blue)

try:

    while True:

        # now randomly choose an LED and set it to a
        # random colour
        for i in range(50):
            led_number = randint(0, 5)
            red = randint(60, 255)
            green = randint(60, 255)
            blue = randint(60, 255)
            set_led_rgb(led_number, red, green, blue)
	    sleep(0.3)

except KeyboardInterrupt:
    all_leds_off()
