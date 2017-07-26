#!/usr/bin/python
################################################################
#                       Random Green                           #
################################################################
# Description:                                                 #
# Lights up the Unicorn PHAT in different shades of greeen.    #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

y = [0, 1, 2, 3, 4]
x = [0, 1, 2, 3, 4, 5, 6, 7]

color_list = [
    (102, 255, 0), (51, 255, 0), (51, 204, 0), (102, 255, 51), (51, 153, 0), (102, 204, 51), (153, 255, 102), (51, 102, 0),
    (102, 204, 0), (153, 255, 51), (102, 153, 51), (153, 255, 51), (153, 204, 102), (204, 255, 153), (0, 255, 0), (51, 255, 51),
    (102, 255, 102),  (153, 255, 153), (204, 255, 204), (0, 204, 0),  (51, 204, 51), (102, 204, 102), (153, 204, 153), (0, 153, 0), 
    (51, 153, 51), (102, 153, 102), (0, 102, 0), (51, 102, 51), (0, 51, 0), (102, 255, 153), (51, 204, 102), (0, 153, 51),
    (0, 153, 51), (51, 255, 102), (0, 204, 51), (0, 255, 102)
]


def random_x_coordinate():
    return int(random.choice(x))

def random_y_coordinate():
    return int(random.choice(y))

def get_random_color():
    color_tuple = random.choice(color_list) 
    return int(color_tuple[0]), int(color_tuple[1]), int(color_tuple[2])  

def light_up_random_led():
    unicornhat.set_pixel(random_x_coordinate(), random_y_coordinate(), r, g, b)

while True:
    # Turn on a random LED
    r, g, b = get_random_color()
    light_up_random_led()
    #Turn off a random LED
    unicornhat.set_pixel(random_x_coordinate(), random_y_coordinate(), 0, 0, 0)
    unicornhat.show()
    time.sleep(0.01)
