# Adafruit IO MQTT 'debug' view to see all messages.  Will display every
# message published for an account on AIO.  Useful for debugging when other
# devices are writing to AIO for an account.
#
# Copyright (c) 2014, 2016 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import logging

import paho.mqtt.client as mqtt


# Edit below to include your AIO account details.
USERNAME  = 'YOUR AIO USERNAME'
KEY       = 'YOUR AIO KEY'

# Adafruit IO MQTT service details.
SERVER    = 'io.adafruit.com'
PORT      = 1883
KEEPALIVE = 3600  # One minute

# Path to subscribe to for messages.  By default this is the '<username>/#' path
# which means all messages for that user will be seen.
PATH      = USERNAME + '/#'


# Setup message handlers for connect, disconnect and message received.
def on_connect(client, userdata, flags, rc):
    print('Connected!')
    client.subscribe(PATH)
    print('Subscribed to path {0}!'.format(PATH))

def on_disconnect(client, userdata, rc):
    print('Disconnected!')

def on_message(client, userdata, msg):
    print('Received on {0}: {1}'.format(msg.topic, msg.payload.decode('utf-8')))


# Create MQTT client and connect to Adafruit IO.
client = mqtt.Client()
client.username_pw_set(USERNAME, KEY)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect(SERVER, port=PORT, keepalive=KEEPALIVE)

print('Press Ctrl-C to quit.')
client.loop_forever()
