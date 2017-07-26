##### Libraries #####
from sense_hat import SenseHat
from time import sleep

##### Functions #####


##### Pixel Art #####
r = (255, 0, 0)
g = (0, 255, 0)
w = (255, 255, 255)
e = (0, 0, 0)

locked = [e,e,e,e,e,e,e,e,e,e,e,w,w,e,e,e,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,e,e,r,r,r,r,e,e,e,e,r,r,r,r,e,e,e,e,r,r,r,r,e,e,e,e,e,e,e,e,e,e]

unlocked = [e,e,e,e,e,e,e,e,e,e,e,e,e,w,w,e,e,e,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,g,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,e,e,e,e,e,e]


##### Main Program #####
sense = SenseHat()
sense.set_pixels(locked)
sleep(2)

##### Locks #####


##### Unlocked #####
sense.set_pixels(unlocked)
sleep(2)
sense.show_message("This is a secret message",scroll_speed=0.05,text_colour=(255,0,0))
