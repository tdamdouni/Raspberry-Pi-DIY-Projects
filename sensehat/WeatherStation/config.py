'''*****************************************************************************************************************
    Raspberry Pi + Raspbian Weather Station
    By Uladzislau Bayouski
    https://www.linkedin.com/in/uladzislau-bayouski-a7474111b/
    
    Configuration package.
********************************************************************************************************************'''

class Config:
    """Configuration class for Weather Station"""

    # Weather Undeground configuration
    STATION_ID = 'YOUR_STATION_ID'
    STATION_KEY = 'YOUR_STATION_KEY'
    WU_URL = 'http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php'

    # Runtime configuration
    WEATHER_UPLOAD = True
    UPLOAD_INTERVAL = 600 # in seconds
    LOG_TO_CONSOLE = False
    LOG_INTERVAL = 5 # in seconds
    UPDATE_DISPLAY = True
    UPDATE_INTERVAL = 60 # in seconds

    # Visual styles configuration
    TEMP_POSITIVE = (255, 0, 0)    # red
    TEMP_NEGATIVE = (0, 0, 255)    # blue
    HUM_POSITIVE = (0, 255, 0)     # green
    HUM_NEGATIVE = (255, 255, 255) # white
    PRESS_POSITIVE = (148, 0, 211)  # purple
    PRESS_NEGATIVE = (255, 140, 0)   # orange
    SCROLL_TEXT = True
    SCROLL_TEXT_SPEED = .05
