# https://forums.pimoroni.com/t/2-mote-hubs-1-pi/7427/8

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

