# Raspberry Pi Physical Dashboard Main Application
# Author: Tony DiCola
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
import abc


class Widget(object):
    """Base class for LED board widgets."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_value(self, value):
        pass

    def parse_bool(self, value):
        """Parse a boolean true/false string value into a Python bool."""
        if value is None:
            return False
        if value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
        else:
            raise ValueError('Expected boolean to be either true or false value.')


def find_widget(type_name):
    """Look for a widget with the defined type name and return the class
    of the widget.  If no widget is found then None is returned.
    """
    for sc in Widget.__subclasses__():
        if type_name.lower() == sc.__name__.lower():
            return sc
    return None
