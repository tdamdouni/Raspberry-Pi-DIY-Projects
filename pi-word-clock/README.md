Pi LED Matrix tools - Word Clock/Eyes/Text Scroller
===================================================

My 7 and 8yr old kids wanted to get started with electronics and programming,
 so we started off with an LED word clock. Since then, we have made a lot of
 projects with the Pi and we upload the Marix code (Word Clock, Scrolling Text,
 Halloween Eyes) here.

 See them in action [I2C Version](http://www.youtube.com/watch?v=Dd1wtXz80Cs) | [Unicorn Hat Colour Version](http://www.youtube.com/watch?v=QlTQ89PbJo4) | [Halloween LED Eyes](https://www.youtube.com/watch?v=rT0zYCxDIbY)

 Click the image below for the first project we made.

[![Raspberry Pi Word Clock](http://gurgleapps.com/assets/images/blog/raspberry-pi-word-clock-460x276.jpg)]
(http://www.youtube.com/watch?v=Dd1wtXz80Cs)

Click image below to see the LED Animated Eyes

[![Raspberry Pi Word Clock](http://img.youtube.com/vi/rT0zYCxDIbY/0.jpg)]
(https://www.youtube.com/watch?v=rT0zYCxDIbY)

Code & Images for making Word Clocks included. We used Raspberry Pi and 8x8 matrix. Works with I2C Adafruit Backpack and the Unicorn Hat from Pimoroni.

Code is Python & will possibly add a C version.

There are 8x8 fonts included and the ability to scroll messages or animate frames of 8x8 sprites. There is a tool at http://gurgleapps.com/tools/matrix which makes it easy to design 8x8 sprites and get the HEX code out.

The code has a demo mode to run through times, and takes command line arguments to set brightness and I2C address etc.

You can buy transparency paper for inkjet printers but even regular printer paper works quite well.

I2C Version
```bash
sudo python I2CWordClock.py
usage: I2CWordClock.py [-h] [--demo] [--address ADDRESS]
                       [--brightness BRIGHTNESS]

optional arguments:
  -h, --help            show this help message and exit
  --demo, -d            run through some example times
  --address ADDRESS, -a ADDRESS
                        I2C address default is 0x70
  --brightness BRIGHTNESS, -b BRIGHTNESS
                        LED brightness (0->15) default is 0
```

Unicorn Hat Version
```bash
sudo python UnicornWordClock.py
usage: UnicornWordClock.py [-h] [--demo] [--brightness BRIGHTNESS]

optional arguments:
  -h, --help            show this help message and exit
  --demo, -d            run through some example times
  --brightness BRIGHTNESS, -b BRIGHTNESS
                        LED brightness (0.0->1.0) default is 0.2
```

Instructions to get i2c working on a pi are [here](docs/new_pi_setup.md#i2c-setup)

Adafruit LED backpack
https://learn.adafruit.com/adafruit-led-backpack/overview

Pimoroni Unicorn Hat
http://shop.pimoroni.com/products/unicorn-hat

Template inspired by Daniel Rojas https://github.com/formatc1702/Micro-Word-Clock

