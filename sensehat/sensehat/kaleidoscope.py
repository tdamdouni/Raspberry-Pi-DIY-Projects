import random
from time import sleep

from sense_hat import SenseHat

sense=SenseHat()
sense.clear()

def fade( pixel ):
	new_pixel=[]
	for comp in pixel:
		if comp>0:
			new_pixel.append( comp-1)
		else:
			new_pixel.append( 0 )
	return new_pixel
	

while True:
	rx=random.randint(0,3)
	ry=random.randint(0,3)
	if random.randint(0,100) < 25:
		col=[	random.randint(0,255),
			random.randint(0,255),
			random.randint(0,255)
		]
		if sense.get_pixel(rx,ry)==[0,0,0]:
			sense.set_pixel(rx, ry, col)	
			sense.set_pixel(7-rx, ry, col)
			sense.set_pixel(7-rx, 7-ry, col)
			sense.set_pixel(rx, 7-ry, col)
	pixels=sense.get_pixels()	
	new_pixels=[]
	for p in pixels:
		new_pixels.append( fade( p ) )
	sense.set_pixels( new_pixels )
	#sleep(0.1)
