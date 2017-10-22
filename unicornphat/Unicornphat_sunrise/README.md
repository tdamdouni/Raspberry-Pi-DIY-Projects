# Unicornphat_sunrise
## Description
A little script, that changes the unicornphat's color based on color temperatures to simulate a sunrise from 1000 K to 5000 K color-temperature.
The calculation itself was adapted from [Tanner Helland](http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/). 
## Use
Simply use the script on your RaspberryPi/UnicornPHATt. If UnicornHAT is used, you have to adapt the unicornsettings in the top of the script. 
The duration of the 'sunrise' can be influenced by changing the **delay** and/or **steps** parameters. 

### Application
I use this function in a script that check's twitter messages from a specific user and extracts a wakeuptime (like '08:00') from there. At that time, the the script will then invoke the sunrise and you have a nice sunrise_alarm.py. 
