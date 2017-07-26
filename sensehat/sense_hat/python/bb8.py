# Display animated BB-8 character using LED matrix display on Sense HAT
# MJ Legg 29/11/15

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(r=180)

# Set up colours
w = [255,255,255]
b = [0,0,0]
o = [243,145,27]
g = [77,69,62]

# Set up sprites
sprite_b = [[b,b,b,b,b,b,b,b],
            [b,b,b,b,b,b,b,b],
            [b,b,b,b,b,b,b,b],
            [b,b,b,b,b,b,b,b],
            [b,b,b,b,b,b,b,b],
            [b,b,b,b,b,b,b,b],
            [b,b,b,b,b,b,b,b],
            [b,b,b,b,b,b,b,b]]

sprite_0 = [[b,b,b,w,w,b,b,b],
            [b,b,w,g,w,w,b,b],
            [b,b,b,w,w,b,b,b],
            [b,b,o,w,w,w,b,b],
            [b,o,g,o,w,o,w,b],
            [b,w,o,w,o,g,o,b],
            [b,b,w,w,w,o,b,b],
            [b,b,b,w,w,b,b,b]]

sprite_1 = [[b,b,b,w,w,b,b,b],
            [b,b,w,g,w,w,b,b],
            [b,b,b,w,w,b,b,b],
            [b,b,w,w,w,o,b,b],
            [b,w,o,w,o,g,o,b],
            [b,o,g,o,w,o,w,b],
            [b,b,o,w,w,w,b,b],
            [b,b,b,w,w,b,b,b]]

sprite_2 = [[b,b,b,w,w,b,b,b],
            [b,b,w,g,w,w,b,b],
            [b,b,b,w,o,b,b,b],
            [b,b,w,o,g,o,b,b],
            [b,w,w,w,o,w,w,b],
            [b,w,w,o,w,w,w,b],
            [b,b,o,g,o,w,b,b],
            [b,b,b,o,w,b,b,b]]

sprite_3 = [[b,b,b,w,w,b,b,b],
            [b,b,w,g,w,w,b,b],
            [b,b,b,o,w,b,b,b],
            [b,b,o,g,o,w,b,b],
            [b,w,w,o,w,w,w,b],
            [b,w,w,w,o,w,w,b],
            [b,b,w,o,g,o,b,b],
            [b,b,b,w,o,b,b,b]]

# Join two blank sprites with character sprite in middle
def combine_sprite(sprite, black_sprite=sprite_b):
    combine = [black_sprite[i] + sprite[i] + black_sprite[i] for i in range(len(sprite))]
    return flatten_array(combine)

# Flatten nested lists
def flatten_array(array):
    return [v for i in array for v in i]

# Reverse pixels in sprite
def reverse_sprite(sprite):
    return [i[::-1] for i in sprite]

# Take a 8x8 slice from sprite at given point
def slice_sprite(sprite, start):
    pixels = 192
    pixel_width = 24
    sprite_width = 8
    slice_range = [range(i,i+sprite_width) for i in range(start,pixels,pixel_width)]
    flat_range = flatten_array(slice_range)
    return [sprite[i] for i in flat_range]

# Left scroll through sequence of sprites
def scroll_left(sprites, scroll_start, scroll_stop):
    sprite_sequence = [i for i in range(4)]*4
    slice_starts = [(i,v) for i,v in enumerate(sprite_sequence)]
    slice_selection = slice_starts[scroll_start:scroll_stop]
    for i,v in slice_selection:
        sense.set_pixels(slice_sprite(sprites[v],i))
        time.sleep(0.1)

# Right scroll through sequence of sprites
def scroll_right(sprites, scroll_start, scroll_stop):
    sprite_sequence = [i for i in range(4)]*4
    slice_starts = [(i,v) for i,v in enumerate(sprite_sequence[::-1])]
    slice_selection = slice_starts[scroll_start:scroll_stop]
    slice_selection_reverse = slice_selection[::-1]
    for i,v in slice_selection_reverse:
        sense.set_pixels(slice_sprite(sprites[v],i))
        time.sleep(0.1)

# Animate through sequence of sprites
def animate(sprites):
    for i,v in enumerate(sprites):
        sense.set_pixels(slice_sprite(sprites[i],8))
        time.sleep(0.1)

sprites = [sprite_0,sprite_1,sprite_2,sprite_3]
rev_sprites = [reverse_sprite(i) for i in sprites]
padded_sprites = [combine_sprite(i) for i in sprites]
padded_rev_sprites = [combine_sprite(i) for i in rev_sprites]

# Enter from stage right
scroll_left(padded_sprites,0,9)

# Animate sprite in reaction to accelerometer movement
while True:
    x, y, z = sense.get_accelerometer_raw().values()
    if y > 0.1 and y < 0.3:
        animate(padded_sprites)
    elif y > 0.3:
        scroll_left(padded_sprites,9,16)
        scroll_left(padded_sprites,0,9)
    elif y < -0.1 and y > -0.3:
        animate(padded_rev_sprites)
    elif y < -0.3:
        scroll_right(padded_rev_sprites,0,9)
        scroll_right(padded_rev_sprites,8,16)

