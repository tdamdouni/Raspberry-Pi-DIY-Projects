# Environment Monitor

_Captured: 2017-08-02 at 13:13 from [frederickvandenbosch.be](http://frederickvandenbosch.be/?p=2242)_

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/IMG_3366.jpg)

For my first mini project of 2017, I will be trying out a couple of software tools I haven't used before: Etcher, Adafruit IO and Fusion 360. With the help of these tools, I will create a wall mounted environment monitor with a Pi Zero and Enviro pHAT.

Up until now, I've always been using the command line to burn images onto SD cards, using "dd". This process requires various commands to determine the device name, unmount and flash it.

Recently, [LifeHacker](http://lifehacker.com/etcher-is-the-easiest-way-to-make-a-raspberry-pi-sd-car-1790879312) posted an article about [Etcher](https://etcher.io/), a new, super easy to use tool to burn images onto SD cards. It's cross-platform, so it works on Windows, Linux and Mac!

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-18.52.22.png)

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-18.53.40.png)

The first step is to select an image. In this particular case, I used the latest [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) image. For the second step, the tool automatically tries to determine which device represents the SD card, so no action should be required unless multiple flash drives are connected. Finally, the flash process can be started. After a couple of minutes, the image is burned on the SD card!

To enable wifi and ssh without hooking up the Pi to a display:

  * put an empty file called _"ssh"_ on the SD card
  * put a file called _"wpa_supplicant.conf"_ with your network's SSID and key:

1234567 
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdevupdate_config=1network={ssid="<your ssid>"psk="<your key>"}

After boot, connect via SSH, and:

  * expand the filesystem
  * update the hostname
  * update the default SSH password
  * upgrade the installed packages

pi@raspberrypi:~ $ sudo raspi-configpi@enviropi:~ $ sudo apt-get update && sudo apt-get upgrade -y

The [Enviro pHAT](https://shop.pimoroni.com/products/enviro-phat) is one of the many awesome pHATs by [Pimoroni](https://shop.pimoroni.com/). It has a bunch of sensors on board to monitor your environment (pressure, temp, light, colour and motion) and some analog inputs to add your own.

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/IMG_3359.jpg)

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/IMG_3358.jpg)

As with many of their pHATs, the software can be installed with a single command:

The installation process will install the necessary files and enable the required interfaces such as I2C for example.

Earlier this week, my prize for the [Pi IoT Design Challenge](http://frederickvandenbosch.be/?p=1918) finally arrived: the CEL Robox 3D printer. So creating a mounting plate for the Pi Zero would be a great test for printing accuracy.

I normally design models in SketchUp, but seeing so many people use [Fusion 360](http://www.autodesk.com/products/fusion-360/overview), I thought I'd give it a try as well. The software can be downloaded as a trial version, but makers, hobbyists and startups can activate it for free!  
At first, the software was a bit intimidating, but I rather quickly managed to sketch something basic based on the Pi Zero's dimensions.

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-13.34.34.png)

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/Screen-Shot-2017-01-08-at-13.35.00.png)

The STL file of the model has been uploaded on [Thingiverse](http://www.thingiverse.com/thing:2023487) so anyone with access to a 3D printer can download and print it.

I printed the mounting plate with a resolution of 0.2mm and it fit without any post-processing!

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/IMG_3332.jpg)

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/IMG_3335.jpg)

[Adafruit IO](https://io.adafruit.com) (currently in beta) is an online system by Adafruit, that allows you to make data connections easily and with very little programming. Using various building blocks like buttons, sliders, graphs, etc … custom dashboards can be created to visualise your data.

The blocks are linked to feeds, which provide the data. The feeds are automatically created when using the client, but keep in mind that (due to the beta?) there is a limit of 10 feeds. For this particular application, this is enough.

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/Screen-Shot-2017-01-09-at-19.34.32.png)

![](http://frederickvandenbosch.be/wp-content/uploads/2017/01/Screen-Shot-2017-01-09-at-19.33.31.png)

A Python [client](https://github.com/adafruit/io-client-python) is available on Adafruit's GitHub page and can be installed easily, as follows:

I've created following script, capable of sending the data from the Enviro pHAT straight to IO. Don't forget to put your own IO client ID!

```
#!/usr/bin/env python

from envirophat import weather, light, analog, motion, leds

from Adafruit_IO import Client

# Personal Adafruit IO Key

aio = Client('<Adafruit IO Key>')

# Select which sensors to use

bmp280_enabled = True # Temp and Pressure

tc3472_enabled = True # Light and Colour

lsm303d_enabled = True # Motion and Heading

ads1015_enabled = False # Analog inputs

# Send the Enviro values to Adafruit IO feeds

if bmp280_enabled:

# Temperature

t = round(weather.temperature(), 1)

aio.send("enviro_temp", t)

# Pressure

p = round((weather.pressure()/100), 2)

aio.send("enviro_pressure", p)

if tc3472_enabled:

# Light

l = round(light.light(), 0)

aio.send("enviro_light", l)

# Colour

leds.on()

r, g, b = light.rgb()

leds.off()

aio.send("enviro_colour_r", r)

aio.send("enviro_colour_g", g)

aio.send("enviro_colour_b", b)

if lsm303d_enabled:

# Motion

x, y, z = motion.accelerometer()

aio.send("enviro_motion_x", x)

aio.send("enviro_motion_y", y)

aio.send("enviro_motion_z", z)

# Heading

h = motion.heading()

aio.send("enviro_heading", h)

if ads1015_enabled:

# Analog 0

a0 = round(analog.read(0), 2)

aio.send("enviro_analog_0", a0)

# Analog 1

a1 = round(analog.read(0), 2)

aio.send("enviro_analog_1", a1)

# Analog 2

a2 = round(analog.read(0), 2)

aio.send("enviro_analog_2", a2)

# Analog 3

a3 = round(analog.read(0), 2)

aio.send("enviro_analog_3", a3)
```

By adding the script to cron, it can be executed every minute, or whatever desired interval, automatically. To do this, use the crontab command:

Et voila, that's it, data should start appearing in the IO dashboard and be updated every minute.

What will you be monitoring? Let me know in the comments!
