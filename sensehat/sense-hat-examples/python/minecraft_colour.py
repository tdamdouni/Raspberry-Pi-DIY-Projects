from mcpi import minecraft
from sense_hat import SenseHat
from time import sleep

mc = minecraft.Minecraft.create()
sense = SenseHat()

# blocks
air = 0
grass = 2
water = 9
sand = 12

# colours
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# block: colour
colours = {
    air: white,
    grass: green,
    water: blue,
    sand: yellow
}

while True:
    x, y, z = mc.player.getTilePos()
    block = mc.getBlock(x, y-1, z)
    if block in colours:
        colour = colours[block]
        sense.clear(colour)
    sleep(0.1)
