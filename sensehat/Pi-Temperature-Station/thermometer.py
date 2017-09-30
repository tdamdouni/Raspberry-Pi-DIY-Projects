#!/usr/bin/env python

import os
import os.path
import glob
import time
from subprocess import *

#Read the Adafruit API key in from file /home/pi/apikey.txt.
file = open('/home/pi/apikey.txt', 'r')
apikey = file.readline().replace("\n", '')
file.close()

# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client(apikey)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

device_folder = []
device_file = []

base_dir = '/sys/bus/w1/devices/'
device_folder.append(glob.glob(base_dir + '28*')[0])
device_file.append(device_folder[0] + '/w1_slave')
device_folder.append(glob.glob(base_dir + '28*')[1])
device_file.append(device_folder[1] + '/w1_slave')
print('Device File 0:', device_file[0])
print('Device File 1:', device_file[1])

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def get_usb_temp():
    usbtemp_str= run_cmd("temper-poll | grep 'Device'  | awk '{print $3}' | cut -c 1-4")
    #print('usbtemp_str: ', usbtemp_str)
    if usbtemp_str != "":
        usbtemp = float(usbtemp_str) - 8
        return usbtemp
    else: return False

def readTempGPIO(index):
    lines = readRawTempGPIO(index)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readRawTempGPIO(index)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    else: return False
    
def readRawTempGPIO(index):
    f = open(device_file[index], 'r')
    lines = f.readlines()
    f.close()
    return lines
    
def readTemps(index):
    
    if index != 2:
       temp = readTempGPIO(index)
    else: temp = get_usb_temp()
    
    return temp

while True:
        
        tempList = [None, None, None]
        temps = []
        #data = []
        
        for index, temp in enumerate(tempList):
            tempList[index] = readTemps(index)
            
            if tempList[index] != False:
                print('Sensor ', index, ' temp: ',tempList[index])
                temps.append(tempList[index])
                
        temp = sum(tempList)/len(tempList)
        
        aio.send('temperature', '%.3f'%temp)
        value = aio.receive('temperature')
        print('Received value: {0}'.format(value.value))
        
        time.sleep(10)