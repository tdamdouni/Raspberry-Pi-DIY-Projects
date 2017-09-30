from Adafruit_BME280 import *
from time import sleep
import picamera
import os
import time
import subprocess
import datetime


def read_temp():

    my_file = open('log.txt', 'a')

    sensor = BME280(mode=BME280_OSAMPLE_8)

    time_stamp = datetime.datetime.now()

    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()

    timestamp = 'Timestamp = ' + str(time_stamp)
    temp = 'Temp = {0:0.3f} deg C'.format(degrees)
    pressure = 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
    humidity = 'Humidity  = {0:0.2f} %'.format(humidity)


    print ("Current date & time = %s" % time_stamp)
    print temp
    print pressure
    print humidity
    
    line = timestamp + "," + temp + "," + pressure + "," + humidity + "\n"

    my_file.write(line)
 
    list_ex  = ['auto']    
    list_awb = ['auto']
 
# EV level
    photo_ev = 0
 
# Photo dimensions and rotation
    photo_width  = 640
    photo_height = 480
    photo_rotate = 0
 
    photo_interval = 0.25 # Interval between photos (seconds)
    photo_counter  = 0    # Photo counter
 
    total_photos = len(list_ex) * len(list_awb)
 
 
# Lets start taking photos!
    try:
 
      for ex in list_ex:
        for awb in list_awb:
          photo_counter = photo_counter + 1
          filename = 'imgs/photo_' + str(time_stamp.isoformat()) + '.jpg'
          cmd = 'raspistill -o ' + filename + ' -t 1000 -ex ' + ex +' -awb ' + awb + ' -ev ' + str(photo_ev) + ' -w ' + str(photo_width) + ' -h ' + str(photo_height) + ' -rot ' + str(photo_rotate)
          pid = subprocess.call(cmd, shell=True)
          print "Image created in 'imgs' folder: " + filename
          print '--------------------------------------------------------------------------' + '\n'
          time.sleep(photo_interval)
 
 
    except KeyboardInterrupt:
  # User quit
      print "\nGoodbye!"

    return None
