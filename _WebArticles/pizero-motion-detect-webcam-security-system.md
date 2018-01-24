# Pizero Motion Detect Webcam Security System

_Captured: 2017-11-11 at 10:10 from [www.instructables.com](http://www.instructables.com/id/Pizero-Motion-Detect-Webcam-Security-System/)_

![](https://cdn.instructables.com/FXI/3V25/J9OJ931A/FXI3V25J9OJ931A.MEDIUM.jpg)

This system uses a pizero, wifi dongle and an old webcam in a customized matchbox case. It records motion detect videos at 27fps of any significant movement on my driveway. It then uploads the clips to a dropbox account. Also can view the logs and change the configuration via dropbox.

## Step 1: Setting Up the Prerequisites

First update the operating system to the latest version as described [here](https://www.raspberrypi.org/documentation/raspbian/updating.md).

Then set up the wifi as described [here](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md).

Then you will need to set up OpenCv. There are good instructions on how to do this on [pyimagesearch](https://www.pyimagesearch.com/2015/12/14/installing-opencv-on-your-raspberry-pi-zero/). If you are going for version 3.0 expect it to take a long time. One of the steps takes 9 hours to make. You will also need the python bindings which are explained on that page.

When you have got this all up and running you are ready to download the motion detect software.

## Step 2: Setting Up the Motion Detect Software

![](https://cdn.instructables.com/FXQ/Z0F8/J9OJ932Q/FXQZ0F8J9OJ932Q.SMALL.jpg)

The code can be found on [bitbucket](https://bitbucket.org/dani_thomas/multimotiondetect). Copy these files by using

or if you prefer download them individually.

The main part of this system is multiMotionDetect.py. It uses a lot of the multiprocessing queues and events.

First of all you need to decide where you want the video images stored MotionVideos and set this value in the globalConfig.json file. Then copy the config.json.txt and maskedAreas.json.txt to the root of this folder.

_If you would rather use a simple logger_ rather than the socket logger (below) change the import miaLogging to

_import logging_

_logging.basicConfig(filename='example.log',level=logging.DEBUG)_

and remove the log receiver from the motionDetect file and everything else should work fine.

_If you want to run the motion detect automatically on startup. _

First edit the script and check that the homedir points to where you have multiMotionDetect.py, then copy the motionDetect file to /etc/init.d ie

_cp motionDetect /etc/init.d/motionDetect_

Should be executable already but

_chmod +x /etc/init.d/motionDetect_

Finally register the script with

_sudo update-rc.d motionDetect defaults_

You can also start, stop and restart the system with

_sudo /etc/init.d/motionDetect start|stop|restart_

By default the miaLogReceiver socket logging will start at the same time. The other three programs are independent but use the same socket logger (but could easily be converted). I call all these using a cron script of different intervals. [For instructions look here](https://www.computerhope.com/unix/ucrontab.htm).

** CheckRunning.py** checks that multiMotionDetect.py is running and does a restart if not.

**fileMaint.py** does housekeeping on the video folders removing these after the given number of days. It removes subdirectories of the motion video folder set in the first paragraph. It checks that they start with "MV" so make sure you haven't got another directory of importance starting with the same characters within that folder.

## Step 3: Accessing the Videos and Configuration Through Dropbox

![](https://cdn.instructables.com/FNA/VY5V/J9OJ9332/FNAVY5VJ9OJ9332.MEDIUM.jpg)

Finally if you want to view your videos, logs and config files remotely then you will need to set up dropbox.

First get a dropbox account which is free. Then set up the API for python -[https://www.dropbox.com/developers/documentation/...](https://www.dropbox.com/developers/documentation/python#tutorial) This includes downloading the sdk and registering the app to access the API.

When you've got a key enter that in the globalConfig.json file. More info on the system can be found on my blog [dani cymru - cyber renegade](https://danicymru.wordpress.com/2017/10/23/motion-detection-security-camera-using-pizero-and-opencv/) If you find anything of interest or any questions please put a comment on the blog.

## Comments
