################################################################
#                      Pibow Zero 1.2                          #
################################################################
# Description:                                                 #
# It's like my other moving rainbow programs except that it    #
# only displays the colors of the Pibow Zero 1.2 case          #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
#!/usr/bin/python
import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.4)
unicornhat.rotation(180)

B = (0,0,255)
I = (0,204,204)
V = (127,0,255)
W = (255, 255, 255)
off = (0, 0, 0)

rainbow0 = [
    [V, B, I, W, V, B, I, W], 
    [V, B, I, W, V, B, I, W], 
    [V, B, I, W, V, B, I, W], 
    [V, B, I, W, V, B, I, W], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow1 = [
    [B, I, W, V, B, I, W, V], 
    [B, I, W, V, B, I, W, V], 
    [B, I, W, V, B, I, W, V], 
    [B, I, W, V, B, I, W, V], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow2 = [
    [I, W, V, B, I, W, V, B], 
    [I, W, V, B, I, W, V, B], 
    [I, W, V, B, I, W, V, B], 
    [I, W, V, B, I, W, V, B], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow3 = [
    [W, V, B, I, W, V, B, I], 
    [W, V, B, I, W, V, B, I], 
    [W, V, B, I, W, V, B, I], 
    [W, V, B, I, W, V, B, I], 
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
