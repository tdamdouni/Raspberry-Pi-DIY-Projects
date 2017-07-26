#!/usr/bin/python
import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

y = [0, 1, 2, 3, 4]
x = [0, 1, 2, 3, 4, 5, 6, 7]

G = (0,255,0)
Y = (255,255,0)
W = (255, 255, 255)
off = (0, 0, 0)

color_list = [
    (0,255,0), (255,255,0), (255, 255, 255)
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