# Part of PiNet https://github.com/PiNet/PiNet-Support
#
# See LICENSE file for copyright and license details

# Tool for checking if all the domains used by PiNet are accessable.
# Run with     python3 check-web.py

version="0.0.1"

def testSiteConnection(siteURL, timeoutLimit = 5):
    """
    Tests to see if can access the given website.
    """
    import urllib.request
    try:
        response=urllib.request.urlopen(siteURL,timeout=int(timeoutLimit))
        return True
    except:
        return False


def internetFullStatusCheck(timeoutLimit = 5):
    """
    Full check of all sites used by PiNet.
    """
    sites = []
    sites.append(["Main Raspbian repository", "http://archive.raspbian.org/raspbian.public.key", "Critical", False])
    sites.append(["Raspberry Pi Foundation repository", "http://archive.raspberrypi.org/debian/raspberrypi.gpg.key", "Critical",False])
    sites.append(["Github", "https://github.com", "Critical", False])
    sites.append(["Bitbucket (Github mirror)", "https://bitbucket.org", "Recommended", False])
    sites.append(["BlueJ", "http://bluej.org", "Recommended", False])
    sites.append(["Bit.ly", "http://bit.ly", "Highly recommended", False])
    sites.append(["PiNet metrics", "https://secure.pinet.org.uk", "Recommended", False])
    for website in range(0, len(sites)):
    	sites[website][3] = (testSiteConnection(sites[website][1]))
    for website in range(0, len(sites)):
        print(str(sites[website][3]) + " - " + str(sites[website][0]) + " {" + str(sites[website][2]) +"}" + " (" + str(sites[website][1]) + ")")

print("")
print("------------------------")
print("PiNet site checking tool")
print("------------------------")
print("")
print("This tool is for checking if you can access the sites used by PiNet in the installation process and the day to day running of PiNet")
print("It is recommended not to proceed with a PiNet install if ANY of the sites below are marked as false, as this means they cannot be accessed")
print("Note that any of the below services could actually be down themselves instead, but that is very rare")
print("")
print("Starting test, this can take up to 120 seconds")
print("")

internetFullStatusCheck()

