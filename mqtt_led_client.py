#!/usr/bin/env python

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def on_connect(client, userdata, rc):
    #print ("Connected with rc: " + str(rc))
    client.subscribe("kwf/demo/led")

def on_message(client, userdata, msg):
    #print ("Topic: "+ msg.topic+"\nMessage: "+str(msg.payload))
    if "green" in msg.payload:
        #print("  Green on!")
        GPIO.output(11, True)
    else:
        #print("  Green off!")
        GPIO.output(11, False)
    if "yellow" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(12, True)
    else:
        #print("  Yellow off!")
        GPIO.output(12, False)
    if "red" in msg.payload:
        #print("  Red on!")
        GPIO.output(13, True)
    else:
        #print("  Red off!")
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
