#!/bin/bash

# Raspberry Pi + Raspbian Weather Station
# By Uladzislau Bayouski
# https://www.linkedin.com/in/uladzislau-bayouski-a7474111b/

# How To Autostart Apps In Rasbian LXDE Desktop
# http://www.raspberrypi-spy.co.uk/2014/05/how-to-autostart-apps-in-rasbian-lxde-desktop/

echo "Starting Weather Station"
echo "Process ID: $$"

/usr/bin/python /home/pi/weather_station/weather_station.py