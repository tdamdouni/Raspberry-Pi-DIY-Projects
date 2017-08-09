# Build a Raspberry Pi Security Camera Network

_Captured: 2017-05-06 at 16:08 from [pimylifeup.com](https://pimylifeup.com/raspberry-pi-security-camera/)_

![raspberry-pi-security-camera](https://pimylifeup.com/wp-content/uploads/2015/02/raspberry-pi-security-camera.jpg)

> _In this project I am going to make a Raspberry Pi security camera simply using the standard Pi camera such as the one I used in the time-lapse tutorial._

This is a cost effective way of getting a security camera up and running that you can view over the network and also have it so it is motion activated! So let's get to it.

![Pi Book Large](https://pimylifeup.com/wp-content/uploads/2017/04/pi-book-long.jpg)

If you want to see how to setup the Raspberry Pi security camera visually then check out the video i have prepared below. As always if you like what you see and want to stay up to date with all the latest and greatest projects, guides and much more then please subscribe.

##  Equipment:

You will need the following equipment in order to complete this Raspberry Pi security camera project.

[SD Card](https://pimylifeup.com/out/amazon/sdcard4gb) (8 GB+ Recommended) or [Micro SD Card](https://pimylifeup.com/out/amazon/microsdcard8gb) if you're using a Raspberry Pi 2, 3 or B+

##  Installing the Raspberry Pi Camera

Firstly before we do anything we need to have a Raspberry Pi camera. In this tutorial I use the normal IR camera and it works just fine however if it gets dark it can't see at all. (Which is probably not much good for a security camera). You can find the normal camera [here](https://pimylifeup.com/out/amazon/raspberrypicamera) or the non-IR camera [here](https://pimylifeup.com/out/amazon/raspberrypicameranoir).

If you're after for more information check out my [Raspberry Pi camera](https://pimylifeup.com/raspberry-pi-camera-vs-noir-camera/) guide for everything you need to know.

Secondly we will need to install the camera(If you haven't got one you can get one here), to do this go to the ribbon slot (the one directly behind the Ethernet port) using two fingers gently pull up on both sides of the connector.

![Clips & Ribbon Cabble](https://pimylifeup.com/wp-content/uploads/2014/12/clips-and-ribbon-cable.jpg)

Now the connector is open insert the ribbon cable with the metal leads facing away from the Ethernet port. Make sure it is nicely line up and then gently press back down on the connector. The cable should now be locked in place and we can now move onto the software.

On a side note if you want to install this into a more secure enclosure there is some great equipment you can buy or even design to do this. To keep this tutorial pretty basic I am not going to go into a heavily customized camera enclosure.

##  Installing MotionPie

I settled on using MotionPie as it seems to be an all in one solution for what I require and it also didn't involve as much fiddling around to get it to work.

![The MotionPie Logo](https://pimylifeup.com/wp-content/uploads/2015/02/MotionPie-logo.jpg)

  1. Download the Motion Pie SD Card Image from the [Motion Pie GitHub repository](https://github.com/ccrisan/motioneyeos/releases).
  2. You will need a formatting tool. Visit the [SD Association's website](https://www.sdcard.org/downloads/formatter_4/) and download SD Formatter 4.0 for either Windows or Mac.
  3. Follow the instructions to install the formatting software.
  4. Insert your SD card into the computer or laptop's SD card reader and check the drive letter allocated to it, e.g. G:/
  5. In SD Formatter, select the drive letter for your SD card (eg. G:/) and format

####  Install the Motion Pie Image onto the SD Card

  1. Now unzip the MotionPie img file so you can install it onto the Pi safely.
  2. Select the MotionPie img file and the drive letter your SD card is assigned (Eg. G:/)
  3. Confirm you have the correct details and click on Write.
  4. Once done you can safely remove your SD card from the computer.
![win32diskimager-motionpie](https://pimylifeup.com/wp-content/uploads/2015/02/win32diskimager-motionpie.jpg)

##  Booting/Setting up MotionPie

Now we're ready for boot up, so insert the SD Card, an Ethernet cord and the power cord. We will need to communicate to the Pi over the network rather than directly like I have done in most of the previous tutorials.

So now go ahead and boot the Pi up and then we can move onto getting it setup correctly.

Once the Pi has booted you will need to do the following:

  1. First we will need the IP or host name so we're able to connect to the Pi.
    * If you're using Windows simply go to network on the right hand side in the File Explorer.
    * You should see a computer names something like **MP-E28D9CE5 **
    * Go to your browser and add this to your browser bar eg. `**http://MP-E28D9CE5**`
    * You should now have the Motion Pie interface up.
  2. Alternatively you can find out the IP of the Pi by going to your router. Since all routers are different I will not go into how this is done. Please refer to your manufacturer's manual.
  3. To login as the admin go to key symbol in the upper left corner. The username is admin and the password is blank, this can be changed later.
  4. You can access all the setting for the camera stream here. If you're interested in altering these settings keep reading as I explain them as much as possible below.

Now we should have a working security hub that we can configure! Require the security camera to be wireless? No problem! Require to alert you with an email? No problem! Read on more to find out what the settings do in Motion Pie.

If you want to run more than one Pi cameras it is pretty easy to set this up so you have all the streams under in one window. You can even add a stream that has been setup using the [Raspberry Pi Webcam server](https://pimylifeup.com/raspberry-pi-webcam-server/) tutorial.

  1. First click on the 3 lines with dots on them in the upper left hand corner.
  2. Now up in the upper left hand corner and click on the dropdown box and select add camera.
  3. In here you have four settings to set up.
  4. **Device: **This is allows you to select where the camera is located(network/local) and type. (Eg. motionEye, MJEPG camera)
  5. **URL**: This is the URL to the other network camera. Eg. `http://othercamera:8080`
  6. **Username**: This is the username to the camera device. (If no username/password required leave the fields blank)
  7. **Password: **This is the password for the username chosen above.
  8. **Camera**: Select the camera you wish to add.

In the example below camera1 (Pi Camera) and camera2 (USB WebCam) are connected to the Pi running motionpie while camera3 is coming from a different Pi that was setup using the webcam server tutorial. This is a great way to setup a strong Raspberry Pi security camera network.

![Raspberry Pi Multiple Cameras](https://pimylifeup.com/wp-content/uploads/2015/06/Raspberry-Pi-Multiple-Cameras.jpg)

> _Connecting to the surveillance outside your network_

Now that you have your Raspberry Pi security cameras setup it might be worth considering allowing access to the central Pi so you can monitor your cameras elsewhere.

To do this simply head over to my guide on how to setup port forwarding and also how to setup dynamic DNS, you can find the guide at [Raspberry Pi Dynamic DNS & Port Forwarding](https://pimylifeup.com/raspberry-pi-port-forwarding/).

A few important bits of information you will need for the setting up the port forwarding.

  * The IP of your Raspberry Pi for example mine is 192.168.1.108
  * Internal port is 80.

Ensure you have also setup passwords on both the admin and the surveillance user to help avoid unwanted visitors.

Once setup should now be able to connect using your external IP address such as `XX.XXX.XXX.XXX:**80**` (80 should be changed to something else, I would recommended changing it to avoid easy access for unwanted visitors)

![Raspberry Pi MotionPie Interface](https://pimylifeup.com/wp-content/uploads/2015/06/Raspberry-Pi-MotionPie-interface.jpg)

> _General Settings_

In here you are able to set the administrator username and password. This account will have access to all the settings you're seeing at the moment.

Surveillance username and password can also be set in here this can be used to just access the camera interface.

To view all the settings available to set turn the show advanced settings to **on.**

Turn this on if you plan on connecting to the network via a wireless dongle. There are two things you will need to fill in here.

  1. **Network Name** - Enter the network name/SSID you wish to connect to in here.
  2. **Network Key** - Enter the network password/network key in here for the network you're connecting to.

Once done you should be a able to disconnect the Ethernet cord and remain connected to the network.

Under this menu you're able to set certain settings regarding the Raspberry Pi camera device.

  1. **Camera Name**: Set this to whatever you would like the camera to be named. For example kitchen would work well for a camera in a kitchen.
  2. **Camera Device**: You're unable to edit this one but this is the device name of the camera.
  3. **Light Switch Detection:** Enable this if you want sudden changes such as a light being switched on to not be treated as motion. (This will help prevent false positives)
  4. **Automatic Brightness:** This will enable software automatic brightness, this means the camera software will make adjustments for the brightness. You don't need to activate this if your camera already handles this.
    * In here you change the brightness, contrast and saturation of the video of the camera.
  5. **Video Resolution: **Here you can set the video resolution of the camera. The higher the resolution the more room it will take up and the more bandwidth it will need to use in order to stream the footage. I set mine to 1280×800 and that seems to work perfectly fine.
  6. **Video Rotation: **You can rotate your video from the Raspberry Pi security if you're finding that it is looking the wrong way.
  7. **Frame Rate: **This sets the amount of frames that will be sent be every second. The higher this is the smoother the video but again this will increase the storage used and bandwidth.

Under this menu you can specify where you would like the files stored for the Raspberry Pi Security Camera. This can be a custom path on the Pi, the predetermined path or the network path.

In here you can set the text overlay on the output of the camera. By default the left text reads the camera name and the right read the time stamp (Today's date and current time).

This menu you're able to set the video streaming options, this is the video you see in the browser.

  * **Streaming Frame Rate**: This is exactly the same as mentioned above under video device.
  * **Streaming Quality: **You can reduce the video streaming quality. This is good to reduce if you need to access the camera on a low bandwidth device often.
  * **Streaming Image Resizing**: Enable this if you want MotionPie to resize the images before being sent to a browser. (Not recommended on a Pi)
  * **Streaming Port: **This is the port that the device will listen to for connections looking to view the stream. Eg. http://motionpie:8081
  * **Motion Optimization: **This will reduce the frame rate whenever no motion is detected. This will save you bandwidth.

You can also see three URLs that can be used to access different footage. These URLs are very important if you have multiple cameras per Pi as each camera will have a unique port that you listen to the stream on.

Here you can set the Raspberry Pi security camera to take still images whenever motion is triggered, during specific intervals or all the time.

In here you can activate the Raspberry Pi security camera motion detection that is included in the software. You are able to make adjustments to the settings here so that you can get better motion detection.

In here you can set the Pi to record movies whenever motion is detected.

You're able to set up email notifications, webhook notifications or even run a command whenever motion is detected. This will allow you to be notified whenever activity is detected on the cameras, perfect if they are monitoring areas with low traffic.

Here you can set the days and the hours of operation you would like the system to be monitoring (If you leave this off then it is 24/7). This option is perfect if you only need it running during specific hours.

##  Summary

The Raspberry Pi security camera system is a great way to have multiple cameras hooked up both locally and over a network. All the extra setting motion pie provides allows you to have a strong functioning security hub for your home, office or wherever you're setting this up.

I hope this tutorial has helped you in creating a fantastic Raspberry Pi security camera network. If you have had any problems, provide feedback or have a great setup you would like to share then feel free to drop a comment below. If you're after more [great Raspberry Pi projects](https://pimylifeup.com) then be sure to check out many other great tutorials.

![Cayenne Large](https://pimylifeup.com/wp-content/uploads/2016/06/cayenne-raspberry-pi-long-v2-border.jpg)
