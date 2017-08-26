#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import locale
import socket
import sys
import time
from datetime import datetime
import requests
import scrollphat
from Adafruit_IO import Client
from Adafruit_BME280 import *
import logging.handlers

# this is useful for locale string formats
locale.setlocale(locale.LC_TIME, 'de_DE.utf-8')

# read the config file
config_data = open('config.json').read()
config = json.loads(config_data)

# set the configs
FORECAST_IO_KEY = config['FORECAST_IO_KEY']
ADAFRUIT_IO_KEY = config['ADAFRUIT_IO_KEY']
LOG_SIZE = config['LOG_SIZE']
BACKUP_COUNT = config['BACKUP_COUNT']
REFRESH_RATE = config['REFRESH_RATE']

# create a sensor instance for the adafruit BME280
sensor = BME280(mode=BME280_OSAMPLE_8)

# get the host and build a path for the logfile and make the file name individual
host = socket.gethostname()
path = '/home/pi/RPI-Weather-Log/logs/rpi_weather_data_{}.log'.format(host)
LOG_FILENAME = path

# Set up a specific logger with our desired output level
weather_logger = logging.getLogger('WeatherLogger')
weather_logger.setLevel(logging.INFO)

# Add the log message handler to the logger and make a log-rotation of 100 files with max. 10MB per file
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=LOG_SIZE, backupCount=BACKUP_COUNT,)
weather_logger.addHandler(handler)

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

# Every refresh_interval seconds we'll refresh the weather data
pause = 0.1
ticks_per_second = 1 / pause
refresh_interval = 60 * REFRESH_RATE

# reed brightness slider from adafruit io feed
brightness = aio.receive('brightness')
brightness = int(brightness.value)


# get location for weather requests
def get_location():
    location_request_url = 'http://ip-api.com/json'
    location_data = requests.get(location_request_url).json()

    return location_data


# parameter for the request url
base_url = 'https://api.forecast.io/forecast/'  # endpoint for the API
api_key = FORECAST_IO_KEY  # enter your secret API Key in config.json

latitude = get_location()['lat']  # geolocation data for the request url
longitude = get_location()['lon']  # geolocation data for the request url

options = '?lang=de&units=si&exclude=flags'  # some options, see details in API documentation


# build and return the request url
def get_request_url():
    request_url = base_url + api_key + '/' + str(latitude) + ',' + str(longitude) + options  # build it

    return request_url


# create and return a timeout value
def get_timeout():
    return ticks_per_second * refresh_interval


# get timestamp and build a human readable format
def get_timestamp():
    current_time = datetime.now()
    return current_time.isoformat()


# some special german characters need a little love for scroll pHAT
# TODO: I know this is not the best way to do it... but anyway... it works ;)
def translate_umlaute(string_input):

    translations = {  # only if you need...
        'Ö': 'OE',
        'ö': 'oe',
        'Ü': 'UE',
        'ü': 'ue',
        'Ä': 'AE',
        'ä': 'ae',
        'ß': 'ss',
        # etc...
    }

    return string_input.translate(str.maketrans(translations))


# let's get the weather data and build some nice output strings
# TODO: This have to be separated and ordered... split it etc. and get rid of the print for debug (no need anymore)
def get_weather():
    # Get the weather data
    print('Wetterdaten werden aktualisiert')

    # read the sensor data
    sensor_temp = sensor.read_temperature()
    pascals = sensor.read_pressure()
    sensor_pressure = pascals / 100     # hectopascals
    sensor_humidity = sensor.read_humidity()

    # uncomment the next block for debugging

    # get the API Key Calls from header
    # response = requests.get(get_request_url())
    # api_calls = response.headers['X-Forecast-API-Calls']
    # print('API Calls Today: {} of 1000'.format(api_calls))

    data = requests.get(get_request_url()).json()
    print('Requesting Data from: {}\n'.format(get_request_url()))

    location = str(get_location()['city'])
    output_timestamp = str(datetime.fromtimestamp(data['currently']['time']).strftime('%A %H:%M').upper())
    summary = str(data['currently']['summary'])

    temperature = str(int(data['currently']['temperature']))

    timestamp = get_timestamp()

    scroll_output = "{} {}'C ".format(
        translate_umlaute(summary).upper(),
        round(sensor_temp, 1),
    )

    print_output = "{}: {} UHR {} {}'C ".format(
        location,
        output_timestamp,
        summary,
        temperature,
    )

    hourly = data['hourly']['data']
    daily = data['daily']['data']

    forecast_today = daily[0]

    today = 'HEUTE'
    temp_range_today_min = str(int(forecast_today['temperatureMin']))
    temp_range_today_max = str(int(forecast_today['temperatureMax']))
    next_weather_today = str(forecast_today['summary'])

    hourly_forecast = data['hourly']['summary']

    io_str = '{} bis {}°C - {}'.format(
        temp_range_today_min,
        temp_range_today_max,
        hourly_forecast
    )

    forecast_today = 'Die Vorhersage für {}: {} bis {}°C - {}'.format(
        today,
        temp_range_today_min,
        temp_range_today_max,
        next_weather_today,
    )

    print('Das aktuelle Wetter für {}\nDEBUG SCROLL OUTPUT: {}\n{}\n'.format(
        print_output,
        scroll_output,
        forecast_today
        )
    )

    # prints the full 48h forecast; use 'extend=hourly' as option in your request_url to get hourly data for 7 days

    forecast_range_hour = 24  # use len(hourly) for full data (48h)

    print('Das Wetter für die nächsten {} Stunden\n'.format(forecast_range_hour))

    for item in range(forecast_range_hour):
        hour = str(datetime.fromtimestamp(hourly[item]['time']).strftime('%H:%M'))
        next_temp = str(int(hourly[item]['temperature']))
        next_weather = str(hourly[item]['summary'])

        hourly_forecast = '{} {}°C - {}'.format(
            hour,
            next_temp,
            next_weather
        )
        print(hourly_forecast)
    print('\n')

    # prints a short overview of the next 7 days forecast, ordered by day
    forecast_range_day = len(daily)

    # - 1 to reduce the range from today data
    print('Das Wetter für die nächsten {} Tage\n'.format(forecast_range_day - 1))

    # skip the first in the list, cause it's today's data and we've already printed that
    for item in range(forecast_range_day)[1:]:
        day = str(datetime.fromtimestamp(daily[item]['time']).strftime('%a %d.%m.'))
        min_temp = str(int(daily[item]['temperatureMin']))
        max_temp = str(int(daily[item]['temperatureMax']))
        next_weather = str(daily[item]['summary'])

        daily_forecast = '{} {} bis {}°C - {}'.format(
            day,
            min_temp,
            max_temp,
            next_weather
        )
        print(daily_forecast)
    print('\n')

    log_string = '[timestamp={}], [temp_api={}], [sensor_temp={}], [sensor_pressure={}],' \
                 ' [sensor_humidity={}], [summary="{}"], [next_weather_today="{}"],' \
                 ' [latitude={}], [longitude={}], [location={}]'.format(
                    timestamp,
                    temperature,
                    round(sensor_temp, 1),
                    round(sensor_pressure, 1),
                    round(sensor_humidity, 1),
                    summary,
                    io_str,
                    latitude,
                    longitude,
                    location
                    )

    # send some data to adafruit.io
    aio.send('weather', temperature)
    aio.send('forecast', str(summary))
    aio.send('forecast_today', str(io_str))
    aio.send('sensor_temp', round(sensor_temp, 1))
    aio.send('sensor_pressure', round(sensor_pressure, 1))
    aio.send('sensor_humidity', round(sensor_humidity, 1))

    # write log_string to log file
    weather_logger.info(log_string)

    # return the output string for the scroll pHAT
    return scroll_output

# write everything to the scroll pHAT for the first time... than update the data in the loop
timeout = get_timeout()
count = 0
msg = get_weather()
scrollphat.clear()
scrollphat.set_brightness(brightness)  # from 0 to 255
scrollphat.write_string(msg)

# run the loop to print the output to scroll pHAT
# TODO: Learn how this works cause it's creepy shit and could be done better... but it works ;)
while True:
    try:
        scrollphat.scroll()
        time.sleep(pause)

        if count > timeout:
            msg = get_weather()
            scrollphat.clear()
            scrollphat.set_brightness(brightness)  # from 0 to 255
            scrollphat.write_string(msg)
            timeout = get_timeout()
            count = 0

        else:
            count += 1
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
