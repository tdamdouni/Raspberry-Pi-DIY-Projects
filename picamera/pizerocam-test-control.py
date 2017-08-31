#!/usr/bin/python3

# http://richardhayler.blogspot.de/2016/06/pi-zero-cctv-with-zeroview.html

# Some simple python checks the accelerometer and looks for abrupt changes in the values reported, to detect if the Pi falls off the window. In this event it uploads a picture of Humpty Dumpty to DropBox. The same code also periodically checks that it is still connected to the Internet (by pinging Google) and changes the colour of the RGB LED from green to red.  There are a few other visual cues too: the LED flashes blue when the baseline accelerometer readings are being measured at start-up and also flashes green when a ping test is underway. This is run at startup via /etc/rc.local.

from gpiozero import RGBLED
from adxl345 import ADXL345
import time, numpy
from datetime import datetime
import dropbox
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()
import os,sys,logging

logfile = "/home/pi/cctv-"+str(datetime.now().strftime("%Y%m%d-%H%M"))+".csv"
logging.basicConfig(filename=logfile, level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d, %H:%M:%S,')

led = RGBLED(26,13,6)
eggfile='/home/pi/Humpty-Dumpty.gif'
adxl345 = ADXL345()
client = dropbox.client.DropboxClient('<ENTER YOUR DROPBOX KEY HERE>')
#print('linked account: ', client.account_info())
logging.info('linked account: ', client.account_info())

axes = adxl345.getAxes(True)
#print("ADXL345 on address 0x%x:" % (adxl345.address))
logging.info("ADXL345 on address 0x%x:" % (adxl345.address))
t = 0
x_av = 0
y_av = 0
x_values = []
y_values = []
#print('Calibrating....')
logging.info('Calibrating....')
led.blink(on_time=0.1,off_time=0.1,on_color=(0,0,1), n=50,background=True)
while t < 100:
    axes = adxl345.getAxes(True)
    x = axes['x']
    y = axes['y']
#    print(x)
    x_values.append(x)
    y_values.append(y)
    time.sleep(0.1)
    t+=1
x_av = numpy.mean(x_values)
y_av = numpy.mean(y_values)
x_range = numpy.max(x_values) - numpy.min(x_values)
y_range = numpy.max(y_values) - numpy.min(y_values)
logging.info('Set mean x: ' + str(x_av))
logging.info('Set range x: ' + str(x_range))
logging.info('Set mean y: ' + str(y_av))
logging.info('Set range y: ' + str(y_range))
led.color = (0,0.2,0)
counter = 0
jiggle = 5
while True:
    axes = adxl345.getAxes(True)
    x = axes['x']
    y = axes['y']
    if ((x > (x_av + (jiggle*x_range))) or (x < (x_av - (jiggle*x_range)))) and  ((y > (y_av + (jiggle*y_range))) or (y < (y_av - (jiggle*y_range)))):
        #print('Humpty')
        logging.info('Humpty')
        led.color = (1,0,0)
        f = open(eggfile, 'rb')
        response = client.put_file(eggfile,f)
        f.close()
        time.sleep(1)
    time.sleep(0.1)
    counter +=1
    if counter > 6000:
        #print('Checking network comms...')
        logging.info('Checking network comms...')
        counter = 0
        response = os.system("ping -c 3 8.8.8.8")
        if response == 0:
            logging.info('I pinged Google successfully')
            led.blink(on_time=0.1, off_time=0.1, on_color=(0,0.5,0), n=3, background=False)
            led.color = (0,0.2,0)
        else:
            logging.info('Comms Down :-(')
            led.blink(on_time=0.1, off_time=0.1, on_color=(1,0,0), background=True)
