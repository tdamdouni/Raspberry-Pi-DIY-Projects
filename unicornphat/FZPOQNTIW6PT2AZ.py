# https://www.hackster.io/masteruan/play-with-raspberry-pi-zero-and-phat-140b9a

import pyowm
import time
import sys
import scrollphat

scrollphat.set_brightness(3)

owm = pyowm.OWM(‘£££££££££££££££££££££’)#You MUST provide a valid API key

#forecast = owm.daily_forecast("Milan,it")
#tomorrow = pyowm.timeutils.tomorrow()
#result = forecast.will_be_sunny_at(tomorrow) 
#f = forecast.get_forecast()
#print (f)


while True:
    try:
        observation = owm.weather_at_place('Milan,it')
        w = observation.get_weather()
        wind = w.get_wind()
        hum = w.get_humidity()
        temp = w.get_temperature('celsius')
        print(wind)
        print (hum)
        print(temp)
        results = ("Meteo Milano Temp min: "+str(temp['temp_min'])+" Temp max: "+str(temp['temp_max'])+" Humy: "+str(hum)+"%  Wind: "+str(wind['speed']))
        time.sleep(3)
        for i in range(600):
            scrollphat.write_string(results, 11)
            scrollphat.scroll()
            time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
