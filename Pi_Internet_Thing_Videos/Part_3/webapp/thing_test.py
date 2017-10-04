import time

import thing


# Create the pi thing.
pi_thing = thing.PiThing()

# Print the current switch state.
switch = pi_thing.read_switch()
print('Switch status: {0}'.format(switch))

# Now loop forever blinking the LED and reading temp/humidity.
print('Looping with LED blinking (Ctrl-C to quit)...')
while True:
    # Blink the LED.
    pi_thing.set_led(True)
    time.sleep(0.5)
    pi_thing.set_led(False)
    time.sleep(0.5)
    # Get temp & humidity and print them out.
    humidity = pi_thing.get_humidity()
    temperature = pi_thing.get_temperature()
    print('Humidity: {0:0.2F}%  Temperature: {1:0.2F}C'.format(humidity, temperature))
