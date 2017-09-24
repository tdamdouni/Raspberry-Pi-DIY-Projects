from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()
button = Button(2)
drum = Sound("samples/DrumBuzz.wav")

button.when_pressed = drum.play
pause()