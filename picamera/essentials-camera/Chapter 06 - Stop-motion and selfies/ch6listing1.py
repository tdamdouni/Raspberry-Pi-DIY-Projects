#importing the necessary modules
from datetime import datetime
from gpiozero import Button
import picamera
import time

b=Button(14)
pc=picamera.PiCamera()
running = True
#pc.resolution = (1024, 768)
#use this to set the resolution if you dislike the default values
timestamp=datetime.now()
def picture():
	pc.capture('pic'+str(timestamp)+'.jpg') #taking the picture

pc.start_preview() #running the preview
b.when_pressed=picture
try:
	while running:
		print('Active')#displaying 'active' to the shell
		time.sleep(1)
#we detect Ctrl-C then quit the program
except KeyboardInterrupt:
	pc.stop_preview()
	running = False