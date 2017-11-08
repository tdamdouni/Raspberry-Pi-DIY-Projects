#!/usr/bin/env python

# wordclock.py by Carl Monk (@ForToffee)
# https://github.com/ForToffee/UnicornHAT
# no unicorns were harmed in the making of this code

import unicornhat as UH
import time

#global variables
hourPattern = []
minPattern = []

#pre-defined patterns - groups of x,y co-ords - 0,0 is bottom right with GPIO at bottom
fivePattern = [[7,6],[6,6],[4,6],[2,6]]
tenPattern = [[1,7],[1,6],[0,6]]
fiftPattern = [[7,6],[6,6],[5,6],[3,6],[2,6],[1,6],[0,6]]
twenPattern = [[5,7],[4,7],[3,7],[2,7],[1,7],[0,7]]
halfPattern = [[7,7],[6,7],[7,5],[6,5]]

pastPattern = [[4,5],[3,5],[2,5],[1,5]]
toPattern = [[1,5],[0,5]]

#function to light the pixels we need to display the time
#pixels is a list of pixels
def showTime(pixels):
	UH.clear()
	for coords in pixels:
		UH.set_pixel(coords[0],coords[1],255,0,255)		#magenta

	UH.show()	#once pixels set, call .show() to enable them
		
#function to light the '*' character to show seconds and minutes elapsing
def showTick(m):
	colour = []
	minPart = m % 5		
	# % is modulo which gives us the remainder of m divided by 5
	# this tells us the value 0 - 4 or the part of 5 minutes the time is
	
	if m == -1:		# for setting the '*' off or black
		colour = [0,0,0]

	elif minPart == 0:	#:m0 or :m5
		colour = [255,0,0]		#red 

	elif minPart == 1 :	#:m1 or :m6
		colour = [0,255,0]		#green

	elif minPart == 2 : #:m2 or :m7
		colour = [0,0,255]		#blue

	elif minPart == 3 : #:m3 or :m8
		colour = [255,255,0]	#yellow

	elif minPart == 4 : #:m4 or :m9
		colour = [0,255,255]	#cyan

	UH.set_pixel(5,5,colour[0],colour[1],colour[2])	#5,5 is the position of '*'
	UH.show()

#takes the current hour and provides the required pattern of letters
def getHourPattern(h,m):
	global hourPattern
	hourPattern = []

	#convert 24hr into 12hr
	if h >= 12:
		h -= 12

	#if minutes > 35 then display will be 'to' the next hour
	if m >= 35:
		h = h + 1
		#special case for 11:35 - 12:00.  Hour is 0 to 11 so need to reset to 0
		if h == 12:		
			h = 0

	if h == 0:	#aka Twelve
		hourPattern =  [[7,2],[6,2],[5,2],[4,2],[2,2],[1,2]]
	elif h == 1:
		hourPattern =  [[7,3],[6,3],[5,3]]
	elif h == 2:
		hourPattern =  [[7,2],[6,2],[6,1]]
	elif h == 3:
		hourPattern =  [[4,3],[3,3],[2,3],[1,3],[0,3]]
	elif h == 4:
		hourPattern =  [[7,1],[6,1],[5,1],[4,1]]
	elif h == 5:
		hourPattern =  [[3,1],[2,1],[1,1],[0,1]]
	elif h == 6:
		hourPattern =  [[7,0],[6,0],[5,0]]
	elif h == 7:
		hourPattern =  [[4,0],[3,0],[2,0],[1,0],[0,0]]
	elif h == 8:
		hourPattern =  [[4,4],[3,4],[2,4],[1,4],[0,4]]
	elif h == 9:
		hourPattern =  [[7,4],[6,4],[5,4],[4,4]]
	elif h == 10:
		hourPattern =  [[0,4],[0,3],[0,2]]
	elif h == 11:
		hourPattern =  [[5,2],[4,2],[3,2],[2,2],[1,2],[0,2]]

#takes the current minute and provides the required pattern of letters
def getMinutePattern(m):
	global minPattern
	minPattern = []
	if 10 > m >= 5 or m >= 55:
		minPattern = fivePattern
	elif 15 > m >= 10 or 55 > m >= 50:
		minPattern = tenPattern
	elif 20 > m >= 15 or 50 > m >= 45:
		minPattern = fiftPattern
	elif 25 > m >= 20 or 45 > m >= 40:
		minPattern = twenPattern
	elif 30 > m >= 25 or 40 > m >= 35:
		minPattern = twenPattern + fivePattern
	elif 35 > m >= 30:
		minPattern = halfPattern

	#if time between 5 and 34 we need to show 'past' the hour
	if 35 > m >= 5:
		minPattern = minPattern + pastPattern
	elif m >= 35:	#otherwise 'to' the hour
		minPattern = minPattern + toPattern

#cycle through a full 12hrs minute by minute
def fullTest():		
	for n in range(12*60):
		getHourPattern(n / 60, n % 60)
		getMinutePattern(n % 60)
		showTime(minPattern + hourPattern)
		showTick(n)
		time.sleep(.25)

#cycle through hours, then minutes
def quickTest():
		
	for n in range(12):
		getHourPattern(n, 0)
		showTime(hourPattern)
		time.sleep(.5)

	for n in range(60):
		getMinutePattern(n)
		showTime(minPattern )
		showTick(n)
		time.sleep(.25)

		
#main function 
quickTest()
#while True:
#	fullTest()
	
while True:
	#get time parts
	h = time.localtime().tm_hour
	m = time.localtime().tm_min
	s = time.localtime().tm_sec

	#get patterns
	getHourPattern(h, m)
	getMinutePattern(m)
	
	#show patterns
	showTime(minPattern + hourPattern)

	#flash '*' to show time passing, lit every 2 seconds
	if s % 2:
		showTick(m)
	else:
		showTick(-1)

	
	time.sleep(1)
