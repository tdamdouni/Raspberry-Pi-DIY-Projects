import httplib
import requests
import unicornhat as unicorn
import time

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.6)
unicorn.off()


def statuspage():
	resp = requests.get('https://kd2w7ghdk56w.statuspage.io/api/v2/status.json') # saucelabs status page
	if resp.status_code != 200:
   		# This means something went wrong.
   		return resp.status_code
	data = resp.json()
	return data["status"]["description"] + ':' + data["status"]["indicator"]

def getHead(url):
    conn = httplib.HTTPConnection(url)
    try:
        conn.request("HEAD", "/")
        return True
    except:
        return False

def numTickets(url):
	resp = requests.get(url, auth=('username', 'password')) # replace username and password with desk username/email and password
	if resp.status_code != 200:
   		# This means something went wrong.
   		return 'error: HTTP ' + str(resp.status_code)
   	data = resp.json()
   	return str(data["total_entries"])

def unassigned():
  try:
    # various unassigned ticket filters in desk
    unassignedCount = int(numTickets('https://support.saucelabs.com/api/v2/filters/2320481/cases')) \
    + int(numTickets('https://support.saucelabs.com/api/v2/filters/2320481/cases')) \
    + int(numTickets('https://support.saucelabs.com/api/v2/filters/2319006/cases')) \
    + int(numTickets('https://support.saucelabs.com/api/v2/filters/2318445/cases')) \
    + int(numTickets('https://support.saucelabs.com/api/v2/filters/2318446/cases'))
    return str(unassignedCount)
  except:
    return "error"

def lightEmUp(y1,y2,r,g,b):
  for y in range(y1,y2):
    for x in range(8):
      unicorn.set_pixel(x,y,r,g,b)
      unicorn.show()
      time.sleep(0.05)


# check if online
online = getHead("www.google.com")
print('internet connectivity: connected' if online else 'internet connectivity: no internet!')
if (online):
  # continue

  # check saucelabs.com is reachable
  sauce = getHead("www.saucelabs.com")
  print('saucelabs.com is up' if sauce else 'saucelabs.com not reachable!')
  if (sauce):
    lightEmUp(0,1,0,255,0)
  else:
    lightEmUp(0,1,255,0,0)

  # check statuspage
  saucestatus = statuspage()
  print('sauce statuspage: ' + statuspage())
  if (saucestatus.startswith('All Systems Operational')):
    lightEmUp(1,2,0,255,0)
  elif (saucestatus.startswith('Partial System Outage')):
    if (saucestatus.endswith(':minor')):
      lightEmUp(1,2,255,255,0)
    elif (saucestatus.endswith(':major')):
      lightEmUp(1,2,255,145,0)
    elif (saucestatus.endswith(':critical')):
      lightEmUp(1,2,255,0,0)  
  elif (saucestatus == 'Major Service Outage'):
    lightEmUp(1,2,255,0,0)  
  else:
    lightEmUp(1,2,255,0,0)

  # check desk tickets
  numMine = numTickets('https://support.saucelabs.com/api/v2/filters/2428139/cases') # 'my open tickets' filter in desk
  if (numMine.startswith('error')):
    print('error getting number of support tickets: ' + numMine)
    lightEmUp(2,4,255,0,0)
  else: 
    print('number of support tickets in my queue: ' + numMine)
    intNumMine = int(numMine)
    if (intNumMine == 0):
      lightEmUp(2,3,0,255,0)
    elif (intNumMine < 4):
      lightEmUp(2,3,200,255,0)
    elif (intNumMine < 7):
      lightEmUp(2,3,255,255,0)
    elif (intNumMine < 11):
      lightEmUp(2,3,255,200,0)
    elif (intNumMine < 15):
      lightEmUp(2,3,255,100,0)
    else:
      lightEmUp(2,3,255,0,0)

    numUnassigned = unassigned();
    if (numUnassigned.startswith('error')):
      print('error getting number of unassigned support tickets: ' + numUnassigned)
      lightEmUp(3,4,255,0,0)
    else:
      print('number of unassigned support tickets: ' + numUnassigned)
      intNumUnassigned = int(numUnassigned)
      if (intNumUnassigned == 0):
        lightEmUp(3,4,0,255,0)
      elif (intNumUnassigned < 4):
        lightEmUp(3,4,200,255,0)
      elif (intNumUnassigned < 7):
        lightEmUp(3,4,255,255,0)
      elif (intNumUnassigned < 11):
        lightEmUp(3,4,255,200,0)
      elif (intNumUnassigned < 15):
        lightEmUp(3,4,255,100,0)
      else:
        lightEmUp(3,4,255,0,0)


else:
  lightEmUp(0,4,255,0,0)

time.sleep(600)
