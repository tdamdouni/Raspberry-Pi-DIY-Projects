import httplib, urllib
 
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
	urllib.urlencode({
		"token": "APP_TOKEN",                    # Insert app token here
		"user": "USER_TOKEN",                    # Insert user token here
		"html": "1",                             # 1 for HTML, 0 to disable
		"title": "Motion Detected!",             # Title of the message
		"message": "<b>Front Door</b> camera!",  # Content of the message
		"url": "http://IP.ADD.RE.SS",            # Link to be included in message
		"url_title": "View live stream",         # Text for the link
		"sound": "siren",                        # Define the sound played	
	}), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()