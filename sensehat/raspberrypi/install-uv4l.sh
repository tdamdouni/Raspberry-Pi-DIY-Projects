#!/bin/bash
# This script will install UV4L for Raspberry Pi camera

# Get key
wget http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc && sudo apt-key add ./lrkey.asc

# Add repo
sudo bash -c 'echo "deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ wheezy main" >> /etc/apt/sources.list'

# Update firmware
sudo rpi-update

# Install deps
sudo apt-get update
sudo apt-get install -y uv4l uv4l-raspicam uv4l-raspicam-extras uv4l-server

# Start uv4l_raspicam
sudo service uv4l_raspicam start

# View stream
IP=$(hostname -I | rev | cut -c 2- | rev)
echo "You can view your stream by browsing to http://$IP:8080"