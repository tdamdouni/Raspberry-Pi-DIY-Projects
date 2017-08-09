# Getting Started with Raspberry pi and Node.js

_Captured: 2017-08-08 at 18:49 from [thejackalofjavascript.com](http://thejackalofjavascript.com/getting-started-raspberry-pi-node-js/)_

Did you know that there will be [6.18 billion devices](https://gigaom.com/2014/02/13/step-aside-6-billion-new-devices-will-connect-to-the-internet-in-2014/) connected to the internet by the end of 2014 and a whooping 19.42 billion devices between 2015 and 2017. Imagine the fight for bandwidth!

With so many devices connected to the Internet, the next big thing for us is the "Internet of Things" or the _IoT_. If you do not already know what Internet of Things is, check out this video

So what can we really do with IoT, take a look at this

Awesome right! A piece of hardware, some internet and a world full of opportunities.

This post marks the beginning of a bunch of posts that are targeted at integrating Hardware/embedded devices like sensors and motors with the internet and build meaningful and smart apps that would know and do things as per your instructions taking us one step closer to pure Artificial Intelligence!

In this post, we will take the first few tiny steps towards IoT. For most of the experiments, I am going to use [Raspberry Pi B+](http://www.raspberrypi.org/products/model-b-plus/). And as you might have guessed, all the programming we are going to do will be in Javascript.

First we will take a look at connecting our pi to our computer and next, we will install Node.js.

So, let us get started

## What is Raspberry pi?

## Purchasing a Pi

I am not going to provide links on where and how you can purchase Raspberry pi. But if you have issues locating one in your neighbourhood, do drop a comment and I can help you.

## Connecting Pi to your Computer

We will take a look at connecting the pi to both a Mac as well as Windows machines. There are numerous ways out there how you can connect your pi with your computer. I found the below method to be the easiest.

To connect the pi with your computer, we will be using an Ethernet cable.

The assumption is that you are using a wifi connection to connect your computer to the internet.

As long as we are not detaching the pi from your computer, this way to connect to the pi should work fine. When required, I will put out instructions to connect your pi via a USB wifi dongle.

### Setup Pi on your mac

**Step 1** : Insert the SD card into place on your Raspberry pi

**Step 2** : Connect the power cable to the pi. You should see a red light blinking on the board

**Step 3** : Connect one end of the ethernet cable to your pi and connect the other end to your mac

**Step 4** : We will setup a shared network between your Mac and the pi. The Mac will share its network with pi over the ethernet cable.

For that, on your Mac, open _System Preferences_.

Click on sharing and enable Internet sharing from the left tree as show below.

On the right hand side, select Ethernet. This will now enable Internet sharing between your Mac and any device you connect on your ethernet port.

**Step 5** : Now, Open a new terminal and run

And you should see something like

Note : If you do not see any devices listed after you enable the ethernet sharing, switch off the pi wait for 10 seconds and start it back on. Now run the above command again and you should see the list of ip addresses.

One of the above listed ip addresses belongs to your pi. I do not have a sure shot way of telling which one. So we will be taking each ip address and running the below command

After testing out all, I came to know my pi's ip address is 192.168.2.2 . So, when I run ssh pi@192.168.2.2, it will ask for my password.

The password for your pi is _raspberry_. And once you are successfully authenticated, you should see this

Now, you are successfully connected to you pi!

**Step 6** : Connect to the pi's GUI. From the command prompt shell (which we established above), run

sudo apt-get install tightvncserver

This will install tightvncserver on the pi. Using this, we can interact with the pi's gui using our mac's keyboard and mouse.

After _tightvncserver_ is setup, we need to setup a password run

tightvncserver

Now, to enable sharing your pi's GUI, run

This will start vnc sharing. Now, on you Mac, open up safari and navigate to

from the address bar. This is the ip address of the Mac. Safari will prompt for the ip address again. Press enter and a screen sharing should start.

Voila!! your Raspberry pi's GUI from your Mac!

The above process is simple but the only problem is, we need to run

every time we restart the pi.

To work around that, we will add this command to the list of boot tasks. So as soon the pi boots, the vncserver will start.

For that let us go back to the ssh shell.

run the following commands in sequence

This will switch to superuser

cd /etc/init.d/

Next, we will create a new file named vncboot. Run

Copy everything from below and paste it in the window

12345678910111213141516171819202122232425262728293031323334353637 
### BEGIN INIT INFO# Provides: vncboot# Required-Start: $remote_fs $syslog# Required-Stop: $remote_fs $syslog# Default-Start: 2 3 4 5# Default-Stop: 0 1 6# Short-Description: Start VNC Server at boot time# Description: Start VNC Server at boot time.### END INIT INFO#! /bin/sh# /etc/init.d/vncbootUSER=rootHOME=/rootexport USER HOMEcase "$1" instart)echo "Starting VNC Server"#Insert your favoured settings for a VNC session/usr/bin/vncserver :0 -geometry 1280x800 -depth 16 -pixelformat rgb565;;stop)echo "Stopping VNC Server"/usr/bin/vncserver -kill :0;;*)echo "Usage: /etc/init.d/vncboot {start|stop}"exit 1;;esacexit 0

and it should like

Now press ctrl + x and you will be asked to save the file (_bottom of the screen_). Press Y and you will be asked for the file name. Name it _vncboot_. Press enter and you should be out of the nano editor.

Now, we will set up permissions to make this file executable. Run

Finally we will enable dependency based boot sequencing. Run

update-rc.d vncboot defaults

And you should see a console out like

Now, we will test this out by rebooting pi. Back to the ssh terminal run

And you should see a log like

And the connection will be terminated. Lets give ~30 seconds time for the pi to reboot.

Back to Safari, we will launch a new vnc connection as we did earlier and you should see the pi desktop.

If you see a message like

ssh into your pi and run the following commands

Now setup the password. Reboot the pi and you should be able to connect to your pi using vnc on bootup.

Note : All the above instruction are taken from [here](http://www.raspberrypi.org/documentation/remote-access/vnc/).

### Setup Pi on your Windows

**Step 1** : Insert the SD card into place on your Raspberry pi

**Step 2** : Connect the power cable to the pi. You should see a red light blinking on the board

**Step 3** : Connect one end of the ethernet cable to your pi and connect the other end to your PC

You can follow this easy to set up video to connect your pi to your windows machine

Once you get the ip address, please follow step 6 from above. Instead of using Safari, we will use tightvnc software to view the screen on windows.

You can find all the instruction to run Tightvnc on windows [here](http://www.raspberrypi.org/documentation/remote-access/vnc/windows.md).

If you want to interact with the pi over command line, you can install putty and then tunnel through to the pi.

Now that we have connected pi to our computed, we will go ahead and install Node.js on pi.

## Installing Node.js on pi

If you are new to Node.js, I would recommend going through the following posts

You can run the below steps over ssh or you can run it using xterminal (as root) from the GUI. I will be running the below steps from the terminal (ssh on Mac/putty on windows). This will take comparatively less time when working with a GUI.

First we will update and upgrade our pi. Run

sudo apt-get update -y && sudo apt-get upgrade -y

_This will take quite some time, if you are running this for the first time. (~ 1 hour)_

Next, we will download the latest version of Node-ARM

wget http://node-arm.herokuapp.com/node_latest_armhf.deb

Install it by running

sudo dpkg -i node_latest_armhf.deb

If everything works fine without issues, you can run

and you should see the installed Node's version.

You can also start off a Node REPL and log something like

Hope this post gave you a decent idea as how to setup Node.js on the Pi. If you think there is a more easy way of connecting the Pi to a computer, please do share.

Thanks for reading! Do comment.  
@arvindr21
