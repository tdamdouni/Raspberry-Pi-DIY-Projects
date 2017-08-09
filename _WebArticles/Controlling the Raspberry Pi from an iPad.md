# Controlling the Raspberry Pi from an iPad

_Captured: 2015-12-19 at 13:19 from [whatapalaver.co.uk](http://whatapalaver.co.uk/2013/12/controlling-raspberry-pi-from-ipad/)_

After the frustrations of the first few days I am now coming on in leaps and bounds with the [Raspberry Pi](http://whatapalaver.co.uk/category/raspberry-pi/). Today I managed to set up my iPad so it can take control of the RPi. This means that the Raspberry Pi can be tucked away in corner, running headless while the iPad seizes control so I can make use of its keypad and monitor.

This means that I can now log on to RPi from anywhere that I have internet access - my main desire for doing this is so that I can run python and start learning to program from the mobile convenience of my iPad.

Before you can connect remotely to your Raspberry Pi you need to have connected it to the internet. You can do this by plugging it into an ethernet cable or as I have done by using the [Edimax Wireless Nano USB Adapter](http://www.amazon.co.uk/gp/product/B003MTTJOY/ref=as_li_qf_sp_asin_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B003MTTJOY&linkCode=as2&tag=warriorwomen-21), which is a fantastic piece of kit, its tiny and was a doddle to install.

## Apps Required to Connect to your Raspberry Pi from an iPad

![Apps to connect iPad to Raspberry Pi](http://whatapalaver.co.uk/wp-content/uploads/2013/12/20131227-171630.jpg)

> _[Apps to connect iPad to Raspberry Pi](http://whatapalaver.co.uk/wp-content/uploads/2013/12/20131227-171630.jpg)_

These are the apps that I've used to connect and all have proved effortless to setup and have so far served me well. Note the VNC Viewer is quite expensive so you might want to play around with some free versions before deciding to part with this much cash.

Fing (free) ([Fing - Network Scanner](https://itunes.apple.com/gb/app/fing-network-scanner/id430921107?mt=8&uo=4&at=1l3v7HE))  
WebSSH (free) ([WebSSH](https://itunes.apple.com/gb/app/webssh/id497714887?mt=8&uo=4&at=1l3v7HE))  
VNC Viewer (£6.99) ([VNC Viewer](https://itunes.apple.com/gb/app/vnc-viewer/id352019548?mt=8&uo=4&at=1l3v7HE))

## Using SSH to connect to your Raspberry Pi

Enable SSH  
SSH (Secure SHell) provides access to the Pi's command line interface. Before you can use it you need to enable SSH from the RPi config.txt file.

Open up the terminal and type
    
    
    sudo raspi-config

From here you should select Advanced Options and then enable SSH. Now save and exit.

In order to connect to your Raspberry Pi you need to know the IP address that it is using. You can find this from the command (see instructions [here](http://computers.tutsplus.com/tutorials/take-control-of-your-raspberry-pi-using-your-mac-pc-ipad-or-phone--mac-54603))
    
    
    ifconfig

but I have found it convenient to install the free iPhone or iPad app Fing which enables me to scan the home network to see all connections (will prove useful later).

Connect via SSH

![Setting up SSH Connection with Raspberry Pi](http://whatapalaver.co.uk/wp-content/uploads/2013/12/20131227-171510.jpg)

> _[Setting up SSH Connection with Raspberry Pi](http://whatapalaver.co.uk/wp-content/uploads/2013/12/20131227-171510.jpg)_

Download WebSSH (or similar) and add a new SSH connection.

The Host is the IP address used by your Raspberry Pi and identified using Fing. User and password are as set up in raspi-config. The default is pi raspberry

![iPhone connected to Raspberry Pi via SSH](http://whatapalaver.co.uk/wp-content/uploads/2013/12/20131227-171523.jpg)

> _[iPhone connected to Raspberry Pi via SSH](http://whatapalaver.co.uk/wp-content/uploads/2013/12/20131227-171523.jpg)_

If you hit connect now you will be rewarded with access to the command line.

I find this extremely satisfying. One thing to bear in mind is that your Raspberry Pi will be using a dynamic IP address so every time you reboot it is likely to select a different address, which means you would need to amend your SSH connection details in the app.

You can get around that by forcing your RPi to use a static IP address.

## How to Use a Static IP Address with your Raspberry Pi

There are detailed instructions on both [Raspberry Shake](http://www.raspberryshake.com/raspberry-pistatic-ip-address/) and [tuts+](http://computers.tutsplus.com/tutorials/take-control-of-your-raspberry-pi-using-your-mac-pc-ipad-or-phone--mac-54603) but this is what I did:

From the terminal, enter the following code to open the nano text editor in order to change the connection details
    
    
    $sudo nano /etc/network/interfaces

You will now be in the editor and can overwrite and add additional instructions.

Look for the line that reads
    
    
    iface eth0 inet dhcp

and change the dhcp to static
    
    
    iface eth0 inet static

Beneath this add the following lines of instructions:

address 192.168.0.11 <---this should be your IP address as identified by Fing  
netmask 255.255.255.0  
network 192.168.0.1 <--you can also identify this in Fing, for me it was the address of my router  
broadcast 192.168.100.255  
gateway 192.168.100.254

In order to save this file you need to press CTRL O and then enter. CTRL X will close the nano editor. It is then worth opening a web browser to check that you are still connected to the internet and you haven't messed everything up but entering the wrong addresses.

If you have messed something up, just retrace your steps and alter the details in the nano editor.

When you reboot, your IP address will be fixed and you won't have to amend the SSH connection details.

## Using VNC to Connect your Raspberry Pi from an iPad

The SSH protocol has just enabled us to connect to the command line of your Raspberry Pi but if you want to replicate the graphical desktop you will need to use VNC (Virtual Network Computing).

Install the VNC Server on the Raspberry Pi

To use this we need to install a VNCserver on the RPi. Follow these instructions from the terminal:
    
    
    sudo apt-get install tightvncserver

follow the instructions and enter a username and password as instructed and then run the server by entering
    
    
    tightvncserver

the VNC server won't automatically run after you reboot (unlike SSH which will always be enabled). This could be a nuisance if you reboot regularly and if so you might want to follow the instructions below that force the VNC server to run at start up.

Connecting via VNC

![Raspberry Pi running on an iPad](http://whatapalaver.co.uk/wp-content/uploads/2013/12/20131227-181238.jpg)

> _[Raspberry Pi running on an iPad](http://whatapalaver.co.uk/wp-content/uploads/2013/12/20131227-181238.jpg)_

Download a VNC Viewer to your iPad, I've used VNC Viewer but there are cheaper and free versions available.

Add a new connection. The address will be the static IP address that you set above but should also include the port number. So mine reads 192.168.0.11:1 (I believe 1 is the default port so should work for you as well.

The password will be whatever you set up when installing tightVNCserver.

Hit connect and you should be rewarded with a beautiful raspberry on your iPad screen.

## Running VNC when your Raspberry Pi Starts Up

The details for this task are can be found at adfruit who have provided a very clear tutorial for [running VNC at StartUp](http://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/running-vncserver-at-startup).

## Resources

I've used some really useful tutorials to help me complete the task - here are the ones I found the most useful:

## Update

I have just added a second tutorial that explains how to go further with the setup and allows you to access the Raspberry Pi from an external network for true [remote control of a Raspberry Pi](http://whatapalaver.co.uk/2014/01/remote-control-raspberry-pi-ipad/).
