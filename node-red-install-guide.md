# Setting up Node.js on Raspberry PI

sudo apt-get update
sudo apt-get upgrade
sudo wget http://node-arm.herokuapp.com/node_latest_armhf.deb
sudo dpkg -i node_latest_armhf.deb
node -v

# Setting up Node-Red on RPI

1. Install Git for future commits

sudo apt-get install git-core

2. Access Home Directory

cd ~

3. Download Node-Red

git clone https://github.com/node-red/node-red.git

4. Install Node-Red

cd node-red
sudo npm install

5.

sudo node red.js

6.

http://Pi-IP-Address:1880
