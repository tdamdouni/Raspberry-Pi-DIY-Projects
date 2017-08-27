# Timelapse camera taking a photo every 10 minutes for 12 hours
from picamera import PiCamera
import time
from UHScroll import *
import datetime
import unicornhat as UH



frames = 5
timebetween = 10
actual_timebetween = timebetween - 6
framecount = 0
flash = 1

text = 'Uni-Cam'
colour = 'green'
speed = 0.1
unicorn_scroll(text,colour,255,speed)
time.sleep(0.5)
frame_text = str(frames) + ' Fr'
interval_text = str(timebetween)

if flash ==1:
	flash_text='Flash'
if flash ==0:
	flash_text='No Flash'

unicorn_scroll(frame_text,'green', 255, 0.1)
unicorn_scroll(flash_text,'red',255,0.1)

time.sleep(0.1)

for count in range (3):
	for y in range(8):
		for x in range (8):
			if count ==0:
				r = 255
				g = 0
				b = 0

			if count ==1:
				r = 255
				g = 255
				b = 0

			if count ==2:
				r = 0
				g = 255
				b = 0

			UH.set_pixel(x,y,r,g,b)
	UH.show()
	time.sleep(0.5)
		
while framecount < frames: 
	with PiCamera() as camera:
		camera.start_preview()
		localtime = time.asctime( time.localtime(time.time()) )
		camera.annotate_text=localtime
		UH.brightness(0.3)
		if flash ==1:
			for y in range(8):
                		for x in range (8):
					UH.set_pixel(x,y,255,255,255)
			UH.show()
		camera.capture('/home/pi/photo_output/image%s.jpg'%(framecount))
		framecount +=1
		camera.stop_preview()
		text = str(framecount)
		colour = 'red'
		speed = 0.1
		unicorn_scroll(text,colour,255,speed)
		if flash ==1:
			for y in range(8):
				for x in range (8):
					UH.set_pixel(x,y,0,0,0)
			UH.show()
		time.sleep(actual_timebetween)

text = 'Photos completed'
colour = 'green'
speed = 0.1
unicorn_scroll(text,colour,255,speed)		  

