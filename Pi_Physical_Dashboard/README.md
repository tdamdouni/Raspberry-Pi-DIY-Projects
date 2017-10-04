# Raspberry Pi Physical Dashboard

Python code to drive a physical dashboard built with a Raspberry Pi, LED backpacks, and automotive gauges.  See the full guide at: https://learn.adafruit.com/raspberry-pi-physical-dashboard/

## Installation

Perform the following commands on a Pi running Raspbian Jessie to install:

    sudo apt-get update
    sudo apt-get install -y git build-essential python-pip python-smbus
    git clone https://github.com/adafruit/Pi_Physical_Dashboard.git
    cd Pi_Physical_Dashboard
    sudo pip install -r requirements.txt

Modify the config.ini to match your dashboard widget configuration, then run
the main.py script to start the server:

    sudo python main.py
