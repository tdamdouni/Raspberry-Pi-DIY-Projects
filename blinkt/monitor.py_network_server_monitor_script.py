# https://pastebin.com/7TvNKqMV

# http://forums.pimoroni.com/t/simple-network-monitor-with-blinkt/5915

import os,signal
from blinkt import clear,set_brightness, set_pixel, show,set_all
from time import sleep

hostlist = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4", "192.168.0.5", "192.168.0.6", "192.168.0.7", "8.8.8.8"]
hostid = ["Router", "Server 1", "Server 2", "Server 3", "Server 4", "Server 5", "Server 6", "Internet"]

clear()
set_brightness(0.05)
set_all(0,0,255)
show()
sleep(30)

def handler(signum, frame):
   clear()
   show()
   exit(0)

signal.signal(signal.SIGTERM, handler)

while True:
   for hostnum, hostname in enumerate(hostlist):
      response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")
      if response == 0:
#         print hostnum, ' - ', hostid[hostnum], 'is up!'
         set_pixel(hostnum, 0, 255, 0)
      else:
#         print hostnum, ' - ', hostid[hostnum], 'is down!'
         set_pixel(hostnum, 255, 0, 0)
   show()
   sleep(60)