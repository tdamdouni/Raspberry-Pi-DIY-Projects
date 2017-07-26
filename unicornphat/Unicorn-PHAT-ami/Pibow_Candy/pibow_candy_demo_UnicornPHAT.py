#!/usr/bin/env python
################################################################
#          Pibow Candy Demo for the Unicorn pHAT               #
################################################################
# Description:                                                 #
# This program is a collection of all my Pibow Candy programs. #
# It picks one at random and runs it for 15 seconds.           #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

import unicornhat, signal, time, random
unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

R = (255, 105, 97)
O = (255, 179, 71)
Y = (253, 253, 150)
G = (119, 190, 119)
B = (119, 158, 203)
I = (150, 111, 214)
V = (203, 153, 201)
W = (244, 154, 194)
off = (0, 0, 0)
R2 = (128, 53, 49)
O2 = (128, 90, 36)
Y2 = (127, 127, 75)
G2 = (60, 95, 60)
B2 = (60, 79, 102)
I2 = (75, 56, 107)
V2 = (102, 77, 101)
W2 = (122, 77, 97)

color_list = [
    (255, 105, 97), (255, 179, 71), (253, 253, 150), (119, 190, 119), 
    (119, 158, 203), (150, 111, 214), (203, 153, 201), (244, 154, 194)
]
    
y_coordinates = [0, 1, 2, 3]
x_coordinates = [0, 1, 2, 3, 4, 5, 6, 7]

x0_color_tuple  = (255, 105, 97)
x1_color_tuple  = (255, 179, 71)
x2_color_tuple  = (253, 253, 150)
x3_color_tuple  = (119, 190, 119)
x4_color_tuple  = (119, 158, 203)
x5_color_tuple  = (150, 111, 214)
x6_color_tuple  = (203, 153, 201)
x7_color_tuple  = (244, 154, 194)

def get_pibow_candy_rainbow():
	
	rainbow = [
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]
	
	return rainbow

def move_the_rainbow(rainbow0, rainbow1, rainbow2, rainbow3, rainbow4, rainbow5,
		rainbow6, rainbow7):
	
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
		unicornhat.set_pixels(rainbow4)
		unicornhat.show()
		time.sleep(0.5)
		unicornhat.set_pixels(rainbow5)
		unicornhat.show()
		time.sleep(0.5)
		unicornhat.set_pixels(rainbow6)
		unicornhat.show()
		time.sleep(0.5)
		unicornhat.set_pixels(rainbow7)
		unicornhat.show()
		time.sleep(0.5)

def pibow_candy_rainbow():
	#print "pibow_candy_rainbow"
	rainbow0 = get_pibow_candy_rainbow()

	rainbow1 = [
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow2 = [
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow3 = [
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow4 = [
		[B, I, V, W, R, O, Y, G], 
		[B, I, V, W, R, O, Y, G], 
		[B, I, V, W, R, O, Y, G], 
		[B, I, V, W, R, O, Y, G], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow5 = [
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow6 = [
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow7 = [
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]
		
	move_the_rainbow(rainbow0, rainbow1, rainbow2, rainbow3, rainbow4, rainbow5,
		rainbow6, rainbow7)

def pibow_candy_rainbow_2():
	#print "pibow_candy_rainbow_2"
	rainbow0 = get_pibow_candy_rainbow()

	rainbow1 = [
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		[W, R, O, Y, G, B, I, V], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow2 = [
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		[V, W, R, O, Y, G, B, I], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow3 = [
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B], 
		[I, V, W, R, O, Y, G, B],
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow4 = [
		[B, I, V, W, R, O, Y, G], 
		[B, I, V, W, R, O, Y, G], 
		[B, I, V, W, R, O, Y, G], 
		[B, I, V, W, R, O, Y, G], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow5 = [
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		[G, B, I, V, W, R, O, Y], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow6 = [
		[Y, G, B, I, V, W, R, O],
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O], 
		[Y, G, B, I, V, W, R, O], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	rainbow7 = [
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		[O, Y, G, B, I, V, W, R], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	move_the_rainbow(rainbow0, rainbow1, rainbow2, rainbow3, rainbow4, rainbow5,
		rainbow6, rainbow7)

def get_diaginal_ripple_rainbow_1_or_3():
	
	ripple00 = [
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple01 = [
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple02 = [
		[R, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[R2, O, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple04 = [
		[R, O2, Y, G, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[R, O, Y2, G, B, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G, B, I2, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B, I, V2, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V, W2], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple08 = [
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple09 = [
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple10 = [
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
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
		[R2, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple01 = [
		[R, O2, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple02 = [
		[R, O, Y2, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple04 = [
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple08 = [
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I2, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple09 = [
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V2, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]	

	ripple10 = [
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W], 
		[R, O, Y, G, B, I, V, W2], 
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
	

def pibow_candy_ripple_1():
	#print "pibow_candy_ripple_1"
	rainbow = get_pibow_candy_rainbow()
	
	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, \
	ripple07, ripple08, ripple09, ripple10 = get_diaginal_ripple_rainbow_1_or_3()
	
	ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06,
		ripple07, ripple08, ripple09, ripple10)

def pibow_candy_ripple_2():
	#print "pibow_candy_ripple_2"
	rainbow = get_pibow_candy_rainbow()

	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, \
	ripple07, ripple08, ripple09, ripple10 = get_diaginal_ripple_rainbow_2_or_4()

	ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06,
		ripple07, ripple08, ripple09, ripple10)

def pibow_candy_ripple_3():
	#print "pibow_candy_ripple_3"
	rainbow = get_pibow_candy_rainbow()

	ripple10, ripple09, ripple08, ripple07, ripple06, ripple05, ripple04, \
	ripple03, ripple02, ripple01, ripple00 = get_diaginal_ripple_rainbow_1_or_3()
	
	ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06,
		ripple07, ripple08, ripple09, ripple10)

def pibow_candy_ripple_4():
	#print "pibow_candy_ripple_4"
	rainbow = get_pibow_candy_rainbow()

	ripple10, ripple09, ripple08, ripple07, ripple06, ripple05, ripple04, \
	ripple03, ripple02, ripple01, ripple00 = get_diaginal_ripple_rainbow_2_or_4()

	ripple_the_rainbow_diagonally(rainbow, ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06,
		ripple07, ripple08, ripple09, ripple10)

def get_horizontal_ripple_rainbow():
	
	ripple00 = [
		[R2, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple01 = [
		[R, O2, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
]

	ripple02 = [
		[R, O, Y2, G, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
]

	ripple04 = [
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B, I2, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V2, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W2], 
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

def pibow_candy_ripple_5():
	#print "pibow_candy_ripple_5"
	rainbow = get_pibow_candy_rainbow()

	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07 = get_horizontal_ripple_rainbow()

	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def pibow_candy_ripple_6():
	#print "pibow_candy_ripple_6"
	
	rainbow = get_pibow_candy_rainbow()

	ripple07, ripple06, ripple05, ripple04, ripple03, ripple02, ripple01, ripple00 = get_horizontal_ripple_rainbow()
	
	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def get_double_ripple_rainbow_1_or_3():

	ripple00 = [
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		[R2, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
]

	ripple01 = [
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		[R, O2, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple02 = [
		[R, O, Y2, G, B, I, V, W], 
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		[R, O, Y2, G, B, I, V, W], 
		[R, O, Y2, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[R, O, Y, G2, B, I, V, W], 
		[R2, O2, Y2, G2, B2, I2, V2, W2],  
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple04 = [
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		[R, O, Y, G, B2, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B, I2, V, W],  
		[R2, O2, Y2, G2, B2, I, V2, W2],
		[R, O, Y, G, B, I2, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V2, W], 
		[R2, O2, Y2, G2, B2, I, V2, W2], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W2], 
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	return ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07
	
def get_double_ripple_rainbow_2_or_4():
	
	ripple00 = [
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W2], 
		[R, O, Y, G, B, I, V, W2], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
]

	ripple01 = [
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V2, W], 
		[R, O, Y, G, B, I, V2, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple02 = [
		[R, O, Y, G, B, I2, V, W], 
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		[R, O, Y, G, B, I2, V, W], 
		[R, O, Y, G, B, I2, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple03 = [
		[R, O, Y, G, B2, I, V, W], 
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		[R, O, Y, G, B2, I, V, W], 
		[R, O, Y, G, B2, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple04 = [
		[R, O, Y, G2, B, I, V, W], 
		[R, O, Y, G2, B, I, V, W], 
		[R2, O2, Y2, G2, B2, I2, V2, W2],
		[R, O, Y, G2, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple05 = [
		[R, O, Y2, G, B, I, V, W], 
		[R, O, Y2, G, B2, I, V, W], 
		[R2, O2, Y2, G2, B2, I2, V2, W2],
		[R, O, Y2, G, B, I, V, W], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple06 = [
		[R, O2, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W], 
		[R, O2, Y, G, B, I, V, W],  
		[R2, O2, Y2, G2, B2, I2, V2, W2], 
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]

	ripple07 = [
		[R2, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		[R2, O, Y, G, B, I, V, W], 
		[R2, O2, Y2, G2, B2, I2, V2, W2],  
		# Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
		[off, off, off, off,off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off], 
		[off, off, off, off, off, off, off, off]
	]
	
	return ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07

def pibow_candy_double_ripple_1():
	#print "pibow_candy_double_ripple_1"
	rainbow = get_pibow_candy_rainbow()

	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07 = get_double_ripple_rainbow_1_or_3()
	
	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def pibow_candy_double_ripple_2():
	#print "pibow_candy_double_ripple_2"
	rainbow = get_pibow_candy_rainbow()

	ripple00, ripple01, ripple02, ripple03, ripple04, ripple05, ripple06, ripple07 = get_double_ripple_rainbow_2_or_4()
	
	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def pibow_candy_double_ripple_3():
	#print "pibow_candy_double_ripple_3"
	rainbow = get_pibow_candy_rainbow()

	ripple07, ripple06, ripple05, ripple04, ripple03, ripple02, ripple01, ripple00 = get_double_ripple_rainbow_1_or_3()
	
	ripple_the_rainbow_horinzontally(rainbow, ripple00, ripple01, ripple02, ripple03, 
		ripple04, ripple05, ripple06, ripple07)

def pibow_candy_double_ripple_4():
	#print "pibow_candy_double_ripple_4"
	rainbow = get_pibow_candy_rainbow()

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

def pibow_candy_sprinkles():
	#print "pibow_candy_sprinkles"
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

def get_color(x_color_tuple): 
    return int(x_color_tuple[0]), int(x_color_tuple[1]), int(x_color_tuple[2]) 

def pibow_candy_striper_1():
	#print "pibow_candy_striper_1"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates
	
	pibow_candy_striper(x_coordinate_list, y_coordinate_list)
	
def pibow_candy_striper_2():
	#print "pibow_candy_striper_2"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates[::-1]
	
	pibow_candy_striper(x_coordinate_list, y_coordinate_list)

def pibow_candy_striper_3():
	#print "pibow_candy_striper_3"
	x_coordinate_list = x_coordinates[::-1]
	y_coordinate_list = y_coordinates
	
	pibow_candy_striper(x_coordinate_list, y_coordinate_list)

def pibow_candy_striper_4():
	#print "pibow_candy_striper_4"
	x_coordinate_list = x_coordinates[::-1]
	y_coordinate_list = y_coordinates[::-1]
	
	pibow_candy_striper(x_coordinate_list, y_coordinate_list)

def pibow_candy_striper_5():
	#print "pibow_candy_striper_5"
	x_coordinate_list = x_coordinates
	random.shuffle(x_coordinate_list)
	y_coordinate_list = y_coordinates
	
	pibow_candy_striper_shuffle(x_coordinate_list, y_coordinate_list)
	
def pibow_candy_striper_6():
	#print "pibow_candy_striper_6"
	x_coordinate_list = x_coordinates
	random.shuffle(x_coordinate_list)
	y_coordinate_list = y_coordinates[::-1]
	
	pibow_candy_striper_shuffle(x_coordinate_list, y_coordinate_list)


def pibow_candy_striper_7():
	#print "pibow_candy_striper_7"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates[::-1]
	
	pibow_candy_striper_alternate(x_coordinate_list, y_coordinate_list)

def pibow_candy_striper_8():
	#print "pibow_candy_striper_8"
	x_coordinate_list = x_coordinates[::-1]
	y_coordinate_list = y_coordinates
	
	pibow_candy_striper_alternate(x_coordinate_list, y_coordinate_list)

def pibow_candy_striper_9():
	#print "pibow_candy_striper_9"
	x_coordinate_list = x_coordinates
	y_coordinate_list = y_coordinates
	
	pibow_candy_striper_shuffle_alternate(x_coordinate_list, y_coordinate_list)

def pibow_candy_striper(x_coordinate_list, y_coordinate_list):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		unicornhat.clear()
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
			for y in y_coordinate_list:
				unicornhat.set_pixel(x, y, r, g, b)
				unicornhat.show()
				time.sleep(0.05)
		time.sleep(1.0)

def pibow_candy_striper_shuffle(x_coordinate_list, y_coordinate_list):
	
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
			for y in y_coordinate_list:
				unicornhat.set_pixel(x, y, r, g, b)
				unicornhat.show()
				time.sleep(0.05)
		time.sleep(1.0)

def pibow_candy_striper_alternate(x_coordinate_list, y_coordinate_list):
	
	start_time = time.time()
	time.clock()
	seconds_elapsed = 0
	
	while seconds_elapsed < 15:
		seconds_elapsed = time.time() - start_time
		unicornhat.clear()
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

def pibow_candy_striper_shuffle_alternate(x_coordinate_list, y_coordinate_list):
	
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

function_list = [
				 pibow_candy_rainbow, pibow_candy_rainbow_2, pibow_candy_ripple_1, pibow_candy_ripple_2, 
				 pibow_candy_ripple_3, pibow_candy_ripple_4, pibow_candy_ripple_5, pibow_candy_ripple_6,
				 pibow_candy_double_ripple_1, pibow_candy_double_ripple_2, pibow_candy_double_ripple_3,
				 pibow_candy_double_ripple_4, pibow_candy_sprinkles, pibow_candy_striper_1, pibow_candy_striper_2, 
				 pibow_candy_striper_3, pibow_candy_striper_4, pibow_candy_striper_5, pibow_candy_striper_6, 
				 pibow_candy_striper_7, pibow_candy_striper_8, pibow_candy_striper_9
]

def main():
	while True:
	    random.choice(function_list)()
	
if __name__ == '__main__':
    main()
