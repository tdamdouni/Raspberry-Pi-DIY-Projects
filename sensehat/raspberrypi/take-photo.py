#!/usr/bin/env python

# This script will take a photo from the Raspberry Pi camera

import pygame
import pygame.camera
import os
import time
from pygame.locals import *

# Take a photo from the camera
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (768, 1024))
cam.start()
image = cam.get_image()
image = pygame.transform.rotate(image, -90)
pygame.image.save(image, 'webcam.jpg')
