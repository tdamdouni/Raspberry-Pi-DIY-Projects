##### Libraries #####
from sense_hat import SenseHat
from time import sleep
from random import choice
from piGPS import GPS

##### Functions #####

##### Pixel Art #####
r = (255, 0, 0)
g = (0, 255, 0)
w = (255, 255, 255)
e = (0, 0, 0)

locked = [e,e,e,e,e,e,e,e,e,e,e,w,w,e,e,e,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,e,e,r,r,r,r,e,e,e,e,r,r,r,r,e,e,e,e,r,r,r,r,e,e,e,e,e,e,e,e,e,e]

unlocked = [e,e,e,e,e,e,e,e,e,e,e,e,e,w,w,e,e,e,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,g,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,e,e,e,e,e,e]

tick = [e,e,e,e,e,e,e,g,e,e,e,e,e,e,g,g,e,e,e,e,e,g,g,e,e,e,e,e,g,g,e,e,g,g,e,g,g,e,e,e,e,g,g,g,e,e,e,e,e,e,g,e,e,e,e,e,e,e,e,e,e,e,e,e]


##### Main Program #####
sense = SenseHat()
sense.set_pixels(locked)
sleep(2)

##### Locks #####

## Temperature Lock ##
gps = GPS()
targets = [
    [52.220370, 0.111730],
    [52.189315, 0.176366]
]


for target in targets:
    distance = 999999

    while distance > 0.01:
        if gps.sat < 4:
            sense.show_message(
                "Are you outside?",
                scroll_speed=0.05,
                text_colour=(150,150,150)
          )
        else:
            lastDistance = distance
            distance = round(gps.distanceToTarget(target),2)

            if distance < lastDistance and lastDistance !=999999:
                msg = "Warmer...{0}m".format(int(distance*1000))
                colour = (150,0,0)
            elif distance > lastDistance:
                msg = "Colder...{0}m".format(int(distance*1000))
                colour = (0,0,150)

                sense.show_message(
                  msg,
                  scroll_speed=0.05,
                  text_colour=colour
                )

        sense.set_pixels(locked)
        sleep(5)
    sense.set_pixels(tick)
    sleep(5)




##### Unlocked #####
sense.set_pixels(unlocked)
sleep(2)
sense.show_message("This is a secret message",scroll_speed=0.05,text_colour=(255,0,0))
