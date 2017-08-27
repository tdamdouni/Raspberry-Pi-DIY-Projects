# SSH Raspberry Pi 2 in Ubuntu

_Captured: 2017-08-25 at 11:52 from [akashkollipara.blogspot.de](https://akashkollipara.blogspot.de/2017/06/ssh-raspberry-pi-2-in-ubuntu.html?m=1)_

![Image](https://lh5.googleusercontent.com/-H586sMBmhdE/AAAAAAAAAAI/AAAAAAAAE-8/Q2_brzw8uxI/w168-h168-p-k-no-nu/photo.jpg)

I am raspberry pi 2 beginner and Ubuntu user, I did not have monitor, keyboard and mouse, so how do I connect and get started? Well I surfed the web and could not find satisfactory results.

If you have searched for the same query, you will be coming across "ssh raspberry pi or headless connection of raspberry pi" and "finding the IP address of RPi". For this again you will be needing tools or monitor, keyboard and mouse. Well this post will direct you to connect RPi to your Computer/PC running on Ubuntu or SSH without these tools.

When you boot RPi with **Raspbian OS**, the "avahi-daemon" is already installed, this will provide the access to RPi with domain name <hostname>.local. Your hostname can be found in preferences>Raspberry Pi Configuration. The hostname might by abc_xyz (just an example), but in domin name it will not contain any special characters like '_', '-',... etc.. Therefore it will resemble: abcxyz.local

**_Computer/PC running on Ubuntu (Wired/Ethernet):_**

  * Launch Terminal (ctrl+alt+T) type "nm-connection-editor" press enter.
  * Click "Add" button, select "Ethernet" then click "create".
![](https://2.bp.blogspot.com/-4cEEwb-Jnx8/WUNeo0K9Q1I/AAAAAAAAFfY/0NnyF8sd4L853Yyf4wvJZOsiVn4vTnPoQCLcBGAs/s320/Screenshot%2Bfrom%2B2017-06-16%2B09-58-03.png)

  * Then edit the connection name and select the device.![](https://1.bp.blogspot.com/-BnoEMwhUnPA/WUNfc8w5VmI/AAAAAAAAFfg/zhsPo2w8KPM4gvujnk_ywrC_iubcjV50wCLcBGAs/s320/Screenshot%2Bfrom%2B2017-06-16%2B10-01-52.png)

  * Click on IPv4 Settings tab and in method drop down menu select the "Shared to other computers". Save and close the window. 
  * Connect the Ethernet cable to RPi and wait till the boot up about a minute. Then in Computer/PC settings>network manager in Ethernet/Wired (for me its Wired) select the connection you have just created. 
  * To test this method, launch Terminal, type ping <hostname>.local; hostname should be replaced by hostname of RPi. If you get response then this method worked. 
  * In Terminal if you wish to ssh the type ssh pi@<hostname>.local. This will start the ssh session by asking password. 
  * Or in PuTTy enter the <hostname>.local in the respective field and launch the session. 
  * Once you login, to test the sharing of internet, type ping <any website address>, if you get response then you are good to go. 

****_Computer/PC running on Ubuntu (Wireless/WiFi):_****

  * Suppose you have previously connected your RPi to WiFi/home network/Hotspot then its easier to connect. As raspberry pi already has access to internet, you need not do any additional settings.
  * Connect you Computer to WiFi, and in terminal ping <hostname>.local, if you get response then RPi can be connected. To SSH follow from the 7th point mention above.

**_RPi GUI on your Computer:_**

  * In your computer download the [real VNC viewer](https://www.realvnc.com/download/viewer/) and in raspberry pi install tightvncserver to do that type...

sudo apt-get update && sudo apt-get upgrade

sudo apt-get install tightvncserver

  * After installation and download of vnc, in raspberry pi terminal launch tightvncserver by entering tightvncserver.
  * It will ask you for password enter it and verify it. Later if you wish to change it the command is vncpasswd.
  * In your computer open real vnc viewer and in file select "new connection". In VCN Server field enter the <hostname>.local:<the channel provided by the RPi when tightvncserver is launched>, If you launch it for the first time it will be <hostname>.local:1. The rest of the edits depends on you, save the connection profile and right click on the icon> connect; this will start the vnc session.
  * To end vncserver session type vncserver -kill in terminal of RPi.

Please do comment/ask if any and keep visiting the blog for upcoming posts.
