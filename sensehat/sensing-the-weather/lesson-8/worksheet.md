# Sensing the Weather - Air Quality Sensor Worksheet

In this lesson you will:

- Understand how an air quality sensor works
- Be able to take a reading from an air quality sensor
- Be able to connect to the Twitter API to post tweets with weather data

## How does the air quality sensor work?

Here is the air quality sensor supplied with the Raspberry Pi Weather Station kit:

![Air Quality Sensor](images/air_quality_sensor.png)

The air quality sensor detects the presence of contaminants in the air. The conductivity of the material inside the sensor increases depending on the concentration of detectable gases in the air around the sensor. This change in conductivity is converted to an output signal which corresponds to the gas concentration. The Python library converts this value into a percentage reading of air purity, with 100% being completely free from detectable contaminants.

This sensor is particularly sensitive to hydrogen, carbon monoxide, and methane gases which are present in contaminants such as cigarette smoke and traffic fumes.


## Taking a reading from the air quality sensor

You have taken a reading from other sensors where you create an object to talk to the sensor, and then call a method to get data from that object. The air quality sensor works in exactly the same way:

```python
import tgs2600 as aqsensor

air_quality = aqsensor.TGS2600()

print( str(air_quality.get_value()) + "%")
```

1. Start a new Python program called `air_quality.py` inside the `weather_station` directory on your Raspberry Pi Weather Station.

1. Type in the code above and check that you get a sensor reading percentage. If you're testing your Weather Station inside a building, you can probably expect to get a reading of around 55-60%.

## Sharing our weather data

### Question

How can we share data from the Weather Station with people across the world?

### Answer

Your Weather Station already shares data with schools across the world via the Oracle database. Readings are taken from every sensor and uploaded via the Weather Station's internet connection to the database. You can use data from the database in the [Graphing the weather](https://www.raspberrypi.org/learning/graphing-the-weather/) resource.

However, we can also share local weather data on social media. Let's make our Weather Station tweet the weather!

## Setting up your Weather Station to tweet

1. Ask your teacher for the consumer keys and access tokens for the class Twitter account. Your teacher might provide these to you as a file, or on their own.

1. Follow steps 1-4 on the guide [Getting started with Twitter](https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/worksheet/).

	Your program so far should look like this:

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

	Run the program and check whether it tweets the message.

1. Comment out the line of code which performs the tweet. We're going to make some changes to the program and we don't want to generate a lot of nonsense tweets whilst we are testing, and potentially make mistakes in the code!

	```python
	# Comment out by putting a # in front of the line
	# twitter.update_status(status=message)
	```

## Tweeting the weather

The aim of this lesson is to use the Twitter API to tweet the air quality data from your Weather Station. For our tweet weather bulletin to be useful, it would be good if the program could:

- Tweet the weather sensor reading (rounded to a whole percentage)
- Tweet a reading at regular intervals e.g. once every hour
- Add a random message to the tweet depending on the value

1. Firstly, we will tackle simply tweeting a sensor reading. You need to combine your `twitter.py` code from before with the code that takes a reading from the sensor:

	```python
	import tgs2600 as aqsensor

	air_quality = aqsensor.TGS2600()

	print( str(air_quality.get_value()) + "%")
	```

	Work out where to put the first two lines of the code above in your `twitter.py` program and add them.

1. Instead of printing the air quality value, we would like to tweet it. Change your `message` variable to be equal to the sensor reading:

	```python
	message = str(air_quality.get_value()) + "%"
	```

	Run your program and check whether it tells us it has tweeted the sensor reading. Remember, if you have commented out the line of code which actually tweets, you won't see an actual tweet.

1. The value we are given comes with lots of decimal places. To round the number to a whole number, use the `round()` function:

	```python
	message = str( round( air_quality.get_value() ) ) + "%"
	```

1. Next, let's make the code tweet at regular intervals. Think back to the lesson about [wind gust speed](../lesson-3/worksheet.md) where we saw this code:

	```python
	while True:
        count = 0
        sleep(interval)
        print( calc_speed(interval), "kph")
        print("Gust speed " + str(check_for_gusts() + "kph")
    ```

    This code set up an infinite loop which calculated the wind speed at an `interval`, or in other words calculated it every few seconds. Tweeting the air quality every few seconds is too often, but we could provide readings further apart, for example one every hour.

1. Add `from time import sleep` at the start of the program to be able to use the `sleep()` function.

1. The loop below runs forever and tweets every 10 minutes. Work out how to modify the code to tweet every hour, and then put your tweet code *inside* the loop.

	```python
	while True:

	    sleep(60*10)
	    print("Tweeting...")
    ```

1. Finally, let's add a message about the air quality, depending on how good or bad it is. Think back to the [wind direction](lesson-3/worksheet.md) lesson where we used code to determine what to do based on boundaries:

	```python
	if degrees >= 338 or degrees < 23:
    	print("N")
    ```

	Add some code after you generate the message, but *before* actually tweeting it, to **concatenate** a comment about the air quality onto the end of the message, depending on the value read from the sensor. The `+=` performs the concatenation. Here's an example to get you started:

	```python
	if current_quality > 55:
        message += "That's pretty good!"
    ```

    Does it matter whether you test the smallest value first or the largest?

1. If you want to check your code, the [finished code](code/tweeting_weather_station.py) is available.

## Summary

- You have read data from the air quality sensor
- You now know how to display this data as a tweet
- You have considered the validity of the data generated by sensors

## What next

- Can you add any of the weather data collected from the other sensors into your tweet? For example, could you provide the current wind speed or the relative humidity as well as the air quality?
- Now that you have finished working with all of the sensors, why not try [Graphing the weather](https://www.raspberrypi.org/learning/graphing-the-weather/)?
