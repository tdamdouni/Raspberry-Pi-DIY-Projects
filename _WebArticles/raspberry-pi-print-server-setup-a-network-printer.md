# Raspberry Pi Print Server: Setup a Network Printer 

_Captured: 2017-02-20 at 20:18 from [pimylifeup.com](https://pimylifeup.com/raspberry-pi-print-server/)_

![Raspberry Pi Print Server](https://pimylifeup.com/wp-content/uploads/2017/02/Raspberry-Pi-Print-Server-v2.jpg)

In this tutorial, I will be going through the steps on how to setup a Raspberry Pi Print Server. The process of getting the software installed is pretty simple, but configuring it and getting a Windows network to find the print server is a bit more of an involved process.

Setting up a print server is a simple way of bringing your regular USB printer to more modern standards without you having to shell out hundreds of dollars. It allows you to move the printer to wherever you want and have it accessible by multiple computers rather than having it connected straight into a singular computer. It's also a great way to share a printer without needing a costly tower computer running all the time.

To make this all work, we will be making use of a piece of software called CUPS. CUPS stands for Common Unix Printing System and is the backbone of most Linux printing software. Basically it is the software that communicates with your printer and gets it to print files correctly.

If you want to make sure your printer is supported by the CUPS printing software, then go to their website at [open printing](http://www.openprinting.org/printers) and look up your specific model number.

## Equipment List

Below are the pieces of equipment that you will need for this Raspberry Pi print server tutorial.

**Recommended:**

[Micro SD Card](https://pimylifeup.com/out/amazon/microsdcard8gb) or an [SD card](https://pimylifeup.com/out/amazon/sdcard8gb) if you're using an old version of the Pi.

**Optional:**

## Installing the Raspberry Pi Print Server Software

Installing the print server for the Raspberry Pi is a simple process since it is available through the Debian Jessie packages. I will be using the latest version of Raspbian throughout this tutorial so if you need to install it then be sure to check out my [how to install Raspbian tutorial](https://pimylifeup.com/how-to-install-raspbian/).

**1.** To get started we should first update the Raspberry Pi to ensure we are running the latest software. You can do this by entering the following commands into the terminal:
    
    
    sudo apt-get update
    sudo apt-get upgrade

**2.** Once the Raspberry Pi has been updated we can now start installing the print server software. In this case, we will be installing CUPS, this software manages printers connected via USB or over the network and it has the bonus of providing a management interface that you can view over the internet.

Install this software by typing the following command into the terminal:
    
    
    sudo apt-get install cups

**3.** When CUPS has finished installing there is a few extra things that we will need to do.

The first thing to do is add the pi user to the lpadmin group. This will allow the pi user to access the administrative functions of CUPS without needing to use the super user.
    
    
    sudo usermod -a -G lpadmin pi

**4.** There is one other thing that we will need to do to CUPS to ensure that it runs well on the home network and that is to make CUPS accessible across your whole network, at the moment it will block any non-localhost traffic.

We can get it to accept all traffic by running the following two commands:
    
    
    sudo cupsctl --remote-any
    sudo /etc/init.d/cups restart
    

**5.** Now we should be able to access the Raspberry Pi print server from any computer within your network. If you are unsure on what your Raspberry Pi's local IP Address is then you can make use of the following command:
    
    
    hostname -I
    

**6.** Once you have your Raspberry Pi's IP Address, go to the following web address in your favorite web browser, make sure to swap out my IP address (192.168.1.105) with your own.
    
    
    http://192.168.1.105:631
    

Below we look at setting up SAMBA correctly to ensure Windows can properly identify the print server running on the Raspberry Pi. We will also show you how to add a printer using the CUPS interface.

## Setting up SAMBA for the Pi Print Server

If you intend on using your print server with Windows, then setting up SAMBA correctly is necessary. We will need to install SAMBA and make a few changes to its configuration to ensure that it runs correctly and utilizes the CUPS print drivers.

**1.** Now firstly, we should make sure we have SAMBA installed, the easiest way to do this is simply run the install command in the terminal. We can do that by entering the following command in the terminal:
    
    
    sudo apt-get install samba
    

**2.** With [SAMBA now installed to our Raspberry Pi](https://pimylifeup.com/raspberry-pi-nas/), we will need to open its configuration file and make several edits, we can open the file with the following command:
    
    
    sudo nano /etc/samba/smb.conf
    

**3.** Now with the file open, we will need to scroll to the bottom of the file. The quickest way to do this is to use _Ctrl+V_.

Once at the bottom of the file you should add or change the following lines. In my case the [printers] and the [print$] sections were already in the file, so I just needed to change the values to match the following.
    
    
    # CUPS printing.  
    [printers]
    comment = All Printers
    browseable = no
    path = /var/spool/samba
    printable = yes
    guest ok = yes
    read only = yes
    create mask = 0700
    
    # Windows clients look for this share name as a source of downloadable
    # printer drivers
    [print$]
    comment = Printer Drivers
    path = /var/lib/samba/printers
    browseable = yes
    read only = no
    guest ok = no
    

Save the file by pressing _Ctrl+X_ and then pressing _Y_ and then Enter.

**4.** We can now restart SAMBA to get it to load in our new configuration, to do that, all we need to do is type the following command into the terminal:
    
    
    sudo /etc/init.d/samba restart

## Adding a printer to CUPS

**1.** Adding a printer to CUPS is a rather simple process, but first we need to load up the CUPS web interface. If you're unsure what your Raspberry Pi's IP address is, then run the following command in the terminal:
    
    
    hostname -I

**2.** Once you have your Raspberry Pi's IP address, go to the following web address in your favorite web browser, make sure to swap out my IP address (192.168.1.105) with your own.
    
    
    https://192.168.1.105:631

**3.** You should be greeted with the following screen, on here we need to click "Administration".

![](https://pimylifeup.com/wp-content/uploads/2017/02/CUPS-Main-screen-1024x559.png)

> _Now that we are on the administration screen, we need to click on the "Add Printer" button._

**4.**

![](https://pimylifeup.com/wp-content/uploads/2017/02/CUPS-Administrative-Screen-1024x559.png)

> _With the "Add Printer" screen now loaded, we can select the printer we want to setup. In our case, that is the Canon MG25000 series (Canon MG2500 series) printer. Once selected, press the "continue" button._

**5.**

![](https://pimylifeup.com/wp-content/uploads/2017/02/Cups-select-printerpng-1024x559.png)

> _If your printer is not showing up on this screen, ensure that you have plugged it into one of the USB ports on the Raspberry Pi and that it is turned on._

You may need to restart your Raspberry Pi if it is still refusing to show up, ensure the printer is turned on and plugged in when you restart.

**6.** On this screen you need to select the model of your printer. CUPS will try and automatically detect the model and pick the correct driver.

However, in some cases this will not function correctly, so you will have to go through the list yourself and find the most relevant driver.

Once you are certain everything is correct, click the "Add Printer" button.

![](https://pimylifeup.com/wp-content/uploads/2017/02/cups-select-model-1024x559.png)

**7.** Now this is the last screen you need to deal with before the printer is successfully added, you can set the name and description to whatever you want. It is handy setting the location if you have multiple printers in your house that you need to deal with.

Also, make sure you enable "Share This Printer", otherwise other computers will not be able to access it.

Once you are happy with the settings, feel free to press "Continue".

![](https://pimylifeup.com/wp-content/uploads/2017/02/cups-add-printer-1024x559.png)

**8.** The final screen that you will be presented with after setting up your printer is pictured right below. This allows you to change a few of the printer's specific settings. Such as the page print size, the print quality, and various other options.

![](https://pimylifeup.com/wp-content/uploads/2017/02/Cups-final-screen-1024x559.png)

> _Now we will go over how to add our newly setup Raspberry Pi print server to Windows. This should be a relatively easy process thanks to setting up SAMBA earlier in the tutorial._

## Adding a Raspberry Pi Print Server to Windows

**1.** Adding a CUPS printer to Windows can be a bit of work, mainly because you need to select the driver for Windows to be able to connect to and understand the printer.

To get started, first go to the network page in Windows, one of the fastest ways to get to this is to load up "My Computer" or "This PC" and click on "network" in the sidebar. Once there you should have a screen that looks like the one below with your Raspberry Pi's hostname there, in my case it is RASPBERRYPI.

Double click on your Raspberry Pi's share, it may ask for a username and password. If just pressing enter doesn't work, try entering pi as the username.

![](https://pimylifeup.com/wp-content/uploads/2017/02/Cups-Network-01-Network-page-1024x555.png)

> _You should now be greeted with a screen displaying the printers available on your Raspberry Pi print server. Double click on the printer you want to have connected to your computer._

**2.**

![](https://pimylifeup.com/wp-content/uploads/2017/02/Cups-Network-02-Network-page-1024x555.png)

> _Upon double clicking this, you will likely be greeted with the warning message below, just click the "OK" button._

**3.**

![](https://pimylifeup.com/wp-content/uploads/2017/02/Cups-Network-03-Network-page-1024x555.png)

**4.** Now you will need to find your printer within this list, on the left is a list of all the brands, and on the right, is a list of all the printers for that brand that Windows has drivers for. If you don't find your printer on here, then try looking up your printer's model online and download the appropriate drivers for it.

In my case I had to look for the Canon MG2500 series as shown below. Once you have selected your printer press the "Ok" button.

![](https://pimylifeup.com/wp-content/uploads/2017/02/Cups-Network-04-Network-page-1024x555.png)

> _This will now load up a connection with your printer, if you want to make this the default printer for the computer, the click Printer -> Set as Default Printer_

**5.**

![](https://pimylifeup.com/wp-content/uploads/2017/02/Cups-Network-05-Network-page-1024x555.png)

> _The printer should now be successfully added to your computer and be available for any program to use. You can ensure the printer is correctly set up by printing a file._

**6.**

![](https://pimylifeup.com/wp-content/uploads/2017/02/Cups-Network-06-1024x555.png)

> _If you have any issues with the file printing. Ensure that you have selected the correct printer driver in both CUPS and Windows._

Make sure your printer is also switched on, some printers like the Canon MG2500 series don't automatically turn back on when a file it sent to it to be printed.

I hope that this tutorial has shown you how to setup a Raspberry Pi print server and that you haven't run into any issues. If you have some feedback, tips or have come across any issues that you would like to share then please don't hesitate to leave a comment below.
