# Raspberry Pi Physical Dashboard Automotive Gauge Widget
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
from Adafruit_MotorHAT import Adafruit_MotorHAT

import widget


class AutoGaugeWidget(widget.Widget):
    """Automotive gauge stepper motor.  Small dual-coil stepper that can travel
    ~315 degrees with 600 steps.  Send a numeric value from 0-100 to move the
    dial to the specified percent along its entire range of movement.
    """

    def __init__(self, motor_id, invert='False'):
        """Create an instance of the auto stepper motor.  Must provide a motor_id
        parameter with the motor ID from the motor HAT (sent as a string).  Can
        optionally provide:
          - invert: Set to True to reverse the forward/backward direction.  Set
                    this if the motor spins the wrong way when going forward/backward.
        """
        # Create stepper motor driver.
        self._mh = Adafruit_MotorHAT()
        self._stepper = self._mh.getStepper(600, int(motor_id))
        self._forward = Adafruit_MotorHAT.FORWARD
        self._backward = Adafruit_MotorHAT.BACKWARD
        if self.parse_bool(invert):
            # Invert forward/backward directions
            self._forward, self._backward = self._backward, self._forward
        # Rotate forward 600 times to get back into a known 0/home state.
        for i in range(600):
        	self._stepper.oneStep(self._backward,  Adafruit_MotorHAT.DOUBLE)
        self._steps = 0

    def set_value(self, value):
        """Set the value of the gauge.  Must pass in a string with a floating
        point value in the range 0-100.  The dial will be moved to the specified
        percent location along its range of movement (about 315 degrees).
        """
        # Convert the value to a float percentage.
        value = float(value)
        if value < 0.0 or value > 100.0:
            raise RuntimeError('Value must be in range of 0-100!')
        # Figure out how many forward or backward steps need to occur to move
        # to the specified position.
        new_steps = value/100.0*600.0
        delta = int(new_steps - self._steps)
        direction = self._backward if delta < 0 else self._forward
        # Move the required number of steps and update the current step location.
        for i in range(abs(delta)):
            self._stepper.oneStep(direction, Adafruit_MotorHAT.DOUBLE)
        self._steps = new_steps
