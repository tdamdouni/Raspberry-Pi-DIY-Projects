from sense_hat import SenseHat
import random
import time
import paho.mqtt.client as paho
from tinydb import TinyDB, Query
import datetime
import json

sense = SenseHat()
sense.set_rotation(180)
db = TinyDB('/home/pi/Documents/Python/daneR.json')

info =''
  
def on_subscribe(client, userdata, mid, granted_qos):
    print('Subscribed')
    
def on_message(client, userdata, msg):
    #print(msg.topic + str(msg.payload))
    global info
    info=str(msg.payload)
    
      
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('192.168.1.150', 1883)    
client.subscribe('/andrzej/sensorki') 

client.loop_start()

while True:     
    try:
        client.loop_start() == True
    except:
        print('no network')
        time.sleep(2)        
    else:  
        time.sleep(5)
        print(info)
        sense.show_message(info, text_colour=[random.randrange(0,150), random.randrange(70,210), random.randrange (50,150)], scroll_speed = 0.1)
        db.insert({'datetime': str(datetime.datetime.now()), "sensor" : str(info)})

    
