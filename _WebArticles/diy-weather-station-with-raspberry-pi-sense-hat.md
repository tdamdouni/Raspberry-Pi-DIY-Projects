# DIY Weather Station with Raspberry Pi Sense HAT

_Captured: 2017-05-19 at 10:12 from [www.anavi.org](https://www.anavi.org/article/195/)_

### Mobile & Embedded

Keywords: **DIY, humidity, IoT, Linux, Node.js, pressure, Python, Sense HAT, temperature, Yocto, Raspberry Pi**

## Rabbit Pi Weather Station

Recently I joined [the second edition of the Eclipse Open IoT challenge](http://iot.eclipse.org/open-iot-challenge/). I am working on a hobby IoT project. I want to create do it yourself (DIY) weather station using Raspberry Pi 2 Model B and the add-on board [Raspberry Pi Sense HAT](https://www.raspberrypi.org/products/sense-hat/).

Sense HAT was initially created for the Astro Pi space mission. It contains RGB LED matrix and bunch of sensors. Nowadays [Farnell](http://uk.farnell.com/raspberry-pi-sense-hat) sells it for a bit less than 30 EUR.

The installation is super easy. Attach the add-on board, plug microSD card and launch Raspberry Pi.

The import part is the software. It will retrieve information about temperature, humidity and barometric pressure from the sensors and will display it on the LED matrix. There is an infinite loop so the weather station should work forever or at least until it is not turned off. The first values retrieved from the sensors immediately after boot are not very accurate but it gets better after that.

## How does it work?

I am using a custom distribution for Raspberry Pi that suits the exact needs of my project. I have created this distribution using Poky from the Yocto Project and Openembedded. Systemd service launches a Node.js script at startup. This script uses a couple of Python scripts to retrieve data from the I2C sensors and to print text on the RGB LED matrix.

Rabbit Pi is an open source project and the whole source code is [available at GitHub](https://github.com/RabbitPi/weather-station). In order to get it working you need to enable I2C kernel drivers for Raspberry Pi and to install sense-hat Python modules.
