#!/usr/bin/env python

'''
This basic example shows use of the Python Pillow library:

sudo pip-3.2 install pillow # or sudo pip install pillow

The tiny 8x8 chars in lofi.png are from Oddball:
http://forums.tigsource.com/index.php?topic=8834.0

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License.
'''

import signal
import time

try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)

img = Image.open('heart.png')
print(img)

for y in range(img.size[1]):
    for x in range(img.size[0]):
        pixel = img.getpixel((x,y))
        # print(pixel)
        r, g, b, a = int(pixel[0]),int(pixel[1]),int(pixel[2]), int(pixel[3])
        # r, g, b, a = 255, 255, 255, 255
        unicorn.set_pixel(x + 1, y, a, 0, 0)
        print(x, y, r, g, b, a)
unicorn.show()
time.sleep(1.0)
