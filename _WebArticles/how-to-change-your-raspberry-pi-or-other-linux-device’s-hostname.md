# How to Change Your Raspberry Pi (or Other Linux Device’s) Hostname

_Captured: 2017-08-24 at 13:00 from [www.google.de](https://www.google.de/amp/s/www.howtogeek.com/167195/how-to-change-your-raspberry-pi-or-other-linux-devices-hostname/amp/)_

![](https://www.howtogeek.com/wp-content/uploads/2013/07/xraspberrynewhostheader.jpeg.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.NNgCMn7BWu.jpg)

The default hostname for the Raspberry Pi is, creatively enough, "`raspberrypi`". What if you want a different hostname or you want to avoid hostname conflicts on your local network? Read on as we show you how to quickly change the hostname of a Linux-based device.

## Why Do I Want to Do This?

There are two primary reasons why you would want to take a few minutes to edit the local hostname of a Linux device on your network. The most common reason would simply be customization-it's fun to personalize things. Rather than leave your Raspberry Pi music station as plain old "`raspberrypi`", for example, you could rename it to "`jukebox`".

The other reason you would want to customize the local host is to avoid name conflicts. If you, for example, have purchased and set up three Raspberry Pi units, all three of them (assuming a default Raspbian installation) will attempt to claim the local hostname "`raspberrypi`".

The first one will succeed and the next two will fail to resolve their hostnames, leaving them blank in your router's device list (as seen in the screenshot above) and unreachable via hostname-based protocols like Samba file sharing.

Fortunately it's super simple, assuming you know where to perform a few quick edits, to change the hostname of your Raspberry Pi (and most other Linux-based devices you have full access to). For demonstration purposes we'll be performing the change on [a stock Raspbian installation](https://www.howtogeek.com/138281/the-htg-guide-to-getting-started-with-raspberry-pi/all/), but the same file edits will work on Debian, Ubuntu, and most other Linux platforms.

## Changing the Host on your Pi

We have so many Raspberry Pi units around the office that a bunch of them are now in conflict. Today we're going to fix that by assigning unique names to each Pi unit based on their current function. A perfect candidate for this renaming is our awesome [Raspberry Pi weather station](https://www.howtogeek.com/140063/build-an-led-indicator-with-a-raspberry-pi-for-email-weather-or-anything/all/); it will be much easier to identify it on the network once we change the hostname to "`weatherstation`".

The first step is to either open up the terminal on the device or to SSH into the device and open up a remote terminal. Our device is headless and currently running, so we'll take the remote terminal route and connect to it via SSH.

At the terminal, type the following command to open the hosts file:

> `sudo nano /etc/hosts`

Your hosts file will look like so:

Leave all of the entries alone except for the very last entry labeled `127.0.1.1` with the hostname "`raspberrypi`". This is the only line you want to edit. Replace "raspberrypi" with whatever hostname you desire. We replaced it on our device with "`weatherstation`". Press CTRL+X to close the editor; agree to overwrite the existing file and save it.

Back at the terminal, type the following command to open the hostname file:

> `sudo nano /etc/hostname`

This file only contains your current hostname:

Replace the default "`raspberrypi`" with the same hostname you put in the previous step (e.g. "`weatherstation`"). Again, press CTRL+X to close the editor, agree to overwrite the existing file and save it.

Finally, we need to commit the changes to the system and reboot the system for the changes to take effect. At the terminal, enter the following command to commit the changes:

> `sudo /etc/init.d/hostname.sh`

Follow that command with:

> `sudo reboot`

Once the system comes back online, you can check the device list in your router to see if the new hostname has properly resolved:

Success! Now instead of wandering the network without a name, our little Raspberry Pi weather station has a hostname all its own.
