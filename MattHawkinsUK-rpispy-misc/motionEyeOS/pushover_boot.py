#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           pushover_boot.py
#  Send pushover notification when motionEyeOS boots.
#  Use with userinit.sh
#
# Author : Matt Hawkins
# Date   : 29/08/2017
#
# http://www.raspberrypi-spy.co.uk/tag/motioneyeos/
#
#--------------------------------------
import httplib, urllib
import sys

if len(sys.argv)==5:

  # Get 4 arguments passed to this script
  mytitle=sys.argv[1]+" camera rebooted"
  myip="http://"+sys.argv[2]
  myuser=sys.argv[3]
  mytoken=sys.argv[4]
  mymessage="Your "+sys.argv[1]+" camera has just rebooted"

  print(mytitle)
  
  conn = httplib.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
    urllib.urlencode({
      "token": mytoken,      # Pushover app token
      "user": myuser,        # Pushover user token
      "html": "1",           # 1 for HTML, 0 to disable
      "title": mytitle,      # Title of message
      "message": mymessage,  # Message (HTML if required)
      "url": myip,           # Link to include in message
      "url_title": myip,     # Text for link
      "sound": "cosmic",     # Sound played on receiving device
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()