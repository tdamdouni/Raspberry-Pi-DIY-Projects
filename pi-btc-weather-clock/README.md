#Pi BTC Weather Clock
#####Bitcoin Weather Clock for your Raspberry Pi

Want a spiffy display that tells you the time, weather and bitcoin price? Got an extra RaspBerry Pi laying around? Let's do this!

Note: This project will change background colors on the span of a few minutes, as well as slightly zoom in and out the display a little. This is both for effect and to prevent burn-in.

![alt text](http://s32.postimg.org/5ffoae6xx/pibtcweatherclock.png "Pi BTC Weather Clock")

* * *

## Items needed

+ Raspberry Pi (running the latest Raspbian)
+ Official Raspberry Pi Touchscreen (or other HDMI display)
+ WiFi Adapter
+ Internet connection
+ (Optionally) Wireless Keyboard and Mouse for setup

## Instructions

Note: All of these commands should be run on your Raspberry Pi!

### Updating your Raspberry Pi

It's a good idea to make sure your Raspberry Pi is running the latest Raspbian for this project to work:

1. sudo apt-get update
2. sudo apt-get upgrade

If you plan on using the Official Raspberry Pi Touchscreen, you'll likely need to rotate the screen for your display (on the original touchscreen model):

1. Open /boot/config.txt
2. Add lcd_rotate=2 to the bottom.


### Cloning

Clone this repository with `git clone https://github.com/jakeday/pi-btc-weather-clock.git`.


### Configuring your Display

Open `js/app.js` and find the following section at the top:

```javascript
/*
 * BEGIN CONFIG VARIABLES
 */

// Yahoo WOEID code
// Find your WOEID code at http://zourbuth.com/tools/woeid/
var woeid = 12774129;

// Your temperature unit measurement
// 'c' for Celcius, and 'f' for Fahrenheit
var unit = 'f';

// Yahoo! query interval (milliseconds)
var waitBetweenWeatherQueries = 900000;

// Bitcoin price query interval (milliseconds)
var waitBetweenBitcoinPriceQueries = 300000;

// Default zoom level. Transitions from 0.9 to 1.1 (90% to 110%)
var zoom = 1.0;

/*
 * END CONFIG VARIABLES
 */
```

Adjust these variables to match the settings you prefer.

### Configuring your Raspberry Pi

You'll want to follow these steps to get the most out of your display!

#### Set Locale and Timezone

Set your locale and timezone so your time is correct.

`sudo raspi-config`

#### Disable Screen Sleep

We need to disable screen sleep to prevent the display from turning off after the timeout.

`sudo nano /etc/lightdm/lightdm.conf`

Add the following lines to the [SeatDefaults] section:

```bash
xserver-command=X -s 0 dpms
```

#### Install Unclutter

Unclutter hides the mouse cursor when no movement is detected. This prevents the cursor from showing on the display.

`sudo apt-get install unclutter`

#### Install Midori

Midori is the lean WebKit browser that we will use to run our display.

`sudo apt-get install midori`

#### Auto-start Unclutter and Midori

1. Create a new directory at `~/.config/autostart`
2. `cd ~/.config/autostart`
3. `nano unclutterStartup.desktop` - Add the below lines and then save.

	```
	[Desktop Entry]
	Type=Application
	Exec=unclutter -idle 0.1
	```
5. `nano midoriStartup.desktop` - Add the below lines and then save.

	```
	[Desktop Entry]
	Type=Application
	Exec=midori -e Fullscreen -a file:///home/pi/pi-btc-weather-clock/index.html
	```

Your Raspberry Pi will now launch our display when it boots!

#### Schedule Screen Sleep (Optional)

If you want your display to turn off during certain hours, you can do so with cron jobs.

1. Set display scripts to executable
	
	```bash
	cd pi-btc-weather-clock
	chmod +x displayOff.sh
	chmod +x displayOn.sh
	```

2. Run `crontab -e` and add cronjobs to the end using the provided scripts. The following lines shut off the display at 11:00PM each night and turn it back on at 7:00AM.
	
	```
	0 23 * * * /home/pi/pi-btc-weather-clock/displayOff.sh
	0 7 * * * /home/pi/pi-btc-weather-clock/displayOn.sh
	```

## Credit

Weather icons by Lukas Bischoff and Erik Flowers https://github.com/erikflowers/weather-icons. Icons licensed under [SIL OFL 1.1](http://scripts.sil.org/OFL).

Time formatting by [Moment.js](http://momentjs.com/)

Weather data retrieved using Yahoo! Weather API.

Project is a cleaned up, slimmed down, and enhanced version of Pi Kitchen Dashboard (https://github.com/userexec/Pi-Kitchen-Dashboard).

Bitcoin donations appreciated! 1JkpbAJ41W6SUjH9vCRDpHNNpecjPK3Zid
