# sensehat
Raspberry Python SenseHat code
Just some simple programs to play around with Raspberry Pi SenseHat Board.

'kaleidoscope.py'
================

Just draws pretty symmetrical patterns.

'smallhex.py'
=============

Defines small (3x5) pixel characters to display two digit number on the
SenseHat LEDs; to avoid scrolling text.

Hex + Decimal digits defined.


'sensor_client.py'
==================

Publishes SenseHat data (temperature, humidity, pressure) to an 'mqtt' broker.
Allows other clients (by sending a '?' (question-mark) to the appropriate topic)
to recieve the information from the SenseHat.

Other devices can then be used to request and display the information from the SenseHat.

See: https://pypi.python.org/pypi/paho-mqtt for required library.

Needs an 'mqtt' broker: you can install 'mosquitto' on the Pi with:

	sudo apt-get install mosquitto

Note: the broker and the client can be run on different machines or the same machine.

Screenshot: showing an iOS client (https://itunes.apple.com/us/app/zmqtt-utility/id737370079?mt=8) sending out MQTT messages
and displaying the output.

The UI is very responsive , (probably) due to the lightweight nature of MQTT.

![screenshot](https://github.com/midijohnny/sensehat/blob/master/mqtt-ipod.png)


'mqtt_lights.py'
================

Simple subscriber (does not publish anything itself) that listens for messages and switches SenseHat LEDs on/off.

'log_sensors_to_csv.py'
======================
Writes date+sensor data to a 'CSV' file in a loop. 
Loop will run for a fixed number of readings, pausing for a fixed number of secondsbetween readings.


'ledpaint.py'
=============
A 'painting' tool - runs a GUI (Tkinter) that lets you 'paint' in realtime onto the SenseHat LED matrix.

Here's a screenshot showing a rudimentary representation of a smiling human face. And then a photo showing the result of the SenseHat itself

![screenshot](https://github.com/midijohnny/sensehat/blob/master/ledpainter.png)
![screenshot](https://github.com/midijohnny/sensehat/blob/master/senseface.jpg)

New ! Multi-coloured support - simply press SPACE to cycle through 7 fantastic colours !
Also: you can hold down the mouse button to paint - as well as clicking individual pixels !

![screenshot](https://github.com/midijohnny/sensehat/blob/master/ghost.png)
![screenshot](https://github.com/midijohnny/sensehat/blob/master/senseghost.jpg)

'morse_sense.py'
================

Just blinks morse code on the SenseHat.
For a small novelty you can blink the actual letters on the sense hat ('flash_letter'=True on the constructor).
Additionally: it is the only program I have written where I have had to pleasure of being able to name a method 'do_dah' and for the name to be meaningful ! :-)

I don't speak Morse, so I can't say whether the output it is actually discernable to anybody - although "SOS" looked about right !
Gets the definitions from a text file (default 'morse.txt', included)

