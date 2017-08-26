#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

#Author: Callum Pritchard, Joachim Hummel
#Project Name: Scroll-Phat
#Project Description: Getting data from MQTT and displaying it on the scroll-phat
#Version Number: 0.5
#Date: 10/5/17
#Release State: Beta testing
#Changes: Changed the replace to a range to output as to avoide replacing the letter B

#needed commands
#pip3 install paho-mqtt
#curl https://get.pimoroni.com/scrollphat | bash

import paho.mqtt.client as mqtt  
import time
import scrollphat

global output
output = ''

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " +str(rc))
    client.subscribe('#')

def on_message(client, userdata, msg):  #triggers on an update
    scrollphat.clear()
    global output
    if  str(msg.topic) == 'msg/sensor1':  #name of the publisher
        print(str(msg.payload)[2:len(str(msg.payload))-1])
        output = str(msg.payload)[2:len(str(msg.payload))-1] + '   '
        #since the loop cannot be here, the text needs to looped in itself so it can be displayed
        #until a new value is sent via mqtt
        
scrollphat.set_rotate(True)
scrollphat.set_brightness(2)

client = mqtt.Client()
client.connect("mqtt.unixweb.de",1883,60)  #connects to the broker
client.on_connect = on_connect
client.on_message = on_message

while True:
    client.loop()        
    scrollphat.write_string(output, 11)  #writes to display starting at position 11 on x axis
    for i in range(len(output) + 3):
        scrollphat.scroll() #initiates the scrolling
        time.sleep(0.1)    
    
    
    
