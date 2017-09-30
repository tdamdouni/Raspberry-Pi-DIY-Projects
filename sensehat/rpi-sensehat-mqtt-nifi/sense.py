from sense_hat import SenseHat
import json
import paho.mqtt.client as paho
sense = SenseHat() 
sense.clear()
temp = sense.get_temperature()
temp = round(temp, 1)
humidity = sense.get_humidity()
humidity = round(humidity, 1)
pressure = sense.get_pressure()
pressure = round(pressure, 1)
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
row = [ { 'temp': temp, 'tempf': ((temp * 1.8) + 12), 'humidity': humidity, 'pressure': pressure, 'pitch': pitch, 'roll': roll, 'yaw': yaw, 'x': x, 'y': y, 'z': z } ]
json_string = json.dumps(row)
client = paho.Client()
client.username_pw_set("myuser","mypassword")
client.connect("cloudserver", 134324, 60)
client.publish("sensor", payload=json_string, qos=0, retain=True)
