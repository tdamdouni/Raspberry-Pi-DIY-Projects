import pygame.mixer
from pygame.mixer import Sound

pygame.mixer.init()

drum = Sound("samples/DrumBuzz.wav")

while True:
    drum.play()