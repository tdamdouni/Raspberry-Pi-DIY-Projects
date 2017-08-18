#!/usr/bin/env python
#-*-coding:utf-8-*-
#This program creates graphs with data obtained by the Sense HAT.
#Created by Iker García.

import csv
import matplotlib
matplotlib.use("Agg") #Added to plot graphs without running X server.
import matplotlib.pyplot as plt
import numpy as np
from sense_hat import SenseHat
import time 

while True:
  try:
    sense = SenseHat()
    temp = sense.get_temperature() #Reads temperature from Sense HAT.
    hum = sense.get_humidity() #Reads humidity from Sense HAT.

    file = open("/var/www/dashboard/linetemp.csv", "a") #Opens file to save data.
    writer = csv.writer(file, delimiter = ",")
    readfile = open("/var/www/dashboard/linetemp.csv", "r") #Opens file to count rows.
    reader = csv.reader(readfile, delimiter = ",")
    log = list(reader)
    rows = len(log)   
    measure = 60*rows #Data is going to be added each 60 minutes, we want to reflect this in the data file.
    data = [measure,temp]
    data = [int(i) for i in data] #Transforms data list in int, in order to be read by Matplotlib.
    writer.writerow(data) #Writes data on the csv file.

    file2 = open("/var/www/dashboard/linehum.csv", "a") #Same as previous part, in this case with humidity.
    writer2 = csv.writer(file2, delimiter = ",")
    readfile2 = open("/var/www/dashboard/linehum.csv", "r")
    reader2 = csv.reader(readfile2, delimiter = ",")
    log2 = list(reader2)
    rows2 = len(log2)
    measure2 = 60*rows2
    data2 = [measure2, hum]
    data2 = [int(i) for i in data2]
    writer2.writerow(data2)

    if rows >= 1 & rows2 >= 1: #Graph can't be plotted with only one data point, so for the first data point (rows = 0), matplotlib is not executed.
      x,y=np.loadtxt("/var/www/dashboard/linetemp.csv", unpack = True, delimiter = ",") #Opens first data set.
      plt.plot(x,y, label = u"Temperature (\u00B0C)") #Plots first data set.
      x,y2=np.loadtxt("/var/www/dashboard/linehum.csv", unpack = True, delimiter = ",") #Opens second data set.
      plt.plot(x,y2, label = "Humidity (%)") #Plots second data set.
      plt.legend(loc = "best") #Plots legend at the best location.
      plt.xlabel("Time(min)") #x axis label.
      plt.savefig("/var/www/dashboard/images/lines.png") #Saves created plot.
      plt.clf() #Clears figure, in order to create a tidy plot.
      time.sleep(3600) #Code is executed each hour.
    else: 
      time.sleep(3600) 

  except KeyboardInterrupt: #Exits program.
    break 

