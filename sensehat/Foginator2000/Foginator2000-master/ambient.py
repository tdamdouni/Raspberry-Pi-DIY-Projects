import pygame

audio_path = '/home/pi/Desktop/audio/ambient.mp3'

var = True

while var ==True:
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(5)
