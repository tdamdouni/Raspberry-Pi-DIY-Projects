#!/usr/bin/env python

# based on https://github.com/adafruit/io-client-python/blob/master/examples/mqtt_client.py

import io
import time

# Camera setup guide: https://learn.adafruit.com/cloud-cam-connected-raspberry-pi-security-camera/pi-camera-setup
import picamera
import base64
import sys

# Installing the Python Imaging Library on a Raspberry Pi 3
#
# $ sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
# $ sudo pip install pillow
#
from PIL import Image

# Import Adafruit IO MQTT client. Install with:
#
# $ sudo pip install adafruit-io
#
from Adafruit_IO import MQTTClient

IO_USERNAME="[REDACTED]"
IO_KEY="[REDACTED]"

camera = picamera.PiCamera()
camera.resolution = (640, 480)

# Start a preview and let the camera warm up for 2 seconds
camera.start_preview()
time.sleep(2)

def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print 'Connected to Adafruit IO!  Listening for /click changes...'

    # Subscribe to changes on a feed with key, 'click'. This will tell the
    # camera when to snap a pic
    client.subscribe('click')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print 'Disconnected from Adafruit IO!'
    time.sleep(10)
    start()

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print 'Feed {0} received new value: {1}'.format(feed_id, payload)

    if payload == '1':
        send_image(camera, client)

def send_image(camera, client):
    # Take a photo, optimize it with PIL, and publish it to Adafruit IO.
    stream = io.BytesIO()

    print('> capturing')

    # Tweak point 1: if your data size is too big, try reducing the original
    # dimensions here.
    camera.capture(stream, format='jpeg', resize=(800, 600))
    stream.seek(0)

    print('> optimizing')
    image = Image.open(stream, 'r')
    optim_stream = io.BytesIO()

    # Tweak point 2: if your data size is too big, try reducing the quality
    # here. 85 is a good middle ground, but lower will still produce
    # recognizable images.
    image.save(optim_stream, format='jpeg', quality=85, optimize=True)
    optim_stream.seek(0)

    print('> converting')
    value = base64.b64encode(optim_stream.read())

    if len(value) > 102400:
        print "image is too big!"
        print "  got %i bytes" % len(value)
        client.publish('actions', 'image too big')
        time.sleep(2)
        return

    print 'Publishing {0}... {1} bytes to image-stream.'.format(value[0:32], len(value))

    # the actual moment of publishing, this is where the image feed key is set
    client.publish('image-stream', value)

    # Publish to a second feed with notification that the image has been sent.
    # Not necessary, but can be helpful for debugging.
    client.publish('actions', 'image sent, {} bytes'.format(len(value)))

###

def start():
    # Create an MQTT client instance.
    client = MQTTClient(IO_USERNAME, IO_KEY)

    # Setup the callback functions defined above.
    client.on_connect    = connected
    client.on_disconnect = disconnected
    client.on_message    = message

    # Connect to the Adafruit IO server.
    client.connect()

    # Now the program needs to use a client loop function to ensure messages
    # are sent and received. This command will block foreground processing and
    # let the MQTT library do its work.
    client.loop_blocking()

if __name__ == '__main__':
    start()

