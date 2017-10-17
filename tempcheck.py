#!/usr/bin/python

# https://stackoverflow.com/questions/39815791/raspberry-crontab-python-script-at-boot

import os, sys
from subprocess import check_output
from re import findall
from time import sleep, strftime, time

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    temp = float(findall("\d+\.\d+",temp)[0])
    return(temp)

while True:
    log=open("cpu_temp.txt","a")
    temp = get_temp()
    log.write("{0} {1}".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp))+" degreeC\r\n")
    sleep(60)  
    log.close()
