import picamera
import time

with picamera.PiCamera() as camera:
	camera.start_preview()
	try: 
		for i in range(100):
			camera.brightness = i
			time.sleep(.2)
	finally:
		camera.stop_preview()
