# An introduction to GPIO and physical computing on the Raspberry Pi

One powerful feature of the Raspberry Pi is the row of General-Purpose Input/Output (GPIO) pins along the top edge of the board. Models A+, B+, Pi 2, and Pi 3 have 40 pins that look like this:

![GPIO pins](images/gpio-pins-pi2.jpg)

These pins are a physical interface between the Pi and the outside world. At the simplest level, you can think of them as switches that you can turn on or off (input) or that the Pi can turn on or off (output). Of the 40 pins, 26 are GPIO pins and the others are power or ground pins. There are also two ID EEPROM pins which you should not play with unless you know your stuff!

![GPIO layout](images/gpio-numbers-pi2.png)

Models A and B have only 26 pins and look like this:

![](images/gpio-pins.jpg)

Note that the numbering of the GPIO pins is a little unusual. Our guide to [GPIO Pin Numbering](sensing-the-weather/guides/GPIO/pin-numbering.md) explains why.

## What are the GPIO pins for? What can I do with them?

You can program the GPIO pins to interact with the real world in amazing ways. Inputs don't have to come from a physical switch: an input could be from a sensor, or a signal from another computer or device, for example. The output can also do anything, from turning on an LED to sending a signal or some data to another device. If the Raspberry Pi is connected to a network, you can control other devices that are attached to it and those devices can send data back; you can do this from almost anywhere, provided your devices have the requisite network connection and power. Control of physical devices over the internet is a powerful and exciting thing, and the Raspberry Pi is ideal for this. There are lots of brilliant examples of physical computing on [our blog](http://www.raspberrypi.org/blog/).

## How the GPIO pins work

### Output

**WARNING**: If you follow the instructions, then experimenting with the GPIO pins is safe and fun. Randomly plugging wires and power sources into your Pi, however, may kill it. Bad things can also happen if you try to connect things to your Pi that use a lot of power: LEDs are fine, motors are not. If you are worried about this, then you might want to consider using a breakout board such as the [Pibrella](http://pibrella.com/) until you are confident enough to use the GPIO directly.

Setting the Pi aside for a moment, one of the simplest electrical circuits that you can build is a battery connected to a light source and a switch (the resistor is there to protect the LED):

![Simple circuit](images/simple-circuit.png)

When we use a GPIO pin as an output, the Raspberry Pi replaces **both the switch and the battery** in the above diagram. Each pin can turn on or off, or go HIGH or LOW in computing terms. When the pin is HIGH it outputs 3.3 volts (3V3); when the pin is LOW it is off.

Here's the same circuit using the Raspberry Pi. The LED is connected to a GPIO pin (which can output +3V3) and a ground pin (which is 0V and acts like the negative terminal of the battery):

![GPIO wth LED](images/gpio-led-pi2.png)

The next step is to write a program to tell the pin to go HIGH or LOW. Here's an example using [Python](http://www.raspberrypi.org/learning/quick-reaction-game/) (see Step 2 of the resource), and here's how to do it in [Scratch](http://www.raspberrypi.org/learning/robot-antenna/).

### Input

GPIO are straightforward in that they are on or off, HIGH or LOW, 3V3 or 0V. Inputs are a bit trickier because of the way that digital devices work. Although it might seem reasonable just to connect a button across an input pin and a ground pin, the Pi can get confused as to whether the button is on or off. It might work properly, it might not. It's a bit like floating around in deep space; without a reference it would be hard to tell if you were going up or down, or even what up or down meant!

This is why you will see phrases like "pull up" and "pull down" in Raspberry Pi GPIO tutorials. It's a way of giving the input pin a reference so it knows for certain when an input is received.

If you'd like to have a go at using the GPIO as an input then have a look at our [Buring Jelly Baby](http://www.raspberrypi.org/learning/burping-jelly-baby/) and [Quick Reaction Game](http://www.raspberrypi.org/learning/quick-reaction-game/) tutorials for Python, or a [Reaction Game](http://www.raspberrypi.org/learning/reaction-game/) for Scratch.

We hope that this has encouraged you to have a go at physical computing using the Pi's GPIO pins; it's really not as daunting as it looks. It all starts with a simple LED, but it can take you to incredible places. Do not underestimate the fun, creativity, and sense of achievement you can get from a little computer and a bunch of pins. Have fun, and let us know what you make! 

---

## Glossary

### GPIO

General-Purpose Input/Output. In this specific case, this refers to the pins on the Raspberry Pi and what you can do with them. They are named this way because you can use them various purposes; most can be used as either inputs or outputs, depending on your program.

### LED

Light-emitting diode. A small, low-power light source used widely in electronics. Ideal as an introduction to physical computing on the Pi.

### Physical computing

Computing that involves tangible things connected to a computer, beyond standard input and output devices like keyboards and monitors. Think buttons, lights, robots, alarms, sensors, home automation, teddy bears called Babbage in near space, and so on. We love physical computing because as well as being lots of fun, it's such a powerful teaching and learning tool. It encourages creativity, problem solving, and collaboration. Computing beyond the screen engages children of all ages, and you can make very cool stuff!

