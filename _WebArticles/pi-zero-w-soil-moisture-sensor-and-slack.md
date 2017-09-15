# Pi Zero W Soil Moisture Sensor and Slack

_Captured: 2017-09-12 at 17:58 from [www.raspberrycoulis.co.uk](https://www.raspberrycoulis.co.uk/diy-hacks/pi-zero-w-soil-moisture-sensor-and-slack/)_

![Raspberry Pi Zero Soil Moisture Sensor with Slack Notifications](https://i1.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2017/09/pi0_soil_sensor.jpg?w=960&ssl=1)

We recently moved offices at work as we have been expanding over the last 12 months, and outgrew our old office. Our new office is fantastic and has its very own Garden Room, where we have a picnic bench, astro-turf flooring and, until recently, two office plants.

![The ](https://i0.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2017/09/garden-room-LucasEdition.jpg?w=1536&ssl=1)

However, as with any office there are times where people neglect the simple things and our office plants were the unfortunate victims here. Everybody was under the assumption that somebody else was watering the plants, which sadly was not the case. After a number of weeks without water, one of our office plants died and ended up in the compost heap in the sky but the other was clinging to life, and with some watering has slowly returned to its former glory.

Now when you work for a [software development company](https://silktide.com/?r=raspberrycoulis), if there is an excuse to use something involving tech or code then we often will. Throwing myself into the mix, and my passion for Raspberry Pi, then if I have the excuse to use one at work then I will!

## Raspberry Pi soil moisture sensor

I've come across Raspberry Pi soil moisture sensors before, but I've never really had the use-case to buy one. Until now. Our office plants plant means a lot to our MD's wife, as they used to be in her office and she donated them to us when she moved out. As you can imagine, she was not best pleased that one of the plants died and I thought that this would be the perfect case to whip out a spare office Raspberry Pi and put together a simple Python script that uses our preferred in-work chat tool, Slack.

For those of you who have not heard of [Slack](https://slack.com), it is a chat system that is perfect for in-office communication, especially if you want to cut out the unnecessary email conversations. It is also useful for collaboration - in fact, I'm in a Slack group with other Raspberry Pi fans and coders including the talented likes of [Alex Ellis](https://blog.alexellis.io/?r=raspberrycoulis), [Richard Gee](https://twitter.com/rgee0) and [Ryan Walmsley](https://twitter.com/ryanteck) to name but a few and it is really helpful when bouncing ideas of each other.

## Inspiration for the project

After a quick search online for Raspberry Pi soil moisture sensors projects, I came across a [relatively old post on ModMyPi](https://www.modmypi.com/blog/raspberry-pi-plant-pot-moisture-sensor-with-email-notification-tutorial/?r=raspberrycoulis) about using the soil moisture sensor in combination with email to notify you when to water the plant.

I thought that this would be a great place to start, so I took parts from their script and added my own parts to help call a Slack webhook to send notifications to our office Slack channel whenever the soil moisture is too low.

## Required parts

For my project, I used the following parts:

## Connect the soil moisture sensor

This is very simple. There are two connections on the fork shaped part (that goes into the soil) marked positive and negative - simply connect these to the sensor module part. It doesn't matter which of the two pins you use. Whilst there are 4 pins on the part of the sensor module that connects to your Raspberry Pi, you only need 3: VCC, GND and D0. Connect these as follows:

  * VCC to pin 1 on the Pi (3.3v)
  * GND to pin 9 on the Pi (Ground)
  * D0 to pin 11 on the Pi (GPIO 17).

If connected corrrectly, you should see at least 1 LED light up on the sensor module. If you then stick the fork end into a glass of water (only the prongs, not the entire module!), you should then see a second LED light up on the sensor module. If you don't, go back and check your connections - try swapping the two from the fork to the sensor module around first.

### Calibrate the soil moisture sensor

There is a small potentiometer on the sensor module that allows you to calibrate the sensitivity of the sensor. The best way to do this is to insert the prongs of the fork into the soil and then slowly turn the potentiometer until 1 LED goes off, this means that when the soil moisture drops to this level, the script will be triggered and alert you via Slack that it needs watering.

## Clone my code on GitHub

Obviously you'll need the code, so clone this on your Raspberry Pi by running this in your command line:

If you want to see what the code looks like, then you can also use this:

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455
#!/usr/bin/python###################################################################################### This was inspired by a guide on ModMyPi (http://bit.ly/mmpsms). ## ## Use a soil moisture sensor and a Raspberry Pi to monitor the soil in a plant pot ## and warn the office, via Slack, that it needs watering. ## ## By Wesley Archer (@raspberrycoulis - https://www.raspberrycoulis.co.uk) ####################################################################################### Import the necessary libraries:import RPi.GPIO as GPIOimport timeimport httplib, urllibimport urllib2import json# Slack webhook - get this from https://api.slack.com/custom-integrations/incoming-webhookswebhook_url = "ADD_HERE"# This is the function that calls the Slack webhook to notify you:def postToSlack():data = '{"attachments":[{"fallback":"Water plant!","pretext":"The soil is too dry!","color":"#cc0000","fields":[{"title":"The Garden Room plant needs watering!","short":false}]}]}'slack = urllib2.Request(webhook_url, data, {'Content-Type': 'application/json'})post = urllib2.urlopen(slack)post.close()# This is the function that checks if the soil is moist or dry:def moisture(channel):if GPIO.input(channel):#print "Soil is dry!" # Uncomment to show feedback in consolepostToSlack()else:#print "Soil is moist" # Uncomment to show feedback in consolereturn "Soil is moist"# Set the GPIO mode:GPIO.setmode(GPIO.BCM)# Define the GPIO pin that the moisture sensor (D0 on the sensor) is connected to:channel = 17# Set the GPIO pin above as an input:GPIO.setup(channel, GPIO.IN)# Check whether the GPIO pin is high or low. The bouncetime is the minimum time between two callbacks (default=300) in millseconds:GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)# This line assigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function:GPIO.add_event_callback(channel, moisture)# Run the code in an infinite loop and tells the script to wait 0.1 seconds, this is so the script doesnt hog all of the CPU:while True:time.sleep(0.1)

### Edit the code to use your Slack webhook

After you have created your webhook integration in Slack, you'll need to edit the Python script accordingly:

Find the variable on line 20 called `webhook_url` and then replace `"ADD_HERE"` with your Slack webhook URL. Then save and exit:

Your script is now good to go.

![When your plant needs watering, the Pi will send you Slack messages accordingly](https://i2.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2017/09/IMG_1509.jpg?w=747&ssl=1)

> _When your plant needs watering, the Pi will send you Slack messages accordingly_

## Running the script automatically on boot using systemd

In order to run the script automatically when the Raspberry Pi boots, I recommend using systemd to run it as a service:

Then add the following:

1234567891011
[Unit]Description=Plant soil moisture sensor serviceAfter=multi-user.target[Service]Type=idleExecStart=/usr/bin/python /home/pi/plant-hydro-slack/dry-to-slack.py > /home/pi/plant-hydro-slack/dry-to-slack.log 2>&1Restart=always[Install]WantedBy=multi-user.target

The parts to check are the `ExecStart` command as this assumes the `dry-to-slack.py` script is located in `/home/pi/plant-hydro-slack` so please update accordingly if you have installed the script in a different location.

Once you have done this, `Ctrl+X` to exit and `Y` to save then run:

You can `sudo reboot` or simply run `sudo systemctl start moisturesensor.service` to start the script. Check the status by running `sudo systemctl status moisturesensor.service`.
