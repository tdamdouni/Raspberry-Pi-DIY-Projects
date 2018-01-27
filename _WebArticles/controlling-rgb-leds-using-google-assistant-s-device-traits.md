# Controlling RGB LEDs Using Google Assistant's Device Traits

_Captured: 2018-01-06 at 13:31 from [www.hackster.io](https://www.hackster.io/shiva-siddharth/controlling-rgb-leds-using-google-assistant-s-device-traits-7b293b)_

![Controlling RGB LEDs Using Google Assistant's Device Traits](https://hackster.imgix.net/uploads/attachments/399964/untitled_OiNtzXqbuD.png?auto=compress%2Cformat&w=900&h=675&fit=min)

The Project has adopted the new Google Assistant SDK features released on 20th Dec 2017. Old installations will not work. So kindly reformat your SD Card and start fresh.

CLI or Raspbian Lite does not support all features and custom wakeword does not work with Google's AIY image. So please use the Standard Raspbian Desktop image - link <https://www.raspberrypi.org/downloads/raspbian/>

  * Open the terminal and execute the following:
    
    
    git clone 
    

  * Update OS and Kernel
    
    
    sudo apt-get update  
    sudo apt-get install raspberrypi-kernel  
    

  * Restart Pi
  * Choose the audio configuration according to your setup. **The speaker-test command is used to initialize alsa, so please do not skip that.** **AIY-HAT and CUSTOM-HAT users, please reboot the Pi at places mentioned, else it will lead to audio and taskbar issues.**

3.1. USB DAC or USB Sound CARD users
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/USB-DAC/scripts/install-usb-dac.sh  
    sudo /home/pi/GassistPi/audio-drivers/USB-DAC/scripts/install-usb-dac.sh
    speaker-test  
    

3.2. AIY-HAT users
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/AIY-HAT/scripts/configure-driver.sh  
    sudo /home/pi/GassistPi/audio-drivers/AIY-HAT/scripts/configure-driver.sh  
    sudo reboot  
    sudo chmod +x /home/pi/GassistPi/audio-drivers/AIY-HAT/scripts/install-alsa-config.sh
    sudo /home/pi/GassistPi/audio-drivers/AIY-HAT/scripts/install-alsa-config.sh  
    speaker-test  
    

3.3. USB MIC AND HDMI users
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/USB-MIC-HDMI/scripts/install-usb-mic-hdmi.sh  
    sudo /home/pi/GassistPi/audio-drivers/USB-MIC-HDMI/scripts/install-usb-mic-hdmi.sh  
    speaker-test  
    

3.4. USB MIC AND AUDIO JACK users
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/USB-MIC-JACK/scripts/usb-mic-onboard-jack.sh  
    sudo /home/pi/GassistPi/audio-drivers/USB-MIC-JACK/scripts/usb-mic-onboard-jack.sh  
    speaker-test 
    

3.5. CUSTOM VOICE HAT users
    
    
    sudo chmod +x /home/pi/GassistPi/audio-drivers/CUSTOM-VOICE-HAT/scripts/install-i2s.sh  
    sudo /home/pi/GassistPi/audio-drivers/CUSTOM-VOICE-HAT/scripts/install-i2s.sh
    sudo reboot
    sudo chmod +x /home/pi/GassistPi/audio-drivers/CUSTOM-VOICE-HAT/scripts/custom-voice-hat.sh  
    sudo /home/pi/GassistPi/audio-drivers/CUSTOM-VOICE-HAT/scripts/custom-voice-hat.sh  
    speaker-test   
    

**Those using HDMI/Onboard Jack, make sure to force the audio.**
    
    
    sudo raspi-config  
    

Select advanced options, then audio and choose to force audio.

**Those using any other DACs or HATs install the cards as per the manufacturer's guide and then you can try using the USB-DAC config file after changing the hardware IDs**

  * Restart Pi
  * Check the speaker using the following command
    
    
    speaker-test -t wav
    

  * Place the .json file in/home/pi directory **DO NOT RENAME**
  * Use the one-line installer for installing Google Assistant 

**Pi3 and Armv7 users use the "gassist-installer-pi3.sh" installer and Pi Zero, Pi A and Pi 1 B+ users use the "gassist-installer-pi-zero.sh" installer.**

4.1 Make the installers executable
    
    
    sudo chmod +x /home/pi/GassistPi/scripts/gassist-installer-pi3.sh 
    sudo chmod +x /home/pi/GassistPi/scripts/gassist-installer-pi-zero.sh  
    

4.2 Execute the installers

**Pi3 and Armv7 users use the "gassist-installer-pi3.sh" installer and Pi Zero; Pi A and Pi 1 B+ users use the "gassist-installer-pi-zero.sh" installer. When prompted, enter your Google Cloud console Project-ID, a name for your Assistant and the Full Name of your credentials file, including the json extension.**
    
    
    sudo  /home/pi/GassistPi/scripts/gassist-installer-pi3.sh   
    sudo  /home/pi/GassistPi/scripts/gassist-installer-pi-zero.sh  
    

  * Copy the Google Assistant authentication link from terminal and authorize using your google account
  * Copy the authorization code from browser onto the terminal and press enter
  * After successful authentication, the Google Assistant Demo test will automatically start. At the start, the volume might be low, the assistant volume is independent of the Pi volume, so increase the volume by using "Volume Up" command.
  * After verifying the working of assistant, close and exit the terminal.
  * Register your device traits using:
    
    
    source env/bin/activate/
    googlesamples-assistant-devicetool register-model --manufacturer "Assistant SDK developer"  --product-name "Assistant SDK light" --type LIGHT --trait action.devices.traits.OnOff  --trait action.devices.traits.Brightness --trait action.devices.traits.ColorTemperature --trait action.devices.traits.ColorAbsolute --model my-model
    

  * If you are using Pi 3 or Pi 2, register the device using:
    
    
     googlesamples-assistant-devicetool register-device --client-type LIBRARY \           --model my-model --device my-device-id 
    

  * If you are using Pi Zero, register the device using:
    
    
     googlesamples-assistant-devicetool register-device --client-type SERVICE \           --model my-model --device my-device-id
    

**HEADLESS AUTOSTART on BOOT SERVICE SETUP**

  * Open the service files in the /home/pi/GassistPi/systemd/ directory and add your project and model IDs in the indicated places and save the file.
  * Make the service installer executable:
    
    
    sudo chmod +x /home/pi/GassistPi/scripts/service-installer.sh
    

  * Run the service installer:
    
    
    sudo /home/pi/GassistPi/scripts/service-installer.sh
    

  * Enable the services

**Pi3 and Armv7 users, enable the "gassistpi-ok-ggogle.service"; Pi Zero, Pi A and Pi 1 B+ users, enable "gassistpi-push-button.service".** **To stop music playback using a pushbutton connected to GPIO 23, enable stopbutton.service**
    
    
    sudo systemctl enable gassistpi-ok-google.service  
    sudo systemctl enable gassistpi-push-button.service
    sudo systemctl enable stopbutton.service  
    

  * Start the service 

**Pi3 and Armv7 users, start the "gassistpi-ok-ggogle.service" and Pi Zero, Pi A and Pi 1 B+ users, start "gassistpi-push-button.service".** **To stop music playback using a pushbutton connected to GPIO 23 ,start stopbutton.service**
    
    
    sudo systemctl start gassistpi-ok-google.service  
    sudo systemctl start gassistpi-push-button.service
    sudo systemctl start stopbutton.service  
    
    
    
    source env/bin/activate
    sudo pip3 install blinkt 
    

Replace the main.py in the src folder with main-sample.py in extras folder and rename it to main.py.

Now you can control the blink using the Google Assistant's traits.
