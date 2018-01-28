# Manual installation on a Raspberry Pi

_Captured: 2017-11-09 at 23:46 from [home-assistant.io](https://home-assistant.io/docs/installation/raspberry-pi/)_

[Edit this page on GitHub](https://github.com/home-assistant/home-assistant.github.io/tree/current/source/_docs/installation/raspberry-pi.markdown)

This installation of Home Assistant requires the Raspberry Pi to run [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/). The installation will be installed in a [Virtual Environment](https://home-assistant.io/docs/installation/virtualenv) with minimal overhead. Instructions assume this is a new installation of Raspbian Lite.

Connect to the Raspberry Pi over SSH. Default password is `raspberry`. You will need to enable SSH access. The Raspberry Pi website has instructions [here](https://www.raspberrypi.org/documentation/remote-access/ssh/).
    
    
    $ ssh pi@ipadress
    

Changing the default password is encouraged.
    
    
    $ passwd
    

Update the system.
    
    
    $ sudo apt-get update
    $ sudo apt-get upgrade -y
    

Install the dependencies.

Add an account for Home Assistant called `homeassistant`. Since this account is only for running Home Assistant the extra arguments of `-rm` is added to create a system account and create a home directory.

Next we will create a directory for the installation of Home Assistant and change the owner to the `homeassistant` account.

Next up is to create and change to a virtual environment for Home Assistant. This will be done as the `homeassistant` account.

Once you have activated the virtual environment you will notice the prompt change and then you can install Home Assistant.

Start Home Assistant for the first time. This will complete the installation, create the `.homeassistant` configuration directory in the `/home/homeassistant` directory and install any basic dependencies.

You can now reach your installation on your Raspberry Pi over the web interface on <http://ipaddress:8123>.
