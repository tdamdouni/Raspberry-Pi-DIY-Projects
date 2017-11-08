#!/bin/bash

# chmod +x my-pi-temp.sh

# ./my-pi-temp.sh

temp=`cat /sys/class/thermal/thermal_zone0/temp`

echo "CPU Temperature: $(($temp/1000)) C = $(($temp/1000*9/5+32))F"

#!/bin/bash
# Script: my-pi-temp.sh
# Purpose: Display the ARM CPU and GPU  temperature of Raspberry Pi 2/3 
# Author: Vivek Gite  under GPL v2.x+
# -------------------------------------------------------
cpu=$(/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU => $((cpu/1000))'C"