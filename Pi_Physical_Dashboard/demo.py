# Raspberry Pi Physical Dashboard Demo
# Author: Tony DiCola
#
# This demo will randomly set a collection of widgets to random values and is
# a basic example of setting dashboard values from a Python script.
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import random
import time

import requests


SERVER_URL = 'http://raspberrypi:5000'  # URL of the Pi dashboard server.
                                        # Note this should NOT end in a slash!
SLEEP_RANGE = (0.01, 0.5)               # Range of time (in seconds) to randomly
                                        # sleep between dashboard updates.

# Define the list of widgets and possible values.
# Each dict key should be a widget name, and each dict value should be a list
# of possible values.  When the script runs it will pick a random widget and
# a random value from the list of possible values for that widget.
widgets = {
  'cpu': ['29', '55', '99', '1', '14', '22', '27', '28', '18'],
  'memory': ['87.63', '92.22', '78.91', '77.65', '65.45', '86.82'],
  'uptime': ['22.6', '22.7', '22.8', '22.9'],
  'happiness': ['23', '55', '85', '214', '230', '275', '430', '460', '480'],
  'word': ['ADA', 'BOT', 'FUN', 'COOL'],
  'email': ['32', '64', '2', '50', '20']
}


print('Press Ctrl-C to quit...')
while (True):
    # Pick a random widget to update and send a random value.
    widget = random.choice(widgets.items())
    widget_name = widget[0]
    widget_value = random.choice(widget[1])
    # Make the request using the requests library.  See their documentation for
    # details on usage:
    #   http://docs.python-requests.org/en/latest/user/quickstart/
    r = requests.post('{0}/widgets/{1}'.format(SERVER_URL, widget_name),
                      data={'value': widget_value})
    print('Updated widget "{0}" with value "{1}" and received response: {2}'.format(widget_name, widget_value, r.status_code))
    # Sleep for a small period of random time and do it all again.
    time.sleep(random.uniform(SLEEP_RANGE[0], SLEEP_RANGE[1]))
