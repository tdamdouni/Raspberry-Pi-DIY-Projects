import time

import thing


# Create the pi thing.
pi_thing = thing.PiThing()

# Print the current switch state.
switch = pi_thing.read_switch()
print('Switch status: {0}'.format(switch))

# Now loop forever blinking the LED.
print('Looping with LED blinking (Ctrl-C to quit)...')
while True:
    pi_thing.set_led(True)
    time.sleep(0.5)
    pi_thing.set_led(False)
    time.sleep(0.5)
