# How to turn the Raspberry Pi into a wireless printer server

_Captured: 2016-02-21 at 00:29 from [www.techradar.com](http://www.techradar.com/how-to/computing/how-to-turn-the-raspberry-pi-into-a-wireless-printer-server-1312717)_

![How to turn the Raspberry Pi into a wireless printer server](http://cdn.mos.techradar.com/art/How%20tos/turn%20raspberry%20pi%20into%20print%20server/hero-970-80.jpg)

A printer isn't the most convenient of peripherals. They look out of place on most work desks and create quite a racket when spitting out pages.

You could throw a few hundred quid on a snazzy new network printer that sits in a corner somewhere and can receive print orders from any computer on the local network or you could just hook your regular USB printer to the Raspberry Pi and enjoy the same conveniences offered by top of the line network printers.

If you haven't already used your printer on Linux, before you get started with this project head to the [Open Printing website](http://www.openprinting.org/printers) to check whether your printer is compatible with the CUPS printing server software.

If your printer is listed, hook it up to the Raspberry Pi using one of the USB ports. For this project, we're using the Raspbian distro and the Raspberry Pi is connected to the local network via a compatible wireless adaptor.

However, you can also hook the Raspberry Pi up to your network via the wired Ethernet port.

You can follow the instructions in this tutorial by accessing the Raspberry Pi remotely from any other computer on the network. Just make sure that the SSH server inside Raspbian is enabled by using the raspi-config tool. It's also a good idea to assign a fixed IP address to the Raspberry Pi.

You can do this easily from within your router's admin page. For this tutorial we'll assume that the IP address of your Raspberry PI is 192.168.3.111.

You can now access the Pi from within Windows using the [PuTTY](http://www.chiark.greenend.org.uk/%20sgtatham/putty/download.html) client or from any Linux distro with the SSH CLI command with:

**$ sudo ssh pi@192.168.3.111**

### Install CUPS

Once you're inside Raspbian, update the repositories (repos) with **$ sudo apt-get update** and then install any updates with **$ sudo apt-get upgrade** . Now pull in the CUPS print server with **$ sudo apt-get install cups**

When it's installed, add your user to the group created by CUPS called lpadmin that has access to the printer queue.

![How to turn the Raspberry Pi into a wireless printer server](http://cdn0.beta.static.techradar.futurecdn.net/media/img/missing-image.svg)

> _You can also browse through its extensive documentation from the CUPS browser-based control panel_

Unless you have created a custom user, the default user on Raspbian is called pi. Use the following command to allow it to interact with the printer: **$ sudo usermod -a -G lpadmin pi**

Here we use the usermod tool to add (** -a **) the pi user to the lpadmin group ( **-G** ). By default, CUPS can only be configured from the local computer that it's installed on.

Because that doesn't work in our case, we need to edit its configuration file to allow us to make changes to the server from a remote computer. First of all, you need to create a backup of the original configuration file with:

**$ sudo cp /etc/cups/cupsd.conf /etc/cups/cupsd.conf.orig**

Then open the file with the nano text editor: **$ sudo nano /etc/cups/cupsd.conf** . Inside the file, scroll down to the following section:

**# Only listen for connections from the local machine  
Listen localhost:631**

Comment out that line (by adding the # to the beginning of the line) and add another to ask CUPS to accept connects from any computer on the network. Make sure the section looks like this:

**# Only listen for connections from the local machine  
# Listen localhost:631  
Port 631**

Then scroll further down in the configuration file until you reach the **<Location>** sections, and add a new line that reads **Allow @local** just before the close of the section. The section with the appended line should now read like this:

**< Location / >  
# Restrict access to the server  
Order allow,deny  
Allow @local  
< /Location >**

Now add the **Allow @local line** to the other two Location sections - **<Location /admin>** and **<Location /admin/conf>**

Save the file and restart the CUPS server with: **$ sudo /etc/init.d/cups restart**

You should now be able to access the CUPS administration panel via any computer on your local network by pointing the web browser to your Pi. Then follow the walkthrough over the page to add your printer to CUPS.

Some Linux distros ship with a restrictive iptables firewall policy that doesn't allow connections via the CUPS ports.

Even if Raspbian doesn't, make sure it doesn't throw up any unexpected errors by punching holes in the firewall with:

**$ sudo iptables -A INPUT -i wlan0 -p tcp -m tcp --dport 631 -j  
ACCEPT  
$ sudo iptables -A INPUT -i wlan0 -p udp -m udp --dport 631  
-j ACCEPT**

If you connect to the Raspberry Pi via Ethernet instead of a wireless adaptor, modify the command and replace **wlan0** with **eth0** . When you are through setting up your printer using the CUPS administration panel, it's time to make it accessible to other machines on your network.

While Linux distros will have no trouble detecting your new network printer, making them visible to Windows and Apple devices requires a couple of extra steps.

> _From the Printers tab, you can track the status of every job on every printer_

### Network-wide access

For Windows, install the Samba server on the Raspberry Pi with **$ sudo apt-get install samba **. Then open its configuration file (/etc/samba/smb.conf) in the nano text editor and hunt for the section labelled [printers] and make sure it contains the line:

**guest ok = yes**

Then scroll down to the [print$] section and change its path to the following:

**path = /usr/share/cups/drivers**

Then scroll up to the Global Settings section at the top of the configuration file. Modify the workgroup parameter within to point to the name of your workgroup, which by default is named WORKGROUP .

Also enable the wins support by adding the line **wins support = yes**

Now save the file and restart Samba with **$ sudo /etc/init.d/samba restart** .

Then head over to the Windows machine and launch the Add New Printer wizard and click on the option to install a network printer. Thanks to the modified Samba configuration, the wizard will detect and list any printers hooked up to the Raspberry Pi.

If you have Apple devices, you can enable support for Apple's AirPrint system, which allows you to print from the iPad and iPhone. For this, just install the Avahi daemon with **sudo apt-get install avahi-daemon** on the Raspberry Pi, which will then make the connected printer visible to AirPrint-compatible devices.

In addition to the ability to use our network printer from within graphical applications across all platforms, we can also use it to print from the command line interface. Furthermore, we can also interact with the printer using the Python programming language.

  


The CUPS printing server installs a bunch of command-line tools (see Administering CUPS later in this guide) for interacting with the server and any connected printers.

You can send files to the printer using the lp command, such as: **$ lp /docs/a_text_file.txt**

If you have multiple printers, you can print to a specific printer by specifying its name, such as:

**$ lp /docs/another-text.txt -d EPSON_LX-300**

When you use the commands with a PDF or image file, CUPS converts the files using the printer drivers. You can also use Python to generate printer-friendly content.

This is best done by using the PyCups library, which provides Python **bindings for the CUPS server. Install the library with:**

**$ sudo apt-get install python-cups**

Then create an example.py Python script with:

**import cups  
conn = cups.Connection()  
printers = conn.getPrinters ()  
for printer in printers:  
print printer, printers[printer]["device-uri"]**

The script fetches details about all the printers managed by CUPS and prints their name and device address to the screen. When you execute the script, it produces an output similar to the following:

**EPSON_LX-300 usb://EPSON/LX-300+?serial=L010209081  
RICOH_Aficio_SP_100 usb://RICOH/  
Aficio?serial=T382M977983**

You can also print files from the Python script using the printFile function, by specifying them in the format:

**$ printFile (name of the printer, filename to print, job title,  
options)**

Open the previous example.py script and add the following lines to it:

**file = "/home/pi/testfile.txt"  
printer_name=printers.keys()[0]  
conn.printFile (printer_name, file, "Project Report", {})**

The first line saves the name of the file you wish to print inside a variable named **file**. The second line fetches the list of printers and saves the first name, which is the default printer inside a variable named **printer_name**. The third line then uses the first two variables and prints the file in the specified format.

![Turn Raspberry Pi into Printer Server](http://cdn0.beta.static.techradar.futurecdn.net/media/img/missing-image.svg)

> _All Linux distros can access the USB printers connected to the Raspberry Pi without any tweaks to the distro_

### Converting from HTML to PDF

A more interesting way to convert HTML pages into PDF file is to use the wkHTMLtoPDF toolkit, which passes on the PDF to the printer from within a Python script.

Before you can install the toolkit, first install the required components and a set of fonts to process the web pages:

**$ sudo apt-get install xvfb xfonts-100dpi xfonts-75dpi xfonts  
scalable xfonts-cyrillic**

Then install the tool with

**sudo apt-get install wkhtmltopdf**

before installing the Python wrapper with:

**$ sudo pip install git+https://github.com/qoda/pythonwkhtmltopdf.git**

You can now use the following to convert a web page into a PDF file:

**from wkhtmltopdf import WKHtmlToPdf**

**wkhtmltopdf = WKHtmlToPdf (**

**url='http://www.techradar.com',**

**output_file='/home/pi/docs/lxf.pdf',**

**)**

**wkhtmltopdf.render()**

When executed, the above code saves the main techradar into a PDF file under the /home/pi/docs directory.

Refer to the listing below to see how all the pieces fit together - **wkHTMLtoPDF** converts a page into a PDF and prints it out.

**#!/usr/bin/env python  
import cups  
from wkhtmltopdf import WKHtmlToPdf  
wkhtmltopdf = WKHtmlToPdf(**

** url='http://www.techradar.com',  
output_file='/home/pi/techradar.pdf',  
)  
wkhtmltopdf.render()  
conn = cups.Connection()  
printers = conn.getPrinters()  
for printer in printers:  
print printer, printers[printer]["device-uri"]  
file="/home/pi/techradar.pdf"  
printer_name=printers.keys()[0]  
conn.printFile (printer_name, file, "PDF Print", {})**

The script first converts the techradar home page into a PDF. It then connects to CUPS, prints a list of attached and configured printers on the screen, and uses the default printer to print the PDF. The PyCups library is chockfull of methods (https://pythonhosted.org/pycups) that you can use to control all aspects of the CUPS print server.

> _You have to install and configure Samba to access the network printers on Windows_

### Administering CUPS

In addition to adding printers, the CUPS web interface provides access to various other useful settings. You can administer most of the printing tasks from the Administration tab, which houses settings under various different categories.

Under the Server section, for instance, you can find options to tweak the configuration of the server as well as view various types of access and error logs.

Using the 'Manage Printers' button under the Printer section, you can control the settings for individual printers. Every printer's page has options rolled under two pull-down menus labelled Maintenance and Administration. From under the Maintenance menu, you can print a test page, a self-test page, clean print heads and manage print jobs.

To customise the behaviour of the printer, use the Administration menu to tweak its default options, set it as the default printer, restrict user access, modify its settings or delete it from the CUPS server altogether. Besides the Administration tab, there are a couple of other important tabs we should mention as well.

For starters, you need to switch to the Classes tab for printer class management. A class is a collection of several printers. When you send print job to a class, CUPS automatically assigns the job to the next available printer, instead of waiting for a specific printer. Then there's the Jobs tab, which enables you to view and manage all print jobs that are currently in the print queue.

  
![How to turn the Raspberry Pi into a wireless printer server](http://cdn1.mos.techradar.futurecdn.net/art/How%20tos/turn%20raspberry%20pi%20into%20print%20server/addprinter1-650-80.jpg)

> _1. The CUPS dashboard_

The CUPS print server includes a built-in web server that powers its configuration panel. It's running on port 631 on the Raspberry Pi, which in our case is 192.168.3.111:631. Access the address from any browser on the network.

You have to accept its security certificate and then log into the interface using the credentials of the user that you've added to the lpadmin group, which in our case is the pi user.

![How to turn the Raspberry Pi into a wireless printer server](http://cdn3.mos.techradar.futurecdn.net/art/How%20tos/turn%20raspberry%20pi%20into%20print%20server/addprinter2-650-80.jpg)

> _2. Add a printer_

Once logged in, switch to the Administration tab and click on the 'Add Printer' button, which brings up a list of printers. Toggle the radio button next to your printer and head to the next step. Here you're be asked to add or edit the name, description and location of the printer.

Make sure you enable the 'Share This Printer' option to make the printer accessible all over the network.

![How to turn the Raspberry Pi into a wireless printer server](http://cdn0.beta.static.techradar.futurecdn.net/media/img/missing-image.svg)

> _3. Select a driver_

In the next step, you're asked to choose a driver for the selected printer. CUPS shows you a list of drivers based on the make of printer. Chances are that several of the drivers are marked 'Recommended'.

However, scroll through the list until you find the driver for your exact model. Alternatively, if you have a PPD file for the printer's driver, click on the 'Browse' button and navigate to it.

### 4\. Set default options

In the final step, CUPS enables you to set some generic print settings, such as page size and source. The number and type of options vary from one printer to another, and might spread over several sections.

When you've finished setting your preferences, click 'Set Default Options'. You're then taken to the main administration page for that printer. Use the Maintenance pull-down menu to print a test page.

  * Enjoyed this article? Expand your knowledge of Linux, get more from your code, and discover the latest open source developments inside Linux Format. [Read our sampler today and take advantage of the offer inside.](http://issuu.com/futurepublishing/docs/lxf204.sampler_tr?e=1191357/31271343)
