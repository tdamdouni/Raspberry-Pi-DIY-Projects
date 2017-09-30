# Pi-Web-Status-Display
A Raspberry Pi-based project for tracking and displaying certain network metrics.

Currently the system keeps track of the:

- WAN address
- Ping time to 8.8.8.8
- Min Ping
- Average Ping
- Max Ping

THe metrics are then displayed on an HDD44780 compatible LCD and through Adafruit.io

### Installing the display script
- Follow the Adafruit installation guide for wiring and testing out the display
- Clone this repository into the pi users home directory
- make sure that the three python scripts are executable (`sudo chmod +x WAN_ping_display.py temperature.py highping.py`)
- Place the Adafruit APIkey in a file called apikey.txt in the repo directory
- Place the OpenWeatherMap API key in a file called weatherapikey.txt in the repo directory 
- Install Upstart with: `sudo apt-get install upstart`
- Place the networktestservice.conf file in /etc/init
- Reboot the Pi

#### Installing the calculation script

Create a cron job: `crontab-e`

Add a line at the bottom of the file similar to this: `* */24 * * * python /home/pi/ping_calculations.py`

Make sure to replace `/home/pi/ping_calculations.py` with the full location and name of the `ping_calculations.py` file 


### Resources
THe main reference for this project was the Adafruit LCD guide: https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/overview

The python code used to drive the diaplay uses Adafruits LCD library. For a combination of reasons (could be the older Pi being used, or the more obscure 20x4 LCD) the legacy branch of the older LCD library was what I managed to get working on my screen: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/legacy

Information on how to create an Upstart Service was found here: https://stackoverflow.com/questions/17747605/daemon-vs-upstart-for-python-script

Details about including Adafruit.io were found here: https://github.com/adafruit/io-client-python





