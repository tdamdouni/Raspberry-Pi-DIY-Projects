# 1 Micro:Bit + 1 Raspberry Pi 3 + 1 Bluez Upgrade = 1 Huge Headache

_Captured: 2017-08-08 at 17:27 from [www.element14.com](https://www.element14.com/community/community/stem-academy/microbit/blog/2016/09/16/1-microbit-1-raspberry-pi-3-1-bluez-upgrade-1-huge-headache)_

_Updated 9/21/2016 to include an image and Bluez/BLE setup instructions for Raspbian "Jessie" on Raspberry Pi 3._

Oh deary dear...this is not what I wanted to do on a Thursday afternoon.

Some background:

I recently won an opportunity to build an "alert button" project using a Micro:Bit and a Raspberry Pi (thanks again, element14!). The Micro:Bit will be shipping soon, and the Raspberry Pi (not supplied by element14) is sitting in my office humming very warmly under a table, waiting to be put to work.

![microbit.jpg](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-24107-325046/290-386/microbit.jpg)

Coincidentally, a Mini Maker Faire took place last weekend in my city, and one of the workshops at the event was about Micro:Bits. I made sure I was first in line, and lucky me, the first 20 people got a free Micro:Bit. That was a very nice surprise! So, all week I've been playing around with a Micro:Bit while I wait for the element14 Micro:Bit to arrive.

Communication between a Micro:Bit and my Raspberry Pi is central to my project. Both devices support Bluetooth Low Energy (BLE), so I figured I'd be in good shape communication-wise. What I didn't consider was _how well_ BLE is supported on Raspbian, which is the version of Linux running on the Raspberry Pi. And by "how well BLE is supported," I actually mean "how _little_ BLE is supported." In fact, I'm pretty sure there is no distribution of Linux for Raspberry Pis that supports BLE out of the box. BLE support is experimental at best, and you can't even get the experimental support without replacing a tricky software package/suite called "Bluez". The version of Bluez in the latest Raspbian (Linux on Raspberry Pi) is 5.23, but you need at least version 5.40 to get BLE. And folks, let me tell you, this is one BEAR of a package to replace. It's ugly, very ugly, and even when it's installed and allegedly running it does not always work as expected. To make things even more fun, there are many forums and webpages that discuss upgrading Bluez, but none of them describes 100% of the process.

I managed to upgrade Bluez today. I took detailed notes as I upgraded, and they are shared below. The problem is, like anything that sporadically works on Linux, good instructions can get you 95% of the way to a solution but that last 5% is going to resemble throwing spaghetti at a wall. Maybe that's why none of the online help takes you 100% of the way toward a solution? Once the software is installed and running, nothing short of a series of random power on/off cycles, scan sessions, connect and pairing attempts, reboots, etc will get the Micro:Bit seen and paired. Once paired, the pairing seems to stick at least for a while. Sometimes the pairing mysteriously drops and the process begins again. And even when the Micro:Bit is paired and connected, experimenting with its GATT attributes is sometimes effective, sometimes not so effective. After a few hours of experimenting, I felt like a caveman banging two rocks together trying to get them to talk.

Anyway, here are the steps and/or commands that I executed to get Bluez/BLE set up on my Raspberry Pi so my Micro:Bit could at least pair and connect to it:

**sudo apt-get install bluetooth**

**sudo apt-get install bluez-tools**

**sudo apt-get install build-essential**

**sudo apt-get install autoconf**

**sudo apt-get install glib2.0**

**sudo apt-get install libglib2.0-dev**

**sudo apt-get install libdbus-1-dev**

**sudo apt-get install libudev-dev**

**sudo apt-get install libical-dev**

**sudo apt-get install libreadline-dev**

Download and extract the latest Bluez source code (v5.41 is the latest as of 9/21/2016):

**tar xf bluez-5.41.tar.xz**

Change into the directory created by the **tar** command above, then configure, build, and install Bluez:

**cd bluez-5.41**

**./configure --prefix=/usr \**

** \--mandir=/usr/share/man \**

** \--sysconfdir=/etc \**

** \--localstatedir=/var \**

** \--enable-experimental \**

** \--enable-maintainer-mode**

**make**

**sudo make install**

You may want to play with **gatttool** at some point. It is part of Bluez and is built in the make step above, but it is not installed by default. You will need to manually install it (optional):

**sudo cp attrib/gatttool /usr/local/bin**

Enable experimental support in the bluetooth daemon (this enables BLE). Put this all on a single command line:

**sudo sed -i '/^ExecStart.*bluetoothd\s*$/ s/$/ --experimental/' /lib/systemd/system/bluetooth.service**

Raspbian installs bluetooth firmware in directory not recognized by Bluez, so make a symbolic link (it's like a Windows alias) that references the firmware directory in the location Bluez expects it to be in (/etc/firmware):

**sudo ln -s /lib/firmware /etc/firmware**

Now, enable bluetooth to load during system boot, then reload daemons to load it without rebooting, or just reboot after enabling it.

**sudo systemctl enable bluetooth**

**sudo systemctl daemon-reload**

The following seems to be needed every time the Raspberry Pi boots. This should go in a startup script somewhere, but I have not figured out which one yet. For now, every time the Raspberry Pi reboots, just run this command:

**/usr/bin/hciattach /dev/ttyAMA0 bcm43xx 921600 noflow -**

At this point, you should be able to run **bluetoothctl** as root (**sudo bluetoothctl**) and start playing. If you wish to do bluetoothy things as user _pi_, allegedly you can make this happen by duplicating the entire policy for user _root_ and changing _root_ to _pi_ in /etc/dbus-1/system.d/bluetooth.conf. Just copy/paste the entire section from the opening _root_ policy tag to its closing policy tag and edit the username. I suspect you need to be _root_ to do other things so I won't promote this as a solid path to follow. It's best to stick with _root_ (**sudo _command_**).

Some people think it's best to set the bluetooth system to be BLE-only. If you want to do this, ensure that /etc/bluetooth/main.conf contains the following line:

**ControllerMode = le**

I tried this and did not notice any difference, but your mileage may vary.

One last thing. Be sure to suspend updates to the Bluez package in Raspbian, otherwise you'll overwrite your hand-built version of Bluez next time you update/upgrade:

**sudo apt-mark hold bluez**

To remove the hold at a later date:

**sudo apt-mark unhold bluez**

WHEW, that's a lot of steps just to get one package updated. Quite frankly, I'm surprised that the Raspbian folks use such an outdated version of Bluez in "Jessie" considering that bluetooth is one of the Raspberry Pi's bigger selling points.

As a backup plan, I took a shot in the dark and ordered two 2.4GHz transceivers via eBay in case the vanilla 2.4GHz radio support in the Micro:Bit works better without being clogged with BLE. Something tells me the Micro:Bit radio protocol relies on Micro:Bits speaking only with other Micro:Bits, but the transceivers were dirt cheap so I won't be upset if they don't work like I want them to. I'll do something else with them, I guess. The transceivers have arrived, and as soon as I come up with a method by which Micro:Bits can chat with Raspberry Pis via a transceiver, I'll write another post. This one's long enough.

I was inclined to write this off as a Raspberry Pi + Bluez issue more than a Micro:Bit issue, but my two Roku boxes have had no problems being seen by Bluez while Micro:Bits have been more finicky, so the issues I've experienced are probably a combination of Bluez, Raspberry Pi's bluetooth hardware, and Micro:Bit's bluetooth hardware. Don't know. It will work eventually, I just know it.

Onward.
