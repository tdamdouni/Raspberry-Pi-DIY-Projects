# !/usr/bin/env python3
# coding: utf-8

import os
import re
import time
import gpiozero
from gpiozero import Button
from twython import Twython
import scrollphathd
from scrollphathd.fonts import font5x7
from signal import pause

#Twitter authorisation keys - add your own here
CONSUMER_KEY = 'YOUR CONSUMER KEY HERE'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET HERE'
ACCESS_KEY = 'YOUR ACCES KEY HERE'
ACCESS_SECRET = 'YOUR ACCESS SECRET HERE'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

def news():
# Put the Twitter usernames of the news organisations you want to read here
    twits = ["BBCNews", "GranadaReports", "SkyNews", "itvnews", "MENnewsdesk"]
    for index in range (len(twits)):
# The count parameter defines how many tweets from each account you'll read            
        tweets = api.get_user_timeline(screen_name=twits[index], count=3)
        for tweet in tweets:
            clean_tweet = '%s: %s' % (      tweet['user']['screen_name'],
                                                tweet['text'])

# This line clear URLs from the tweets
            clean_tweet = re.sub(r"(https?\://|http?\://|https?\:)\S+", "", clean_tweet)
            clean_tweet = clean_tweet.encode('ascii', 'ignore').decode('ascii')
            scrollphathd.write_string(clean_tweet, x=17, font=font5x7)
            tweet_length = scrollphathd.write_string(clean_tweet, x=17, y=0,font=font5x7) + 7
            time.sleep(0.25)
            while tweet_length > 0:
                scrollphathd.show()
                scrollphathd.scroll()
                tweet_length -= 1
                time.sleep(0.01)
            scrollphathd.clear()
            scrollphathd.show()

def weather():
    # usernames of the weather accounts you'll be using        
    twitweather = ["mcrweather", "Manches_Weather"]
    for index in range (len(twitweather)):
        tweets = api.get_user_timeline(screen_name=twitweather[index], count=1)
        for tweet in tweets:
            clean_tweet = '%s: %s' % (      tweet['user']['screen_name'],
                                                tweet['text'])

            clean_tweet = re.sub(r"(https?\://|http?\://)\S+", "", clean_tweet)
            clean_tweet = clean_tweet.encode('ascii', 'ignore').decode('ascii')
            scrollphathd.write_string(clean_tweet, x=17, font=font5x7)
            tweet_length = scrollphathd.write_string(clean_tweet, x=17, y=0,font=font5x7) + 7
            time.sleep(0.25)
            while tweet_length > 0:
                scrollphathd.show()
                scrollphathd.scroll()
                tweet_length -= 1
                time.sleep(0.01)
            scrollphathd.clear()
            scrollphathd.show()

scrollphathd.rotate(degrees=180)
scrollphathd.set_brightness(0.1)
scrollphathd.write_string("Ready   ", x=17, font=font5x7)
ready_length = scrollphathd.write_string("Ready   ", x=17, font=font5x7) + 7
time.sleep(0.25)
while ready_length > 0:
    scrollphathd.show()
    scrollphathd.scroll()
    ready_length -= 1
    time.sleep(0.01)
scrollphathd.clear()
scrollphathd.show()
news_button = Button(17)
weather_button = Button(27)
news_button.when_pressed = news
weather_button.when_pressed = weather
pause()
