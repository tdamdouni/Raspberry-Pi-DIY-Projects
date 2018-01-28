# How to use interrupts with Python on the Raspberry Pi and RPi.GPIO

_Captured: 2017-11-30 at 12:14 from [raspi.tv](http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio)_

![](http://raspi.tv/wp-content/uploads/2013/03/RasPi.TV-interrupt1_bb-150x150.jpg)

The latest big news in the world of Raspberry Pi Python GPIO programming is that [Ben Croston has released an update for RPi.GPIO](http://code.google.com/p/raspberry-gpio-python/). Why is that a big deal? Because this version has interrupts. "What's an interrupt?" I hear you say. It's a way of waiting for something to happen without checking constantly whether or not it's happening.

Imagine that you're waiting for a delivery - something you're really excited about - like a Pi camera.You spend far too much time looking down the street in eager anticipation of the postman's arrival. You can't fully focus on what you're supposed to be doing because you know it's imminent. Every time you hear something in the street, you jump up and look out of the window. Woe betide any door-knocking salesman who calls when you're expecting a delivery.

What I've just described in human terms is a bit like polling. Polling is continually checking for something. For example, if you want to make sure your program reacts as quickly as possible to a button press, you can check the button status about ten thousand times per second. This is great if you need a quick reaction, but it uses quite a bit of the computer's processing power. In the same way that you can't fully focus when you're expecting a delivery, a large part of your CPU is used up with this polling.

### There has to be a better way, right?

Yes. And there is. It's interrupts. This is the first in a series of articles which aim to show you how to use this new interrupt facility in Python.

Interrupts are a much more efficient way of handling the "wait for something to happen and react immediately when it does" situation. They free up the resources you would have wasted on polling, so that you can use them for something else. Then, when the event happens, the rest of your program is "interrupted" and your chosen outcome occurs.

So, to carry on our human example…  
An interrupt is like having an automatic postman detector that will tell you for sure when the postman arrives, so you can get on with something else. You now know you will not miss that knock on the door and end up with one of those "we tried to deliver your item but you were out and the collection office is closed for the next two days, so enjoy the wait" cards.

So interrupts are good, as you can set them up to wait for events to occur without wasting system resources.

### So how do you code them?

I'm going to show a simple "wait for a button press" example in this blog article and follow up with other examples in subsequent articles. But before you try this, you will quite likely need to update your RPi.GPIO package. You can check what version of RPi.GPIO you have in the command line with…

`sudo python  
import RPi.GPIO as GPIO  
GPIO.VERSION`

This should show you what RPi.GPIO version you have. You need 0.5.1 or higher for this example.  
You can exit the python environment with `CTRL+Z`

### Install RPi.GPIO version 0.5.1 for simple interrupts

If you need to, you can install 0.5.1 or later with  
`sudo apt-get update  
sudo apt-get dist-upgrade` (This will update all your Raspbian packages and may take up to an hour)

or, from the command line prompt (this will only update RPi.GPIO)…  
`wget http://raspberry-gpio-python.googlecode.com/files/python-rpi.gpio_0.5.1a-1_armhf.deb  
wget http://raspberry-gpio-python.googlecode.com/files/python3-rpi.gpio_0.5.1a-1_armhf.deb  
sudo dpkg -i python-rpi.gpio_0.5.1a-1_armhf.deb  
sudo dpkg -i python3-rpi.gpio_0.5.1a-1_armhf.deb`

### And now the circuit

![](http://raspi.tv/wp-content/uploads/2013/03/RasPi.TV-interrupt1_bb.jpg)

> _Circuit for simple button press interrupt_

It's simply a question of rigging up a button connecting 23 to GND when pressed.

### And now onto the code

I've put most of the explanation in the code, so that if you use it, you will still have it.

### Decoding the code

lines 4-5 import the RPi.GPIO module and set up the BCM port numbering scheme

line 8 sets GPIO 23 as an input with the pullup resistor set to UP.  
This means that the signal will be HIGH all the time until the button is pressed connecting the port to GND, which makes it LOW. This avoids false event detection.

lines 10-11 print some instructions  
line 12 waits for user to hit enter before starting. This gives an opportunity to check the wiring

lines 14-21 further instructions and documentation

line 22 `try:` & line 26 `except KeyboardInterrupt:`  
This allows us to run the program and exit cleanly if someone presses `CTRL-C` to stop the program. If we didn't do this, the ports would still be set when we forcefully exit the program.

line 23 sets up the "wait for the signal on port 23 to start falling towards 0"

lines 24-25 further on-screen instructions

line 27 cleans up the GPIO ports we've used during this program when `CTRL-C` is pressed  
line 28 cleans up the GPIO ports we've used during this program when the program exits normally

### Two ways to get the above code on your Pi

If you are in the command line on your Pi, type…  
`nano interrupt1.py`  
Then click "copy to clipboard" (above) and paste into the nano window.  
`CTRL+O  
Enter  
CTRL+X`

Alternatively, you can download this directly to your Pi using…  
`wget http://raspi.tv/download/interrupt1.py.gz  
gunzip interrupt1.py.gz`

Then you can run it with…  
`sudo python interrupt1.py`

### That's cool, what next?

So that was a simple "wait for a button press" interrupt. There's a lot more you can do with them, as I will show you in [the next article, which will cover "threaded callback"](http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-2), which allows us to use the spare capacity we've freed up by not polling continually.

[Click here for the next article (part 2)](http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-2)  
[Or check out the official documentation here ](http://code.google.com/p/raspberry-gpio-python/wiki/Inputs)and press on by yourself.

### RasPiO® GPIO Reference Aids

Our sister site [RasPiO has three really useful reference products for Raspberry Pi GPIO work...](https://shop.rasp.io/collections/reference/)
