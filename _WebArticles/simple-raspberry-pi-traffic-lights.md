# Simple Raspberry Pi Traffic Lights

_Captured: 2017-08-08 at 17:42 from [4tronix.co.uk](https://4tronix.co.uk/blog/?p=219)_

## Using Breadboard, LED & Resistors to Create a Traffic Light

**Click on any image to enlarge**

### Fritzing Diagram

![tl04](http://4tronix.co.uk/blog/wp-content/uploads/2014/03/tl04-265x300.jpg)

### PiCard:

![picard02](http://4tronix.co.uk/blog/wp-content/uploads/2014/03/picard02-221x300.jpg)

### Assembling Hardware

Pop the PiCard pinout display over the GPIO pins on your Raspberry Pi ® making sure that pin 2 is in the corner of the board. This allows you to easily see where to plug the wires.

Push the LEDs and resistors (cut the legs shorter on the resistors first) into the breadboard as shown. LEDs have a positive and a negative leg. Positive leg on the right above is longer. Make sure you plug them in the correct way round or they will not work.

  * Connect resistor on Red LED to pin 7
  * Connect resistor on Amber LED to pin 11
  * Connect resistor on Green LED to pin 13
  * Connect negative leg of Red LED to pin 6
  * Connect negative leg of Amber LED to pin 14
  * Connect negative leg of Green LED to pin20
  * Connect one side of switch to pin 22
  * Connect other side of switch to pin 25

### Completed Traffic Lights

![tl03b](http://4tronix.co.uk/blog/wp-content/uploads/2014/03/tl03b-300x209.jpg)

### Programming

To light the LEDs you need to make the corresponding GPIO pin High. Make the pin low to turn off the light.

  * Red is on **pin 7**
  * Amber is on **pin 11**
  * Green is on **pin 13**

To read the switch you need to read on **pin 22**. A High value ('1′) when the switch is up (not pressed) and a Low value ('0′) when the switch is pressed.

### Python Examples

Download the example code [from here ](http://www.4tronix.co.uk/rpi/TrafficKit01.py)and place it in your home directory on the Raspberry Pi.Then you can run it by typing:

_sudo python TrafficKit01.py_

This will light the LEDs in the well know traffic light sequence. Now try to edit the code to make it do something different.

You can download the second demo example [from here](http://www.4tronix.co.uk/rpi/TrafficKit02.py) and run it with:

_sudo python TrafficKit02.py_

This will light the LEDs in sequence but will also check the button occasionally and force it to the Red if the button is pressed

### ScratchGPIO Examples

You will need to first install ScratchGPIO if you haven't already. Go to [SimpleSi's page](http://cymplecy.wordpress.com/scratchgpio/)

Within ScratchGPIO you can switch the Red LED on with

Switch it off again with

Similarly you can use the other pins for the Yellow and Green LEDs. A complete Traffic Light Sequence is shown here:

![traffic](http://4tronix.co.uk/blog/wp-content/uploads/2014/03/traffic-149x300.jpg)

You can download this [from here](http://www.4tronix.co.uk/rpi/Traffic01.sb)
