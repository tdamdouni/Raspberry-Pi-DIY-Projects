# Raspberry Pi Physical Dashboard LED Backpack Widget Tests
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
import time
import unittest

import led_backpacks


class TestSevenSegmentWidget(unittest.TestCase):
    def tearDown(self):
        time.sleep(2.0)  # 2 second delay between tests to see results on hardware.

    def test_colon_on(self):
        widget = led_backpacks.SevenSegmentWidget(address='0x76')
        widget.set_value('colon_on')

    def test_colon_off(self):
        widget = led_backpacks.SevenSegmentWidget(address='0x76')
        widget.set_value('colon_off')

    def test_number(self):
        widget = led_backpacks.SevenSegmentWidget(address='0x76')
        widget.set_value('-10.25')

    def test_decimal_digits(self):
        widget = led_backpacks.SevenSegmentWidget(address='0x76', decimal_digits='1')
        widget.set_value('-10.25')

    def test_justify_left(self):
        widget = led_backpacks.SevenSegmentWidget(address='0x76', justify_right='False')
        widget.set_value('-10.25')

    def test_invert(self):
        widget = led_backpacks.SevenSegmentWidget(address='0x76', invert='True')
        widget.set_value('-10.25')

    def test_brightness(self):
        widget = led_backpacks.SevenSegmentWidget(address='0x76', brightness='1')
        widget.set_value('-10.25')

    def test_invalid_value_fails(self):
        widget = led_backpacks.SevenSegmentWidget(address='0x76')
        with self.assertRaises(ValueError):
            widget.set_value('foo')

class TestAlphaNum4Widget(unittest.TestCase):
    def tearDown(self):
        time.sleep(2.0)  # 2 second delay between tests to see results on hardware.

    def test_number(self):
        widget = led_backpacks.AlphaNum4Widget(address='0x73')
        widget.set_value('-10.25')

    def test_small_string(self):
        widget = led_backpacks.AlphaNum4Widget(address='0x73')
        widget.set_value('foo')

    def test_long_string(self):
        widget = led_backpacks.AlphaNum4Widget(address='0x73')
        widget.set_value('foobar')

    def test_justify_left(self):
        widget = led_backpacks.AlphaNum4Widget(address='0x73', justify_right='False')
        widget.set_value('foo')

    def test_brightness(self):
        widget = led_backpacks.AlphaNum4Widget(address='0x73', brightness='1')
        widget.set_value('-10.25')

class TestBicolorBargraph24Widget(unittest.TestCase):
    def tearDown(self):
        time.sleep(2.0)  # 2 second delay between tests to see results on hardware.

    def test_0(self):
        widget = led_backpacks.BicolorBargraph24Widget(address='0x72')
        widget.set_value('0.0')

    def test_25(self):
        widget = led_backpacks.BicolorBargraph24Widget(address='0x72')
        widget.set_value('25.0')

    def test_50(self):
        widget = led_backpacks.BicolorBargraph24Widget(address='0x72')
        widget.set_value('50.0')

    def test_100(self):
        widget = led_backpacks.BicolorBargraph24Widget(address='0x72')
        widget.set_value('100.0')

    def test_brightness(self):
        widget = led_backpacks.BicolorBargraph24Widget(address='0x72', brightness='1')
        widget.set_value('100.0')

    def test_yellow(self):
        widget = led_backpacks.BicolorBargraph24Widget(address='0x72')
        widget.set_value('250.0')

    def test_red(self):
        widget = led_backpacks.BicolorBargraph24Widget(address='0x72')
        widget.set_value('450.0')

    def test_justify_left(self):
        widget = led_backpacks.BicolorBargraph24Widget(address='0x72', justify_right='False')
        widget.set_value('50.0')

    def test_invalid_value(self):
        widget = led_backpacks.BicolorBargraph24Widget(address='0x72')
        with self.assertRaises(ValueError):
            widget.set_value('foo')
