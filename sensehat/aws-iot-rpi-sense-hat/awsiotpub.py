#!/usr/bin/python

import paho.mqtt.client as paho
import os
import socket
import ssl
import json
from time import sleep
from sense_hat import SenseHat

connflag = False

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    if rc==0:
        print ("Connection status: successful")
    elif rc==1:
        print ("Connection status: Connection refused")

sense = SenseHat()

mqttc = paho.Client()
mqttc.on_connect = on_connect

awshost = "data.iot.us-west-2.amazonaws.com"
awsport = 8883
clientId = "rpisensehat-publisher"
thingName = "rpisensehat"
caPath = "rootCA.pem"
certPath = "3b60693e48-certificate.pem.crt"
keyPath = "3b60693e48-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

while True:

    message = {}

    device = {}
    device['cpuTemperature'] = os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C\n","")

    environment = {}

    temp = {}
    temp['basedOnHumidity'] = sense.get_temperature_from_humidity()
    temp['basedOnPressure'] = sense.get_temperature_from_pressure()
  
    environment['humidity'] = sense.get_humidity()
    environment['pressure'] = sense.get_pressure()
    environment['temperature'] = temp

    message['device'] = device
    message['environment'] = environment

    jsonData = json.dumps(message)

    if connflag == True:
        mqttc.publish("environmentData", jsonData, qos=1)
        print jsonData
        sleep(10)
    else:
        print("waiting for connection...")
        sleep(5)
