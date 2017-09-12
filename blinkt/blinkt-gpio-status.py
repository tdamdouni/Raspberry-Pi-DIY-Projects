# http://forums.pimoroni.com/t/use-blinkt-to-show-door-open-or-closed/3633/3

import RPi.GPIO as GPIO
from blinkt import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

while True:
    switch_open = GPIO.input(4)
    if switch_open:
        for i in range(8):
            set_pixel(i , 0, 255, 0)
            # set_all() function
    else:
        for i in range(8):
            set_pixel(i , 255, 0, 0)
            # set_all() function

    show()
