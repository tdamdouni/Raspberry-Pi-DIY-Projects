import time
import time
import sys, subprocess, urllib, time, tweepy
import binascii
from sense_hat import SenseHat
sense = SenseHat()

# == OAuth Authentication ==###############
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key= 'xxx'
consumer_secret= 'xxxxx'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token= 'xxx'
access_token_secret= 'xxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

###Number one###
X = [0, 0, 0]
Y = [255, 255, 255]

number_one = [
X, X, X, Y, Y, X, X, X,
X, X, Y, Y, Y, X, X, X,
X, Y, Y, Y, Y, X, X, X,
X, X, X, Y, Y, X, X, X,
X, X, X, Y, Y, X, X, X,
X, X, X, Y, Y, X, X, X,
X, Y, Y, Y, Y, Y, Y, X,
X, Y, Y, Y, Y, Y, Y, X
]

number_zero = [
X, Y, Y, Y, Y, Y, Y, X,
X, Y, Y, Y, Y, Y, Y, X,
X, Y, Y, X, X, Y, Y, X,
X, Y, Y, X, X, Y, Y, X,
X, Y, Y, X, X, Y, Y, X,
X, Y, Y, X, X, Y, Y, X,
X, Y, Y, Y, Y, Y, Y, X,
X, Y, Y, Y, Y, Y, Y, X
]

sense.set_pixels(number_one)
###CODE TO GET TWITTER TO LISTEN FOR KEYWORD###
class My_Tweets(tweepy.StreamListener):
    def on_status(self, tweet):
        ###ASCII Dictionary###
       
        try:
            print tweet.user.screen_name
            print tweet.text
            Tweet = str(tweet.text.lower())
            print type(Tweet)
            print ""
            time.sleep(1)
                        
            """Converts the letter to a Binary Value"""
            
            word = bin(int(binascii.hexlify(Tweet), 16))
                
            print word

            sense.show_message(word, text_colour =[255, 255, 255])

            
        except:
             print "Could not decode, probably had an emoji"

tream = tweepy.Stream(auth, My_Tweets())

while(True):
     stream.userstream()


    
