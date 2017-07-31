# set up unicorn pHAT
import unicornhat as unicorn
from time import sleep

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()


for x in range(width):
    for y in range(height):
        unicorn.set_pixel(x, y, 0, 255, 255)
unicorn.show()

while True:
    sleep(1)
