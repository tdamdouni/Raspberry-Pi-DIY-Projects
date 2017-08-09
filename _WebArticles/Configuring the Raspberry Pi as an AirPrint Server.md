# Configuring the Raspberry Pi as an AirPrint Server

_Captured: 2016-12-03 at 23:09 from [rohankapoor.com](https://rohankapoor.com/2012/06/configuring-the-raspberry-pi-as-an-airprint-server/)_

As a $35 pc with very low power requirements, the [Raspberry Pi](http://raspberrypi.org) is uniquely suited to serve many different purposes especially as an always-on low power server. When I first heard of the Pi, I was excited because I wanted it to become an AirPrint Server. This allows Apple's iOS line of devices to print to the Raspberry Pi which then turns around and prints to your regular printer via CUPS. I used my network laser printer for this, but there is no reason why you couldn't use a hardwired printer (over USB) on the Pi itself. About a month ago, I [succeeded](https://rohankapoor.com/2012/04/raspberry-pi-working-as-airprint-server/). Last week, I put up a [video demonstrating it](https://rohankapoor.com/2012/06/demonstration-raspberry-pi-running-as-an-airprint-server/), and today, I bring you the long-promised tutorial so that you can set it up yourself.

I'd like to thank Ryan Finnie for his research into [setting up AirPrint on Linux](http://www.finnie.org/2010/11/13/airprint-and-linux/) and TJFontaine for his [AirPrint Generation Python Script](https://github.com/tjfontaine/airprint-generate).

For the purpose of this tutorial, I used PuTTY to remotely SSH into my Raspberry Pi from my Windows 7 running Desktop PC.

To begin, let's login to the pi which uses the username `pi` and password `raspberry`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/02-Login-2.png)

We now have to install a whole bunch of packages including CUPS and Avahi. Before we do this, we should update the package repositories as well as update all packages on the Raspberry Pi. To update the repositories, we type in the command `sudo apt-get update`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/03-Update-Packages.png)

> _[Update Packages](https://rohankapoor.com/wp-content/uploads/2012/06/03-Update-Packages.png)_

Naturally, this doesn't quite work as expected, ending with an error requesting another package update. If you get this error just type in `sudo apt-get update` again.

![](https://rohankapoor.com/wp-content/uploads/2012/06/04-Update-Packages-2.png)

> _It seems the second time is the charm!_

![](https://rohankapoor.com/wp-content/uploads/2012/06/06-Update-Packages-4.png)

> _[Update Packages Again](https://rohankapoor.com/wp-content/uploads/2012/06/06-Update-Packages-4.png)_

Now we need to upgrade the packages installed on the Pi using the new repository information we've just downloaded. To do this, we type in `sudo apt-get upgrade`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/07-Upgrade-Packages.png)

> _[Upgrade Packages](https://rohankapoor.com/wp-content/uploads/2012/06/07-Upgrade-Packages.png)_

This will generate a list of packages to install and will then request approval before continuing. Just type in `y` and press enter to let it continue.

![](https://rohankapoor.com/wp-content/uploads/2012/06/08-Upgrade-Packages-2.png)

> _[Upgrade Packages Approval](https://rohankapoor.com/wp-content/uploads/2012/06/08-Upgrade-Packages-2.png)_

This will take a few minutes as it downloads and installs many packages. Eventually you will be returned back to a bash prompt.

![](https://rohankapoor.com/wp-content/uploads/2012/06/09-Upgrade-Packages-3.png)

> _[Upgrade Packages Complete](https://rohankapoor.com/wp-content/uploads/2012/06/09-Upgrade-Packages-3.png)_

At this point, we have to begin to install all of the programs that the AirPrint functionality will rely on: namely CUPS to process print jobs and the Avahi Daemon to handle the AirPrint announcement. Run `sudo apt-get install avahi-daemon avahi-discover libnss-mdns cups cups-pdf gutenprint pycups avahi python2` to begin this install.

![](https://rohankapoor.com/wp-content/uploads/2012/06/10-Install-New-Packages.png)

> _[Install New Packages](https://rohankapoor.com/wp-content/uploads/2012/06/10-Install-New-Packages.png)_

Looks like some of those have been deprecated or had their names changed. We'll have to install those ones again in a minute.

![](https://rohankapoor.com/wp-content/uploads/2012/06/11-Install-New-Packages-2.png)

> _[Install New Packages 2](https://rohankapoor.com/wp-content/uploads/2012/06/11-Install-New-Packages-2.png)_

For some strange reason CUPS didn't get installed, even though it was the list of programs to install in the last command. Run `sudo apt-get install cups` to fix this.

![](https://rohankapoor.com/wp-content/uploads/2012/06/12-Install-New-Packages-3.png)

> _[Install CUPS](https://rohankapoor.com/wp-content/uploads/2012/06/12-Install-New-Packages-3.png)_

Once again, it will need confirmation before continuing. As before, just type in `y` and press enter to continue.

![](https://rohankapoor.com/wp-content/uploads/2012/06/13-Install-New-Packages-4.png)

> _Once it finishes, you will again be returned to the bash prompt._

![](https://rohankapoor.com/wp-content/uploads/2012/06/14-Install-New-Packages-5.png)

> _[CUPS is installed](https://rohankapoor.com/wp-content/uploads/2012/06/14-Install-New-Packages-5.png)_

Time to install python-cups which allows python programs to print to the CUPS server. Run `sudo apt-get install python-cups` to install.

![](https://rohankapoor.com/wp-content/uploads/2012/06/15-Install-New-Packages-6.png)

> _[Install python-cups](https://rohankapoor.com/wp-content/uploads/2012/06/15-Install-New-Packages-6.png)_

Once you've returned to the bash prompt, run `sudo apt-get install avahi-daemon` to install the avahi daemon (an mDNS server needed for AirPrint support).

![](https://rohankapoor.com/wp-content/uploads/2012/06/17-Install-New-Packages-8.png)

> _[Install Avahi-Daemon](https://rohankapoor.com/wp-content/uploads/2012/06/17-Install-New-Packages-8.png)_

For security purposes, the CUPS server requires configuration changes (managing printers, etc) to come from an authorized user. By default, it only considers users authorized if they are members of the `lpadmin` group. To continue with the tutorial, we will have to add our user (in this case `pi`) to the `lpadmin` group. We do this with the following command: `sudo usermod -aG lpadmin pi` (replace pi with your username).

![](https://rohankapoor.com/wp-content/uploads/2012/06/20-Add-User-to-lpadmin-Group.png)

> _[Add User to lpadmin Group](https://rohankapoor.com/wp-content/uploads/2012/06/20-Add-User-to-lpadmin-Group.png)_

Before continuing, lets start the cups service and make sure the default configuration is working: `sudo /etc/init.d/cups start`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/22-Start-Cups-Service-2.png)

> _[Start Cups Service](https://rohankapoor.com/wp-content/uploads/2012/06/22-Start-Cups-Service-2.png)_

Since we just tested CUPS's default configuration, we might as well do the same to the Avahi-Daemon: `sudo /etc/init.d/avahi-daemon` start.

![](https://rohankapoor.com/wp-content/uploads/2012/06/24-Start-Avahi-Daemon-2.png)

> _[Start Avahi Daemon](https://rohankapoor.com/wp-content/uploads/2012/06/24-Start-Avahi-Daemon-2.png)_

If you get any errors during the previous two startup phases, it is likely that you didn't install something properly. In that case, I recommend that you go through the steps from the beginning again and make sure that everything is okay! If you proceed through without any errors then it's time to edit the CUPS config file to allow us to remotely administer it (and print to it without a user account on the local network - needed for AirPrint). Enter in `sudo nano /etc/cups/cupsd.conf`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/25-Edit-Cups-Config.png)

> _The configuration file will load in the nano editor. It will look like this._

![](https://rohankapoor.com/wp-content/uploads/2012/06/26-Edit-Cups-Config-2.png)

> _[CUPS Config File](https://rohankapoor.com/wp-content/uploads/2012/06/26-Edit-Cups-Config-2.png)_

Use the down arrow until you come to the line that says `Listen localhost:631`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/27-Edit-Cups-Config-3.png)

> _[Edit Cups Config 3](https://rohankapoor.com/wp-content/uploads/2012/06/27-Edit-Cups-Config-3.png)_

This tells CUPS to only listen to connections from the local machine. As we need to use it as a network print server, we need to comment that line out with a hashtag(`#`). As we want to listen to all connections on Port 631, we need to add the line `Port 631` immediately after the line we commented out.

![](https://rohankapoor.com/wp-content/uploads/2012/06/28-Edit-Cups-Config-4.png)

> _[Edit Cups Config 4](https://rohankapoor.com/wp-content/uploads/2012/06/28-Edit-Cups-Config-4.png)_

We also need to tell CUPS to alias itself to any hostname as AirPrint communicates with CUPS with a different hostname than the machine-defined one. To do this we need to add the directive `ServerAlias *` before the first `<Location />` block.

![](https://rohankapoor.com/wp-content/uploads/2012/06/37-Edit-Cups-Config-13.png)

> _[Add ServerAlias Directive](https://rohankapoor.com/wp-content/uploads/2012/06/37-Edit-Cups-Config-13.png)_

To continue setting up remote administration, there are several places that we need to enter the line `Allow @Local` after the line `Order allow, deny` - however this does not apply to all instances of that line.

![](https://rohankapoor.com/wp-content/uploads/2012/06/30-Edit-Cups-Config-6.png)

> _[Change Permissions](https://rohankapoor.com/wp-content/uploads/2012/06/30-Edit-Cups-Config-6.png)_

![](https://rohankapoor.com/wp-content/uploads/2012/06/32-Edit-Cups-Config-8.png)

> _[Change Permissions 2](https://rohankapoor.com/wp-content/uploads/2012/06/32-Edit-Cups-Config-8.png)_

![](https://rohankapoor.com/wp-content/uploads/2012/06/34-Edit-Cups-Config-10.png)

> _[Change Permissions 3](https://rohankapoor.com/wp-content/uploads/2012/06/34-Edit-Cups-Config-10.png)_

We now need to save the CUPS config file and exit the nano text editor. To do this hold down `ctrl` and press `x`. You will be prompted to save the changes. Make sure to type `y` when it prompts you.

![](https://rohankapoor.com/wp-content/uploads/2012/06/35-Edit-Cups-Config-11.png)

> _[Save CUPS Config](https://rohankapoor.com/wp-content/uploads/2012/06/35-Edit-Cups-Config-11.png)_

It will then ask you to confirm the file name to save to. Just press `enter` when it prompts you.

![](https://rohankapoor.com/wp-content/uploads/2012/06/36-Edit-Cups-Config-12.png)

> _[Save CUPS Config 2](https://rohankapoor.com/wp-content/uploads/2012/06/36-Edit-Cups-Config-12.png)_

Next, we need to restart CUPS to have the currently running version use the new settings. Run `sudo /etc/init.d/cups restart` to restart the server.

![](https://rohankapoor.com/wp-content/uploads/2012/06/37-Restart-Cups.png)

> _[Restart Cups](https://rohankapoor.com/wp-content/uploads/2012/06/37-Restart-Cups.png)_

It's time to find out the Pi's IP address to continue setting up printing via the web configuration tool. In my case, my Pi is assigned a static address by my DHCP server of `192.168.1.75`. To find out your Pi's IP address, just run `ifconfig`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/38-Get-IP-Address.png)

> _[Get IP Address](https://rohankapoor.com/wp-content/uploads/2012/06/38-Get-IP-Address.png)_

Once we have the IP address, we can open a browser to the CUPS configuration page located at `ip_address:631`. More than likely you will see a security error as the Raspberry Pi is using a self-made SSL certificate (unless you have bought and installed one).

![](https://rohankapoor.com/wp-content/uploads/2012/06/39-Connect-to-Cups-1024x555.png)

> _[Connect to CUPS](https://rohankapoor.com/wp-content/uploads/2012/06/39-Connect-to-Cups.png)_

To continue on, click on Proceed anyway or your browser's equivalent if you are sure you have entered in the correct IP address. You will then see this screen.

![](https://rohankapoor.com/wp-content/uploads/2012/06/40-Connect-to-Cups-2-1024x555.png)

> _[CUPS Home](https://rohankapoor.com/wp-content/uploads/2012/06/40-Connect-to-Cups-2.png)_

From there, go ahead and click the Administration tab at the top of the page. You will need to check the box that says `Share Printers connected to this system` and then click the `Change Settings` button.

![](https://rohankapoor.com/wp-content/uploads/2012/06/42-Cups-Administration-2-1024x555.png)

> _[Share Printers](https://rohankapoor.com/wp-content/uploads/2012/06/42-Cups-Administration-2.png)_

CUPS will request password authentication, and since we added the user `pi` to the `lpadmin` group earlier, we can login with the username `pi` and password `raspberry`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/42-Cups-Administration-3-1024x555.png)

> _The CUPS server will write those changes to it's configuration file and then reboot._

![](https://rohankapoor.com/wp-content/uploads/2012/06/43-Cups-Administration-4-1024x555.png)

> _[CUPS Reboot](https://rohankapoor.com/wp-content/uploads/2012/06/43-Cups-Administration-4.png)_

At this point, it is time to setup your printer with CUPS. In my case, I am using a Brother HL-2170w network laser printer and my screenshots will be tailored to that printer. Most other printers that are CUPS compatible (check <http://www.openprinting.org/printers> for compatibility) will operate the same way. If you are using a USB printer, now is the time to plug it in. Give it about a few seconds to get recognized by the Pi and then click the `Add Printer` button to begin!

![](https://rohankapoor.com/wp-content/uploads/2012/06/44-Cups-Administration-5-1024x555.png)

> _CUPS will begin looking for printers. Just wait till it comes to a list of discovered printers._

![](https://rohankapoor.com/wp-content/uploads/2012/06/45-Add-a-Printer-1024x555.png)

> _Eventually you will come to a page that looks like this:_

![](https://rohankapoor.com/wp-content/uploads/2012/06/46-Add-a-Printer-2-1024x555.png)

> _[Add a Printer 2](https://rohankapoor.com/wp-content/uploads/2012/06/46-Add-a-Printer-2.png)_

Once you have chosen the correct printer and clicked continue - you will be brought to the settings page. Make sure to check the box regarding sharing or AirPrint may not work correctly.

![](https://rohankapoor.com/wp-content/uploads/2012/06/48-Add-a-Printer-4-1024x555.png)

> _[Printer Setup](https://rohankapoor.com/wp-content/uploads/2012/06/48-Add-a-Printer-4.png)_

You will then have to select the driver for your printer. In most cases, CUPS will have the driver already and all you need to do is select it - but with newer printers, you will need to get a ppd file from the [OpenPrinting database](http://www.openprinting.org/printers) and use that.

![](https://rohankapoor.com/wp-content/uploads/2012/06/50-Add-a-Printer-6-1024x555.png)

> _[Select Driver](https://rohankapoor.com/wp-content/uploads/2012/06/50-Add-a-Printer-6.png)_

Then you need to set the default settings for the printer, including paper size and type. Make sure those match your printer so that everything prints out properly.

![](https://rohankapoor.com/wp-content/uploads/2012/06/51-Add-a-Printer-7-1024x555.png)

> _[Default Options](https://rohankapoor.com/wp-content/uploads/2012/06/51-Add-a-Printer-7.png)_

Once you are done, you should see the Printer Status page. In the Maintenance box, select Print Test Page and make sure that it prints out and looks okay.

![](https://rohankapoor.com/wp-content/uploads/2012/06/53-Add-a-Printer-9-1024x555.png)

> _[Print Test Page](https://rohankapoor.com/wp-content/uploads/2012/06/53-Add-a-Printer-9.png)_

If you get a proper test page, then you've successfully setup your CUPS server to print to your printer(s). All that's left is setting up the AirPrint announcement via the Avahi Daemon. Thankfully, we no longer have to do this manually, as [TJFontaine ](https://github.com/tjfontaine/airprint-generate)has created a python script that automatically talks to CUPS and sets it up for us! It's time to go back to the Raspberry Pi terminal and create a new directory. Run `sudo mkdir /opt/airprint` to create the directory `airprint` under `/opt/`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/55-AirPrint-Setup.png)

> _[Create Directory](https://rohankapoor.com/wp-content/uploads/2012/06/55-AirPrint-Setup.png)_

We next need to move to that directory with the command `cd /opt/airprint`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/56-AirPrint-Setup-2.png)

> _[Change Directories](https://rohankapoor.com/wp-content/uploads/2012/06/56-AirPrint-Setup-2.png)_

Now we need to download the script with the following command: `sudo wget -O airprint-generate.py --no-check-certificate https://raw.github.com/tjfontaine/airprint-generate/master/airprint-generate.py`

![](https://rohankapoor.com/wp-content/uploads/2012/06/57-AirPrint-Setup-3.png)

> _[Download the Script](https://rohankapoor.com/wp-content/uploads/2012/06/57-AirPrint-Setup-3.png)_

Next, we need to change the script's permissions so that we can execute it with the command `sudo chmod 755 airprint-generate.py`.

![](https://rohankapoor.com/wp-content/uploads/2012/06/59-AirPrint-Setup-5.png)

> _[Change Permissions](https://rohankapoor.com/wp-content/uploads/2012/06/59-AirPrint-Setup-5.png)_

It's time to finally run the script and generate the Avahi service file(s). Use the command: `sudo ./airprint-generate.py -d /etc/avahi/services` to directly place the generated files where Avahi wants them.

![](https://rohankapoor.com/wp-content/uploads/2012/06/63-AirPrint-Setup-9.png)

> _[Generate Avahi Services](https://rohankapoor.com/wp-content/uploads/2012/06/63-AirPrint-Setup-9.png)_

At this point everything should be working, but just to make sure, I like to do a full system reboot with the command sudo reboot. Once the system comes back up, your new AirPrint Server should be ready!

![](https://rohankapoor.com/wp-content/uploads/2012/06/65-Reboot-2.png)

To print from iOS, simply go to any application that supports printing (like Mail or Safari) and click the print button.

![](https://rohankapoor.com/wp-content/uploads/2012/06/photo.png)

> _[Send Printjob](https://rohankapoor.com/wp-content/uploads/2012/06/photo.png)_

Once you select your printer, and it queries it and will send the printjob! It may take a couple minutes to come out at the printer but hey, your iOS device is printing to your regular old printer through a Raspberry Pi! That's pretty cool and functional right? And the absolute best part, since the Raspberry Pi uses such little power (I've heard it's less than 10 watts), it is very cheap to keep running 24/7 to provide printing services!

**UPDATE:** If you are running iOS6, due to slight changes in the AirPrint definition, you will have to follow the instructions [here](http://blog.mornati.net/2012/09/22/linux-airprint-server-for-ios6-devices/), to make it work. Thanks to Marco for sharing them!
