#!/bin/bash

# Install Packages
sudo apt-get install bluez python-gobject dbus-glib -y
sudo aptitude install blueman -y

# Initialize Raspberry Pi Bluetooth USB Dongle and scan for devices
sudo service bluetooth restart
sudo service bluetooth status
/etc/init.d/bluetooth status
lsusb | grep -i bluetooth
sudo hciconfig hci0 reset
sudo hciconfig hci0 piscan
hcitool scan
bluetoothctl
