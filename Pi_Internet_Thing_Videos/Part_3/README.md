# Raspberry Pi Internet 'Thing' Part 3 Code

This is a simple [flask](http://flask.pocoo.org/) web application that prints the current state of the switch, has a button to turn on/off the LED, and displays
a dynamically updating chart of temperature and humidity data.

## Hardware

Setup the Raspberry Pi with an LED connected to pin 23 (LED anode/longer leg connected to pin 23, then cathode/shorter leg connect through a ~560 ohm resistor to ground).  Also connect a slide switch (or just move wires manually) with its output (middle pin) connected to pin 24 and one of its other pins connected to ground and the other 3.3V.

In addition you will need a DHT temperature sensor connected to pin 18 (and power
connected to Pi 3.V, ground connected to Pi ground).  See this guide for more
information on using a DHT sensor with the Pi: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview

## Requirements

    sudo apt-get update
    sudo apt-get install -y python-pip python-dev python-smbus build-essential git
    sudo pip install flask
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    cd Adafruit_Python_DHT
    sudo python setup.py install

## Running (manually)

    cd webapp
    sudo python main.py

Open browser and access [http://raspberrypi:5000/](http://raspberrypi:5000/).

## Running (automatically with systemd)

Do this one time setup to create and enable the systemd service.

    sudo cp pi_thing.service /lib/systemd/system/
    sudo systemctl enable pi_thing

Now reboot and the pi thing webapp should automatically run after boot.  You can manually stop it with:

    sudo systemctl stop pi_thing

Start it with:

    sudo systemctl start pi_thing

And check its status with:

    sudo systemctl status pi_thing
