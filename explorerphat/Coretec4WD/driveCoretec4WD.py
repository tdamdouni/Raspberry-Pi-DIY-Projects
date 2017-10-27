#!/usr/bin/env python3
# coding: Latin-1

# Load library functions we want

from inputs import get_gamepad
from explorerhat import motor


def mixer(inYaw, inThrottle, ):
    left = inThrottle + inYaw
    right = inThrottle - inYaw
    scaleLeft = abs(left / 125.0)
    scaleRight = abs(right / 125.0)
    scaleMax = max(scaleLeft, scaleRight)
    scaleMax = max(1, scaleMax)
    out_left = int(constrain(left / scaleMax, -125, 125))
    out_right = int(constrain(right / scaleMax, -125, 125))
    results = [out_right, out_left]
    return results


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


# Setup
maxPower = 1.0
power_left = 0.0
power_right = 0.0
x_axis = 0.0
y_axis = 0.0
invert_y = False
invert_x = True

try:
    print('Press CTRL+C to quit')

    # Loop indefinitely
    while True:

        events = get_gamepad()
        for event in events:
            print(event.code, event.state)
            if event.code == "ABS_Y":
                y_axis = event.state
                if y_axis > 130:
                    y_axis = -(y_axis - 130)
                elif y_axis < 125:
                    y_axis = ((-y_axis) + 125)
                else:
                    y_axis = 0.0
                if invert_y:
                    y_axis = -y_axis

            if event.code == "ABS_Z":
                x_axis = event.state
                if x_axis > 130:
                    x_axis = (x_axis - 130)
                elif x_axis < 125:
                    x_axis = -((-x_axis) + 125)
                else:
                    x_axis = 0.0
                if invert_x:
                    x_axis = -x_axis

            # if event.code == "BTN_TL":
            #     if event.state == True:
            #         print("Botton Left")
            # if event.code == "BTN_TR":
            #     if event.state == True:
            #         print("Botton Right")
            # if event.code == "BTN_Z":
            #     if event.state == True:
            #         print("Top right")
            #
            # if event.code == "BTN_WEST":
            #     if event.state == True:
            #         print("Top left")

            if event.code == "BTN_TL2":
                if event.state == True:
                    # print("Select")
                    x_axis = 0
                    y_axis = 0

            # if event.code == "ABS_HAT0X":
            #     if event.state == -1:
            #         print("D pad Left")
            #     elif event.state == 1:
            #         print("D pad Right")
            #
            # if event.code == "ABS_HAT0Y":
            #     if event.state == -1:
            #         print("D pad Up")
            #     elif event.state == 1:
            #         print("D pad Down")

            mixer_results = mixer(x_axis, y_axis)
            # print (mixer_results)
            power_left = int((mixer_results[0] / 125.0) * 100)
            power_right = int((mixer_results[1] / 125.0) * 100)
            # print("left: " + str(power_left) + " right: " + str(power_right))

            motor.one.speed((-power_right * maxPower))
            motor.two.speed(power_left * maxPower)

            # print(event.ev_type, event.code, event.state)

except KeyboardInterrupt:

    # CTRL+C exit, disable all drives
    print("stop")
    motor.stop()
print("bye")
