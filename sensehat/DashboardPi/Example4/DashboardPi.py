#!/usr/bin/env python
#-*-coding:utf-8-*-
#This program creates animations with data obtained by the Sense HAT.
#Created by Iker García.

import matplotlib
matplotlib.use("Agg") #Added to create animations without running X server.
import matplotlib.animation as animation
import matplotlib.pyplot as plt  
import numpy as np
from sense_hat import SenseHat
import time
storetemp = [] #Defines array to store data
storetime = []


def update_line(num, data, line): #Defines line update function.
    line.set_data(data[..., :num])
    return line, 

fig = plt.figure() #Creates figure.


for i in range (25): #Takes data 25 times.
  sense = SenseHat()
  temp = sense.get_temperature() #Reads temperature from SenseHAT.
  temp = round(temp ,2)
  measure = 60*i
  temperature = np.array([temp],float) #Creates temperature array.
  storetemp = np.concatenate((storetemp ,temperature)) #Stores temperature.
  measuretime = np.array([measure] ,float)
  storetime = np.concatenate((storetime, measuretime))
  data = np.concatenate((storetime, storetemp)) #Creates data array. First variable is x axis, second one is y axis.
  time.sleep(3600) #Code is executed each hour.

data = np.reshape(data,(2,25)) #Reshapes data array to create theanimation.

line1, = plt.plot([], [], "b-") #Creates the line. 
xmin = data[0][0] #x min is  the first point of the array.
xmax = data[0][24] #x max is the last point of the array.
ymin = np.min(data[1])-1 #y min is the minimum temperature value of the array, -1 added to create some space under the value.
ymax = np.max(data[1])+1 #y max is the maximum temperature value of the array, +1 added to create some space above the value.
plt.xlim(xmin,xmax) #x limits are set.
plt.ylim(ymin,ymax) #y limits are set.
plt.xlabel("Time(min)") #x axis label.
plt.ylabel(u"Temperature (\u00B0C)") #y axis label.
line_ani = animation.FuncAnimation(fig, update_line, 25, fargs=(data, line1), interval=50, blit=True) #Creates animation.
line_ani.save("/var/www/dashboard/images/temperatureanimation.mp4") #Saves animation

