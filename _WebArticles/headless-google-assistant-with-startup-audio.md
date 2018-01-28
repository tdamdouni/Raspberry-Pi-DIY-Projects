# Headless Google Assistant with Startup Audio

_Captured: 2017-11-09 at 23:11 from [www.hackster.io](https://www.hackster.io/shiva-siddharth/headless-google-assistant-with-startup-audio-a2c551)_

_https://github.com/shivasiddharth/GassistPi_

![Headless Google Assistant with Startup Audio](https://hackster.imgix.net/uploads/attachments/345633/img_20170902_0144041_wo3lH7fzqm.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

Now, by starting Google Assistant as a service on boot, the unit can be used headless. Also, I have added a cool startup audio and an audio alert for wakeword detection.

Clone the project from github and follow the instructions in the readme file. It should not take you more than 10-15 mins.
    
    
    git clone https://github.com/shivasiddharth/GassistPi
    

**This is implemented in Python2 so your existing Google Assistant may not work. So please start by making a fresh copy of latest RaspbianINSTALL AUDIO CONFIG FILES**1\. Update OS and Kernel
    
    
    sudo apt-get update  
    sudo apt-get install raspberrypi-kernel  
    

2\. Restart Pi3. Choose the audio configuration according to your setup. (Run the commands till you get .bak notification in the terminal)3.1. USB DAC users,
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/USB-DAC/scripts/install-usb-dac.sh
      
    sudo /home/pi/GassistPi/audio-drivers/USB-DAC/scripts/install-usb-dac.sh 
    

3.2. AIY-HAT users,
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/AIY-HAT/scripts/configure-driver.sh
      
    sudo /home/pi/GassistPi/audio-drivers/AIY-HAT/scripts/configure-driver.sh  
    sudo chmod +x /home/pi/GassistPi/audio-drivers/AIY-HAT/scripts/install-alsa-config.sh  
    sudo /home/pi/GassistPi/audio-drivers/AIY-HAT/scripts/install-alsa-config.sh 
    

3.3. USB MIC AND HDMI users,
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/USB-MIC-HDMI/scripts/install-usb-mic-hdmi.sh 
    sudo /home/pi/GassistPi/audio-drivers/USB-MIC-HDMI/scripts/install-usb-mic-hdmi.sh 
    

3.4. USB MIC AND AUDIO JACK users,
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/USB-MIC-JACK/scripts/usb-mic-onboard-jack.sh
      
    sudo /home/pi/GassistPi/audio-drivers/USB-MIC-JACK/scripts/usb-mic-onboard-jack.sh 
    

3.5. CUSTOM VOICE HAT users,
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/CUSTOM-VOICE-HAT/scripts/custom-voice-hat.sh
      
    sudo /home/pi/GassistPi/audio-drivers/CUSTOM-VOICE-HAT/scripts/custom-voice-hat.sh  
    sudo chmod +x /home/pi/GassistPi/audio-drivers/CUSTOM-VOICE-HAT/scripts/install-i2s.sh  
    sudo /home/pi/GassistPi/audio-drivers/CUSTOM-VOICE-HAT/scripts/install-i2s.sh 
    

**Those Using HDMI/Onboard Jack, make sure to force the audio**
    
    
    sudo raspi-config  
    

Select advanced options, then audio and choose to force audio**Those using any other DACs or HATs install the cards as per the manufacturer's guide and then you can try using the USB-DAC config file after changing the hardware ids**4\. Restart Pi5. Check the speaker using the following command
    
    
    speaker-test -t wav  
    

**CONTINUE AFTER SETTING UP AUDIO**

1\. Download credentials--->.json file

2\. Place the .json file in/home/pi directory

3\. Rename it to assistant--->assistant.json

4\. Use the one-line installer for installing Google Assistant

4.1 Make the installers Executable
    
    
    sudo chmod +x /home/pi/GassistPi/scripts/gassist-installer-pi3.sh 
    

4.2 Execute the installers
    
    
    sudo  /home/pi/GassistPi/scripts/gassist-installer-pi3.sh    
    

5\. Copy the google assistant authentication link from terminal and authorize using your google account6. Copy the authorization code from browser onto the terminal and press enter7. Move into the environment and test the google assistant
    
    
    source env/bin/activate  
    google-assistant-demo 
    

  * After verifying the working of assistant, close and exit the terminal

**HEADLESS AUTOSTART ON BOOT SERVICE SETUP**

  * Make the service installer executable
    
    
    sudo chmod +x /home/pi/GassistPi/scripts/service-installer.sh 
    

  * Run the service installer
    
    
    sudo /home/pi/GassistPi/scripts/service-installer.sh
    

  * Enable the services 
    
    
    sudo systemctl enable gassistpi-ok-google.service 
    

  * Start the service
    
    
    sudo systemctl start gassistpi-ok-google.service 
    

**RESTART and ENJOY**

**VOICE CONTROL OF GPIOs and Pi Shutdown**

The default GPIO and shutdown trigger word is "trigger" if you wish to change the trigger word, you can replace the 'trigger'in the main.py(src folder) code with your desired trigger word.Similarly, you can define your own device names under the variable name var.The number of GPIO pins declared should match the number of devices.

**FOR NEOPIXEL INDICAOR**

1\. Replace the main.py in src folder with the main.py from Neopixel Indicator Folder.

2\. Reboot

3\. Change the Pin numbers in the given sketch according to your board and upload it.

4\. Follow the circuit diagram given.

**Now you have your Google Home Like Indicator**
