# Raspberry Pi Physical Dashboard LED Backpack Widgets
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
from Adafruit_LED_Backpack import AlphaNum4, BicolorBargraph24, SevenSegment

import widget


class AlphaNum4Widget(widget.Widget):
    """Quad alpha-numeric LED backpack widget.  Can display 4 character text
    and numeric values.
    """

    def __init__(self, address='0x70', brightness='15', decimal_digits='0',
                 justify_right='True'):
        """Create an instance of the quad alpha-numeric display widget.  Can pass
        in the following optional parameters to control the widget (note all
        parameters are strings as they are parsed from config files):
          - address: I2C address, default is 0x70
          - brightness: Brightness of the display, can be a value from 0 to 15
                        with 15 being the brightest.  The default is 15.
          - decimal_digits: Number of digits to show after decimal point, default
                            is 0.
          - justify_right: Justify numeric display to the right side if true (the
                           default).  Set to false to justify to the left side.
        """
        # Setup display and initial state.
        self._display = AlphaNum4.AlphaNum4(address=int(address, 0))
        self._display.begin()
        self._display.set_brightness(int(brightness))
        self._decimal_digits = int(decimal_digits)
        self._justify_right = self.parse_bool(justify_right)
        # Clear the display
        self._display.clear()
        self._display.write_display()

    def set_value(self, value):
        """Set the value of the display.  Must pass in a string with either a
        floating point value (note that only values -999 to 9999 will display),
        or up to 4 alpha-numeric characters.
        """
        # Check if the value can be converted to a float and displayed as such.
        self._display.clear()
        try:
            value = float(value)
            self._display.print_float(value, decimal_digits=self._decimal_digits,
                                      justify_right=self._justify_right)
        except ValueError:
            # Value isn't a float, so display the first 4 characters.
            self._display.print_str(value[0:4], justify_right=self._justify_right)
        self._display.write_display()

class BicolorBargraph24Widget(widget.Widget):
    """Bi-color 24 count bar graph LED backpack widget.  Can display a bar graph
    with 24 LEDs.  Set the value to a percentage of the LEDs to illuminate, like
    50.0 to turn on half of the LEDs.  Values in the range 0-100 will light up
    green, 200-300 will light up yellow, and 400-500 will light up red.
    """

    def __init__(self, address='0x70', brightness='15', justify_right='True'):
        """Create an instance of the bi-color bar graph widget.  Can pass in the
        following optional parameters to control the widget (note all
        parameters are strings as they are parsed from config files):
          - address: I2C address, default is 0x70
          - brightness: Brightness of the display, can be a value from 0 to 15
                        with 15 being the brightest.  The default is 15.
          - justify_right: Justify numeric display to the right side if true (the
                           default).  Set to false to justify to the left side.
        """
        # Setup display and initial state.
        self._display = BicolorBargraph24.BicolorBargraph24(address=int(address, 0))
        self._display.begin()
        self._display.set_brightness(int(brightness))
        self._justify_right = self.parse_bool(justify_right)
        # Clear the display
        self._display.clear()
        self._display.write_display()

    def set_value(self, value):
        """Set the value of the display.  Pass a string with a floating point
        value to set the bargraph with the specified percent of LEDs enabled.
        Passing a value in the range 0-100% will use green LEDs, 200-300% will
        use yellow LEDs, and 400-500% will use red LEDs.
        """
        # Get the floating point value and determine the range for the color.
        value = float(value)
        if 0.0 <= value <= 100.0:
            color = BicolorBargraph24.GREEN
        elif 200.0 <= value <= 300.0:
            color = BicolorBargraph24.YELLOW
            value -= 200.0  # Normalize value to be within 0-100.
        elif 400.0 <= value <= 500.0:
            color = BicolorBargraph24.RED
            value -= 400.0  # Normalize value to be within 0-100.
        else:
            raise RuntimeError('Unexpected bar graph value, must be in range of 0-100, 200-300, or 400-500!')
        # Light up the appropriate percent of LEDs.
        if self._justify_right:
            # Start from right and move left.
            positions = range(23, -1, -1)
        else:
            # Start from left and move right.
            positions = range(24)
        self._display.clear()
        for i, pos in enumerate(positions):
            if (i+1.0)/24.0*100.0 <= value:
                self._display.set_bar(pos, color)
        self._display.write_display()

class SevenSegmentWidget(widget.Widget):
    """Seven segment LED backpack widget.  Can display simple numeric values
    in the range of -999 to 9999.
    """

    def __init__(self, address='0x70', brightness='15', decimal_digits='0',
                 justify_right='True', invert='False'):
        """Create an instance of the seven segment display widget.  Can pass in
        the following optional parameters to control the widget (note all
        parameters are strings as they are parsed from config files):
          - address: I2C address, default is 0x70
          - brightness: Brightness of the display, can be a value from 0 to 15
                        with 15 being the brightest.  The default is 15.
          - decimal_digits: Number of digits to show after decimal point, default
                            is 0.
          - justify_right: Justify numeric display to the right side if true (the
                           default).  Set to false to justify to the left side.
          - invert: Vertically flip the display if true.  Default is false.  Note
                    that when flipped the decimal points will be at the top!
        """
        # Setup display and initial state.
        self._display = SevenSegment.SevenSegment(address=int(address, 0))
        self._display.begin()
        self._display.set_brightness(int(brightness))
        if self.parse_bool(invert):
            self._display.set_invert(True)
        self._decimal_digits = int(decimal_digits)
        self._justify_right = self.parse_bool(justify_right)
        # Clear the display
        self._display.clear()
        self._display.write_display()

    def set_value(self, value):
        """Set the value of the display.  Must pass in a string with either a
        floating point value (note that only values -999 to 9999 will display),
        or 'colon_on' to turn on the colon or 'colon_off' to turn off the colon.
        """
        value = value.lower()
        # Check if the value is a command to turn on/off the colon.
        if value == 'colon_on':
            self._display.set_colon(True)
        elif value == 'colon_off':
            self._display.set_colon(False)
        else:
            # Otherwise assume the value is a number and attempt to set the
            # display to show it.
            self._display.clear()
            value = float(value)
            self._display.print_float(value, decimal_digits=self._decimal_digits,
                                      justify_right=self._justify_right)
        self._display.write_display()
