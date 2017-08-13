# joystick.py - Joystick Example
This program is an example of using a joystick or gamepad to remote control the motor outputs and Explorer Hat touch pads of a Raspberry Pi running STS-PiLot.  
Although joystick.py is meant to run on a different computer than your STS-Pi it can be run on the same machine by using the loopback IP address (127.0.0.1).  
If you want video output on your client computer you can use a web browser and connect to the STS-PiLot web interface.
## Using joystick.py
* Required Python module: python-requests
* Edit lines 11 and 12 to match the IP address and Port of the STS-Pilot instance you want to control.
* Invoke the program with  
python joystick.py
* You can also set address, port and joystick number from the command line  
python joystick.py -a IP -p PORT -j JOYSTICK No.
* Joystick buttons 1-4 are by default mapped to the four touch pads on the Explorer Hat. Their role is similar to the HUD buttons on the web interface.

Enjoy! Mark Dammer, Forres, Scotland 2017
