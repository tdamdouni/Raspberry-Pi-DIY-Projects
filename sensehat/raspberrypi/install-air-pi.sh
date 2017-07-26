#!/bin/bash
# This script will install the Shairport Airplay emulator for Raspberry Pi

# Install deps
sudo apt-get install -y git libao-dev libssl-dev libcrypt-openssl-rsa-perl libio-socket-inet6-perl libwww-perl avahi-utils libmodule-build-perl libavahi-client-dev libasound2-dev libpulse-dev

# Install perl net sdp
git clone https://github.com/njh/perl-net-sdp.git perl-net-sdp
cd perl-net-sdp
perl Build.PL
sudo ./Build
sudo ./Build test
sudo ./Build install
cd ~

# Install shairport
git clone git@github.com:abrasive/shairport.git
cd shairport
./configure
make

# Optionally install it to run at boot
sudo make install
cp shairport.init.sample /etc/init.d/shairport
cd /etc/init.d
chmod a+x shairport
update-rc.d shairport defaults
echo "change DAEMON_ARGS to -w \$PIDFILE -a AirPi"
read -p "Press any key to continue..."
sudo nano shairport


# Start up Airplay
./shairport -a AirPi &

echo "Airplay started as device: AirPi"