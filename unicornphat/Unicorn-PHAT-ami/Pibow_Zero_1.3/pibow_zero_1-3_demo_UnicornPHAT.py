#!/usr/bin/env python
################################################################
#          Pibow Zero 1.3 Demo for the Unicorn pHAT            #
################################################################
# Description:                                                 #
# This program is a collection of all my Pibow zero programs. #
# It picks one at random and runs it for 15 seconds.           #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

import unicornhat, signal, time, random
unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

V = (255,0,0)
B = (255,128,0)
I = (255,255,0)
W = (255, 255, 255)
off = (0, 0, 0)
B2 = (128, 0, 0)
I2 = (128, 114, 102)
V2 = (128, 128, 128)
W2 = (128, 128, 128)

color_list = [
    (255,0,0), (255,128,0), (255,255,0), (255, 255, 255) 
]
    
y_coordinates = [0, 1, 2, 3]
x_coordinates = [0, 1, 2, 3, 4, 5, 6, 7]

x0_color_tuple  = (255,0,0)
x1_color_tuple  = (255,128,0)
x2_color_tuple  = (255,255,0)
x3_color_tuple  = (255, 255, 255)
x4_color_tuple  = (255,0,0)
x5_color_tuple  = (255,128,0)
x6_color_tuple  = (255,255,0)
x7_color_tuple  = (255, 255, 255)

y0_color_tuple  = (255,0,0)
y1_color_tuple  = (255,128,0)
y2_color_tuple  = (255,255,0)
y3_color_tuple  = (255, 255, 255)

def get_pibow_zero_horizontal_rainbow():
	
	rainbow = [
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
	
	return rainbow

def get_pibow_zero_vertical_rainbow():
	
	rainbow = [
		[W, W, W, W, W, W, W, W], 
		[I, I, I, I, I, I, I, I], 
		[B, B, B, B, B, B, B, B], 
		[V, V, V, V, V, V, V, V], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
]
	
	return rainbow

def get_horizontal_rainbow():
	
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

	return rainbow1, rainbow2, rainbow3

def move_the_rainbow_horizontally(rainbow0, rainbow1, rainbow2, rainbow3):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
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

def pibow_zero_rainbow():
	#print "pibow_zero_rainbow"
	rainbow0 = get_pibow_zero_horizontal_rainbow()

	rainbow1, rainbow2, rainbow3 = get_horizontal_rainbow()
		
	move_the_rainbow_horizontally(rainbow0, rainbow1, rainbow2, rainbow3) 

def pibow_zero_rainbow_2():
	#print "pibow_zero_rainbow_2"
	rainbow0 = get_pibow_zero_horizontal_rainbow()

	rainbow3, rainbow2, rainbow1 = get_horizontal_rainbow()

	move_the_rainbow_horizontally(rainbow0, rainbow1, rainbow2, rainbow3)

def get_vertical_rainbow():

	rainbow1 = [
		[I, I, I, I, I, I, I, I], 
		[B, B, B, B, B, B, B, B], 
		[V, V, V, V, V, V, V, V], 
		[W, W, W, W, W, W, W, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow2 = [ 
		[B, B, B, B, B, B, B, B], 
		[V, V, V, V, V, V, V, V], 
		[W, W, W, W, W, W, W, W], 
		[I, I, I, I, I, I, I, I], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow3 = [ 
		[V, V, V, V, V, V, V, V], 
		[W, W, W, W, W, W, W, W], 
		[I, I, I, I, I, I, I, I], 
		[B, B, B, B, B, B, B, B],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	return rainbow1, rainbow2, rainbow3

def move_the_rainbow_vertically(rainbow0, rainbow1, rainbow2, rainbow3):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
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

def pibow_zero_rainbow_3():
	#print "pibow_zero_rainbow"
	rainbow0 = get_pibow_zero_vertical_rainbow()

	rainbow1, rainbow2, rainbow3 = get_vertical_rainbow()
		
	move_the_rainbow_vertically(rainbow0, rainbow1, rainbow2, rainbow3) 

def pibow_zero_rainbow_4():
	#print "pibow_zero_rainbow_2"
	rainbow0 = get_pibow_zero_vertical_rainbow()

	rainbow3, rainbow2, rainbow1 = get_vertical_rainbow()

	move_the_rainbow_vertically(rainbow0, rainbow1, rainbow2, rainbow3)

def get_diaginal_ripple_rainbow_1_or_3():
	
	ripple00 = [
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple01 = [
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple02 = [
		[V, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		[V, B, I2, W, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[V2, B, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		[V, B, I2, W, V, B, I, W], 
		[V, B, I, W2, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple04 = [
		[V, B2, I, W, V, B, I, W], 
		[V, B, I2, W, V, B, I, W], 
		[V, B, I, W2, V, B, I, W], 
		[V, B, I, W, V2, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[V, B, I2, W, V, B, I, W], 
		[V, B, I, W2, V, B, I, W], 
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W, V, B2, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[V, B, I, W2, V, B, I, W], 
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V, B, I2, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I, W2],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple08 = [
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple09 = [
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple10 = [
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]
	
	return ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, \
			ripple06, ripple07, ripple08, ripple09, ripple10

def get_diaginal_ripple_rainbow_2_or_4():

	ripple00 = [
		[V2, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple01 = [
		[V, B2, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W],  
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple02 = [
		[V, B, I2, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[V, B, I, W2, V, B, I, W], 
		[V, B, I2, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple04 = [
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W2, V, B, I, W], 
		[V, B, I2, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W],  
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W2, V, B, I, W], 
		[V, B, I2, W, V, B, I, W],  
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W2, V, B, I, W],  
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V2, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple08 = [
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B2, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple09 = [
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I2, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]	

	ripple10 = [
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W], 
		[V, B, I, W, V, B, I, W2], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	return ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, \
			ripple06, ripple07, ripple08, ripple09, ripple10

def ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, ripple02, ripple03, ripple04, ripple05,
		ripple06, ripple07, ripple08, ripple09, ripple10):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		unicornhat.set_pixels(rainbow)
		unicornhat.show()
		time.sleep(3.0)    
		unicornhat.set_pixels(ripple00)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple01)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple02)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple03)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple04)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple05)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple06)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple07)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple08)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple09)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple10)
		unicornhat.show()
		time.sleep(0.05)
	

def pibow_zero_ripple_1():
	#print "pibow_zero_ripple_1"
	rainbow = get_pibow_zero_horizontal_rainbow()
	
	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, \
	ripple07, ripple08, ripple09, ripple10 = get_diaginal_ripple_rainbow_1_or_3()
	
	ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06,
		ripple07, ripple08, ripple09, ripple10)

def pibow_zero_ripple_2():
	#print "pibow_zero_ripple_2"
	rainbow = get_pibow_zero_horizontal_rainbow()

	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, \
	ripple07, ripple08, ripple09, ripple10 = get_diaginal_ripple_rainbow_2_or_4()

	ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06,
		ripple07, ripple08, ripple09, ripple10)

def pibow_zero_ripple_3():
	#print "pibow_zero_ripple_3"
	rainbow = get_pibow_zero_horizontal_rainbow()

	ripple10, ripple09, ripple08, ripple07, ripple06, ripple05, ripple04, \
	ripple03, ripple02, ripple01, ripple00 = get_diaginal_ripple_rainbow_1_or_3()
	
	ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06,
		ripple07, ripple08, ripple09, ripple10)

def pibow_zero_ripple_4():
	#print "pibow_zero_ripple_4"
	rainbow = get_pibow_zero_horizontal_rainbow()

	ripple10, ripple09, ripple08, ripple07, ripple06, ripple05, ripple04, \
	ripple03, ripple02, ripple01, ripple00 = get_diaginal_ripple_rainbow_2_or_4()

	ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06,
		ripple07, ripple08, ripple09, ripple10)

def get_horizontal_ripple_rainbow():
	
	ripple00 = [
		[V2, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple01 = [
		[V, B2, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
]

	ripple02 = [
		[V, B, I2, W, V, B, I, W], 
		[V, B, I2, W, V, B, I, W], 
		[V, B, I2, W, V, B, I, W], 
		[V, B, I2, W, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[V, B, I, W2, V, B, I, W], 
		[V, B, I, W2, V, B, I, W], 
		[V, B, I, W2, V, B, I, W], 
		[V, B, I, W2, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
]

	ripple04 = [
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W, V2, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V, B2, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I2, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W2], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]
	
	return ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07

def ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		unicornhat.set_pixels(rainbow)
		unicornhat.show()
		time.sleep(3.0)    
		unicornhat.set_pixels(ripple00)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple01)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple02)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple03)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple04)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple05)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple06)
		unicornhat.show()
		time.sleep(0.05)
		unicornhat.set_pixels(ripple07)
		unicornhat.show()
		time.sleep(0.05)

def pibow_zero_ripple_5():
	#print "pibow_zero_ripple_5"
	rainbow = get_pibow_zero_horizontal_rainbow()

	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07 = get_horizontal_ripple_rainbow()

	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def pibow_zero_ripple_6():
	#print "pibow_zero_ripple_6"
	
	rainbow = get_pibow_zero_horizontal_rainbow()

	ripple07, ripple06, ripple05, ripple04, ripple03, ripple02, ripple01, ripple00 = get_horizontal_ripple_rainbow()
	
	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def get_double_ripple_rainbow_1_or_3():

	ripple00 = [
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V2, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
]

	ripple01 = [
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V, B2, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple02 = [
		[V, B, I2, W, V, B, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V, B, I2, W, V, B, I, W], 
		[V, B, I2, W, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[V, B, I, W2, V, B, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V, B, I, W2, V, B, I, W], 
		[V, B, I, W2, V, B, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple04 = [
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W, V2, B, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V, B, I, W, V2, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V, B2, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V, B, I, W, V, B2, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I2, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W2], 
		[V2, B2, I2, W2, V2, B2, I2, W2],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	return ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07
	
def get_double_ripple_rainbow_2_or_4():
	
	ripple00 = [
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W2], 
		[V, B, I, W, V, B, I, W2], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
]

	ripple01 = [
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I2, W], 
		[V, B, I, W, V, B, I2, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple02 = [
		[V, B, I, W, V, B2, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2],  
		[V, B, I, W, V, B2, I, W], 
		[V, B, I, W, V, B2, I, W],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[V, B, I, W, V2, B, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V, B, I, W, V2, B, I, W], 
		[V, B, I, W, V2, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple04 = [
		[V, B, I, W2, V, B, I, W], 
		[V, B, I, W2, V, B, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2],  
		[V, B, I, W2, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[V, B, I2, W, V, B, I, W], 
		[V, B, I2, W, V, B, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		[V, B, I2, W, V, B, I, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[V, B2, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		[V, B2, I, W, V, B, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[V2, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		[V2, B, I, W, V, B, I, W], 
		[V2, B2, I2, W2, V2, B2, I2, W2],  
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]
	
	return ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07

def pibow_zero_double_ripple_1():
	#print "pibow_zero_double_ripple_1"
	rainbow = get_pibow_zero_horizontal_rainbow()

	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07 = get_double_ripple_rainbow_1_or_3()
	
	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def pibow_zero_double_ripple_2():
	#print "pibow_zero_double_ripple_2"
	rainbow = get_pibow_zero_horizontal_rainbow()

	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07 = get_double_ripple_rainbow_2_or_4()
	
	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def pibow_zero_double_ripple_3():
	#print "pibow_zero_double_ripple_3"
	rainbow = get_pibow_zero_horizontal_rainbow()

	ripple07, ripple06, ripple05, ripple04, ripple03, ripple02, ripple01, ripple00 = get_double_ripple_rainbow_1_or_3()
	
	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def pibow_zero_double_ripple_4():
	#print "pibow_zero_double_ripple_4"
	rainbow = get_pibow_zero_horizontal_rainbow()

	ripple07, ripple06, ripple05, ripple04, ripple03, ripple02, ripple01, ripple00 = get_double_ripple_rainbow_2_or_4()
	
	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def random_x_coordinate():
    return int(random.choice(x_coordinates))

def random_y_coordinate():
    return int(random.choice(y_coordinates))

def get_random_color():
    color_tuple = random.choice(color_list) 
    return int(color_tuple[0]), int(color_tuple[1]), int(color_tuple[2])  

def light_up_random_led(r, g, b):
    unicornhat.set_pixel(random_x_coordinate(), random_y_coordinate(), r, g, b)

def pibow_zero_sprinkles():
	#print "pibow_zero_sprinkles"
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		# Turn on a random LED
		r, g, b = get_random_color()
		light_up_random_led(r, g, b)
		#Turn off a random LED
		unicornhat.set_pixel(random_x_coordinate(), random_y_coordinate(), 0, 0, 0)
		unicornhat.show()
		time.sleep(0.01)

def get_x_color(x_color_tuple): 
    return int(x_color_tuple[0]), int(x_color_tuple[1]), int(x_color_tuple[2])

def get_y_color(y_color_tuple): 
    return int(y_color_tuple[0]), int(y_color_tuple[1]), int(y_color_tuple[2])

def pibow_zero_horizontal_striper_1():
	#print "pibow_zero_horizontal_striper_1"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates
	
	pibow_zero_horizontal_striper(x_coordinate_list, y_coordinate_list)
	
def pibow_zero_horizontal_striper_2():
	#print "pibow_zero_horizontal_striper_2"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates[::-1]
	
	pibow_zero_horizontal_striper(x_coordinate_list, y_coordinate_list)

def pibow_zero_horizontal_striper_3():
	#print "pibow_zero_horizontal_striper_3"
	x_coordinate_list = x_coordinates[::-1]
	y_coordinate_list = y_coordinates
	
	pibow_zero_horizontal_striper(x_coordinate_list, y_coordinate_list)

def pibow_zero_horizontal_striper_4():
	#print "pibow_zero_horizontal_striper_4"
	x_coordinate_list = x_coordinates[::-1]
	y_coordinate_list = y_coordinates[::-1]
	
	pibow_zero_horizontal_striper(x_coordinate_list, y_coordinate_list)

def pibow_zero_horizontal_striper_5():
	#print "pibow_zero_horizontal_striper_5"
	x_coordinate_list = x_coordinates
	random.shuffle(x_coordinate_list)
	y_coordinate_list = y_coordinates
	
	pibow_zero_horizontal_striper_shuffle(x_coordinate_list, y_coordinate_list)
	
def pibow_zero_horizontal_striper_6():
	#print "pibow_zero_horizontal_striper_6"
	x_coordinate_list = x_coordinates
	random.shuffle(x_coordinate_list)
	y_coordinate_list = y_coordinates[::-1]
	
	pibow_zero_horizontal_striper_shuffle(x_coordinate_list, y_coordinate_list)


def pibow_zero_horizontal_striper_7():
	#print "pibow_zero_horizontal_striper_7"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates[::-1]
	
	pibow_zero_horizontal_striper_alternate(x_coordinate_list, y_coordinate_list)

def pibow_zero_horizontal_striper_8():
	#print "pibow_zero_horizontal_striper_8"
	x_coordinate_list = x_coordinates[::-1]
	y_coordinate_list = y_coordinates
	
	pibow_zero_horizontal_striper_alternate(x_coordinate_list, y_coordinate_list)

def pibow_zero_horizontal_striper_9():
	#print "pibow_zero_horizontal_striper_9"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates
	
	pibow_zero_horizontal_striper_shuffle_alternate(x_coordinate_list, y_coordinate_list)

def pibow_zero_horizontal_striper(x_coordinate_list, y_coordinate_list):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		unicornhat.clear()
		for x in x_coordinate_list:
			#Get the RGB color for the x coordinate
			if x == 0:
				r, g, b, = get_x_color(x0_color_tuple)
			if x == 1:
				r, g, b, = get_x_color(x1_color_tuple)
			if x == 2:
				r, g, b, = get_x_color(x2_color_tuple)
			if x == 3:
				r, g, b, = get_x_color(x3_color_tuple)
			if x == 4:
				r, g, b, = get_x_color(x4_color_tuple)
			if x == 5:
				r, g, b, = get_x_color(x5_color_tuple)
			if x == 6:
				r, g, b, = get_x_color(x6_color_tuple)
			if x == 7:
				r, g, b, = get_x_color(x7_color_tuple)						
			for y in y_coordinate_list:
				unicornhat.set_pixel(x, y, r, g, b)
				unicornhat.show()
				time.sleep(0.05)
		time.sleep(1.0)

def pibow_zero_horizontal_striper_shuffle(x_coordinate_list, y_coordinate_list):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		unicornhat.clear()
		random.shuffle(x_coordinate_list)
		for x in x_coordinate_list:
			#Get the RGB color for the x coordinate
			if x == 0:
				r, g, b, = get_x_color(x0_color_tuple)
			if x == 1:
				r, g, b, = get_x_color(x1_color_tuple)
			if x == 2:
				r, g, b, = get_x_color(x2_color_tuple)
			if x == 3:
				r, g, b, = get_x_color(x3_color_tuple)
			if x == 4:
				r, g, b, = get_x_color(x4_color_tuple)
			if x == 5:
				r, g, b, = get_x_color(x5_color_tuple)
			if x == 6:
				r, g, b, = get_x_color(x6_color_tuple)
			if x == 7:
				r, g, b, = get_x_color(x7_color_tuple)						
			for y in y_coordinate_list:
				unicornhat.set_pixel(x, y, r, g, b)
				unicornhat.show()
				time.sleep(0.05)
		time.sleep(1.0)

def pibow_zero_horizontal_striper_alternate(x_coordinate_list, y_coordinate_list):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		unicornhat.clear()
		for x in x_coordinate_list:
			#Get the RGB color for the x coordinate
			if x == 0:
				r, g, b, = get_x_color(x0_color_tuple)
			if x == 1:
				r, g, b, = get_x_color(x1_color_tuple)
			if x == 2:
				r, g, b, = get_x_color(x2_color_tuple)
			if x == 3:
				r, g, b, = get_x_color(x3_color_tuple)
			if x == 4:
				r, g, b, = get_x_color(x4_color_tuple)
			if x == 5:
				r, g, b, = get_x_color(x5_color_tuple)
			if x == 6:
				r, g, b, = get_x_color(x6_color_tuple)
			if x == 7:
				r, g, b, = get_x_color(x7_color_tuple)						
			# Light up selected x column, alternately
			if x_coordinate_list[x] == 0 or x_coordinate_list[x] == 2 or \
				x_coordinate_list[x] == 4 or x_coordinate_list[x] == 6:
				y_coordinate_list = y_coordinates
			else:
				y_coordinate_list = y_coordinates[::-1]
			for y in y_coordinate_list:
				unicornhat.set_pixel(x, y, r, g, b)
				unicornhat.show()
				time.sleep(0.05)
		time.sleep(1.0)

def pibow_zero_horizontal_striper_shuffle_alternate(x_coordinate_list, y_coordinate_list):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		unicornhat.clear()
		random.shuffle(x_coordinate_list)
		for x in x_coordinate_list:
			#Get the RGB color for the x coordinate
			if x == 0:
				r, g, b, = get_x_color(x0_color_tuple)
			if x == 1:
				r, g, b, = get_x_color(x1_color_tuple)
			if x == 2:
				r, g, b, = get_x_color(x2_color_tuple)
			if x == 3:
				r, g, b, = get_x_color(x3_color_tuple)
			if x == 4:
				r, g, b, = get_x_color(x4_color_tuple)
			if x == 5:
				r, g, b, = get_x_color(x5_color_tuple)
			if x == 6:
				r, g, b, = get_x_color(x6_color_tuple)
			if x == 7:
				r, g, b, = get_x_color(x7_color_tuple)
			# Light up selected x column, alternately
			if x_coordinate_list[x] == 0 or x_coordinate_list[x] == 2 or \
				x_coordinate_list[x] == 4 or x_coordinate_list[x] == 6:
				y_coordinate_list = y_coordinates
			else:
				y_coordinate_list = y_coordinates[::-1]						
			for y in y_coordinate_list:
				unicornhat.set_pixel(x, y, r, g, b)
				unicornhat.show()
				time.sleep(0.05)
		time.sleep(1.0)

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
				 pibow_zero_rainbow, pibow_zero_rainbow_2, pibow_zero_rainbow_3, pibow_zero_rainbow_4,
				 pibow_zero_ripple_1, pibow_zero_ripple_2, pibow_zero_ripple_3, pibow_zero_ripple_4, 
				 pibow_zero_ripple_5, pibow_zero_ripple_6, pibow_zero_double_ripple_1, pibow_zero_double_ripple_2, 
				 pibow_zero_double_ripple_3, pibow_zero_double_ripple_4, pibow_zero_sprinkles, 
				 pibow_zero_horizontal_striper_1, pibow_zero_horizontal_striper_2, pibow_zero_horizontal_striper_3, pibow_zero_horizontal_striper_4, 
				 pibow_zero_horizontal_striper_5, pibow_zero_horizontal_striper_6, pibow_zero_horizontal_striper_7, pibow_zero_horizontal_striper_8, 
				 pibow_zero_horizontal_striper_9, pibow_zero_vertical_striper_1, pibow_zero_vertical_striper_2, pibow_zero_vertical_striper_3, 
				 pibow_zero_vertical_striper_4
]

def main():
	while True:
	    random.choice(function_list)()
	
if __name__ == '__main__':
    main()
