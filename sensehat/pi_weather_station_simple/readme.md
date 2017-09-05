Pi Weather Station (Simple Sensor)
==================================

I recently published an article in Make Magazine for a Raspberry Pi Weather Station application using the Astro Pi Sense HAT board and Weather Underground. You can find the code for this project [here](https://github.com/johnwargo/pi_weather_station). As part of the process of publishing the article, Make's editors asked me what readers should do if they wanted to use a simple temperature sensor instead of the Sense HAT, that question drove the creation of this project. Just in case you're interested, there's a Tessel 2 version of this project as well [here](https://github.com/johnwargo/tessel_weather_station). 

This is a project for the Raspberry Pi that measures temperature and humidity then uploads the data to a Weather Underground weather station. For this project, I used a [DHT22 sensor from Adafruit](https://www.adafruit.com/product/385). To help you get started, Adafruit created [a nice overview of the sensor](https://learn.adafruit.com/dht/overview) and a [Python library the DHT22](https://github.com/adafruit/Adafruit_Python_DHT) plus a blog article that shows [how to wire the DHT22 to the Raspberry Pi](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview).
 
Required Components
-------------------

This project is very easy to assemble, all you need is the following parts, and they all connect together:

+ [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) - I selected this model because it has built in Wi-Fi capabilities. You can use one of the other models, but you'll need to also purchase a Wi-Fi module or run the device on a wired connection.
+ DHT22 temperature-humidity sensor - Since I used the Adafruit drivers for this project, it's probably best if you acquire one from [Adafruit](https://www.adafruit.com/products/385). Adafruit suggests adding a resistor to the circuit; when you buy the DHT22 from Adafruit, it's in there. 
+ Raspberry Pi Power Adapter. I used this one from [Amazon](http://amzn.to/29VVzT4). 

Hardware Assembly
-----------------

Connect the DHT22 to the Raspberry Pi using the instructions provided [here](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview). For easiest assembly, I soldered the components to a [Adafruit Perma-Proto HAT for Pi Mini Kit - No EEPROM](https://www.adafruit.com/products/2310) and attached it to the Raspberry Pi before putting it in a case.

Project Files
-------------

The project folder contains several files: 

+ `config.py` - This is the project's external service configuration file, it provides the weather station with details about your Weather Underground station.
+ `LICENSE` - The license file for this project
+ `readme.md` - This file. 
+ `start-station.sh` - Shell script to start the weather station process. 
+ `weather_station.py` - The main data collection application for this project. You'll run this application to read the DHT22 and post the collected data.   

Weather Underground Setup
-------------------------

Weather Underground (WU) is a public weather service now owned by the Weather Channel; it's most well-known for enabling everyday people to setup weather stations and upload local weather data into the WU weatherbase for public consumption. Point your browser of choice to [https://www.wunderground.com/weatherstation/overview.asp](https://www.wunderground.com/weatherstation/overview.asp) to setup your weather station. Once you complete the setup, WU will generate a station ID and access key you'll need to access the service from the project. Be sure to capture those values, you'll need them later.

Software Installation
---------------------

Download the Raspbian image from [raspberrypi.org](https://www.raspberrypi.org/downloads/raspbian/) then burn it to an SD card using the instructions found at [Installing Operating System Images](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).

Power up the Raspberry Pi. If you'll be using a Wi-Fi connection for your Pi, configure Wi-Fi access using [Wi-Fi](https://www.raspberrypi.org/documentation/configuration/wireless/).

Next, open a terminal window and execute the following commands:

	sudo apt-get update
	sudo apt-get upgrade

These commands update the Pi's software repository with the latest package information then upgrades the existing code in the Raspbian image to the latest versions.

Next, you'll need to install some support libraries used to install the Adafruit's DHT22 library. In the same terminal window, execute the following command:

	sudo apt-get install build-essential python-dev

**Note:** you may see a warning indicating that the `build-essential` package is already installed. That's expected, so you can ignore that one. I'm simply not sure whether that's pre-installed on all versions of Raspbian.

Download and install the Adafruit DHT Python library. Point the Pi's web browser to [https://github.com/adafruit/Adafruit_Python_DHT](https://github.com/adafruit/Adafruit_Python_DHT) and click the **Clone or Download** link on the right side of the page to download the library. Unzip the archive to the folder where you downloaded it then navigate your terminal window into that folder and execute the following command:

	sudo python setup.py install

You should see a bunch of text output in the terminal to let you know the installation is progressing. 

Project Software Installation
-----------------------------

Make a folder called `pi_weather_staton` in the pi user's home folder. to do this, open a terminal window and enter the following command: 

	mkdir pi_weather_station

Copy the project files from this repository into the folder that was just created.

Configuration
-------------

In order to upload weather data to the Weather Underground service, the application needs the station ID and station access key you created earlier in this setup process. Open the project's `config.py` in your editor of choice and populate the `STATION_ID` and `STATION_KEY` fields with the appropriate values from your Weather Underground Weather Station: 

	class Config:
    	# Weather Underground
    	STATION_ID = ""
    	STATION_KEY = ""

Refer to the Weather Underground [Personal Weather Station Network](https://www.wunderground.com/personal-weather-station/mypws) to access these values.

The project's main application file, `weather_station.py` uses several settings to control how the application operates. Open the file in your favorite text editor and look for the following line near the beginning of the file:

	# specifies how often to measure values from the DHT22 (in minutes)
	MEASUREMENT_INTERVAL = 10  # minutes

The `MEASUREMENT_INTERVAL` variable controls how often the application reads temperature measurements from the sensor. To change how often the application checks temperature values, change the value on the right of the equals sign on the second line.

If you’re testing the application and don’t want the weather data uploaded to Weather Underground until you're ready, change the value for `WEATHER_UPLOAD` to `True` (case matters, so it has to be `True`, not `true`):

	# Set to False when testing the code and/or hardware
	# Set to True to enable upload of weather data to Weather Underground
	WEATHER_UPLOAD = False

Testing the Application
-----------------------
  
To execute the data collection application, open a terminal window, navigate to the folder where you copied the project files and execute the following command: 

	python ./weather_station.py

The terminal window should quickly sprout the following output:

	########################################
	# Pi Weather Station (Simple Sensor)   #
	# By John M. Wargo (www.johnwargo.com) #
	########################################
	
	Initializing Weather Underground configuration
	Successfully read Weather Underground configuration values
	Station ID: YOUR_ID		
	Initialization complete!
 
If you see something like that, you're golden. If not, figure out what any error messages mean, fix things, then try again.

At this point, the application will start collecting data and uploading it to the Weather Underground every 10 minutes on the 10 minute mark (unless you changed the app's configuration to make the application work differently).

Starting The Project's Application's Automatically
--------------------------------------------------

There are a few steps you must complete to configure the Raspberry Pi so it executes the project's python application on startup. If you don't already have a terminal window open, open one then navigate to the folder where you extracted the project files. Next, you need to make the project's bash script files executable by executing the following command:

    chmod +x start-station.sh
    
`chmod` doesn't report anything to the terminal when it completes successfully, so no output is a good thing. If anything gets written to the console, pay attention to is because it's describing a problem, a typo or that you're in the wrong folder.

Next, you'll need to open the pi user's session autostart file using the following command:  

	sudo nano ~/.config/lxsession/LXDE-pi/autostart

**Note:** Case matters, so be sure to enter the command exactly as it's shown above. There's two L's in the command for example. 

When the file opens in the nano editor, you should see some existing content in the file. If nano opens, but displays an empty file, you may have typed the command incorrectly. 

Add the following lines to the end (bottom) of the file:

	@lxterminal -e /home/pi/pi_weather_station/start-station.sh	

To save your changes, press ctrl-o then press the Enter key. Next, press ctrl-x to exit the nano application.
  
Reboot the Raspberry Pi. When it restarts, both python processes should execute in a terminal window.

Revision History
----------------

None yet!

***

You can find information on many different topics on my [personal blog](http://www.johnwargo.com). Learn about all of my publications at [John Wargo Books](http://www.johnwargobooks.com). 
