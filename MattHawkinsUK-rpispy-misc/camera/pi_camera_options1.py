#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# pi_camera_options.py
# Takes a sequence of photos with the Pi camera
# using a range of Exposure and White Balance
# settings.
#
# Project URL :
# http://www.raspberrypi-spy.co.uk/2013/06/testing-multiple-pi-camera-options-with-python/
#
# Author : Matt Hawkins
# Date   : 15/01/2017
import os
import time
import subprocess

# Full list of Exposure and White Balance options
#list_ex  = ['off','auto','night','nightpreview','backlight',
#            'spotlight','sports','snow','beach','verylong',
#            'fixedfps','antishake','fireworks']
#list_awb = ['off','auto','sunlight','cloudy','shade','tungsten',
#            'fluorescent','incandescent','flash','horizon']

# Test list of Exposure and White Balance options. 9 photos.
list_ex  = ['off','auto','backlight']
list_awb = ['off','auto','sunlight']

# EV level
photo_ev = 0

# Photo dimensions and rotation
photo_width  = 640
photo_height = 480
photo_rotate = 90

photo_interval = 0.25 # Interval between photos (seconds)
photo_counter  = 0    # Photo counter

total_photos = len(list_ex) * len(list_awb)

# Delete all previous image files
try:
  os.remove("photo_*.jpg")
except OSError:
  pass

# Lets start taking photos!
try:

  print("Starting photo sequence")

  for ex in list_ex:
    for awb in list_awb:
      photo_counter = photo_counter + 1
      filename = 'photo_' + ex + '_' + awb + '.jpg'
      cmd = 'raspistill -o ' + filename + ' -t 1000 -ex ' + ex + ' -awb ' + awb + ' -ev ' + str(photo_ev) + ' -w ' + str(photo_width) + ' -h ' + str(photo_height) + ' -rot ' + str(photo_rotate)
      pid = subprocess.call(cmd, shell=True)
      print(' [' + str(photo_counter) + ' of ' + str(total_photos) + '] ' + filename)    
      time.sleep(photo_interval)
  
  print("Finished photo sequence")
  
except KeyboardInterrupt:
  # User quit
  print("\nGoodbye!")
