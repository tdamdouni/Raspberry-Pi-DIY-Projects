#!/usr/bin/env python

# https://forums.pimoroni.com/t/bitcoin-value-ticker-for-scroll-phat-hd/6319

import time
import signal
import unicodedata
import scrollphathd
from scrollphathd.fonts import font5x5

from time import sleep
import json
#import requests, json
import urllib

# choose currencies to display
currencies = ['btcusd']


#Uncomment to rotate the text
#scrollphathd.rotate(180)


while True:
    string = ''

    for currency in currencies:

        url = 'https://www.bitstamp.net/api/v2/ticker/%s/' % currency
        #print(url)
        data = json.load(urllib.urlopen(url))

        string += '%s' % data['last'] + '   '

    for i in range(10):
        scrollphathd.clear()
        #print(string)
        buffer = scrollphathd.write_string(string, x=17, y=0, font=font5x5, brightness=0.2, monospaced=False)
        for c in range(buffer):
            scrollphathd.show()
            scrollphathd.scroll(1)
            time.sleep(0.05)

    sleep(10)
