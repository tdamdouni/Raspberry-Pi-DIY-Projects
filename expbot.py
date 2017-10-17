import explorerhat
import time

steps = [0 for x in range(16)]

G_FORWARDS = 2
G_BACKWARDS = 3
G_LEFT = 1
G_RIGHT = 4
G_PLAY = 5
G_STOP = 6

G_PREV = 7
G_NEXT = 8

edit_index = 0

def turn_on_light(light):
    explorerhat.light.off()
    if 0 <= light <= 3:
        explorerhat.light[light].on()

def handle_touch(ch, evt):
    global steps, running, edit_index
    print(ch, evt)

    if ch == G_PLAY:
        running = True
        print("Running...")
        return

    if ch == G_STOP:
        print("Stopped...")
        running = False
        return

    if ch == G_PREV:
        edit_index -= 1
        edit_index %= len(steps)
        turn_on_light(steps[edit_index]-1)

    if ch == G_NEXT:
        edit_index += 1
        edit_index %= len(steps)
        turn_on_light(steps[edit_index]-1)

    if ch in [G_FORWARDS, G_BACKWARDS, G_LEFT, G_RIGHT] and not running:
        turn_on_light(ch - 1)
        steps[edit_index] = ch
        edit_index += 1
        edit_index %= len(steps)

explorerhat.touch.pressed(handle_touch)
explorerhat.touch.released(handle_touch)

step_index = 0
running = False

while True:
    if not running:
        time.sleep(0.1)
        continue

    current_action = steps[step_index]

    if current_action == 0:
        explorerhat.light.off()
        step_index = 0
        continue

    turn_on_light(current_action - 1)

    if current_action == G_FORWARDS:
        explorerhat.motor.forwards()
    if current_action == G_BACKWARDS:
        explorerhat.motor.backwards()
    if current_action == G_LEFT:
        explorerhat.motor.two.forwards()
        explorerhat.motor.one.backwards()
    if current_action == G_RIGHT:
        explorerhat.motor.two.backwards()
        explorerhat.motor.one.forwards()

    time.sleep(0.5)

    explorerhat.motor.stop()

    step_index += 1
    step_index %= len(steps)