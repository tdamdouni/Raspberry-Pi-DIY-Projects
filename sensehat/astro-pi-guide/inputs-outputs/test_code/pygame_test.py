#!/usr/bin/python
from sense_hat import SenseHat
import os
import time
import pygame  # See http://www.pygame.org/docs
from pygame.locals import *


print("Press Escape to quit")
time.sleep(1)

pygame.init()
pygame.display.set_mode((640, 480))

sense = SenseHat()
sense.clear()  # Blank the LED matrix
sense.set_rotation(270)  # Flight orientation

# 0, 0 = Top left
# 7, 7 = Bottom right
UP_PIXELS = [[3, 0], [4, 0]]
DOWN_PIXELS = [[3, 7], [4, 7]]
LEFT_PIXELS = [[0, 3], [0, 4]]
RIGHT_PIXELS = [[7, 3], [7, 4]]
CENTRE_PIXELS = [[3, 3], [4, 3], [3, 4], [4, 4]]


def set_pixels(pixels, col):
    for p in pixels:
        sense.set_pixel(p[0], p[1], col[0], col[1], col[2])


# Joystick is turned 90 degrees clockwise for flight orientation
def handle_event(event, colour):
    if event.key == pygame.K_DOWN:
        set_pixels(LEFT_PIXELS, colour)
    elif event.key == pygame.K_UP:
        set_pixels(RIGHT_PIXELS, colour)
    elif event.key == pygame.K_LEFT:
        set_pixels(UP_PIXELS, colour)
    elif event.key == pygame.K_RIGHT:
        set_pixels(DOWN_PIXELS, colour)
    elif event.key == pygame.K_RETURN:
        set_pixels(CENTRE_PIXELS, colour)
    elif event.key == pygame.K_u:
        sense.show_letter("u", colour)
    elif event.key == pygame.K_d:
        sense.show_letter("d", colour)
    elif event.key == pygame.K_l:
        sense.show_letter("l", colour)
    elif event.key == pygame.K_r:
        sense.show_letter("r", colour)
    elif event.key == pygame.K_a:
        sense.show_letter("a", colour)
    elif event.key == pygame.K_b:
        sense.show_letter("b", colour)


running = True

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            handle_event(event, WHITE)
        if event.type == KEYUP:
            handle_event(event, BLACK)
