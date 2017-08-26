#!/usr/bin/env python
#Original code by alexellis and andicui, updated to run on scroll-phat-hd by alexmburns.


# Retrieve and print either the public IP or an internal IP address for an
# adapter such as wlan0 by passing it as an argument to the program.
# sudo python wlan0 => 192.168.0.x (useful for wifi hotspots)
#
# requires: netifaces for looking up IP in readable way
# requires: requests human readable HTTP requests
#
# Usage:
# "sudo python ip.py"
# Prints out your public IP address
#
# "sudo python ip.py internal"
# Prints out your internal, i.e. wi-fi or DHCP IP address

import json
import socket
import sys
import time

try:
    import requests
except ImportError:
    sys.exit("This script requires the requests module\nInstall with: sudo pip install requests")

import scrollphathd


def get_internal_ip():
    # As an alternative, look into netifaces package - pip install netifaces
    # netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

    ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
    return ip

def get_public_ip():
    ip = "127.0.0.1"
    res = requests.get('http://ipinfo.io')
    if(res.status_code == 200):
        json_data = json.loads(res.text)

        # this response also contains rich geo-location data
        ip = json_data['ip']
    return ip

def get_ip(mode):
    return get_public_ip() if mode == "public" else get_internal_ip()
#    return mode == "public" ? get_public_ip() : get_internal_ip()
    
address_mode = "public"
if(len(sys.argv) == 2):
    address_mode = sys.argv[1]

ip = get_ip(address_mode)

print(address_mode + " IP Address: " +str(ip))

scrollphathd.set_brightness(0.5)

scrollphathd.write_string("  IP: " + str(ip) + "    ")

while True: 
    try:
	scrollphathd.show()
	scrollphathd.scroll()
        time.sleep(0.05)

    except KeyboardInterrupt:
        scrollphathd.clear()
        sys.exit(-1)
