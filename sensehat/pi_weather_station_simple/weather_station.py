#!/usr/bin/python
'''*****************************************************************************************************************
    Pi Temperature Station
    By John M. Wargo
    www.johnwargo.com

    This is a Raspberry Pi project that measures enviromnment values (temperature and humidity ) using
    the a DHT22 Temperature sensor then uploads the data to a Weather Underground weather station.

    This application uses the Adafruit Python libraries for the DHT22 from:
    https://github.com/adafruit/Adafruit_Python_DHT

    The temperature reading code was shamelesly copied from the example project located at:
    https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/simpletest.py
********************************************************************************************************************'''

from __future__ import print_function

import datetime
import sys
import time
from urllib import urlencode

import Adafruit_DHT
import urllib2

from config import Config

# create the sensor object
# Valid options are 'Adafruit_DHT.DHT11', 'Adafruit_DHT.DHT22', or 'Adafruit_DHT.AM2302'
sensor = Adafruit_DHT.DHT22
# DHT sensor connected to the Raspberry Pi GPIO23.
gpio_pin = 23

# ============================================================================
# Constants
# ============================================================================
# specifies how often to measure values from the Sense HAT (in minutes)
MEASUREMENT_INTERVAL = 10  # minutes
# Set to False when testing the code and/or hardware
# Set to True to enable upload of weather data to Weather Underground
WEATHER_UPLOAD = False
# the weather underground URL used to upload weather data
WU_URL = "http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php"
# some string constants
SINGLE_HASH = "#"
HASHES = "########################################"
SLASH_N = "\n"


def c_to_f(input_temp):
    return (input_temp * 1.8) + 32


def main():
    # initialize the lastMinute variable to the current time to start
    last_minute = datetime.datetime.now().minute
    # on startup, just use the previous minute as lastMinute
    if last_minute == 0:
        last_minute = 59
    else:
        last_minute -= 1
    # infinite loop to continuously check weather values
    while 1:
        # get the current minute
        current_minute = datetime.datetime.now().minute
        # is it the same minute as the last time we checked?
        if current_minute != last_minute:
            # reset last_minute to the current_minute
            last_minute = current_minute
            # is minute zero, or divisible by 10?
            # we're only going to take measurements every MEASUREMENT_INTERVAL minutes
            if (current_minute == 0) or ((current_minute % MEASUREMENT_INTERVAL) == 0):
                # get the reading timestamp
                now = datetime.datetime.now()
                print("\n%d minute mark (%d @ %s)" % (MEASUREMENT_INTERVAL, current_minute, str(now)))

                # ========================================================
                # read the values from the sensor
                # ========================================================
                # Try to grab a sensor reading.  Use the read_retry method which will retry up
                # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
                humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)

                # Note that sometimes you won't get a reading and the results will be null (because Linux can't
                # guarantee the timing of calls to read the sensor). If this happens try again!
                if humidity is not None and temperature is not None:
                    temp_c = round(temperature, 1)
                    temp_f = round(c_to_f(temperature), 1)
                    humidity = round(humidity, 2)
                    print("Temp: %sF (%sC), Humidity: %s%%" % (temp_f, temp_c, humidity))

                    # ========================================================
                    # Upload the weather data to Weather Underground
                    # ========================================================
                    # is weather upload enabled?
                    if WEATHER_UPLOAD:
                        # From http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
                        print("Uploading data to Weather Underground")
                        # build a weather data object
                        weather_data = {
                            "action": "updateraw",
                            "ID": wu_station_id,
                            "PASSWORD": wu_station_key,
                            "dateutc": "now",
                            "tempf": str(temp_f),
                            "humidity": str(humidity)
                        }
                        try:
                            upload_url = WU_URL + "?" + urlencode(weather_data)
                            response = urllib2.urlopen(upload_url)
                            html = response.read()
                            print("Server response:", html)
                            # do something
                            response.close()  # best practice to close the file
                        except:
                            print("Exception:", sys.exc_info()[0], SLASH_N)
                    else:
                        print("Skipping Weather Underground upload")

                else:
                    print('Unable to obtain sensor reading')

        # wait a second then check again
        # You can always increase the sleep value below to check less often
        time.sleep(1)  # this should never happen since the above is an infinite loop

    print("Leaving main()")


# ============================================================================
# here's where we start doing stuff
# ============================================================================
print(SLASH_N + HASHES)
print(SINGLE_HASH, "Pi Weather Station (Simple Sensor)  ", SINGLE_HASH)
print(SINGLE_HASH, "By John M. Wargo (www.johnwargo.com)", SINGLE_HASH)
print(HASHES)

# make sure we don't have a MEASUREMENT_INTERVAL > 60
if (MEASUREMENT_INTERVAL is None) or (MEASUREMENT_INTERVAL > 60):
    print("The application's 'MEASUREMENT_INTERVAL' cannot be empty or greater than 60")
    sys.exit(1)

# ============================================================================
#  Read Weather Underground Configuration Parameters
# ============================================================================
print("\nInitializing Weather Underground configuration")
wu_station_id = Config.STATION_ID
wu_station_key = Config.STATION_KEY
if (wu_station_id is None) or (wu_station_key is None):
    print("Missing values from the Weather Underground configuration file\n")
    sys.exit(1)

# we made it this far, so it must have worked...
print("Successfully read Weather Underground configuration values")
print("Station ID:", wu_station_id)
print("Initialization complete!")

# Now see what we're supposed to do next
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting application\n")
        sys.exit(0)
