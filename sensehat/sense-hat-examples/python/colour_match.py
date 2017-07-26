from sense_hat import SenseHat
from random import randint
import pygame
import pygame.locals as pgl
from time import sleep

STEP = 10

def random_colour():
    r = randint(0, int(255 / STEP)) * STEP
    g = randint(0, int(255 / STEP)) * STEP
    b = randint(0, int(255 / STEP)) * STEP
    return (r, g, b)

def set_centre_square(colour):
    centre_pixels = [(3, 3), (3, 4), (4, 3), (4, 4)]
    for x, y in centre_pixels:
        sense.set_pixel(x, y, colour)

def handle_event(event):
    global colour
    r, g, b = colour

    if event.key == pgl.K_r:
        if r < (255 - STEP):
            r += STEP
    elif event.key == pgl.K_t:
        if r >= STEP:
            r -= STEP
    elif event.key == pgl.K_g:
        if g < (255 - STEP):
            g += STEP
    elif event.key == pgl.K_h:
        if g >= STEP:
            g -= STEP
    elif event.key == pgl.K_b:
        if b < (255 - STEP):
            b += STEP
    elif event.key == pgl.K_n:
        if b >= STEP:
            b -= STEP

    colour = (r, g, b)
    set_centre_square(colour)

sense = SenseHat()

pygame.init()
pygame.display.set_mode((640, 480))

target_colour = random_colour()
initial_colour = random_colour()

sense.clear(target_colour)
set_centre_square(initial_colour)

colour = initial_colour

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pgl.KEYDOWN:
            if event.key == pgl.K_ESCAPE:
                running = False
            else:
                handle_event(event)

    if colour == target_colour:
        running = False
        print("Well done")

if colour != target_colour:
    diff = tuple(c - t for c, t in zip(colour, target_colour))
    print("Aiming for (%4.0f, %4.0f, %4.0f)" % target_colour)
    print("You got    (%4.0f, %4.0f, %4.0f)" % colour)
    print("Difference (%4.0f, %4.0f, %4.0f)" % diff)
    print("Out by %i" % sum(abs(n) for n in diff))
