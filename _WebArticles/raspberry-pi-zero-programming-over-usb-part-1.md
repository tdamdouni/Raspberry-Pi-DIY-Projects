# Raspberry Pi Zero – Programming over USB! (Part 1)

_Captured: 2017-09-03 at 23:34 from [blog.gbaman.info](http://blog.gbaman.info/?p=699)_

![](http://blog.gbaman.info/wp-content/uploads/2015/12/IMG_5140-1038x576.jpg)

#### _Part 2 to this post can be [found here](http://blog.gbaman.info/?p=791). _

_**Update 19/05/2016** - The modules are now included in the most recent version of Raspbian and thanks to some digging around in kernel documentation, it is now possible to set the full thing up without a keyboard/mouse/screen! Just need a Windows/Mac/Linux computer!_

_**Update 15/01/2016** - The modules have now been merged into the Raspberry Pi Foundation maintained kernels! So no more need for custom kernels, just need to grab the most recent alpha kernels. Doing this is now far simpler._

Full credit for the initial documentation for this goes to a number of Pi experts from the Raspberry Pi community, see [here](https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=129653) and [here](https://github.com/raspberrypi/linux/pull/1239).

An acknowledgement also to Lady Ada of Adafruit who was working on documenting in parallel to myself on Christmas eve. She has taken a different approach which requires a UART serial cable. Her guide can be found [here](https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget).

## What is this?

The Raspberry Pi Zero is a very cool little computer. At £4, is pretty amazing for the price. But one thing many Pi users have wanted to be able to do for a long time is program their Raspberry Pi from another computer, **using only a single USB cable!**

The Raspberry Pi Zero is able to do this, hardware wise anyway, although a lack of software support was holding up it ever happening. Until now!

## So what can it do?

Using the Linux USB Gadget modules, we can get the Pi Zero to emulate a whole host of USB devices including

  * Virtual Serial - So can get a serial connection into the Pi, similar to using the UART pins. You can use Putty (on Windows) or Screen (on Mac and Linux).
  * Virtual Ethernet - You can get your Pi Zero to appear as a USB Ethernet modem. With a little configuration, you can then get full SSH, VNC, FTP etc.
  * Mass storage device - You can get the Pi Zero to appear as a flash drive, allowing you to for example, copy files over and have the Pi run these files (useful for robotics for example)
  * Virtual MIDI - The Pi Zero could appear as a virtual MIDI instrument.
  * Virtual Audio - The Pi Zero could appear as a virtual headphone output or microphone input.
  * Virtual Human Interface Device (HID) - The Pi Zero could appear as a virtual HID, for example a keyboard or mouse. So when you plug it into your computer, it could start typing!

You can also combine a few of the above (up to 3 at a time) using the g_multi module, although Windows and Mac have difficulty handling it then.

## Examples

Where is this useful? Lets take an example of some Raspberry Pi robots in a classroom. Although you could be using Wifi for each robot, remembering addresses, unreliability with wifi etc all make wifi a bit of a rubbish answer.  
With this, the student simply plugs in the robot and perhaps drops their script onto the flash drive that appears. When they unplug it, the robot runs the script, dumping the results of the script back onto the mass storage device, ready to be read when it is plugged in next.

Another example, lets say you don't have access to a screen to use with your Raspberry Pi Zero, in for example, a school. You could still let your students play with GPIO or Linux by simply using the serial module (with Putty or Screen), or the virtual ethernet module to allow them SSH access.

## How to I set it up on my Raspberry Pi?

I have thrown together a [guide over on Github Gists](https://gist.github.com/gbaman/50b6cca61dd1c3f88f41), including links to the downloadable precompiled kernels.

Simple guide for setting up OTG modes on the Raspberry Pi Zero - By Andrew Mulholland (gbaman).

The Raspberry Pi Zero (and model A and A+) support USB On The Go, given the processor is connected directly to the USB port, unlike on the B, B+ or Pi 2 B, which goes via a USB hub.  
Because of this, if setup to, the Pi can act as a USB slave instead, providing virtual serial (a terminal), virtual ethernet, virtual mass storage device (pendrive) or even other virtual devices like HID, MIDI, or act as a virtual webcam!  
It is important to note that, although the model A and A+ can support being a USB slave, they are missing the ID pin (is tied to ground internally) so are unable to dynamically switch between USB master/slave mode. As such, they default to USB master mode. There is no easy way to change this right now.  
It is also important to note, that **a USB to UART serial adapter is not needed for any of these guides**, as may be documented elsewhere across the internet.

##Which process should I choose?  
There are 2 routes you can take for setting up the Raspberry Pi Zero as a USB Slave (OTG mode).

  1. **The quick route** \- The quick route doesn't require anything beside your Pi Zero, SD card and a Windows, Mac or Linux computer. It though only supports setting up the Pi Zero as a virtual Ethernet device (allowing full SSH, SFTP, VNC etc). For any of the other USB Gadget drivers (beside g_ether), use route 2.
  2. **The modular slower, but more flexible route** \- This route requires a screen and keyboard to configure your Pi Zero once it has completed its first boot.

###1. Very quick way (No USB keyboard, mouse, HDMI monitor needed)  
The newer method has now been brought out into a separate Gist, [which can be found here](http://bit.ly/pi-otg).

###2. Modular, but slower to setup method For this method, a Pi Zero, SD card (with Raspbian Jessie lite or full), screen and keyboard are required.  
You are able to set up any of the below modules using this method and are not just limited to `g_ether`. The required kernels are also now shipped with Raspbian 2016-05-10 releases and beyond. So no need to do a `raspi-update`.  
No web connectivity is required, nor is a USB-UART adapter required for this method. This documentation is based off the initial excellent work done on this [Github pull request](https://github.com/raspberrypi/linux/pull/1239).  
**Modules included**

  * Serial (g_serial)
  * Ethernet (g_ether)
  * Mass storage (g_mass_storage)
  * MIDI (g_midi)
  * Audio (g_audio)
  * Keyboard/Mouse (g_hid)
  * Mass storage and Serial (g_acm_ms)
  * Ethernet and Serial (g_cdc)
  * Multi (g_multi) - Allows you to configure 2 from Ethernet, Mass storage and Serial  
In addition to the above modules, a few other (less useful) modules are included.
  * Webcam (g_webcam)
  * Printer (g_printer)
  * Gadget tester (g_zero)
  1. First, flash Jessie (only tested on full, lite version may also work though) onto a blank microSD card.
  2. **(step only needed if running Raspbain version before 2016-05-10)** Once it starts up again, run `sudo BRANCH=next rpi-update`. This will take a while.
  3. Next we need to make sure we are using the dwc2 USB driver `echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt`.
  4. And enable it in Raspbian `echo "dwc2" | sudo tee -a /etc/modules`
  5. Need to now pick which module you want to use from the list above, for example for ethernet `echo "g_ether" | sudo tee -a /etc/modules`. You can only pick one of the above modules to use at a time.
  * **g_serial** \- To use the standard serial module, you need to tell the Pi to forward the serial console to it with `sudo systemctl enable getty@ttyGS0.service`, then you can connect to the device via Putty or Screen.
  * **g_ether** \- Using virtual ethernet, you should simply be able to ssh into the address of your Raspberry Pi. To do this, there is a little extra configuration required though. There is a few ways we could set up the point to point networking. The proper way would be to set up a DHCP server on one of the ends. A far simplier was though is just to give the Raspberry Pi a fixed IP address. To do this, you will need to run `echo -e "interface usb0 \nstatic ip_address=169.254.64.64" | sudo tee -a /etc/dhcpcd.conf`. You can then access the Raspberry Pi Zero by connecting to `169.254.64.64`, or by using `raspberrypi.local` if your computer has Bonjour installed (Mac and most Linux OSs including Raspbian). Note this method does not support adding a fixed address to the cmdline.txt file. For that, you have to use the Ethernet only kernel below.
  * **g_mass_storage** \- To have your Pi Zero appear as a mass storage device (flash drive), first create a mini filesystem in a file on your Pi with `sudo dd if=/dev/zero of=/piusb.bin bs=512 count=2880` and set it up as a fat32 filesystem with `sudo mkdosfs /piusb.bin`. Then, when enabling it, add `file=/piusb.bin stall=0` onto the end, for example `sudo modprobe g_mass_storage file=/piusb.bin stall=0`.

In theory, most USB devices should work alongside these kernels, to switch to USB OTG mode, simply don't use an OTG adapter cable and use a standard USB cable to plug your Pi Zero into another computer, it should auto switch.

The legacy guides can be [found on a separate Gist](https://gist.github.com/gbaman/4c1345c0c4d6d82149d4).
