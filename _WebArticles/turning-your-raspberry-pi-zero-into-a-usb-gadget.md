# Turning your Raspberry PI Zero into a USB Gadget

_Captured: 2017-09-03 at 23:14 from [learn.adafruit.com](https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget?view=all)_

![raspberry_pi_2885-04.jpg](https://cdn-learn.adafruit.com/assets/assets/000/029/343/large1024/raspberry_pi_2885-04.jpg?1451151062)

> _When the Pi Zero came out, one of the downsides (!) of the low-cost design was swapping the 'standard' USB A-port for a micro-B port. Now you have to use an 'OTG' cable instead of just plugging in a device._

[There was also the matter of, if you didn't have anything connected to USB, and powered up the Pi Zero with an old Raspbian image, you'd get a strange warning](https://github.com/raspberrypi/firmware/issues/513)

`WARN::dwc_otg_handle_mode_mismatch_intr:68: Mode Mismatch Interrupt: currently in Device mode`

Basically, the Pi sorta-trying to become a **usb device **rather than a **usb host**

[Some awesome people on github](https://github.com/raspberrypi/linux/issues/1212) sorted out that if you used the DWC2 USB driver, and patched a few files, you could get the Pi to act like a USB device (in linux-land this is called the **USB Gadget** system)

[Thx for the tips from Andrew, as of May 2016, Raspbian Jessie does not require a new kernel](http://blog.gbaman.info/?p=791)

This tutorial is basically just a writeup of how you can follow along and turn your Pi zero into a **USB Serial** device or** Ethernet **device. That's two whole ways of being able to connect to your Pi zero just by plugging in a micro B cable! You don't even need to power your Pi seperately, as power is provided from your computer.

Yeah the gadget system can do a lot more, but these are the two modules we've tested so far. The compiled kernel package has just about every USB gadget compiled in as a module if you'd like to try others

This tutorial isn't _terribly_ difficult but you should have some raspberry Pi experience. In particular you will want to do the following **before anything else**

For Gadget serial you'll also want

While you don't _need_ a console cable, it's a lot easier to copy & paste the commands into a terminal than to type into a keyboard + montor.

![raspberry_pi_954-02.jpg](https://cdn-learn.adafruit.com/assets/assets/000/029/295/large1024/raspberry_pi_954-02.jpg?1451150940)

Basically, get your Pi zero to a point you can log in. Power it from the Power USB port, leave the Data USB port 'empty'

![raspberry_pi_1login.png](https://cdn-learn.adafruit.com/assets/assets/000/029/294/large1024/raspberry_pi_1login.png?1451150940)

> _OK now you can continue!_

![raspberry_pi_dwc2.png](https://cdn-learn.adafruit.com/assets/assets/000/034/983/large1024/raspberry_pi_dwc2.png?1471834032)

![raspberry_pi_cmd.png](https://cdn-learn.adafruit.com/assets/assets/000/034/985/large1024/raspberry_pi_cmd.png?1471835684)

![raspberry_pi_1login.png](https://cdn-learn.adafruit.com/assets/assets/000/029/297/large1024/raspberry_pi_1login.png?1451150941)

> _While booting, or later when runing sudo dmesg you can see that it bound driver g_serial_

![raspberry_pi_gserial.png](https://cdn-learn.adafruit.com/assets/assets/000/034/986/large1024/raspberry_pi_gserial.png?1471835769)

> _Set up logging in on Pi Zero via Serial Gadget_

![raspberry_pi_gserial.png](https://cdn-learn.adafruit.com/assets/assets/000/029/303/large1024/raspberry_pi_gserial.png?1451150961)

> _On your computer you'll see a new Serial port is created. Check the Windows device driver:_

![raspberry_pi_gserialcom.png](https://cdn-learn.adafruit.com/assets/assets/000/029/304/large1024/raspberry_pi_gserialcom.png?1451150963)

![raspberry_pi_puttyset.png](https://cdn-learn.adafruit.com/assets/assets/000/029/307/large1024/raspberry_pi_puttyset.png?1451150967)

![raspberry_pi_seriallogin.png](https://cdn-learn.adafruit.com/assets/assets/000/029/308/large1024/raspberry_pi_seriallogin.png?1451150970)

> _You may have to hit return a few times to get it to come up with the login prompt. But that's it! You're now connected to your Pi Zero directly_

![raspberry_pi_dwc2.png](https://cdn-learn.adafruit.com/assets/assets/000/034/993/large1024/raspberry_pi_dwc2.png?1471836970)

![raspberry_pi_gether.png](https://cdn-learn.adafruit.com/assets/assets/000/034/995/large1024/raspberry_pi_gether.png?1471837027)

![raspberry_pi_getherboot.png](https://cdn-learn.adafruit.com/assets/assets/000/034/996/large1024/raspberry_pi_getherboot.png?1471837170)

![raspberry_pi_pilocal.png](https://cdn-learn.adafruit.com/assets/assets/000/034/997/large1024/raspberry_pi_pilocal.png?1471837385)

![raspberry_pi_getherifconfig.png](https://cdn-learn.adafruit.com/assets/assets/000/029/316/large1024/raspberry_pi_getherifconfig.png?1451150990)

> _Try plugging the Pi Zero into your computer now. For example, on a Mac, we plugged it in_

![raspberry_pi_interface.png](https://cdn-learn.adafruit.com/assets/assets/000/029/327/large1024/raspberry_pi_interface.png?1451151027)

![raspberry_pi_selfassigned.png](https://cdn-learn.adafruit.com/assets/assets/000/029/328/large1024/raspberry_pi_selfassigned.png?1451151031)

![raspberry_pi_1rndisdriver.png](https://cdn-learn.adafruit.com/assets/assets/000/029/332/large1024/raspberry_pi_1rndisdriver.png?1451151038)

![raspberry_pi_2networksharing.png](https://cdn-learn.adafruit.com/assets/assets/000/029/333/large1024/raspberry_pi_2networksharing.png?1451151039)

![raspberry_pi_Screenshot_2016-11-22_18.24.59.jpg](https://cdn-learn.adafruit.com/assets/assets/000/037/775/large1024/raspberry_pi_Screenshot_2016-11-22_18.24.59.jpg?1480902759)

_ _

[ ![Adafruit Logo](/logos/adafruit_logo_small.png?-3983450236884509208) ](https://www.adafruit.com)

[ 0 __ ](https://www.adafruit.com/shopping_cart)

  * Search __
  * [SHOP](https://www.adafruit.com/categories)
  * [BLOG](https://blog.adafruit.com)
  * [LEARN](https://learn.adafruit.com)
  * [FORUMS](https://forums.adafruit.com)
  * [VIDEOS](https://www.youtube.com/adafruit)
  * [SIGN IN](/users/sign_in)
  * CLOSE MENU

[ 0 Items __ ](https://www.adafruit.com/shopping_cart)

[Sign In](/users/sign_in)

Search __

[ ![Adafruit Logo](/logos/logo_2x.png?-3983450236884509208) ](https://www.adafruit.com)

  * [SHOP](https://www.adafruit.com)
  * [BLOG](https://blog.adafruit.com)
  * [LEARN](https://learn.adafruit.com)
  * [FORUMS](https://forums.adafruit.com)
  * [VIDEOS](https://www.youtube.com/adafruit)

![](https://s3.amazonaws.com/learn-production/guides/images/000/001/199/medium800/raspberry_pi_2885-04.jpg?1451151097)

# [Turning your Raspberry PI Zero into a USB Gadget](/turning-your-raspberry-pi-zero-into-a-usb-gadget/overview)

[Go Go Gadget Pi Zero](/turning-your-raspberry-pi-zero-into-a-usb-gadget/overview)

  * Overview
  * Serial Gadget
  * Ethernet Gadget
    * Ethernet Tweaks

  * Other Modules!
  * Old Kernel Install
  *   * [Multiple Pages](/turning-your-raspberry-pi-zero-into-a-usb-gadget)
  * [Download PDF](https://cdn-learn.adafruit.com/downloads/pdf/turning-your-raspberry-pi-zero-into-a-usb-gadget.pdf)

#### Contributors

[lady ada](/users/adafruit2)

[ Feedback? Corrections? ](/pages/6663/settings_modal)

[RASPBERRY PI](/category/raspberry-pi) [ __ ](/guides/1199/favorites.js)

#  Overview

by [ lady ada ](/users/adafruit2)

[ ![raspberry_pi_2885-04.jpg](https://cdn-learn.adafruit.com/assets/assets/000/029/343/medium800/raspberry_pi_2885-04.jpg?1451151062) __ ](/assets/29343)

When the Pi Zero came out, one of the downsides (!) of the low-cost design was swapping the 'standard' USB A-port for a micro-B port. Now you have to use an 'OTG' cable instead of just plugging in a device.

[There was also the matter of, if you didn't have anything connected to USB, and powered up the Pi Zero with an old Raspbian image, you'd get a strange warning](https://github.com/raspberrypi/firmware/issues/513)

`WARN::dwc_otg_handle_mode_mismatch_intr:68: Mode Mismatch Interrupt: currently in Device mode`

Basically, the Pi sorta-trying to become a **usb device **rather than a **usb host**

[Some awesome people on github](https://github.com/raspberrypi/linux/issues/1212) sorted out that if you used the DWC2 USB driver, and patched a few files, you could get the Pi to act like a USB device (in linux-land this is called the **USB Gadget** system)

[Thx for the tips from Andrew, as of May 2016, Raspbian Jessie does not require a new kernel](http://blog.gbaman.info/?p=791)

This tutorial is basically just a writeup of how you can follow along and turn your Pi zero into a **USB Serial** device or** Ethernet **device. That's two whole ways of being able to connect to your Pi zero just by plugging in a micro B cable! You don't even need to power your Pi seperately, as power is provided from your computer.

__ As of May 2016, Raspbian Jessie has built in kernel support - this tutorial is way easier! 

__ Yeah the gadget system can do a lot more, but these are the two modules we've tested so far. The compiled kernel package has just about every USB gadget compiled in as a module if you'd like to try others 

#  Before You Begin

This tutorial isn't _terribly_ difficult but you should have some raspberry Pi experience. In particular you will want to do the following **before anything else**

  * [Burn a copy of Rasbian Jessie Lite (or just plain Jessie) to a 4G or 8G SD card.](../../../../adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi)
  * Micro USB cable

For Gadget serial you'll also want

  * [Solder in a 2x20 male header](https://www.adafruit.com/products/2822) or somehow be able to connect a console cable to your Pi Zero
  * [Have a USB console cable and be able to log into your Pi over serial from a desktop computer](../../../../adafruits-raspberry-pi-lesson-5-using-a-console-cable)

While you don't _need_ a console cable, it's a lot easier to copy & paste the commands into a terminal than to type into a keyboard + montor.

[ ![raspberry_pi_954-02.jpg](https://cdn-learn.adafruit.com/assets/assets/000/029/295/medium800/raspberry_pi_954-02.jpg?1451150940) __ ](/assets/29295)

Basically, get your Pi zero to a point you can log in. Power it from the Power USB port, leave the Data USB port 'empty'

[ ![raspberry_pi_1login.png](https://cdn-learn.adafruit.com/assets/assets/000/029/294/medium800/raspberry_pi_1login.png?1451150940) __ ](/assets/29294)

OK **now** you can continue!

#  Serial Gadget

by [ lady ada ](/users/adafruit2)

We'll start with Serial Gadget, which is the 'simplest' of the USB gadgets. This one basically makes it so when you plug in the Pi Zero to your computer, it will pop up as a **Serial (COM) Port** \- the nice thing about this technique is you can use the pi with any computer and operating system and it doesnt require special drivers or configuration.

_[Thx for the tips from Andrew, as of May 2016, Raspbian Jessie does not require a new kernel ](http://blog.gbaman.info/?p=791)_

#  Step 0. Download and install latest Jessie

We're using Jessie Lite but plain Jessie Raspbian should work too! You need May 2016 or later (tested with 2016-05-27)

[This tutorial has the details](../../../../adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi)

#  Step 1. Edit config.txt & cmdline.txt

After burning the SD card, do not eject it from your computer! Use a text editor to open up the **config.txt **file that is in the SD card post-burn.

Go to the bottom and add `dtoverlay=dwc2`as the last line:

[ ![raspberry_pi_dwc2.png](https://cdn-learn.adafruit.com/assets/assets/000/034/983/medium800/raspberry_pi_dwc2.png?1471834032) __ ](/assets/34983)

Save the config.txt file as plain text and then open up cmdline.txt After **rootwait** (the last word on the first line) add a space and then `modules-load=dwc2,g_serial`

[ ![raspberry_pi_cmd.png](https://cdn-learn.adafruit.com/assets/assets/000/034/985/medium800/raspberry_pi_cmd.png?1471835684) __ ](/assets/34985)

At the time of writing, this is the full cmdline.txt contents (in case you need to start over). Note it is one very long line

Copy Code

    
    
    dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_serial quiet init=/usr/lib/raspi-config/init_resize.sh
    
    
    dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_serial quiet init=/usr/lib/raspi-config/init_resize.sh

#  Log into your Pi Zero

Insert the SD into your Pi Zero, connect the console cable, power the Pi & log into via the USB console.

[ ![raspberry_pi_1login.png](https://cdn-learn.adafruit.com/assets/assets/000/029/297/medium800/raspberry_pi_1login.png?1451150941) __ ](/assets/29297)

While booting, or later when runing **sudo dmesg** you can see that it bound driver **g_serial**

[ ![raspberry_pi_gserial.png](https://cdn-learn.adafruit.com/assets/assets/000/034/986/medium800/raspberry_pi_gserial.png?1471835769) __ ](/assets/34986)

#  Set up logging in on Pi Zero via Serial Gadget

OK just cuz you have a Serial port doesn't mean you can log in with it _yet. _The Pi knows it has a Serial port but you have to tie it to a console. You can do that very easily with:

  * **sudo systemctl enable [email protected]**

[ ![raspberry_pi_getty.png](https://cdn-learn.adafruit.com/assets/assets/000/029/306/medium800/raspberry_pi_getty.png?1451150964) __ ](/assets/29306)

(don't forget the sudo like i did at first!)

You can then verify its running with

  * **sudo systemctl is-active [[email protected]](/cdn-cgi/l/email-protection)**

[ ![raspberry_pi_isactive.png](https://cdn-learn.adafruit.com/assets/assets/000/029/323/medium800/raspberry_pi_isactive.png?1451151018) __ ](/assets/29323)

Thats...pretty much it. run **sudo reboot** to start up your Pi Zero. Plug in a USB Micro cable from your computer to the Pi Zero.

__ Don't forget to plug in the USB cable from your computer to the "USB" connector port on the Pi Zero, not the PWR connector. 

While the Zero is rebooting you can see that it loads the **g_cdc** module which provides "CDC USB Serial support" ([CDC stands for 'communications device class'](https://en.wikipedia.org/wiki/USB_communications_device_class))

[ ![raspberry_pi_gserial.png](https://cdn-learn.adafruit.com/assets/assets/000/029/303/medium800/raspberry_pi_gserial.png?1451150961) __ ](/assets/29303)

On your computer you'll see a new Serial port is created. Check the Windows device driver:

[ ![raspberry_pi_gserialcom.png](https://cdn-learn.adafruit.com/assets/assets/000/029/304/medium800/raspberry_pi_gserialcom.png?1451150963) __ ](/assets/29304)

On mac, it will be a new device called **/dev/tty.usbmodemNNNN** where NNNN can be any number

[ ![raspberry_pi_lstty.png](https://cdn-learn.adafruit.com/assets/assets/000/029/305/medium800/raspberry_pi_lstty.png?1451150964) __ ](/assets/29305)

#  Log into your Pi using Serial Port Software

OK now that your Pi is rebooted and you get that USB serial device again, you can connect to it at** 115200 **baud (8N1 8-bit No-parity 1-stop if you need to set that)

[ ![raspberry_pi_puttyset.png](https://cdn-learn.adafruit.com/assets/assets/000/029/307/medium800/raspberry_pi_puttyset.png?1451150967) __ ](/assets/29307)

you can disconnect the console cable, so you dont mix up the USB console cable and the direct-console connection (since they both have COM/Serial ports)

You can also remove the power cable to the 'power USB' port, since the desktop computer will be powering the Pi thru the USB gadget port.

[ ![raspberry_pi_seriallogin.png](https://cdn-learn.adafruit.com/assets/assets/000/029/308/medium800/raspberry_pi_seriallogin.png?1451150970) __ ](/assets/29308)

You may have to hit return a few times to get it to come up with the login prompt. But that's it! You're now connected to your Pi Zero directly

#  Ethernet Gadget

by [ lady ada ](/users/adafruit2)

The Ethernet Gadget is a little more difficult to set up, but is a lot more powerful because you can tunnel networking, VNC, ssh and scp files, etc. Basically you get the ability to log in to the console as well as anything else you could want to do over a network connection

**Note that even though it's called "Ethernet Gadget" you do not use an Ethernet cable!** The only cable is the USB micro-B cable from your computer to your Pi Zero. The Pi 'appears' like an Ethernet device.

You can even share your desktop computer's network setup so your Pi can access the internet through your computer via the USB cable! Cool huh?

_[Thx for the tips from Andrew, as of May 2016, Raspbian Jessie does not require a new kernel & has raspberrypi.local setup by default so it's a lot easier](http://blog.gbaman.info/?p=791)_

#  Step 0. Download and install latest Jessie

We're using Jessie Lite but plain Jessie Raspbian should work too! We're using Jessie Lite but plain Jessie Raspbian should work too! You need May 2016 or later (tested with 2016-05-27)

[This tutorial has the details](../../../../adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi)

#  Step 1. Edit config.txt & cmdline.txt

After burning the SD card, do not eject it from your computer! Use a text editor to open up the **config.txt **file that is in the SD card post-burn.

Go to the bottom and add `dtoverlay=dwc2`as the last line:

[ ![raspberry_pi_dwc2.png](https://cdn-learn.adafruit.com/assets/assets/000/034/993/medium800/raspberry_pi_dwc2.png?1471836970) __ ](/assets/34993)

Save the config.txt file as plain text and then open up cmdline.txt After **rootwait** (the last word on the first line) add a space and then `modules-load=dwc2,g_ether`

[ ![raspberry_pi_gether.png](https://cdn-learn.adafruit.com/assets/assets/000/034/995/medium800/raspberry_pi_gether.png?1471837027) __ ](/assets/34995)

#  Boot Your Pi with USB

Plug in a MicroUSB cable from your Pi Zero's USB port to your computer

__ Don't forget to plug in the USB cable from your computer to the "USB" connector port on the Pi Zero, not the PWR connector. 

If you have a console cable you can watch the Zero's console to see it enable the **g_ether** device:

[ ![raspberry_pi_getherboot.png](https://cdn-learn.adafruit.com/assets/assets/000/034/996/medium800/raspberry_pi_getherboot.png?1471837170) __ ](/assets/34996)

#  SSH!

If you enable SSH on your Pi, you can then also SSH in to **raspberrypi.local**

[Start by enabling SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)

If you are using a Mac or Linux chances are you have Bonjour already installed. [On Windows, you may need to add Bonjour support so it knows what to do with .local names](../../../../bonjour-zeroconf-networking-for-windows-and-linux/)

[ ![raspberry_pi_pilocal.png](https://cdn-learn.adafruit.com/assets/assets/000/034/997/medium800/raspberry_pi_pilocal.png?1471837385) __ ](/assets/34997)

[ ![raspberry_pi_ssh.png](https://cdn-learn.adafruit.com/assets/assets/000/034/998/medium800/raspberry_pi_ssh.png?1471837401) __ ](/assets/34998)

#  Advanced Networking (Fixed IP)

If you need to manage fixed IP addresses for some reason - here's some useful techniques for managing your Pi's Gadget Ethernet device. Otherwise, you can always just keep using **raspberrypi.local**

You can now log in and check that you have a new network device called **usb0**

  * **sudo ifconfig -a**

[ ![raspberry_pi_getherifconfig.png](https://cdn-learn.adafruit.com/assets/assets/000/029/316/medium800/raspberry_pi_getherifconfig.png?1451150990) __ ](/assets/29316)

Try plugging the Pi Zero into your computer now. For example, on a Mac, we plugged it in

[ ![raspberry_pi_dhcpd.png](https://cdn-learn.adafruit.com/assets/assets/000/029/320/medium800/raspberry_pi_dhcpd.png?1451151003) __ ](/assets/29320)

As you can see above, between the first ifconfig and second, the network came up with an address. The problem this is a arbitrary (Bonjour/Zero Conf assigned) address, and we dont want to have to guess it.

We can configure this device to have a fixed address (this makes it easier to find on a network!)

  *  **sudo nano /etc/network/interfaces  

**

and add at the end

Copy Code

    
    
    allow-hotplug usb0
    iface usb0 inet static
            address 192.168.7.2
            netmask 255.255.255.0
            network 192.168.7.0
            broadcast 192.168.7.255
            gateway 192.168.7.1
    
    
    allow-hotplug usb0
    iface usb0 inet static
            address 192.168.7.2
            netmask 255.255.255.0
            network 192.168.7.0
            broadcast 192.168.7.255
            gateway 192.168.7.1

This will give the **Raspberry Pi the IP Address 192.168.7.2**

you can change this to a different address but unless you're sure that 192.168.7.* is unavailable, keep it as above for now.

[ ![raspberry_pi_interface.png](https://cdn-learn.adafruit.com/assets/assets/000/029/327/medium800/raspberry_pi_interface.png?1451151027) __ ](/assets/29327)

Save the file and run

  * **sudo ifdown usb0 **(this may fail, its fine)
  * **sudo ifup usb0**
  * **ifconfig usb0**

to verify it now has the 192.168.7.2 address

[ ![raspberry_pi_ifdownup.png](https://cdn-learn.adafruit.com/assets/assets/000/029/318/medium800/raspberry_pi_ifdownup.png?1451150995) __ ](/assets/29318)

Now on your **computer** you'll need to set it up as well.

#  If you are using a Mac as the Host Computer

On a Mac OS X machine, open up the **System Preferences**** -> Network** box.

[ ![raspberry_pi_selfassigned.png](https://cdn-learn.adafruit.com/assets/assets/000/029/328/medium800/raspberry_pi_selfassigned.png?1451151031) __ ](/assets/29328)

You'll see the device show up as an RNDIS/Ethernet Gadget. it'll probably be set up for DHCP by default so change it to **Configure IP4 Manually**

  * For the IP address pick **192.168.7.1 **(note that this is not the same as the Pi Zero's address!)
  * For the subnet mask, use **255.255.255.0  **(same as Pi)
  * For the router/gateway use **192.168.7.1 **(same as Pi)

If you didnt use our suggested netconfig above on the Pi, you may have to adjust this one to match

[ ![raspberry_pi_networkconfig.png](https://cdn-learn.adafruit.com/assets/assets/000/029/325/medium800/raspberry_pi_networkconfig.png?1451151023) __ ](/assets/29325)

Click **Apply** when done, and wait a minute or so you will get a green dot:

[ ![raspberry_pi_connected.png](https://cdn-learn.adafruit.com/assets/assets/000/029/330/medium800/raspberry_pi_connected.png?1451151032) __ ](/assets/29330)

If you're still having issues, a reader reported some Mac's need a special option on the g_ether device. While logged into your Pi with a console cable, run `sudo nano/etc/modprobe.d/g_ether.conf`   
and add: `options g_ether use_eem=0`

on it's own line, at the end.

After a reboot or manual load of the module, the the RNDIS/CNC gadget will turn yellow then green after assigning an IP.

You can use a terminal on the computer to check the IP address was set, your device will be called **enX** where X is some number, use **ifconfig -a **to see a list of all devices, chances are the Pi is the last one.

Once you can see that the IP address is set, try pinging the pi with

  * **ping 192.168.7.2**

[ ![raspberry_pi_ifconfigping.png](https://cdn-learn.adafruit.com/assets/assets/000/029/326/medium800/raspberry_pi_ifconfigping.png?1451151023) __ ](/assets/29326)

_To be honest, I rebooted the Pi after setting up the network config file, so if it doesnt work at first, try that._

Next up you can ssh into your pi from your Mac!

  * **ssh [[email protected]](/cdn-cgi/l/email-protection)**

[ ![raspberry_pi_ssh.png](https://cdn-learn.adafruit.com/assets/assets/000/029/329/medium800/raspberry_pi_ssh.png?1451151032) __ ](/assets/29329)

#  If you are using Windows as the Host Machine

Plug in the Pi Zero into your computer, I'm using Windows 7 64-bit. It will automatically download and install the RNDIS Ethernet drivers

[ ![raspberry_pi_usbrnd.png](https://cdn-learn.adafruit.com/assets/assets/000/029/331/medium800/raspberry_pi_usbrnd.png?1451151038) __ ](/assets/29331)

Some versions of windows may mis-interpret the PI as a COM port and you must manually force or install Microsoft RNDIS driver usage in Device Manager by right-click>Update Driver Software>Browse my computer>Pick from a list>Network Adapters>Microsoft>Remote NDIS compatible device.

Check the Device Manager to check that it is a new network adapter

[ ![raspberry_pi_1rndisdriver.png](https://cdn-learn.adafruit.com/assets/assets/000/029/332/medium800/raspberry_pi_1rndisdriver.png?1451151038) __ ](/assets/29332)

Open up **Network and Sharing Center** and click on **Change Adapter Settings** 

[ ![raspberry_pi_2networksharing.png](https://cdn-learn.adafruit.com/assets/assets/000/029/333/medium800/raspberry_pi_2networksharing.png?1451151039) __ ](/assets/29333)

You'll see a list of all the myriad adapters you have. I have a lot but you'll likely only have 2 or 3. Find the RNDIS adapter and rename it **pizero** (makes it easier to find)

[ ![raspberry_pi_3rename.png](https://cdn-learn.adafruit.com/assets/assets/000/029/334/medium800/raspberry_pi_3rename.png?1451151041) __ ](/assets/29334)

Then right-click and select **Properties...**

[ ![raspberry_pi_4properties.png](https://cdn-learn.adafruit.com/assets/assets/000/029/335/medium800/raspberry_pi_4properties.png?1451151043) __ ](/assets/29335)

And select the **Internet Protocol Version 4 (TCP/IPv4)** from the connection list and click **Properties**

[ ![raspberry_pi_5tcp4.png](https://cdn-learn.adafruit.com/assets/assets/000/029/336/medium800/raspberry_pi_5tcp4.png?1451151048) __ ](/assets/29336)

Enter in **192.168.7.1** as the computer's IP address and gateway (the gateway got erased later, I think Windows just automatically uses the IP address if they're the same) the subnet mask is **255.255.255.0** same as the Pi's

There's no DNS address

[ ![raspberry_pi_manual.png](https://cdn-learn.adafruit.com/assets/assets/000/029/337/medium800/raspberry_pi_manual.png?1451151049) __ ](/assets/29337)

I unplugged & replugged in the Pi Zero, Windows will then identify the network.

[ ![raspberry_pi_pizeroidentifying.png](https://cdn-learn.adafruit.com/assets/assets/000/029/338/medium800/raspberry_pi_pizeroidentifying.png?1451151051) __ ](/assets/29338)

[ ![raspberry_pi_unidentified.png](https://cdn-learn.adafruit.com/assets/assets/000/029/339/medium800/raspberry_pi_unidentified.png?1451151054) __ ](/assets/29339)

Now you can use a command box to run **ipconfig /all** if you want to check out the stats on the connection

[ ![raspberry_pi_ipconfig.png](https://cdn-learn.adafruit.com/assets/assets/000/029/340/medium800/raspberry_pi_ipconfig.png?1451151057) __ ](/assets/29340)

and **ping 192.168.7.2 **(the pi)

[ ![raspberry_pi_ping.png](https://cdn-learn.adafruit.com/assets/assets/000/029/341/medium800/raspberry_pi_ping.png?1451151058) __ ](/assets/29341)

and even **ssh!**

[ ![raspberry_pi_winssh.png](https://cdn-learn.adafruit.com/assets/assets/000/029/342/medium800/raspberry_pi_winssh.png?1451151059) __ ](/assets/29342)

#  Ethernet Tweaks

by [ lady ada ](/users/adafruit2)

#  Using mDNS/Bonjour Naming

If you don't want to have to remember your Pi's IP address, you don't have to! Jessie Lite includes and automatically enables **avahi **which lets you use names like **raspberrypi.local**

[If for some reason its not activated, we have a full tutorial that will help you get set up. ](../../../../bonjour-zeroconf-networking-for-windows-and-linux/overview)

**Don't forget, Windows doesn't have native Bonjour support, so download & install Bonjour Print Services!   
**(check the tutorial above for a link on where/how to install, you only have to do it once)

So, after you get ping'ing working...try **ping raspberrypi.local**

[ ![raspberry_pi_avahi.png](https://cdn-learn.adafruit.com/assets/assets/000/029/346/medium800/raspberry_pi_avahi.png?1451151072) __ ](/assets/29346)

Or for ssh, it's also perfectly fine:

[ ![raspberry_pi_localssh.png](https://cdn-learn.adafruit.com/assets/assets/000/029/349/medium800/raspberry_pi_localssh.png?1451151077) __ ](/assets/29349)

#  Sharing Network Access to Your Pi

On OS X, open the **Network** tab of System **Preferences.**

[ ![raspberry_pi_osx_network_system_pref.png](https://cdn-learn.adafruit.com/assets/assets/000/029/353/medium800/raspberry_pi_osx_network_system_pref.png?1451151095) __ ](/assets/29353)

Select the existing **CDC** or **RNDIS** USB connection to your Raspberry Pi by selecting **Manually** from the _Configure IPv4_ menu. Use **192.168.2.1** for the _IP Address_, and **255.255.255.0** for the _Subnet Mask_. Click _Apply_ to save your changes.

[ ![raspberry_pi_cdc_network_osx.png](https://cdn-learn.adafruit.com/assets/assets/000/029/352/medium800/raspberry_pi_cdc_network_osx.png?1451151091) __ ](/assets/29352)

Then, open the **Sharing** tab in System Preferences.

[ ![raspberry_pi_share_osx_system_pref.png](https://cdn-learn.adafruit.com/assets/assets/000/029/351/medium800/raspberry_pi_share_osx_system_pref.png?1451151085) __ ](/assets/29351)

Turn on **Internet Sharing** to share your existing internet connection from Wi-Fi or ethernet with the **CDC** or **RNDIS **Raspberry Pi connection.

[ ![raspberry_pi_cdc-network-osx-enable.png](https://cdn-learn.adafruit.com/assets/assets/000/029/350/medium800/raspberry_pi_cdc-network-osx-enable.png?1451151083) __ ](/assets/29350)

Edit your /etc/network/interfaces file on your Pi to match the one below.

Copy Code

    
    
    # interfaces(5) file used by ifup(8) and ifdown(8)
    
    # Please note that this file is written to be used with dhcpcd
    # For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
    
    # Include files from /etc/network/interfaces.d:
    source-directory /etc/network/interfaces.d
    
    auto lo usb0
    iface lo inet loopback
    
    iface eth0 inet manual
    
    allow-hotplug wlan0
    iface wlan0 inet manual
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    
    allow-hotplug wlan1
    iface wlan1 inet manual
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    
    allow-hotplug usb0
    iface usb0 inet manual
    
    
    # interfaces(5) file used by ifup(8) and ifdown(8)
    
    # Please note that this file is written to be used with dhcpcd
    # For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
    
    # Include files from /etc/network/interfaces.d:
    source-directory /etc/network/interfaces.d
    
    auto lo usb0
    iface lo inet loopback
    
    iface eth0 inet manual
    
    allow-hotplug wlan0
    iface wlan0 inet manual
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    
    allow-hotplug wlan1
    iface wlan1 inet manual
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    
    allow-hotplug usb0
    iface usb0 inet manual

The important lines are:

Copy Code

    
    
    auto lo usb0
    
    
    auto lo usb0

and also:

Copy Code

    
    
    allow-hotplug usb0
    iface usb0 inet manual
    
    
    allow-hotplug usb0
    iface usb0 inet manual

Restart your Pi using **sudo reboot**, and SSH back in to it using **ssh [[email protected]](/cdn-cgi/l/email-protection)**. You can then attempt to **ping google.com.**

Copy Code

    
    
    $ ping -c 5 google.com
    PING google.com (216.58.219.238): 56 data bytes
    64 bytes from 216.58.219.238: icmp_seq=0 ttl=55 time=20.975 ms
    64 bytes from 216.58.219.238: icmp_seq=1 ttl=55 time=20.904 ms
    64 bytes from 216.58.219.238: icmp_seq=2 ttl=55 time=20.646 ms
    64 bytes from 216.58.219.238: icmp_seq=3 ttl=55 time=20.401 ms
    64 bytes from 216.58.219.238: icmp_seq=4 ttl=55 time=20.379 ms
    
    --- google.com ping statistics ---
    5 packets transmitted, 5 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 20.379/20.661/20.975/0.247 ms
    
    
    $ ping -c 5 google.com
    PING google.com (216.58.219.238): 56 data bytes
    64 bytes from 216.58.219.238: icmp_seq=0 ttl=55 time=20.975 ms
    64 bytes from 216.58.219.238: icmp_seq=1 ttl=55 time=20.904 ms
    64 bytes from 216.58.219.238: icmp_seq=2 ttl=55 time=20.646 ms
    64 bytes from 216.58.219.238: icmp_seq=3 ttl=55 time=20.401 ms
    64 bytes from 216.58.219.238: icmp_seq=4 ttl=55 time=20.379 ms
    
    --- google.com ping statistics ---
    5 packets transmitted, 5 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 20.379/20.661/20.975/0.247 ms

If using Windows, open **Network and Sharing Center** and click on **Change Adapter Settings**

[ ![raspberry_pi_Screenshot_2016-11-22_18.06.14.jpg](https://cdn-learn.adafruit.com/assets/assets/000/037/771/medium800/raspberry_pi_Screenshot_2016-11-22_18.06.14.jpg?1480902554) __ ](/assets/37771)

Right-Click on your internet connection and select **P****roperties**.

[ ![raspberry_pi_Screenshot_2016-11-22_18.08.55.jpg](https://cdn-learn.adafruit.com/assets/assets/000/037/773/medium800/raspberry_pi_Screenshot_2016-11-22_18.08.55.jpg?1480902641) __ ](/assets/37773)

Select the **Sharing** tab. Click the checkbox if it is not already checked. Then click on **Select a private network connection** and select **PiZero** from the dropdown. 

[ ![raspberry_pi_Screenshot_2016-11-22_18.21.51.jpg](https://cdn-learn.adafruit.com/assets/assets/000/037/774/medium800/raspberry_pi_Screenshot_2016-11-22_18.21.51.jpg?1480902655) __ ](/assets/37774)

[ ![raspberry_pi_Screenshot_2016-11-22_18.24.59.jpg](https://cdn-learn.adafruit.com/assets/assets/000/037/775/medium800/raspberry_pi_Screenshot_2016-11-22_18.24.59.jpg?1480902759) __ ](/assets/37775)

Restart your Pi using **sudo reboot**, and SSH back in to it using **ssh [[email protected]](/cdn-cgi/l/email-protection)**. You can then attempt to **ping google.com.**

Copy Code

    
    
    $ ping -c 5 google.com
    PING google.com (216.58.219.238): 56 data bytes
    64 bytes from 216.58.219.238: icmp_seq=0 ttl=55 time=20.975 ms
    64 bytes from 216.58.219.238: icmp_seq=1 ttl=55 time=20.904 ms
    64 bytes from 216.58.219.238: icmp_seq=2 ttl=55 time=20.646 ms
    64 bytes from 216.58.219.238: icmp_seq=3 ttl=55 time=20.401 ms
    64 bytes from 216.58.219.238: icmp_seq=4 ttl=55 time=20.379 ms
    
    --- google.com ping statistics ---
    5 packets transmitted, 5 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 20.379/20.661/20.975/0.247 ms
    
    
    $ ping -c 5 google.com
    PING google.com (216.58.219.238): 56 data bytes
    64 bytes from 216.58.219.238: icmp_seq=0 ttl=55 time=20.975 ms
    64 bytes from 216.58.219.238: icmp_seq=1 ttl=55 time=20.904 ms
    64 bytes from 216.58.219.238: icmp_seq=2 ttl=55 time=20.646 ms
    64 bytes from 216.58.219.238: icmp_seq=3 ttl=55 time=20.401 ms
    64 bytes from 216.58.219.238: icmp_seq=4 ttl=55 time=20.379 ms
    
    --- google.com ping statistics ---
    5 packets transmitted, 5 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 20.379/20.661/20.975/0.247 ms

#  Other Modules!

by [ lady ada ](/users/adafruit2)

Serial and Ethernet are the easiest to get going but they are far from the _only_ gadgets the Linux kernel supports. You can also try such options as:

  * **Mass storage** (you can have the Pi appear as a 'USB key' disk drive ) - note, we didn't get this up and running smoothly, it enumerated but disk access to the backing file didnt work on our windows machine
  * **MIDI** \- shows up as a 'native' USB MIDI audio device
  * **HID** \- appear to the host computer as a mouse/keyboard/joystick
  * **Audio** \- Show up as an audio/speaker device & line in as well?
  * **Composite** \- a mix of serial/ethernet/mass storage composite devices is available. Note that this may work on a Mac or Linux but for windows you'd need a custom driver
  * **Printer, webcam, etc** \- There's about a dozen more options

[For more details, check out the USB gadget API framework page](http://www.linux-usb.org/gadget/)

[Sunxi also has a handy page](http://linux-sunxi.org/USB_Gadget)

We compiled all of the available USB gadget modules into the December 25, 2015 (or later) kernel tgz. You can enable them by using **modprobe** or editing the **/etc/modules** file to enable. If they need options, creating a new file for those options in **/etc/modprobe.d/usbgadget.conf** or similar

In particular, here's the modules that are available:

Copy Code

    
    
    #
    # USB Peripheral Controller
    #
    # CONFIG_USB_FUSB300 is not set
    # CONFIG_USB_FOTG210_UDC is not set
    # CONFIG_USB_GR_UDC is not set
    # CONFIG_USB_R8A66597 is not set
    # CONFIG_USB_PXA27X is not set
    # CONFIG_USB_MV_UDC is not set
    # CONFIG_USB_MV_U3D is not set
    # CONFIG_USB_M66592 is not set
    # CONFIG_USB_BDC_UDC is not set
    # CONFIG_USB_NET2272 is not set
    # CONFIG_USB_GADGET_XILINX is not set
    # CONFIG_USB_DUMMY_HCD is not set
    CONFIG_USB_LIBCOMPOSITE=m
    CONFIG_USB_F_ACM=m
    CONFIG_USB_F_SS_LB=m
    CONFIG_USB_U_SERIAL=m
    CONFIG_USB_U_ETHER=m
    CONFIG_USB_F_SERIAL=m
    CONFIG_USB_F_OBEX=m
    CONFIG_USB_F_NCM=m
    CONFIG_USB_F_ECM=m
    CONFIG_USB_F_EEM=m
    CONFIG_USB_F_SUBSET=m
    CONFIG_USB_F_RNDIS=m
    CONFIG_USB_F_MASS_STORAGE=m
    CONFIG_USB_F_FS=m
    CONFIG_USB_F_UAC1=m
    CONFIG_USB_F_UAC2=m
    CONFIG_USB_F_UVC=m
    CONFIG_USB_F_MIDI=m
    CONFIG_USB_F_HID=m
    CONFIG_USB_F_PRINTER=m
    CONFIG_USB_CONFIGFS=m
    CONFIG_USB_CONFIGFS_SERIAL=y
    CONFIG_USB_CONFIGFS_ACM=y
    CONFIG_USB_CONFIGFS_OBEX=y
    CONFIG_USB_CONFIGFS_NCM=y
    CONFIG_USB_CONFIGFS_ECM=y
    CONFIG_USB_CONFIGFS_ECM_SUBSET=y
    CONFIG_USB_CONFIGFS_RNDIS=y
    CONFIG_USB_CONFIGFS_EEM=y
    CONFIG_USB_CONFIGFS_MASS_STORAGE=y
    CONFIG_USB_CONFIGFS_F_LB_SS=y
    CONFIG_USB_CONFIGFS_F_FS=y
    CONFIG_USB_CONFIGFS_F_UAC1=y
    CONFIG_USB_CONFIGFS_F_UAC2=y
    CONFIG_USB_CONFIGFS_F_MIDI=y
    CONFIG_USB_CONFIGFS_F_HID=y
    CONFIG_USB_CONFIGFS_F_UVC=y
    CONFIG_USB_CONFIGFS_F_PRINTER=y
    CONFIG_USB_ZERO=m
    CONFIG_USB_AUDIO=m
    # CONFIG_GADGET_UAC1 is not set
    CONFIG_USB_ETH=m
    CONFIG_USB_ETH_RNDIS=y
    CONFIG_USB_ETH_EEM=y
    # CONFIG_USB_G_NCM is not set
    CONFIG_USB_GADGETFS=m
    CONFIG_USB_FUNCTIONFS=m
    CONFIG_USB_FUNCTIONFS_ETH=y
    CONFIG_USB_FUNCTIONFS_RNDIS=y
    CONFIG_USB_FUNCTIONFS_GENERIC=y
    CONFIG_USB_MASS_STORAGE=m
    CONFIG_USB_G_SERIAL=m
    CONFIG_USB_MIDI_GADGET=m
    CONFIG_USB_G_PRINTER=m
    CONFIG_USB_CDC_COMPOSITE=m
    CONFIG_USB_G_ACM_MS=m
    CONFIG_USB_G_MULTI=m
    CONFIG_USB_G_MULTI_RNDIS=y
    CONFIG_USB_G_MULTI_CDC=y
    CONFIG_USB_G_HID=m
    CONFIG_USB_G_DBGP=m
    # CONFIG_USB_G_DBGP_PRINTK is not set
    CONFIG_USB_G_DBGP_SERIAL=y
    CONFIG_USB_G_WEBCAM=m
    # CONFIG_USB_LED_TRIG is not set
    # CONFIG_UWB is not set
    CONFIG_MMC=y
    # CONFIG_MMC_DEBUG is not set
    
    
    #
    # USB Peripheral Controller
    #
    # CONFIG_USB_FUSB300 is not set
    # CONFIG_USB_FOTG210_UDC is not set
    # CONFIG_USB_GR_UDC is not set
    # CONFIG_USB_R8A66597 is not set
    # CONFIG_USB_PXA27X is not set
    # CONFIG_USB_MV_UDC is not set
    # CONFIG_USB_MV_U3D is not set
    # CONFIG_USB_M66592 is not set
    # CONFIG_USB_BDC_UDC is not set
    # CONFIG_USB_NET2272 is not set
    # CONFIG_USB_GADGET_XILINX is not set
    # CONFIG_USB_DUMMY_HCD is not set
    CONFIG_USB_LIBCOMPOSITE=m
    CONFIG_USB_F_ACM=m
    CONFIG_USB_F_SS_LB=m
    CONFIG_USB_U_SERIAL=m
    CONFIG_USB_U_ETHER=m
    CONFIG_USB_F_SERIAL=m
    CONFIG_USB_F_OBEX=m
    CONFIG_USB_F_NCM=m
    CONFIG_USB_F_ECM=m
    CONFIG_USB_F_EEM=m
    CONFIG_USB_F_SUBSET=m
    CONFIG_USB_F_RNDIS=m
    CONFIG_USB_F_MASS_STORAGE=m
    CONFIG_USB_F_FS=m
    CONFIG_USB_F_UAC1=m
    CONFIG_USB_F_UAC2=m
    CONFIG_USB_F_UVC=m
    CONFIG_USB_F_MIDI=m
    CONFIG_USB_F_HID=m
    CONFIG_USB_F_PRINTER=m
    CONFIG_USB_CONFIGFS=m
    CONFIG_USB_CONFIGFS_SERIAL=y
    CONFIG_USB_CONFIGFS_ACM=y
    CONFIG_USB_CONFIGFS_OBEX=y
    CONFIG_USB_CONFIGFS_NCM=y
    CONFIG_USB_CONFIGFS_ECM=y
    CONFIG_USB_CONFIGFS_ECM_SUBSET=y
    CONFIG_USB_CONFIGFS_RNDIS=y
    CONFIG_USB_CONFIGFS_EEM=y
    CONFIG_USB_CONFIGFS_MASS_STORAGE=y
    CONFIG_USB_CONFIGFS_F_LB_SS=y
    CONFIG_USB_CONFIGFS_F_FS=y
    CONFIG_USB_CONFIGFS_F_UAC1=y
    CONFIG_USB_CONFIGFS_F_UAC2=y
    CONFIG_USB_CONFIGFS_F_MIDI=y
    CONFIG_USB_CONFIGFS_F_HID=y
    CONFIG_USB_CONFIGFS_F_UVC=y
    CONFIG_USB_CONFIGFS_F_PRINTER=y
    CONFIG_USB_ZERO=m
    CONFIG_USB_AUDIO=m
    # CONFIG_GADGET_UAC1 is not set
    CONFIG_USB_ETH=m
    CONFIG_USB_ETH_RNDIS=y
    CONFIG_USB_ETH_EEM=y
    # CONFIG_USB_G_NCM is not set
    CONFIG_USB_GADGETFS=m
    CONFIG_USB_FUNCTIONFS=m
    CONFIG_USB_FUNCTIONFS_ETH=y
    CONFIG_USB_FUNCTIONFS_RNDIS=y
    CONFIG_USB_FUNCTIONFS_GENERIC=y
    CONFIG_USB_MASS_STORAGE=m
    CONFIG_USB_G_SERIAL=m
    CONFIG_USB_MIDI_GADGET=m
    CONFIG_USB_G_PRINTER=m
    CONFIG_USB_CDC_COMPOSITE=m
    CONFIG_USB_G_ACM_MS=m
    CONFIG_USB_G_MULTI=m
    CONFIG_USB_G_MULTI_RNDIS=y
    CONFIG_USB_G_MULTI_CDC=y
    CONFIG_USB_G_HID=m
    CONFIG_USB_G_DBGP=m
    # CONFIG_USB_G_DBGP_PRINTK is not set
    CONFIG_USB_G_DBGP_SERIAL=y
    CONFIG_USB_G_WEBCAM=m
    # CONFIG_USB_LED_TRIG is not set
    # CONFIG_UWB is not set
    CONFIG_MMC=y
    # CONFIG_MMC_DEBUG is not set

[Compiling your own kernel? Here's the v4.4 .config we used](https://learn.adafruit.com/system/assets/assets/000/029/354/original/.config?1451251999)

[You'll also have to patch the 'common' rpi overlay as shown here](https://github.com/raspberrypi/linux/issues/1212#issuecomment-165148405)

#  Old Kernel Install

by [ lady ada ](/users/adafruit2)

__ This is the older, no longer required technique - documented in case you need it! 

#  Step 0. Download new Kernel Package

Download the following onto your desktop computer:

[Download the modular Gadget Kernel TGZ file](http://adafruit-download.s3.amazonaws.com/gadgetmodulekernel_151226a.tgz)

and rename it **gadgetkernel.tgz**

#  Step 1. Copy New Kernel to SD Card

Copy the new kernel file over to the **boot** directory of the Jessie Lite card. After you're done burning the SD image, don't eject it just yet. Drag the **kernel.tgz** file over to the SD card. This way you can ferry the kernel into your Pi without needing network

[ ![raspberry_pi_copykernel.png](https://cdn-learn.adafruit.com/assets/assets/000/034/977/medium800/raspberry_pi_copykernel.png?1471833653) __ ](/assets/34977)

#  Step 2. Log into your Pi Zero

Insert the SD into your Pi Zero, connect the console cable, power the Pi & log into via the USB console.

[ ![raspberry_pi_1login.png](https://cdn-learn.adafruit.com/assets/assets/000/034/978/medium800/raspberry_pi_1login.png?1471833673) __ ](/assets/34978)

#  Step 3. Uncompress new kernel package

Uncompress and install the **kernel .tgz file**

 run the following commands:

  * **cd ~**
  * **sudo mv /boot/gadgetkernel.tgz .**
  * **tar -xvzf gadgetkernel.tgz**

[ ![raspberry_pi_2untar.png](https://cdn-learn.adafruit.com/assets/assets/000/034/979/medium800/raspberry_pi_2untar.png?1471833685) __ ](/assets/34979)

You'll see a long stream of file names ending with **tmp/boot/kernel.img**

__ You may see a bunch of complaints about timestamps being in the future, this is totally OK 

#  Step 4. Backup and Install new Kernel

Run

  * **sudo mv /boot/kernel.img /boot/kernelbackup.img**

to make a backup of the current kernel. Now run

  * **sudo mv tmp/boot/kernel.img /boot**

You may see complaints about preserving ownership, you can ignore them

[ ![raspberry_pi_3install.png](https://cdn-learn.adafruit.com/assets/assets/000/034/980/medium800/raspberry_pi_3install.png?1471833707) __ ](/assets/34980)

#  Step 5. Install Overlays & Modules

Run the commands to install the new overlays & modules

  * **sudo mv tmp/boot/overlays/* /boot/overlays**
  * **sudo mv tmp/boot/*dtb /boot**
  * **sudo cp -R tmp/boot/modules/lib/* /lib**

[ ![raspberry_pi_4install.png](https://cdn-learn.adafruit.com/assets/assets/000/034/981/medium800/raspberry_pi_4install.png?1471833754) __ ](/assets/34981)

[ ![raspberry_pi_5modules.png](https://cdn-learn.adafruit.com/assets/assets/000/034/982/medium800/raspberry_pi_5modules.png?1471833763) __ ](/assets/34982)

#  Gadget Serial!

Now we'll tell the Pi we want to use the **g_serial** module

Run

  * **sudo nano /etc/modules**

and add **g_serial** on a single line at the end, then save

[ ![raspberry_pi_gserialmod.png](https://cdn-learn.adafruit.com/assets/assets/000/034/988/medium800/raspberry_pi_gserialmod.png?1471836167) __ ](/assets/34988)

[Continue from this step for the rest of Serial Gadget setup and testing](../../../../turning-your-raspberry-pi-zero-into-a-usb-gadget/serial-gadget#set-up-logging-in-on-pi-zero-via-serial-gadget)

#  Gadget Ethernet!

Now we'll tell the Pi we want to use the **g_ether** module

Run

  * **sudo nano /etc/modules**

and add **g_ether** on a single line at the end, then save

[ ![raspberry_pi_gethermod.png](https://cdn-learn.adafruit.com/assets/assets/000/034/992/medium800/raspberry_pi_gethermod.png?1471836827) __ ](/assets/34992)

[ ![954-02.jpg](https://cdn-learn.adafruit.com/products/images/000/000/954/medium310/954-02.jpg?1504461887) ](https://www.adafruit.com/product/954)

USB to TTL Serial Cable - Debug / Console Cable for Raspberry Pi

$9.95 [OUT OF STOCK (NOTIFY ME)](https://www.adafruit.com/product/954)

[ ![2822-00.jpg](https://cdn-learn.adafruit.com/products/images/000/002/822/medium310/2822-00.jpg?1504462567) ](https://www.adafruit.com/product/2822)

Break-away 0.1" 2x20-pin Strip Dual Male Header

$0.95 [ ADD TO CART ](https://www.adafruit.com/product/2822)

[ ![2816-08.jpg](https://cdn-learn.adafruit.com/products/images/000/002/816/medium310/2816-08.jpg?1504462559) ](https://www.adafruit.com/product/2816)

Raspberry Pi Zero Starter Pack - Includes Pi Zero v1.3

$54.95 [OUT OF STOCK (NOTIFY ME)](https://www.adafruit.com/product/2816)

[ ![2817-02.jpg](https://cdn-learn.adafruit.com/products/images/000/002/817/medium310/2817-02.jpg?1504462562) ](https://www.adafruit.com/product/2817)

Raspberry Pi Zero Budget Pack - Includes Pi Zero v1.3

$29.50 [ ADD TO CART ](https://www.adafruit.com/product/2817)

[ ![2885-06.jpg](https://cdn-learn.adafruit.com/products/images/000/002/885/medium310/2885-06.jpg?1504462591) ](https://www.adafruit.com/product/2885)

Raspberry Pi Zero - Version 1.3

$5.00 [OUT OF STOCK (NOTIFY ME)](https://www.adafruit.com/product/2885)

ADD ALL TO CART

##  RELATED GUIDES 

#####  [ Using a Mini PAL/NTSC Display with a Raspberry Pi  
](/using-a-mini-pal-ntsc-display-with-a-raspberry-pi)

[ Use a tiny composite video display with a Raspberry Pi ](/using-a-mini-pal-ntsc-display-with-a-raspberry-pi)

by [ Simon Monk ](/users/simonmonk)

[ ![](https://s3.amazonaws.com/learn-production/guides/images/000/000/202/medium310/overview.jpg?1448301158) ](/using-a-mini-pal-ntsc-display-with-a-raspberry-pi)

[ In this tutorial, you will learn how to attach a miniature display to your Raspberry Pi and to adjust the Pi's settings to reduce the resolution sufficiently to read the screen. ](/using-a-mini-pal-ntsc-display-with-a-raspberry-pi)

[FEATURED](/guides/featured)

#####  [ Google Glass talks to Raspberry Pi with XMPP  
](/google-glass-talks-to-raspberry-pi-with-xmpp)

[ Connect Raspberry Pi with Google Glass ](/google-glass-talks-to-raspberry-pi-with-xmpp)

by [ Deqing Sun ](/users/DeqingSun)

[ ![](https://s3.amazonaws.com/learn-production/guides/images/000/000/341/medium310/google_glass2.jpg?1448301374) ](/google-glass-talks-to-raspberry-pi-with-xmpp)

[ This project enables Google Glass to talks to a hardware platform, raspberry Pi, with Mirror API and XMPP protocol. So users can access physical stuff with their Google Glass via voice commands. ](/google-glass-talks-to-raspberry-pi-with-xmpp)

#####  [ Adding Basic Audio Ouput to Raspberry Pi Zero  
](/adding-basic-audio-ouput-to-raspberry-pi-zero)

[ Get your Pi Zero singing ](/adding-basic-audio-ouput-to-raspberry-pi-zero)

by [ lady ada ](/users/adafruit2)

[ ![](https://s3.amazonaws.com/learn-production/guides/images/000/001/182/medium310/raspberry_pi_IMG_0074.jpg?1449202288) ](/adding-basic-audio-ouput-to-raspberry-pi-zero)

[ To keep the Raspberry Pi Zero as low cost and small as possible, the Pi foundation didn't include a 3.5mm audio jack. There's also no breakout pads for the audio output. This made us a little :( at first but then we thought "hey you know, we can probably figure out how to get audio out with a little hacking! ](/adding-basic-audio-ouput-to-raspberry-pi-zero)

#####  [ Resizing the Raspberry Pi Boot Partition  
](/resizing-raspberry-pi-boot-partition)

[ Long live Sneakernet! ](/resizing-raspberry-pi-boot-partition)

by [ Phillip Burgess ](/users/pburgess)

[ ![](https://s3.amazonaws.com/learn-production/guides/images/000/001/327/medium310/final-partitions.png?1464295452) ](/resizing-raspberry-pi-boot-partition)

[ Though the Raspberry Pi computer is eminently networkable, some projects still just work best by physically moving the SD card to a desktop system to exchange data…but normally only a small section of the card is accessible to Windows and Mac computers. This guide explains one way of making more space available to both the Pi and other systems. ](/resizing-raspberry-pi-boot-partition)

×

##### OUT OF STOCK NOTIFICATION

YOUR NAME

YOUR EMAIL

You have been successfully subscribed to the Notification List for this product and will therefore receive an e-mail from us when it is back in stock!

For security reasons, an e-mail has been sent to you acknowledging your subscription. Please remember that this subscription will not result in you receiving any e-mail from us about anything other than the restocking of this item.

If, for any reason, you would like to unsubscribe from the Notification List for this product you will find details of how to do so in the e-mail that has just been sent to you!

CLOSE NOTIFY ME

  * [CONTACT](https://www.adafruit.com/contact_us)
  * [SUPPORT](https://www.adafruit.com/support)
  * [DISTRIBUTORS](https://www.adafruit.com/distributors)
  * [EDUCATORS](https://www.adafruit.com/educators)
  * [JOBS](https://www.adafruit.com/jobs)
  * [FAQ](https://www.adafruit.com/faq)
  * [SHIPPING & RETURNS](https://www.adafruit.com/shippinginfo/)
  * [TERMS OF SERVICE](https://www.adafruit.com/terms_of_service/)
  * [PRIVACY & LEGAL](https://www.adafruit.com/privacy)
  * [ABOUT US](https://www.adafruit.com/about)

[ENGINEERED IN NYC](http://nytm.org/made-in-nyc/) Adafruit ®

"This good fun, explore, explore, explore, that's what science is, exploration, finding out new things, so have a good time with it" \- [Charles Townes](http://en.wikipedia.org/wiki/Charles_H._Townes)

![Seals 2x](/logos/seals_2x.jpg))
