# Simple 'mqtt' client that publishes 'SenseHat' data to an 'mqtt' broker.
# Incoming messages with a payload of '?' (question-mark) will re-publish a fresh value for the requested topic.
#
# See: https://pypi.python.org/pypi/paho-mqtt for how to install required library for the client (this program)
# 
# To install a 'broker' (can be the same or different host) ; you can install 'mosquitto' by running:
# sudo apt-get install mosquitto
#
# Once the 'mosquitto' broker is installed, it will start automatically on the default port of 1883.
# To install a separate 'subscriber' client; you can either use another Python Program based on 'paho-mqtt'
# Or (for instance) use an Ipod/Iphone App, for instance : https://itunes.apple.com/us/app/zmqtt-utility/id737370079?mt=8
# 
# The program will publish on the following 'topics':
# <hostname-client-is-running-on>/sensehat/<sensor>
# eg:
# raspberrypi/sensehat/temperature
#

import paho.mqtt.client as mqtt
from os import uname
from sense_hat import SenseHat

class SensorClient(object):

	def __init__(self, broker, broker_port):
		self.sense=SenseHat()
		self.broker=broker
		self.broker_port=broker_port
		self.client_id=uname()[1]
		
		sub_topics=	{	"temperature"	:	lambda: self.sense.get_temperature(),
					"humidity"	:	lambda: self.sense.get_humidity(),
					"pressure"	:	lambda:	self.sense.get_pressure() }

		self.topics={}
		root_topic="%s/sensehat"%self.client_id
		for sub_topic in sub_topics.keys():
			topic="%s/%s"%(root_topic, sub_topic)
			self.topics[topic]=sub_topics[sub_topic]
			

	def on_connect(self, client, userdate, flags, rc):
		for topic in sorted(self.topics):
			print "Subscribing to %s"%(topic)
			client.subscribe( topic )
		self.publish_sensor_topics()

	# If we recieve the payload of '?' (question-mark)
	# Then publish the value to the topic
	def on_message(self, client, userdata, msg):
		if msg.payload=="?":
			try:
				self.publish_topic( msg.topic )
			except Exception as e:
				print "Error when trying to publish '%s' ?"%msg.topic
		else:
			print "Ignoring message %s=%s"%(msg.topic, msg.payload)
		
	
	def publish_topic( self, topic ):
		topic_value=self.topics[topic]() # execute the Lambda to fetch value
		print "Publishing %s=%s"%(topic, topic_value)
		self.mqtt_client.publish( topic, topic_value )

	# Publish all topics (called when we first connect)
	def publish_sensor_topics(self):
		for topic in sorted(self.topics):
			self.publish_topic( topic )

	def run(self):
		self.mqtt_client=mqtt.Client( self.client_id )
		self.mqtt_client.on_message=self.on_message
		self.mqtt_client.on_connect=self.on_connect
		self.mqtt_client.connect(broker, broker_port)
		self.mqtt_client.loop_forever()

if __name__=='__main__':
	broker="broker_pi" # change this to match your broker's IP or hostname
	broker_port=1883
	client=SensorClient(broker, broker_port)
	client.run()
