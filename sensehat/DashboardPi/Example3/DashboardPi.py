#!/usr/bin/env python
#-*-coding:utf-8-*-
#This program creates graphs with data obtained by the Sense HAT.
#Created by Iker García.

import csv
import datetime
import matplotlib
matplotlib.use("Agg") #Added to plot graphs without running X server.
import matplotlib.dates as md
import matplotlib.pyplot as plt
from sense_hat import SenseHat
import time

x = [] #Defines list needed for the plot.
y = []

while True:
  try:
    sense = SenseHat()
    temp = sense.get_temperature() #Reads temperature from SenseHAT.
    temp = round(temp, 2)
    now = datetime.datetime.now()
    file = open("/var/www/dashboard/temperature.csv", "a") #Opens file to save data.
    writer = csv.writer(file, delimiter = ",")
    data = [now,temp]
    writer.writerow(data) #Writes data on the csv file.
    x.append(now) #Updates list for the plot.
    y.append(temp)
   
    plt.plot(x,y) #Plots data set.
    plt.gca().xaxis.set_major_formatter(md.DateFormatter("%Y-%m-%d %H:%M:%S")) #Format the date.
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False) #Format y axis, in order not to get scientific units.
    plt.xlabel("Date") #x axis label.
    plt.ylabel(u"Temperature (\u00B0C)") #y axis label.
    plt.gcf().autofmt_xdate()#Correct format of the date on the axis.
    plt.savefig("/var/www/dashboard/images/linedate.png", bbox_inches = "tight") #Save the plot with the optimal size.
    plt.clf() #Clears the plot, in order to get a tidy plot. 
    time.sleep(3600) #Code is executed each hour.
 
  except KeyboardInterrupt:
    break

