# Web IDE on a Raspberry Pi

_Captured: 2017-08-24 at 23:39 from [www.espruino.com](http://www.espruino.com/Raspberry+Pi+Web+IDE)_

If you want to use Node-RED on your Raspberry Pi there is also a [Node-RED Tutorial](http://www.espruino.com/Puck.js+Node-RED).

We'd recommend you use a Raspberry Pi 3 - it's faster, and has Ethernet, WiFi and Bluetooth LE on-board. If you use a different Raspberry Pi you'll have to find a compatible Bluetooth LE adaptor and plug it in.

## Initial Pi Setup

If you've got a Raspberry Pi with an up to date OS and a command primpt (either via network, or with a monitor & keyboard) then you can skip this bit.

  * Follow the instructions on that site to copy it to an SD card for your Raspberry Pi
  * Open the SD card on your computer, and go to the `boot` drive that appears. Add an empty file called `ssh` with no extension (as of Nov 2016 this is needed to enable SSH).
  * Connect your Pi up to Ethernet and Power, and wait a minute
  * On Linux or MacOS: Type `ssh pi@rasbperrypi`
  * If you can't connect, check your router's configuration page - under `connected devices` it might show `raspberrypi` and you can use the IP address from that.
  * When prompted, enter `raspberry` as the password.
  * You should now have a command-prompt showing `pi@raspberrypi`
  * You can now type `sudo raspi-config` to set up your Pi in more detail (if you want to).

## Setting up the IDE Server

  * First, we need to set the Pi up to use the latest version of node.js. Enter the following command:
    
    
    curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -

  * Then type `sudo apt-get install nodejs bluetooth bluez libbluetooth-dev libudev-dev` and press `Y` and `Enter` when asked. This will install node.js as well as some system libraries needed for bluetooth.

  * Now install the Web IDE via NPM:
    
    
    sudo npm install -g espruino-web-ide

This will probably give some errors, but should soldier on and complete successfully.

  * And finally you need to give node.js the permissions needed to access Bluetooth.
    
    
    sudo setcap cap_net_raw+eip $(eval readlink -f `which node`)

## Using the Web IDE from Raspberry Pi

On the Pi, all you need to do is run `espruino-server`

Now, connect to the Pi on port `8080` by typing `http://raspberrypi.local:8080` into your web browser's address bar.

If you click the orange connect icon in the top right, you should now see a list of devices that you can connect to. Click one of them and you'll be able to program your Pi!

## Installing command-line tools

Once you've installed what's needed for the IDE server, you can also install command-line tools.

Just type:

You can now just type `espruino` to access your Espruino/Puck.js devices.

This page is auto-generated from [GitHub](https://github.com/espruino/EspruinoDocs/blob/master/puck/Raspberry Pi Web IDE.md). If you see any mistakes or have suggestions, please [let us know](https://github.com/espruino/EspruinoDocs/issues/new?title=puck/Raspberry Pi Web IDE.md).
