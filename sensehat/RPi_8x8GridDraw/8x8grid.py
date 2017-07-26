import os, sys

if os.path.isfile("/proc/device-tree/hat/product"):
	file = open("/proc/device-tree/hat/product","r")
	hat = file.readline()
	if  hat == "Sense HAT\x00":
		print('Sense HAT detected')
		mypath = os.path.dirname(os.path.abspath(__file__))
		file.close()
		os.system("/usr/bin/env python3 " + mypath+"/8x8grid-sense.py")
	elif hat == "Unicorn HAT\x00":
		print('Unicorn HAT detected')
		mypath = os.path.dirname(os.path.abspath(__file__))
		file.close()
		os.system("/usr/bin/env python3 " + mypath+"/8x8grid-unicorn.py")
	else:
		print("Unknown HAT : " + str(hat))
		file.close()
		sys.exit()
else:
	print('No HAT detected')
	answer = input('Do you have a Unicorn Phat (y/n)?')
	if answer == 'y':
		print('Configuring for Unicorn Phat')
		mypath = os.path.dirname(os.path.abspath(__file__))
		os.system("/usr/bin/env python3 " + mypath+"/8x8grid-unicornphat.py")
	else:
		sys.exit()
