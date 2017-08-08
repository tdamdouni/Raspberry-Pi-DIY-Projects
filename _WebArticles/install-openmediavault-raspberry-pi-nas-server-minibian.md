# Install OpenMediaVault Raspberry Pi NAS Server Minibian

_Captured: 2017-05-19 at 11:41 from [www.htpcguides.com](https://www.htpcguides.com/install-openmediavault-raspberry-pi-nas-server-minibian/)_

![raspberry-pi-openmediavault](https://www.htpcguides.com/wp-content/uploads/2015/03/raspberry-pi-openmediavault.png)

[OpenMediaVault](http://www.openmediavault.org/) is an excellent NAS software solution. It sports a beautiful web interface to manage all of your services, hard drives, users and more. There is a great plugin system which allows you to install software for usenet, torrent and media management. For the Raspberry Pi 2 there is even a Plex Media Server plugin and OwnCloud. There is both a step by step install guide and a prepared image for the Raspberry Pi 2 at the bottom for those who want to give it a go, I request you share the post if you use the image link to help spread the word of this great software. I have used [Minibian](https://www.htpcguides.com/lightweight-raspbian-distro-minibian-initial-setup/) as a base and recommend only installing OpenMediaVault on a fresh, unaltered image. This guide will not always work on the Raspberry Pi B+ or earlier devices (because of php issues - see the comments). The image does not work on the B+ but is reported to work with Raspberry Pi Model A.

If you are trying to figure out which hardware would work best for you, consider reading the [Pi benchmarks](https://www.htpcguides.com/raspberry-pi-vs-pi-2-vs-banana-pi-pro-benchmarks/).

**Updated** for Erasmus version of OpenMediaVault

Pi UnitProcessorRAMRAM BusNetworkWiFiUSBSATACost

[Raspberry Pi 3](https://www.htpcguides.com/product/k-raspberry+pi+3/US/htpcguidestext-20/)
1.2 GHz ARMv8  
Quad Core
1 GB DDR2
450 MHz
100 Mbit
Yes
4
No
[$35](https://www.htpcguides.com/product/k-raspberry+pi+3/US/htpcguidestext-20/)

[Raspberry Pi 2](https://www.htpcguides.com/product/k-raspberry+pi+2/US/htpcguidestext-20/)
900 MHz ARMv7  
Quad Core
1 GB DDR2
450 MHz
100 Mbit
No
4
No
[$35.00](https://www.htpcguides.com/product/k-raspberry+pi+2/US/htpcguidestext-20/)

[Raspberry Pi](https://www.htpcguides.com/product/k-raspberry+pi/US/htpcguidestext-20/)
700 MHz ARMv6  
Single Core
512 MB SDRAM
400 MHz
100 Mbit
No
4
No
[$25](https://www.htpcguides.com/product/k-raspberry+pi/US/htpcguidestext-20/)

[Banana Pi](https://www.htpcguides.com/product/k-banana+pi/US/htpcguidestext-20/)
1 GHz ARMv7  
Dual Core
1 GB DDR3
432 MHz
Gigabit
No
2
Yes
[$36.99](https://www.htpcguides.com/product/k-banana+pi/US/htpcguidestext-20/)

[Banana Pi Pro](https://www.htpcguides.com/product/k-banana+pro/US/htpcguidestext-20/)
1 GHz ARMv7  
Dual Core
1 GB DDR3
432 MHz
Gigabit
Yes
2
Yes
[$45.00](https://www.htpcguides.com/product/k-banana+pro/US/htpcguidestext-20/)

## Install OpenMediaVault Raspberry Pi

Add the OpenMediaVault repository and grab the gpg key
    
    
    echo "deb http://packages.openmediavault.org/public erasmus main" | sudo tee -a /etc/apt/sources.list.d/openmediavault.list
    wget -O - http://packages.openmediavault.org/public/archive.key | sudo apt-key add -

Update and install OpenMediaVault including a keyring fix
    
    
    sudo apt-get update
    sudo apt-get install openmediavault-keyring postfix -y --force-yes
    sudo apt-get install php-apc openmediavault -y --force-yes

General mail configuration I chose no configuration, MD arrays I chose all, run proftpd from inetd

### Install OpenMediaVault Extras Plugins

The OpenMediaVault Extras plugins has all of the goodies like CouchPotato, SickRage, SickBeard, NZBGet, Sabnzbd, Plex Media Server and Sonarr (should be added soon) so you will likely want this awesome repository.
    
    
    echo "deb http://packages.omv-extras.org/debian/ erasmus main" | sudo tee -a /etc/apt/sources.list.d/omv-extras-org-kralizec.list
    sudo apt-get update
    sudo apt-get install openmediavault-omvextrasorg -y --force-yes

Stop the apache2 service and disable it
    
    
    sudo service apache2 stop
    sudo update-rc.d apache2 disable
    sudo update-rc.d apache2 remove

Start nginx service
    
    
    sudo service nginx start

Try to access OpenMediaVault at http://ip.address, the default login is **admin** with password **openmediavault**

Initialize the OpenMediaVault system, this disables SSH but you can enable it again from the Web interface
    
    
    sudo omv-initsystem

Enable SSH again by granting the pi user SSH access to OpenMediaVault. Go to the OpenMediaVault web interface by opening a web browser and entering the IP address of the Raspberry Pi. The default user is **admin** and the password is **openmediavault**.

Once logged into the web interface go to **Access Rights Management** > **Users** > Choose the user **pi** and click on the **Edit** button

![OMV_access-rights-management](https://www.htpcguides.com/wp-content/uploads/2016/01/OMV_access-rights-management.png)

Go to the **Groups** tab and check the button next to **SSH**, click **Save**.

![OMV_pi_ssh](https://www.htpcguides.com/wp-content/uploads/2016/01/OMV_pi_ssh.png)

You will be asked if you would like to apply the changes, click **Apply**.

![OMV_apply_changes](https://www.htpcguides.com/wp-content/uploads/2016/01/OMV_apply_changes.png)

## Hard drive and storage tweaks

SSH to the Pi. Turn off swap to save excessive SD card writes
    
    
    sudo swapoff -a

Disable caching processes to save the SD card's life (not necessary according to an OMV developer if you use the flashmemory plugin)
    
    
    sudo update-rc.d rrdcached disable
    sudo update-rc.d collectd disable
    sudo monit stop rrdcached
    sudo monit stop collectd

Setup security patch upgrades to install automatically with a cronjob that will run every night
    
    
    sudo apt-get install unattended-upgrades -y
    crontab -l | { cat; echo "@daily apt-get update && unattended-upgrade"; } | crontab -

Install the openmediavault-flashmemory plugin in the web interface which will also extend the life of your sd card.

OpenMediaVault at http://ip.address, the default login is admin with password openmediavault.

You should add DNS servers (8.8.8.8 is a good choice) under System -> Network -> DNS Servers in the OpenMediaVault gui.

If you use the prepared Pi 2 image below, the SSH login is root and password is htpcguides. The login for the web interface is admin with password openmediavault, use raspi-config to expand the file system after flashing the img. It has been reported to work on the Raspberry Model A and should work on Model B and B+ as well but it may mess with your ethernet changing eth0 to eth1.

If it doesn't work you can grab the official images from the [OpenMediaVault](http://www.openmediavault.org/download.html) site which require a 4 GB SD card.

If you use the image you may have to remove persistent rules with a keyboard, use this command when logged in as root
    
    
    sudo rm /etc/udev/rules.d/70-persistent-net.rules

Update OpenMediaVault on the Raspberry Pi in SSH
    
    
    omv-update
    omv-upgrade
