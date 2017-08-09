# My Experiments With IoT: Meeting With Pi

_Captured: 2017-02-26 at 23:50 from [dzone.com](https://dzone.com/articles/my-experiments-with-iot-meeting-with-pi?edition=272906&utm_source=Daily%20Digest&utm_medium=email&utm_campaign=dd%202017-02-26)_

When I heard the term IoT from one of my colleagues back in 2012, I thought it was just a piece of tech that seemed to be very far from my world. Later, when I started working with Arduino and Raspberry Pi in 2015, I realized the potential.

## **How It Started**

I am a graduate in computer science, with not a lot of interest in electronics. During my college days, we had a paper on electronics and my score was "just passed." My prime focus was programming languages and their concepts -- I tried to learn as many programming languages as I could during my college days. It seemed very easy for me to learn new languages as I tried to understand the concepts first, then the constructs. It was in 2015 when one of my colleagues explained to me the workings of Raspberry Pis. I was quite interested in it, and there began a new phase of my learning.

## **The IoT Life **

After hearing about Raspberry Pi, I decided to buy one from Amazon after a little research. My initial experiments included connecting the Pi to my TV using HDMI and trying a different OS in it so I wouldn't be limited to Raspian, the default OS. I also tried BerryBoot, RetroPie, and XMBC in my Pi. I used the device for playing games as well as using it as a media hub. Soon, I realized that I was deviating from the purpose that I had bought the Pi for. Anyone can do those things. I needed to try something unique, something innovative. That thought drove me into the world of the Internet of Things.

## **Who Can Learn IoT?**

Anyone with a fair knowledge of C++, Node.js, or Python and with a little common sense can jump in.

## **Let's Begin**

Let's start with the basics: electronics. What you need to understand here is that current flows in a closed loop and not in an open loop. If you place an LED in a circuit between the positive and ground terminal, the LED turns on.

![](http://vinodsr.com/myblog/wp-content/uploads/2017/02/Closed-Loop.png)

In other words, a binary one (1) can be used to represent where there is voltage (+) and a binary zero (0) to represent the ground. These 1s and 0s are the basics of electronics circuits and thus the building blocks of IoT.

## **The Basics of Raspberry Pi**

There are different types of Raspberry Pis out there, like Pi 2, Pi 3, Pi Zero, etc. Each of these differs from each other in terms of specifications like chipsets, RAM size, USB ports, display ports, etc. But in general, they have a set of pins called GPIO (General Purpose Input Output) pins. Apart from the GPIO pins, there are specific purpose pins like clock pins, ground pins, 5V pins, 3.3V pins, etc. These pins have a specific purpose, whereas we can programmatically set the GPIO pins to a high or low state. We can use C++, Node.js, or Python for controlling the GPIO pins.

![Image result for raspberry pi 2 model b pinout](http://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg)

Each GPIO pin has a number associated with it. See the above pin diagram for more details. For now, we will use a small Node.js script to work with our Pi with the help of the [rpio library](https://github.com/jperkin/node-rpio). To install it, just use this command:

Below is a small Node.js snippet to set GPIO pin 12 (GPIO 18) to high, then to low five times every 500 milliseconds.
    
    
    var rpio = require('rpio');
    
    
    rpio.open(12, rpio.OUTPUT, rpio.LOW);
    
    
    for (var i = 0; i < 5; i++) {

![Image title](https://dzone.com/storage/temp/4426665-pi-led.png)

So if I connect an LED pin to the GPIO pin 12 (GPIO 18), then the LED will blink at an interval of 2 seconds! Wow! We did our Hello World! on a Raspberry i.P Coming back to how it worked, let's check this out:

The above code initializes pin 12 to output mode and sets the default value as zero.

The write method then keeps the pins high and low periodically, which makes the LED blink.

## **Processing Input**

![Image title](https://dzone.com/storage/temp/4426667-pi-led-buton.png)
    
    
    var rpio = require('rpio');
    
    
    rpio.open(15, rpio.INPUT, rpio.PULL_DOWN);
    
    
    rpio.open(12, rpio.OUTPUT, rpio.LOW);
    
    
        var state = rpio.read(pin) ? rpio.HIGH :rpio.LOW ;

So, with this script, upon clicking on the button, it will make GPIO pin 15 high, which is captured as an interrupt, and the logic is executed, which will turn the LED on.

This way, you can control almost any sensor using a Raspberry Pi/Arduino.
