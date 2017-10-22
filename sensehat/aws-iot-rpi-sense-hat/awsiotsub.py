#!/usr/bin/python

import paho.mqtt.client as paho
import ssl
import json
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
        mqttc.subscribe("environmentData", qos=1)
    elif rc==1:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")

def on_message(mqttc, obj, msg):
    print(str(msg.payload))
    sense.show_message(str(json.loads(msg.payload)['environment']['temperature']['basedOnPressure']))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "data.iot.us-west-2.amazonaws.com"
awsport = 8883
clientId = "rpisensehat-subscriber"
thingName = "rpisensehat"
caPath = "rootCA.pem"
certPath = "3b60693e48-certificate.pem.crt"
keyPath = "3b60693e48-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_forever()
