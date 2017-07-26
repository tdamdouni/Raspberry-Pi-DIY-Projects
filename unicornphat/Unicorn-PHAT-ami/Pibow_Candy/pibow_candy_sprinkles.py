#!/usr/bin/env python
################################################################
#                    Pibow Candy Sprinkles                     #
################################################################
# Description:                                                 #
# This takes the colors from the Pibow Candy programs and      #
# lights up random LEDs.
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
#unicornhat.rotation(180)

y = [0, 1, 2, 3, 4]
x = [0, 1, 2, 3, 4, 5, 6, 7]

color_list = [
    (255, 105, 97), (255, 179, 71), (253, 253, 150), (119, 190, 119), 
    (119, 158, 203), (150, 111, 214), (203, 153, 201), (244, 154, 194)
]

def random_x_coordinate():
    return int(random.choice(x))

def random_y_coordinate():
    return int(random.choice(y))

def get_random_color():
    color_tuple = random.choice(color_list) 
    return int(color_tuple[0]), int(color_tuple[1]), int(color_tuple[2])  
    
def light_up_random_led(r, g, b):
    unicornhat.set_pixel(random_x_coordinate(), random_y_coordinate(), r, g, b)
    
def pibow_candy_sprinkles():
	# Turn on a random LED
	r, g, b = get_random_color()
	light_up_random_led(r, g, b)
	#Turn off a random LED
	unicornhat.set_pixel(random_x_coordinate(), random_y_coordinate(), 0, 0, 0)
	unicornhat.show()
	time.sleep(0.01)

def main():
	while True:
		pibow_candy_sprinkles()

if __name__ == '__main__':
    main()
