#!/bin/bash
# This script will install the Raspberry Pi camera compatible MJPG-Streamer

# Install deps
sudo apt-get install -y libjpeg8-dev cmake

# Download mjpg-streamer with raspicam plugin
git clone https://github.com/jacksonliam/mjpg-streamer.git ~/mjpg-streamer

# Change directory
cd ~/mjpg-streamer/mjpg-streamer-experimental

# Compile
make clean all

# Install
sudo cp mjpg_streamer /usr/local/bin
sudo cp input_raspicam.so output_http.so /usr/local/lib
sudo cp www/stream_simple.html /var/www/index.html

# Begin streaming
/usr/local/bin/./mjpg_streamer -i "/usr/local/lib/input_raspicam.so -fps 15 -q 75 -x 1440 -y 1280 -vf -hf" -o "/usr/local/lib/output_http.so -p 9000 -w /var/www" &

# View stream
IP=$(hostname -I | rev | cut -c 2- | rev)
echo "You can view your stream by browsing to http://$IP:9000"