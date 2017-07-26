# http://forums.pimoroni.com/t/addressing-pixels-of-unicorn-phat-wierdness/2226/2

import unicornhat as uh
uh.set_layout(uh.PHAT)
uh.brightness(0.5)

uh.set_pixel(0,0,255,0,0) # red - top left
uh.set_pixel(7,0,0,255,0) # green - top right
uh.set_pixel(0,3,0,0,255) # blue - bottom left
uh.set_pixel(7,3,255,255,0) # yellow - bottom right

uh.show()