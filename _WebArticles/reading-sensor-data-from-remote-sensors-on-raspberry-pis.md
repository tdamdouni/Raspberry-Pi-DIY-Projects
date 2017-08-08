# Reading Sensor Data from Remote Sensors on Raspberry Pis

_Captured: 2017-03-15 at 00:33 from [community.hortonworks.com](https://community.hortonworks.com/content/kbentry/55839/reading-sensor-data-from-remote-sensors-on-raspber.html)_

**Sensor Reading with Apache NiFi 1.0.0**

There are many types of sensors, devices and meters that can be great sources of data. Some can push data, some can pull data, some provide APIs, some give you access to install software.

**How To Access Sensors**

One option is to install [MiNiFi](https://cwiki.apache.org/confluence/display/NIFI/MiNiFi) on the device if you have **root **access. This will provide fast access to allow you to script and manage your local data. Another option for bigger devices is to install a full Java based [NiFi](https://nifi.apache.org/) node.

It starts becoming harder once you have tens of thousands of devices. You can install an HDF Edge and communicate from this node to your HDF cluster via [Site-to-Site](http://docs.hortonworks.com/HDPDocuments/HDF1/HDF-1.2.0.1/bk_UserGuide/content/site-to-site.html) protocol. From this Edge Node that acts as an accumulator for many devices (a good idea so that you don't send 10,000 network requests a second from each set of devices, keep as much traffic locally to save time, time-outs, networking and cloud costs). You can also now aggregate and send larger batches of data and also process some summaries and aggregates locally in NiFi. This will also let you populate local databases, dashboards and statistics that may only be of interest to the local source of the sensors (perhaps a plant manager or automated monitoring system).

Another option is to have devices push or pull to a local or remote NiFi install via various protocols including TCP/IP, UDP/IP, REST HTTP, JMS, MQTT, SFTP and Email.

**Device Push to NiFi**

Your device can send messages to NiFi via any number of [protocols](https://nifi.apache.org/docs.html) listed. For my example, I push via MQTT. My local NiFi node will consume these messages via [ConsumeMQTT](https://nifi.apache.org/docs/nifi-docs/components/org.apache.nifi.processors.mqtt.ConsumeMQTT/index.html).

![](https://community.hortonworks.com/storage/attachments/7527-mqtt6.png)

Your device will need to run Linux (or something related), have Python 2.7 or better and PiP installed. With Pip, you can install the Eclipse library that you need to send MQTT messages. **pip install paho-mqtt**
    
          1. import paho.mqtt.client as paho
      2. client = paho.Client()
      3. client.connect("servername", 1883, 60)
      4. client.publish("sensor", payload="Test", qos=0, retain=True)

Where "**servername" **is the name of the server you are sending the message to (it could also be on the NiFi Node, another server, a bigger device, a central aggregator or messaging server). I would recommend having it as close in the network as possible. **"sensor"** is the name of the topic that we are publishing the message to, NiFi will consume this message. I have cron job setup to run every minute and publish messages **(* * * * * /opt/demo/sendit.sh** )

**NiFi Poll Device**

NiFi can poll your device and consume from various protocols like JMS, MQTT, SFTP, TCP and UDP. For my example, I chose a REST API over HTTP to get past hurdles of firewalls and such.

I setup a Flask Server on RPI, to run my REST API, I run this in a shell script.
    
          1. flask run --host=0.0.0.0 --port=8888 --no-debugger

To install [Flask](http://mattrichardson.com/Raspberry-Pi-Flask/), you need to run** pip install flask**

**Sensor Reading Code**
    
          1. from flask import Flask, jsonify
      2. import paho.mqtt.client as paho
      3. sense.clear()
      4. app = Flask(__name__)
      5. @app.route('/pi/api/v1.0/sensors', methods=['GET'])
      6.        	p = subprocess.Popen(['/opt/vc/bin/vcgencmd','measure_temp'], stdout=subprocess.PIPE,
      7.                                     stderr=subprocess.PIPE)
      8. out, err = p.communicate()
      9.        	temp = sense.get_temperature()
      10.        	temp = round(temp, 1)
      11.        	temph = sense.get_temperature_from_humidity()
      12.         temph = round(temph, 1)
      13.         tempp = sense.get_temperature_from_pressure()
      14.         tempp = round(tempp, 1)
      15.        	humidity = sense.get_humidity()
      16.        	humidity = round(humidity, 1)
      17.        	pressure = sense.get_pressure()
      18.        	pressure = round(pressure, 1)
      19.        	tasks = [ { 'tempp': tempp, 'temph': temph, 'cputemp': out, 'temp': temp, 'tempf': ((temp * 1.8) + 12), 'humidity': humidity, 'pressure': pressure } ]
      20. # As an option we can push this message when we get called as well
      21.      	client = paho.Client()
      22.       	client.connect("mqttmessageserver", 1883, 60)
      23.      	client.publish("sensor", payload=jsonify({'readings': tasks}), qos=0, retain=True)
      24. return jsonify({'readings': tasks})
      25. @app.route('/pi/api/v1.0/location', methods=['GET'])
      26.        	orientation = sense.get_orientation()
      27.         pitch = orientation['pitch']
      28.         roll = orientation['roll']
      29.         yaw = orientation['yaw']
      30.         acceleration = sense.get_accelerometer_raw()
      31.        	x = acceleration['x']
      32.        	y = acceleration['y']
      33.        	z = acceleration['z']
      34.        	x=round(x, 0)
      35.        	y=round(y, 0)
      36.        	z=round(z, 0)
      37.        	tasks = [ { 'pitch': pitch, 'roll': roll, 'yaw': yaw, 'x': x, 'y': y, 'z': z } ]
      38. return jsonify({'readings': tasks})
      39. @app.route('/pi/api/v1.0/show', methods=['GET'])
      40.        	temp = sense.get_temperature()
      41.        	temp = round(temp, 1)
      42.        	humidity = sense.get_humidity()
      43.        	humidity = round(humidity, 1)
      44.        	pressure = sense.get_pressure()
      45.        	pressure = round(pressure, 1)
      46.         sense.clear()
      47.         info = 'T(C): ' + str(temp) + 'H: ' + str(humidity) + 'P: ' + str(pressure)
      48.         sense.show_message(info, text_colour=[255, 0, 0])
      49.        	sense.clear()
      50.        	tasks = [ { 'temp': temp, 'tempf': ((temp * 1.8) + 12), 'humidity': humidity, 'pressure': pressure } ]
      51. return jsonify({'readings': tasks})
      52. if __name__ == '__main__':
      53.     app.run(debug=True)

The device I am testing is a [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) with a [Sense Hat sensor attachment](https://www.raspberrypi.org/learning/getting-started-with-the-sense-hat/worksheet/). Besides having sensors for temperature, humidity and barometric pressures it also has a 8x8 light grid for displaying text and simple graphics. We can use this to print messages (**sense.show_message**) or warnings that we send from NiFi. This allows for 2 way very visceral communication to remote devices. This could be used to notify local personnel of conditions.

![](https://community.hortonworks.com/storage/attachments/7521-mqtt5.jpeg)

**nifi 1.0.0 Flows**

![](https://community.hortonworks.com/storage/attachments/7522-mqtt1.png)

![](https://community.hortonworks.com/storage/attachments/7523-mqtt3.png)

![](https://community.hortonworks.com/storage/attachments/7524-mqtt5.png)

![](https://community.hortonworks.com/storage/attachments/7526-mqtt2.png)

> _JSON File Landed in HDFS in our HDP 2.5 Cluster_
    
          1. [root@myserverhdp sensors]# hdfs dfs -ls /sensor
      2. -rw-r--r--   3 root hdfs        202 2016-09-09 17:26 /sensor/181528179026826
      3. drwxr-xr-x   - hdfs hdfs          0 2016-09-09 15:43 /sensor/failure
      4. [root@tspanndev13 sensors]# hdfs dfs -cat /sensor/181528179026826
      5. "cputemp": "temp=55.8'C\n",

![](https://community.hortonworks.com/storage/attachments/7525-mqtt4.png)

The final results of our flow is a JSON file on HDFS. We could easily send a copy of the data to Phoenix via **PutSQL** or to Hive via **PutHiveQL** or to Spark Streaming for additional processing via Site-To-Site or Kafka.

**Resources:**

<https://www.raspberrypi.org/learning/sense-hat-data-logger/worksheet>/

<https://www.raspberrypi.org/learning/astro-pi-flight-data-analysis/worksheet>/

<https://breadfit.wordpress.com/2015/06/24/installing-mosquitto-under-centos>/
