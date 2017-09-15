# Pi Camera and Motion

_Captured: 2017-08-31 at 01:14 from [www.raspberrypi.org](https://www.raspberrypi.org/forums/viewtopic.php?f=43&t=166287#p1071988)_

OMG It works.   
Simple in the end..... but see Pitfalls at the bottom.  
Thanks Mal for putting me on the right track   
Don't use Motion-MMAL as in many articles and posts. It is much simpler.....  
So for the poor others trying this, here is what I did and the pitfalls.  
first install the hardware Pi Camera   
enable it in the config Raspberry Pi Configuration in the GUI

The first thing is motion can be used in its unmodified form. The trick to this is to get the PI camera to behave as a USB type webcam using the special add on module   
bcm2835-v4l2

first install motion in the straight forward way  
then the good news is that bcm2835-v4l2 is already on your system if you have the latest OS

To start it type To check it is working type you should see something like this  
crw-rw----+ 1 root video 81, 0 Nov 23 11:26 /dev/video0  
next get the bcm2835-v4l2 to load at start up using and add at the end   
bcm2835-v4l2  
then close the file  
reboot and check it is loaded by OK now time to edit the motion.conf file The changes you need to make are   
daemon on  
width 640  
height 480  
framerate 100  
stream_localhost off

Close the file  
next you need to fix an issue with motion or it only runs for a few seconds reboot PI

OK now time to start motion  
Then go to a browser on your network and type  
192.168.1.124:8081

The 192.168.1.124 is the IP of my Pi replace it with yours

and hey presto you should see the video from your pi camera.

PITFALLS  
I messed up initially as some of the articles incorectly us an underbar "_" instead of a dash "-" in the name of the bcm2835-v4l2

Also in some articles the lowercase l (12th letter in the alphabet) in v4l2 looks like a 1. It is a lowercase l  
This article has the mistakes but if you follow above you should be OK  
[https://learn.adafruit.com/cloud-cam-co ... opbox-sync](https://learn.adafruit.com/cloud-cam-connected-raspberry-pi-security-camera/dropbox-sync)  
I found the mods to motion.conf here  
[http://www.techradar.com/how-to/computi ... me-1314466](http://www.techradar.com/how-to/computing/use-a-raspberry-pi-to-remotely-watch-your-home-1314466)

Thanks also to Mal a star.
