# Raspberry Pi Internet 'Thing' Part 1 Code

This is a simple [flask](http://flask.pocoo.org/) web application that prints the current state of the switch and has a button to turn on/off the LED.

## Hardware

Setup the Raspberry Pi with an LED connected to pin 23 (LED anode/longer leg connected to pin 23, then cathode/shorter leg connect through a ~560 ohm resistor to ground).  Also connect a slide switch (or just move wires manually) with its output (middle pin) connected to pin 24 and one of its other pins connected to ground and the other 3.3V.

## Requirements

    sudo apt-get update
    sudo apt-get install -y python-pip python-dev
    sudo pip install flask

## Running (manually)

    cd webapp
    python main.py

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
