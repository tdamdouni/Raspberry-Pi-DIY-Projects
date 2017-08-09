# Raspberry Pi Zero Headless Setup

_Captured: 2017-05-23 at 19:01 from [davidmaitland.me](https://davidmaitland.me/2015/12/raspberry-pi-zero-headless-setup/)_

![raspberry-pi-zero-otg](https://davidmaitland.me/images/posts/raspberry-pi-zero-otg.jpg)

**Update Mar 2017:** Works with the new Pi Zero W!

So last Thursday (26th Nov 2015) the [Raspberry Pi Zero](https://www.raspberrypi.org/blog/raspberry-pi-zero/) was announced and made available that very day. Basically the Zero is a small and ultra cheap (£[4](https://shop.pimoroni.com/products/raspberry-pi-zero)) fully functioning Raspberry Pi, but it doesn't have any native networking and has only one USB port (which you need an OTG adapter to use).

In the UK I was lucky enough to be able to order two Pi Zero's and have them delivered the next day. The only problem was I didn't have an HDMI monitor or a USB hub to connect a keyboard and a WiFi adapter at the same time. My intended use for the Zero's is for them to be little headless Linux boxes that I can put into various electronic projects and program them over WiFi (Think [IoT](https://en.wikipedia.org/wiki/Internet_of_Things)), so I didn't want to mess around with HDMI and GUI interfaces.

So here is a little guide showing you how to setup a Raspberry Pi Zero without an HDMI monitor or a keyboard / mouse. We will just use a USB WiFi adapter (connected to the OTG USB port) and a Linux machine to do the setup. If you don't have a Linux machine available, you could even use another Rasberry Pi with a card reader to set this up.

_This should be possible to do on other platforms as well but you will need to be able to mount an Ext4 partition natively._

## Step One - Install the Linux image

First you will need to install a copy of Raspbian Jessie onto your micro SD card. You can find the downloads [here](https://www.raspberrypi.org/downloads/raspbian/) and the installation guides are on the same page as well. For Linux I will be using [this](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md) guide.

## Step Two - Mounting it locally

After you have copied the Raspbian image onto the SD card you will need to mount it to your system. The easiest way to do this is just unplug your card reader and plug it back in.

Once the drive has mounted to your system you will need to find where it has mounted. An easy way to do this is using the command `df -h`. For me it returns:

I can see from this my 64GB SD card is the device **/dev/sdc** and the boot and main partition are mounted under `/run/media/davidmaitland/`. Change directory into the main partition as root ready to edit the files. This is likely to be the same drive that was referenced during the image installation earlier.

## Step Three - Configure your WiFi

Next we're going to configure the network interface. Edit the interfaces file `etc/network/interfaces`. Pay attention to the path in the files I reference, there is no leading slash as you want to edit the files on your SD card and not the ones on your host system!

_If you're not sure how to edit files on Linux, try `nano etc/network/interfaces` then `Ctrl + x` to save when done._

Find this block in the file:

Then change it to this:

If you want to have a static IP instead of using DHCP (easier to find once the Pi has come up on your network) then change it to this instead:

As pointed out by someone on Reddit, if you're using static networking you will want to setup your DNS servers as well. Edit `etc/resolv.conf` and add the following:

Now let's setup the WiFi connection and passkey. Edit the file `etc/wpa_supplicant/wpa_supplicant.conf`.

Add this to the end:

**Update (16/02/17)**

[@stevegraken](https://disqus.com/by/stevegraken) in the comments pointed out that in newer versions of Raspbian SSH is disabled by default, which is something we will need.

You can [read more about this here](https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/).

To make it work again you need to create an empty file named `ssh` in the `boot` mount. This is a completely different mount point, so you will have to change directories to get there. _(Thanks to Chris T for pointing out what I had overlooked)_

Here are the results of the command `df -h` which we ran earlier, you can see the `sdc` partitions and their corresponding mount points at the bottom:

On my system I'm currently on partition 2 (`/dev/sdc2`) which is mounted at `/run/media/davidmaitland/ad6203a1-ec50-4f44-a1c0-e6c3dd4c9202` (my current directory). We need to change to partition 1 (`/dev/sdc1`) by running `cd /run/media/davidmaitland/boot`.

Now all you have to do is add an empty file named `ssh`:

_Remember to change the default password (use `passwd`) after you have setup your Pi!_

Finally remove the SD card from your computer (you may wish to unmount it first) and place into your Zero.

## Step Four - Boot the Pi Zero!

Now it's time to boot the Raspberry Pi Zero. Make sure you have your WiFi adapter plugged into the Zero and give it some power. For me it takes about **45** seconds to boot and connect to my WiFi network.

Now you can SSH directly into your Raspberry Pi Zero!

If you configured your Zero to use DHCP you will need to find it's IP address. There are a few ways you can do this:

  * Most routers will tell you somewhere in their web interfaces what IP allocations they have assigned to devices.
  * You could use [nmap](https://nmap.org) to scan the local network for devices running with port 22 open `sudo nmap -p22 -sV 192.168.0.0/24`.
  * From the comments _Coder-256_ pointed out the default hostname for a Raspberry Pi is `raspberrypi` and on most networks you can SSH directly to this instead of the IP address `ssh pi@raspberrypi.local`.

The default password is `raspberry`.

## Extras

After a new install there are a few things you're probably going to want to do.

First I would update the software running on your Zero:

If you're going to be using your Zero completely headlessly like me there are various things you can do to save energy and speed up the device.

Boot up into multi-user mode (disable GUI on boot) `sudo systemctl set-default multi-user.target`.

To disable HDMI edit `/etc/rc.local` and add the following line at the bottom above `exit 0` line:

You may want to run `sudo raspi-config` to change other common Raspberry Pi settings as well.

Let me know below if this guide was useful or if you have any suggestions!

[Nimvelo Phone](http://www.nimvelo.com/recommend/NzE5LDkzMg) is the best no contract phone system for your business.   
Get £[20 calling credit for free](http://www.nimvelo.com/recommend/NzE5LDkzMg) when you sign up.
