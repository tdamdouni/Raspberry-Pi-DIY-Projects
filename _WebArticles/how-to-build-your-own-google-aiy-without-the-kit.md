# How to Build Your Own Google AIY without the Kit

_Captured: 2017-11-09 at 22:47 from [hackaday.com](https://hackaday.com/2017/05/30/diy-google-aiy/)_

![](https://hackadaycom.files.wordpress.com/2017/05/aiy-feat.jpg?w=800)

Google's voice assistant has been around for a while now and when Amazon released its Alexa API and ported the PaaS Cloud code to the Raspberry Pi 2 it was just a matter of time before everyone else jumped on the fast train to maker kingdom. Google just did it in style.

Few know that the Google Assistant API for the Raspberry Pi 3 has been out there for some time now but when they decided to [give away a free kit](https://hackaday.com/2017/05/04/google-aiy-artificial-intelligence-yourself/) with the May 2017 issues of MagPi magazine, they made an impression on everyone. Unfortunately the world has more makers and hackers and the number of copies of the magazine are limited.

In this writeup, I layout the DIY version of the AIY kit for everyone else who wants to talk to a cardboard box. I take a closer look at the free kit, take it apart, put it together and replace it with DIY magic. To make things more convenient, I also designed an enclosure that you can 3D print to complete the kit. Lets get started.

## The Teardown

![](https://hackadaycom.files.wordpress.com/2017/05/sensors.png)

A shout out to my friend [Shabaz] in the UK for sending me a copy of the MagPi. The "Google AIY Projects Voice Kit"(henceforth known as the kit) contains two PCBs and a bunch of other stuff. The Voice HAT which looks like a Sound-Card-On-A-Diet has very limited number of components. I will detail each section and draw the KiCAD schematic for the same one by one

### Servos

![aiy-servos](https://hackadaycom.files.wordpress.com/2017/05/aiy-servos.jpg?w=299&h=282)

![servos](https://hackadaycom.files.wordpress.com/2017/05/servos.png?w=493&h=282)

Starting from the left side, there are 6 sets of 3-pin headers that are labelled 'Servos'. The intended servo control is made possible using the Raspberry Pi 3's on-board PWM module. Each set has a GPIO pin, 5V and GND connection. The GPIO pin does not connect directly to the Raspberry Pi 3's header but rather through 220Ohm current limiting resistors (labelled R1-R6).

### Power Supply

![aiy-power](https://hackadaycom.files.wordpress.com/2017/05/aiy-power.jpg?w=241&h=261)

![power](https://hackadaycom.files.wordpress.com/2017/05/power.png?w=551&h=261)

Just south of these are devices labeled Q5 and Q6 which I am assuming are part of a power supply selection circuit. Correct me if I am wrong but here is my estimate. The working is simple where Q5 only turns ON when the input voltage is greater than the 5V from the USB port. A simple comparator should do so I am using the LM393 for reference.

EDIT: [Raivsr] pointed out that this could be the equivalent of the Raspberry Pi 'Ideal Diode'.

### Communication Interfaces

![](https://hackadaycom.files.wordpress.com/2017/05/aiy-terminals.jpg)

North of the 'Servo' headers is J15 labelled I2C that directly connect to the Raspberry Pi 3 header. That means these should not be connected to anything with 5V pull-ups. They are not being used on the board but we will discuss more on this later. Right next to it is the SPI and 2-pin UART headers. Again these connect directly to the main header and serve only as a breakout.

### The DAC and EEPROM

![aiy-chips](https://hackadaycom.files.wordpress.com/2017/05/aiy-chips.jpg?w=299&h=261)

![MAX98357A](https://hackadaycom.files.wordpress.com/2017/05/max98357a.png?w=493&h=261)

A little lower and we arrive at the boxed circuit with a 16-Pin QFN marked 'AKK BDQ'. This is the Maxim MAX98357A([PDF](https://datasheets.maximintegrated.com/en/ds/MAX98357A-MAX98357B.pdf)) which is an I2S DAC with a class D amplifier. It drives the speaker directly however since there is only one output, it can only be mono or combined stereo. It's still pretty rocking for the budget.

The interesting thing is the presence of JP6 which seems to have all the I2S connections from the Maxim MAX98357A and a few other select lines. Combined with the two vias that connect to the second speaker output, you could possibly fit another Maxim MAX98357A breakout board on top to get stereo sound. I am going to do the schematic and make it downloadable and if you want to give it a shot let me know the results. Consider it optional homework.

![](https://hackadaycom.files.wordpress.com/2017/05/eeprom.png)

Next to the DAC is an 8-pin SSOP which is a 24C32 ([PDF](http://www.st.com/content/ccc/resource/technical/document/datasheet/80/4e/8c/54/f2/63/4c/4a/CD00001012.pdf/files/CD00001012.pdf/jcr:content/translations/en.CD00001012.pdf)) I2C EEPROM. It's not connected to the I2C header I talked about earlier but rather to pins 27 and 28 of the Raspberry Pi 3 header. According to the Raspberry Pi Foundation's blog.

> "The EEPROM holds the board manufacturer information, GPIO setup and a thing called a 'device tree' fragment - basically a description of the attached hardware that allows Linux to automatically load the required drivers."

So its got some extra sauce that makes things tick and I could use a BusPirate to Dump the data but I am not sure if Google considers it Intellectual Property so I won't. I have an alternative for it as well so read on.

### Drivers

![aiy-drivers](https://hackadaycom.files.wordpress.com/2017/05/aiy-drivers1.jpg?w=387&h=561)

![drivers](https://hackadaycom.files.wordpress.com/2017/05/drivers.png?w=405&h=561)

Moving towards the right, we find 4 headers marked 'Drivers'. These are MOSFET circuits for controlling loads such as relays. [Shabaz] did a great job tracing out the components on this one and the 3 pins are GPIO, 5V and Driver.

The MOSFETs can drive loads of up to 500mA each thanks to a polyswitch however the GPIOs are available for use directly as well. Loads to be driven should be connected between the pins marked '+' and '-'. The header pin on the left is a direct access to GPIOs header pins from the Raspberry Pi 3 and the schematic reflects the same.

Use these to connect LEDs or similar devices to indicate the operation of the relays or loads.

### Microphone and Button Connectors

More interesting stuff is happening on the right side's upper right with a push button and two JST connectors. The 4 pin connector is meant for the push button that sits on top of the assembled enclosure. The small PCB mounted push button is wired in parallel with the external switch and can be used in its place while setting up and testing. The 5 pin JST is for the microphone connector and has all the I2S pins.

### The Microphones

![aiy-mic](https://hackadaycom.files.wordpress.com/2017/05/aiy-mic.jpg?w=226&h=170)

![mic](https://hackadaycom.files.wordpress.com/2017/05/mic.png?w=566&h=170)

![](https://hackadaycom.files.wordpress.com/2017/05/aiy-assembled.jpg?w=690&h=800)

Lastly, the microphone board is marked 432 QDF21G, and has Knowles SPH0645LM4H MEMs digital microphones that talk I2S directly.

## That's It!

That about wraps up the teardown and all the information required to make your own AIY Kit. The KiCAD schematic files are available for download from [GitHub](https://github.com/inderpreet/DIY-AIY) however I leave you with the fun part which is the layout and routing.

Here is some food for thought. Some parts can be omitted and the size of the hat can be shrunk down to the Pi Zero pHat.

For simplicity reasons, I am using the preconfigured OS image from the Google AIY page. It is a tad short of 900MB and can be downloaded directly from Goolge ([huge file](https://dl.google.com/dl/aiyprojects/voice/aiyprojects-latest.img.xz)).

## Add A Shutdown Button

![](https://hackadaycom.files.wordpress.com/2017/05/aiy-shutdown1.jpg)

You probably noticed the small golden button next to the big green button in the image above and that is the first part of the exercise. It is a shutdown button and is added because I don't want to SSH to the box every time I want to turn it off safely.

Get the button you want to use and add two wires with female headers. This bit works even without the Voice Hat so feel free to try it out. Next if you have a voice hat, add male headers to the I2C part. You may choose any other pins and it will still work. Connect the button to the SDA or GPIO 2 and boot the Pi 3 up.

Open up your favourite text editor and copy-paste the following code into it.

```
#!/bin/python
# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh
 
import RPi.GPIO as GPIO
import time
import os
 
# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(02, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
# Our function on what to do when the button is pressed
def Shutdown(channel):
    os.system("sudo shutdown -h now")
 
# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(02, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)
# Now wait!
while 1:
    time.sleep(1)
```

Save the files in your /home/pi folder as shutdown.py

In a terminal type the following commands

```
chmod +x shutdown.py python shutdown.py &
```

This should make the script run in the background. If you press the button, the Pi should shutdown immediately. You may choose to add a delay by uncommenting the sleep call in the example code. Alternatively, you may also change the GPIO by replacing the appropriate number in the python script.

Cool! Now we can shutdown by pressing a button.

## Add a USB Sound Card

The obvious alternative to the Google AIY Voice Hat is to use any USB Sound Cards that are available from a number of sources. The simplest way is to just plug one in and configure the software to use that instead of the Hat but when there two drivers installed, the python scripts need to be reconfigured to make everything seamless.

Once you plug in the soundcard, the first thing to do is check if it was recognized or not. In the terminal window, type in:

```
aplay - l
```

![](https://hackadaycom.files.wordpress.com/2017/05/aplay-1.png)

'aplay' is used by the scripts to speak out the replies so you should be able to see two sound devices. Note that the onboard sound has been disabled from within the config.txt ([see device tree reference](https://www.raspberrypi.org/documentation/configuration/device-tree.md)) and can be enabled if you plan to use a USB microphone instead of the sound card. The windows output should look like the image below.

I would like to set the USB sound card as the default audio, and for that we need to modify the /etc/asound.conf .

```
sudo nano /etc/asound.conf
```

![](https://hackadaycom.files.wordpress.com/2017/05/asound.png)

Delete the existing content and replace it with text as shown below. Though this sets the default input and output device to the USB device, there is one more step to make things work. (To exit nano, use Ctrl+x, y, return)

Next we edit to audio.py file that handles all the audio playing and recording functionality. For that, open up the file in your favourite text editor; mine is nano:

```
1
sudo nano /home/pi/voice-recognizer-raspi/src/audio.py
```

Scroll down to the part that says 'arecord' which is in the __init__ function. Apparently there is a dedicated process that keeps the recorder running as I will show in the video. For now, we want to edit the arguments so that it uses the USB Card to capture audio instead of the original Voice Hat. A simple modification to use '-D', 'sysdefault:CARD=1' should suffice as shown in the image below.

![](https://hackadaycom.files.wordpress.com/2017/05/record.png)

> _A similar change is require for the aplay function a little further in the code._

![](https://hackadaycom.files.wordpress.com/2017/05/playpy.png)

![](https://hackadaycom.files.wordpress.com/2017/05/button.jpg?w=800&h=378)

With that, the hack is complete! Double click the 'test_audio.py' to check if audio works. We are missing just one part of the puzzle though -- the 'listen' button! So simply wire a push button between GPIO23 and the adjacent ground pin and then run 'src/main.py' to start playing with a DIY Google AIY.

### A Demo

A small video demo of the proposed hack with a USB sound card, external speaker and a cheap microphone.

## An Enclosure

The 3D printed enclosure is designed in Fusion360 and the STL files are part of the GitHub repository. You can use the same enclosure for a number of projects since there are standoffs for the Raspberry Pi and the ports are brought out for convenience. There is a lot of space inside to add hats and additional circuits.

I made the enclosure split from the middle so that it becomes easy to access the GPIOs. The whole thing will press fit including the top cap which has holes for three buttons. I though it would make sense to have smaller buttons since the result is expected to be tougher than cardboard. There is ample space for the speaker should you choose to include one that is slightly different.

I have not had a chance to print one out and will update this page once there is any progress in the topic. Here is the render of the design.

![](https://hackadaycom.files.wordpress.com/2017/05/diy-google-aiy-v4.png)

## Summary

Google has already had their APIs open to the public, but the preconfigured Raspbian image will help a lot of people to get started. I have tried to layout the basics of the sound card as well as give out the plans for an equivalent card if you want to make one. For others the option to use an external sound card is explained and demonstrated and I hope it inspires people to really get into such projects. The world needs more AIY and here is your chance to get started, so what are you waiting for? Get hacking.
