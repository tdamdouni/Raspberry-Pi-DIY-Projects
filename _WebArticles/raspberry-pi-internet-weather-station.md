# Raspberry Pi Internet Weather Station

_Captured: 2017-12-04 at 22:10 from [www.hackster.io](https://www.hackster.io/4DMakers/raspberry-pi-internet-weather-station-f960c4)_

![Raspberry Pi Internet Weather Station](https://hackster.imgix.net/uploads/attachments/377091/raspberry_pi_weater_station_PUHjsejHxT.png?auto=compress%2Cformat&w=900&h=675&fit=min)

The Raspberry Pi Internet Weather Station project displays the weather information such as temperature, humidity and successive weather forecasts. This project uses 4D Systems' 4DPi-35-II. 4DPi-35-II acts as the primary display of this RPi Project.

![](https://hackster.imgix.net/uploads/attachments/377094/blobid1509759255751.png?auto=compress%2Cformat&w=680&h=510&fit=max)

The 4DPi-35-II is a 3.5" 480x320 Primary Display for the Raspberry Pi, which plugs directly on top of a Raspberry Pi and displays the primary output which is normally sent to the HDMI or Composite output. It features an integrated Resistive Touch panel, enabling the 4DPi-35-II to function with the Raspberry Pi without the need for a mouse.

Communication between the 4DPi-35-II and the Raspberry Pi is interfaced with a high speed 48Mhz SPI connection, which utilises an on-board processor for direct command interpretation and SPI communication compression, and features a customised DMA enabled kernel.

The 4DPi-35-II is designed to work with the Raspbian Operating System running on the Raspberry Pi, as that is the official Raspberry Pi operating system. It also supports the new PIXEL addition to Raspbian. _[...Know more](http://www.4dsystems.com.au/product/4DPi_35/)_

  * Raspberry Pi 3
  * **Software** • Python-tk module • Pywapi (Python weather API) • [Raspberry Pi Internet Weather Station by Jim](https://www.instructables.com/id/Raspberry-Pi-Internet-Weather-Station/)
  * Connect the 4DPi-35 to Raspberry Pi 3.
  * Recommended application to use for SSH connection: **Mobaxterm - https://mobaxterm.mobatek.net/download-home-edition.html** Steps in Raspberry Pi Weather Station 
  * Install the latest raspbian OS that is available on the [Raspberry Pi website .](https://www.raspberrypi.org/downloads/raspbian/) Follow the installation guide.
  * Set up network connections (https://www.raspberrypi.org/documentation/configuration/wireless/README.md), Enable SSH (https://www.raspberrypi.org/documentation/remote-access/ssh/README.md), change password and restart.
  * Connect to SSH, download and install the 4DPi-Kernel. Follow the instruction on the [4DPi-35 II Datasheet. ](http://www.4dsystems.com.au/productpages/4DPi-35/downloads/4DPi-35_datasheet_R_2_7.pdf)
  * When installation is successful, connect thru SSH and download python weather api.
  * When download is complete. Untar the file
  * sudo tar -xzvf pywapi-0.3.8.tar.gz 
  * Go to the folder
  * `cd pywapi-0.3.8`
  * Build
  * `sudo python setup.py build`
  * Install
  * `sudo python setup.py install`
  * Go back to the folder /home/pi
  * `cd ~`
  * Reconfigure tzdata
  * `dpkg-reconfigure tzdata`
  * Download he Raspberry Pi Internet Weather Station by
  * `wget http://www.instructables.com/files/orig/FAQ/7BWL/I1NULEIL/FAQ7BWLI1NULEIL.zip`
  * Unzip the file
  * `sudo unzip FAQ7BWLI1NULEIL.zip`
  * Go to the folder
  * `cd Weather`
  * Open the file weather.py
  * sudo nano weather.py 
  * Look for the line # Larger Display and put """ before the line to uncomment and look for the line tmdateYPosSm = 8 # Time & Date Y Position Small and delete the """ below. This will use the small display. It should look like the code below.
  * `"""` ` # Larger Display` ` self.xmax = 800 - 35` ` self.ymax = 600 - 5` ` self.scaleIcon = True # Weather icons need scaling.`` self.iconScale = 1.5 # Icon scale amount.` ` self.subwinTh = 0.05 # Sub window text height` ` self.tmdateTh = 0.100 # Time & Date Text Height` ` self.tmdateSmTh = 0.06` ` self.tmdateYPos = 10 # Time & Date Y Position` ` self.tmdateYPosSm = 18 # Time & Date Y Position Small` ` """` ` # Small Display` ` self.xmax = 480 - 20`` self.ymax = 320 - 5` ` self.scaleIcon = False # No icon scaling needed.` ` self.iconScale = 1.0` ` self.subwinTh = 0.065 # Sub window text height` ` self.tmdateTh = 0.120 # Time & Date Text Height` ` self.tmdateSmTh = 0.075` ` self.tmdateYPos = 1 # Time & Date Y Position` ` self.tmdateYPosSm = 8 # Time & Date Y Position Small`
  * Look for the line `w = pywapi.get_weather_from_weather_com( '48085', units='imperial' )`
  * And change with `self.w = pywapi.get_weather_from_weather_com('ASNS0055', units='metric' )` This will change to the desired location by replacing the value '48085' to 'ASNS0055'and the units to be use from 'imperial' to 'metric'. You can find your location by visiting weather.com. 
  * Save the file,
  * Ctrl + x Press Y, and enter. 
  * Test the file by typing,
  * `python weather.py`
  * If all are correct, set to run after boot up. Edit the file .bashrc, this will be executed when you open the terminal. Go to the bottom of the file and add the lines below. Save and exit.
  * `cd Weather` `python weather.py`
  * Then we need to open the terminal after the raspberry pi boots up. To do this type the code below.
  * `sudo nano .config/lxsession/LXDE-pi/autostart`
  * Go to the bottom of the last line and add the line below. Save and exit.
  * `@lxterminal`
