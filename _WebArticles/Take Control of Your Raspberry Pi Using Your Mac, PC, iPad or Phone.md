# Take Control of Your Raspberry Pi Using Your Mac, PC, iPad or Phone

_Captured: 2015-12-19 at 13:16 from [computers.tutsplus.com](http://computers.tutsplus.com/tutorials/take-control-of-your-raspberry-pi-using-your-mac-pc-ipad-or-phone--mac-54603)_

In this tutorial I will show you how to setup your Raspberry Pi for remote control on your home network or over an internet connection. This is really useful if you want to run your Pi as a 'headless' machine without the need for its own monitor, mouse and keyboard - instead you can use your home computer, ipad or even mobile phone to access and control your Pi.

I'm going to be using two methods to remotely control the Pi -- SSH (Secure SHell) which provides access to the Pi's command line interface, and VNC (Virtual Network Computing) which replicates the graphical desktop. Of the two SSH is much quicker as it's just text based, but VNC is probably easier to use on a tablet or smartphone.

## Prerequisites

You'll need:

  * a Raspberry Pi, model A or B, and 
  * a basic understanding of using the console.

## Setting Up Your Raspberry Pi

First you need to get your Raspberry Pi up and running with the latest version of Raspbian. The easiest way to do this is by downloading the _New Out Of the Box System_ (NOOBS) installer from the [Raspberry Pi website](http://raspberrypi.org/downloads), and unpacking it to an SD card prepared with the SD Card Association's [formatting tool](https://www.sdcard.org/downloads/formatter_4/).

Switch on your Raspberry Pi, with a monitor and keyboard attached, and go through the prompts on the screen to install the recommended Raspbian software.

Next you need to run the **pi config** program. If you are installing Raspbian for the first time you'll see this once the pi has booted up - alternatively you can access it by opening a terminal window and typing:
    
    
    sudo raspi-config

This will load up the blue configuration screen.

First task is to change your default Pi password. Choose **change user password** and enter your new password twice to confirm.

Next enable SSH server -- this enables us to talk to your pi using a command line interface from another computer.

**Advanced options > SSH > Enable**

Save and exit the configuration tool.

The next steps all use the Raspberry Pi's command line - this is the first thing you see after the Pi has booted up. If you're running the Pi's desktop you can access the command line by running the console app.

Now we need to find out the IP address of your Pi. If you haven't already, make sure your Pi is connected to your home network - either with the ethernet cable, or with a WiFi adapter.

Run **ifconfig** to find out the IP address of your Pi:

This will display some information about how your Pi is connected to the network -- for example:

`eth0 Link encap:Ethernet HWaddr b8:27:eb:39:3e:7b  
inet addr:192.168.1.93 Bcast:192.168.1.255 Mask:255.255.255.0  
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1  
RX packets:95549 errors:0 dropped:0 overruns:0 frame:0  
TX packets:17775 errors:0 dropped:0 overruns:0 carrier:0  
collisions:0 txqueuelen:1000  
RX bytes:7387491 (7.0 MiB) TX bytes:20279618 (19.3 MiB)`

The information you're looking for will start `inet addr:192.168.1.` followed by a number - in the example above the IP address of the Pi is:

`192.168.1.93`

Make a note of the number, if you reboot your Pi this number will change so you'll need to go through the steps again to find it. In this tutorial I'll refer to this number as 192.168.1.(number)

That's all you need from the Pi. Leave it running, but we can do the next steps from another machine attached to the same network.

## Connecting via SSH

To connect via SSH you'll need a remote access app. You can use any remote desktop app that supports SSH and VNC.

For SSH -- On the Mac you can use the built in terminal app, or try an app like [Remoter](http://remoterlabs.com/main/) which supports VNC as well. On a PC you can use [puTTY](http://www.putty.org/) and on an Android phone [Connect Bot](https://play.google.com/store/apps/details?id=org.connectbot&hl=en).

Regardless of the software you use, the SSH settings will be `192.168.1.(number)` for host, `22` for the port number, `pi` for the username, and your Pi's password to login.

For example on the Mac open the console and type:

`ssh pi@192.168.1.(number)`

You'll be asked if you want to continue connecting? Select **yes**.

Log in with your username and password. You can now control your Pi from your new machine.

To connect to your Raspberry Pi with Remoter on the iPad, start the app and click on **Discovery List > Add Session Manually**. On the **Server Type** choose **SSH**.

In the box that says **SSH Hostname** enter the Pi's IP address that was determined earlier: **192.168.1.(number)** then choose **Manual**. Leave the **SSH Port** setting at **22** and in **SSH Username** enter your Pi username and **SSH Password** your Pi password.

![ipadSSHsetup](https://cdn.tutsplus.com/mac/uploads/2013/10/ipadSSHsetup.jpg)  


> _No IP configuration screen_

Then connect -- you might get a warning message (just accept) and then you should be seeing the Linux prompt.

## Creating a Static IP Address for Your Pi

Next, I'm going to fix the IP address of the Pi. Most home networks use something called _DHCP_, or _Dynamic Host Configuration Protocol_, to assign a temporary IP address to the devices on your network -- so if you were to switch off your pi and reboot, you may be unable to reconnect using the same IP address.

In the Raspberry Pi's console type:
    
    
    cd /etc/network
    sudo nano interfaces

This launches nano which is a basic text editor. The following settings will depend on your Router and most routers will give you this information if you visit their configuration page. This can usually be found on your network by typing [192.168.1.1](http://192.168.1.1/) into a web browser.

The following settings worked for the BT Homehub version 3, for example. Again replace `address 192.168.1.(number)` with your Pi's IP address.
    
    
    auto eth0
    iface eth0 inet static
    address 192.168.1.(number)
    gateway 192.168.1.254
    netmask 255.255.255.0
    network 192.168.1.1
    broadcast 192.168.1.255

Press **Control O** and then **Enter** to save, followed by **Control X** to exit.

You might want to test your settings -- either by using the `Ping` command, or by attaching a monitor, keyboard and mouse directly to the Pi and firing up the web-browser. The Pi should be able to connect to the internet.

## Installing VNC

Installing tightvncserver allows me to use the Pi desktop on another machine. Again you'll need a remote access client. On the PC you can use [tightVNC](http://www.tightvnc.com/) which also has a client application for android as well. On the Mac and iPad you can use [Remoter](http://remoterlabs.com/main/).

On the Pi type:
    
    
    sudo apt-get install tightvncserver

once it's finished, start VNC by typing
    
    
    tightvncserver

Unlike SSH tightVNC doesn't automatically start each time you reboot the Pi.

Now create a new session in your VNC client. You'll need to choose VNC/ScreenSharing, and add the Pi's IP address `192.168.1.(number)` as the hostname. If it prompts you for a VNC port use `5901`. The username and password are what you originally set for your Pi on the configuration page.

![VNC Ipad screenshot](https://cdn.tutsplus.com/mac/uploads/2013/10/ipadscreen.png)  


> _Raspberry Pi on your iPad_

That's it - you can now control your pi from an ipad or mac on your local network.

## Accessing Your Pi Over the Internet

Assuming you have a residential broadband account, I'm using BT broadband, most ISP's use dynamic IP addresses which are assigned each time you connect to the internet.

I'm going to use a service called No IP, which uses a program on your Pi to find out it's address, to update a domain to point to this address. We'll also need to open a port in the home router to allow connections to the Pi.

First sign up for an account at [noip.com](http://www.noip.com/) \- there is a free option available, or you can opt to pay $15 a year for a service with more features.

Add a **Host**, and choose a **Hostname** from the list of options. Then choose the **DNS Host (A)** option and save. The settings I've been using are below.

![No IP configuration](https://cdn.tutsplus.com/mac/uploads/2013/10/no-ipconfig.gif)  


> _No IP configuration screen_

Next, on the Pi download and install the noip software:
    
    
    mkdir /home/pi/noip
    cd /home/pi/noip
    wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
    tar vzxf noip-duc-linux.tar.gz
    cd noip-2.1.9-1
    sudo make
    sudo make install
    sudo /usr/local/bin/noip2

Whilst installing it will prompt you for your **noip.com** login details.

Finally you need to open a port in your router to allow traffic through -\- there is a [port forwarding guide for most routers available here](http://portforward.com/english/routers/port_forwarding/) \-- typically opening the Router's configuration in your browser, finding the advanced menu and adding the local fixed IP address of my Pi and SSH and VNC to the forwarding options.

Now, when you connect to your Raspberry Pi using SSH or VNC, you can connect using your NoIP.com hostname, rather than the IP address and this will work over any internet connection.

## Conclusion

In this tutorial I have shown you how to connect to your Raspberry Pi, over the internet, using SSH and VNC. This is a really useful starting point for controlling your Pi remotely and thinking about remote control hardware projects.

You might also want to try out a few different SSH and VNC hosts on different platforms.
