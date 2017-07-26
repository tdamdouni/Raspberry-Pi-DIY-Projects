################################################################
#                           Flag                               #
################################################################
# Description:                                                 #
# The title pretty much explains it.                           #
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
W = (255, 255, 255)
B = (0,0,255)
off = (0, 0, 0)

flag = [
    [B, B, B, B, R, R, R, R], 
    [B, B, B, B, W, W, W, W], 
    [R, R, R, R, R, R, R, R], 
    [W, W, W, W, W, W, W, W], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

unicornhat.set_pixels(flag)
unicornhat.show()
signal.pause()
