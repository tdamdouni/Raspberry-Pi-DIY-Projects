#!/bin/bash

echo "downloading Pimoroni Unicorn HAT HD installer..."
curl https://get.pimoroni.com/unicornhathd | bash
echo "installer completed, getting Unicontrol frontend..."
git clone https://github.com/flash76/Unicontrol.git
echo "getting server framework..."
sudo apt-get install apache2
echo "installing dependencies..."
sudo apt-get install python python3-pip
pip3 install flask
echo "finalising install..."
mv ledsetting /var/www/html
mv bower.json /var/www/html
mv index.html /var/www/html
mv LICENSE /var/www/html
mv material.css /var/www/html
mv material.js /var/www/html
mv material.min.css /var/www/html
mv material.min.css.map /var/www/html
mv material.min.js /var/www/html
mv material.min.js /var/www/html
mv package.json /var/www/html
mv welcome_card_unicontrol.png /var/www/html
cd /var/www/html
mkdir ledsetting
mv led.html ledsetting
cd ledsetting
mv led.html index.html
