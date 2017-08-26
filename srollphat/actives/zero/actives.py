#!/usr/bin/python

import scrollphat
import requests
import time

brightness = 2 # Scroll pHAT brightness 1-100
updatePeriod = 5 # Update every in seconds
server = "http://davidmaitland.me:7070" # URL for server
apiKey = "AWTVLL76ZY8YOW50" # Replace with your own key (Must be the same one as in the Node.js code!)

last = 0 # Used for keeping track (Don't change this)

def status(status):

    scrollphat.set_pixel(10,4,status)
    scrollphat.update()

def update(count):

    global last

    scrollphat.set_pixel(10,4,0)

    if count == None:

        scrollphat.clear()
        scrollphat.write_string("----")

    else:

        if count != last:

            scrollphat.clear()
            scrollphat.write_string(str(count))

            last = count

def process():

    try:

        params = {"key": apiKey}
        r = requests.get(server, params=params, timeout=5)
        count = int(r.text)
        update(count)

    except:

        status(1)
        #update(None)


if __name__ == "__main__":

    scrollphat.set_brightness(brightness)
    scrollphat.write_string("0")

    while True:

        process()
        time.sleep(updatePeriod)
