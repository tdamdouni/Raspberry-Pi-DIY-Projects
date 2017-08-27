from picamera import PiCamera
with PiCamera() as camera:
	input("Are you scared?")
	camera.start_preview()
	camera.annotate_text='Watch out for the scary ghosts!!!!!!'
	camera.capture('/home/pi/scare.jpg')
camera.stop_preview()
    
