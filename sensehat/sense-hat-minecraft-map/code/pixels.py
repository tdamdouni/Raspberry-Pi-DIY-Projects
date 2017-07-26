from sense_hat import SenseHat
from time import sleep

sense  = SenseHat()

sense.clear()

# colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

colours = [white, red, white, green, white, blue, white, yellow]

sense.clear()
for y in range(8):
    colour = colours[y]
    for x in range(8):
        sense.set_pixel(x, y, colour)
        sleep(0.1)

r = red
b = blue

pixels = [
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
]

sense.set_pixels(pixels)
