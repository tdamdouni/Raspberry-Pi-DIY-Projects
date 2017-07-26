#!/usr/bin/env python3

import unicornhat as unicorn
import time
import sys,subprocess
import _thread
import os


# set max bandwidth in bytes per second
maxin =  5000000  
maxout = 1000000

#set colors
colorIn =    [0,   255,   0]
colorOut =   [255,   0,   0]
colorError = [255, 255,   0]


# init unicorn hat
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.2)

# get size
width,height=unicorn.get_shape()
steps = 100 / (width + 1)

# target number of active LEDs
ledIn = 0
ledOut = 0


def getRate():
	global ledIn, ledOut

	while 1:
			error = False
			rate = ""
			
			# get xml from router
			try:
				rate = str(subprocess.check_output([os.getcwd() + "/connection_rate.sh"]))
			except subprocess.CalledProcessError:
				error = True
			if rate == "":
				error = True
			else:
				sendrate = rate.split('NewByteSendRate', maxsplit=3)
				receiverate = rate.split('NewByteReceiveRate', maxsplit=3)
			
				if len(sendrate) != 3:
					error = True
				if len(receiverate) != 3:
					error = True
			if error:
				ledIn = -1
				ledOut = -1
			else:
				sendrate = sendrate[1][1:-2]
				receiverate = receiverate[1][1:-2]
				
				percin = 0
				percout = 0
				
				# calc percentage of max bandwidth used
				if receiverate != 0:
					percin = float(receiverate) / maxin * 100
				if sendrate != 0:
					percout = float(sendrate) / maxout * 100
				
				# calc number of LEDs to light
				ledIn = int( percin / steps)
				ledOut = int( percout / steps)


def paint():
	# number of active LEDs
	curIn = 0
	curOut = 0
	
	while 1:
		curInPre = curIn
		curOutPre = curOut

		if ledIn < 0:
			for x in range(8):
				for y in range(4):
					unicorn.set_pixel(x, y, colorError[0], colorError[1], colorError[2])
			unicorn.show()
		else:
			if curIn < ledIn:
				curIn = curIn + 1
			if curIn > ledIn:
				curIn = curIn - 1
			if curOut < ledOut:
				curOut = curOut + 1
			if curOut > ledOut:
				curOut = curOut - 1

			#print (str(curIn))
			#skip painting if nothing changed
			if curOutPre == curOut and curInPre == curIn:
				continue

			# turn all off
			for x in range(8):
				for y in range(4):
					unicorn.set_pixel(x,y,0,0,0)

			# paint input
			for x in range(curIn):
				unicorn.set_pixel(x, 0, colorIn[0], colorIn[1], colorIn[2])
				unicorn.set_pixel(x, 1, colorIn[0], colorIn[1], colorIn[2])
			
			# paint output
			for x in range(curOut):
				unicorn.set_pixel(x, 2, colorOut[0], colorOut[1], colorOut[2])
				unicorn.set_pixel(x, 3, colorOut[0], colorOut[1], colorOut[2])
			
			unicorn.show()

		time.sleep(0.07)


#create unicorn tread 
#create upnp query thread
try:
	_thread.start_new_thread( getRate, () )
	_thread.start_new_thread( paint, () )
	
	# keep alive
	while 1:
		pass

except:
	print ("Error: unable to start thread")

