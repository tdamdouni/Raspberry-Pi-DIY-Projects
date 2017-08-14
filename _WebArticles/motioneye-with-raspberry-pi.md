# motionEye with Raspberry PI

_Captured: 2017-08-14 at 10:11 from [www.howtoembed.com](http://www.howtoembed.com/projects/raspberry-pi/95-motioneye-with-raspberry-pi)_

**motionEye** is a web frontend for a Linux video surveillance program called **motion**. This tutorial will walk you through the necessary steps to install and configure **motionEye** on a **Raspberry PI**. You will build yourself an intelligent video surveillance system based on afordable components and opensource software.

Special thanks go to Kenneth Lavrsen, the original author of **motion**, a great piece of software that does all the hard work for this project.

## motionEye Features

  * web interface, responsive design
  * user/password protection (administrator and normal user)
  * mjpg streaming
  * motion detection, output to jpeg and avi files
  * timelapse capturing
  * browsing, previewing and downloading of media files
  * advanced camera settings

## Required Hardware

  * a [Raspberry PI](http://downloads.element14.com/raspberryPi1.html?COM=raspi-group)
  * a micro USB power supply (5V, 1A)
  * an SD memory card (at least 4GB)
  * an [USB WiFi adapter](http://elinux.org/RPi_USB_Wi-Fi_Adapters) (optionally, if an ethernet connection is not available)

## Screenshots

![motioneye1](http://www.howtoembed.com/images/thumbnails/images-users-ccrisan-motioneye1-800x393.png)

![motioneye2](http://www.howtoembed.com/images/thumbnails/images-users-ccrisan-motioneye2-535x398.png)

![motioneye6](http://www.howtoembed.com/images/thumbnails/images-users-ccrisan-motioneye6-800x393.png)

## Installing The OS

Download the latest version of the [Raspbian](http://www.raspberrypi.org/downloads) operating system. [Here](http://elinux.org/RPi_Easy_SD_Card_Setup) you'll find instructions on how to transfer the OS image to the memory card. Once the OS is on the SD card, boot your **Raspberry PI**. The commands presented with the following steps are to be executed exclusively in a terminal on the **Raspnberry PI**.

Before moving on, it is recommended that you update the packages on your system:

`1`
`sudo` `aptitude update && ``sudo` `aptitude upgrade`

## Installing The Required Packages

**motionEye** requires a few libraries and extra programs. Install them with the following command:

`1`
`sudo` `aptitude ``install` `python-tornado python-jinja2 python-imaging motion ffmpeg v4l-utils`

Choose the latest version from the [downloads](https://bitbucket.org/ccrisan/motioneye/downloads) list (use the _Tags_ tab) and download it to /home/pi. Unpack (replacing xyz with the code in the filename):

`2`
`tar` `zxvf ccrisan-motioneye-xyz.``tar``.gz`

`3`
`mv` `ccrisan-motioneye-xyz motioneye`

`4`
`cd` `motioneye`

After this step you'll have **motionEye** installed in /home/pi/motioneye, your current directory.

Create a settings.py file from the existing template:

The default settings are good in most of the cases. If you wish to customize **motionEye**, you can later edit the settings.py file - you'll find a short description next to each of the available options.

Follow this step only if you use the CSI Camera Board instead of a regular USB webcam.

## limitations

  * only a single camera module can be used with **motionEye**
  * given the high resolution at which this camera can work, it is possible that the performance of **Raspberry PI** be not enough (processing of large images is CPU-hungry)

## the uv4l driver

The camera module does not have a native **v4l** driver (at the time of writing). There is however a set of [userspace components](http://www.linux-projects.org/modules/sections/index.php?op=viewarticle&artid=14) that emulate the **v4l** interface for such a camera module.

UPDATE: now it has :)

## the bcm2835_v4l2 module

Append bcm2835_v4l2 to /etc/modules

## troubleshooting

  * make sure you run the latest version of the Raspberry PI firmware
  * make sure you have enabled the camera module in raspi-config
  * don't overclock your PI too much, using the camera module causes core overheating already
  * allocate at least 64MB of RAM to the GPU

**motionEye** does not need _root_ privileges to run; it can be started directly from the directory where it was extracted:

If everything was properly installed and configured, **motionEye** should emit an info message saying that the _server started_. Now point your browser to http://raspberrypi:8765 (replacing raspberrypi with the IP adress of your device). The **motionEye** web interface should show up. Use admin with no password, when prompted for authentication. Start by adding a new camera and feel free to experiment with the various available settings.

When you're done "experimenting", hit _ctrl-c_.

You'll probably want **motionEye** to start automatically at boot. Add the following line to /etc/rc.local (right before the exit 0):

This will start the server with the user pi, put the log into motioneye.log and run the process in the background.

The **motion** daemon will be run automatically by **motionEye** \- it should not run at startup.

Below you can find affiliate linked images to buy directly from Amazon. Thank you for supporting this site!

  * 
