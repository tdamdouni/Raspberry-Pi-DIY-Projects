import paho.mqtt.client as paho
client = paho.Client()
client.connect("servername", 1883, 60)
client.publish("sensor", payload="Test", qos=0, retain=True)
