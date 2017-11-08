#!/usr/bin/env python
########################################
# Basic light show to go in a pumpkin  #
# and light the internals to go with   #
# the 8x8 matrix eyes                  #
#                                      #
#                                      #
########################################
import unicornhat as unicorn
import time

def blit(r,g,b):
    for x in range (8):
        for y in range(8):
            unicorn.set_pixel(x,y,r,g,b)
    unicorn.show()

def flash(r,g,b):
    for b in range(0,20):
        blit(r,g,b)
        time.sleep(0.1)
        blit(0,0,0)
        time.sleep(0.1)
unicorn.brightness(1.0)
unicorn.show()
while True:
    blit(255,0,0)
    time.sleep(5)
    for b in range(0,255):
        blit(255-b,b,0)
        time.sleep(0.01)
    time.sleep(5)
    for b in range(0,255):
        blit(0,255-b,b)
        time.sleep(0.01)
    time.sleep(5)
    for b in range(0,255):
        blit(b,0,255)
        time.sleep(0.01)
    time.sleep(5)
    for b in range(0,255):
        blit(255,b,255)
        time.sleep(0.01)
    time.sleep(2)
    for b in range(0,255):
        blit(255-b,255,255)
        time.sleep(0.01)
    time.sleep(2)
    for b in range(0,255):
        blit(b,255,255-b)
        time.sleep(0.01)
    time.sleep(2)
    flash(255,0,0)
    flash(0,255,0)
    # flash(0,0,255)
    flash(255,255,255)
    flash(255,255,0)
    flash(0,255,255)
    flash(255,0,255)
