# Timelapse camera using Pibrella to indicate status

from picamera import PiCamera
import time
import pibrella

pibrella.light.red.on()

frames = int(input("How many frames? "))
timebetween = int(input("Interval between each photo "))
actual_timebetween = timebetween - 6
framecount = 0
total_time = round((frames * timebetween)/60)
print ("It will take approx ",total_time," minutes")
print ("photos will be saved in photo_output")

#pibrella.light.red.off()

while framecount < frames: 
	with PiCamera() as camera:
		camera.start_preview()
		pibrella.light.green.on()
		pibrella.light.amber.off()	
		localtime = time.asctime( time.localtime(time.time()) )
		camera.annotate_text=localtime
		camera.capture('/home/pi/photo_output/image%s.jpg'%(framecount))
		framecount +=1
		pibrella.light.green.off()
		pibrella.light.amber.on()
		time.sleep(actual_timebetween)
camera.stop_preview()	

