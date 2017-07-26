#!/usr/bin/env python
################################################################
#              Pibow Zero 1.2 Vertical Striper                 #
################################################################
# Description:                                                 #
# This program is a collection of all my Pibow zero programs.  #
# It picks one at random and runs it for 15 seconds.           #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
import unicornhat, signal, time, random
unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)


y_coordinates = [0, 1, 2, 3]
x_coordinates = [0, 1, 2, 3, 4, 5, 6, 7]

y0_color_tuple  = (127,0,255)
y1_color_tuple  = (0,0,255)
y2_color_tuple  = (0,204,204)
y3_color_tuple  = (255, 255, 255)

def get_y_color(y_color_tuple): 
    return int(y_color_tuple[0]), int(y_color_tuple[1]), int(y_color_tuple[2])


def pibow_zero_vertical_striper_1():
	#print "pibow_zero_vertical_striper_1"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates
	
	pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list)

def pibow_zero_vertical_striper_2():
	#print "pibow_zero_vertical_striper_2"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates[::-1]
	
	pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list)

def pibow_zero_vertical_striper_3():
	#print "pibow_zero_vertical_striper_3"
	x_coordinate_list = x_coordinates[::-1]
	y_coordinate_list = y_coordinates
	
	pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list)

def pibow_zero_vertical_striper_4():
	#print "pibow_zero_vertical_striper_4"
	x_coordinate_list = x_coordinates[::-1]
	y_coordinate_list = y_coordinates[::-1]

	pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list)

def pibow_zero_vertical_striper(x_coordinate_list, y_coordinate_list):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	unicornhat.clear()
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		unicornhat.clear()
		for y in y_coordinate_list:
			#Get the RGB color for the x coordinate
			if y == 0:
				r, g, b, = get_y_color(y0_color_tuple)
			if y == 1:
				r, g, b, = get_y_color(y1_color_tuple)
			if y == 2:
				r, g, b, = get_y_color(y2_color_tuple)
			if y == 3:
				r, g, b, = get_y_color(y3_color_tuple)						
			for x in x_coordinate_list:
				unicornhat.set_pixel(x, y, r, g, b)
				unicornhat.show()
				time.sleep(0.05)
		time.sleep(1.0)

function_list = [
				 pibow_zero_vertical_striper_1, pibow_zero_vertical_striper_2, pibow_zero_vertical_striper_3, 
				 pibow_zero_vertical_striper_4
]

def main():
	while True:
	    random.choice(function_list)()
	
if __name__ == '__main__':
    main()
