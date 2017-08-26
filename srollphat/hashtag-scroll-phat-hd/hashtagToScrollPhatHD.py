#!/usr/bin/env python

import sys
import time
import tweepy
import scrollphathd
import Queue
from scrollphathd.fonts import font5x7smoothed

# scrollphathd.clear()

#make FIFO queue
q = Queue.Queue()

#define main loop to fetch formatted tweet from queue
def mainloop():
    while True:
        # not q.empty():
        status = q.get()
        scrollphathd.write_string(status,font=font5x7smoothed, brightness=0.1)
        status_length = scrollphathd.write_string(status, x=0, y=0,font=font5x7smoothed, brightness=0.1)
        #print(status)
        #print ("<<<<<< Scrolling tweet", status)
        time.sleep(0.25)
        #print 'status length --->',status_length
        while status_length > 0:
             #print 'status length',status_length
             #print 'buffer_len',scrollphathd.write_string(status, x=0, y=0,font=font5x7smoothed, brightness=0.1)
             #scrollphathd.flip(x=True)
             scrollphathd.rotate(degrees=180)
             scrollphathd.show()
             scrollphathd.scroll(1)
             status_length -= 1
             time.sleep(0.01)
        else:
             #scrollphathd.scroll(0)
             #print ">>status length is zero<<"
             scrollphathd.clear()
             #scrollphathd.show()

# while True:

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if not status.text.startswith('RT'):
            #scroll_tweet(status)
            #format the incoming tweet string
            status = '     >>>>>     @%s: %s     ' % (status.user.screen_name.upper(), status.text.upper())
            status = status.encode('ascii', 'ignore').decode('ascii')
            # put tweet into the fifo queue
            q.put(status)
            #print ("**tweet saved**", status)
            #print q.get()
    def on_error(self, status_code):
        if status_code == 420:
            return False

consumer_key =''
consumer_secret =''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['hug'], stall_warnings=True, async=True)


try:
    mainloop()
except KeyboardInterrupt:
    print('exit')
    myStream.disconnect()
    sys.exit(-1)
