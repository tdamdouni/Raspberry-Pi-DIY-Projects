# Build Yourself a Raspberry Pi Zero Availability Checker powered by a Raspberry Pi

_Captured: 2017-09-03 at 23:28 from [isticktoit.net](http://isticktoit.net/?p=1434)_

The Raspberry Pi Zero is still very hard to get - it seems to be constantly out of stock.  
So I made Raspberry Pi powered* Raspberry Pi Zero Checker: It scans Adafruit, Pimoroni and The Pi Hut for strings indicating stock and warns you with an annoying ‚alarm' sound. I also have a [PHP version](https://gist.github.com/girst/c7088bd94b777675d7e8) for my web server that also works very well.

*Note: any computer will do - but a Pi can be left on all the time without annoying fan noise or high power bill.

This is a very simple project both soft- and hardwarewise: Get your Pi online, automatically start the script on boot (rc.local or systemd) and plug in some speakers.  
If you do not want to get woken up in the middle of the night, you might want to add some code to not trigger the alarm after 22.00h for example.
    
    
    #!/bin/bash
    
    # (C) 2016 Tobias Girstmair,
    # released under the WTFPL License, see: http://www.wtfpl.net/txt/copying/
    
    # Checks the official distributors for stock of the Raspberry Pi Zero
    
    # Alarm Function
    alarm() {
    	echo $1 in stock
    	aplay warn.wav # put any wav file here
    	# speaker-test -f 800 -t sine # very annoying 800Hz sine wave - very effective in getting your attention
    }
    
    while true; do
    sleep 60; # test once every minute
    	# US: Adafruit
    	curl -A "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0" https://www.adafruit.com/products/2885 2>/dev/null | grep -A 1 '' |grep "IN STOCK" >/dev/null #"OUT OF STOCK"
    	[[ $? -eq 0 ]] && alarm "adafruit" || echo "adafruit out of stock"
    
    	# EU: Pimoroni
    	curl -A "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0" https://shop.pimoroni.com/products/raspberry-pi-zero 2>/dev/null | grep '' >/dev/null #'class="stock-level out-of-stock">'
    	[[ $? -eq 0 ]] && alarm "pimoroni" || echo "pimoroni out of stock"
    	# EU: The Pi Hut
    	curl -A "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0" http://thepihut.com/products/raspberry-pi-zero?variant=14062715972 2>/dev/null | grep 'Raspberry Pi Zero Only - Sold Out' >/dev/null
    	[[ $? -ne 0 ]] && alarm "thepihut" || echo "thepihut out of stock"
    done
    
    
