#!/usr/bin/env python

# http://www.pcworld.com/article/3027446/hardware/irate-comcast-subscriber-turns-raspberry-pi-into-a-watchdog-for-slow-internet-speeds.html
# http://pastebin.com/WMEh802V
# https://github.com/sivel/speedtest-cli
# https://twitter.com/A_Comcast_User

# Requires sudo pip install twitter
# DO NOT sudo pip install python-twitter

import csv
import datetime
import os
# import sys
import time

import twitter


def test():

        # Run speedtest-cli
        print 'Running speedtest...'
        a = os.popen("python /usr/local/bin/speedtest-cli --simple").read()
        print 'Speedtest completed:'
        # Split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print a
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        # If speedtest could not connect set the speeds to 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        # Extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print date, p, d, u
        # Save the data to file for local network plotting
        out_file = open('/home/pi/speedtest.csv', 'a')
        writer = csv.writer(out_file)
        writer.writerow((ts * 1000, p, d, u))
        out_file.close()

        # Twitter Credentials
        token = ""
        token_key = ""
        con_sec = ""
        con_sec_key = ""

        my_auth = twitter.OAuth(token, token_key, con_sec, con_sec_key)
        twit = twitter.Twitter(auth=my_auth)

        # Try to tweet if speedtest couldnt even connect. Probably wont work if the internet is down
        if "Cannot" in a:
                print "Internet seems to be down."
                try:
                        tweet = "Hey @TWC @TWC_Help why is my #internet #down? I pay for 100 down\\10 up in #Westchester #NY? #twcoutage #TWC"
                        twit.statuses.update(status=tweet)
                except:
                        pass

        # Tweet if down speed is less than whatever I set
        elif eval(d) < 100:
                print "Tweeting slow bandwidth."
                try:
                        # I know there must be a better way than to do (str(int(eval())))
                        tweet = "Hey @TWC why is my #internet #speed " + str(int(eval(d))) + " down\\" + str(int(eval(u))) + " up when I pay for 100 down\\10 up in #Westchester #NY? @TWC_Help @TWC_NYNJ #TWC #slow #speedtest"
                        twit.statuses.update(status=tweet)
                except Exception, e:
                        print str(e)
                        pass
        return

if __name__ == '__main__':
        test()
        print 'Completed!'
