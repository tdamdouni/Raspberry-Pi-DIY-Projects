# Raspberry Pi Physical Dashboard & Adafruit IO Example
# Author: Tony DiCola
# License: Public domain
#
# This example will display three feeds from Adafruit IO on a dashboard.  The
# feeds are:
#  - pi-dashboard-slider: Will display a slider with values from 0-100 on a
#                         dashboard 7-segment display called 'slider'.
#  - pi-dashboard-humidity:  Humidity sensor feed displayed on a 7-segment display
#                            called 'humidity'.
#  - pi-dashboard-temp: Temperature sensor feed displayed on a 7-segment display
#                       called 'temp'.
#
# To modify this example to use your own feeds you'll want to change the following
# code:
#  - connected function: Add a client.subscribe() call for each feed you want to
#                        display on the dashboard.
#  - message function:  Add an if/elif check to check for each feed you want
#                       to display and have it make an HTTP POST against the
#                       dashboard using the feed payload as a value.
#  - DASHBOARD_URL variable: Change this to the URL of your Pi dashboard if you
#                            aren't running this script on the same Pi as the
#                            dashboard (otherwise keep it the same localhost:5000
#                            value).  Make sure NOT to end this with a slash!
#
# Be sure to modify the ADAFRUIT_IO_KEY and ADAFRUIT_IO_USERNAME variables to
# set your AIO key and username!

# Import standard python modules.
import random
import sys
import time

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

# Import requests library used for making HTTP calls to the dashboard server.
import requests


# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = 'YOUR ADAFRUIT IO KEY'       # Set to your Adafruit IO key.
ADAFRUIT_IO_USERNAME = 'YOUR ADAFRUIT IO USERNAME'  # See https://accounts.adafruit.com
                                                    # to find your username.
# Set the URL of the physical dashboard to use.  If running on the same Pi as
# the dashboard server then keep this the default localhost:5000 value.  If
# modified make sure not to end in a slash!
DASHBOARD_URL = 'http://localhost:5000'  # URL of the physical dashboard.
                                         # Don't end with a slash!


# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print 'Connected to Adafruit IO!  Listening for feed changes...'
    # Subscribe to the three pi-dashboard feeds that will be displayed on the
    # dashboard.  Modify this to subscribe to all the feeds you want to display.
    client.subscribe('pi-dashboard-slider')
    client.subscribe('pi-dashboard-humidity')
    client.subscribe('pi-dashboard-temp')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print 'Disconnected from Adafruit IO!'
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    # Update physical dashboard depending on the changed feed.
    # Notice the feed_id is checked to find out which feed changed, then the
    # appropriate physical dashboard widget is changed.
    if feed_id == 'pi-dashboard-slider':
        # The requests.post function will make an HTTP request against the
        # dashboard.  See the requests documentation for more information:
        #   http://docs.python-requests.org/en/latest/
        requests.post('{0}/widgets/slider'.format(DASHBOARD_URL), data={'value': payload})
    elif feed_id == 'pi-dashboard-humidity':
        requests.post('{0}/widgets/humidity'.format(DASHBOARD_URL), data={'value': payload})
    elif feed_id == 'pi-dashboard-temp':
        requests.post('{0}/widgets/temp'.format(DASHBOARD_URL), data={'value': payload})


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Use the loop_blocking function to run the message loop for processing Adafruit
# IO events.  Since this script doesn't do any other processing this blocking
# version of the message loop is fine.  All the program logic will occur in the
# callback functions above when Adafruit IO feeds are changed.
client.loop_blocking()
