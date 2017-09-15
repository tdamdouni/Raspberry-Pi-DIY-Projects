#!/usr/bin/env python

# https://drive.google.com/file/d/0B-0UNek611hKV2g5SVdQVHppYmc/view

# http://forums.pimoroni.com/t/pan-tilt-hat-roaming/5127/3

import cv2, sys, time, os, random
from pantilthat import *

# Load the BCM V4l2 driver for /dev/video0
os.system('sudo modprobe bcm2835-v4l2')
# Set the framerate ( not sure this does anything! )
os.system('v4l2-ctl -p 8')

# Frame Size. Smaller is faster, but less accurate.
# Wide and short is better, since moving your head
# vertically is kinda hard!
FRAME_W = 200
FRAME_H = 100

# Motion params
HYSTERESIS = 0.05

# Roam params
ROAM_START = 40

frames_since_face = 0

# Default Pan/Tilt for the camera in degrees.
# Camera range is from -90 to 90
cam_pan = 90
cam_tilt = 60

# Set up the CascadeClassifier for face tracking
#cascPath = 'haarcascade_frontalface_default.xml' # sys.argv[1]
cascPath = '/usr/share/opencv/lbpcascades/lbpcascade_frontalface.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

# Set up the capture with our frame size
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  FRAME_W)
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, FRAME_H)
time.sleep(2)

# Turn the camera to the default position
pan(cam_pan-90)
tilt(cam_tilt-90)
light_mode(WS2812)

def lights(r,g,b,w):
    for x in range(18):
        set_pixel_rgbw(x,r if x in [3,4] else 0,g if x in [3,4] else 0,b,w if x in [0,1,6,7] else 0)
    show()

lights(0,0,0,50)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    # This line lets you mount the camera the "right" way up, with neopixels above
    frame = cv2.flip(frame, -1)

    if ret == False:
      print("Error getting image")
      continue

    # Convert to greyscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist( gray )

    # Do face detection
    faces = faceCascade.detectMultiScale(frame, 1.1, 3, 0, (10, 10))

    if len(faces) > 0:
        frames_since_face = 0
        for (x, y, w, h) in faces:

            # Draw a green rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Get the center of the face
            x = x + (w/2)
            y = y + (h/2)

            # Correct relative to center of image
            turn_x = float(x - (FRAME_W/2))
            turn_y = float(y - (FRAME_H/2))

            # Convert to percentage offset
            turn_x /= float(FRAME_W/2)
            turn_y /= float(FRAME_H/2)

            # Scaleframes_since_face offset to degrees
            turn_x *= 2.5 # VFOV
            turn_y *= 2.5 # HFOV

            if abs(turn_x) > HYSTERESIS:
                cam_pan  += -turn_x

            if abs(turn_y) > HYSTERESIS:
                cam_tilt += turn_y

            # Clamp Pan/Tilt to 0 to 180 degrees
            cam_pan = max(0, min(180,cam_pan))
            cam_tilt = max(0, min(180,cam_tilt))

            # Update the servos
            pan(int(cam_pan-90))
            tilt(int(cam_tilt-90))

            # Exit after first face
            break

    elif len(faces) == 0:
        frames_since_face = frames_since_face + 1
        if frames_since_face > ROAM_START:
            frames_since_face = 0
            cam_pan = random.randint(60,120)
            cam_tilt = random.randint(60,120)
            pan(int(cam_pan-90))
            tilt(int(cam_tilt-90))
    else:
        print("ERROR")
        break


    print("%.2f %.2f" % (cam_pan-90, cam_tilt-90))

    cv2.imshow("preview", frame)
    cv2.waitKey(20)
    #cv2.imwrite("test.jpg", frame)
