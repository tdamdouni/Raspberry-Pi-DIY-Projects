# http://forums.pimoroni.com/t/multiple-remote-enviro-phats-on-a-single-raspberry-pi/5925/4

from envirophat import analog

analog_values = analog.read_all()
print(analog_values)
