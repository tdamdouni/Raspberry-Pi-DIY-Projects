#/usr/bin/env python

import time
import bluetooth

tag = "ff:ff:ff:ff:ff:ff"

def search():
	devices = bluetooth.discover_devices(duration=5, lookup_names = True)
	return devices

 while True:
	results = search()

	for addr, name in results:
		if addr == tag:
			# perform function
 
 time.sleep(20)