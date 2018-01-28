# ScoutBot—Pi Bot With Camera

_Captured: 2017-11-18 at 23:34 from [www.instructables.com](http://www.instructables.com/id/Scout-Bot/)_

![](https://cdn.instructables.com/FZJ/AM4N/J9JFY2Q1/FZJAM4NJ9JFY2Q1.MEDIUM.jpg)

Here, we present our Raspberry Pi 8 DOF Wi-Fi quadruped robot. The robot is featured video vision streaming and Wi-Fi control via simple web UI. We release all information to people to build it by themselves. Any Pi version from 1A+/1B+ to 3 and Zero/Zero W can be used to build this robot. Below figures show an implementation using Pi B+ and camera module V1.3.

## Step 1: Preparation

![](https://cdn.instructables.com/FIS/HERG/J9JFY2S2/FISHERGJ9JFY2S2.MEDIUM.jpg)

To build one, you will need following items. The electronic components can be found in the online store such as Taobao, Amazon, etc.

  * Nano size WiFi USB dongle or equivalent for 1A+,1B+, 2 & Zero
  * Raspberry Camera V1.3 (optional if no vision video streaming)
  * 3D printed STL model files, download [here](https://drive.google.com/file/d/0ByZam-eTh4SXb2pwVkxCMHpzaUU/view)
  * Robot System SD card image: The image is based on [ LEDE Project](https://lede-project.org/). The user guide is applicable to the robot for other system settings. You see _Step 3: Installation of System Image_ for writing images to SD card. SD card bigger than 256MB can be used since the size of the image file is less than 256MB. There are 3 images respective to the different version of Pi, download below:  

  * 8 servo motors - [Tower Pro MG996R](http://www.towerpro.com.tw/product/mg995-robot-servo-180-rotation/) or compatible
  * 3.7V [18650 battery pack](http://www.batterysupports.com/36v-37v-2-18650-5200mah-2p-lithium-ion-liion-battery-pack-p-44.html) \- two in parallel

Prior to build or assemble the robot, you need to 3D-print the models and preparing the SD card for Pi.

## Step 2: 3D Printing

![](https://cdn.instructables.com/FR2/ZN8X/J9JFY39Y/FR2ZN8XJ9JFY39Y.MEDIUM.jpg)

Those implementations in demo were printed in PLA. The models were sliced using Cura. Here are the suggested parameters for slicing the robot models to print. You may adjust to fit the 3D printer you're using.

  * layer height: 0.2mm 
  * shell thickness: 1mm 
  * bottom/top thickness: 1.2mm 
  * support: needed 
  * adhesion type: none 
  * fill density: 10%

## Step 3: ​Installation of System Image 

![](https://cdn.instructables.com/F96/G0YV/J9JFY39B/F96G0YVJ9JFY39B.MEDIUM.jpg)

You will need to use an image writing tool to write the image onto your micro SD card.

Etcher is a graphical SD card writing tool that works on macOS, Linux and Windows, and is the easiest option for most users. Etcher also supports writing images directly from the zip file, without any unzipping required. To write your image with Etcher:

  * Download [Etcher](https://etcher.io/) image writer
  * Connect an SD card reader with the SD card inside
  * Open Etcher and select the image file you wish to write to the SD card
  * Select the SD card you wish to write the image to
  * Review your selections and click _Flash!_ to begin writing data to the SD card

## Step 4: WiFi Setup

![](https://cdn.instructables.com/F14/NG6T/J9JFY3G7/F14NG6TJ9JFY3G7.MEDIUM.jpg)

![](https://cdn.instructables.com/FSU/WBXH/J9JFY3QM/FSUWBXHJ9JFY3QM.SMALL.jpg)

![](https://cdn.instructables.com/F85/5U73/J9JFY3QU/F855U73J9JFY3QU.SMALL.jpg)

![](https://cdn.instructables.com/FQN/FDEJ/J9JFY3QX/FQNFDEJJ9JFY3QX.SMALL.jpg)

![](https://cdn.instructables.com/F86/VCLJ/J9JFY3R1/F86VCLJJ9JFY3R1.SMALL.jpg)

![](https://cdn.instructables.com/F1Z/NY6S/J9OWF3AX/F1ZNY6SJ9OWF3AX.SMALL.jpg)

After you install the system image to the SD card, next step is to setup the Wi-Fi connection.

  * Connect your computer to the LAN port of Pi
  * Optionally, connect Pi to an HDMI monitor for booting messages
  * Connect the USB Wi-Fi dongle to USB port if not Pi 3
  * Insert the SD card to Pi
  * Power on Pi to boot, the green LED will be flashing for few seconds
  * After boot up, the Pi becomes an Internet and WiFi router, it will allocate IP address in the range of [ http://192.168.1.1/. ](http://192.168.1.1/.) to any network devices connected to it via LAN port or WiFi.

## Step 5: Robot Assembly

You must have 3D printed models and the SD card ready. If you have those ready, watch assembling video at below.

## Step 6: Play!

Firstly is to join the robot WiFi network. Initially the SSID is LEDE. The WiFi password is the one you set in above _Step 4: WiFi Setup_. If you are success to join the WiFi network, you can access the web control interface with the URL **http://192.168.1.1:8080/robot.html**. You can control the robot as the previously video demo shows.
