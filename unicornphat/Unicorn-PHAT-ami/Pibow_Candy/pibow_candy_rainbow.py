#!/usr/bin/env python
################################################################
#                  Pibow Candy Rainbow                         #
################################################################
# Description:                                                 #
# This is a modification of my Moving Rainbow program. I just  #
# changed the colors to pastels to match the Pibow Candy case. #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
import unicornhat, signal, time, random
unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

def pibow_candy_rainbow():
	
	R = (255, 105, 97)
	O = (255, 179, 71)
	Y = (253, 253, 150)
	G = (119, 190, 119)
	B = (119, 158, 203)
	I = (150, 111, 214)
	V = (203, 153, 201)
	W = (244, 154, 194)
	off = (0, 0, 0)

	rainbow0 = [
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

def main():
	while True:
	    pibow_candy_rainbow()
	
if __name__ == '__main__':
    main()
