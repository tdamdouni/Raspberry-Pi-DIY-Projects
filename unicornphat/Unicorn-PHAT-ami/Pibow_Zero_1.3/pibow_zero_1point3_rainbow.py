################################################################
#                     Pibow Zero 1.3                           #
################################################################
# Description:                                                 #
# It's like my other moving rainbow programs except that it    #
# only displays the colors of the Pibow Zero 1.3 case          #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
#!/usr/bin/python
import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.4)
unicornhat.rotation(180)

R = (255,0,0)
O = (255,128,0)
Y = (255,255,0)
W = (255, 255, 255)
off = (0, 0, 0)

rainbow0 = [
    [R, O, Y, W, R, O, Y, W], 
    [R, O, Y, W, R, O, Y, W], 
    [R, O, Y, W, R, O, Y, W], 
    [R, O, Y, W, R, O, Y, W], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow1 = [
    [O, Y, W, R, O, Y, W, R], 
    [O, Y, W, R, O, Y, W, R], 
    [O, Y, W, R, O, Y, W, R], 
    [O, Y, W, R, O, Y, W, R],
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow2 = [
    [Y, W, R, O, Y, W, R, O], 
    [Y, W, R, O, Y, W, R, O], 
    [Y, W, R, O, Y, W, R, O], 
    [Y, W, R, O, Y, W, R, O], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow3 = [
    [W, R, O, Y, W, R, O, Y], 
    [W, R, O, Y, W, R, O, Y], 
    [W, R, O, Y, W, R, O, Y], 
    [W, R, O, Y, W, R, O, Y], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
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
