################################################################
#                 Green Bay Packers Rainbow                    #
################################################################
# Description:                                                 #
# The title pretty much explains it. It moves a rainbow of     #
# green, gold, and white from one side of the Unicorn PHAT to  #
# the other.                                                   #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
#!/usr/bin/python
import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

G = (0,255,0)
Y = (255,255,0)
W = (255, 255, 255)
off = (0, 0, 0)

rainbow0 = [
    [G, Y, W, G, Y, W, G, Y], 
    [G, Y, W, G, Y, W, G, Y], 
    [G, Y, W, G, Y, W, G, Y], 
    [G, Y, W, G, Y, W, G, Y], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow1 = [
    [Y, W, G, Y, W, G, Y, W], 
    [Y, W, G, Y, W, G, Y, W], 
    [Y, W, G, Y, W, G, Y, W], 
    [Y, W, G, Y, W, G, Y, W], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow2 = [
    [W, G, Y, W, G, Y, W, G], 
    [W, G, Y, W, G, Y, W, G], 
    [W, G, Y, W, G, Y, W, G], 
    [W, G, Y, W, G, Y, W, G],
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow3 = [
    [G, Y, W, G, Y, W, G, Y], 
    [G, Y, W, G, Y, W, G, Y], 
    [G, Y, W, G, Y, W, G, Y], 
    [G, Y, W, G, Y, W, G, Y],
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow4 = [
    [Y, W, G, Y, W, G, Y, W], 
    [Y, W, G, Y, W, G, Y, W], 
    [Y, W, G, Y, W, G, Y, W], 
    [Y, W, G, Y, W, G, Y, W], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

rainbow5 = [
    [W, G, Y, W, G, Y, W, G], 
    [W, G, Y, W, G, Y, W, G], 
    [W, G, Y, W, G, Y, W, G], 
    [W, G, Y, W, G, Y, W, G], 
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