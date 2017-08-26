#  Sensing the Weather - Air Quality Lesson

In this lesson students will learn about how air quality is monitored, and will take readings from an air quality sensor expressed as a percentage of air purity. The Weather Station will generate a regular tweet showing the air quality in the local area.

## Sensor guide

Here is some background information about the [air quality sensor](../guides/air_quality.md).

## Learning objectives

- Understand how an air quality sensor works
- Be able to take a reading from an air quality sensor
- Be able to connect to the Twitter API to post tweets with weather data

## Cross-curricular applications

- Computer Science - concatenation, using an API
- Geography - GIS mapping, climate change


## Lesson summary

- How does the air quality sensor work - which gases does it look for?
- Collecting readings from an air quality sensor
- Using the Twitter API to tweet air quality data for an area

## Starter

Data is freely available online about the quantity of pollutants recorded in the atmosphere. For example, in the UK this [interactive emissions map](http://naei.defra.gov.uk/data/gis-mapping) is a GIS map where you can inspect the quantity of a variety of pollutants in your local area. Select 'Carbon Monoxide' from the drop-down menu and enter your post code or zoom in to your local area on the map to see how polluted your area is.

The air sensor on the Raspberry Pi Weather Station board measures the concentration of contaminants such as hydrogen, carbon monoxide, and methane. They are not returned in the same units as this map, but rather expressed as a percentage of air purity; the higher the percentage, the more pure the surrounding air is.

## Main development

1. Students boot their Raspberry Pi Weather Station and log in.

1. Demonstrate the basic program to gather a reading from the air quality sensor. It follows the exact same concepts students have already encountered: import a library, create an object, call a method on the object to get the data, and then print it.

	```python
	import tgs2600 as aqsensor

	air_quality = aqsensor.TGS2600()

	print( str(air_quality.get_value()) + "%")
	```

1. To allow your Weather Station to tweet, you will need to create a class Twitter account for students to tweet from. This requires a valid email address and a mobile phone number. The students will need access to the **OAuth consumer key, consumer secret, access token, and access token secret** values from the Twitter account.

1. Following steps 1-4 from the [Getting started with Twitter](https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/) guide, students write a program that will allow the Weather Station to send tweets from a Twitter account.

	You may need to install the `requests_oauthlib` package if you receive an error that this is missing. To do this, make sure your Raspberry Pi Weather Station is connected to the internet, open the terminal and type:

	```bash
	sudo pip3 install requests_oauthlib
	```

	Follow the steps up to and including step 4, where you will create a program which tweets. The program so far should look like this:

	```python
	from twython import Twython
	from auth import (
	    consumer_key,
	    consumer_secret,
	    access_token,
	    access_token_secret
	)
	twitter = Twython(
	    consumer_key,
	    consumer_secret,
	    access_token,
	    access_token_secret
	)
	message = "Hello World! I'm a tweeting weather station."
	twitter.update_status(status=message)
	print("Tweeted: %s" % message)
	```
1. Now students will need to add the following to their program, using the [worksheet](worksheet.md) as a guide:

	- How to tweet the weather sensor reading (rounded to a whole percentage)
	- How to tweet a reading at regular intervals e.g. once every hour
	- How to add a random message to the tweet depending on the value

	It's probably a good idea to comment out the line that actually tweets with a `#` whilst testing the program, to avoid producing lots of tweets by mistake!

	```python
	# Comment out by putting a # in front of the line
	# twitter.update_status(status=message)
	```

	The finished program is [here](code/tweeting_weather_station.py).

## Plenary

Ask the class the following question:

- Why might the data from this sensor not be as useful as the data from other sensors?

**Answer:**

- The air quality sensor can only detect some gases in the atmosphere, not all possible pollutants. The value returned is a percentage of air purity, but what does that really mean? How is it calibrated? A value of around 60% actually indicates a pretty good air quality.


## Extension

- Can you add any of the weather data collected from the other sensors into your tweet? For example, could you provide the current wind speed or the relative humidity as well as the air quality?
- Now that you have finished working with all of the sensors, why not try [Graphing the weather](https://www.raspberrypi.org/learning/graphing-the-weather/)?
