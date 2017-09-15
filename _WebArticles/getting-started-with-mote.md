# Getting Started with Mote

_Captured: 2017-08-30 at 09:40 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-mote)_

This tutorial will show you how to install the [Mote Python library](https://github.com/pimoroni/mote), and then walk through its functionality, finishing with an example of how to use Mote with Cheerlights.

![mote-6.jpg](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-6.jpg)

## Installing the software

### Raspberry Pi (Raspbian)

We always recommend using the most up-to-date version of Raspbian, as this is what we test our boards and software against, and it often helps to start with a completely fresh install of Raspbian, although this isn't necessary.

As with most of our boards, we've created a really quick and easy one-line-installer to get your Mote set up. We'd suggest that you use this method to install the Mote software.

Open a new terminal, and type the following, making sure to type 'y' or 'n' when prompted:
    
    
    curl https://get.pimoroni.com/mote | bash
    

Once that's done, it probably a good idea to reboot your Pi to let the changes propagate.

### Mac or Linux (flavours other than Raspbian)

On Mac or Linux, to install the Mote Python library with pip, open a terminal and type the following:
    
    
    sudo pip install mote
    

That should install the Mote library. Alternatively, if you want to clone the Mote GitHub repo, including all of the examples, then open a terminal and type the following:
    
    
    git clone https://github.com/pimoroni/mote
    cd mote/python/library
    sudo python setup.py install
    

### Windows

If you've installed [Python for Windows](https://www.python.org/downloads/windows/), then it comes with the pip installer, and you should be able to use it to install the Mote Python library. Open a command prompt and type:
    
    
    pip install mote
    

## Connecting Mote

If you've got the Mote kit, then you'll have four of the Mote strips, a controller, four Mote cables (the black ones with micro-B connectors), and a USB cable (the red one, USB A to micro-B).

The Mote cables are used to connect the Mote strips to the controller board. Plug either end of the cable into the micro-B connector on a Mote strip, and the other end into one of the four numbered ports on the Mote controller board. Do this for all four strips (assuming you want to use all four).

![mote-3.jpg](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-3.jpg)

> _The red USB cable plugs into the port on the controller marked with the USB symbol (the micro-B end of the cable). Plug the other end of the USB cable (the larger A connector) into a free USB port on your computer._

![mote-2.jpg](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-2.jpg)

The remaining port on the controller, marked with the lightning bolt power symbol, can be used to supply extra power to the Mote strips provided by a micro-USB power supply, to take them to full brightness. You can safely plug this additional power supply in and out while your Mote strips are connected and running quite safely.

## Lighting pixels

In terms of functionality, the Mote library works very similarly to our Blinkt! Python library. However, instead of just 8 pixels on Blinkt!, Mote has up to 4 x 16 pixels per controller. So, the `set_pixel` method for Mote, takes an additional argument that specifies which channel (and hence strip) to act on.

Before we get to the `set_pixel` method, we need to import the `Mote` class, create an instance of the class on which to work, and set up the 4 channels. Let's do that now.
    
    
    from mote import Mote
    
    mote = Mote()
    
    mote.configure_channel(1, 16, False)
    mote.configure_channel(2, 16, False)
    mote.configure_channel(3, 16, False)
    mote.configure_channel(4, 16, False)
    

`mote.configure_channel` takes three arguments - a channel from 1 to 4, the number of pixels on that channel, and a `True` or `False` that specifies whether to enable gamma correction or not. We're assuming here that you're using four of the sixteen pixel strips but, if not, you can modify the code accordingly for the number of strips and pixels per strip you have.

To start, we're going to light the first pixel of the first strip red. The `set_pixel` method takes five arguments - the strip number, pixel number, and the red, green and blue values (from 0-255). In RGB, red is represented as 255, 0, 0.
    
    
    mote.clear()
    mote.set_pixel(1, 0, 255, 0, 0)
    mote.show()
    

![mote-4.jpg](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-4.jpg)

You'll notice that we also called `mote.clear()` before we set the pixel, just in case there were any pixels already set. It's also worth noting that the strips are numbered from 1 to 4, but the pixels on each strip are indexed from 0 and hence numbered from 0 to 15. After setting a pixel or pixels, you have to call `mote.show()` to actually display the set pixels on the Mote strips.

Next, we'll light all of the pixels on all four strips blue. To do this, we'll use two `for` loops, that will first loop through each strip, and then through each pixel on each strip, setting each one in turn.
    
    
    mote.clear()
    for channel in range(1, 5):
        for pixel in range(16):
            mote.set_pixel(channel, pixel, 0, 0, 255)
    mote.show()
    

![mote-5.jpg](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-5.jpg)

Notice that we're using `range(1, 5)` for the `channel`, since we want the numbers 1 to 4 (ranges in Python go up to, but do not include the second number), but we're using `range(16)` for the `pixel` since the 0 is implicit when only a single number is passed to `range`.

Now that we know how to light individual pixels and iterate through all of the pixels, we'll look at how to do some basic animations.

## Basic animations

By rejigging our code that we used in the previous section to light all of the pixels, we can create a simple animation that fills up all of the pixels on the strips one at a time.
    
    
    import time
    
    while True:
        mote.clear()
        for channel in range(1, 5):
            for pixel in range(16):
                mote.set_pixel(channel, pixel, 0, 0, 255)
                mote.show()
                time.sleep(0.05)
    

We need to import an additional library, the `time` library, that allows us to add a small delay to our animation (the last line that reads `time.sleep(0.05)`). The only other changes we'll make are to wrap the whole thing in a `while True` loop to keep it running continuously, and move the `mote.show()` into the innermost `for` loop so that the Mote strips update after each pixel is lit.

To change this animation so that a single pixel scans across all of the strips, all we have to do is to move the `mote.clear()` to the start of the `for` loop where the pixels are lit, meaning that any existing pixels that are lit will be cleared before a new one is lit.
    
    
    import time
    
    while True:
        for channel in range(1, 5):
            for pixel in range(16):
                mote.clear()
                mote.set_pixel(channel, pixel, 0, 0, 255)
                mote.show()
                time.sleep(0.05)
    

## Cheerlights

Cheerlights is a really simple web service that allows anyone to change the colour that is currently set, from a range of about a dozen different colours, by tweeting `@cheerlights green`, for example, or `#cheerlights green`. By pulling the currently set colour from the Cheerlights API, every so often, we can use that to change the colour of our Mote strips.

We'll go through the code bit by bit, and explain it along the way.
    
    
    import requests
    import time
    from mote import Mote
    
    mote = Mote()
    
    mote.configure_channel(1, 16, False)
    mote.configure_channel(2, 16, False)
    mote.configure_channel(3, 16, False)
    mote.configure_channel(4, 16, False)
    

Most of this code looks similar to the code that we ran at the very beginning of the tutorial, to set up the Mote strips. We've additionally imported the `requests` library, that we'll use to query the Cheerlights API.

Before the main `while` loop that will run our code, we'll clear the Mote strips by calling `mote.clear()` and then `mote.show()`.
    
    
    mote.clear()
    mote.show()
    

And here's the `while True` loop that will run every second, query the Cheerlights API, and then update our Mote strips accordingly.
    
    
    while True:
        r = requests.get('http://api.thingspeak.com/channels/1417/field/2/last.json')
        col = r.json()['field2']
        r, g, b = tuple(ord(c) for c in col[1:].lower().decode('hex'))
        for channel in range(1, 5):
            for pixel in range(16):
                mote.set_pixel(channel, pixel, r, g, b)
        mote.show()
        time.sleep(1)
    

We're using the `requests` library to send a GET request to the Cheerlights API: `r = requests.get('http://api.thingspeak.com/channels/1417/field/2/last.json')`. If we look at the JSON returned by that request, we see something that looks like the following.
    
    
    {"created_at":"2016-09-06T17:31:02Z","entry_id":127729,"field2":"#800080"}
    

If you don't already have the `requests` library installed, you can install it by typing the following in the terminal.
    
    
    sudo pip install requests
    

`field2` is the colour, in this case `#800080`, which is purple. In the next line, we use the `.json()` method of our returned request `r` to then pull out `['field2']` with the hex colour value.

Because the `set_pixel` method accepts RGB values, and we have a hex value, we'll use a bit of slightly clunky tuple interpretation to convert hex to unpacked `r`, `g`, and `b` values all in one line.
    
    
    r, g, b = tuple(ord(c) for c in col[1:].lower().decode('hex'))
    

And then it's just a matter of looping through the channels and pixels, as we did previously, setting the pixels, and then calling `mote.show()`, with a second delay so that we don't hit their API with too many requests.
    
    
    for channel in range(1, 5):
        for pixel in range(16):
            mote.set_pixel(channel, pixel, r, g, b)
    

Here's the entire code that you can save in a file called `mote_cheerlights.py`, or some such, and then run in the terminal.
    
    
    import requests
    import time
    from mote import Mote
    
    mote = Mote()
    
    mote.configure_channel(1, 16, False)
    mote.configure_channel(2, 16, False)
    mote.configure_channel(3, 16, False)
    mote.configure_channel(4, 16, False)
    
    mote.clear()
    mote.show()
    
    while True:
        r = requests.get('http://api.thingspeak.com/channels/1417/field/2/last.json')
        col = r.json()['field2']
        r, g, b = tuple(ord(c) for c in col[1:].lower().decode('hex'))
        for channel in range(1, 5):
            for pixel in range(16):
                mote.set_pixel(channel, pixel, r, g, b)
        mote.show()
        time.sleep(1)
    

## Taking it further

We've designed Mote to work really well as a decorative light for under-shelf, or under-cabinet lighting, and we've also written a really neat (if quite lengthy) [tutorial](http://learn.pimoroni.com/tutorial/sandyj/using-mote-with-homekit-and-siri) about how to control Mote with Homekit and Siri (for voice control) on the iPhone.

Why not combine Mote with an Enviro pHAT or the Flotilla Light module, and use it to turn Mote on automatically when it gets dark? Or you could use Display-O-Tron HAT as an all-singing all-dancing controller for Mote!

Our Mote strips also fit perfectly in IKEA's Kallax shelving units, and we'll have a tutorial and mounting template very soon to show you how to do it.
