#!/bin/bash

# Get various system parameters

# 1. CPU Temperature in 1/1000's degree C
cputemp=$( cat /sys/devices/virtual/thermal/thermal_zone0/temp )

# 2. Uptime in Seconds
up=$( cat /proc/uptime ) ;# Get uptime values in seconds
uptime=${up%%\.*} ;# Remove all except the integer part of the first value

# 3. Memory
meminfo=$( free | sed -n "s/^Mem: *[0-9]* *\([0-9]*\) *\([0-9]*\) .*$/memused=\1\&memfree=\2/p" )

# Add any more values here..

# Push to server
wget -q "http://myserver.com/temp.php?temp=$cputemp&uptime=$uptime"

# Reboot

if [ "$( wget -q -O - http://myserver.com/reboot.php )" = "reboot" ]
then
  sudo /sbin/reboot
fi