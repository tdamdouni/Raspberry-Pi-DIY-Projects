import time
import math
import pygame

NUM_CHANNELS = 3

pygame.mixer.init(44100, -16, 1, 512)
pygame.mixer.set_num_channels(NUM_CHANNELS)

channels = [pygame.mixer.Channel(n) for n in range(NUM_CHANNELS)]

melody = pygame.mixer.Sound("./fn-melody.wav")
bass = pygame.mixer.Sound("./fn-bass.wav")
percussion = pygame.mixer.Sound("./fn-percussion.wav")

channels[0].play(melody, loops=-1)
channels[1].play(bass, loops=-1)
channels[2].play(percussion, loops=-1)

channels[1].set_volume(0.5)

while True:
    vol = (math.sin(time.time()) + 1) / 2
    channels[0].set_volume(vol)
    time.sleep(0.01)
