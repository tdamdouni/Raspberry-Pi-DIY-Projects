import time
import picamera
import random


with picamera.PiCamera() as cam:
    cam.vflip = 1
    cam.hflip = 1

    cam.resolution = (800, 600)
    time.sleep(2)
    cam.start_preview()
    for fname in cam.capture_continuous('img{counter:03d}.jpg'):
        eff = random.choice(cam.IMAGE_EFFECTS.keys())
        cam.image_effect = eff
        print "Captured {}".format(fname)
        time.sleep(5)
    
    
