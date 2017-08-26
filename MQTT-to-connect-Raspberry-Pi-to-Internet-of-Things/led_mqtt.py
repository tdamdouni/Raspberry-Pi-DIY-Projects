# Example of using the MQTT client class to subscribe to a feed and print out
# any changes made to the feed.  Edit the variables below to configure the key,
# username, and feed to subscribe to for changes.

# Import standard python modules.
import RPi.GPIO as GPIO

import sys

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

GPIO.setmode(GPIO.BCM)

# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_USERNAME      = 'Your Adafruit IO user name'
ADAFRUIT_IO_KEY           = 'Your Adafruit IO Key'  # See https://accounts.adafruit.com
                                                    # to find your username.

# Set to the ID of the feed to subscribe to for updates.
FEED_ID1 = 'Bulb1'
FEED_ID2 = 'Bulb2'

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.LOW)



# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print 'Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID1)
    print 'Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID2)

     # Subscribe to changes on a feed named DemoFeed.
    client.subscribe(FEED_ID1)
    client.subscribe(FEED_ID2)


def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print 'Disconnected from Adafruit IO!'
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print 'Feed {0} received new value: {1}'.format(feed_id, payload)
    if feed_id=="Bulb1" and payload=="1":
           GPIO.output(23, GPIO.HIGH)
    if feed_id=="Bulb1" and payload=="0":
        GPIO.output(23, GPIO.LOW)
    if feed_id=="Bulb2" and payload=="1":
        GPIO.output(2, GPIO.HIGH)
    if feed_id=="Bulb2" and payload=="0":
        GPIO.output(2, GPIO.LOW)

  

    #print 'Feed {0} received new value: {1}'.format(feed_id, payload)


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Start a message loop that blocks forever waiting for MQTT messages to be
# received.  Note there are other options for running the event loop like doing
# so in a background thread--see the mqtt_client.py example to learn more.
client.loop_blocking()
