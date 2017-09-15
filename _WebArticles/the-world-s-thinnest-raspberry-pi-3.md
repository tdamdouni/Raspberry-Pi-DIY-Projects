# The World's Thinnest Raspberry Pi 3*

_Captured: 2017-09-11 at 22:24 from [blog.pimoroni.com](http://blog.pimoroni.com/slimming-down-a-pi-3/)_

For [last week's Bilge Tank](https://www.youtube.com/watch?v=NQvRNU3sTtI), we decided to have a little fun and tried to create what we dubbed the World's Thinnest Raspberry Pi 3*, by removing all of the bulky pins and ports. The original intention was to try to do it in under 30 minutes, but we didn't quite manage that, although we did do it in less than an hour.

Here's a TL;DR of the Bilge Tank episode!

_*not officially ratified by the Guinness Book of World Records_

![Slim Pi, top down](http://blog.pimoroni.com/content/images/2017/09/slim-pi-1.jpg)

## Isn't that... a Pi Zero?

Well, it's more or less that, quite literally. The Pi 3 has a much more capable quad core processor compared with the Pi Zero, especially handy if you're planning to embed a Pi into a handheld games console, for example, which may require a bit more grunt.

Once stripped down, our Pi 3 is actually almost exactly the same thickness as a Pi Zero and, of course, we could have removed the micro-USB port as well, and supplied power by soldering wires to the GPIO (the Pi 3 is actually a hair thicker, since the micro-SD card slot is on the bottom unlike the Zero / W).

![Slim Pi vs. Pi Zero W](http://blog.pimoroni.com/content/images/2017/09/slim-pi-2-1.jpg)

## Thinning down the Pi

You can watch the [Bilge Tank episode](https://www.youtube.com/watch?v=NQvRNU3sTtI) for the full details but, briefly, here's how we did it...

The first step was to unfold the metal shrouding on the USB and ethernet ports and pull/snap the plastic guts out of them. After doing that, it was simply a case of desoldering and pulling out the pins.

Next, we removed the GPIO pins. We started by trying to remove the plastic shrouding, as this would free up all of the pins and allow them to be pulled out individually, however the shrouding was tougher than we bargained for. We ended up using the hot air gun!

The HDMI, CSI, and DSI connectors again need the hot air gun to remove them. The metal body of the HDMI port is a single piece of thick metal, unlike the wrapped, thinner metal of the USB and ethernet ports, so it couldn't be easily snipped off to leave the pins at our mercy.

After the show, we used the solder sucker and some desoldering braid to clean up the desoldered joints a bit, et voila, the World's Thinnest Pi 3*!

## Thinning down the software

Since we removed the HDMI and USB/ethernet ports, it didn't really make any sense having them enabled in Raspbian, so we disabled them. It's fairly straightforward.

To disable the USB/ethernet, we used the following snippet of code, that disables the device driver.
    
    
    sudo sh -c "echo 0 > /sys/devices/platform/soc/3f980000.usb/buspower"  
    

And to disable the HDMI, you can use the following.
    
    
    tvservice -o  
    

Both of these commands can be wrapped in a little bash script and then set to run when your Pi reboots with the crontab `@reboot` command.

Disabling both of these dropped the current draw (while idle) from about 260mA to 180mA, so it's a pretty significant power saving.

You can watch the whole Bilge Tank episode below.
