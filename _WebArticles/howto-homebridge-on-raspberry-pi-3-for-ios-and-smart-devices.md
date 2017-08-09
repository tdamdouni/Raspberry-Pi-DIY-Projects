# HowTo Homebridge on Raspberry Pi 3 for iOS and Smart Devices

_Captured: 2017-05-06 at 10:07 from [blog.bram.co.nl](https://blog.bram.co.nl/howto-homebridge-on-raspberry-pi-3-for-ios-and-smart-devices/)_

![HowTo Homebridge on Raspberry Pi 3 for iOS and Smart Devices](https://blog.bram.co.nl/wp-content/uploads/2016/04/homekit.jpg)

In the Easter weekend I suffered some eye injury on both my left and right eye. My sight went fro 100% back to 5% on the left and right eye. From that day i knew it was going to be a long recovery with several surgery's. As a tech guy i already have some Smart Devices and wanted to use them with my Apple Devices. Considering the HomeKit does not support mutch I did some research and found HomeBridge. My devices currently connected to my home network are:

  * Philips Hue lights
  * Kodi MediaCenter
  * NetAtmo Weather Station
  * IFTTT
  * Temp Sensors connected to my Pi

Let's use Siri to talk with those devices and get information out of them! Too bad Apple does only support Hue, this is where HomeBridge comes in Handy. HomeBridge serves as an extra layer to control devices through plugins with Siri from your iOS device like iPad / iPhone.

I'm running a Raspberry Pi 3 already as a private DNS (to manage my devices by DNS instead of IP address (Kodi, Printer, Switches, Server(s), and so on..), this device can do a lot more.

**Installing HomeBridge (Raspberry Pi 3)**

First of all update your Raspbian installation

> sudo apt-get update
> 
> sudo apt-get upgrade

This can take a while…

Next we start installing NodeJS and a prereq for HomeBridge

> wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv6l.tar.gz
> 
> tar -xzf node-v4.0.0-linux-armv7l.tar.gz
> 
> cd node-v4.0.0-linux-armv7l

Now we have downloaded NodeJS and extracted it. Next step is to copy all the files to /usrlocal Use the following command:

> sudo cp -R * /usr/local/

The -R stands for Recursive so we will copy all files in all directorys. After we have copied them we have nodejs installed. You can check your version with

> node -v

Let's continue with the installation of the PreReqs.

> sudo apt-get install libavahi-compat-libdnssd-dev

Now we have the PreReq qe can install **_Homebridge_**

As we already installed NodeJS, we now have some new commands available. With these commands we can install the Homebridge server.

This can take some time, on my RPi 3 it took about 5 to 10 minutes. When the installation is done we can start Homebridge by entering the following command:

When you run this command it will try to start Homebridge, this will fail because we have no plugins installed and a valid config.json file with the homebridge configuration. You will see a similar error "_**No plugins found. See the README for information on installing plugins."**_

**Homebridge Config.json**

Now we have installed Homebridge we need a configuration for Homebridge. Also if we install any plugin we have to add it in the config file.

> cd /home/pi/.homebridge  
nano config.json

Paste the following code

`  
{  
"bridge": {  
"name": "Homebridge",  
"username": "CC:22:3D:E3:CE:30",  
"port": 51826,  
"pin": "031-45-154"  
},`

"description": "This is my Homebridge Config file",

"accessories": [

],

"platforms": [

]  
}

Now we have the default config ready, but we still need a plugin to make it work properly. I did setup my NetAtmo weather station, you can use the following commands to setup your NetAtmo plugin, or download any other NPM plugin and follow the this guide as a how to. Make sure to download the right config example from the NPM website and replace the NetAtmo config with your plugin config file. This config is provided on the NPM Plugin website.

**Configure Netatmo**

Search for the Homebridge-netatmo NPM website and you will get information on how to install the plugin. This is also outlined below. First we have to install the plugin, and next we have to modify the config file. Let's start by installing the plugin.

> sudo npm install -g homebridge-netatmo

This will take a few seconds to install, after this is done we only have to configure this. On the website you will see an example config. You can use this one and modify it for you NetAtmo setup. Enter your Username and Password, and create an Application through the NetAtmo dev website so you can allow homebridge to connect to the NetAtmo API.

The config will look like the config below:  
`  
{  
"bridge": {  
"name": "Homebridge",  
"username": "CC:22:3D:E3:CE:30",  
"port": 51826,  
"pin": "031-45-154"  
},`

"description": "This is my Homebridge Config file",

"accessories": [

],

"platforms": [  
{  
"platform": "netatmo",  
"name": "netatmo weather",  
"ttl": 5,  
"auth": {  
"client_id": "CREATE ID AT https://dev.netatmo.com/",  
"client_secret": "CREATE SECRET AT https://dev.netatmo.com/",  
"username": "your netatmo username",  
"password": "your netatmo password"  
}  
}

]  
}

If we now start Homebridge we will see there is a NetAtmo Weather Station plugin loaded. Now you can start your Apple iOS application to connect to HomeBridge.

I'm using **Insteon+ **add a new device and it will find your Homebridge. Connect to Homebridge and enter the pin code in the config or check your SSH session to your RPi. Now you can start configuring the Siri Commands and create your Home with Rooms / Scenes and so on.

**Autostart / start Homebridge**

The final thing we need to do is to create an init.d script to start Homebridge. We use the following commands to create a script and add it to the defaults so it will start with a reboot from your RPi.

> sudo nano /etc/init.d/homebridge
> 
> Paste the following code into this file and chmod it to 755 so we can execute it.  
`  
#!/bin/sh  
### BEGIN INIT INFO  
# Provides: homebridge  
# Required-Start: $network $remote_fs $syslog  
# Required-Stop: $remote_fs $syslog  
# Default-Start: 2 3 4 5  
# Default-Stop: 0 1 6  
# Short-Description: Start daemon at boot time  
# Description: Enable service provided by daemon.  
### END INIT INFO`
> 
> dir="/home/pi"  
cmd="DEBUG=* /usr/local/bin/homebridge"  
user="pi"
> 
> name=`basename $0`  
pid_file="/var/run/$name.pid"  
stdout_log="/var/log/$name.log"  
stderr_log="/var/log/$name.err"
> 
> get_pid() {  
cat "$pid_file"  
}
> 
> is_running() {  
[ -f "$pid_file" ] && ps `get_pid` > /dev/null 2>&1  
}
> 
> case "$1" in  
start)  
if is_running; then  
echo "Already started"  
else  
echo "Starting $name"  
cd "$dir"  
if [ -z "$user" ]; then  
sudo $cmd >> "$stdout_log" 2>> "$stderr_log" &  
else  
sudo -u "$user" $cmd >> "$stdout_log" 2>> "$stderr_log" &  
fi  
echo $! > "$pid_file"  
if ! is_running; then  
echo "Unable to start, see $stdout_log and $stderr_log"  
exit 1  
fi  
fi  
;;  
stop)  
if is_running; then  
echo -n "Stopping $name.."  
kill `get_pid`  
for i in {1..10}  
do  
if ! is_running; then  
break  
fi
> 
> echo -n "."  
sleep 1  
done  
echo
> 
> if is_running; then  
echo "Not stopped; may still be shutting down or shutdown may have failed"  
exit 1  
else  
echo "Stopped"  
if [ -f "$pid_file" ]; then  
rm "$pid_file"  
fi  
fi  
else  
echo "Not running"  
fi  
;;  
restart)  
$0 stop  
if is_running; then  
echo "Unable to stop, will not attempt to start"  
exit 1  
fi  
$0 start  
;;  
status)  
if is_running; then  
echo "Running"  
else  
echo "Stopped"  
exit 1  
fi  
;;  
*)  
echo "Usage: $0 {start|stop|restart|status}"  
exit 1  
;;  
esac
> 
> exit 0

chmod with the following command:

> sudo chmod 755 /etc/init.d/homebridge

Next we have to tell the OS to start it at boot, we can do this with the following command

> sudo update-rc.d homebridge defaults

_**Enjoy your Homebridge setup on your RPi 3!**_

## EDIT 12-27-2016

For some reason my homebridge got killed after some hours, or some days or even after some minutes. I'm not sure why and was not in the mood to do research. I made a cronjob to check every hour if my homebridge is running (with the status), and if it was not running to just start it. You could set it to more ofter check for the status, like every 15 or even 5 minutes, but as i'm not checking every 5 minutes my iPhone or Apple Device for the Temps on my NetAtmo every hour was sufficient for me

You could also just run the _**/etc/init.d/homebridge restart**_ command to make sure it gets restarted or started. Script i made is a bit buggy so not posting it here
