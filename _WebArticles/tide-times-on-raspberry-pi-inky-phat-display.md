# Tide times on Raspberry Pi Inky pHAT display

_Captured: 2017-09-02 at 19:11 from [www.suppertime.co.uk](http://www.suppertime.co.uk/blogmywiki/2017/07/tides/)_

![](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2017/07/tides.png)

> _Now updated with weather info - see end of this blog post!_

Someone once said 'information wants to be free'. Well, yes and no. If you're looking for publicly-funded academic research papers or live train running information or potentially life-saving data like tide times, then forget it. (Little bit of a rant, there. Sorry.)

After [my radio](http://www.suppertime.co.uk/blogmywiki/2017/07/inkyphat-flotilla-radio/), I fancied making a gizmo to show high and low tide times on my Raspberry Pi's [Inky pHAT](https://shop.pimoroni.com/products/inky-phat) e-ink display. This turned out to be way harder than I expected, chiefly because UK tide time data does not seem to be syndicated as an RSS or other accessible data feed. There is a privately-run web site that appears to have an RSS feed, but all the tide times are contained in one XML tag, so it's not very useful. Magic Seaweed have an API but it requires a key - I have asked for one as they have loads more lovely surf data.

So I decided to find out how to do screen-scraping in Python. I used [this very nice guide](https://www.dataquest.io/blog/web-scraping-tutorial-python/) which uses two Python modules, 'requests' (which I already had on my Pi) and 'Beautiful Soup' which I installed with  
`sudo apt-get install python3-bs4`

You can get tide times on many different sites, I chose the Met Office almost at random but partly because I want to add weather info. Screen-scraping is, I have to say, a Hideous Kludge. (I think I saw Hideous Kludge at the Bull and Gate once…) If the Met Office reconfigure their site it any way, this program will probably stop working. It could also do with some error handling…

**DISCLAIMER: this beta is provided for amusement only!  
Do not rely on the tide times presented as code may be buggy.**

![](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2017/07/emptier-backdrop.png)

So here we go - put the background image file (mine is shamelessly modified from the supplied Pimoroni one but you could add one of your own making) and a font of your choice in the same folder as this script, install Beautiful Soup, find your local seaside place geohash code on the Met Office web site and replace mine with it, and off you jolly well go.

If you want to use my retro 68k Mac font (which does look lovely on the Inky pHAT) you can [download it here](http://www.pentacom.jp/pentacom/bitfontmaker2/gallery/?id=3778).

You can set cron to run this automatically - I would suggest running it every morning at 5am; the current version of Raspbian allows you to do this easily on the desktop (Raspberry > System Tools > Scheduled tasks). I think this would be a great project to run on a PiZeroW to make a little tide time gizmo for your beach house!
    
    
    # A program to display tide times on Raspberry Pi with Inky pHAT e-ink display
    # by Giles Booth - www.suppertime.co.uk/blogmywiki
    # Updated 1 Aug 17 to fix bug when only 3 tides in 24 hr period.
    
    # DISCLAIMER: this beta is provided for amusement only!
    # Do not rely on the tide times presented as code may be buggy.
    # This screen-scrapes the Met Office web site, may break at any time.
    # -------------------------------------------------------------
    # I did not need to install 'requests', it was already on Pi.
    # I installed Beautiful Soup with 'sudo apt-get install python3-bs4'
    # using tutorial at https://www.dataquest.io/blog/web-scraping-tutorial-python/
    # Download your own .ttf font eg ChiKareGo.ttf from
    # http://www.pentacom.jp/pentacom/bitfontmaker2/gallery/?id=3778
    # and place it in same folder as this program.
    
    # To do: add weather, wind direction, custom backdrop, fix 3 tide bug.
    
    import requests
    from bs4 import BeautifulSoup
    import inkyphat
    from PIL import Image, ImageFont
    
    # Fetch Gwithian tide times from Met Office web site
    # Find other geohash location codes on the site, eg
    # Godrevy, Cornwall gbujv26hb
    # Walton-on-Naze u10yuyqrf
    # Gt Yarmouth u135pr5sv
    page = requests.get("http://www.metoffice.gov.uk/public/weather/tide-times/gbujtpnch")
    
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]
    
    # print location name in console - you could print this straight to Inky pHAT
    location = soup.find_all('h2')[1].get_text()
    print(location)
    
    # print 1st date (today!)
    today_date = soup.find_all('h3', class_='dayTitle')[0].get_text()
    print(today_date)
    
    # print tide times - needs work as there are not always 4 tides in each 24 hour period
    for i in range (4):
        print(soup.find_all('td')[i].get_text(),soup.find_all('span', class_='tideTime')[i].get_text())
    
    # replace with font of your choice
    font = ImageFont.truetype("ChiKareGo.ttf", 16)
    inkyphat.set_image("emptier-backdrop.png")
    
    title = 'Gwithian ' + today_date
    w, h = font.getsize(title)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    inkyphat.text((x, 0), title, inkyphat.WHITE, font=font)
    inkyphat.line((31, 15, 184, 15)) # Horizontal  line
    
    tide_y = 16
    
    for i in range (4):
        tide_line = soup.find_all('td')[i].get_text() + ' tide: ' + soup.find_all('span', class_='tideTime')[i].get_text()
        if not tide_line[0].isdigit():  # filter out spurious lines when only 3 tides in 24 hrs
            inkyphat.text((50, tide_y), tide_line, inkyphat.WHITE, font=font)
            tide_y += 16
    
    inkyphat.show()
    

**Updated version**

![](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2017/07/tides-wx-300x223.jpg)

I've since tweaked the code (inefficiently I know) to show wind direction, speed and general weather outlook. I've also made a new background image which allows for more text:

![](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2017/07/even-emptier-backdrop.png)
    
    
    # A program to display tide times on Raspberry Pi with Inky pHAT e-ink display
    # by Giles Booth - www.suppertime.co.uk/blogmywiki
    
    # DISCLAIMER: this beta is provided for amusement only!
    # Do not rely on the tide times presented as code may be buggy.
    # This screen-scrapes the Met Office web site, may break at any time.
    # -------------------------------------------------------------
    # I did not need to install 'requests', it was already on Pi.
    # I installed Beautiful Soup with 'sudo apt-get install python3-bs4'
    # using tutorial at https://www.dataquest.io/blog/web-scraping-tutorial-python/
    # Download your own .ttf font eg ChiKareGo.ttf from
    # http://www.pentacom.jp/pentacom/bitfontmaker2/gallery/?id=3778
    # and place it in same folder as this program.
    
    import requests
    from bs4 import BeautifulSoup
    import inkyphat
    from PIL import Image, ImageFont
    import string
    
    # Fetch Gwithian tide times from Met Office web site
    # Find other geohash location codes on the site, eg
    # Godrevy, Cornwall gbujv26hb
    # Walton-on-Naze u10yuyqrf
    # Gt Yarmouth u135pr5sv
    page = requests.get("http://www.metoffice.gov.uk/public/weather/tide-times/gbujtpnch")
    
    soup = BeautifulSoup(page.content, 'html.parser')
    #html = list(soup.children)[2]
    #body = list(html.children)[3]
    
    # print location name in console - you could print this straight to Inky pHAT
    location = soup.find_all('h2')[1].get_text()
    print(location)
    
    # print 1st date (today!)
    today_date = soup.find_all('h3', class_='dayTitle')[0].get_text()
    print(today_date)
    
    # print tide times
    for i in range (4):
        print(soup.find_all('td')[i].get_text(),soup.find_all('span', class_='tideTime')[i].get_text())
    
    # replace with font of your choice
    font = ImageFont.truetype("ChiKareGo.ttf", 16)
    inkyphat.set_image("even-emptier-backdrop.png")
    
    title = 'Gwithian ' + today_date
    w, h = font.getsize(title)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    inkyphat.text((x, 0), title, inkyphat.WHITE, font=font)
    inkyphat.line((31, 15, 184, 15)) # Horizontal  line
    
    tide_y = 16
    for i in range (4):
        tide_line = soup.find_all('td')[i].get_text() + ' tide: ' + soup.find_all('span', class_='tideTime')[i].get_text()
        if not tide_line[0].isdigit():  # filter out spurious lines when only 3 tides in 24 hrs
            inkyphat.text((10, tide_y), tide_line, inkyphat.WHITE, font=font)
            tide_y += 16
    
    # find wind speed and direction
    wx = soup.find_all('div', class_="tideForecast")[0].get_text()
    wxList = wx.splitlines()
    windSpeed = wxList[17]
    windDirection = wxList[13]
    print('Wind',windSpeed,windDirection)
    inkyphat.text((110, 16), 'Wind: '+windDirection+' '+windSpeed+' mph', inkyphat.WHITE, font=font)
    
    # Find weather description
    weather = soup.find(class_="tideForecast")
    forecast_items = weather.find_all(class_="tideWxIcon")
    outlook = forecast_items[0]
    img = outlook.find("img")
    desc = img['alt']
    print('Outlook',desc)
    inkyphat.text((110, 32), desc, inkyphat.WHITE, font=font)
    
    inkyphat.show()
    

  


Back in 2015 I backed Pimoroni's Flotilla modular physical computing devices on Kickstarter and got an early set. I had some fun exploring it, but the software and support materials weren"t quite ready at the time and I started a … [Continue reading ->](http://www.suppertime.co.uk/blogmywiki/2017/07/flotilla/)
