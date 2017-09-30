#!flask/bin/python
from flask import Flask, jsonify
import sys
import time
import datetime
import subprocess
import sys
import urllib2
import json
import paho.mqtt.client as paho
from sense_hat import SenseHat
 
sense = SenseHat()
sense.clear()
 
app = Flask(__name__)
 
@app.route('/pi/api/v1.0/sensors', methods=['GET'])
def get_sensors():
       	p = subprocess.Popen(['/opt/vc/bin/vcgencmd','measure_temp'], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
       	out, err = p.communicate()
       	temp = sense.get_temperature()
       	temp = round(temp, 1)
       	temph = sense.get_temperature_from_humidity()
        temph = round(temph, 1)
        tempp = sense.get_temperature_from_pressure()
        tempp = round(tempp, 1)
       	humidity = sense.get_humidity()
       	humidity = round(humidity, 1)
       	pressure = sense.get_pressure()
       	pressure = round(pressure, 1)
       	tasks = [ { 'tempp': tempp, 'temph': temph, 'cputemp': out, 'temp': temp, 'tempf': ((temp * 1.8) + 12), 'humidity': humidity, 'pressure': pressure } ]
 
# As an option we can push this message when we get called as well
     	client = paho.Client()
      	client.connect("mqttmessageserver", 1883, 60)
     	client.publish("sensor", payload=jsonify({'readings': tasks}), qos=0, retain=True)
       	return jsonify({'readings': tasks})
 
@app.route('/pi/api/v1.0/location', methods=['GET'])
def get_loc():
       	orientation = sense.get_orientation()
        pitch = orientation['pitch']
        roll = orientation['roll']
        yaw = orientation['yaw']
        acceleration = sense.get_accelerometer_raw()
       	x = acceleration['x']
       	y = acceleration['y']
       	z = acceleration['z']
       	x=round(x, 0)
       	y=round(y, 0)
       	z=round(z, 0)
       	tasks = [ { 'pitch': pitch, 'roll': roll, 'yaw': yaw, 'x': x, 'y': y, 'z': z } ]
       	return jsonify({'readings': tasks})
 
@app.route('/pi/api/v1.0/show', methods=['GET'])
def get_pi():
       	temp = sense.get_temperature()
       	temp = round(temp, 1)
       	humidity = sense.get_humidity()
       	humidity = round(humidity, 1)
       	pressure = sense.get_pressure()
       	pressure = round(pressure, 1)
       	# 8x8 RGB
        sense.clear()
        info = 'T(C): ' + str(temp) + 'H: ' + str(humidity) + 'P: ' + str(pressure)
        sense.show_message(info, text_colour=[255, 0, 0])
       	sense.clear()
       	tasks = [ { 'temp': temp, 'tempf': ((temp * 1.8) + 12), 'humidity': humidity, 'pressure': pressure } ]
       	return jsonify({'readings': tasks})
 
if __name__ == '__main__':
    app.run(debug=True)
