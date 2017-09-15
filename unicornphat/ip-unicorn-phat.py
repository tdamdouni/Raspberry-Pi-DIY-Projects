# https://www.hackster.io/colinodell/binary-ip-address-display-for-raspberry-pi-163cc0

import socket 
import time 
import unicornhat as unicorn 

# From http://commandline.org.uk/python/how-to-find-out-ip-address-in-python/ 
def getNetworkIp(): 
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
   s.connect(('google.com', 0)) 
   return s.getsockname()[0] 

# Prepare the Unicorn pHAT display
unicorn.set_layout(unicorn.PHAT) 
unicorn.rotation(0) 
unicorn.brightness(0.5) 

# Obtain our IP address and split it into the 4 components ("octets")
ip = getNetworkIp() 
octets = ip.split('.') 

# Render the binary representation for each octet
y = 0 
for octet in octets: 
 bits = '{0:08b}'.format(int(octet)) 
 x = 0 
 for b in bits: 
   if int(b): 
     unicorn.set_pixel(x, y, 0, 0, 128) 
   x += 1 
 y += 1 

# Render the display
unicorn.show() 

# Keep the LEDs lit for 30 seconds
time.sleep(30) 