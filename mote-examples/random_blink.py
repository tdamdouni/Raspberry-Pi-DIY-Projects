# Adapted from blinkt example
import random
import time
from mote import Mote

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

try:
    while True:
        for channel in range(4):
            pixels = random.sample(range(16), random.randint(1, 5))
            for i in range(16):
                if i in pixels:
                    mote.set_pixel(channel+1,i, random.randint(0,255), random.randint(0,255), random.randint(0,255))
                else:
                    mote.set_pixel(channel+1,i, 0, 0, 0)
            mote.show()
        time.sleep(0.05)


except KeyboardInterrupt:
	mote.clear()
	mote.show()
	quit()
