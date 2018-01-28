# Pimoroni HyperPixel

_Captured: 2017-11-07 at 18:22 from [orbitalfruit.blogspot.de](http://orbitalfruit.blogspot.de/2017/06/pimoroni-hyperpixel.html?m=1)_

##  Something to Compare

![](https://3.bp.blogspot.com/-9S5FziOgonI/WUBjFgIImKI/AAAAAAAAAQg/vx5_cysGTXM9ZZ6HUrEgnvWbcaaYmYPoQCLcBGAs/s280/hyperpixel.jpg)

> _HyperPixel 800x480_

At the end of the day these screens are likely to be embedded (for me that I means glued) into most projects. The 7in official screen is available, but I feel it's just a bit too big for embedding and too small for development.

The HyperPixel fits in-between the cheap and expensive touchscreens. At the cheap end screens are [resistive touch](https://en.wikipedia.org/wiki/Resistive_touchscreen) where as the top end are [capacitive touch](https://en.wikipedia.org/wiki/Capacitive_sensing). A stylus is usually required for accurate touch on a resistive screen, although a finger nail can be an good enough substitute. Capacitive touch will pick up from a finger tip without much pressure on the screen.  
The HyperPixel is a capacitive touch screen whereas the XPT2046 uses resistive. In my opinion each have their pros and cons. Resistive is good for single screen clicks but a bit poor for dragging and dropping type actions. Capacitive won't work through gloves or with a stylus (unless conductive), but is better for swiping and dragging.

##  HyperPixel

![](https://1.bp.blogspot.com/-PB3Ze15d_EA/WUBjGifDDYI/AAAAAAAAAQo/HSmMsYV8SJwf1aBgTQ7t5ELXU9OjW-newCEwYBhgL/s280/pixelhp.jpg)

Setup of the HyperPixel is really straight forward. It's a single command install provided by Pimoroni. There are detailed instructions for manual installation if you like to know what's going on.

I ran the simple one on a fresh Jessie install and it worked straight after reboot. Happy days compared to the XPT2046.

Booting up to the desktop presents a really clear display with excellent viewing angles. I need to tilt the XPT2046 to see it clearly, whereas this is clear at all angles.

The screen fits in my [Short Crust Plus](http://shortcrust.net/short-crust-plus/) case very neatly, but the lid or other extenders will not fit as the screen is in the way.

Touch detection is accurate and works to the edges reliably which is also a plus against the cheaper XPT2046 which just doesn't like the edges.

In the packaging there is a nylon thread which is to support one side of the screen. I found this to be too long for use with a bare Pi 3 board and too short when used with a Pimoroni coupe case. There may be a bit of DIY to cut this down to size. The screen sits neatly on the USB ports so the support isn't really necessary.

![](https://3.bp.blogspot.com/-uPCogORlmp4/WUBjGwBTTcI/AAAAAAAAAQw/3mlX_jM9QjY89vKjpd2ZEYZfRADnMwwqACEwYBhgL/s280/support.jpg)

> _Nylon Thread Support_

The Pixel desktop isn't a touchscreen friendly environment and the small icons are a pain to access on the small 3.5'' display. You will see that I have a wireless keyboard and mouse attached and this is necessary for both screens to setup the software and quickly navigate in a browser. What this screen, and other small touchscreens need is a window manager like Android to really work with just touch.

The HyperPixel screen connects using the [DPI ](https://www.raspberrypi.org/documentation/hardware/raspberrypi/dpi/README.md)parallel display interface. This means that you lose the SPI and I2C capability. There are still free GPIO pins available but the ability to interface with these isn't straight forward when the screen is attached. Some research is needed to discover the available pins. In comparison the XPT2046 avoids this by connecting to the HDMI and keeping a lot of pins free for other components.

##  XPT2046 5'' Display

![](https://1.bp.blogspot.com/-v-aiAd7tnIo/WUBjGFkg__I/AAAAAAAAAQk/JQviBmFoVL0aQ9cZ-ehya5zjTKlshyW9QCEwYBhgL/s280/desktopxpt.jpg)

This screen is the cheaper choice and at 5'' gives a bit more for your money. The viewing angle is poor and even a slight tilt reduces colour contrast. Colours are not as bright as the HyperPixel. On a plus point the bigger screen is better on the old eyesight for reading text.

Out of the box the screen is a bit fiddly to setup. A disc of instructions are provided and clear enough to step through with a bit of patience. It works with the latest Jessie install quite happily. A bit of tweaking is needed in config.txt to prevent to the overscan at the bottom of the screen.

As the screen connects up to the HDMI it refreshes as well as the HyperPixel. Touch response isn't as good and the accuracy is poor near the edges. Mouse and keyboard are still needed to manage Pixel.

Once connected the 40 pin header still has a lot of free pins to play with. Only the SPI and 2 GPIO pins are used. The screen actually only connects to 26 pins allowing jumper wires to squeeze in.

The screen also has a pass through for all 26 pins allowing another header to be attached to the back of the screen.

##  What Does This Mean?

HyperPixel is a good high quality screen. If you want mobile phone quality then this is the one.

Both screens are useless in my opinion for Pixel desktop. This isn't the fault of the screens and is more to do with Pixel being designed for mouse and keyboard.

If you are coding up your own interfaces, for example in Pygame, then you can cater for the touchscreen inputs and have a great experience. This should open the doors to cool custom applications and games on the Pi.

Directly these screens are hard to compare. They are for different purposes and it will depend on what they will be running.

Overall the XPT2046 screen is better for people who want to add extra hardware and run a display. Attaching I2C devices or running stuff off the GPIO pins is much easier than the HyperPixel.

HyperPixel appears to be for applications which need a clear screen and capacitive touch at a decent price.

###  Virtual Keyboard Setup

![](https://4.bp.blogspot.com/-FX9L13at0AI/WUBjHv_5tAI/AAAAAAAAAQ0/umdNs7kKdcQAe_n1NflykqzCIzpDp3zEgCEwYBhgL/s280/xvkbd-hp.jpg)

> _XVKBD on the HyperPixel_

If you are determined to use the touchscreen then I'd recommend XVKBD

> sudo apt-get install xvkbd

Run the keyboard from the command line with

![](https://2.bp.blogspot.com/-yqRn3PDaGLo/WUBjGxDXlXI/AAAAAAAAAQs/rzq_lR4HuBMwr2ICr7QwpdldVd6dXLScwCEwYBhgL/s280/matchboxxpt.jpg)

> _Matchbox on the XPT2046_

Another keyboard is Matchbox

> sudo apt-get install matchbox-keyboard

Run matchbox from the command line with

> matchbox-keyboard &

Both keyboards work well, but the xvkbd has slightly larger buttons and is a bit easier to read and touch first time. Both are a bit clunky to use and will need scripting into the start up scripts to load automatically.

Modmypi has a quick post about [Matchbox setup](https://www.modmypi.com/blog/matchbox-keyboard-raspberry-pi-touchscreen-keyboard), but the principles are the same for xvkbd desktop icon setup as well.
