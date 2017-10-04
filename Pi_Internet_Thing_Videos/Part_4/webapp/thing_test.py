import time

import thing


# Create the pi thing.
pi_thing = thing.PiThing()

# Print the current switch state.
switch = pi_thing.read_switch()
print('Switch status: {0}'.format(switch))

# Print when the switch changes.
def switch_change(switch):
    if switch:
        print('Switch is ON!')
    else:
        print('Switch is OFF!')

# Print when the temperature & humidity reading is updated.
def temp_humidity_change(temperature, humidity):
    print('Humidity: {0:0.2F}%  Temperature: {1:0.2F}C'.format(humidity, temperature))

# Register the callbacks above to fire when their state changes.
pi_thing.on_switch_change(switch_change)
pi_thing.on_temp_humidity_change(temp_humidity_change)

# Now loop forever blinking the LED.  When the switch & temp/humidity state
# changes the callbacks above will be called and print out the new values.
print('Looping with LED blinking (Ctrl-C to quit)...')
while True:
    # Blink the LED.
    pi_thing.set_led(True)
    time.sleep(0.5)
    pi_thing.set_led(False)
    time.sleep(0.5)
