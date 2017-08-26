#!/usr/bin/env python
#Thanks To campag for concept/code.
#Written by alexmburns.

from __future__ import print_function
import subprocess
import sys
import time

try:
    import feedparser
except ImportError:
    sys.exit("You need to install feedparser with: sudo pip install feedparser") 

import scrollphathd

scrollphathd.set_brightness(0.5)

# Every refresh_interval seconds we'll refresh the news data, currently set to 30mins.
pause = 0.12
ticks_per_second = 1/pause
refresh_interval = 60*30

print("My RSS Feed") #Change Text as appropriate.

url = "http://feeds.feedburner.com/InterestingThingOfTheDay" #Insert your choice of RSS feed here.

def get_timeout():
    return ticks_per_second * refresh_interval

def get_data():
# Get the data from rss feed
    d = feedparser.parse(url)
    entries = int(len(d['entries']))
    val = "        " + d['entries'][0]['title']
    val +="        " + d['entries'][1]['title']
    val +="        " + d['entries'][2]['title']
    return val

timeout = get_timeout()
count = 0
msg = get_data()
scrollphathd.write_string(msg)

while True:
    try:
	scrollphathd.show()
        scrollphathd.scroll()
        time.sleep(0.05)

        if(count > timeout):
            msg = get_data()
            scrollphathd.write_string(msg)
            timeout = get_timeout()
            count = 0
        else:
            count = count+ 1
    except KeyboardInterrupt:
        scrollphathd.clear()
        sys.exit(-1)
