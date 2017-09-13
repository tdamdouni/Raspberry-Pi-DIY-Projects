import os

# Function definition
def DetectNetwork(interface='eth0'):
  # Read ifconfig.txt and determine
  # if network is connected
  try:
    filename = 'ifconfig_' + interface + '.txt'
    os.system('ifconfig ' + interface + ' > /home/pi/' + filename)
    f = open('/home/pi/' + filename, 'r')
    line = f.readline() # skip 1st line
    line = f.readline() # read 2nd line
    f.close()
    
    if line.find('inet addr:')>0:
      return True
    else:
      return False
  except:
    return False
 
# Run function and test result
if DetectNetwork:
  print "Network detected"
else:
  print "No network detected" 