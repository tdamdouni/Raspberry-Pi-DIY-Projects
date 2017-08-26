from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
import tgs2600 as aqsensor
from time import sleep

air_quality = aqsensor.TGS2600()

current_quality = round(air_quality.get_value())


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


# Start the message
while True:
    
    # Wait for 10 minutes
    sleep(60*10)
    
    message = "The current air quality rating in your area is " + str(current_quality) + "%. "

    if current_quality > 55:
        message += "That's pretty good!"
    elif current_quality > 45:
        message += "That's not bad :)"
    else:
        message += "That's not great. Stay safe :("


    # Do the tweet
    twitter.update_status(status=message)
    print("Tweeted: %s" % message)
