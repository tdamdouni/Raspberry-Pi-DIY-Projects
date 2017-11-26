from rrb3 import *
from random import randint

rr = RRB3(12, 12) # Battery voltage 12V, motor 12V

T = 20  # 20 seconds to extend

extended = False

try:
	while True:
		if rr.get_distance() < 20:
			if extended:  # if extended retract and vice versa
				print("retracting")
				rr.set_led1(True)  # LED 1 on
				rr.reverse(T, 1.0)
				rr.set_led1(False)
				extended = False
			else:
				print("extending")
				rr.set_led2(True)
				rr.forward(T, 1.0)
				rr.set_led2(False)
				extended = True
			print("done")
finally:
	rr.cleanup() # Set all GPIO pins to safe input state