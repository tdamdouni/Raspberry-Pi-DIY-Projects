# Guide To…Direct Network Connection

_Captured: 2017-11-09 at 23:43 from [pihw.wordpress.com](https://pihw.wordpress.com/guides/direct-network-connection/)_

## Raspberry Pi Remote Connections - Without A Network!

**_No keyboard or screen available for your Raspberry Pi, but you have a laptop? There is now a very easy solution!_**

There are often times when a HDMI monitor is not available to use with your Raspberry Pi. To overcome this I've often set-up my phone to be a portable Wi-Fi hotspot, but you do have to ensure the details are set-up ready on my Raspberry Pi beforehand.

So what happens if it is a new or someone else's Raspberry Pi?

In those circumstances it can be very useful to remote connect using a nearby network and a laptop (see the [Guide to…Remote Connections](https://pihw.wordpress.com/guides/guide-to-remote-connections/)). You have two options here:

  1. If you have a wired connection available you can simply plug into it and look up the IP address on the router.
  2. If you have a wireless connection available, you can now place a file on the SD-Card with the required settings which should be transferred on start-up to the system (I'll create a guide to this at some stage).

However, sometimes when you are travelling, at an event or perhaps in a school classroom there isn't a network available either!

**_So how can we make use of a laptop screen and keyboard when there is no network?_**

As discussed previously (in the [Guide to…Remote Connections](https://pihw.wordpress.com/guides/guide-to-remote-connections/)), there is the option of using a (console) TTL-serial cable, however this only provides rather slow access. The serial connection won't support X11 (which as we have seen, allows us to run graphical programs too), and you won't be able use VNC or shared folders if you have them set-up.

**_The answer is a simple network cable!_**

![Connect and use your Raspberry Pi with just a Network Cable, SDCard and Power!](https://pihw.files.wordpress.com/2013/04/directconnect1.png?w=614&h=355)

> _Connect and use your Raspberry Pi with just a Network Cable, a standard Imaged SD-Card and Power!_

It is advisable to set this up before you need it so you can be sure that it is configured and working correctly. Once you do you can use the methods described in the [Guide to…Remote Connections](https://pihw.wordpress.com/guides/guide-to-remote-connections/) to access your Raspberry Pi as if it was on a standard network (if you already have a network available you can just connect to that instead).

Remember if you need the wired network for your computer (i.e. to get to the internet) then you shall have to make a choice about which one you wish to use (or get an extra network port by adding a USB network dongle). If you use wireless connections, then you can still have both!

### What you will need:

  * Raspberry Pi (Model B, B+, 2B or 3B)
  * Micro USB Cable & Power Supply
  * Micro SD-Card (loaded with NOOBS see below)
  * A network cable

Any standard network cable should be suitable (needs to have a male RJ45 connector on each end), most cables available will be fine for our needs.

> **Note:** You can use a normal network cable since the Raspberry Pi LAN chip is smart enough to reconfigure itself for direct network connections (in the past older computers would have needed a special "cross-over" cable).

Don't worry if you don't have NOOBS setup already, it is possible to do everything you need without a screen or keyboard attached to the Pi… Just configure the SD-Card and add power (see the section below for automated installs). If you are already set-up with a recent NOOBS/Raspbian install then it couldn't be simpler.

### Connect and go!

Previously this process was rather difficult without a screen and keyboard attached to the Raspberry Pi. This was because, by default, the system would not set-up an IP address when a cable was connected. This meant you had to configure the Raspberry Pi manually to have a fixed IP address appropriate for the temporary network.

> Thankfully, things have finally moved forward and the latest installs of Raspbian include software which detects a new network connection and automatically assigns a suitable IP address. This is a HUGE help!

The final piece of the puzzle, is now we have a valid network link we still need to know what IP address the Raspberry Pi had given itself so we can tell our software to connect to it.

Fortunately Apple have this covered with their aptly named "Bonjour" service which checks the addresses on the network and ensures their **hostnames** are valid. A hostname is simply like a nickname given to a computer so you don't need to remember it's full address, just call the nickname instead.

If you don't want/can't install Bonjour then you will have to find the IP address either directly on the Pi using "hostname -I" or using a network scanner such as Fingbox (<https://www.fingbox.com/download>).

> This means you can now use the Raspberry Pi by just referring to it's hostname, by default this is set to **raspberrypi.local** or **raspberrypi**.

### Hello Bonjour

If you have a OSX Mac you will have Bonjour running already. On Windows you can either install iTunes (if you haven't got it) which also includes the service, or you can install it separately (via the [Apple Bonjour Installer](https://support.apple.com/kb/DL999)).

We now have a simple network just for two, allowing SSH, X-forwarding, file shares etc etc. We can now do all the lovely networky things we like to do, as detailed in the [Guide to…Remote Connections](https://pihw.wordpress.com/guides/guide-to-remote-connections/) page.

![Scratch](https://pihw.files.wordpress.com/2013/04/scratch.png)

> _Scratch running nicely inside a window using X-11!_

**There's even more good news for the Pi-Zero**

This method has been used in the Pi-Zero network device video for excellent results. It is particularly special since we use the Pi-Kitchen to pre-configure the USB to act as if it is a network device - allowing us to make a simple network link using just a standard micro-USB cable (which will also power it!).

![PiZeroNetworkDevice](https://pihw.files.wordpress.com/2013/04/pizeronetworkdevice.png)

> _Raspberry Pi Zero with Micro SDCard and Micro USB Cable._

## Installing NOOBS to your SDCard

_**Update:** In order to put security first, the default operating system install (such as the one provided by NOOBS) no longer has SSH enabled._

<https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/>

_If you want to later use SSH you will need to add a file called "ssh" to the boot partition on the Raspberry Pi. This can be done with the following command:_
    
    
    _sudo touch /boot/ssh_

_This means that although you can perform an automated install without using a screen, you won't be able to connect to it! Unfortunately, in the name of improved security, this method for running a Raspberry Pi headless has been broken (although I shall see if this can be fixed in newer versions of NOOBS). There IS a work around if you are brave ([thanks to Procount](https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=166984&p=1075797#p1075797)). Another option is to add _**vncinstall**_ to the end of the **recovery.cmdline **file._

> **Note:** If you already have an up to date install you can skip this!

### Load SD Card with NOOBS:

  1. Download NOOBS.zip from the RaspberryPi.org website.
  2. Format the SD-Card using the SD-Card formatter (SDFormatter)
  3. Extract NOOBS.ZIP to the SD-Card

> **Note:** Your SD-Card should look something like this (with all the files in the root of the SD-Card and not in a directory).

![SDCard](https://pihw.files.wordpress.com/2013/04/sdcard.png)

> _NOOBS files on the SD-Card_

### Automated Headless Install:

#### Option A: Using NOOBS

Although not a commonly known feature, NOOBS is able to automatically install a selected operating system without the need for a keyboard or screen.

To perform an automated install of Raspbian, you will need to edit the **recovery.cmdline** file on the SD-Card.

> **Note:** If you are editing this file in Windows it is recommended that you use an editor which supports Linux format files (such as the freeware [Notepad++](https://notepad-plus-plus.org/download/)).

Change the **recovery.cmdline** file:
    
    
    runinstaller quiet ramdisk_size=32768 root=/dev/ram0 init=/init vt.cur_default=1 elevator=deadline

By adding **silentinstall** to the file (keeping everything else the same):
    
    
    **silentinstall** runinstaller quiet ramdisk_size=32768 root=/dev/ram0 init=/init vt.cur_default=1 elevator=deadline

#### Option B: Pi-Kitchen

Set up Pi-Kitchen & select Auto Install (see the [Pi-Kitchen pages](https://pihw.wordpress.com/guides/pi-kitchen/how-it-works/quickstart/) for more details).

> **Note:** The Pi-Kitchen allows complete customisation of the install and allows you to define multiple "flavours" set-up in whatever way you like.

### Power Up & Install:

  * Insert the SD-Card into the Raspberry Pi
  * Connect the network cable between the computer and the Raspberry Pi.

> **Note:** The network port on the Raspberry Pi will sense the connection type and automatically provide a cross-over for direct networking. Therefore we can use any standard RJ45 cable.

Add power and wait…and wait…and wait some more. You should see the activity LEDs flash while the OS installs. Depending on your SD-Card this can take up to 40-60 minutes. If this is your first go it is helpful to connect a screen so you can observe the installation progress.

### Check your network settings…

While the OS is installing you can check your computer's network settings are set to automatic. And if required we can enable Internet Connection Sharing (ICS) so we can use the host computer's internet (assuming it usually connects to the internet via Wi-Fi).

> **Note:** Most network set-ups will be set to automatic but if not ensure you write down the automatic, but if not ensure you write down the original settings so you can restore them later.

Set each of the settings to automatic which will allow the network to configure it.

![Settings](https://pihw.files.wordpress.com/2013/04/settings.png)

> _Network Settings_

### Enable Internet Connection Sharing (ICS):

Select the ICS tab and select share this connection, and if needed select the network adaptor which your Raspberry Pi is connected to.

![InternetConnectionSharing](https://pihw.files.wordpress.com/2013/04/internetconnectionsharing.png)

> _Internet Connection Sharing_

That's it, when the Raspberry Pi starts it should detect the settings and configure the internet gateway to match the IP address of the host computer.

### Ready to connect?

When the Raspberry Pi has finished installing you should notice that the network adaptor will report "limited connection".

**NOTE THE FOLLOWING:**

  1. You will need to wait for your computer to finish detecting the network settings (you may see a small networking icon flashing in your system tray while it does, or open up the network settings to see when it has finished and has an IP address) - it can take around 1/2 minute. Your computer may report the connection as "limited or no connection" when connected to the Raspberry Pi in this way, this is normal as indicates it is a direct computer to computer connection rather than a standard network (where it would expect to find an internet connection).
  2. If you are using multiple wired network adaptors (i.e. Using an extra USB-LAN dongle) on your computer you may find you have to unplug the other network cable and reattach afterwards (my Windows XP machine needed this before it would connect through the direct link).

### Summary

Now you should be able to do most of the things you would normally do when connected to a network.

One VERY useful thing to do is to set up "Putty" and "Xming" to allow you to control the terminal and graphical programs directly from your laptop/computer.

![Scratch running nicely inside a window!](https://pihw.files.wordpress.com/2013/03/scratch-x11.png?w=598&h=466)

> _Scratch running nicely inside a window using X-11!_

See the main [Guide to…Remote Connections](https://pihw.wordpress.com/guides/guide-to-remote-connections/) for links for how to set-up VNC and shared folders, and X-11 on other computers.

### Install Putty and Xming Server (for SSH and X11)

I am assuming you are using the latest version of [Raspbian](http://www.raspberrypi.org/downloads) which has **SSH** and **X11 Forwarding** enabled by default (if not see the bottom of this post to enable them if things don't work).

#### 1\. Install and run a X-Windows server on your computer

Download and run <http://sourceforge.net/projects/xming/> from the [Xming](http://people.arsc.edu/~murakami/xming/) site.

Follow the installation, including installing "Putty" if you don't have it already. You can also download "Putty" separately from <http://www.putty.org/>

An alternative X-Windows server is available called mobaxterm, this provides a little more control, keeps your X-Windows together and handles your sessions etc. You can get it from <http://mobaxterm.mobatek.net/>. (Thanks to Mike for this tip).

#### 2\. Ensure your SSH program (Putty) has X-11 enabled.

In the PuTTY configuration, find "Connection", "SSH", "X11" and tick the check-box for "X11 forwarding". If you leave the X display location blank, it will assume the default "Server 0:0" (you can confirm the server number by hovering your mouse over the Xming icon in the system tray when it is running). You can save your set-up within Putty so you will won't have to do this each time.

![Putty Configuration for X11 Forwarding](https://pihw.files.wordpress.com/2013/03/puttycongif-x11.png?w=600&h=532)

> _Putty Configuration for X11 Forwarding_

#### 3\. Enter the Raspberry Pi's IP Address

![Putty Configuration for IP 192.168.1.69](https://pihw.files.wordpress.com/2013/03/puttyconfig.png?w=600&h=532)

> _Putty Configuration for given IP_

Enter the IP Address of the Raspberry Pi in the Session settings above (you may also find that you can use the Raspberry Pi's hostname here instead (default: raspberrypi)).

Save the setting using a suitable name (RaspberryPiDirect) and press "open" to connect to your Raspberry Pi. You will likely get a warning pop-up stating you haven't connected to the computer before (allows you to check you have everything right before continuing).

All being well, you should be greeted with a prompt for your username and password (remember the defaults are pi and raspberry).

#### 4\. Using X11 and Xming

Ensure you have Xming running, by starting the Xming program from your computers start menu and then in the terminal window, type a program which normally runs within the Raspberry Pi desktop (such as "leafpad" or "scratch"). Wait a little while and the program should appear on your computers desktop (if you get an error you have probably forgotten to start "Xming", so run it and try again).

  1. If you want to run an X program, but still be able to use the same terminal console for other stuff, you can run the command in the background with &:

i.e. leafpad &

Just remember that the more programs you run, the slower everything will get. You can switch to the background program by typing "fg", check for background jobs with "bg".

  1. You can even run a full desktop session through X-11, although it isn't particularly user-friendly and VNC will produce better results. To do this you have to use "lxsession" instead of "startx".
  2. If you get the following error (or similar) when running PyGame or Tkinter scripts:
    
    
    _tkinter.TclError: couldn't connect to display "localhost:10.0"

Use the fix below:
    
    
    cd ~
    sudo cp .Xauthority ~root/

**More details and links are in the main [Guide to…Remote Connections](https://pihw.wordpress.com/guides/guide-to-remote-connections/).**

## Additional Information / Troubleshooting

  1. To switch on (or off) SSH you can access raspi config (just type "sudo raspi-config" from the terminal) and select SSH in the menu (it seems like SSH is already enabled by default for some distros).

![Enable/Disable SSH via Raspi-config](https://pihw.files.wordpress.com/2013/03/ssh-raspi-config.png?w=300&h=187)

> _Enable/Disable SSH via Raspi-config_

  1. Ensure X-11 forwarding is enabled on the Raspberry Pi (again, a lot of distros now have this enabled by default).

Use nano with the following command:
    
    
    sudo nano /etc/ssh/sshd_config

Look for a line in the /etc/ssh/sshd_config file which controls X11Forwarding and ensure it says (with no # before it):
    
    
    X11Forwarding yes

Save if required (ctrl+x,Y, enter), and reboot:

sudo reboot

### What is an IP Address / Hostnames / Pinging / Subnets?

An IP Address is like your phone number or post code, it simply allows other computers to find that particular computer in the network and ensure any messages it sends goes to that one in particular.

Often, IP Address's can be replaced with hostname's so that we can ask for a specific computer without knowing all the numbers (like the contacts list on your phone, the computer looks up the name and uses the number for you). For instance, <http://www.google.com>, is a hostname, where it's IP address is 173.194.45.49 (probably depending on where you are). We can "ping" the address using the following command, which simply sends some short messages to see if there is another computer on the other side to respond to them.
    
    
    ping www.google.com

or:
    
    
    ping 173.194.45.49

### Subnets:

Networks use subnets to help handle the fact that there could be a HUGE number of computers on a network (like the internet) and it would be impossible for a computer to listen to and respond to any computer in the address range 0.0.0.0 to 255.255.255.255.

To handle this, networks will use a subnet mask, this ensures that a computer only needs to respond to computers with are within the same SUBSET, which is defined by the SUBNET MASK setting.

The mask is a series of flags which defines which range of addresses the computer will respond to (by filtering out any which are not within the allowed range):

255.255.255.0

Means it will respond to computers which have IP addressing matching at least the 3 first numbers. So a computer with an address of 192.168.1.90 and subnet mask of 255.255.255.0 will only talk to other computers with addresses in the range 192.168.1.0-192.168.1.255 (except 90 of course!). Large networks often use SUBNETs to split up larger networks into sections so that they run more efficiently.

_Note: You will not be able to set the SUBNET MASK to wider than 255.0.0.0. The Raspberry Pi defaults to a subnet mask of 255.255.0.0, which is perfect for most situations._

### Trouble-shooting:

Steps to check:  
1\. Check the IP address which get set on both machines (both should be in range 169.254.x.x).

On RPI use one of the following commands:
    
    
    hostname -I
    ifconfig

On PC use the following (or look it up from the Network & Sharing Center and look at the adaptor properties):
    
    
    ipconfig

  * If this fails, check the cmdline.txt file is right/cable connected etc. You can use the following to force the IP address on the RPI (for testing the rest - but this won't be set next time you reboot):
    
    
    sudo ifconfig eth0 169.254.0.2

  1. Check you can ping each of the addresses from the other computer (where 169.254.0.xxx should match the computer you want to talk to). Test both directions.
    
    
    ping 169.254.0.xxx

  * If this fails, check PC's firewall and disable wifi (sometimes the ping command will try using the PC's wifi instead)
  1. Check you can connect via SSH (using putty)
  * This should work if you can already ping the other machine (it is unlikely to work if you can't ping it).

### References:

Thanks to fellow MagPi - Colin Deady for testing out on Mac for me.

Thanks to the following sites for providing various parts of the puzzle (in no specific order):

<http://learn.adafruit.com/adafruits-raspberry-pi-lesson-6-using-ssh>

<http://people.arsc.edu/~murakami/xming/>

<http://jeremy-nicola.info/portfolio-item/ssh-x-forwarding-on-windows/>

<http://en.wikipedia.org/wiki/Subnetwork>

<http://en.wikipedia.org/wiki/Link-local_address>

[http://www.raspberrypi.org/phpBB3/viewtopic.php?f=29&t=22716](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=29&t=22716)

[http://www.raspberrypi.org/phpBB3/viewtopic.php?f=27&t=24993](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=27&t=24993)

[http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=26934](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=26934)
