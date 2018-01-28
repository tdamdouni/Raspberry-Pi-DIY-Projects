import time
from PIL import Image
import pianohat
import unicornhathd

SPRITE_W = 16
SPRITE_H = 16

# Map the white piano keys to the 8 sprites
map = [0,2,4,5,7,9,11,12]

img = Image.open('unicorn-sprite-switch.png')

def display_sprite(source, sprite, frame):
    image_width, image_height = source.size

    num_sprites = image_width / SPRITE_W
    num_frames = image_height / SPRITE_H

    offset_x = (sprite % num_sprites) * SPRITE_W
    offset_y = (frame % num_frames) * SPRITE_H

    width, height = unicornhathd.get_shape()

    for x in range(width):
        for y in range(height):
            pixel = source.getpixel((offset_x + x, offset_y + y))
            r, g, b, alpha = [int(p) for p in pixel]
            if alpha > 0:
                unicornhathd.set_pixel(x, y, r, g, b)
            else:
                unicornhathd.set_pixel(x, y, 0, 0, 0)

    unicornhathd.show()

def handle_touch(ch, evt):
    global sprite
    if ch in map:
        sprite = map.index(ch)

pianohat.on_note(handle_touch)

frame = 0
sprite = 0
while True:
    frame += 1
    display_sprite(img, sprite, frame)
    time.sleep(1.0/5)