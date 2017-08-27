from gpiozero import LED, Button
from picamera import PiCamera

yellow = LED(15)
button = Button(21)

with PiCamera() as camera:
	camera.start_preview()
	frame =1
	while True:
		button.wait_for_press()
		yellow.source = button.values
		camera.capture('/home/pi/photo_output/frame%03d.jpg' % frame)
		frame +=1
