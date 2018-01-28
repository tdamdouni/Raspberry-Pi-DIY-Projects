# How to connect and control a Raspberry Pi WS2801 RGB LED Strip

_Captured: 2017-10-27 at 19:03 from [tutorials-raspberrypi.com](https://tutorials-raspberrypi.com/how-to-control-a-raspberry-pi-ws2801-rgb-led-strip/)_

![Raspberry Pi WS2801B RGB LED Streifen anschließen und steuern](https://tutorials-raspberrypi.com/wp-content/uploads/2016/11/Raspberry-Pi-WS2801B-RGB-LED-Streifen-anschließen-und-steuern.jpg)

One of the many Raspberry Pi projects is the lighting of rooms or objects. LED strips are particularly suitable for this purpose, because many individual LEDs are aligned and each individual LED can display all RGB colors. Thus, some projects such as room lighting, Ambilight or e.g. a Christmas tree lighting can be realized. The effects of the colorful lights are impressive.

This article shows the general usage of the WS2801B on the Raspberry Pi. In doing so, we create an example in which LEDs of the strip are set (rainbow colors) and the brightness is dimmed. In the video at the end of the tutorial you can see the whole thing in action.

## Equipment

The RGB LED strips require an input voltage of 5V. The most favorable variant with 32 LEDs per meter has a distance between the LEDs of only 2.5 cm:

  * WS2801B LED strip with 32 LEDs per meter ([US](https://www.amazon.com/s/ref=nb_sb_noss_2?tag=754u-20&url=search-alias%3Daps&field-keywords=WS2801+RGB+32+LED) / [UK](https://www.amazon.co.uk/s/ref=nb_sb_noss/?tag=755-21&url=search-alias%3Daps&field-keywords=WS2801+RGB+32+LED))

There are also versions available that are dust and water-resistant (IP67). Each of the individual LEDs has a current consumption of about 60 mA. At one meter this is almost 2A. This is quite more than the GPIOs of Raspberry Pi can deliver. We therefore need an external current source that supplies power to the RGB stripe. Depending on how long your strip is, the maximum current must be higher. The power supply should therefore be able to supply 10A at 5 meters.  
You have the choice between two possibilities:

![DC Steckeradapter](https://tutorials-raspberrypi.com/wp-content/uploads/2016/10/DC-Steckeradapter-CCTV.jpg)

> _With a plug adapter and power supply, the plus and minus poles can be easily connected to the LED strips._

  * For beginners: Power adapter ([US](https://www.amazon.com/s/ref=nb_sb_noss_2?tag=754u-20&url=search-alias%3Daps&field-keywords=AC+DCAdapter+5V+10A) / [UK](https://www.amazon.co.uk/s/ref=nb_sb_noss/?tag=755-21&url=search-alias%3Daps&field-keywords=AC+DCAdapter+5V+10A)) + plug-in connector ([US](https://www.amazon.com/s/ref=nb_sb_noss_2?tag=754u-20&url=search-alias%3Daps&field-keywords=DC+power+jack+male+female+cctv) / [UK](https://www.amazon.co.uk/s/ref=nb_sb_noss/?tag=755-21&url=search-alias%3Daps&field-keywords=DC+power+jack+male+female+cctv)) (c.f. picture on the right)

The difference is that a power cable has to be disconnected and then connected to the switching power supply. Since working with high voltage is dangerous, this is not recommended for beginners. For a power supply (similar to the laptop chargers) you only need an additional Power Jack adapter, so that you can detach the two voltage poles.

Last but not least jumper cables and a breadboard ([US](http://www.ebay.com/sch/i.html?_nkw=breadboard&_sacat=0) | [UK](http://www.ebay.co.uk/sch/i.html?_nkw=breadboard&_sacat=0)) are required.

#### WS2801B vs. WS2812B

The WS2812 LED strips are often found on the Internet, which are also somewhat cheaper than the WS2801 models. However, these are not all too good for the Raspberry Pi, since the onboard audio output of the Raspberry Pi can not be used anymore. However, I will write another tutorialon how to use the WS2812 LED strips.

WS2801B strips have two data lines (data and clock), whereby individual LEDs can be addressed via the integrated SPI bus of the Raspberry Pi. This is different for the WS2812B models. These strips have only a single data pin, which is why before sending a lot more has to be calculated. For this reason the **WS2801B** RGB LED strips are preferable to the WS2812 for use on the Raspberry Pi, despite their supposedly smaller "serial number".

## Connect the switching power supply to the WS2801

Before we start, we have to connect the current source (only for the plug-in power supply). If you have selected the first variant - a charger-like power supply - you can jump to the next point. You only need to clamp the plug adapter to the power supply and loosen the screws.

![Netzkabel für Raspberry Pi WS2801](https://tutorials-raspberrypi.de/wp-content/uploads/Netzkabel-für-Raspberry-Pi-WS2801-180x142.jpg)

> _Ensure that the power cord is compatible with 10A._

First of all: Working with 230V voltage can be deadly! While you make changes, all connections to the socket must be disconnected! Be careful and only work with it if you are sure of your cause. If this is not the case, I recommend the first power supply.

We start by cutting the power cord (e.g. old PC power cable). There are two or three cables inside. These must be carefully separated by about 1cm from the insulation, so that only the wire is visible in the cables. The switching power supply has three connections on the left side. On the one hand, "L" (phase / outer conductor) and "N" (neutral conductor), which are marked with AC (alternating current) and a [grounding symbol](https://en.wikipedia.org/wiki/Ground_\(electricity\)#Electronics). If your cable only contains two smaller cables, they will be connected to the AC connectors. If there are three, you must also identify the earth cable and connect it to the earthing symbol / "PE" connector.

Since the colors of the inner cables differ with older power cables, here is a brief overview, what color comes:

  * The **black** or **brown** cable comes to the outer conductor "**L**".
  * The **blue** cable is connected to the neutral conductor "**N**".
  * The **green-yellow** cable is connected to the protective conductor "**PE**" or **grounding symbol**.
![Aufgeschnittenes Netzkabel mit abgetrennter Isolation](https://tutorials-raspberrypi.de/wp-content/uploads/Aufgeschnittenes-Netzkabel-mit-abgetrennter-Isolation-600x275.jpg)

> _Cut-out two-core power cable with separated insulation._

For connecting the cables, the screws of the power supply must be loosened. Then place the wires under the screws. Make sure that they are well screwed and that the cables can not come loose. Normally, these devices still have a small protective flap, so that you don't touch them accidentally. If you want to be safe, you can also wrap insulation tape around the sensitive spots.

On the other side, there are outgoing 5V voltage (+V) and the ground connections (-V or COM). As a test, you can use a Multimeter to measure the voltage as shown here:

![Multimeter am Schaltnetzteil des WS2801 LED Strip](https://tutorials-raspberrypi.de/wp-content/uploads/Multimeter-am-Schaltnetzteil-des-WS2801-LED-Strip-339x500.jpg)

> _The output voltage of the switching power supply should be about 5V._

## Wiring between Raspberry Pi, WS2801 and current source

Normally, the LED strips come with soldered plugs, which are intended for connecting several WS2801 strips. In addition, there is usually also a plug, which can be put on a Breadboard (4 connected cables). Furthermore, two additional cables for the external power connection from the LED Strip (red and black) are often used.

Since the color of the cable does not necessarily correspond to the standards, you should pay attention exactly which cable leads to which connection on the strip. Incorrect wiring on the Raspberry Pi could result in overheating or a short-circuit.

![WS2801 RGB LED Streifen](https://tutorials-raspberrypi.de/wp-content/uploads/WS2801-RGB-LED-Streifen-500x500.jpg)

> _The LEDs on one meter are numbered (1 - 32). The WS2801 RGB LED strip has 2 data pins (here: CK and SI) as well as the 5V connector and GND._

If you are aware of which cable leads to which connection, we can connect it. The Raspberry Pi should be switched off and the switching power supply should not be connected to the socket. The cables are connected as follows:

WS2801 LED Stripe Raspberry Pi (Switching-) Power Supply

5V
--
+V

CK / CI
Pin 23 (SCKL)
--

SI / DI
Pin 19 (MOSI)
--

GND
Pin 6 (GND)
-V or COM

For the connection to the switching power supply you can also use the two additional cables (if available). It is important that GND / ground is connected to both the Raspberry Pi **and** the external power supply. The structure now looks as follows:

![Raspberry Pi WS2801B RGB LED Stripe Schaltplatine](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2801B-RGB-LED-Stripe-Schaltplatine-600x296.png)

## Installing the Raspberry Pi WS2801 RGB LED Library

To control the LED strip we use a Python library from [Adafruit](https://github.com/adafruit/Adafruit_Python_WS2801/blob/master/Adafruit_WS2801/WS2801.py). This special Raspberry Pi WS2801 library includes some functions for controlling the individual LEDs. The good thing is that each LED can be addressed individually and any [RGB color](https://en.wikipedia.org/wiki/RGB_color_space) is possible.

The library requires the SPI bus, which we have to activate (if not already done). We call the following:
    
    
    sudo raspi-config

Under "Advanced Option" there is a point for "SPI". We enable it and exit the configuration menu.

The installation now works quite simply via the Python package manager from the normal console / terminal. Preventively, we are first updating the package sources and installing PIP (this is not included on the Raspbian Lite versions by default):
    
    
    sudo apt-get update
    sudo apt-get install python-pip -y
    sudo pip install adafruit-ws2801

![Raspberry Pi WS2801B Weihnachtsbaumbeleuchtung](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2801B-Weihnachtsbaumbeleuchtung-120x180.jpg)

> _Christmas tree lighting with the WS2801._

If you have a lite version or SpiDev is not installed on your system, please follow [this guide](http://tightdev.net/SpiDev_Doc.pdf) to install and activate it. On newer Raspbian versions, however, it should already be pre-installed.

Since the given example of the developers apparently does not work on all (fresh) Raspbian versions, I have changed that and expanded.

## Sample code for brightness dimming of the WS2801 LEDs

The following example can be used and extended for your own projects. Here, a few colors (rainbows) are first switched in series, whereupon the brightness of the individual colors is dimmed. For this, it must be said that the brightness of a color can also be defined with the RGB value (see [RGB Color Picker](http://www.w3schools.com/colors/colors_picker.asp) for this).

So let's create a file:
    
    
    sudo nano ws2801_example.py

The following content should be inserted:

In line 11 you have to specify the number of LEDs that are on the connected strip. This should be 32 meters. You can save the file with CTRL + O and close the editor with CTRL + X.

Here is the promised video with the different effects from the file:

I would be interested in what projects do you plan to do (Advent lighting, Christmas tree decoration, spice up rooms, "Infinite Mirror Table", etc.)? Are there any requests for specific tutorials related to the Raspberry Pi WS2801B controller? I already have some ideas, but would also like to hear your opinion
