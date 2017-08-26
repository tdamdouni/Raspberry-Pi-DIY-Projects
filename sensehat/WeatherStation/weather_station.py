#!/usr/bin/python
'''*****************************************************************************************************************
    Raspberry Pi + Raspbian Weather Station
    By Uladzislau Bayouski
    https://www.linkedin.com/in/uladzislau-bayouski-a7474111b/

    A Raspberry Pi based weather station that measures temperature, humidity and pressure using
    the Astro Pi Sense HAT then uploads the data to a Weather Underground weather station.
    Calculates dew point. Completely configurable and working asyncroniously in multi threads. 
    Uses stick for choosing different weather entities and visual styles. 
    Uses logger to log runtime issues/errors.
    
    Inspired by http://makezine.com/projects/raspberry-pi-weather-station-mount/ project
********************************************************************************************************************'''
from __future__ import print_function
from collections import deque
from sense_hat import SenseHat, ACTION_RELEASED, DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT
from threading import Timer
from urllib import urlencode

import datetime
import logging 
import os
import signal
import sys
import time
import urllib2

from config import Config
from weather_entities import DEFAULT_WEATHER_ENTITIES, CarouselContainer, WeatherEntityType

class WeatherStation(CarouselContainer):
    """Weather Station controlling class, setups and manages station run time."""

    # Constants
    SMOOTH_READINGS_NUMBER = 3
    READINGS_PRINT_TEMPLATE = 'Temp: %sC (%sF), Humidity: %s%%, Pressure: %s inHg'

    def __init__(self):
        super(WeatherStation, self).__init__()

        self._sense_hat = None
        self._log_timer = None
        self._upload_timer = None
        self._update_timer = None
        self._last_readings = None

    @property
    def carousel_items(self):
        return DEFAULT_WEATHER_ENTITIES

    @property
    def current_style(self):
        return self.current_item.current_style

    def activate_sensors(self):
        """Activates sensors by requesting first values and assigning handlers."""
        self._sense_hat = SenseHat()

        # Scroll Init message over HAT screen
        self._show_message('Init Sensors', (255, 255, 0), (0, 0, 255))

        # Init sensors, to be sure first effective run uses correct sensors values
        self._sense_hat.get_humidity()
        self._sense_hat.get_pressure()

        # Setup Sense Hat stick
        self._sense_hat.stick.direction_up = self._change_weather_entity
        self._sense_hat.stick.direction_down = self._change_weather_entity
        self._sense_hat.stick.direction_left = self._change_weather_entity
        self._sense_hat.stick.direction_right = self._change_weather_entity
    
    def start_station(self):
        """Launches multiple threads to handle configured behavior."""
        if Config.LOG_TO_CONSOLE and Config.LOG_INTERVAL:
            self._log_results(first_time=True)

        if Config.WEATHER_UPLOAD and Config.UPLOAD_INTERVAL:
            self._upload_results(first_time=True)

        if Config.UPDATE_DISPLAY and Config.UPDATE_INTERVAL:
            self._update_display()

    def stop_station(self):
        """Tries to stop active threads and clean up screen."""
        if self._sense_hat:
            self._sense_hat.clear()

        if self._log_timer:
            self._log_timer.cancel()

        if self._upload_timer:
            self._upload_timer.cancel()

        if self._update_timer:
            self._update_timer.cancel()

    @staticmethod
    def to_fahrenheit(value):
        """Converts celsius temperature to fahrenheit."""
        return (value * 1.8) + 32

    @staticmethod
    def calculate_dew_point(temp, hum):
        """
        Calculates dewpoint in celsius, uses simplified formula less accurate but obvious.
        https://en.wikipedia.org/wiki/Dew_point#Calculating_the_dew_point
        """
        return temp - (100 - hum) / 5

    def get_temperature(self):
        """
        Gets temperature and adjusts it with environmental impacts (like cpu temperature).
                
        There are some issues, getting an accurate temperature reading from the
        Sense HAT is improbable, see here:
        https://www.raspberrypi.org/forums/viewtopic.php?f=104&t=111457
        We need to take CPU temp into account. The Pi foundation recommendeds using the following:
        http://yaab-arduino.blogspot.co.uk/2016/08/accurate-temperature-reading-sensehat.html        
        """
        
        # Get temp readings from both sensors
        humidity_temp = self._sense_hat.get_temperature_from_humidity()
        pressure_temp = self._sense_hat.get_temperature_from_pressure()
        
        # avg_temp becomes the average of the temperatures from both sensors
        # We need to check for pressure_temp value is not 0, to not ruin avg_temp calculation
        avg_temp = (humidity_temp + pressure_temp) / 2 if pressure_temp else humidity_temp
        
        # Get the CPU temperature
        cpu_temp = self._get_cpu_temp()
        
        # Calculate temperature compensating for CPU heating
        adj_temp = avg_temp - (cpu_temp - avg_temp) / 1.5
        
        # Average out value across the last three readings
        return self._get_smooth(adj_temp)

    def get_humidity(self):
        """Gets humidity sensor value."""
        return self._sense_hat.get_humidity()

    def get_pressure(self):
        """Gets humidity sensor value and converts pressure from millibars to inHg before posting."""
        return self._sense_hat.get_pressure() * 0.0295300
    
    def get_sensors_data(self):
        """Returns sensors data tuple."""

        temp_in_celsius = self.get_temperature()

        return (
            round(temp_in_celsius, 1), 
            round(self.to_fahrenheit(temp_in_celsius), 1), 
            round(self.get_humidity(), 0), 
            round(self.get_pressure(), 1)
        )    

    def _change_weather_entity(self, event):
        """Internal. Switches to next/previous weather entity or next/previous visual style."""
        
        # We need to handle release event state
        if event.action == ACTION_RELEASED:
            self._sense_hat.clear()

            if event.direction == DIRECTION_UP:
                next_entity = self.next_item
                self._show_message(next_entity.entity_messsage, next_entity.positive_color)
            elif event.direction == DIRECTION_DOWN:
                previous_entity = self.previous_item
                self._show_message(previous_entity.entity_messsage, previous_entity.positive_color)
            elif event.direction == DIRECTION_LEFT:
                self.current_item.previous_item
            else:
                self.current_item.next_item

            self._update_display(loop=False)

    def _show_message(self, message, message_color, background_color=(0, 0, 0)):
        """Internal. Shows message by scrolling it over HAT screen."""

        # Need to be sure we revert any changes to rotation
        self._sense_hat.rotation = 0
        self._sense_hat.show_message(message, Config.SCROLL_TEXT_SPEED, message_color, background_color)
    
    def _log_results(self, first_time=False):
        """Internal. Continuously logs sensors values."""

        if not first_time:
            print(self.READINGS_PRINT_TEMPLATE % self.get_sensors_data())

        self._log_timer = self._start_timer(Config.LOG_INTERVAL, self._log_results)

    def _update_display(self, loop=True):
        """Internal. Continuously updates screen with new sensors values."""

        sensors_data = self.get_sensors_data()

        if self.current_item.entity_type is WeatherEntityType.TEMPERATURE:
            pixels = self.current_item.show_pixels(sensors_data[0])
        elif self.current_item.entity_type is WeatherEntityType.HUMIDITY:
            pixels = self.current_item.show_pixels(sensors_data[2])
        else:
            pixels = self.current_item.show_pixels(sensors_data[3])

        self._sense_hat.set_rotation(self.current_style.rotation)
        self._sense_hat.set_pixels(pixels)

        if loop:
            self._update_timer = self._start_timer(Config.UPDATE_INTERVAL, self._update_display)

    def _upload_results(self, first_time=False):
        """Internal. Continuously uploads new sensors values to Weather Underground."""

        if not first_time:
            print('Uploading data to Weather Underground')
            sensors_data = self.get_sensors_data()

            # Build a weather data object http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
            weather_data = {
                'action': 'updateraw',
                'ID': Config.STATION_ID,
                'PASSWORD': Config.STATION_KEY,
                'dateutc': 'now',
                'tempf': str(sensors_data[1]),
                'humidity': str(sensors_data[2]),
                'baromin': str(sensors_data[3]),
                'dewptf': str(self.to_fahrenheit(self.calculate_dew_point(sensors_data[0], sensors_data[2])))
            }

            try:
                upload_url = Config.WU_URL + '?' + urlencode(weather_data)
                response = urllib2.urlopen(upload_url)
                html = response.read()
                print('Server response: ', html)
                
                # Close response object
                response.close()
            except:
                print('Could not upload to Weather Underground')
                logging.warning('Could not upload to Weather Underground', exc_info=True)

        self._upload_timer = self._start_timer(Config.UPLOAD_INTERVAL, self._upload_results)

    def _start_timer(self, interval, callback):
        """Internal. Starts timer with given interval and callback function."""
        
        timer = Timer(interval, callback)
        timer.daemon = True
        timer.start()

        return timer

    def _get_cpu_temp(self):
        """"
        Internal.
        Executes a command at the OS to pull in the CPU temperature.
        Thanks to https://www.raspberrypi.org/forums/viewtopic.php?f=104&t=111457
        """
        
        res = os.popen('vcgencmd measure_temp').readline()
        return float(res.replace('temp=', '').replace("'C\n", ''))

    def _get_smooth(self, value):
        """Moving average to smooth reading."""
        
        # We use deque here as it is more efficient for in/out behaviour than regular list/tuple
        if not self._last_readings:
            self._last_readings = deque((value, ) * self.SMOOTH_READINGS_NUMBER, self.SMOOTH_READINGS_NUMBER)
        else:
            self._last_readings.appendleft(value)
            
        # Average last temperature readings
        return sum(self._last_readings) / self.SMOOTH_READINGS_NUMBER


# Check prerequisites and launch Weather Station
if __name__ == '__main__':
    # Setup logger, to log warning/errors during execution
    logging.basicConfig(
        filename='/home/pi/weather_station/error.log',
        format='\r\n%(asctime)s %(levelname)s %(message)s', 
        level=logging.WARNING
    )

    #  Read Weather Underground Configuration Parameters
    if Config.STATION_ID is None or Config.STATION_KEY is None:
        print('Missing values from the Weather Underground configuration file\n')
        logging.warning('Missing values from the Weather Underground configuration file')

        sys.exit(1)

    # Make sure we don't have an upload interval more than 3600 seconds
    if Config.UPLOAD_INTERVAL > 3600:
        print('The application\'s upload interval cannot be greater than 3600 seconds')
        logging.warning('The application\'s upload interval cannot be greater than 3600 seconds')

        sys.exit(1)

    print('Successfully read Weather Underground configuration values')
    print('Station ID: ', Config.STATION_ID)

    def _terminate_application(signal=None, frame=None):
        """Nested. Internal. Tries to terminate weather station and make a clean up."""

        # We need to check if station was initialized
        if 'station' in globals():
            station.stop_station()

        logging.warning('Application terminated', exc_info=not signal)

        print('\nExiting application')
        
    # Subscribe to signals events
    signal.signal(signal.SIGTERM, _terminate_application)

    try:
        station = WeatherStation()

        station.activate_sensors()
        print('Successfully initialized sensors')
        print(station.READINGS_PRINT_TEMPLATE % station.get_sensors_data())

        station.start_station()
        print('Weather Station successfully launched')

        signal.pause()
    except:
        _terminate_application()

        sys.exit(0)
