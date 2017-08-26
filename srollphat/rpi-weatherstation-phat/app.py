#!/usr/bin/env python
import time
from envirophat import weather
from microdotphat import write_string, set_decimal, clear, show

try:
    while True:
        clear()
        temperature = weather.temperature()
        write_string( "%.2f" % temperature + "C", kerning=False)
        show()
        time.sleep(1)

except KeyboardInterrupt:
    pass
