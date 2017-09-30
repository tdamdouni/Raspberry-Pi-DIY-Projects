# Copyright (c) 2014 Adafruit Industries
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
import time

from Adafruit_IO import MQTTClient

import base


TIMEOUT_SEC = 5  # Max amount of time (in seconds) to wait for asyncronous events
                 # during test runs.


class TestMQTTClient(base.IOTestCase):

    def wait_until_connected(self, client, connect_value=True, 
        timeout_sec=TIMEOUT_SEC):
        # Pump the specified client message loop and wait until it's connected, 
        # or the specified timeout has ellapsed.  Can specify an explicit 
        # connection state to wait for by setting connect_value (defaults to 
        # waiting until connected, i.e. True).
        start = time.time()
        while client.is_connected() != connect_value and \
              (time.time() - start) < timeout_sec:
            client.loop()
            time.sleep(0)

    def test_create_client(self):
        # Create MQTT test client.
        client = MQTTClient(self.get_test_username(), self.get_test_key())
        # Verify not connected by default.
        self.assertFalse(client.is_connected())

    def test_connect(self):
        # Create MQTT test client.
        client = MQTTClient(self.get_test_username(), self.get_test_key())
        # Verify on_connect handler is called and expected client is provided.
        def on_connect(mqtt_client):
            self.assertEqual(mqtt_client, client)
        client.on_connect = on_connect
        # Connect and wait until on_connect event is fired.
        client.connect()
        self.wait_until_connected(client)
        # Verify connected.
        self.assertTrue(client.is_connected())

    def test_disconnect(self):
        # Create MQTT test client.
        client = MQTTClient(self.get_test_username(), self.get_test_key())
        # Verify on_connect handler is called and expected client is provided.
        def on_disconnect(mqtt_client):
            self.assertEqual(mqtt_client, client)
        client.on_disconnect = on_disconnect
        # Connect and wait until on_connect event is fired.
        client.connect()
        self.wait_until_connected(client)
        # Now disconnect and wait until disconnection event occurs.
        client.disconnect()
        self.wait_until_connected(client, connect_value=False)
        # Verify diconnected.
        self.assertFalse(client.is_connected())

    def test_subscribe_and_publish(self):
        # Create MQTT test client.
        client = MQTTClient(self.get_test_username(), self.get_test_key())
        # Save all on_message handler responses.
        messages = []
        def on_message(mqtt_client, feed, payload):
            self.assertEqual(mqtt_client, client)
            messages.append((feed, payload))
        client.on_message = on_message
        # Connect and wait until on_connect event is fired.
        client.connect()
        self.wait_until_connected(client)
        # Subscribe to changes on a feed.
        client.subscribe('TestFeed')
        # Publish a message on the feed.
        client.publish('TestFeed', 42)
        # Wait for message to be received or timeout.
        start = time.time()
        while len(messages) == 0 and (time.time() - start) < TIMEOUT_SEC:
            client.loop()
            time.sleep(0)
        # Verify one update message with payload is received.
        self.assertListEqual(messages, [('TestFeed', '42')])
