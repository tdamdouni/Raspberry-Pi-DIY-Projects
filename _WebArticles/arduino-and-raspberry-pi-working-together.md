# Arduino and Raspberry Pi Working Together

_Captured: 2017-05-13 at 08:58 from [dzone.com](https://dzone.com/articles/arduino-and-raspberry-pi-working-together?edition=298091&utm_source=Daily%20Digest&utm_medium=email&utm_campaign=dd%202017-05-12)_

Basically, everything we can do with Arduino it can be done with a Raspberry Pi (and vice versa). Sure, there are things that are easy to do with Arduino (connecting sensors for example), but other things (such as working with REST servers and databases) are "complicated" with Arduino and C++ (they are possible but require a lot of low-level operations). Meanwhile, those difficult tasks are pretty straightforward with Raspberry Pi and Python (at least for me and because of my background).

With this small project, I want to use an Arduino board and Raspberry Pi together. The idea is blinking two LEDs. One (a green one) will be controlled by the Raspberry Pi directly via GPIO, and the other one (a red one) will be controlled by the Arduino board. The Raspberry Pi will be the "brain" of the project and will tell the Arduino board when to turn on/off its LED. Let's show the code.
    
    
            s.write("1\n" if status else "0\n")

As we can see, the script is a simple loop and blinks the LED (using pin 12) with an interval of one second. Our Arduino board is connected directly to the Raspberry Pi via USB cable and we send commands via serial interface.

Finally, the Arduino program:

Here, our Arduino board is listening to the serial interface (with serialEvent), and each time we receive "\n", the main loop will turn on/off the LED depending on the value (1 = on, 0 = off).

We can use I2C and other ways to connect an Arduino and a Raspberry Pi, but in this example, we're using the simplest way to do it: A USB cable. We only need an A/B USB cable. We don't need any other extra hardware (such as resistors) and the software part is pretty straightforward also.

Hardware:

  * Arduino UNO
  * Raspberry Pi 3
  * Two LEDs and two resistors

The code is in my GitHub [account](https://github.com/gonzalo123/arduino_RPi_together/).
