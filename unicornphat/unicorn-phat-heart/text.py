#!/usr/bin/env python

import sys
import time
import math
import unicornhat as unicorn

speed = 0.2

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.3)
width,height=unicorn.get_shape()

chars = {'a':0b101111101010
        ,'b':0b011101011111
        ,'c':0b110001001110
        ,'d':0b011101101011
        ,'e':0b111001011111
        ,'f':0b001001011111
        ,'g':0b110101001111
        ,'h':0b101101111101
        ,'i':0b111010010111
        ,'j':0b010101100111
        ,'k':0b101101011101
        ,'l':0b111001001001
        ,'m':0b101101111111
        ,'n':0b101101101011
        ,'o':0b010101101010
        ,'p':0b001111101111
        ,'q':0b110111101010
        ,'r':0b101011101011
        ,'s':0b111100011111
        ,'t':0b010010010111
        ,'u':0b010101101101
        ,'v':0b001011101101
        ,'w':0b111111101101
        ,'x':0b101101010101
        ,'y':0b010010010101
        ,'z':0b111001010111
        ,' ':0b000000000000
        }

mincol = 120
i = 0.0

def set_pixel(x, y, val):
    if x >= 0 & x < width:
        r = 0#x * 32
        g = 0#y * 32
        xy = x + y / 4
        r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
        g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
        b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
        r = max(0, min(255, r + mincol))
        g = max(0, min(255, g + mincol))
        b = max(0, min(255, b + mincol))
        if val & 1:
            unicorn.set_pixel(x, y, int(r), int(g), int(b))
        else:
            unicorn.set_pixel(x, y, 0, 0, 0)

def draw_char(c, pos):
    if c in chars:
        val = chars[c]
        for y in range(0, 4):
            for x in range(0 + pos - offset, 3 + pos - offset):
                set_pixel(x, y, val)
                val = val >> 1

# text = 'lara mike kawaiitech'
# text = sys.argv[1]
offset = -8
while True:
    f = open('/home/pi/dev/unicorn-phat/sms.txt', 'r')
    text = f.readline()
    i = i + 0.3
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x,y,0,0,0)
    pos = 0
    for c in text:
        draw_char(c, pos)
        pos = pos + 4
    unicorn.show()
    time.sleep(speed)
    offset = offset + 1
    if offset > len(text) * 4:
        offset = -8

# time.sleep(1)
