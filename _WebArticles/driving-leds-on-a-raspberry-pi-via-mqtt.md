# Driving LEDs on a Raspberry Pi via MQTT

_Captured: 2017-08-09 at 18:03 from [blog.thelifeofkenneth.com](http://blog.thelifeofkenneth.com/2016/07/driving-leds-on-raspberry-pi-via-mqtt.html?m=1)_

![](https://3.bp.blogspot.com/-dyTqIMU1PeQ/V3c7LZrk-jI/AAAAAAAARQw/ifTNK4kmMsw62Pppep0V70IQyfgWcrPYACLcB/s280/2016-07-01%2B19.30.08.jpg)

[MQTT](https://en.wikipedia.org/wiki/MQTT) is essentially an Internet of Things protocol which is designed to pass single short messages between a set of devices publishing messages to a set of devices which are subscribed to that topic.

A fantastic example of where you might use MQTT is an Internet-connected light switch plus light bulbs. You would first define a topic for your room (i.e. home/livingroom/lights/ceiling) and then configure all the appropriate light bulbs to subscribe to that topic and listen for any messages published to it. You could then configure a light switch on the wall to publish "ON" when you flip it up, and "OFF" when you flip it down. Flip the switch up, it publishes the message to the MQTT broker, which forwards it to all the lightbulbs subscribed to the home/livingroom/lights/ceiling topic, which would all respond accordingly. BOOM! IoT paradise! What could possibly go wrong?!

I've been meaning to do something with MQTT for several years, but the [recent (outstanding) series on MQTT published on HaD](http://hackaday.com/tag/minimal-mqtt/) has finally kicked me into action. This post is documenting the low-voltage half of a project I'm working on to upgrade my status lights at work.

![](https://1.bp.blogspot.com/-AX6XUqZLOo0/V3c950mraaI/AAAAAAAARQ8/VqSaRp5UFpICNeaQcZtV56DFLxQ0xANLQCLcB/s280/2016-07-01%2B21.05.49.jpg)

Stack lights, or [Andons](https://en.wikipedia.org/wiki/Andon_\(manufacturing\)), are traditionally used in industrial settings to alert tool operators/management to issues on the factory floor. I instead have one mounted on my cubicle at work which I use to show when I'm in the office, in the lab, off-site, etc. It is... a little conspicuous in the middle of a cube farm, but my coworkers have learned to appreciate its utility.

Until now, I've controlled mine via three toggle switches on my desk, but why use toggle switches where you can use technology?

[Video](https://www.youtube.com/watch?v=NnENfcQTtiU):

On the Raspberry Pi, I'm running a few dozen lines of Python to subscribe to the MQTT topic using the [Paho-MQTT](https://pypi.python.org/pypi/paho-mqtt/) library and write to the GPIO pins using the RPi.GPIO library (which comes pre-installed in Raspbian)

To set up the Raspberry Pi, install Raspbian, then install paho-mqtt by running this in a terminal:

sudo pip install paho-mqtt

[The source code](https://gist.github.com/PhirePhly/5eda4214788429e9d09c060cca10971f) consists of defining a call-back function for the MQTT library to call when it connects to the server, and a second call-back function to call to process each incoming message. Once the callbacks are defined, the GPIO pins are configured as outputs and control is handed off to the MQTT library to process messages forever.

#!/usr/bin/env python

import paho.mqtt.client as mqtt

import RPi.GPIO as GPIO

def on_connect(client, userdata, rc):

#print ("Connected with rc: " \+ str(rc))

client.subscribe("kwf/demo/led")

def on_message(client, userdata, msg):

#print ("Topic: "\+ msg.topic+"\nMessage: "+str(msg.payload))

if "green" in msg.payload:

#print(" Green on!")

GPIO.output(11, True)

else:

#print(" Green off!")

GPIO.output(11, False)

if "yellow" in msg.payload:

#print(" Yellow on!")

GPIO.output(12, True)

else:

#print(" Yellow off!")

GPIO.output(12, False)

if "red" in msg.payload:

#print(" Red on!")

GPIO.output(13, True)

else:

#print(" Red off!")

GPIO.output(13, False)

client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

GPIO.setup(12, GPIO.OUT)

GPIO.setup(13, GPIO.OUT)

client.loop_forever()

Running the script would look like this:

wget https://gist.github.com/PhirePhly/5eda4214788429e9d09c060cca10971f/raw/8696da1520b76fee9c2213503a4e125d9ce1bfdd/mqtt_led_client.py  
chmod +x mqtt_led_client.py  
./mqtt_led_client.py

There are a dozen different ways to have programs automatically run on boot in Linux systems, but my tool of choice is to add a line to my cron table (via running crontab -e):  
@reboot /home/pi/mqtt_led_client.py

![](https://2.bp.blogspot.com/-jid43ELd4IM/V3c7KULSWgI/AAAAAAAARQ0/lgE_Qo-h09spO_brtCGvL9kwt2ejLcsqgCKgB/s280/2016-07-01%2B19.30.48.jpg)

All that's left to do at this point is have the Pi's GPIO's drive transistors instead of LEDs to light up the 24V stack light I managed to find in a debris pile at work and button the whole project up enough to sit on my desk at work.
