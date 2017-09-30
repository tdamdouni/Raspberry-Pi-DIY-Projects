# Shows temp (rounded to nearest degree) on SenseHat LEDs
# Using small 3x5 characters, so we can fit two digits without scrolling
# TBD: we still have 3 lines free on the LED matrix: 
# We could fit a little 'degrees' symbol if digits were shifted down.....

from smallhex import to_dec_chars
from sense_hat import SenseHat
from time import sleep

sense=SenseHat()
sense.set_rotation(180)
sense.low_light = True
while True:
	temp = int( round( sense.get_temperature() ) )
	sense.set_pixels( to_dec_chars( temp ) )
	sleep(5)

