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
import os
import unittest


class IOTestCase(unittest.TestCase):

    def get_test_key(self):
        """Return the AIO key specified in the ADAFRUIT_IO_KEY environment
        variable, or raise an exception if it doesn't exist.
        """
        key = os.environ.get('ADAFRUIT_IO_KEY', None)
        if key is None:
            raise RuntimeError("ADAFRUIT_IO_KEY environment variable must be " \
              "set with valid Adafruit IO key to run this test!")
        return key

    def get_test_username(self):
        """Return the AIO username specified in the ADAFRUIT_IO_USERNAME
        environment variable, or raise an exception if it doesn't exist.
        """
        username = os.environ.get('ADAFRUIT_IO_USERNAME', None)
        if username is None:
            raise RuntimeError("ADAFRUIT_IO_USERNAME environment variable must be " \
              "set with valid Adafruit IO username to run this test!")
        return username
