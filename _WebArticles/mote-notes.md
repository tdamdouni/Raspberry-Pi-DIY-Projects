Set up a test to see if I can replicate this.

I now have green spots in my vision.

Leaving it off for a minute to see what happens.

And… I can’t seem to replicate your issue. Curious!

However…

Now, for…

The Technical Explanation
Okay. So the APA102 pixels are basically a set of tiny shift registers, each with its own memory. These pixels remember what you told them- so if you say “Be green!” they will happily sit and be green for as long as you like until they’re told to do something else.

Or… if random noise happens to look enough like a signal they might decide to light up or change colour seemingly of their own accord. All they need to assume a signal is valid is a sequence of three 1s 0b111, then the next 5 1s are the brightness, and the following 24 are the colour… so…

If you happen to get any kind of interference close enough to Mote pHAT it’s likely to induce something close to a signal on both the clock and the data line, basically shooting a stream of 1s into the APA102 pixels and making them blindingly 100% on.

This might not be what’s happening in your case, but it’s likely.

The Fix
As you’ve found out for yourself, the best fix is to simply keep the pixels updated. You suggest every 10 seconds, but ideally you’d just have your while loop constantly update them at a sensible framerate that depends on how smooth you want your brightness transitions to be. Not so fast that your Pi’s CPU is eaten entirely by pixel updates, but fast enough to eliminate the chance of random noise causing rogue lighting output.

And this is what you’ll find most things that drive APA102 or WS2812 pixels will do- constantly update the pixels.

Now I normally don’t rush to give out code examples, but I think this is a good opportunity to demonstrate how I’d accomplish this sort of program- paying particular attention to the smoothness and timing of effects and the need to output constant updates to the pixels:

```python
import motephat
import sys
import select
import time

# Note it's conventional to use ALL_CAPS to denote constant values
# that we don't expect the program to ever change during runtime.

# Updates per second
# A higher number consumes more CPU but gives smoother transitions
FPS = 60

# Speed of the transition, higher is faster
# Due to gamma weirdness, turning on always feels faster than turning off
# since most of the high-end brightness steps are the same
# A higher speed will look smoother at higher frame rates
SPEED = 1.0

# The colour to display
RED = 255
GREEN = 110
BLUE = 40

# Internal state
brightness = 0.0
lights_on = False
```

# 2 motes

```python
import time
from colorsys import hsv_to_rgb
from sys import exit

from mote import Mote


try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")


import serial.tools.list_ports
list = serial.tools.list_ports.comports()


#Find the MOTE Hubs!   This machine has 2 installed
var1 = 1
for element in list:
    if 'Mote' in element.description:
        if var1 == 1:
            mote1 = Mote(port_name=element.device)
            var1 = 2
        elif var1 == 2:
            mote2 = Mote(port_name=element.device)
 
#Configure the 16 LED's, clear channels on both hubs
mote1.configure_channel(1, 16, False)
mote1.configure_channel(2, 16, False)
mote1.configure_channel(3, 16, False)
mote1.configure_channel(4, 16, False)

mote2.configure_channel(1, 16, False)
mote2.configure_channel(2, 16, False)
mote2.configure_channel(3, 16, False)
mote2.configure_channel(4, 16, False)


mote1.clear()
mote2.clear()

try:
    while True:
        r = requests.get('http://api.thingspeak.com/channels/1417/feed.json')
        j = r.json()
        f = j['feeds'][-8:]

        f = [element for index, element in enumerate(f) if index%2==0]

        print(f)

        channel = 1
        for col in f:
            col = col['field2']
            ## Older versions of Python may need this line
            ##r, g, b = tuple(ord(c) for c in col[1:].lower().decode('hex'))
            r, g, b = tuple(c for c in bytes.fromhex(col[1:]))
            for pixel in range(mote1.get_pixel_count(channel)):
                mote1.set_pixel(channel, pixel, r, g, b)
                mote2.set_pixel(channel, pixel, r, g, b)
            channel += 1        

        mote1.show()
        mote2.show()

        time.sleep(5)

except KeyboardInterrupt:
    mote1.clear()
    mote2.clear()
    
    mote1.show()
    mote2.show()
    time.sleep(0.1)
```

# extension for using more than one mote controller 
_https://forums.pimoroni.com/t/2-mote-hubs-1-pi/7427/9_

Nice work! I might have made it extensible to any number of motes and approached it like:

motes = []

for port in serial.tools.list_ports.comports():
    if 'Mote' in comport.description:
        motes.append(Mote(port_name=comport.device))

motes[0]...

motes[1]...
You can do it with list comprehension, but that’s generally an ugly unreadable mess:

motes = [Mote(port_name=comport.device for comport in serial.tools.list_ports.comports() if 'Mote' in comport.description]
This lets you do bulk updates too:

for mote in motes:
    mote.set_pixel(channel, pixel, r, g, b)
    mote.show()