import paho.mqtt.client as paho
from threading import Timer
from subprocess import Popen, PIPE
import re,time,logging,json

import config

last_tx = -1
last_rx = -1
mac_filter = []
interval_timer = None

def on_connect(mosq, obj, rc):
	logging.info("Connect with RC " + str(rc))

def on_disconnect(client, userdata, rc):
	logging.warning("Disconnected (RC " + str(rc) + ")")
	if rc <> 0:
		try_reconnect(client)

def on_log(client, userdata, level, buf):
	logging.debug(buf)

# MQTT reconnect
def try_reconnect(client, time = 60):
	try:
		logging.info("Trying reconnect")
		client.reconnect()
	except:
		logging.warning("Reconnect failed. Trying again in " + str(time) + " seconds")
		Timer(time, try_reconnect, [client]).start()

def run():
	global interval_timer
	interval_timer = Timer(config.interval, run)
	interval_timer.start()
	publishBandwidth()
	publishLeases()
	

def publishLeases():
	leases_raw = Popen(["ssh", "-i", config.ssh_key, "root@192.168.0.1", "cat /tmp/dnsmasq.leases"], stdout=PIPE, stderr=PIPE).stdout.read()
	leases = leases_raw.strip().split("\n")
	leases = [lease.split()[1] for lease in leases]
	leases = list(set(leases) - set(mac_filter))
	mqttc.publish(config.base_topic + "devices", len(leases), 0, False)
	

def publishBandwidth():
	global last_rx,last_tx
	ifconfig = Popen(["ssh", "-i", config.ssh_key, "root@192.168.0.1", "ifconfig vlan1"], stdout=PIPE, stderr=PIPE).stdout.read()
	rx_bytes = int(re.findall('RX bytes:([0-9]*) ', ifconfig)[0])
	tx_bytes = int(re.findall('TX bytes:([0-9]*) ', ifconfig)[0])
	if last_rx >=0 and last_tx >= 0:
		rx_rate = (rx_bytes - last_rx)/(config.interval * 1024.0)
		tx_rate = (tx_bytes - last_tx)/(config.interval * 1024.0)
		bandwidth = { "rx" : round(rx_rate,2), "tx" : round(tx_rate,2) } 
		mqttc.publish(config.base_topic + "bandwidth", json.dumps(bandwidth), 0, False)
	last_rx = rx_bytes
	last_tx = tx_bytes

logging.basicConfig(format='[%(levelname)s] %(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

# initialize MQTT
logging.info("Initializing MQTT")
mqttc = paho.Client()
mqttc.username_pw_set(config.broker["user"], config.broker["password"])
mqttc.connect(config.broker["hostname"], config.broker["port"], 60)
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_log = on_log

logging.info("Read MAC filter file")

with open(config.mac_filter) as f:
    for line in f:
        line = line.partition('#')[0]
        line = line.rstrip().lower()
        mac_filter.append(line)

run()

# Loop forever
logging.info("Entering loop")
mqttc.loop_forever()

interval_timer.cancel()

# Clean up afterwards
logging.info("Cleanup")
mqttc.disconnect()
