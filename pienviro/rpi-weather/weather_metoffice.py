#!/usr/bin/env python
#===============================================================================
# weather_metoffice.py
#
# Get weather forecast from the Met Office and display as 8x8 icons
#   * Met Office's doc: http://www.metoffice.gov.uk/datapoint/support/api-reference
#   * Retrieve location id from: http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=2a26370d-c529-496c-8d9d-7c7b8468e379
#   * Uses 'UK daily site specific forecast'
#   * Need to have an API key from Met Office: https://register.metoffice.gov.uk/WaveRegistrationClient/public/register.do?service=datapoint
#
# 2016-08-07
# Created by: Carter Nelson
# Modified to Met Office by: Will Jenkins
#===============================================================================

import time
import httplib
import sys
import json
import ConfigParser

from rpi_weather import RpiWeather
from led8x8icons import LED8x8ICONS

display = RpiWeather()

METOFFICE_URL    = "datapoint.metoffice.gov.uk"
REQ_BASE    = r"/public/data/val/wxfcs/all/json/"
CONFIG_FILE = "weather.cfg"
API_KEY = None
LOCATION_ID = None

ICON_MAP = { # Day forecast codes only
#   Met Office weather code         LED 8x8 icon
    "NA":                           "UNKNOWN",
    1:                              "SUNNY",    # Sunny day
    3:                              "CLOUD",    # Partly cloudy (day)
    5:                              "UNKNOWN",      # Mist
    6:                              "UNKNOWN",      # Fog
    7:                              "CLOUD",    # Cloudy
    8:                              "CLOUD",    # Overcast
    10:                             "SHOWERS",  # Light rain shower (day)
    11:                             "RAIN",     # Drizzle
    12:                             "RAIN",     # Light rain
    14:                             "SHOWERS",  # Heavy rain shower (day)
    15:                             "RAIN",     # Heavy rain
    17:                             "SHOWERS",  # Sleet shower
    18:                             "RAIN",     # Sleet
    20:                             "SHOWERS",  # Hail shower (day)
    21:                             "RAIN",     # Hail
    23:                             "SNOW",     # Light snow shower (day)
    24:                             "SNOW",     # Light snow
    26:                             "SNOW",     # Heavy snow shower (day)
    27:                             "SNOW",     # Heavy snow
    29:                             "STORM",    # Thunder shower (day)
    30:                             "STORM"     # Thunder 
}

def giveup():
    """Action to take if anything bad happens."""
    for matrix in xrange(4):
        display.set_raw64(LED8x8ICONS['UNKNOWN'],matrix)
    print "Error occured."
    sys.exit(1)
    
def read_config(filename):
    config = ConfigParser.RawConfigParser()
    global API_KEY, LOCATION_ID
    try:
        config.read(filename)
        API_KEY = config.get('config','API_KEY')
        LOCATION_ID = config.get('config','LOCATION_ID')
    except Exception as err:
        print err
        giveup()
        
def make_metoffice_request():
    """Make request to metoffice.gov.uk and return data."""
    REQUEST = REQ_BASE + format(LOCATION_ID) + "?res=daily&key=" + API_KEY
    try:
        conn = httplib.HTTPConnection(METOFFICE_URL)
        conn.request("GET", REQUEST)
        resp = conn.getresponse()
        data = resp.read()
    except Exception as err:
        print err
        giveup()
    else:
        return data
    
def get_forecast():
    """Return a list of forecast results."""
    json_data = json.loads(make_metoffice_request()) # Inlcudes day & night weather for 5 days (including today)
    forecast = []
    for day in xrange(4): # Only looking for day weather for first 4 days, ignoring night and 5th day
        forecast.append(json_data["SiteRep"]["DV"]["Location"]["Period"][day]["Rep"][0]["W"])
    return forecast
    
def print_forecast(forecast=None):
    """Print forecast to screen."""
    if forecast == None:
        return
    print '-'*20
    print time.strftime('%Y/%m/%d %H:%M:%S')
    print "Location id: {0}".format(LOCATION_ID)
    print '-'*20
    for daily in forecast:
        try:
            print "Daily code:", daily
            print "Icon: {0}".format(ICON_MAP[int(daily)])
        except Exception as err:
            print "Unknown code: {0}".format(err)

def display_forecast(forecast=None):
    """Display forecast as icons on LED 8x8 matrices."""
    if forecast == None:
        return
    for matrix in xrange(4):
        try:
            icon = ICON_MAP[int(forecast[matrix])]
            display.set_raw64(LED8x8ICONS[icon], matrix)
        except:
            display.set_raw64(LED8x8ICONS["UNKNOWN"], matrix)

#-------------------------------------------------------------------------------
#  M A I N
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    read_config(CONFIG_FILE)
    forecast = get_forecast()
    print_forecast(forecast)
    display_forecast(forecast)