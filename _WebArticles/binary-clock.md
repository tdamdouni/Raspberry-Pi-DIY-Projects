# Binary Clock

_Captured: 2017-05-19 at 10:08 from [frederickvandenbosch.be](http://frederickvandenbosch.be/?p=1999)_

![](http://frederickvandenbosch.be/wp-content/uploads/2016/10/IMG_2592.jpg)

I've had a [Unicorn pHAT](https://shop.pimoroni.com/products/unicorn-phat) sitting in a box for a while, but I finally used it in a simple project. Because it has four rows of LEDs, I thought it would be ideal to make a binary clock from.

Let me show you how

This project can be tackled in two ways:

  * an online version fetching time via NTP (network time protocol)
  * an offline version using a RTC (real time clock)

In this instance, I'm focusing on the _online_ version, though the offline version could be achieved as easily with an RTC shim such as the one pictured below, which can slide on the GPIO header between the Pi Zero and the Unicorn pHAT:

![img_2591](http://frederickvandenbosch.be/wp-content/uploads/2016/10/IMG_2591.jpg)

## Electronics

At the center of the project are a PiZero and a Unicorn pHAT. The PiZero fetches the time, converts it to binary and controls the Unicorn pHAT with a Python script. The Unicorn pHAT's RGB LED matrix can be used to display those binary values in any colour.

In order to have the Unicorn pHAT face forward, while still having the Pi Zero connectors at the back, an angled header was used.

![img_2555](http://frederickvandenbosch.be/wp-content/uploads/2016/10/IMG_2555.jpg)

## Enclosure

The enclosure is a combination of acrylic and wood, except this time, the acrylic makes for the majority of the enclosure.

To form the acrylic in the desired shape, a small torch was used to heat it and have it bend 90 degrees. Once cooled off, it retains the new shape. Repeating this action two more times, the final shape is achieved. Careful not to put the torch too close to the acrylic to prevent it from burning or leaving marks!

To finish the enclosure, two wooden "end caps" were milled using the CNC and the edges rounded with a router, though a similar result could be achieved with a bandsaw and some manual sanding for example.

![img_2563](http://frederickvandenbosch.be/wp-content/uploads/2016/10/IMG_2563.jpg)

![img_2564](http://frederickvandenbosch.be/wp-content/uploads/2016/10/IMG_2564.jpg)

On the software side of things, I started off with the latest Raspbian Jessie Lite image from 23/09. Set up network connectivity via wifi by editing the _"wpa-supplicant.conf"_ file.

Once network connectivity was set up, I proceeded with the upgrade of the software:

Don't forget to make sure the time is set to the correct zone:

## Unicorn pHAT

Installing the software to control the Unicorn pHAT and its dependencies, is a breeze as always thanks to [Pimoroni's](https://shop.pimoroni.com/) installation wizard:

I chose a full install, including examples, though they are not required for this project. To know more about the installer, head over to the Unicorn HAT [GitHub](https://github.com/pimoroni/unicorn-hat) page.

## Binary Clock

For the binary clock, I created s mall script which takes the time, converts it to binary format and lights up the correct LEDs on the Unicorn pHAT. A cronjob ensures the script is started at boot time.

Here's the full script:

#!/usr/bin/env python

import unicornhat as unicorn

import time

unicorn.set_layout(unicorn.PHAT)

unicorn.brightness(0.5)

unicorn.rotation(180)

while 1:

decimal = time.strftime("%H%M%S")

decimal_list = list(decimal)

for x in xrange(0, 6):

binary = bin(int(decimal_list[x]))[2:].rjust(4, '0')

binary_list = list(binary)

for y in xrange(0, 4):

if binary_list[y] == '1':

unicorn.set_pixel(x+1,y,255,255,255)

else:

unicorn.set_pixel(x+1,y,0,0,0)

unicorn.show()

time.sleep(1)

Make sure the downloaded script is executable:

Finally, add the cron job:

Upon reboot, you should see the LEDs light up on the Unicorn pHAT!

You are of course free to change the colours for both the time and the background:

![img_2593](http://frederickvandenbosch.be/wp-content/uploads/2016/10/IMG_2593.jpg)

![img_2596](http://frederickvandenbosch.be/wp-content/uploads/2016/10/IMG_2596.jpg)

![img_2594](http://frederickvandenbosch.be/wp-content/uploads/2016/10/IMG_2594.jpg)

Hope you liked this project, let me know in the comments!
