# Timelapse camera taking a photo every 10 minutes for 12 hours
from picamera import PiCamera
import time
frames = 50
timebetween = 120
actual_timebetween = timebetween - 6
framecount = 0


while framecount < frames: 
	with PiCamera() as camera:
#		camera.start_preview()
		localtime = time.asctime( time.localtime(time.time()) )
		camera.annotate_text=localtime
		camera.capture('/home/pi/photo_output/image%s.jpg'%(framecount))
		framecount +=1
#		camera.stop_preview()
		time.sleep(actual_timebetween)
		  

