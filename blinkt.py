
# Blinkt! micro:bit library/demo based on Pimoroni Blinkt! library
# Some setup and exit functions have been removed for simplicity
# The original library is available from https://github.com/pimoroni/blinkt

# Install micropython on your micro:bit and then save this file as main.py
# on your micro:bit
# See the python tools uflash and microfs from ntoll on github
# microfs(ufs) - micro:bit file system tool: https://github.com/ntoll/microfs
# uflash - micro:bit flashing tool: https://github.com/ntoll/uflash

from microbit import *

__version__ = '0.1.0'

DAT = 16	# pin 16 on the micro:bit is patched to pin 23 on the pi with a jumper
CLK = 8		# pin 8 on the micro:bit needs to be patched to pin 24 on the pi
		# take out the jumpers for micro:bit P8 and P5 and use a cable from
		# MBi P8 to RPi 24 
NUM_PIXELS = 8
BRIGHTNESS = 1	#default is set to very low brightness

pixels = [[0,0,0,BRIGHTNESS]] * NUM_PIXELS

def set_brightness(brightness):
    """Set the brightness of all pixels
    :param brightness: Brightness: 0.0 to 1.0
    """

    if brightness < 0 or brightness > 1:
        raise ValueError("Brightness should be between 0.0 and 1.0")

    for x in range(NUM_PIXELS):
        pixels[x][3] = int(31.0 * brightness) & 0b11111

def clear():
    """Clear the pixel buffer"""
    for x in range(NUM_PIXELS):
        pixels[x][0:3] = [0,0,0]

def _write_byte(byte):
    for x in range(8):
    	if byte & 0b10000000:
    		pin16.write_digital(1)
    	else:
    		pin16.write_digital(0)
        pin8.write_digital(1)
        byte <<= 1
        pin8.write_digital(0)

# Original Pimoroni comment:
# Emit exactly enough clock pulses to latch the small dark die APA102s which are weird
# for some reason it takes 36 clocks, the other IC takes just 4 (number of pixels/2)

# This has been modified for the micro:bit version. It simply emits 32 ones at
# the start of frame (sof) and 32 zeros at the end of frame (eof)
# This works for my Blinkt! board (and is specified in a least one APA102 datasheet)
# Your milage may vary, please modify if you seem to have a different Blinkt! board

def _eof():
    pin16.write_digital(0)
    for x in range(32):
        pin8.write_digital(1)
        pin8.write_digital(0)

def _sof():
    pin16.write_digital(0)
    for x in range(32):
        pin8.write_digital(1)
        pin8.write_digital(0)

def show():
    _sof()

    for pixel in pixels:
        r, g, b, brightness = pixel
        _write_byte(0b11100000 | brightness)
        _write_byte(b)
        _write_byte(g)
        _write_byte(r)

    _eof()

def set_all(r, g, b, brightness=None):
    """Set the RGB value and optionally brightness of all pixels
    If you don't supply a brightness value, the last value set for each pixel be kept.
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    for x in range(NUM_PIXELS):
        set_pixel(x, r, g, b, brightness)

def set_pixel(x, r, g, b, brightness=None):
    """Set the RGB value, and optionally brightness, of a single pixel
    
    If you don't supply a brightness value, the last value will be kept.
    :param x: The horizontal position of the pixel: 0 to 7
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    if brightness is None:
        brightness = pixels[x][3]
    else:
        brightness = int(31.0 * brightness) & 0b11111

    pixels[x] = [int(r) & 0xff,int(g) & 0xff,int(b) & 0xff,brightness]

# Simple little demo of 8 colours rotating around and around
# Save this file as main.py on a micro:bit running micropython and the demo should
# start automatically when the Bit:2:Pi is switched on and the micro:bit boots up
# Displays red, green, blue, yellow, magenta, cyan, white and orange
# LEDs are default at a very low brightness - to avoid eye burn-out!
# change BRIGHTNESS which is 1 (min) to 31 (max) to get blinded!

if __name__== "__main__":
	while True:
		for i in range(0,8):
			set_pixel((i+0)%8,255,0,0)	#red
			set_pixel((i+1)%8,0,255,0)	#green
			set_pixel((i+2)%8,0,0,255)	#blue
			set_pixel((i+3)%8,255,255,0)	#yellow
			set_pixel((i+4)%8,255,0,255)	#magenta
			set_pixel((i+5)%8,0,255,255)	#cyan
			set_pixel((i+6)%8,255,255,255)	#white
			set_pixel((i+7)%8,255,130,0)	#orange
			show()
			sleep(50)			#sleep 50 milliseconds
			
