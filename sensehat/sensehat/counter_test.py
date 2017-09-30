from smallhex import to_hex_chars, to_dec_chars, two_chars
from time import sleep
from sense_hat import SenseHat

sense=SenseHat()
sense.set_pixels( two_chars("Hi") )
for rot in range(0,360,90):
	sense.set_rotation(rot)
	sleep(0.25)

sense.set_rotation(180)

for count in range(256):
	sense.set_pixels( to_hex_chars(count) )
	sleep(0.1)
for count in range(100):
	sense.set_pixels( to_dec_chars(count) )
	sleep(0.1)
	
