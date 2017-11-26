import glob
import time
import urllib, urllib2

ALARM_TEMP = 5.0 # degrees C
MIN_T_BETWEEN_WARNINGS = 60 # Minutes
EVENT = 'pipe_alert'
BASE_URL = 'https://maker.ifttt.com/trigger/'
KEY = 'cyR3vPNFlP9K32W4NZB9cd'  # Place your own key here

# These constants used by the 1-wire device
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# Read the temperature message from the device file
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
    
# Split the actual temperature out of the message
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

# Send an IFTTT pipe_alert event
def send_notification(temp):
    print("TEMPERATURE WARNING")
    data = urllib.urlencode({'value1' : str(temp)})
    url = BASE_URL + EVENT + '/with/key/' + KEY
    response = urllib2.urlopen(url=url, data=data)
    print(response.read())


print("Monitoring")
while True:
    temp = read_temp()
    print(temp)
    if temp < ALARM_TEMP:
        send_notification(temp)
        time.sleep(MIN_T_BETWEEN_WARNINGS * 60)