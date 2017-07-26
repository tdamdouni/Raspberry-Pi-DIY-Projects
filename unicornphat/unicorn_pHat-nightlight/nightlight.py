#!/usr/bin/env python

import unicornhat as unicorn
from random import randint
from time import sleep
import datetime
import time

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.3)


def random():
  x = randint(0, 7)
  y = randint(0, 3)
  r = randint(1, 255)
  g = randint(1, 255)
  b = randint(1, 255)
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()  
def white():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 200
  g = 200
  b = 200
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()
def red():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 255
  g = 0
  b = 0
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()
def blank():
  x = randint(0, 7)
  y = randint(0, 3)
  r = 0
  g = 0
  b = 0
  unicorn.set_pixel(x, y, r , g, b)
  unicorn.show()

def night():
  for i in range(30):
    random()
    sleep(1)
  for i in range(45):
    blank()
    sleep(0.5)
def morning():
  for i in range(30):
    white()
    sleep(1)
  for i in range(45):
    blank()
    sleep(0.5)
def schedule():
  currenttime = time.localtime() 
  currenthour = currenttime.tm_hour
  currentmin = currenttime.tm_min
  localtime = time.asctime( time.localtime(time.time()) )
  
  timestamp = datetime.datetime.now().time()

  start = datetime.time(0, 1)
  end = datetime.time(6, 30)
  if(start <= timestamp <= end):
    print("night " + str(timestamp))
    night()    

  start = datetime.time(6, 15)
  end = datetime.time(8, 1)
  if(start <= timestamp <= end):
    print("morning " + str(timestamp))
    morning()

  start = datetime.time(8, 1)
  end = datetime.time(18, 30)
  if(start <= timestamp <= end):
    unicorn.clear()
    unicorn.show()    

  start = datetime.time(18, 30)
  end = datetime.time(23, 59)
  if(start <= timestamp <= end):
    print("night " + str(timestamp))
    night()
  

while True:
  schedule()
  time.sleep(0.5)
