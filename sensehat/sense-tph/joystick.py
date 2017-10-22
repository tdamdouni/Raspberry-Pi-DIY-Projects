from sense_hat import AstroPi
import time
import datetime
import pygame
from pygame.locals import *

ap = AstroPi()
ap.clear()
ap.set_rotation(180)

pygame.init()
pygame.display.set_mode((640,480))


pressure = 'P: ' + str(int(ap.get_pressure()))
temp =  'T: ' + str(int(ap.get_temperature_from_pressure()))
humidity = 'H: ' + str(int(ap.get_humidity()))
blah = 'blah!'

def handle_event(event):
    if event.key == pygame.K_DOWN:
        ap.show_message(pressure)
    elif event.key == pygame.K_UP:
        ap.show_message(temp)
    elif event.key == pygame.K_LEFT:
        ap.show_message(humidity)
    elif event.key == pygame.K_RIGHT:
        ap.show_message(blah)       


running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            handle_event(event)
        if event.type == KEYUP:
            handle_event(event)
        if event.type == K_ESCAPE:
            running = False
        if event.type == pygame.QUIT:
            running = False
