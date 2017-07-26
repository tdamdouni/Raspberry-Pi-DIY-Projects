################################################################
#                      Moving Rainbow                          #
################################################################
# Description:                                                 #
# The title pretty much explains it. It moves a rainbow of     #
# colors from one side of the Unicorn PHAT to the other.       #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
#!/usr/bin/python
import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

R = (255,0,0)
O = (255,128,0)
Y = (255,255,0)
G = (0,255,0)
B = (0,0,255)
I = (75,0,130)
V = (127,0,255)
W = (255, 255, 255)
off = (0, 0, 0)

rainbow0 = [
    [R, O, Y, G, B, I, V, W], 
    [R, O, Y, G, B, I, V, W], 
    [R, O, Y, G, B, I, V, W], 
    [R, O, Y, G, B, I, V, W], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow1 = [
    [O, Y, G, B, I, V, W, R], 
    [O, Y, G, B, I, V, W, R], 
    [O, Y, G, B, I, V, W, R], 
    [O, Y, G, B, I, V, W, R], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow2 = [
    [Y, G, B, I, V, W, R, O], 
    [Y, G, B, I, V, W, R, O], 
    [Y, G, B, I, V, W, R, O], 
    [Y, G, B, I, V, W, R, O], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow3 = [
    [G, B, I, V, W, R, O, Y], 
    [G, B, I, V, W, R, O, Y], 
    [G, B, I, V, W, R, O, Y], 
    [G, B, I, V, W, R, O, Y], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow4 = [
    [B, I, V, W, R, O, Y, G], 
    [B, I, V, W, R, O, Y, G], 
    [B, I, V, W, R, O, Y, G], 
    [B, I, V, W, R, O, Y, G], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow5 = [
    [I, V, W, R, O, Y, G, B], 
    [I, V, W, R, O, Y, G, B], 
    [I, V, W, R, O, Y, G, B], 
    [I, V, W, R, O, Y, G, B], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow6 = [
    [V, W, R, O, Y, G, B, I], 
    [V, W, R, O, Y, G, B, I], 
    [V, W, R, O, Y, G, B, I], 
    [V, W, R, O, Y, G, B, I], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow7 = [
    [W, R, O, Y, G, B, I, V], 
    [W, R, O, Y, G, B, I, V], 
    [W, R, O, Y, G, B, I, V], 
    [W, R, O, Y, G, B, I, V], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

while True:
    unicornhat.set_pixels(rainbow0)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_pixels(rainbow1)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_pixels(rainbow2)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_pixels(rainbow3)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_pixels(rainbow4)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_pixels(rainbow5)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_pixels(rainbow6)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_pixels(rainbow7)
    unicornhat.show()
    time.sleep(0.5)