# Raspberry Pi Physical Dashboard Main Application
# Author: Tony DiCola
#
# This will run a simple REST API server that has two endpoints:
#   - /widgets - Can perform a GET to retrieve a JSON list of all configured
#                widgets.
#   - /widgets/<widget_name> - Can perform a POST to set a specified widget
#                              value.  Send along a query or form paramter with
#                              name value and value set to the new widget value.
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
import threading

from flask import Flask, jsonify, request

import auto_gauge
import config
import led_backpacks
import widget


# Global configuration:
CONFIG_FILENAME = 'config.ini'  # Name of configuration file.
SERVER_HOST = '0.0.0.0'         # Host to listen on, by default publically accessible.
SERVER_PORT = 5000              # Server port.

# Global application state:
app = Flask(__name__)                   # The flask application.
config = config.Config(CONFIG_FILENAME) # Dashboard configuration.
widgets = config.get_widgets()          # Master widget list.
hw_lock = threading.Lock()              # Use a lock to serialize access to any
                                        # hardware.  This prevents issues with
                                        # multiple requests trying to write to
                                        # the I2C bus at the same time and
                                        # conflicting.

# API server routes and functions:
@app.route('/widgets', methods=['GET'])
def widgets_get():
    """Serialize list of widgets into a JSON result."""
    # Generate a list of widgets with attributes we want to publish.
    result = map(lambda x: {'name': x[0],
                            'type': type(x[1]).__name__,
                            'description': x[1].__doc__},
                 widgets.items())
    return jsonify({'widgets': result})

@app.route('/widgets/<widget_name>', methods=['POST'])
def widget_post(widget_name):
    """Set the value for a specified widget.  Must pass either a query or form
    parameter named 'value' equal to the value to set for the widget.
    """
    # Find the referenced widget.
    if widget_name.lower() not in widgets:
        return '', 404  # HTTP 404 not found error.
    widget = widgets[widget_name]
    # Check that a value was passed in and grab it.
    value = request.values.get('value')
    if value is None:
        return '', 400  # HTTP 400 bad request error.
    # Call the widget's set_value function with the provided value.
    try:
        # Use the lock to serialize calls that might talk to the hardware and
        # collide (only one thing should talk to the hardware at a time since the
        # I2C bus is shared between multiple devices).
        with hw_lock:
            widget.set_value(value)
    except Exception as ex:
        print('Error calling set_value for "{0}": {1}'.format(widget_name, ex))
        return '', 400  # HTTP 400 bad request error.
    return '', 204  # Return HTTP 204 no content response for success.

if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT, threaded=True)
