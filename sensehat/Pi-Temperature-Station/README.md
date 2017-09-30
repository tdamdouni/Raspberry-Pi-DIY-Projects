# Pi-Temperature-Station

A Raspberry Pi-based temperature sensing station. The setup uses 2 DS18B20 digital temperature sensor modules and one USB TEMPer sensor. The data is then fed back to Adafruit.io

### Resources

The basic code for the temperature sensing python script was found here: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/overview

Details about including Adafruit.io were found here: https://github.com/adafruit/io-client-python

The drivers for the TEMPer sensor were found here: https://github.com/padelt/temper-python

Information on how to create an Upstart Service was found here: https://stackoverflow.com/questions/17747605/daemon-vs-upstart-for-python-script

### Installation

Install Upstart
`sudo apt-get install upstart`

Follow the Adafruit.io installation instructions

Follow the TEMPer-python installation instructions

Place the temperature sensing python script in the pi user home directory

Place the Adafruit APIkey in a files in the pi user home directory called apikey.txt

Place the thermoservice.conf file in /etc/init

Reboot the Pi
