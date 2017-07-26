#!/usr/bin/env python

# https://github.com/pimoroni/unicorn-hat/issues/86

import unicornhat as unicorn
import time

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.5)

bToggle = True

print("Unicorn PHat Toggle LEDs with input!")
time.sleep(.5)
print("Press to toggle or + to quit")
time.sleep(.5)

def toggle():
global bToggle
print("On!" if bToggle else "Off!")
i = 255 if bToggle else 0
bToggle = not bToggle
for y in range(4):
for x in range(8):
unicorn.set_pixel(x,y,i,i,i)
unicorn.show()

while True:
toggle()
raw_input("")