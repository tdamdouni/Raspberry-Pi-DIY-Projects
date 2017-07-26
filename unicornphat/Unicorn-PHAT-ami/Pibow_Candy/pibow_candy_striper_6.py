#!/usr/bin/env python
################################################################
#                    Pibow Candy Striper 6                     #
################################################################
# Description:                                                 #
# This program lights up each column of the Unicorn pHAT with  #
# its respective color.                                        #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

y_coordinates = [4, 3, 2, 1, 0]
x_coordinates = [0, 1, 2, 3, 4, 5, 6, 7]

x0_color_tuple  = (255, 105, 97)
x1_color_tuple  = (255, 179, 71)
x2_color_tuple  = (253, 253, 150)
x3_color_tuple  = (119, 190, 119)
x4_color_tuple  = (119, 158, 203)
x5_color_tuple  = (150, 111, 214)
x6_color_tuple  = (203, 153, 201)
x7_color_tuple  = (244, 154, 194)

def get_color(x_color_tuple): 
    return int(x_color_tuple[0]), int(x_color_tuple[1]), int(x_color_tuple[2]) 
    
def pibow_candy_striper_5():
	
	unicornhat.clear()
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates
	# Shuffle the list
	random.shuffle(x_coordinate_list)
	
	for x in x_coordinate_list:
		#Get the RGB color for the x coordinate
		if x == 0:
			r, g, b, = get_color(x0_color_tuple)
		if x == 1:
			r, g, b, = get_color(x1_color_tuple)
		if x == 2:
			r, g, b, = get_color(x2_color_tuple)
		if x == 3:
			r, g, b, = get_color(x3_color_tuple)
		if x == 4:
			r, g, b, = get_color(x4_color_tuple)
		if x == 5:
			r, g, b, = get_color(x5_color_tuple)
		if x == 6:
			r, g, b, = get_color(x6_color_tuple)
		if x == 7:
			r, g, b, = get_color(x7_color_tuple)						
		# Light up selected x column
		for y in y_coordinate_list:
			unicornhat.set_pixel(x, y, r, g, b)
			unicornhat.show()
			time.sleep(0.05)
	time.sleep(1.0)

def main():
	while True:
		pibow_candy_striper_5()
		
if __name__ == '__main__':
    main()
