# Timelapse camera using Lisiparoi flash connected to GPIO7
## This has been updated on My Mac
from picamera import PiCamera
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,GPIO.LOW)

frames = int(input("How many frames? "))
timebetween = int(input("Interval between each photo "))
actual_timebetween = timebetween - 6
framecount = 0
total_time = round((frames * timebetween)/60)
print ("It will take approx ",total_time," minutes")
print ("photos will be saved in photo_output")


while framecount < frames: 
	with PiCamera() as camera:
	#	camera.start_preview()
		GPIO.output(7,GPIO.HIGH)	
		localtime = time.asctime( time.localtime(time.time()) )
		camera.annotate_text=localtime
		camera.capture('/home/pi/photo_output/image%s.jpg'%(framecount))
		framecount +=1
		GPIO.output(7,GPIO.LOW)
		time.sleep(actual_timebetween)
#camera.stop_preview()	

