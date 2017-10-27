#!/usr/bin/env python
# Code for Brian Corteil's Tiny 4WD robot, based on his original code,
# but using appproxeng libraries to allow genuine PS3 support
# (see https://github.com/ApproxEng/approxeng.input.git)

# Load library functions we want

from approxeng.input.dualshock3 import DualShock3
from approxeng.input.selectbinder import ControllerResource
from time import sleep
from explorerhat import motor


# Setup
maxPower  = 1.0
power_left = 0.0
power_right = 0.0
x_axis = 0.0
y_axis = 0.0

def mixer(inYaw, inThrottle,):
    left = inThrottle + inYaw
    right = inThrottle - inYaw
    scaleMax = max(1, abs(left), abs(right))
    results = [left/scaleMax, right/scaleMax]
    return results

try:
    print('Press CTRL+C to quit')

    # Loop indefinitely
    with ControllerResource(controller_class = DualShock3, dead_zone=0.1, hot_zone=0.2) as joystick:
        while True:
            # Loop, printing the corrected value from the left stick
            x_axis = joystick.axes.get_value('lx')
            y_axis = joystick.axes.get_value('ly')
            # Don't be too spammy!
            sleep(0.1)

            mixer_results = mixer(x_axis, y_axis)
            #print (mixer_results)
            power_left = int(mixer_results[0]*100)
            power_right = int(mixer_results[1]*100)

            #print("left: " + str(power_left) + " right: " + str(power_right))

            motor.one.speed((-power_right * maxPower))
            motor.two.speed(power_left * maxPower)

except KeyboardInterrupt:

    # CTRL+C exit, disable all drives
    print("stop")
    motor.stop()
print("bye")
