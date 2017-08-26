# RPI-Weather-Log
A complete weather station for the Raspberry Pi, using forecast.io and adafruit sensors to log all weather data to a file 
which can be used for SPLUNK data analysis. I included the scroll pHAT from Pimoroni to display some of the weather data. 
There are also some examples shown who to make some nice outputs with string transformations. Some data is send to 
adafruit.io. perhaps you have to change the feed names and io-data to your individual likings. Read the adafruit.io 
api documentation for more details.

For controlling the adafruit BME280 sensor i added the necessary and lightly modified sensor and I2C driver, to get 
everything setup in python3. so please use python3 to run this.

Feel free to change it in any way you want... Sorry that the output is in german. The forecast.io data are also fetched
in german. You can change it via the options string in the python script. Read the forecast.io api documentation for 
more details.

#### Raspberry Pi Splunk Weather Dashboard
![Raspberry Pi Splunk Weather Dashboard](https://db.tt/tjRKejq3) 

#### [My adafruit.io Weather Dashboard](https://io.adafruit.com/lovebootcaptain/weatherpi#)
![adafruit.io Weather Dashboard](https://db.tt/0fiiqiEH)

## Install

* `cd`
* `git clone https://github.com/LoveBootCaptain/RPI-Weather-Log.git`

## Config

* `cd RPI-Weather-Log`
* `cp config.example.json config.json`
* `sudo nano config.json`
* Replace the `"xxxx..."` with your forecast.io-API-KEY in `"FORECAST_IO_KEY"`.
* Replace the `"xxxx..."` with your Adafruit.io-API-KEY in `"ADAFRUIT_IO_KEY"`.
* Change the size of the log file in `"LOG_SIZE"` (in Bytes). 10MB is default.
* Change the number of log file backups in `"BACKUP_COUNT"`. 100 is default.
* Change the refresh rate of weather data in `"REFRESH_RATE"`. 5min is default.

`CTRL + S` for save and `CTRL + X` for quit

## Make it a linux service

* `sudo chmod +x rpi_weather_log.sh` make the .sh script executable, this will run as service
* `sudo mv rpi_weather_log.sh /etc/init.d/` move the script to /etc/init.d/ so it can be used in CLI

`sudo shutdown -r now` reboot

## Test

To test if everything is set up correctly just try:

* `sudo python3 /home/pi/RPI-Weather_Log/rpi_weather_log.py`

`CTRL + C` to quit

If it works you can also try the service:

* `sudo service rpi_weather_log start` to start
* `sudo service rpi_weather_log stop` to stop
* `sudo service rpi_weather_log restart` to restart
* `sudo service rpi_weather_log status` for status

If everything is working correctly you can run the service on boot with:

* `sudo update-rc.d rpi_weather_log defaults` for enabling start at boot
* `sudo update-rc.d rpi_weather_log remove` for disabling start at boot

## Enjoy

### Credits

* adafruit for great open source code and hardware
* pimoroni for great open source code and hardware
* christian for his great splunk knowledge

### References

* [forecast.io api doc's](https://developer.forecast.io/docs/v2)
* [adafruit.io python api doc's](https://github.com/adafruit/io-client-python)
* [adafruit BME280 python lib](https://github.com/adafruit/Adafruit_Python_BME280)
* [Pimoroni Scroll pHAT python lib](https://github.com/pimoroni/scroll-phat)
* [splunk doc's](http://docs.splunk.com/Documentation)
