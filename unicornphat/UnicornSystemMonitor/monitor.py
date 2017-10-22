#!/usr/bin/python
import unicornhat as unicorn
import time
from gpiozero import CPUTemperature

# Config

t_min=65	# minimum temperature to show
t_max=85	# maximum temperature to show
t_steps=(t_max-t_min)/8

delay=2	# sleep time between measure steps


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)

cpu = CPUTemperature()

curv=[0,0,0,0,0,0,0,0] # array with temperature history

while True:
	print(cpu.temperature)
        #time.sleep(2)
	pegel = int((cpu.temperature-t_min)/t_steps)-1
	print(pegel)
	curv.insert(0,pegel) # insert latest data
	curv.pop()	# kick oldest entry
	unicorn.clear()
	for i in range(0, len(curv)):
		#print(i)
		#print(curv[i])
		for j in range(0, curv[i]):
			unicorn.set_pixel(i,j,255,0,0)
        	unicorn.set_pixel(i,curv[i],220,220,0)
	unicorn.show()
