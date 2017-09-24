import picamera

with picamera.PiCamera() as camera:
	camera.flash_mode = 'on'
	camera.capture('foo.jpg')