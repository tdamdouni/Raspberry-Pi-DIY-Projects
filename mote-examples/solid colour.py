# Adapted from blinkt example
import time
from mote import Mote

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

try:
    
    step = 0

    def set_all(r,g,b):
        for x in range(16):
            mote.set_pixel(1,x,r,g,b)

    while True:
        if step == 0:
            set_all(128,0,0)
        if step == 1:
            set_all(0,128,0)
        if step == 2:
            set_all(0,0,128)

        step+=1
        step%=3
        time.sleep(0.5)
        mote.show()
    


except KeyboardInterrupt:
	mote.clear()
	mote.show()
	quit()
