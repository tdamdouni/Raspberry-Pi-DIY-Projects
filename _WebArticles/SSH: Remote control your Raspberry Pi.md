# SSH: Remote control your Raspberry Pi

_Captured: 2016-12-28 at 14:15 from [www.raspberrypi.org](https://www.raspberrypi.org/magpi/ssh-remote-control-raspberry-pi/)_

Remote control your Raspberry Pi from a PC, Linux or Mac computer using SSH

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2016/12/SSH.jpg)

> _SSH (also known as 'secure shell') is an encrypted networking technology that enables you to manage computers from the command line over a network._

SSH is handy if you want to quickly connect to your Raspberry Pi from a terminal on another computer. It's also ideal for lightweight distro installations that don't have an interface. It's especially useful when creating Internet of Things (IoT) projects, as these may be embedded and not require a desktop.

We've already looked at VNC (Virtual Network Computing), and Secure Shell offers a similar service. But while VNC shares the entire desktop, SSH works from the command line.

See also: [VNC: Remote Control a Raspberry Pi desktop](http://magpi.cc/2fCUfsK)

### Use SSH on a Raspberry Pi with PC, Windows and Linux

On Linux PCs and Macs, you don't need to install any software to start using secure shell. Linux and Mac OS X have the command-line application installed by default; you can view its manual in the terminal using man VNC.

On Windows you will need to download a client; the most commonly used one is called PuTTY. Download the [PuTTY software from Simon Tatham's website](http://magpi.cc/2hb1IiW).

You'll need to use the password for your Raspberry Pi to log in. For security reasons, [we recommend changing the default password](http://magpi.cc/2iqm9pO).

SSH uses an encrypted network, so it doesn't send your password as plain text. More advanced users can control the encryption keys, using ssh-keygen. For now, we'll look at setting up and using secure shell.

### Step 1 Activate SSH in Raspbian

As of the November 2016 release of Raspbian with PIXEL, secure shell is no longer turned on by default. On your Raspberry Pi, choose Menu > Preferences > Raspberry Pi Configuration. Click on Interfaces and set SSH to Enabled. Click OK.

### Step 2: Get your IP address

Connect your Raspberry Pi to a local network. Use a wireless network, or connect the Raspberry Pi directly to a router with an Ethernet cable. Open a terminal and enter ifconfig to find the IP address. With Ethernet, it'll be the four numbers next to inet addr:, such as 192.168.0.27. If you're connected wirelessly, look for similar numbers under wlan0.

### Step 3: Start SSH on Linux or Mac

On a Linux or Mac, open a terminal and enter ssh pi@youripaddress. On our network, that's ssh pi@192.168.0.19. The first time, you'll get this message: 'The authenticity of host (192.168.0.19') can't be established. ECDSA key fingerprint is SHA256:' followed by a long cryptographic hash of letters and numbers. It will say 'Are you sure you want to continue connecting?'. Enter yes and press RETURN.

### Step 4: Use PuTTY on a Windows PC

![SSH with PuTTY on a PC](https://www.raspberrypi.org/magpi/wp-content/uploads/2016/12/4_ssh.jpg)

On a PC you'll need to install [PuTTY](http://magpi.cc/2hb1IiW). Download the putty.exe file and click Run. The PuTTY Configuration window appears with basic options. Enter the IP address of your Raspberry Pi in the 'Host Name (Or IP Address)' field. Don't change the 'Port' field. Click Open. You will get a PuTTY 'Security Alert' field. Click Yes. The terminal window displays 'login as:' Enter pi and press RETURN. Now enter the password for your Raspberry Pi.

### Step 5: The command line

You will now see your usual command line replaced with pi@raspberrypi: ~$. You are now logged in and working on the command line from your Raspberry Pi. Enter ls and you'll see python_games along with the other unique Raspberry Pi folders and files. You can create, edit, move, and work with files as if you were using a terminal on your Raspberry Pi.

### Step 5: Exiting the shell

There are limitations over VNC. You can't open programs with a graphical interface, so you'll need to use command-line alternatives (such as nano or vim instead of Leafpad for text editing). It's not as easy to share files using secure shell as it is with VNC, but for fast command-line editing, it's hard to beat. Enter exit at the command line to finish
