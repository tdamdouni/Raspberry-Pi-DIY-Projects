from mcpi import minecraft
from sense_hat import SenseHat
from time import sleep

def get_blocks(size):
    global known_blocks

    x, y, z = mc.player.getTilePos()
    y -= 1
    n0 = (size - 1) / 2
    n1 = ((size + 1) / 2)
    if size % 2 == 0:
        n1 += 1

    blocks = []
    for dx in range(x-n0, x+n1):
        for dz in range(z-n0, z+n1):
            b = (dx, dz)
            try:
                block = known_blocks[b]
            except KeyError:
                block = mc.getBlock(dx, y+0, dz)
                known_blocks[b] = block
            blocks.append(block)

    return blocks

def lookup_colour(block):
    if block in colours:
        return colours[block]
    else:
        return white

def map_blocks_to_colours(blocks):
    return [lookup_colour(block) for block in blocks]

mc = minecraft.Minecraft.create()
sense = SenseHat()

known_blocks = {}

# blocks
air = 0
grass = 2
water = 9
sand = 12

# colours
white = (150, 150, 150)
green = (0, 150, 0)
blue = (0, 0, 150)
yellow = (150, 150, 0)
black = (0, 0, 0)

# block: colour
colours = {
    air: white,
    grass: green,
    water: blue,
    sand: yellow,
}

player_pos = 27

while True:
    blocks = get_blocks(8)
    pixels = map_blocks_to_colours(blocks)
    pixels[player_pos] = black  # denote player as black pixel
    sense.set_pixels(pixels)
