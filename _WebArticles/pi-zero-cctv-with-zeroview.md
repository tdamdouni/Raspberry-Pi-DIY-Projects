# Pi Zero CCTV with ZeroView

_Captured: 2017-08-30 at 09:17 from [richardhayler.blogspot.de](http://richardhayler.blogspot.de/2016/06/pi-zero-cctv-with-zeroview.html)_

One of the first things I used a raspberry Pi for was to build a simple CCTV system. In fact that original model B is still up and running and today. It is a nice compact, self contained system.

However the addition of a camera capability to the Pi Zero opened up the possibilities for even smaller photography ideas.

Those rambunctious pirates at Pimoroni were quick off the mark with their dinky Little Bro kit. This is a smart CCTV sign that has a hole for the camera and comes with a mounting bracket for the Pi Zero which also allows you to fix the whole thing to a wall. When I wanted to make a timelapse of some garden work that was happening I simply used some string to hang the Little Bro from the window handle. This worked fine although it was a bit wobbly (especially when the window as opened) and when I had to adjust something I didn't manage to put it back up without altering the field of view slightly (you can see that the picture jumps slightly at about 00:10). It was also difficult to get the camera as close to the glass to keep reflections to a minimum.

![](https://3.bp.blogspot.com/-02Nf35A3oGc/V2JkGzQwnOI/AAAAAAAAGd0/NXz-gwicFLQ3h8fYj7exDe94uVwzOLPDACLcB/s320/IMG_0378.JPG)

Then The PiHut launched the excellent ZeroView, designed for exactly this sort of thing. It uses two sucker pads to stick to a window thus keep the camera as close to the glass as possible. Because the frame can be removed from the suckers while leaving them attached to the window, it also allows for easy adjustment and replacement without altering the field of view.

![](https://3.bp.blogspot.com/-3kfUvStnPSA/V2JkLTEWKaI/AAAAAAAAGeA/vf_Wv1rKaPI3VL9SQ2p_aFFwPTaSnKvHACLcB/s320/IMG_0389.JPG)

Initial tests confirmed that this was genius!

![](https://3.bp.blogspot.com/-tYkpBIoeayI/V2JkKcxL5VI/AAAAAAAAGd8/oPpFaySJQQUIeVaqpCh-cIie6TDfLc13gCLcB/s320/IMG_0379.JPG)

Remixing my original CCTV build (which uses Motion to detect movement and then uploads the resulting movie to Dropbox) was easy. On the first night of testing I managed to catch this wily fox sneaking through my garden at dawn.

![](https://3.bp.blogspot.com/-biBlBQ1NfnY/V2Jk1RNYirI/AAAAAAAAGeU/vxe1RuLtYLgpqP1kEyq8SkGb-4W_6RVXACLcB/s320/Snip20160616_1.png)

However there were a couple of issues about making this a permanent installation that I wanted to address:

1) My experience of headless Pis and wifi is that sometimes the computer drops off the network. Although the power management for dongles seems to be much improved now, I wanted an easy way of seeing that the Zero was still connected.  
2) Suckers are effective but not always reliable, especially in a window which might experience big changes in temperature.

So as a combined solution to both of these, I used a [ProtoZero](http://www.protoboards.co.uk/2016/01/protozero.html) board, an [accelerometer](http://www.ebay.co.uk/itm/For-Arduino-1pcs-New-ADXL345-3-Axis-Digital-Acceleration-Of-Gravity-Tilt-Module-/271870675843?var=&hash=item3f4cc14b83:m:m8NmprfE9r44WGW83T9eHuw) and an RGB LED.

![](https://3.bp.blogspot.com/-o9dJzgi8_IE/V2JlBkJEmtI/AAAAAAAAGec/nG6j-UdfZ6wCW821shjDN4j9oQ4NEFfLQCLcB/s320/IMG_0384.JPG)

Some simple python checks the accelerometer and looks for abrupt changes in the values reported, to detect if the Pi falls off the window. In this event it uploads a picture of Humpty Dumpty to DropBox. The same code also periodically checks that it is still connected to the Internet (by pinging Google) and changes the colour of the RGB LED from green to red. There are a few other visual cues too: the LED flashes blue when the baseline accelerometer readings are being measured at start-up and also flashes green when a ping test is underway. This is run at startup via /etc/rc.local.

#!/usr/bin/python3  
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
# print(x)  
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
if ((x > (x_av + (jiggle*x_range))) or (x < (x_av - (jiggle*x_range)))) and ((y > (y_av + (jiggle*y_range))) or (y < (y_av - (jiggle*y_range)))):  
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

###  Notes:

1) I used numpy to calculate the means and ranges which is really lazy - especially as numpy takes ages to compile on a Pi Zero.

2) I started from a fresh instal of jessie-lite. In addition to the Python libraries at the top of the code, you'll also need to install the following Raspbian packages:

python3-dev  
libffi-dev  
libssl-dev  
requests[security]  
git

3) You''l also need to enable the camera and the i2C interface through raspi-config
