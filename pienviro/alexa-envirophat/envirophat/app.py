import paho.mqtt.client as mqtt
from envirophat import light, weather, motion, analog, leds
import json
from time import sleep

ch = "755560112c589693968780500472f141eb13b8c9"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(ch)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == ch and msg.payload == "query-temp":
    	leds.on()
        temp = weather.temperature()
	res = { "temp": temp }
        client.publish(ch, json.dumps(res) )
	sleep(0.3)
	leds.off()
 
leds.off()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()

