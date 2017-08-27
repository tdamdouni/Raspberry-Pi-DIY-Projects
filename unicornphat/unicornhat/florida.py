from UHScroll import *
import datetime
import time
from datetime import timedelta
import unicornhat as UH
import random

while True:
	#Draw Mickey Ears
	UH.rotation(0)
	colours = [1,2,3]
	colour = random.choice(colours)
	if colour == 1:
		r = 255
		g = 0
		b = 0
	if colour == 2:
		r = 0
		g = 255
		b = 0
	if colour == 3:
		r = 0
		g = 0
		b =255
	
	for y in range(8):
		for x in range (8):
			UH.set_pixel(x,y,0,0,0)
	for y in range(3):
		for x in range (4):
			UH.set_pixel(x+2,y+2,r,g,b)
	for y in range(2):
		for x in range (2):
			UH.set_pixel(x+1,y+5,r,g,b)
			UH.set_pixel(x+5,y+5,r,g,b)
	UH.show()
	time.sleep(10)


#First message

	text = 'Days until Disney' #String to be displayed on the first round of text
	colour = 'red' #String to set the colour of the text
	speed = 0.15
	unicorn_scroll(text,colour,255,speed)
	time.sleep(0.5)

#Second message

	today = datetime.date.today()
	florida = datetime.date(2015,8,1)
	difference = florida - today
	date_difference = (difference).days
	display_text = str(date_difference)
	colour = 'green'
	unicorn_scroll(display_text,colour,255,0.15)
