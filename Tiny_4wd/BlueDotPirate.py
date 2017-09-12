
from bluedot import BlueDot
from signal import pause
from explorerhat import motor

maxPower = 1.0

def move(pos):
    global maxPower
    x_axis = 0.0
    y_axis = 0.0
    if pos.top:
        y_axis= pos.distance

    elif pos.bottom:
        y_axis =-pos.distance
    elif pos.left:
        x_axis =-pos.distance
    elif pos.right:
        x_axis= pos.distance

    mixer_results = mixer(x_axis, y_axis)

    power_left = ((mixer_results[0]) * 100)
    power_right = ((mixer_results[1])* 100)

    print(power_left, power_right)

    motor.one.speed((-power_right * maxPower))
    motor.two.speed(power_left * maxPower)
def stop():
    print("stop")
    motor.one.speed(0)
    motor.two.speed(0)

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


bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()