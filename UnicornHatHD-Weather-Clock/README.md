# UnicornHat HD Weather Clock
Binary clock with weather API integration designed for Pimoroni's UnicornHat HD.

Displays hours, minutes and seconds in binary format, as well as providing weather status (rainy, cloudy, sunny, etc), humidity and temperature.

Humidity is shown on the top bar in units of 10%; temperature is shown on the bottom bar in units of 5degC.

## Dependencies
Requires [pytz](https://pypi.python.org/pypi/pytz), [pyowm](https://github.com/csparpa/pyowm) and [unicornhathd](https://github.com/pimoroni/unicorn-hat-hd)

## Usage
In order for the weather API to function properly you'll need to sign up and get an API key from openweathermap.org and insert it on line 11 of weatherclock.py. Next, enter your location on line 12.

If you want to use a different timezone, enter that on line 16.
