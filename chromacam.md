# ChromaCam

Using Raspberry Pi and CSI camera module to do green screen.
With this program you can do greeen screen images.  Taking out the background and replacing them with a different background.

Using the following libraries within Python

import sys
import pygame
from pygame import locals
from picamera import PiCamera
from time import sleep, time
import subprocess 
import os
import shlex
import glob
import tweepy 

Also, needs ImageMagick install as it does the removing of the back.  It's the convert commands you see in the code.
ImageMagick is in the repository on the Raspberry Pi so just
sudo apt install imagemagick  - will install it.

Copy code to folder /home/pi/chromaCam
Create subfolder

sourcebg   - storage for possible background images
background - where background images are stored at the required resolution

Also, needed an overlap_640.png (assuming resolution is 640x480) that is added to the image when it is tweeted.  This file is in the /home/pi/chromaCam folder

With these 2 sub folders you can start with images at any resolution and store them in sourcegb.  When the code starts it copies the images and resizes them putting them in the background folder.

Use keys left/right to change the background and enter to take a picture and tweet it.
Alternative if you have a gamepad attached can use the gamepad 
I use a small Bluetooth gamepad as it's hardly visible in the persons hand and means the person can control the background the final picture themself.

#The way it works is
Begin by getting the value for the background from the top right corner.  This is the colour to be removed so usually is a green
Then save an image file and using ImageMagick remove the green identified previously.
With different light and shade the green will not always be the same, so there is a variable called fuzzpercent that sets how close to the selected colour the green needs to be.
From experience 20% is a good setting.  Anything else and the lighting needs to be very even.  Anything more and people start losing their shirt and faces.   It's worth playing with fuzzpercent if you are not removing all the green (make it bigger) or removing part of the person in front (make it smaller)







