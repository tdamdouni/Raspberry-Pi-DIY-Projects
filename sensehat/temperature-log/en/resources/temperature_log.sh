#!/bin/bash

timestamp=`date +%F_%H-%M-%S`
echo "Temperature Log - $(date)" >/home/pi/logs/temperature_log_$timestamp.txt
while :
do
	temp=`/opt/vc/bin/vcgencmd measure_temp`
	temp=${temp:5:16}
	echo $temp >>/home/pi/logs/temperature_log_$timestamp.txt
	sleep 10
done
