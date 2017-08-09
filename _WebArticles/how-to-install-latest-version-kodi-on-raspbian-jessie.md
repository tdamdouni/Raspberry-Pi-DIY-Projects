# How to install latest version kodi 17 on Raspbian jessie

_Captured: 2017-05-19 at 11:18 from [linuxsuperuser.com](https://linuxsuperuser.com/install-latest-version-kodi-raspbian-jessie/)_

Raspbian jessie repository is using a bit outdated version of kodi (version 15 and latest stable is 17), To install latest version of kodi (kodi 17) on your raspberry pi follow below steps.

#### Add the pipplware repository to /etc/apt/sources.list

`sudo nano /etc/apt/sources.list`

#### add below line to /etc/apt/sources.list

`deb http://pipplware.pplware.pt/pipplware/dists/jessie/main/binary /`

#### Add the keys

`wget -O - http://pipplware.pplware.pt/pipplware/key.asc | sudo apt-key add - `

#### Now update the sources and Upgrade your Rpi

`sudo apt-get update && sudo apt-get dist-upgrade`

#### Now install Kodi

`sudo apt-get install kodi`

#### install Kodi PVR addons (optional)

`sudo apt-get install kodi-pvr*`

#### Set permissions for kodi

`sudo addgroup --system input`

#### Create new file

`sudo nano /etc/udev/rules.d/99-input.rules`

#### Now add the below lines to above file

`SUBSYSTEM==input, GROUP=input, MODE=0660  
KERNEL==tty[0-9]*, GROUP=tty, MODE=0660`

#### Create new file

`sudo nano /etc/udev/rules.d/10-permissions.rules`

#### Now add the below lines to above file

`#input  
KERNEL=="mouse_|mice|event_", MODE="0660", GROUP="input"  
KERNEL=="ts[0-9]_|uinput", MODE="0660", GROUP="input"  
KERNEL==js[0-9]_, MODE=0660, GROUP=input  
#tty  
KERNEL==tty[0-9]*, MODE=0666  
#vchiq  
SUBSYSTEM==vchiq, GROUP=video, MODE=0660`

#### Now run the following commands

Note:Replace 'pi' with your username (in most cases pi is the default user in raspbian,You can use the command 'whoami' to get your username)

`sudo usermod -a -G audio pi  
sudo usermod -a -G video pi  
sudo usermod -a -G input pi  
sudo usermod -a -G dialout pi  
sudo usermod -a -G plugdev pi  
sudo usermod -a -G tty pi`

#### How to enable shutdown and reboot option in kodi power menu

To add shutdown or reboot option you need create new policy kit file.  
`sudo nano /etc/polkit-1/localauthority/50-local.d/all_users_shutdown_reboot.pkla`  
Now add below contents to the file
    
    
    [Allow all users to shutdown and reboot]
    Identity=unix-user:*
    Action=org.freedesktop.login1.*;org.freedesktop.upower.*;org.freedesktop.consolekit.system.*
    ResultActive=yes
    ResultAny=yes
    ResultInactive=yes 

#### To start kodi automatically with boot (raspbian boots directly to kodi)  
Run below command to add Kodi upstart script
    
    
     sudo wget -O /etc/init.d/kodi https://gist.githubusercontent.com/shyamjos/60ea61fd8932fd5c868c80543b34f033/raw;sudo chmod +x /etc/init.d/kodi

Then enable upstart script by running below command

`sudo systemctl enable kodi`

Voila! now you have successfully installed kodi on your raspberry pi

PS: _Make Sure you have gpu memory of >=160MB to play Full HD videos. (use _raspi-config_ command to increase it)_
