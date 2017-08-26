#!/usr/bin/env python
#===============================================================================
# weather.py
#
# Get weather forecast from NOAA and display as 8x8 icons
#   * NOAA's doc: http://graphical.weather.gov/xml/rest.php
#   * Set location using zipcode
#   * Use 12+hourly format
#   * Somewhat generalized for any number of days
#
# 2014-09-14
# Carter Nelson
#===============================================================================
import time
import httplib
import sys
from xml.dom.minidom import parseString

from rpi_weather import RpiWeather
from led8x8icons import LED8x8ICONS

icons = ['SUNNY','RAIN','CLOUD','SHOWERS','SNOW','STORM']

ZIPCODE     = 98109
NUM_DAYS    = 4
NOAA_URL    = "graphical.weather.gov"
REQ_BASE    = r"/xml/sample_products/browser_interface/ndfdBrowserClientByDay.php?"
TIME_FORMAT = "12+hourly"
HEADERS     = {"User-Agent":"Mozilla/5.0"}

display = RpiWeather()

def giveup():
    """Action to take if anything bad happens."""
    for matrix in xrange(4):
        display.set_raw64(LED8x8ICONS['UNKNOWN'],matrix)
    print "Error occured."
    sys.exit(1)
    
def validate_zip(zip_arg):
    """Return integer conversion of supplied string if valid, global default ZIPCODE otherwise."""
    try:
        zip = int(zip_arg)
        if zip < 99999 and zip > 0 and len(zip_arg) == 5:
            return zip
    except ValueError:
        pass
    return ZIPCODE

def get_offset():
    """ Returns 0 if local time after 6AM and before 6PM, 1 otherwise."""
    hour = time.localtime().tm_hour
    if hour > 6 and hour < 18:
        return 0
    else:
        return 1
    
def make_noaa_request():
    """Make request to NOAA REST server and return data."""
    REQUEST = REQ_BASE + "zipCodeList={0:05d}&".format(ZIPCODE)+\
                        "format={0}&".format(TIME_FORMAT)+\
                        "numDays={0}".format(NUM_DAYS)    
    try:
        conn = httplib.HTTPSConnection(NOAA_URL)
        conn.request("GET", REQUEST, headers=HEADERS)
        resp = conn.getresponse()
        data = resp.read()
    except:
        giveup()
    else:
        return data
    
def get_noaa_forecast():
    """Return a string of forecast results."""
    try:
        vals = parseString(make_noaa_request()) \
                .getElementsByTagName("weather-conditions")
    except:
        giveup()
        
    if len(vals) < 2*NUM_DAYS:
        print "Request-Result Mismatch: REQ=%d RES=%d" % (NUM_DAYS,len(vals))
        giveup()
        
    if '12' in TIME_FORMAT:
        offset = get_offset()
    else:
        offset = 0
    
    forecast = [e.getAttribute("weather-summary") for e in vals[offset::2]]
    
    return forecast
    
def print_forecast(forecast=None):
    """Print forecast to screen."""
    if forecast == None:
        return
    print '-'*20
    print time.strftime('%Y/%m/%d %H:%M:%S')
    print "ZIPCODE {0}".format(ZIPCODE)
    print '-'*20
    for daily in forecast:
        print daily
        
def display_forecast(forecast=None):
    """Display forecast as icons on LED 8x8 matrices."""
    if forecast == None:
        return
    for matrix in xrange(4):
        display.set_raw64(LED8x8ICONS['UNKNOWN'], matrix)    
        for icon in icons:
            if icon in forecast[matrix].encode('ascii','ignore').upper():
                display.set_raw64(LED8x8ICONS[icon], matrix)
                
#-------------------------------------------------------------------------------
#  M A I N
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ZIPCODE = validate_zip(sys.argv[1])
    forecast = get_noaa_forecast()
    print_forecast(forecast)
    display_forecast(forecast)
