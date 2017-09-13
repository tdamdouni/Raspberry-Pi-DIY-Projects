# http://forums.pimoroni.com/t/pi-based-trail-camera/2172/9

counter = 0
recording = 0
video = 1

import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
camera = picamera.PiCamera()
camera.rotation = 180

print "trail camera v1.0\n"
time.sleep(1)
print "ready\n"
time.sleep(1)

def motion(PIR_PIN):
    global counter
    print "motion detected\n"
    counter = 30
    time.sleep(1)

GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motion)

while True:
    if counter > 0:
        if recording == 0:
            recording = 1
            print "recording\n"
            camera.start_recording('/home/pi/Desktop/video%03d.h264' % video)
            time.sleep(1)
        if recording == 1:
            print (counter)
            print ""
            time.sleep(1)
            counter -= 1
    if counter == 0:
        if recording == 0:
            print "idle\n"
            time.sleep(5)
        if recording == 1:
            print "recording stopped\n"
            camera.stop_recording()
            video += 1
            recording = 0
            time.sleep(1)

try:
    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print "Quit"
GPIO.cleanup()