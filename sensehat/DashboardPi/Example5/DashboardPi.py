#!/usr/bin/env python
#-*-coding:utf-8-*-
#This program creates graphs with the position (XYZ) and the angular velocity obtained by the Sense HAT.
#Created by Iker García.

import csv
import matplotlib
matplotlib.use("Agg") #Added to plot graphs without running X server.
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sense_hat import SenseHat
import time

i = [] #Define list needed for the plot.
s = []
v = []
w = []
x = [] 
y = []
z = []
angular = 0 #Initial value of the angular displacement.
count = 0
snooze = 2 #Time in seconds for the time.sleep().
velocity = 0

while True:
  try:
    sense = SenseHat()
    orientation = sense.get_orientation() #Reads orientation from SenseHAT.
    xaxis = round(orientation["roll"], 2)
    yaxis = round(orientation["pitch"], 2)
    zaxis = round(orientation["yaw"], 2)
    count += 1
    
    i.append(count) #Updates list for the plot.
    x.append(xaxis)
    y.append(yaxis)
    z.append(zaxis)

    if count >=2: #Calculates the angular displacement, at least two data points are needed.
      angular = round(((x[count-1]-x[count-2])**(2) + (y[count-1]-y[count-2])**(2) + (z[count-1]-z[count-2])**(2))**(0.5), 2)
    w.append(angular)

    velocity = round(angular/snooze, 2) #Calculates the angular velocity.
    v.append(velocity)

    file = open("/home/pi/orientation.csv", "a") #Opens file to save data.
    writer = csv.writer(file, delimiter = ",")
    data = [count, xaxis, yaxis, zaxis, angular, velocity]
    writer.writerow(data) #Writes data on the csv file.
   
    fig = plt.figure(figsize = (12, 12)) #Starts the 3D figure.
    ax = fig.add_subplot(111, projection = "3d")
    ax.scatter(x, y, z) #Plots data set.
    ax.set_xlim(np.nanmin(x), np.nanmax(x)) #Defines the plot range as minimum-maximum value of the data.
    ax.set_ylim(np.nanmin(y), np.nanmax(y))
    ax.set_zlim(np.nanmin(z), np.nanmax(z))

    ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f")) #Formats the data in the axis with 2 decimal places.
    ax.yaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    ax.zaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    ax.set_xlabel(u"x (\u00B0)") #x axis label.
    ax.set_ylabel(u"y (\u00B0)") #y axis label.
    ax.set_zlabel(u"z (\u00B0)") #z axis label.

    plt.savefig("/home/pi/xyz.png", bbox_inches = "tight") #Saves the plot with the optimal size.
    plt.clf() #Clears the plot, in order to get a tidy plot.

    plt.figure() #Starts the figure.
    plt.plot(i, v) #Plots data set.
    ax.set_xlim(np.nanmin(i), np.nanmax(i)) #Defines the plot range as minimum-maximum value of the data.
    ax.set_ylim(np.nanmin(v), np.nanmax(v))
    plt.xlabel("Count") #x axis label.
    plt.ylabel(u"Angular velocity (s\u207B\u00B9)") #y axis label.
    plt.savefig("/home/pi/angular.png", bbox_inches = "tight") #Saves the plot with the optimal size.
    plt.clf() #Clears the plot, in order to get a tidy plot.

    time.sleep(snooze) #Code is each x seconds, defined as snooze before the while loop.
 
  except KeyboardInterrupt:
    break

