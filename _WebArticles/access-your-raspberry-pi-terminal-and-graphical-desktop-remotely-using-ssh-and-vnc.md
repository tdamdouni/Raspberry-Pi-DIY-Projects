# Access your Raspberry Pi Terminal and Graphical Desktop remotely using SSH and VNC

_Captured: 2017-05-06 at 15:44 from [42bots.com](http://42bots.com/tutorials/access-raspberry-pi-terminal-and-desktop-remotely-with-ssh-and-vnc/)_

This post will cover the steps necessary to set-up remote access to the Raspberry Pi terminal and graphical desktop environment from a Windows, or Linux PC. I do not have a Mac, but the steps should be very simillar. In some posts this is referred to as running your Raspberry Pi "headless".

I want to put my Raspberry Pi 2 on a small mobile robot platform, so I can't have it drag a mouse, keyboard and monitor around. The steps below will work for Raspberry Pi models B, B+ and 2.

My starting point was the [official Raspberry Pi documentation page](http://www.raspberrypi.org/documentation/remote-access/). This is an open source project and more information is being added on a regular basis. Be sure to bookmark the site and check for updates. I also added some additional info, based on my mistakes and some forum posts I read, so keep reading…

To access the Raspberry Pi terminal and issue text commands remotely, we will be using the [SSH (Secure Shell) ](http://en.wikipedia.org/wiki/Secure_Shell)protocol. You could also transfer files and even access some graphical applications over SSH using what is called as "X forwarding". "X" is a window systems used in Unix and also Linux systems, like the Raspbian OS on the Raspberry Pi.

SSH works fine for accessing the Raspberry Pi terminal, but occasionally you need to acess the graphic desktop as well. After some trial and error, I found that for access to the Raspberry Pi graphical desktop and applications, [VNC](http://en.wikipedia.org/wiki/Virtual_Network_Computing) works better than X forwarding over SSH. Also, VNC can be used from both Windows and Linux machines in pretty much the same way.

### What you need

  * A working Raspberry Pi with Raspbian installed and configured on a compatible SD / Micro SD card. [This post](http://42bots.com/tutorials/raspberry-pi-2-initial-set-up-and-configuration-with-noobs-raspbian/) covers the steps to get that set-up, if you have not done so already.
  * Keyborad, mouse, monitor/TV and HDMI cable to configure the Raspberry Pi, at least until you finish the steps in this tutorial.
  * The raspberry Pi needs to be connected to your router, supporting DHCP (as almost all currently do) with an Ethernet cable, or via an USB Wi-Fi adapter. The Raspberry Pi supports connections via the Ethernet port out of the box. Configuring the Wi-Fi access requires some manual steps and will be covered in a separate post.
  * The computer from where you will access the Raspberry Pi.

### Remote access to the Raspberry Pi Terminal

#### Enable SSH on the Raspberry Pi

Remote command line access to the Raspberry Pi via SSH can be enable via the Raspberyy Pi Software Configuration Tool. To launch it open the Raspberry Pi Terminal and type:
    
    
    sudo raspi-config

Once you hit the Enter, the following screen should appear:

![RAspberry Pi Configuration Screen](http://42bots.com/wp-content/uploads/2015/03/raspi-config-01.jpg)

> _Navigate to item 8 "Advanced Options" using the arrow key and hit Enter._

![raspi-config-03](http://42bots.com/wp-content/uploads/2015/03/raspi-config-03-e1427169131581.jpg)

> _Here select item A4 SSH. You will get a prompt to Enable / Disable the SSH Server on the Raspberry Pi._

![raspi-config-04](http://42bots.com/wp-content/uploads/2015/03/raspi-config-04-e1427169233896.jpg)

> _Select <Enable> and hit Enter. If all is well, you should see the confirmation below._

![raspi-config-05](http://42bots.com/wp-content/uploads/2015/03/raspi-config-05-e1427169350311.jpg)

Hit the Enter key to go back to the Main Menu of raspi-config, navigate to the <Finish> option and hit the Enter key again. You will get back to the Terminal window and should see something like this:

![raspi-config-07](http://42bots.com/wp-content/uploads/2015/03/raspi-config-07-e1427169524594.jpg)

Done! You have an SSH service (daemon) running on your Raspberry Pi. It will start on boot, so you only need to go through this process once.

Next we need to identify the IP address of your Raspberry Pi. In the terminal type _ifconfig _and press enter. A list like the one below should appear:

![00-Pi-IP-Address-ifconfig](http://42bots.com/wp-content/uploads/2015/03/00-Pi-IP-Address-ifconfig.jpg)

What you are looking for is the address listed next to "inet addr:". In the image above, my Raspberry Pi is connected to my router via an ethernet cable. This connection is listed as "eth0" and the IP address of the Pi is 192.168.1.70. If you are connected to your router via a USB Wi-Fi dongle, the connection will be listed as something like "wlan0". Write down this IP address, as you will need it later!

Alternatively, if you have access to your router configuration page, your Raspberry Pi's IP address will be there as well, under the list of devices connected to your network.

#### Steps for Windows

On Windows you need to install an SSH client in order to be able to access the Raspberry Pi terminal remotely. PuTTY is one of the most popular such client program. The latest version can be downloaded from [greenend.org.uk](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html). Look for the section called **Binaries** and the subsection **For Windows on Intel x86. **You need the putty.exe file. PuTTY comes as a single putty.exe file and does not require an installation. Just copy the file to a convenient location on your PC.

P

![putty_download](http://42bots.com/wp-content/uploads/2015/03/putty_download.jpg)

Double click on the putty.exe file to start the program. You will be presented with a login / connection set-up screen. Type the IP address of your Raspberry Pi in the "Host Name (or IP address). The default port should be 22, leave that unchanged. Make sure that SSH is selected as the connection type and then click on Open. You can save this settings as well, for quicker access. In the screenshot below, I have saved the settings for my Ethernet and Wi-Fi connections, which have different IP addresses. For more information on PuTTY, refer to the [application documentation](http://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html).

![01-Windows-Putty-01](http://42bots.com/wp-content/uploads/2015/03/01-Windows-Putty-01.jpg)

You may be presented with a security warning. Assuming that you have entered the correct IP address of your Raspberry Pi in the previous step, it is safe to acknowledge the warning and continue, by pressing Yes. This will cache the connection and you will not see this warning in the future. You will then be prompted to enter your username and password. This is the Raspberry Pi username / password (pi/raspberry, by default). After you login you will see the familiar prompt on the Raspberry Pi terminal:

![01-Windows-Putty-03](http://42bots.com/wp-content/uploads/2015/03/01-Windows-Putty-03-e1427173064213.jpg)

#### Steps for Linux and Mac

On a Linux, or a Mac machine you can access the Raspberry Pi remotely over SSH directly from the terminal and do not need to install any additional software. Open your terminal and use the following command:
    
    
    ssh pi@<IP Address of your Pi>

Naturally, replace <IP Address of your Pi> with, well…the IP address of your Raspberry Pi that you wrote down earlier. You may see a security warning on the next step. Type yes to acknowledge and continue. You should only see this warning the first time you connect. You will then be prompted to enter your username and password. This is the Raspberry Pi username / password (pi/raspberry, by default). After you login you will see the familiar prompt on the Raspberry Pi terminal.

### Remote access to the Raspberry Pi graphic desktop environment using VNC

VNC (short for "virtual network computing") is a desktop sharing system that allows remote access to the graphical interface of one computer (in our case the Raspberry Pi) from another (your desktop / laptop). It will transmit keyboard and mouse events from your laptop / desktop to the Raspberry Pi and will provide a view of the Raspberry Pi graphical desktop on your laptop / desktop. For this to work you need a VNC server set-up and running on the Raspberry Pi and a VNC client on your desktop / laptop.

The [Raspberry Pi official VNC documentation page](http://www.raspberrypi.org/documentation/remote-access/vnc/) suggests using tightvncserver on the Raspberry Pi and that worked well for me. To install tightvncserver, open the Raspberry Pi console (either directly on the Pi, or remotely, using SSH) and type:
    
    
    sudo apt-get install tightvncserver

You will see something like this on the console:

![tighvnc install](http://42bots.com/wp-content/uploads/2015/04/tighvnc-install-01-e1428371278273.jpg)

> _Type "Y" and hit enter to continue and the installation script should do the rest. Next you need to run tightvncserver by typing_

in the console:

![tighvnc-install-02](http://42bots.com/wp-content/uploads/2015/04/tighvnc-install-02-e1428371472966.jpg)

You will be prompted to create a password for remotely accessing the Raspberry Pi desktop. You can also set-up an optional read-only password (I did not). **Remember the password, you will need it every time you connect to the Raspberry Pi desktop environment remotely!** Once you do that you will see a message like "New 'X' desktop is raspberrypi:1". This means that you have a VNC server up and running on the Raspberry Pi!

The [Raspberry Pi official VNC documentation page](http://www.raspberrypi.org/documentation/remote-access/vnc/) has instructions on how to get tightvncserver to run at boot. I did not go through that step, as I do not need access to the graphic desktop that often. Instead I open an SSH session to the terminal and manually start the vncserver on the Raspberry Pi using a command like this:
    
    
    vncserver :1 -geometry 1920x1080 -depth 24

This will create a new virtual desktop on display 1, at 1920×1080 (full HD) resulution and a colour depth of 24 bits per pixel. For a full list of options see the [tightvnc page](http://www.tightvnc.com/vncserver.1.php).

![vncserver-start-raspberry-pi-01](http://42bots.com/wp-content/uploads/2015/04/vncserver-start-raspberry-pi-01.jpg)

> _You should see a line like this:_

New 'X' desktop is raspberrypi:1

The number after "raspberrypi:" is important (in my case it is 1). You will need this number to connect from the client. Now that the vncserver is running on the Raspberry pi and a new desktop is created, let us connect to remotely.

#### Getting a VNC client for Windows

On a Windows machine, you need a VNC client. The [Raspberry Pi documentation page](http://www.raspberrypi.org/documentation/remote-access/vnc/windows.md) suggests the TightVNC client, but I use the [VNC](https://www.realvnc.com/download/vnc/) viewer by Real VNC. Both a free programs, so take your pick. The VNC viewer from Real VNC comes in an EXE file and does not need an install. Just save it in a location you can find easily and run it. You will get a prompt like this:

![vnc-windows-01](http://42bots.com/wp-content/uploads/2015/04/vnc-windows-01.jpg)

In the VNC Server field, type the IP address of your Raspberry Pi, followed by a column and the number of the 'X' desktop that you saw when you started the vncserver on the Raspberry Pi in the previous step. In my case the IP address of my Raspberry Pi was 192.168.1.70 and the display number was 1, so the full connection address is: 192.168.1.70:1. Once you hit Connect you will be prompted for a password (the username field is displayed, but not accessible).

![vnc-windows-02](http://42bots.com/wp-content/uploads/2015/04/vnc-windows-02.jpg)

Enter the password you created earlier, when you run tightvncserver on the Raspberry Pi for the first time (see above). Hit OK and you should see a big raspberry on your screen!

![vnc-windows-03](http://42bots.com/wp-content/uploads/2015/04/vnc-windows-03.jpg)

#### Getting a VNC client for Linux

On my Ubuntu laptop, I use Remote Desktop Viewer, as recommended by the [Raspberry Pi documentation](http://www.raspberrypi.org/documentation/remote-access/vnc/linux.md) page. It is likely already available on your Linux distribution. Another option you may have is the Remmina Remote Desktop Client (works almost in the same way). On _Remote Desktop Viewer_ you need to click on the Connect button in the top left and you will get a prompt like this.

You need the IP adress of your Raspberry Pi and the screen number assigned by the current session of the tightvncserver (see above). Again, in my case the IP address of my Raspberry Pi was 192.168.1.70 and the display number was 1. Enter this on the "Host:" line and click the "Connect" button in the lower right corner.

![Remote Desktop Viewer Ubuntu](http://42bots.com/wp-content/uploads/2015/04/Screenshot-from-2015-04-07-200709-e1428462520423.png)

You should be prompted for a password. This is the password you setup earlier, when you run tightvncserver on the Raspberry Pi for the first time (I told you you will need to remember it!). Hit OK and you should see your Raspberry Pi graphic desktop environment!

#### Shutting Down the VNC Server on the Raspberry Pi

When you are done with your remote desktop session, you can shut down the VNC server on the Raspberry Pi. TO do that you need to issue the following command on the Raspberry Pi terminal:

**vncserver** _-kill :1_

Replace 1 with the number of your display. Note that there is a space between the _-kill_ and the semi-column_. _Just closing the VNC client session will leave the vnc server process running in the background. Not a big deal, but why waste resources on the Pi?
