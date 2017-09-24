from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from time import sleep

sensor = MotionSensor(14)
camera = PiCamera()

while True:
	sensor.wait_for_motion()
	filename = datetime.now().strftime("%H.%M.%S_%Y-%m-%d.jpg")
	camera.capture(filename)
	sleep(5)