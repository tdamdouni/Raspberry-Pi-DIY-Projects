# Cluster of Raspberry Pi Zeroes

_Captured: 2016-01-07 at 01:07 from [www.redrobe.com](http://www.redrobe.com/mike/cluster-of-raspberry-pi-zeroes/)_

No ethernet required - each pi zero is both powered and networked by a single usb lead !

![PiCluster](http://www.redrobe.com/mike/wp-content/uploads/2016/01/CXjsR6yWwAAyAQa-300x240.jpg)

The magic happens in the "gadget mode" firmware of the PI Zero. Since it doesn't have the USB HUB chip in the way like other models (B / B+/pi2) it can be configured in device mode.

This makes it appear to any PC (or pi B+ / pi-2) as a virtual usb network adaptor - so you can immediately access it as though it were ethernet connected.  
It also possible to set it up to appear as mass storage device, keyboard, mouse or any other usb peripheral!  
(More discussion on the [pi forums](https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=129653) by DaveB and others)

Power isn't a problem as each Pi Zero only uses around 150mA

**

Convert a Pi Zero to gadget mode:

**

1\. Start with an fresh image of Raspbian Jessie <https://www.raspberrypi.org/downloads/raspbian/>

2\. copy this file to the boot partition: <https://dl.dropboxusercontent.com/u/1122948/temp/PiOTG-Test/PiZeroEthernet.tar.gz> (thanks to gbaman1 / Andrew Mulholland)

or download it on the pi itself:

`wget https://dl.dropboxusercontent.com/u/1122948/temp/PiOTG-Test/PiZeroEthernet.tar.gz`

2\. `sudo tar xvzfC /boot/PiZeroEthernet.tar.gz /tmp/`

3\. `sudo cp -R /tmp/PiZeroEthernet/fat32/* /boot/`

4\. `sudo cp -R /tmp/PiZeroEthernet/ext4/lib/* /lib/`

5\. Now give it a static ip address by editing `/boot/cmdline.txt` and adding this on the end: `ip=169.254.64.64:::255.255.0.0`

(for the lazy all the above has been done on this downloadable image:  
<http://sourceforge.net/projects/pizero-usbhost/> [768MB])

Now the pi Zero can be plugged into a pi2 / B+ (or a PC !) and you can SSH directly to it on the ip you set above ( 169.254.64.64)

[more to follow]
