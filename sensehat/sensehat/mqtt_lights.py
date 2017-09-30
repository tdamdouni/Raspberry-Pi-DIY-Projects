# Simple demonstration of a subscribing mqtt client (no publishing done)
# Will respond to simple messages to turn on/off SenseHat Lights
# Tested on a ipod as the controller using the App : https://itunes.apple.com/us/app/zmqtt-utility/id737370079?mt=8
# But any client that outputs the same format messages should work
#
import paho.mqtt.client as mqtt
import re
from sense_hat import SenseHat

sense=SenseHat()

broker="broker_pi" # change this to match your broker's IP or hostname
broker_port=1883

on=(0,255,0) 	# Green pixel for on
off=(255,0,0)	# Red pixel for off

def on_connect(client, userdata, flags, rc):
	sense.clear()
	client.subscribe("#") # subscribe to ALL topics: we will filter for what we need in the 'on_message' method.

def on_message(client, userdata, msg):
	base=msg.topic.split("/")[-1]
	if re.match( "device\d", base ):
		device=int( base[-1] )
		if msg.payload=="Switch_Off":
			print "Switching device %d off"%device
			state=off
		else:
			if msg.payload=="Switch_On":
				print "Switching device %d on"%device
				state=on
		sense.set_pixel( device,0, state)
	else:
		print "Ignoring message: %s=%s"%(msg.topic, msg.payload)

client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect(broker, broker_port, 60)
client.loop_forever()
