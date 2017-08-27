from gpiozero import LED, Button
from picamera import PiCamera

yellow = LED(16)
button = Button(15)

print ("Starting camera code")

with PiCamera() as camera:
	#camera.start_preview()
	frame =1
	while True:
		button.wait_for_press()
		yellow.source = button.values
		print ("About to capture photo")
		camera.capture('/home/pi/photo_output/frame%03d.jpg' % frame)
		print (frame)
		frame +=1
