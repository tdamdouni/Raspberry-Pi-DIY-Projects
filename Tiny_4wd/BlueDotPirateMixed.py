from bluedot import BlueDot
from signal import pause
from explorerhat import motor

maxPower = 1.0

def pos_to_values(x, y):
    left = y if x > 0 else y + x
    right = y if x < 0 else y - x
    return (clamped(left), clamped(right))

def clamped(v):
    return max(-1, min(1, v))

def drive():
    global maxPower
    x_axis = 0.0
    y_axis = 0.0
    min_power = 0.3
    while True:
        if bd.is_pressed:
            x_axis, y_axis = bd.position.x, bd.position.y
            print(x_axis,y_axis)
        else:
            x_axis, y_axis = 0, 0

        if abs(x_axis) < min_power:
            x_axis = 0

        if abs(y_axis) < min_power:
            y_axis = 0

        mixer_results = mixer(x_axis, y_axis)

        power_left = ((mixer_results[0]) * 100)
        power_right = ((mixer_results[1]) * 100)

        # print(power_left, power_right)

        motor.one.speed((-power_right * maxPower))
        motor.two.speed(power_left * maxPower)

def mixer(inYaw, inThrottle,):
    left = inThrottle + inYaw
    right = inThrottle - inYaw
    scaleLeft = abs(left)
    scaleRight = abs(right)
    scaleMax = max(scaleLeft, scaleRight)
    scaleMax = max(1, scaleMax)
    out_left = (constrain(left / scaleMax, -1, 1))
    out_right = (constrain(right / scaleMax, -1, 1))
    results = [out_right, out_left]
    return results

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

bd = BlueDot()

drive()

pause()