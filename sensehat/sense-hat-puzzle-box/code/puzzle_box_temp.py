##### Libraries #####
from sense_hat import SenseHat
from time import sleep
from random import choice

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

## Temperature Lock ##
temp=sense.get_temperature()

temp_diffs=[
    -1.5,-1.4,-1.3,-1.2,-1.1,-1,-0.9,-0.8,-0.7,-0.6,
      0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5
    ]

diff = choice(temp_diffs)

target_temp=temp+diff

while abs(diff) > 0.1:
    temp = sense.get_temperature()

    diff = target_temp - temp
    print(diff)

    if diff > 0:
        sense.clear(0,0,150)
    else:
        sense.clear(150,0,0)


##### Unlocked #####
sense.set_pixels(unlocked)
sleep(2)
sense.show_message("This is a secret message",scroll_speed=0.05,text_colour=(255,0,0))
