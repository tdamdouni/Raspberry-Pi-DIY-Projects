# Raspi-Sump Water level Monitoring

_Captured: 2016-12-24 at 21:08 from [www.linuxnorth.org](https://www.linuxnorth.org/raspi-sump/)_

Raspi-Sump is a sump pit water level monitoring system using a Raspberry Pi, an HC-SR04 Ultrasonic Sensor and written in Python. It monitors the water level in your sump pit and alerts you if the water level is getting too high, possibly indicating a sump pump problem. The [source code](https://github.com/alaudet/raspi-sump/) is available on GitHub.

![example raspi chart](https://www.linuxnorth.org/raspi-sump/images/raspi-chart.png)

If you would like notifications on changes, bugs, security issues regarding Raspi-Sump feel free to send me an email at [RaspiSump Notifications](mailto:alaudet@linuxnorth.org?Subject=Raspi_Sump%20Notifications%20Subscribe) asking to subscribe to updates.

I will always bcc you on the email so that your info is not visible to other users. I would never share your email address with anyone.....period.

Alternatively, you can follow me on [Twitter](https://twitter.com/Al_Audet) and I will tweet any changes there as well.

### Install Raspi-Sump

### Requirements

\- RaspberryPi (Any model)  
\- Python 2 and 3 compatible  
\- [RPi.GPIO module](https://pypi.python.org/pypi/RPi.GPIO/) for Raspberry Pi (automatically installed)  
\- [hcsr04sensor module](https://github.com/alaudet/hcsr04sensor) (automatically installed)  
\- Matplotlib and Numpy required if you want to graph output of the csv file.

### Current Features

\- Packaged install with PIP.  
\- pre defined interval monitoring of sump pit water level.(time interval is configurable)  
\- Error handling to compensate for fringe readings.  
\- Readings logged to csv file.  
\- Automated SMS Email Alerts if water depth exceeds a predifined level in the sump pit.  
\- Chart of current sump activity (seen above).  
\- Monitor the raspi-sump process and if it is stopped automatically restart it. (if running raspi-sump as a continuous process)  
\- Configure variables for your sump pump and alerts in a seperate configuration file. (raspisump.conf)  
\- Choose between metric or imperial measurements.  
\- create charts for viewing today's waterlevel and past days waterlevels on the local webserver of your Raspberry Pi  
\- Rate limit SMS Email Alerts  
\- Set alerts to alert you on low water (or other liquid) levels

### Sump Pit Setup

\- 4 wires connected from HC-SR04 sensor to the RaspberryPi  
\- Sensor mounted on sliding wood platform

### Pin Setup HC-SR04 to RaspberryPi

\- VCC to 5V  
\- Ground to ground  
\- Trig to GPIO 17  
\- Echo to GPIO 27 (with voltage divider)

![raspberry pi diagram](https://www.linuxnorth.org/raspi-sump/images/raspi-sump-wiring.jpg)

### Voltage Divider

It is essential to add a voltage divider on the wire connecting the Echo pin on the sensor, to the the GPIO pin on the pi. The sensor sends a 5V current through the wire and the GPIO pin is only rated for 3.3V. Not using a voltage divider can damage your Raspberry Pi. I used a 470 Ohm and a 1K Ohm resistor with the 1K connecting Echo and Ground. Voltage is actually a touch higher at 3.4V but I believe it to be within a tolerable level.

The following image illustrates very well how the voltage divider works.

![voltage divider wiring](https://www.linuxnorth.org/raspi-sump/images/voltage_divider.jpg)

The 470 Ohm resister is on top and the 1K resistor is on the bottom. The wires to the right go to the Pi and the ones to the left go to the sensor. The orange wire is the Echo wire and you can see it is connected right at the center of the two connected resistors. The yellow wire goes to Ground on the Pi. There are plenty of diagrams that you can find explaining voltage dividers but this picture provided by github user @rhiller was very helpful in seeing it in practice. Thanks to @rhiller for taking the time to answer many questions. He also has a sump pump monitoring project called [pi-distance](https://github.com/rhiller/pi-distance) on Github that you can check out.

### Sensor Installation

[HC-SR04](https://www.linuxnorth.org/raspi-sump/images/hc-sr04.jpg) sensor mounted to plastic bracket on wood strapping. [HC-SR04 User Manual (3.5MB pdf)](https://www.linuxnorth.org/raspi-sump/HC-SR04Users_Manual.pdf)

![](https://www.linuxnorth.org/raspi-sump/images/hc-sr04a.jpg)

![](https://www.linuxnorth.org/raspi-sump/images/hc-sr04b.jpg)

## View of the Open Sump Pit

![](https://www.linuxnorth.org/raspi-sump/images/sump_open_wiring.jpg)

## Finished View with Raspberry Pi on the Wall

![](https://www.linuxnorth.org/raspi-sump/images/lid_on.jpg)

![](https://www.linuxnorth.org/raspi-sump/images/pi_wall.jpg)

## Raspi-Sump reporting time and level (cm) in real time every 60 seconds

![](https://www.linuxnorth.org/raspi-sump/images/real_time.png)

## Raspi-Sump SMS Email Alert

![](https://www.linuxnorth.org/raspi-sump/images/cli.jpg)
