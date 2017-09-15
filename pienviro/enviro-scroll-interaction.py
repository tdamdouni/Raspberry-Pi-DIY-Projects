# http://forums.pimoroni.com/t/scrollphat-envirophat-error/4049/4

import sys
import time
import scrollphat

from envirophat import weather

scrollphat.set_brightness(2)

while True:
try:
print("updating new temp to diplay")
scrollphat.clear()
temp = "The temp is " + str(weather.temperature())
scrollphat.write_string(temp,0)
length = scrollphat.buffer_len()

            for i in range(length):
                    scrollphat.scroll()
                    time.sleep(0.1)

            scrollphat.clear()
            time.sleep(10)

    except KeyboardInterrupt:
            scrollphat.clear()
            sys.exit(-1)
