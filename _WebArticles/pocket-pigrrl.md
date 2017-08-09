# Overview

_Captured: 2017-08-08 at 17:47 from [learn.adafruit.com](https://learn.adafruit.com/pocket-pigrrl?view=all)_

![gaming_hero_adabot_double_smaller.jpeg](https://cdn-learn.adafruit.com/assets/assets/000/025/201/large1024/gaming_hero_adabot_double_smaller.jpeg?1430690896)

The gameboy is an iconic portable gaming device that most adults will probably remember dedicating hours of their childhood playing games on one.

This DIY project isn't about hacking or modding an old gameboy. In this project, we're building a completely new gaming device using 3D printing, the Raspberry Pi A+ and components from Adafruit.

**Please note** this is not a professional product! It's a DIY kit, and is great fun to build, but it may not have great emulation, video, audio etc.

3D printing allows you to design custom enclosures for your projects. The design and form factor are very much inpsired by the gameboy, but by no means meant to look exactly like it.

![gaming_hero_pigrrl_compare_small.jpeg](https://cdn-learn.adafruit.com/assets/assets/000/025/202/large1024/gaming_hero_pigrrl_compare_small.jpeg?1430692193)

Our first PiGRRL project used the Raspberry Pi Model B and and Adafruit 2.8' PiTFT.

In this project, we're using the Raspberry model A+ and a 2.4" PiTFT HAT. The small size of the A+ and the compact display really allows this project to be one of the smallest builds yet.

  * Raspberry Pi A+
  * PiTFT 2.4" 320x240 Touch Display
  * Retropie w/ Emulation Station
  * Mono Audio Amp + 8 ohm ~1W Speaker
  * Tactile Buttons w/ Perma-Proto
  * Powerboost 1000C w/ 2000mAh lipo battery

This tutorial will walk you through the assembly and wiring. It's a challenging build but it's not the most hardest thing ever. Our intent was to make this project easier than our previous PiGRRL build.

So, if this is your first DIY electronics + 3D Printing project, you might want try a simplier project with less wiring and soldering. That said, you shouldn't feel discouraged to take on the project.

![gaming_hero_pocket_pigrrl_smaller.jpeg](https://cdn-learn.adafruit.com/assets/assets/000/025/200/large1024/gaming_hero_pocket_pigrrl_smaller.jpeg?1430688878)

We recommend walking through these guides to get familiar with the software and components. You don't have to, but it's a good idea to check them out if you're not sure what all these things do.

![gaming_parts.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/832/large1024/gaming_parts.jpg?1430060829)

The parts below were used in this project. You don't have to use the exact same parts but the enclosure was designed to specially fit these parts - so if you want to use different components, you can but just know it may not fit in the provided enclosure. You can of course tweak the CAD files.

Having the right tools makes this build easier and more fun. Most of these are available in the shop but use whatever tools you have on hand.

![gaming_circuit-diagram.png](https://cdn-learn.adafruit.com/assets/assets/000/025/508/large1024/gaming_circuit-diagram.png?1431660433)

![gaming_gamepad-button-pcb.png](https://cdn-learn.adafruit.com/assets/assets/000/025/088/large1024/gaming_gamepad-button-pcb.png?1430419333)

![gaming_four-button-pcb.png](https://cdn-learn.adafruit.com/assets/assets/000/025/569/large1024/gaming_four-button-pcb.png?1431978727)

![gaming_raspberry_pi_wifi2.png](https://cdn-learn.adafruit.com/assets/assets/000/038/174/medium640/gaming_raspberry_pi_wifi2.png?1483658076)

![gaming_pocketpigrrl.png](https://cdn-learn.adafruit.com/assets/assets/000/038/175/large1024/gaming_pocketpigrrl.png?1483660499)

> _Answer "NO" to the reboot question…_

![gaming_noreboot.png](https://cdn-learn.adafruit.com/assets/assets/000/038/178/large1024/gaming_noreboot.png?1483661045)

![gaming_force35.png](https://cdn-learn.adafruit.com/assets/assets/000/038/180/large1024/gaming_force35.png?1483664623)

![gaming_retro.png](https://cdn-learn.adafruit.com/assets/assets/000/038/179/large1024/gaming_retro.png?1483661140)

![gaming_raspberry_pi_input.png](https://cdn-learn.adafruit.com/assets/assets/000/038/176/medium640/gaming_raspberry_pi_input.png?1483660649)

![gaming_raspberry_pi_evtest.png](https://cdn-learn.adafruit.com/assets/assets/000/038/177/large1024/gaming_raspberry_pi_evtest.png?1483660900)

> _Make sure each keypress works and matches the table below!_

![gaming_3d_parts_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/992/large1024/gaming_3d_parts_case.jpg?1430177058)

![gaming_3d_parts_4btn.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/558/large1024/gaming_3d_parts_4btn.jpg?1431970708)

![gaming_3d_parts_buttons.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/993/large1024/gaming_3d_parts_buttons.jpg?1430177100)

![gaming_mags_setup.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/191/medium640/gaming_mags_setup.jpg?1430585642)

![gaming_tinned_switch_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/252/large1024/gaming_tinned_switch_wires.jpg?1430836711)

![gaming_secure_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/254/large1024/gaming_secure_boost.jpg?1430836808)

![gaming_prep_wires_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/255/large1024/gaming_prep_wires_pam8302.jpg?1430836875)

![gaming_buttos_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/256/large1024/gaming_buttos_pitft.jpg?1430836963)

![gaming_install_btns_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/257/large1024/gaming_install_btns_permaproto.jpg?1430837016)

![gaming_soldered_switch_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/841/large1024/gaming_soldered_switch_wires.jpg?1430061771)

![gaming_heatshrink_switch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/842/large1024/gaming_heatshrink_switch.jpg?1430061807)

# [Pocket PiGRRL](/pocket-pigrrl/overview)

[Retropie in your pocket!](/pocket-pigrrl/overview)

  * Overview
  * Circuit Diagram
  * Software
  * Software [Manual]
  * Configuration
  * 3D Printing
  * Wiring
    * Switch
    * Powerboost 1000C
    * PAM8302
    * Pi Audio
    * Speaker
    * 2.4 PiTFT
    * Pi Cable
    * Mount Display
    * Perma-Proto
    * Buttons

  * Assembly
  * RetroPie: Improving Emulator Performance
  *   * [Multiple Pages](/pocket-pigrrl)
  * [Download PDF](https://cdn-learn.adafruit.com/downloads/pdf/pocket-pigrrl.pdf)

#### Contributors

[Ruiz Brothers](/users/pixil3d)

[lady ada](/users/adafruit2)

[Phillip Burgess](/users/pburgess)

[ Feedback? Corrections? ](/pages/5443/settings_modal)

[PROJECTS](/category/projects) / [GAMING](/category/gaming-1) [RASPBERRY PI](/category/raspberry-pi) [3D PRINTING](/category/3d-printing) [ __ ](/guides/988/favorites.js)

#  Overview

by [ Ruiz Brothers ](/users/pixil3d)

[ ![gaming_hero_adabot_double_smaller.jpeg](https://cdn-learn.adafruit.com/assets/assets/000/025/201/medium800/gaming_hero_adabot_double_smaller.jpeg?1430690896) __ ](/assets/25201)

The gameboy is an iconic portable gaming device that most adults will probably remember dedicating hours of their childhood playing games on one. 

This DIY project isn't about hacking or modding an old gameboy. In this project, we're building a completely new gaming device using 3D printing, the Raspberry Pi A+ and components from Adafruit.

**Please note** this is not a professional product! It's a DIY kit, and is great fun to build, but it may not have great emulation, video, audio etc.

3D printing allows you to design custom enclosures for your projects. The design and form factor are very much inpsired by the gameboy, but by no means meant to look exactly like it. 

[ ![gaming_hero_pigrrl_compare_small.jpeg](https://cdn-learn.adafruit.com/assets/assets/000/025/202/medium800/gaming_hero_pigrrl_compare_small.jpeg?1430692193) __ ](/assets/25202)

##  Raspberry Pi

Our first PiGRRL project used the Raspberry Pi Model B and and Adafruit 2.8' PiTFT. 

In this project, we're using the Raspberry model A+ and a 2.4" PiTFT HAT. The small size of the A+ and the compact display really allows this project to be one of the smallest builds yet.

  * Raspberry Pi A+
  * PiTFT 2.4" 320x240 Touch Display
  * Retropie w/ Emulation Station
  * Mono Audio Amp + 8 ohm ~1W Speaker
  * Tactile Buttons w/ Perma-Proto
  * Powerboost 1000C w/ 2000mAh lipo battery

##  This Guide

This tutorial will walk you through the assembly and wiring. It's a challenging build but it's not the most hardest thing ever. Our intent was to make this project easier than our previous PiGRRL build.

So, if this is your first DIY electronics + 3D Printing project, you might want try a simplier project with less wiring and soldering. That said, you shouldn't feel discouraged to take on the project.

[ ![gaming_hero_pocket_pigrrl_smaller.jpeg](https://cdn-learn.adafruit.com/assets/assets/000/025/200/medium800/gaming_hero_pocket_pigrrl_smaller.jpeg?1430688878) __ ](/assets/25200)

##  Prerequisite Guides

We recommend walking through these guides to get familiar with the software and components. You don't have to, but it's a good idea to check them out if you're not sure what all these things do. 

  * [Running OpenGL-based Games](../../../running-opengl-based-games-and-emulators-on-adafruit-pitft-displays)
  * [Adafruit Pi Finder](../../../the-adafruit-raspberry-pi-finder)
  * [Powerboost 1000c intro](../../../adafruit-powerboost-1000c-load-share-usb-charge-boost/overview)
  * [Colin's Lab: Soldering](../../../collins-lab-soldering)

[ ![gaming_parts.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/832/medium800/gaming_parts.jpg?1430060829) __ ](/assets/24832)

##  Parts

The parts below were used in this project. You don't have to use the exact same parts but the enclosure was designed to specially fit these parts - so if you want to use different components, you can but just know it may not fit in the provided enclosure. You can of course tweak the CAD files.

  * [Raspberry Pi A+](https://adafruit.com/products/2266)
  * [2.4" PiTFT touch screen](https://adafruit.com/products/2455)
  * [Powerboost 1000C](https://adafruit.com/products/2465)
  * [2.5W Class D Audio Amplifier - PAM8302](https://www.adafruit.com/products/2130)
  * [2000mAh lithium polmyer battery](https://adafruit.com/products/2011)
  * [Perma-proto half-sized](https://www.adafruit.com/product/1609)
  * [GPIO Pi Ribbon Cable - 26 pin](https://www.adafruit.com/product/862)
  * [6mm tactile buttons (square)](https://www.adafruit.com/product/367)
  * [6mm tactile switch buttons (slim)](https://www.adafruit.com/product/1489)
  * [12mm tactile buttons](https://www.adafruit.com/product/1119)
  * [Mini metal speaker](https://www.adafruit.com/product/1890)
  * [Slide switch](https://www.adafruit.com/product/805)

##  Tools

Having the right tools makes this build easier and more fun. Most of these are available in the shop but use whatever tools you have on hand.

  * [3D Printer](http://www.adafruit.com/category/128)
  * [Soldering Iron](https://www.adafruit.com/categories/84)
  * [Flush cutters](https://www.adafruit.com/product/152)
  * [Wire strippers](https://adafruit.com/products/527)
  * [Panavise Jr.](https://adafruit.com/products/151)
  * [Helping third hand](https://adafruit.com/products/291)
  * [Screwdriver](https://www.adafruit.com/product/829)
  * Rotary cuttting power tool

##  Supplies

Wires, screws, magnets, filament - The supplies listed below are both helpful and necessary for completing this project.  

  * [30AWG silicone cover stranded-core wire](https://adafruit.com/products/2051)
  * [Heat shrink tubing](https://adafruit.com/products/1649)
  * [3D printing filament](https://adafruit.com/products/2080)
  * [Blue painters tape](https://adafruit.com/2416)
  * Solder rosin-core
  * [12 #4-40 flat phillips machine screws](http://amzn.com/B00FAUB99Q) or [here](http://www.albanycountyfasteners.com/Phillips-Flat-Head-Machine-Screw-4-40-Stainless-p/1600000.htm?1=1&CartID=0)
  * 2 Neodymium Magnets 1/4 x 1/16 inch Disc N48

#  Circuit Diagram

by [ Ruiz Brothers ](/users/pixil3d)

[ ![gaming_circuit-diagram.png](https://cdn-learn.adafruit.com/assets/assets/000/025/508/medium800/gaming_circuit-diagram.png?1431660433) __ ](/assets/25508)

The circuit diagram above shows the connections for the power and audio. The lengths of the connections are not exact and mostly ment to visually represent which pin goes where. It's best to use this as a reference for pins.

##  Powerboost 1000c 

The slide switch is wired to pin **GND** and **EN**. The 2000mAh lithium polymer battery is connected to the JST port. The **#2(5V)** and **#6(GND)** connections represent the wire number from the Pi ribbon cable.

##  PAM8302

The **VIN** and **GND** pins are wired to the **5V** and **GND** pins on the powerboost 1000c. The **A+** and** A-** pins are wired directly to the audio pins on the bottom of the Raspberry Pi A+. The speaker is wired to the amps audio output (+ and -).

[ ![gaming_gamepad-button-pcb.png](https://cdn-learn.adafruit.com/assets/assets/000/025/088/medium800/gaming_gamepad-button-pcb.png?1430419333) __ ](/assets/25088)

##  Perma-Proto Two Button Layout

To interface the Pi with the tactile buttons, we'll use a Pi ribbon cable (26 pin). The connections below indicate the wire number, gpio name and keyboard input controller button. The White colored wire will be represented as Wire #1. The blue connections indicate the ground for each buttons. These are all wired to the bottom ground rail.

  * Wire # 2 - 5V Powerboost
  * Wire # 6 - GND Powerboost
  * Wire # 7 (GPIO 4) - Key Left
  * Wire # 9 - Ground for Buttons PCB
  * Wire # 11 (GPIO 17) - Key Right
  * Wire # 12 (GPIO 18) - Key Up
  * Wire # 13 (GPIO 27) - Key Down
  * Wire # 15 (GPIO 22) - Key A
  * Wire # 16 (GPIO 23) - Key B

##  PiTFT Buttons

There is five buttons that is connected to the PCB near on the bottom of the display. The GPIO number for these buttons are listed below and on the PCB.

  * GPIO 5 - Key Z
  * GPIO 6 - ESC
  * GPIO 12 - ENTER
  * GPIO 13 - SPACE
  * GPIO 16 - Key X

[ ![gaming_four-button-pcb.png](https://cdn-learn.adafruit.com/assets/assets/000/025/569/medium800/gaming_four-button-pcb.png?1431978727) __ ](/assets/25569)

##  Perma-Proto Four Button Layout

The four button version uses the same wiring from the Pi Cable, except two extra wires need to be connected to the Perma-proto PCB.

  * Wire #3 (GPIO 2) - Key X
  * Wire #5 (GPIO 3) - Key Y

##  Half size Perma-Proto

The diagram above shows which buttons are connected to the perma-proto PCB. Ideally, I want to say you can customize and change it up, but then the buttons won't fit in the cutouts on the 3D printed enclosure - so if you wanna change this layout, you'll also have to update the CAD, so keep that in mind.

##  GPIO Ribbon Cable

To make the wiring a bit easier, we're using a Pi ribbon cable (the 26-pin one). This cable as a nifty connector that fits perfectly on the GPIO breakout on the 2.4" PiTFT. We'll remove the connector from the other side and wire that up directly to the buttons on the Perma-Proto.

#  Software

by [ Ruiz Brothers ](/users/pixil3d)

##  Download and Burn SD Card

The first step is to download the PocketPiGRRL image, which includes retrogame, fbcp tools and GPIO controls preinstalled. Once it’s downloaded, you’ll need to properly burn the .IMG file to a microSD card (4GB min). I personally used [RPi-SD card builder v1.2](http://elinux.org/RPi_Easy_SD_Card_Setup).

[Download Pocket PiGRRL IMG](http://adafruit-download.s3.amazonaws.com/pocketgamegrrl_5_14_2015_c.zip)

__ This IMG is optimized for the "two-button" version. If you're making the four button version, you'll need to make a minor edit to the retrogame.c file. 

##  Setup Network

Next step is to get wifi network situated on the Pi. We need the Pi to connect to your local wifi network so you can SSH and install ROMs. You’re most likely going to want a USB wifi dongle. To set this up, edit the **/boot/occidentalis.txt** and add your WiFi credentials. 

##  Adding Four Button Controls

The PiGRRL Img is currently configured for the two button version. To get the four buttons working in Retrogame, you'll need to add them in the **retrogame.c** file.

Make sure the Raspberry Pi is configured for Wifi. Open up terminal and ssh into the Pi. (Default username: **pi** password: **raspberry**) Get into the Adafruit-Retrogame directory and edit the **retrogame.c** file.

Copy Code

    
    
    ssh [[email protected]](/cdn-cgi/l/email-protection)
    cd Adafruit-Retrogame
    sudo nano retrogame.c
    
    
    ssh [[email protected]](/cdn-cgi/l/email-protection)
    cd Adafruit-Retrogame
    sudo nano retrogame.c

Scroll down to the part where you see the table called ioStandard (_not_ the ioTFT table — that’s for other projects). Each line in brackets represents one pin on the GPIO header and a corresponding key code.

You can map the controls to any keyboard characters you'd like. The full list of available keycodes can be found in **/usr/include/linux/input.h**

Copy Code

    
    
    ioStandard[] = { 
    // This pin/key table is used when the PiTFT isn't found 
    // (using HDMI or composite instead), as with our original 
    // retro gaming guide. 
    // Input Output (from /usr/include/linux/input.h) 
    { 4, KEY_LEFT }, // Joystick (4 pins) 
    { 17, KEY_RIGHT }, 
    { 18, KEY_UP }, 
    { 27, KEY_DOWN }, 
    { 22, KEY_LEFTCTRL }, // A/Fire/jump/primary/RED
    { 23, KEY_LEFTALT }, // B/Bomb/secondary/YELLOW 
    { 2, KEY_X }, // X/BLUE 
    { 3, KEY_Z }, // Y/GREEN 
    { 5, KEY_A }, // L Shoulder 
    { 16, KEY_S }, // R Shoulder 
    { 6, KEY_ESC }, // EXIT ROM 
    { 12, KEY_ENTER }, // START 
    { 13, KEY_SPACE }, // PAUSE
    
    
    ioStandard[] = { 
    // This pin/key table is used when the PiTFT isn't found 
    // (using HDMI or composite instead), as with our original 
    // retro gaming guide. 
    // Input Output (from /usr/include/linux/input.h) 
    { 4, KEY_LEFT }, // Joystick (4 pins) 
    { 17, KEY_RIGHT }, 
    { 18, KEY_UP }, 
    { 27, KEY_DOWN }, 
    { 22, KEY_LEFTCTRL }, // A/Fire/jump/primary/RED
    { 23, KEY_LEFTALT }, // B/Bomb/secondary/YELLOW 
    { 2, KEY_X }, // X/BLUE 
    { 3, KEY_Z }, // Y/GREEN 
    { 5, KEY_A }, // L Shoulder 
    { 16, KEY_S }, // R Shoulder 
    { 6, KEY_ESC }, // EXIT ROM 
    { 12, KEY_ENTER }, // START 
    { 13, KEY_SPACE }, // PAUSE

After editing, compile, install the code and reboot with:

Copy Code

    
    
    make retrogame
    sudo mv retrogame /usr/local/bin
    sudo reboot
    
    
    make retrogame
    sudo mv retrogame /usr/local/bin
    sudo reboot

When the Raspberry Pi boots back up, it should automatically launch Emulation Station. Your four buttons should all be working now.

The five button on the PiTFT are ordered from left to right:

  1. L shoulder(a key)
  2. Exit ROM (esc key)
  3. Start (enter key)
  4. Pause (spacebar)
  5. R shoulder(s key) 

##  Configuring RetroArch Emulators Controls

Editing the retrogame file configures the buttons for the EmulationStation input — it does NOT transfer to each emulator, but you can configure the **Global** settings - that are settings which should apply to all emulators.

Copy Code

    
    
    sudo nano /opt/retropie/configs/all/retroarch.cfg 
    
    
    sudo nano /opt/retropie/configs/all/retroarch.cfg 

Scroll down and look for the #Keyboard Input block.

Copy Code

    
    
    # Keyboard input, Joypad and Joyaxis will all obey the "nul" bind, which disabl$
    # rather than relying on a default.
    input_player1_a = ctrl
    input_player1_b = alt
    input_player1_y = z
    input_player1_x = x
    input_player1_start = enter
    input_player1_select = space
    input_player1_l = a
    input_player1_r = s
    input_player1_left = left
    input_player1_right = right
    input_player1_up = up
    input_player1_down = down
    
    
    # Keyboard input, Joypad and Joyaxis will all obey the "nul" bind, which disabl$
    # rather than relying on a default.
    input_player1_a = ctrl
    input_player1_b = alt
    input_player1_y = z
    input_player1_x = x
    input_player1_start = enter
    input_player1_select = space
    input_player1_l = a
    input_player1_r = s
    input_player1_left = left
    input_player1_right = right
    input_player1_up = up
    input_player1_down = down

Now most of your four button type game systems (mainly SNES) should be linked to the right controls on the Raspberry Pi.

#  Software [Manual]

by [ Ruiz Brothers ](/users/pixil3d)

__ We recommend you go with the ready-to-download image rather than trying to do this by hand, but here's details if you're interested! 

#  Download & Burn RetroPie

Game emulation is handled by a package called _**RetroPie**._ It’s a complete Linux distribution designed specifically for running classic games on Raspberry Pi.

[Download the current version from the RetroPie web site](https://retropie.org.uk/download/), then [write this to an SD card](../../../../adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi) using Etcher or similar software.

We’ll then make some modifications to tune this for the PiGRRL’s buttons and small display.

Setup will require an **HDMI monitor**, **USB keyboard** and a **network connection** (a USB **WiFi** or **Ethernet** dongle, for example). This is best done_ **before **_the Pi is enclosed in the PiGRRL case. If you have a spare Raspberry Pi board around, that’s an ideal option…you could prepare the software on that system and then move the card over to the PiGRRL.

A USB/Ethernet hub + a Keyboard is ideal

[ ![USB 2.0 and Ethernet Hub - 3 USB Ports and 1 Ethernet](https://cdn-learn.adafruit.com/products/images/000/002/909/medium310/2909-01.jpg?1502194551) ](https://www.adafruit.com/product/2909)

### [USB 2.0 and Ethernet Hub - 3 USB Ports and 1 Ethernet](https://www.adafruit.com/product/2909)

PRODUCT ID: 2909

One can never have enough socks, or USB ports. Add some more USB and Ethernet capability to your Raspberry Pi or, really, any kind of computer with this USB 2.0 and Ethernet Hub...

[ Add To Cart ](https://www.adafruit.com/product/2909)

$14.95

IN STOCK

#  Setup RetroPie

Insert the RetroPie card to your Pi, attach monitor and keyboard (and Ethernet, if networking that way), then power the system from a USB power source (a USB phone charger or a powered USB hub can usually work). The system will automatically reboot once (it needs this to make use of the whole SD card), then on second boot it will ask to configure the game controls…

**The PiGRRL buttons don’t work yet; this is normal.** For initial setup, **use the USB keyboard** to select the D-pad directions (arrow keys), Start, Select, A and B keys. For anything else, just hold down the space bar or other key to skip that item . Don't worry, we'll re-do the keymap later once we've finished assembly! When finished, you’ll see a graphical interface called _Emulation Station_ where you’ll select games and other options.

Let’s **get this Raspberry Pi on the network** first. If WiFi, from the main EmulationStation screen, access the RetroPie settings using whatever key you’ve assigned as the “A” button. You’ll see **WIFI** in this list:

  * [ ![gaming_raspberry_pi_wifi2.png](https://cdn-learn.adafruit.com/assets/assets/000/038/174/medium640/gaming_raspberry_pi_wifi2.png?1483658076) ](/assets/38174)

Here you can select your WiFi network name and enter a password. It’s not beautiful, but gets the job done.

Select “Exit” when done to return to the EmulationStation UI…

With networking enabled, we can now access the remaining software needed for the PiGRRL 2 experience. There are a couple ways to do this…

  * **BEST:** Use an **ssh** terminal client to log into the Raspberry Pi at **retropie.local**   

This is recommended, as you can just copy-and-paste the commands that follow. The default name and password are “pi” and “raspberry,” respectively.

  * **OR:** Press “F4” to exit EmulationStation for a command-line prompt (works, but you’ll need to type these commands _exactly_).

##  Testing Retrogame

Once the SD card is finished, insert it into the Pi and boot it up. You should get emulation station to boot automatically. Configure your controls using a keyboard and test out the games in the ports section to make sure everything is running properly.

#  Install PiTFT (fbcp) Support

This first sequence configures the system for the PiTFT display:

Copy Code

    
    
    cd
    curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/pitft-fbcp.sh
    sudo bash pitft-fbcp.sh
    
    
    cd
    curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/pitft-fbcp.sh
    sudo bash pitft-fbcp.sh

Select the “Pocket PiGRRL” option, which sets up various system parameters to match this project.

[ ![gaming_pocketpigrrl.png](https://cdn-learn.adafruit.com/assets/assets/000/038/175/medium800/gaming_pocketpigrrl.png?1483660499) __ ](/assets/38175)

Answer “**NO**” to the reboot question…

[ ![gaming_noreboot.png](https://cdn-learn.adafruit.com/assets/assets/000/038/178/medium800/gaming_noreboot.png?1483661045) __ ](/assets/38178)

#  Edit Config.txt

For optimized speed and decent audio from the emulators, may want to to tweak some settings in the config.txt file, for overclocking/gpu configuration

Copy Code

    
    
    gpu_mem=44
    disable_audio_dither=1
    overscan_scale=1
    #gpu_mem_256=128
    #gpu_mem_512=256
    #gpu_mem_1024=256
    dtoverlay=pitft22,rotate=270,speed=60000000,fps=40
    display_rotate=0
    hdmi_cvt=320 240 60 1 0 0 0
    arm_freq=1000
    core_freq=500
    sdram_freq=450
    over_voltage=6
    
    
    gpu_mem=44
    disable_audio_dither=1
    overscan_scale=1
    #gpu_mem_256=128
    #gpu_mem_512=256
    #gpu_mem_1024=256
    dtoverlay=pitft22,rotate=270,speed=60000000,fps=40
    display_rotate=0
    hdmi_cvt=320 240 60 1 0 0 0
    arm_freq=1000
    core_freq=500
    sdram_freq=450
    over_voltage=6

Also, set the audio to 3.5mm with **sudo raspi-config **(under Advanced/Audio)

[ ![gaming_force35.png](https://cdn-learn.adafruit.com/assets/assets/000/038/180/medium800/gaming_force35.png?1483664623) __ ](/assets/38180)

#  Installing Keypress (retrogame) support

let’s take care of this second script, which enables the PiGRRL buttons:

Copy Code

    
    
    cd
    curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/retrogame.sh
    sudo bash retrogame.sh
    
    
    cd
    curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/retrogame.sh
    sudo bash retrogame.sh

Again, select the “Pocket PiGRRL” option. When finished, _now_ you can reboot when prompted.

[ ![gaming_retro.png](https://cdn-learn.adafruit.com/assets/assets/000/038/179/medium800/gaming_retro.png?1483661140) __ ](/assets/38179)

After rebooting, the HDMI monitor may display a “no signal” message. This is normal. Not all monitors can handle the resolution setting we’re using. Once the PiTFT is wired up, that will be the primary display.

Also, **after the system is assembled with the PiTFT and controls**, you’ll need to **re-do the controller setup.** This might wait ’til all the parts are **assembled in the case.**

  * [ ![gaming_raspberry_pi_input.png](https://cdn-learn.adafruit.com/assets/assets/000/038/176/medium640/gaming_raspberry_pi_input.png?1483660649) ](/assets/38176)

From the main EmulationStation screen, press whatever key was assigned to the “Start” button to access the main menu. You’ll find an option here for “CONFIGURE INPUT.”

Go through the control setup process again using the PiGRRL buttons now instead of the keyboard; assign the D-pad directions, Start and Select buttons, A, B, X and Y. For anything else, hold down a key or button to skip it.

#  Configuration

by [ lady ada ](/users/adafruit2)

##  Uploading ROMs

Check out the Wiki on the RetroPie Setup page for how to upload ROMs:

[RetroPie - Uploading ROMs](https://github.com/petrockblog/RetroPie-Setup/wiki/How-to-get-ROMs-on-the-SD-card)

#  Exiting ROMs

Retropie has changed how to exit out of ROMs/Emulators. Hold down the **Pause & Start **buttons at the same time to exit.

#  Remapping Controls

The buttons are premapped to work with NES and SNES emulators. If you'd like to remap the controls, you'll need to modify the **retrogame.cfg** file in /boot.

Make sure the Raspberry Pi is configured for Wifi. Open up terminal and ssh into the Pi. (Default username: **pi** password:**raspberry**)

[Then follow the retrogame tutorial to set it up the way you like!](../../../../retro-gaming-with-raspberry-pi/adding-controls-software)

#  Testing Controls

If you log in (via SSH or F4 shell) you can see exactly what keypresses are detected by running **evtest** then select 1 (or whatever **retrogame** is numbered):

[ ![gaming_raspberry_pi_evtest.png](https://cdn-learn.adafruit.com/assets/assets/000/038/177/medium800/gaming_raspberry_pi_evtest.png?1483660900) __ ](/assets/38177)

Make sure each keypress works and matches the table below!

LEFT

Pin 7

GPIO 4

UP

Pin 36

GPIO 16

RIGHT

Pin 35

GPIO 19

DOWN

PIN 37

GPIO 26

#  3D Printing

by [ Ruiz Brothers ](/users/pixil3d)

##  Two Button Version

[ ![gaming_3d_parts_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/992/medium800/gaming_3d_parts_case.jpg?1430177058) __ ](/assets/24992)

##  Four Button Version

[ ![gaming_3d_parts_4btn.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/558/medium800/gaming_3d_parts_4btn.jpg?1431970708) __ ](/assets/25558)

##  Parts

The parts are optimized to print as is, oriented centered on your printers build plate. The parts will fit on any printer with a minimum bed size of 120mm x 70mm.

[Download Files](http://www.thingiverse.com/thing:807591)

File Name

Settings

Time to Print

pgp-top.stl

220c  
2 shells  
10% infill  
50/60 speeds

1hr

pgp-bot.stl

-

1hr 10mins

PiTFT-Buttons.stl

ninjaflex @230  
2 shells  
20% infill  
30/40 speeds

about 15 minutes

ab-buttons.stl

made for two Ninjaflex buttons

about 15 minutes

dpad.stl

Makes the DPAD (Up, Down, Left and Right) can also be printed in PLA or Ninajflex

about 10 minutes

pgp-4-top.stl

used to make four-button version top case

about 1 hour

pgp-4-bot.stl

used to make four-button version bottom case

about 1hr 15min

flex-4btn.stl

used to make four ninjaflex button version

about 6 minutes

hard-btn.stl

used to make four hard PLA buttons

about 3 minutes each

The settings adove are for reference. You're encouraged to slice these files for your printer using your preferred slicing software.

##  Support material

No raft or support material necessary here. The overhands are small enough that it doesn't present any problems with most FDM 3D printers.

##  Tolerances

3D printers tend to vary from one another, so it's no surpise that one printer makes parts tighter than the other. That slight 0.1mm difference is enough to make things not fit exactly. Maybe the mounting holes are too tight, or the speaker doesn't fit. If that's the case, you can loosen them up with a filing tool or adjusting the faces in the CAD model. 

##  Materials

We tested the parts in PLA, ABS, BambooFill and CopperFill. You're can use whatever material and color you want to use in this project. 

##  Warping

Minimize warping by using blue painters tape. Apply gluestick or aqua net hair spray on a glass plate if applicable. If you're using a heated bed, be sure to enclose the printer to avoid air drafts.

##  First layer + Bed Leveling

The first layer should be as thin as a sheet of paper. Kinda of hard to see but here's some stuff to look out for. If you see the layers are not fully bonding together, the nozzle is too far from the bed. If the layers are overlapping, the nozzle is too close to the bed.

Ideally, you want to baby sit the first layer to ensure your bed is leveled. If your printers bed can be adjusted with thumb screws, you'll want to perform leveling "live", while the print is taking place. If you're using a z-probe with auto-leveling, you'll have to manually offset your z-height in gcode.

[ ![gaming_3d_parts_buttons.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/993/medium800/gaming_3d_parts_buttons.jpg?1430177100) __ ](/assets/24993)

##  Ninjaflex buttons

You can use TPE flexible filament for the buttons. The flexible filament works really well here because it gives you a bit of flex and grip when you press the buttons. PLA, ABS and other hard plastics will work just fine for the D-PAD but it might not work so well with the A+B and PiTFT buttons.

##  Quality Prints

If your new to 3D printing and wondering: how did you get such a nice print? It's mainly because the bed was leveled really good and the slice tool path is clean.

When you're slicing  parts, it's a good idea to check the toolpath and see how the nozzle is generating the walls in the part. Ideally you want to adjust your settings so that the walls are being printed with no infill and just the shells. This makes the wall appear really clean.

Don't be fool by the photos though, if you look carefully you can see we have imperfections and minor warped corners. We printed the blue one in ABS and the purple in PLA - The PLA parts even had a small amount of warping. The ABS part was printed on a makerbot replicator 1. Purple parts were printed on a Replicator 2. Both using makerware.

  * [ ![gaming_mags_setup.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/191/medium640/gaming_mags_setup.jpg?1430585642) ](/assets/25191)
  * [ ![gaming_mags_setup.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/191/thumb160/gaming_mags_setup.jpg?1430585642) ](/assets/25191)
  * [ ![gaming_mags_applying.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/192/thumb160/gaming_mags_applying.jpg?1430586191) ](/assets/25192)
  * [ ![gaming_mags_drying.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/193/thumb160/gaming_mags_drying.jpg?1430586238) ](/assets/25193)
  * [ ![gaming_mags_applied.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/195/thumb160/gaming_mags_applied.jpg?1430586335) ](/assets/25195)

## Magnets

In order to keep these parts closed, we used two neodymium magents to keep them shut. I recommend gluing these to the two enclosure part before starting wiring. These magnets fit inside the corner standoff located near the bottom roudned corner - you can't miss it! You can use super glue to keep them in place. Be sure to double check the polarity before gluing them!

#  Wiring

by [ Ruiz Brothers ](/users/pixil3d)

[ ![gaming_tinned_switch_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/252/medium800/gaming_tinned_switch_wires.jpg?1430836711) __ ](/assets/25252)

##  Prep Wiring

Before starting it's a good idea to get your tools and workspace suitated. You'll want to have wires, tools and solder close by while you work through the sections.

##  Cut, Strip, Tin, Repeat

The wiring portion of this build is split into sections relative to the components. This hopefully makes it a good way to take breaks when completing sections. 

##  The Slide Switch

The slide switch is wired to the Powerboost 1000c with just three wires (**Vs**, **GND** and **EN**). It's wired to the enable pin so that it safely discharges the powerboost 1000c. This however will not safely power off the Raspberry Pi - You'll still need to "sudo -halt p" that to do that safely.

[ ![gaming_secure_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/254/medium800/gaming_secure_boost.jpg?1430836808) __ ](/assets/25254)

##  Powerboost 1000C

The Raspberry Pi, PiTFT and PAM8302 are powered by the Powerboost 1000c and a 2000mAh lithium polymer battery. A Pi ribbon cable connects from the PiTFT to the positive and negative power pins on the powerboost breakout board (in place of the USB port). The microUSB port on the powerboost can be used to recharge the lipo battery. The lipo battery connects to the on-board JST conenctor.

[ ![gaming_prep_wires_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/255/medium800/gaming_prep_wires_pam8302.jpg?1430836875) __ ](/assets/25255)

##  PAM8302 & Speaker

This 2.5w mono amplifier is powered by the powerboost 1000c (5V and G). The audio input is connected to the audio jack pins on the bottom of the Raspberry Pi. A single mini metal speaker is wired to the output on the breakout.

[ ![gaming_buttos_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/256/medium800/gaming_buttos_pitft.jpg?1430836963) __ ](/assets/25256)

##  2.4' PiTFT

The PiTFT is designed to fit ontop of the Raspberry Pi GPIO header. The PCB on the display has a GPIO socket which can connect to a Pi ribbon cable. We'll use the Pi ribbon cable to wire up tactile buttons for the controls. The 2.4' PiTFT has five spots on the PCB for tactile buttons. Use these buttons as pause, start, L shoulder, R shoulder or even exit ROM. The display shares power with the Raspberry Pi, so that gets powered on when the Pi ribbon cable is wired up to the powerboost 1000c.

[ ![gaming_install_btns_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/257/medium800/gaming_install_btns_permaproto.jpg?1430837016) __ ](/assets/25257)

##  Perma-proto

To connect our buttons we're using a perma-proto half-sized breadboard to contain them together on a PCB. The PCB will need to be cut and trimmed to fit inside the enclosure. The 6 controller buttons are soldered to the PCB. The Pi ribbon cable is wired to these buttons. The perma-proto has a power rail, so we can connect the ground together in series.

#  Switch

by [ Ruiz Brothers ](/users/pixil3d)

  * [ ![gaming_cut_switch_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/835/medium640/gaming_cut_switch_wires.jpg?1430061193) ](/assets/24835)
  * [ ![gaming_cut_switch_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/835/thumb160/gaming_cut_switch_wires.jpg?1430061193) ](/assets/24835)
  * [ ![gaming_strip_switch_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/836/thumb160/gaming_strip_switch_wires.jpg?1430061354) ](/assets/24836)
  * [ ![gaming_tinning_switch_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/837/thumb160/gaming_tinning_switch_wires.jpg?1430061427) ](/assets/24837)
  * [ ![gaming_tinned_switch_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/838/thumb160/gaming_tinned_switch_wires.jpg?1430061538) ](/assets/24838)

## Prepping Slide Switch

We need to prep the wires for the slide switch. You can use any colored wires. We used three different colored 30AWG silicone coated wires because it’s thin, flexible and easier to indicate. Red for positive, blue for negative and green for enable. Measure three pieces of 30AWG wires and cut to approximately 6cm in length. Use wire stripper to remove 3-4mm of insulation from the tips of each wire. Use a helping third hand to hold the pieces of wire while you apply solder to the tips.

__ Skip the red wire, we don't need a third connection for the slide switch, only EN and GND. 

  * [ ![gaming_secure_switch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/839/medium640/gaming_secure_switch.jpg?1430061631) ](/assets/24839)
  * [ ![gaming_secure_switch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/839/thumb160/gaming_secure_switch.jpg?1430061631) ](/assets/24839)
  * [ ![gaming_tinning_switch_leg.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/840/thumb160/gaming_tinning_switch_leg.jpg?1430061672) ](/assets/24840)

## Secure Slide Switch

Secure the slide switch to a Panavise Jr. to hold it in place while you solder. Heat up the terminal lead on the slide switch with the tip of the soldering iron and lightly touch it with a strand of rosin-core solder. You’ll need to tin the three terminals on the slide switch by applying a small amount of solder to them.

[ ![gaming_soldered_switch_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/841/medium800/gaming_soldered_switch_wires.jpg?1430061771) __ ](/assets/24841)

##  Wire Slide Switch

While the switch is secured, grab a prepped wire and bring it close to the first terminal on the slide switch. Position the soldered tip of the wire to the terminals and hold it there steadily. Press the soldering iron against the terminal and wire to solder them together. You’ll want to do this gently and quickly. Ideally, you want the middle terminal be the “enable” while the far left/right be "ground", negative.

__ Again, skip the red wire, we don't need it! 

[ ![gaming_heatshrink_switch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/842/medium800/gaming_heatshrink_switch.jpg?1430061807) __ ](/assets/24842)

##  Heat Shrink Slide Switch

Once you’ve soldered up the three wires to the terminals, you’ll want to protect the connections with some heat shrink tubing. Cut a piece of heat shrink tubing that sizes for 30AWG wire to about 5-6mm in length. Slip these onto the three wires and position them over the exposed connections. Apply some heat to the tubing to shrink! Ideally want to use hot air.

  * [ ![gaming_case_switch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/843/medium640/gaming_case_switch.jpg?1430061905) ](/assets/24843)
  * [ ![gaming_case_switch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/843/thumb160/gaming_case_switch.jpg?1430061905) ](/assets/24843)
  * [ ![gaming_install_switch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/844/thumb160/gaming_install_switch.jpg?1430061988) ](/assets/24844)
  * [ ![gaming_installed_switch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/845/thumb160/gaming_installed_switch.jpg?1430062039) ](/assets/24845)
  * [ ![gaming_flush_switch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/846/thumb160/gaming_flush_switch.jpg?1430062085) ](/assets/24846)

## Install Slide Switch

Now that the switch is wired up and protected, it’s a good idea to install it into the enclosure before wiring it to the rest of the circuit. Carefully thread the into the slide switch cut out on the bottom enclosure part. Gently push the slide switch into the enclosure. You may want to use a hand tool or surface of a table to help force it in if the tolerances are too tight.

__ Ignore the red wire, we really don't need it for this project. We only need the Enable and Ground. 

#  Powerboost 1000C

by [ Ruiz Brothers ](/users/pixil3d)

  * [ ![gaming_secure_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/847/medium640/gaming_secure_boost.jpg?1430062643) ](/assets/24847)
  * [ ![gaming_secure_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/847/thumb160/gaming_secure_boost.jpg?1430062643) ](/assets/24847)
  * [ ![gaming_tinned_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/848/thumb160/gaming_tinned_boost.jpg?1430062798) ](/assets/24848)

## Prep PowerBoost 1000C

Next up we need to wire up the slide switch to the powerboost 1000c breakout. Secure the PCB to the helping third hands. We need to tin three pins so we can insert the wires from the slide switch. Heat up a pin with the tip of the soldering iron and apply solder. Tin pins 5V, G, GND, EN (we also did VBat but it isnt required). The pins should look like they have little soldered beads.

[ ![gaming_soldered_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/849/medium800/gaming_soldered_boost.jpg?1430062962) __ ](/assets/24849)

##  Wire Powerboost 1000C

Secure the breakout to the third helping hands and position it close to enclosure. Heat up the pins on the breakout board with the soldering iron and insert the wire. You’ll want to do this pretty quickly, about 5 seconds for each connection. Blue to **GND** and green to **EN**. You can **skip** the **red** wire, we don't need it**.**

__ The photo shows red wire to BAT, but you don't need to connect this wire, the circuit will function without the red wire. 

[ ![gaming_thread_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/850/medium800/gaming_thread_boost.jpg?1430063034) __ ](/assets/24850)

##  Thread Mounting Holes

It's a good idea to thead the holes on the PCB to make it easier to mount to the enclosure. #4-40 3/8 flat phillips machine screws work best.

[ ![gaming_tuck_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/851/medium800/gaming_tuck_boost.jpg?1430071048) __ ](/assets/24851)

##  Install PowerBoost 1000C

With the wires on the powerboost soldered, you can release it from the third helping hands. It’s a good idea to tuck the wires underneath the board before mounting it. Position the breakout over the bottom enclosure with the USB port facing the cut out. You’ll want to tuck the three wires from the slide switch underneath the PowerBoost 1000c. The stand-offs should give you enough clearance.

[ ![gaming_fasten_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/852/medium800/gaming_fasten_boost.jpg?1430071164) __ ](/assets/24852)

##  Mount PowerBoost 1000C

You’ll need #4-40 ⅜ Phillips flat machine screws to mount the board to the enclosure. Hold the breakout board in place while you insert and fasten two #4-40 machine screws into the enclosure.

[ ![gaming_test_boost.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/853/medium800/gaming_test_boost.jpg?1430071296) __ ](/assets/24853)

##  Test PowerBoost 100C

Plug in the JST cable from the rechargeable battery into the JST port. Flip the slide switch on to test if the circuit is working. The blue LED should turn on, indicating the battery is charged and ready. If everything lights up, disconnect the battery from the breakout board. If not, double check your wiring.

#  PAM8302

by [ Ruiz Brothers ](/users/pixil3d)

  * [ ![gaming_secure_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/858/medium640/gaming_secure_pam8302.jpg?1430073494) ](/assets/24858)
  * [ ![gaming_secure_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/858/thumb160/gaming_secure_pam8302.jpg?1430073494) ](/assets/24858)
  * [ ![gaming_tin_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/859/thumb160/gaming_tin_pam8302.jpg?1430073530) ](/assets/24859)

## Prep PAM8302

Get the amp breakout secured to the panavise jr. Heat up the pins and apply some solder to all but the **SD** pin on the breakout.

  * [ ![gaming_prep_wires_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/856/medium640/gaming_prep_wires_pam8302.jpg?1430073268) ](/assets/24856)
  * [ ![gaming_prep_wires_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/856/thumb160/gaming_prep_wires_pam8302.jpg?1430073268) ](/assets/24856)
  * [ ![gaming_tin_wire_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/857/thumb160/gaming_tin_wire_pam8302.jpg?1430073318) ](/assets/24857)

## PAM8302 Wires

Measure and cut two 30AWG wires to about the length of the PCB. Strip the ends off each wire and tin the tips.

[ ![gaming_thread_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/860/medium800/gaming_thread_pam8302.jpg?1430073654) __ ](/assets/24860)

##  Thread PAM8302

Just like the powerboost PCB, it's a good idea to thread the mounting hole with a machine screw. We only need one hole threaded since we're using a single screw to secure the PCB to the enclosure.

[ ![gaming_wiring_pwr_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/861/medium800/gaming_wiring_pwr_pam8302.jpg?1430073816) __ ](/assets/24861)

##  Solder Wires to PAM8302

Secure the PCB and solder the red wire to **Vin** pin and the blue wire to **GND.**

  * [ ![gaming_fit_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/862/medium640/gaming_fit_pam8302.jpg?1430074000) ](/assets/24862)
  * [ ![gaming_fit_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/862/thumb160/gaming_fit_pam8302.jpg?1430074000) ](/assets/24862)
  * [ ![gaming_fasten_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/863/thumb160/gaming_fasten_pam8302.jpg?1430074036) ](/assets/24863)

## Mount PAM to enclosure

Fit the breakout over the spot near the powerboost 1000c and line up the holes. Hold the PCB in place while you fasten a single #4-40 3/8 flat phillips machine screw.

[ ![gaming_wired_pwr_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/864/medium800/gaming_wired_pwr_pam8302.jpg?1430074311) __ ](/assets/24864)

##  Solder power to PAM8302

Solder up the red wire from **Vin** to **5V **on the powerboost 1000c. Then connect the blue wire from **Gnd** to **G **on the powerboost 1000c.

#  Pi Audio

by [ Ruiz Brothers ](/users/pixil3d)

[ ![gaming_prep_audio_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/865/medium800/gaming_prep_audio_wires.jpg?1430074555) __ ](/assets/24865)

##  Cut Pi Audio wires

Measure and cut up two wires for connecting to the audio jack on the Pi, to the audio input on the PAM8302.

[ ![gaming_tin_audio_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/866/medium800/gaming_tin_audio_wires.jpg?1430074631) __ ](/assets/24866)

##  Strip and Tin Wires

Strip off the ends of each wire and tin the tips. Quick tip, you can secure both wires to a helping third hand so you can solder them all at once.

[ ![gaming_tin_pi_audio_spots.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/867/medium800/gaming_tin_pi_audio_spots.jpg?1430074669) __ ](/assets/24867)

##  Tin Audio pins on Pi

Next up we need to prep the solder points on the Pi to make it easier to solder our audio wires. Start by securing the Pi to the panavise jr downside up. Locate the audio jack and find the two solder spots for the positive and ground. Add a small amount of solder to these points.

[ ![gaming_soldered_pi_audio_wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/868/medium800/gaming_soldered_pi_audio_wires.jpg?1430077891) __ ](/assets/24868)

##  Solder Audio Wires to Pi

 Hit those points with the iron and solder the wires to positive and ground. The ground (white wire) can be indicated by seeing there's no traces connected to it. The positive (red wire) connection has visible traces.

[ ![gaming_soldered_pam8302.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/870/medium800/gaming_soldered_pam8302.jpg?1430078443) __ ](/assets/24870)

##  Solder Audio wires to PAM8302

Place the Pi into the base with the audio jack facing amp. Wire the positive (red wire) to A+ pin and the ground (white wire) to the A- pin on the PAM8302

  * [ ![gaming_prep_screw_pi.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/872/medium640/gaming_prep_screw_pi.jpg?1430078849) ](/assets/24872)
  * [ ![gaming_prep_screw_pi.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/872/thumb160/gaming_prep_screw_pi.jpg?1430078849) ](/assets/24872)
  * [ ![gaming_screw_pi.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/873/thumb160/gaming_screw_pi.jpg?1430078897) ](/assets/24873)

## Mount Pi

Hold the Pi in place while you insert and fasten four #4-40 3/8 flat phillips machine screws into the mounting holes. 

[ ![gaming_screwed_pi.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/874/medium800/gaming_screwed_pi.jpg?1430079008) __ ](/assets/24874)

##  Mounted Pi

The screws should be fastened all the way so they're flush with the surface of the case.

#  Speaker

by [ Ruiz Brothers ](/users/pixil3d)

[ ![gaming_remove_wires_speaker.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/875/medium800/gaming_remove_wires_speaker.jpg?1430079331) __ ](/assets/24875)

##  Prep Metal Speaker

Secure the speaker on the helping third hands (it has a magnet so just let it stick to one of the grabbers). Hit the solder joints and remove the wires.

__ Be careful not to touch the magnet with the soldering iron tip! 

  * [ ![gaming_prep_wires_speaker.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/877/medium640/gaming_prep_wires_speaker.jpg?1430079684) ](/assets/24877)
  * [ ![gaming_prep_wires_speaker.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/877/thumb160/gaming_prep_wires_speaker.jpg?1430079684) ](/assets/24877)
  * [ ![gaming_tin_wires_speaker.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/878/thumb160/gaming_tin_wires_speaker.jpg?1430079784) ](/assets/24878)

## Prep New Wires for Speaker

Sit the two case parts close to each other to guage wire length and cut two pieces. Strip the tips of each wire and add solder to tin the tips. 

[ ![gaming_solder_wires_speaker.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/879/medium800/gaming_solder_wires_speaker.jpg?1430081555) __ ](/assets/24879)

##  Solder Wires to Speaker

Heat up the solder points on the speaker and connect the wires. The positive and negative symbols are indicated on the speaker. If it's not, follow the photo to reference the polarity (left is negative, right is positive.)

  * [ ![gaming_insert_speaker.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/881/medium640/gaming_insert_speaker.jpg?1430082333) ](/assets/24881)
  * [ ![gaming_insert_speaker.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/881/thumb160/gaming_insert_speaker.jpg?1430082333) ](/assets/24881)
  * [ ![gaming_position_speaker.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/882/thumb160/gaming_position_speaker.jpg?1430082379) ](/assets/24882)

## Install Speaker

Position the speaker into the bottom corner of the enclosure. There's a circular indent with slits near the rounded corner of the case. That's where the speaker needs to go. The tolerance should be sized to fit the speaker tightly.

[ ![gaming_installed_speaker.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/883/medium800/gaming_installed_speaker.jpg?1430082442) __ ](/assets/24883)

##  Connect Speaker wires to PAM8302

Solder the wires from the speaker to the audio out pins on the PAM8302.

#  2.4 PiTFT

by [ Ruiz Brothers ](/users/pixil3d)

  * [ ![gaming_prep_header_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/889/medium640/gaming_prep_header_pitft.jpg?1430084328) ](/assets/24889)
  * [ ![gaming_prep_header_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/889/thumb160/gaming_prep_header_pitft.jpg?1430084328) ](/assets/24889)
  * [ ![gaming_insert_header_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/890/thumb160/gaming_insert_header_pitft.jpg?1430084376) ](/assets/24890)
  * [ ![gaming_tac_header_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/891/thumb160/gaming_tac_header_pitft.jpg?1430084475) ](/assets/24891)

## Install Header

Insert the header that came with the PiTFT into the PCB. Use a piece of fun tac to hold the header in place while you solder.

  * [ ![gaming_solder_header_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/892/medium640/gaming_solder_header_pitft.jpg?1430084585) ](/assets/24892)
  * [ ![gaming_solder_header_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/892/thumb160/gaming_solder_header_pitft.jpg?1430084585) ](/assets/24892)
  * [ ![gaming_soldered_header_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/893/thumb160/gaming_soldered_header_pitft.jpg?1430084653) ](/assets/24893)

## Secure Header

Solder the pins on the GPIO to seure the header to the PCB. The solder joints should look like little herseys kisses.

[ ![gaming_remove_tac_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/899/medium800/gaming_remove_tac_pitft.jpg?1430085229) __ ](/assets/24899)

##  Remove Tac

Remove the tac from the GPIO header. Ball it up and save it for the next project, it's served it's purpose!

  * [ ![gaming_buttos_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/894/medium640/gaming_buttos_pitft.jpg?1430084776) ](/assets/24894)
  * [ ![gaming_buttos_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/894/thumb160/gaming_buttos_pitft.jpg?1430084776) ](/assets/24894)
  * [ ![gaming_buttons_front_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/895/thumb160/gaming_buttons_front_pitft.jpg?1430084845) ](/assets/24895)
  * [ ![gaming_solder_btns_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/896/thumb160/gaming_solder_btns_pitft.jpg?1430084916) ](/assets/24896)
  * [ ![gaming_soldered_btns_pittft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/897/thumb160/gaming_soldered_btns_pittft.jpg?1430085004) ](/assets/24897)

## Add Buttons

Insert five tactile switch buttons into the designated spots on the PiTFT PCB. They snap fit and will hold in place. Secure the PCB to a panavise jr and solder the buttons to secure them.

[ ![gaming_snip_btns_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/898/medium800/gaming_snip_btns_pitft.jpg?1430085069) __ ](/assets/24898)

##  Trim buttons

Snip the excess leads from the buttons the PiTFT PCB. These bits are sharp and could scratch the components. 

  * [ ![gaming_cut_trace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/196/medium640/gaming_cut_trace.jpg?1430586477) ](/assets/25196)

## Disable GPIO 18 Lite

By default, the 2.4' PiTFT uses GPIO 18 to turn on/off the backlight on the display. In this build we're using GPIO 18 as a input button, so we need to cut the trace located on the back of the PCB, labled **#18 Lite**. Use a hobby knife to cut the trace.

[ ![gaming_screen_open_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/901/medium800/gaming_screen_open_pitft.jpg?1430086319) __ ](/assets/24901)

##  Prep Display PCB

With the GPIO header and buttons soldered, go ahead and flip over the display so the two parts are side by side.

  * [ ![gaming_xacto_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/886/medium640/gaming_xacto_pitft.jpg?1430084129) ](/assets/24886)
  * [ ![gaming_xacto_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/886/thumb160/gaming_xacto_pitft.jpg?1430084129) ](/assets/24886)
  * [ ![gaming_peel_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/887/thumb160/gaming_peel_pitft.jpg?1430084179) ](/assets/24887)

## Peel

Use your nail or hobby knife to peel the orange colored sticker backing. Remove and peel both pieces.

[ ![gaming_stick_pitft.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/900/medium800/gaming_stick_pitft.jpg?1430085335) __ ](/assets/24900)

##  Stick Display

Flip over the display and line it up with the screen outline on the PCB. Press down on the screen to make the adhesive stick to the PCB.

You might also want to use some double-sided tape if the side tape pieces are not strong enough

#  Pi Cable

by [ Ruiz Brothers ](/users/pixil3d)

  * [ ![gaming_plug_picable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/905/medium640/gaming_plug_picable.jpg?1430089349) ](/assets/24905)
  * [ ![gaming_plug_picable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/905/thumb160/gaming_plug_picable.jpg?1430089349) ](/assets/24905)
  * [ ![gaming_plugged_picable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/906/thumb160/gaming_plugged_picable.jpg?1430089398) ](/assets/24906)

## Connect Pi Cable

Line up the white wire on the ribbon cable with the white arrow on the PiTFT PCB. Press firmly on the connector to plug it into the pins.

  * [ ![gaming_snip_picable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/907/medium640/gaming_snip_picable.jpg?1430089487) ](/assets/24907)
  * [ ![gaming_snip_picable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/907/thumb160/gaming_snip_picable.jpg?1430089487) ](/assets/24907)
  * [ ![gaming_snipped_picable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/908/thumb160/gaming_snipped_picable.jpg?1430089545) ](/assets/24908)

## Remove Pi Cable Connector

Grab your set of flush cutters and snip off the connector the other end.

  * [ ![gaming_peel_picable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/909/medium640/gaming_peel_picable.jpg?1430089615) ](/assets/24909)
  * [ ![gaming_peel_picable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/909/thumb160/gaming_peel_picable.jpg?1430089615) ](/assets/24909)
  * [ ![gaming_bend_picable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/910/thumb160/gaming_bend_picable.jpg?1430089690) ](/assets/24910)

## Peel Cable

Peel apart each strand of wire from the cable like you would with stringy cheese. Peel it just enough so they're still some ribbon near the fold.

#  Mount Display

by [ Ruiz Brothers ](/users/pixil3d)

  * [ ![gaming_prep_pitft_btns.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/915/medium640/gaming_prep_pitft_btns.jpg?1430143598) ](/assets/24915)
  * [ ![gaming_prep_pitft_btns.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/915/thumb160/gaming_prep_pitft_btns.jpg?1430143598) ](/assets/24915)
  * [ ![gaming_insert_pitft_btns.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/916/thumb160/gaming_insert_pitft_btns.jpg?1430144127) ](/assets/24916)

## Install display buttons

Now is a good time to insert that strip of buttons printed in Ninjaflex. The buttons should fit into the cuts on the enclosure.

  * [ ![gaming_install_pitft_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/917/medium640/gaming_install_pitft_case.jpg?1430144899) ](/assets/24917)
  * [ ![gaming_install_pitft_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/917/thumb160/gaming_install_pitft_case.jpg?1430144899) ](/assets/24917)
  * [ ![gaming_prep_screws_pitft_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/918/thumb160/gaming_prep_screws_pitft_case.jpg?1430144956) ](/assets/24918)

## Install PiTFT

Fit the PiTFT into the enclosure and line up the buttons and mounting holes. Grab four #4-40 3/8 flat phillips machine screws.

  * [ ![gaming_screw_pitft_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/919/medium640/gaming_screw_pitft_case.jpg?1430145040) ](/assets/24919)
  * [ ![gaming_screw_pitft_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/919/thumb160/gaming_screw_pitft_case.jpg?1430145040) ](/assets/24919)
  * [ ![gaming_screwed_pitft_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/920/thumb160/gaming_screwed_pitft_case.jpg?1430145125) ](/assets/24920)

## Mount PiTFT

Hold the PiTFT in place while you insert and secure four machine screws into the PCB. These should fasten all the way through the PCB and the standoffs.

#  Perma-Proto

by [ Ruiz Brothers ](/users/pixil3d)

[ ![gaming_premaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/933/medium800/gaming_premaproto.jpg?1430148783) __ ](/assets/24933)

##  Using Half-size Perma-Proto 

The perma-proto PCB is a lot like a breadboard. The rows are all linked together, while the columns are not. There's two power rails on the top and very bottom that include ground and voltage (indicated by blue and red lines).

The columns are indicated by numbers (1-30) while the rows are indicated by letters (A-J).

The half-size PCB has two separated centers in the center (A-E and F-J). Getting familiar with these labels will help you install the buttons and manage soldering wires.

  * [ ![gaming_permaproto_mark.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/921/medium640/gaming_permaproto_mark.jpg?1430145606) ](/assets/24921)
  * [ ![gaming_permaproto_mark.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/921/thumb160/gaming_permaproto_mark.jpg?1430145606) ](/assets/24921)
  * [ ![gaming_marked_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/923/thumb160/gaming_marked_permaproto.jpg?1430145721) ](/assets/24923)

## Mark Perma-Proto

We need cut the PCB down so it can fit inside the enclosure. Before we do that, let's mark up on the PCB and draw guidelines. 

  * Mark the first row down (including rail)
  * Mark the first column across (including rail)
  * Mark row 26 down (including rail)

##  Cut Perma-Proto

I used a Dremel with a thin cut attachment to saw the excess pieces off the PCB. I recommend taking safety precausions when doing this.

  * Do it in a well ventilated area (outside).
  * Use safety glasses and a breathing mask.
  * Secure the PCB to panavise jr.
  * Always cut away from you.
  * Clean dust from work area.

If you're not satisfied with the sharp edge, use can use a grinding bit to round off the corners.

  * [ ![gaming_prep_btns_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/924/medium640/gaming_prep_btns_permaproto.jpg?1430146865) ](/assets/24924)
  * [ ![gaming_prep_btns_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/924/thumb160/gaming_prep_btns_permaproto.jpg?1430146865) ](/assets/24924)
  * [ ![gaming_install_btns_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/925/thumb160/gaming_install_btns_permaproto.jpg?1430146966) ](/assets/24925)

## Install buttons (Two Action Buttons)

Insert the four 6mm tactile buttons into the perma-proto and form the D-pad. Two 12mm square will be the "A" and "B" buttons. 

[ ![gaming_permaproto-4btn.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/556/medium800/gaming_permaproto-4btn.jpg?1431969914) __ ](/assets/25556)

##  Install buttons (Four action buttons)

If you're making the four-button layout, insert eight 6mm tactile buttons to the perma-proto PCB. Reference the photo above to get the correct spots for each button.

  * [ ![gaming_tin_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/926/medium640/gaming_tin_permaproto.jpg?1430147304) ](/assets/24926)

## Solder buttons to PCB

The buttons should hold in place once inserted into the PCB (if they don't, you can bend the legs to hold them in place). Flip it over so the bottom is face up and secure the PCB to the Panavise jr.

  * [ ![gaming_cut_wires_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/927/medium640/gaming_cut_wires_permaproto.jpg?1430147610) ](/assets/24927)
  * [ ![gaming_cut_wires_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/927/thumb160/gaming_cut_wires_permaproto.jpg?1430147610) ](/assets/24927)
  * [ ![gaming_tin_wires_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/928/thumb160/gaming_tin_wires_permaproto.jpg?1430147718) ](/assets/24928)

## Prep Ground Wires

We need to create short wires to connect the buttons to the ground rail. These wires should be pretty short about 10mm in length. You'll need to create 5 of them. Strip the tips off each wire and tin them.

  * [ ![gaming_tinned_wires_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/931/medium640/gaming_tinned_wires_permaproto.jpg?1430148338) ](/assets/24931)
  * [ ![gaming_tinned_wires_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/931/thumb160/gaming_tinned_wires_permaproto.jpg?1430148338) ](/assets/24931)
  * [ ![gaming_soldering_gnd_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/932/thumb160/gaming_soldering_gnd_permaproto.jpg?1430148440) ](/assets/24932)

## Solder Ground Wires

For each button you'll need to tin the closest pin to the power rail and the ground pin. Since the rows are all linked together, we can just solder the pins that are closed to each other. The only button that doesn't is that up button (which we'll make a longer wire).

  * [ ![gaming_solder_gnd_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/934/medium640/gaming_solder_gnd_permaproto.jpg?1430149215) ](/assets/24934)

## Up Button Ground Wire

The up button for the d-pad is the only button that doesn't use a short wire because its on the top section. We'll need to create a longer wire to connect it to the ground rail. 

[ ![gaming_snip_legs_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/936/medium800/gaming_snip_legs_permaproto.jpg?1430149601) __ ](/assets/24936)

##  Trim legs

Let's go ahead and snip the points legs from the PCB. This will ensure our perma-proto doesn't puncher or scratch any of the other components.

[ ![gaming_install_btns_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/937/medium800/gaming_install_btns_permaproto.jpg?1430149861) __ ](/assets/24937)

##  2-Button Layout

OK now we have the perma-proto trimmed, the buttons solder in place and ground wires, we're ready to wire up the PiCable to the perma-proto PCB. 

This is a good place to take a break. The next section contains lots more stripping, tinning and soldering!

[ ![gaming_pocketpi-perma-proto-completed.jpg](https://cdn-learn.adafruit.com/assets/assets/000/029/776/medium800/gaming_pocketpi-perma-proto-completed.jpg?1453052318) __ ](/assets/29776)

##  4-Button Layout

If you're doing the 4-button version, here's a photo to reference the wired connections. Each button has a wire connected to the ground rail. Note, the PiCable is already wired to the buttons.

#  Buttons

by [ Ruiz Brothers ](/users/pixil3d)

  * [ ![gaming_prep_pwr_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/938/medium640/gaming_prep_pwr_pi_cable.jpg?1430150760) ](/assets/24938)
  * [ ![gaming_prep_pwr_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/938/thumb160/gaming_prep_pwr_pi_cable.jpg?1430150760) ](/assets/24938)
  * [ ![gaming_strip_pwr_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/939/thumb160/gaming_strip_pwr_pi_cable.jpg?1430150917) ](/assets/24939)
  * [ ![gaming_tin_pwr_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/940/thumb160/gaming_tin_pwr_pi_cable.jpg?1430150974) ](/assets/24940)
  * [ ![gaming_solder_pwr_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/941/thumb160/gaming_solder_pwr_pi_cable.jpg?1430151058) ](/assets/24941)

## Connect Pi Cable to Powerboost

Grab the wires from the pi cable and locate wire #2 and #6. Wire #1 is the white colored one. Isolate these two wires and strip the tips off. Secure them to one of the grabbers on the third helping hand Apply some solder to tin them.

Solder wire #2 to the positive pin on the Powerboost. Solder wire #6 to the negative pin on the Powerboost.

[ ![gaming_soldered_pwr_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/942/medium800/gaming_soldered_pwr_pi_cable.jpg?1430151149) __ ](/assets/24942)

##  Soldered Power

Now we should have power wired up from the Pi Cable to the powerboost 1000c. Wire #2 is actually pin 5V on the Pi, wire and #6 is ground.

  * [ ![gaming_cutting_excess_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/943/medium640/gaming_cutting_excess_pi_cable.jpg?1430151504) ](/assets/24943)
  * [ ![gaming_cutting_excess_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/943/thumb160/gaming_cutting_excess_pi_cable.jpg?1430151504) ](/assets/24943)
  * [ ![gaming_cut_excess_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/944/thumb160/gaming_cut_excess_pi_cable.jpg?1430151613) ](/assets/24944)

## Cut extra wires short

Let's go ahead and cut the wires we won't be using short. Be sure to reference the circuit diagram and double, triple check each wires. Trimming these short will helps keep everything tidy and orangized. 

__ If your making the four button version, DO NOT cut wire #3 and #5!! 

  * [ ![gaming_heat_shrink_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/945/medium640/gaming_heat_shrink_pi_cable.jpg?1430160009) ](/assets/24945)

## Heat Shrink Pi Cable

Speaking of being organized and tidy, adding a piece of heat shrinking tubing to the pi cable wires keeps them together. I didn't actually heat it though (depending on the sizing you may want to apply heat to well, shrink it).

  * [ ![gaming_insert_dpad_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/946/medium640/gaming_insert_dpad_case.jpg?1430160105) ](/assets/24946)
  * [ ![gaming_insert_dpad_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/946/thumb160/gaming_insert_dpad_case.jpg?1430160105) ](/assets/24946)
  * [ ![gaming_insert_ab_btns_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/947/thumb160/gaming_insert_ab_btns_permaproto.jpg?1430160152) ](/assets/24947)

## Install Ninjaflex Buttons

Insert the ninjaflex d-pad into the enclosure with the cut out. No special orientation here, its symmetrical so it should just fit. Place the “A” and “B” ninjaflex button set over the two 12mm tactile buttons on the perma-proto. These should have a tight fit.

[ ![gaming_insert_permaproto_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/948/medium800/gaming_insert_permaproto_case.jpg?1430160204) __ ](/assets/24948)

##  Install Perma-Proto

OK, grab the PCB and position it over the enclosure. Notice those clips on the inner walls of the enclosure? Those are going to hold the PCB in place. So position and orient the PCB with the appropriate buttons going into the right spots. The PCB needs to be inserted at an angle so that it can fit into place. Insert the PCB  with the “A” and “B” button side going in first - the PCB should go underneath the clip.

[ ![gaming_installed_permaproto_case.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/949/medium800/gaming_installed_permaproto_case.jpg?1430160260) __ ](/assets/24949)

Ensure the d-pad is still in place while inserting the perma-proto PCB. Carefully angle it into place. You need to fit the ninjaflex AB buttons into the cutouts, then press down the PCB to fit into place. This takes a little force and finesse. The clips are fairly strong, so you don’t need to be super gentle.

  * [ ![gaming_tin_gnd_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/950/medium640/gaming_tin_gnd_permaproto.jpg?1430160358) ](/assets/24950)
  * [ ![gaming_tin_gnd_permaproto.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/950/thumb160/gaming_tin_gnd_permaproto.jpg?1430160358) ](/assets/24950)
  * [ ![gaming_locate_wire_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/951/thumb160/gaming_locate_wire_pi_cable.jpg?1430160434) ](/assets/24951)
  * [ ![gaming_tin_gnd_btn_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/952/thumb160/gaming_tin_gnd_btn_pi_cable.jpg?1430160487) ](/assets/24952)
  * [ ![gaming_solder_gnd_btn_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/953/thumb160/gaming_solder_gnd_btn_pi_cable.jpg?1430160565) ](/assets/24953)

## Wire Ground

Let’s connect the Pi Cable to the ground on the Perma-Proto. We can use a single ground wire from the Pi Cable and solder it to the ground rail on the Perma-Proto PCB. You can count and pull on the wires to determine which one to use. Wire #9 on the Pi Cable is associated with a ground connection.

  * [ ![gaming_cut_left_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/954/medium640/gaming_cut_left_pi_cable.jpg?1430160654) ](/assets/24954)
  * [ ![gaming_cut_left_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/954/thumb160/gaming_cut_left_pi_cable.jpg?1430160654) ](/assets/24954)
  * [ ![gaming_tin_left_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/955/thumb160/gaming_tin_left_pi_cable.jpg?1430161999) ](/assets/24955)
  * [ ![gaming_tin_left_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/956/thumb160/gaming_tin_left_pp.jpg?1430162073) ](/assets/24956)
  * [ ![gaming_solder_left_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/957/thumb160/gaming_solder_left_pp.jpg?1430162250) ](/assets/24957)

## Wire Left Button

Find an available pin on the perma-proto that is linked to the left button. This should be on the opposite pin of the button where we wired ground. Locate wire #7 on the pi cable and position near it the left button. Measure how long it needs to be and cut short - leave a bit of slack so it’s easier to solder. Strip and tin the wire. Then solder the wire to the perma-proto PCB.

  * [ ![gaming_cut_right_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/958/medium640/gaming_cut_right_pi_cable.jpg?1430162395) ](/assets/24958)
  * [ ![gaming_cut_right_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/958/thumb160/gaming_cut_right_pi_cable.jpg?1430162395) ](/assets/24958)
  * [ ![gaming_tin_right_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/959/thumb160/gaming_tin_right_pi_cable.jpg?1430162467) ](/assets/24959)
  * [ ![gaming_solder_right_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/960/thumb160/gaming_solder_right_pp.jpg?1430162556) ](/assets/24960)

## Wire Right Button

Now that you did the first button, you’ll be able to do the song and dance easier. Let’s locate wire #11 on the pi cable - this is going to the right button. Just like we did on the left button, measure how long it needs to be, then cut, strip and tin. Solder this one to the one of the available pins in the same row of the right button.

  * [ ![gaming_tin_up_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/961/medium640/gaming_tin_up_pp.jpg?1430162698) ](/assets/24961)
  * [ ![gaming_tin_up_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/961/thumb160/gaming_tin_up_pp.jpg?1430162698) ](/assets/24961)
  * [ ![gaming_cut_up_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/962/thumb160/gaming_cut_up_pi_cable.jpg?1430162755) ](/assets/24962)
  * [ ![gaming_tin_up_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/963/thumb160/gaming_tin_up_pi_cable.jpg?1430162920) ](/assets/24963)
  * [ ![gaming_solder_up_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/964/thumb160/gaming_solder_up_pp.jpg?1430162977) ](/assets/24964)

## Wire Up Button

Up next, it’s the up button! Locate wire #12 and do the song and dance of measuring, cutting, stripping, tipping and soldering.

  * [ ![gaming_tin_down_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/965/medium640/gaming_tin_down_pp.jpg?1430163168) ](/assets/24965)
  * [ ![gaming_tin_down_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/965/thumb160/gaming_tin_down_pp.jpg?1430163168) ](/assets/24965)
  * [ ![gaming_cut_down_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/966/thumb160/gaming_cut_down_pi_cable.jpg?1430163250) ](/assets/24966)
  * [ ![gaming_tin_down_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/967/thumb160/gaming_tin_down_pi_cable.jpg?1430163534) ](/assets/24967)
  * [ ![gaming_solder_down_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/968/thumb160/gaming_solder_down_pp.jpg?1430163587) ](/assets/24968)

## Wire Down Button

Locate wire #13 and solder this one to the down button. You know the drill!

  * [ ![gaming_tin_a_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/969/medium640/gaming_tin_a_pp.jpg?1430163686) ](/assets/24969)
  * [ ![gaming_tin_a_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/969/thumb160/gaming_tin_a_pp.jpg?1430163686) ](/assets/24969)
  * [ ![gaming_cut_a_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/970/thumb160/gaming_cut_a_pi_cable.jpg?1430163758) ](/assets/24970)
  * [ ![gaming_tin_a_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/971/thumb160/gaming_tin_a_pi_cable.jpg?1430163820) ](/assets/24971)
  * [ ![gaming_solder_a_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/972/thumb160/gaming_solder_a_pp.jpg?1430163871) ](/assets/24972)

## Wire A Button

Get wire #15 and connect this one to the “A” button. Double check to see you’re selecting the correct button - orientation might mess with you a little after soldering all those wires.

  * [ ![gaming_tin_b_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/973/medium640/gaming_tin_b_pp.jpg?1430163935) ](/assets/24973)
  * [ ![gaming_tin_b_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/973/thumb160/gaming_tin_b_pp.jpg?1430163935) ](/assets/24973)
  * [ ![gaming_cut_b_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/974/thumb160/gaming_cut_b_pi_cable.jpg?1430163995) ](/assets/24974)
  * [ ![gaming_tin_b_pi_cable.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/975/thumb160/gaming_tin_b_pi_cable.jpg?1430164057) ](/assets/24975)
  * [ ![gaming_solder_b_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/977/thumb160/gaming_solder_b_pp.jpg?1430164124) ](/assets/24977)

## Wire B button

OK now we should be left with just one wire - Safe to assume its wire #16 which will connect to the “B” button

[ ![gaming_soldered_btns_pp.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/978/medium800/gaming_soldered_btns_pp.jpg?1430164162) __ ](/assets/24978)

##  Wired Perma-Proto to Pi Cable

It’s starting to look finished after soldering all those wires. It’s a good idea to double check all the buttons, pins and wires to ensure everything is correct. If you got any of them mixed, it is possible to remap them in software. But make sure ground is ground and nothing is intersecting (ie, two inputs wired to a single button).

[ ![gaming_permaproto-wiring.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/557/medium800/gaming_permaproto-wiring.jpg?1431970099) __ ](/assets/25557)

##  Perma-Proto (Four button layout)

If your making the four button version, you'll need to connect Wire #3 (GPIO 2) to the button you want to be "**X**". Connect wire #5 (GPIO 3) to the button you'd like to be "**Y**".

That’s all the soldering for this project. Congratulations, you are now a master solderer! Next up, we need to add the battery and close the enclosure. Almost done!

#  Assembly

by [ Ruiz Brothers ](/users/pixil3d)

[ ![gaming_final_wire_check.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/979/medium800/gaming_final_wire_check.jpg?1430164389) __ ](/assets/24979)

##  Final Wire Check

It’s a good idea to check all the wiring before closing it up. It is relatively easy to open and adjust but you should consider reviewing all the connections. If you think you have too much excess wire, now would be a good time to can trim them down.

[ ![gaming_plugged_battery.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/980/medium800/gaming_plugged_battery.jpg?1430164476) __ ](/assets/24980)

##  Plug Battery

Get the 2000mAh battery and insert the cable to the JST port on the powerboost 1000c. You might want to bend it at a right-angle so you can fit it in the case.

[ ![gaming_tack_battery.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/981/medium800/gaming_tack_battery.jpg?1430164508) __ ](/assets/24981)

##  Tack Battery

I added a small piece of fun-tak to the back of the battery so it stick the back of the Perma-Proto PCB. This fun-tak stuff from loctite works really well cause it hold it in place, but easy to remove and doesn’t leave behind any sticky gunk**.**

[ ![gaming_stick_battery.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/982/medium800/gaming_stick_battery.jpg?1430164551) __ ](/assets/24982)

##  Stick Battery

Go ahead and stick the battery onto the Perma-Proto PCB.

[ ![gaming_installed_battery.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/983/medium800/gaming_installed_battery.jpg?1430164633) __ ](/assets/24983)

##  Installed Battery

Seems to be the best place for the battery. I would recommend wrapping this up in gaffers tape but when I did that it no longer fit, so at least you know now. We snipped off all the pointy stuff anyway, so it should be safe. Also note there’s actually not too much force or pressuring being applied to the battery when it’s enclosed.

[ ![gaming_fit_gpio.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/984/medium800/gaming_fit_gpio.jpg?1430164688) __ ](/assets/24984)

##  Close GPIO headers

With two hands, you want to pick up both parts of the enclosure and start closing it together. The first thing you wanna do is line up the header pins from the Pi to the socket on the PiTFT. Once their lined up, squeeze the two parts together to connect it.

  * [ ![gaming_side_check.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/985/medium640/gaming_side_check.jpg?1430164812) ](/assets/24985)
  * [ ![gaming_side_check.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/985/thumb160/gaming_side_check.jpg?1430164812) ](/assets/24985)
  * [ ![gaming_usb_check.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/986/thumb160/gaming_usb_check.jpg?1430164904) ](/assets/24986)
  * [ ![gaming_bottom_check.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/987/thumb160/gaming_bottom_check.jpg?1430164954) ](/assets/24987)

## Wire Kink Check

The top section should be closed now, leaving the bottom and sides a bit open. This is where you need to make sure none of the wires are outside the enclosure - it’s easy to close it up and kink a wire when doing this. You’ll most likely get the two magnets to snap together here since they’re pretty strong.

  * [ ![gaming_insert_last_screw.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/988/medium640/gaming_insert_last_screw.jpg?1430165054) ](/assets/24988)
  * [ ![gaming_insert_last_screw.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/988/thumb160/gaming_insert_last_screw.jpg?1430165054) ](/assets/24988)
  * [ ![gaming_fasten_last_screw.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/989/thumb160/gaming_fasten_last_screw.jpg?1430165120) ](/assets/24989)

## Fasten Last Screw

OK we’re totally almost finished. Grab a single #4-40 ⅜ flat phillips machine screw and insert it into the bottom corner on the back of the enclosure. Hold the two parts together while you fasten the screw all the way through the enclosure. The whole screw will go inside the enclosure and fasten two standoffs together. This single screw keeps the two halves together. The magnet keeps the other corner closed while the top is closed with the aid of the GPIO header. And thats about it!

[ ![gaming_front_done.jpg](https://cdn-learn.adafruit.com/assets/assets/000/024/990/medium800/gaming_front_done.jpg?1430165198) __ ](/assets/24990)

##  Final Build

This build was a lot easier to wire and assemble than the previous PiGRRL projects. Using the perma-proto and tactile buttons in my opinion are more hassle free and ultimately feel better, too. There’s a bit of extra room in the enclosure for other components and buttons, so feel encouraged to customize.

 The audio out of the Pi A+ isn't the best quality so there may be some hissing. You can minimize this by increasing the volume on the Pi as much as possible using **alsamixer** and/or the emulator's sound controls and adjusting the audio amp volume down to a comfy level

[ ![gaming_hero_pigrrrl_bamboo.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/250/medium800/gaming_hero_pigrrrl_bamboo.jpg?1430792035) __ ](/assets/25250)

##  I Made One, YES!

If you made one, we want to see it!! We ask that you please share it with us. Send us a photo on twitter, better yet posit it on Thingiverse - Take photos of your build and post a **make** on the[ thingiverse page](http://www.thingiverse.com/thing:807591). We'll feature your build on our 3D Hangouts show! You can even share it with us on Adafruit Show & Tell show! Post it on any social channel - use hastags #PiGRRL #Adafruit so we can find it easily.

#  RetroPie: Improving Emulator Performance

by [ Phillip Burgess ](/users/pburgess)

On **single-core** Raspberry Pi boards like the **Model A+** and **Pi Zero**, emulation speed is sometimes less than stellar…the screen may update like molasses, or sound may be choppy. Let’s look at some ideas to fight back…

**All of these methods require a USB keyboard attached.**

The directions shown here are for **RetroPie 4.1**, but the same general ideas apply to other versions and possibly even other emulation packages, the steps will just be different.

#  Overclocking

Most Raspberry Pi boards can handle some _overclocking_ — running the processor slightly faster than its “official” speed. Too fast though, and the system can become unstable and crash. Due to manufacturing variances, every single board is slightly different in this regard…you’ll need to do some experimentation to find the fastest _reliable_ setting for your specific board. Restart after making any changes and **try running some games for several minutes** to really put the system through its paces.

  * [ ![gaming_retropie1.png](https://cdn-learn.adafruit.com/assets/assets/000/038/218/medium640/gaming_retropie1.png?1483738524) ](/assets/38218)
  * [ ![gaming_retropie1.png](https://cdn-learn.adafruit.com/assets/assets/000/038/218/thumb160/gaming_retropie1.png?1483738524) ](/assets/38218)
  * [ ![gaming_raspi-config.png](https://cdn-learn.adafruit.com/assets/assets/000/038/222/thumb160/gaming_raspi-config.png?1483739046) ](/assets/38222)
  * [ ![gaming_overclock1.png](https://cdn-learn.adafruit.com/assets/assets/000/038/223/thumb160/gaming_overclock1.png?1483739055) ](/assets/38223)
  * [ ![gaming_overclock2.png](https://cdn-learn.adafruit.com/assets/assets/000/038/224/thumb160/gaming_overclock2.png?1483739066) ](/assets/38224)

You can access the **raspi-config** utility from the RetroPie configuration screen, or press “F4” to exit to a command line and run “sudo raspi-config” manually.

raspi-config is keyboard-based, mostly using the **arrows** and **enter** keys; arcade controls, if connected, probably won’t have the intended effect.

Different Pi models offer different overlock settings. On the Model B+ being tested here, the “Medium” setting seems quite reliable. Other board types may overclock automatically and there’s nothing to adjust here.

If you’re using a **PiTFT display**, the “core” frequency setting should **not exceed 300 MHz**; the display will glitch and may not work at all. So avoid the higher overclock settings if using one of these screens, or manually edit the file /boot/config.txt to fine-tune various system frequencies individually.

#  Choosing an Alternate Emulator

  * [ ![gaming_mash.png](https://cdn-learn.adafruit.com/assets/assets/000/038/225/medium640/gaming_mash.png?1483739334) ](/assets/38225)
  * [ ![gaming_mash.png](https://cdn-learn.adafruit.com/assets/assets/000/038/225/thumb160/gaming_mash.png?1483739334) ](/assets/38225)
  * [ ![gaming_select1.png](https://cdn-learn.adafruit.com/assets/assets/000/038/226/thumb160/gaming_select1.png?1483739357) ](/assets/38226)
  * [ ![gaming_select2.png](https://cdn-learn.adafruit.com/assets/assets/000/038/227/thumb160/gaming_select2.png?1483739363) ](/assets/38227)
  * [ ![gaming_launch.png](https://cdn-learn.adafruit.com/assets/assets/000/038/228/thumb160/gaming_launch.png?1483739377) ](/assets/38228)

When launching a game, there’s a brief moment when it’s possible to access some launch options…

When you see this “launching” screen, press the space bar (or any other key that generates an actual keycode…not a “meta” key like shift or control).

This brings up a menu…similar to raspi-config, it operates with the keyboard, not arcade buttons.

The first option lets you select an alternate emulator program (if available). For example, RetroPie 4.1 includes two different NES emulators: lr-fceumm (the default) and lr-nestopia. Different emulators make tradeoffs with regard to performance and “accuracy” of the emulation. Try an alternative and see how it performs (use the “Launch” option).

The selection you make will “stick” — it is **not necessary to use this menu every time**, unless you want to switch back to the original emulator choice. There’s also an option to use an alternate emulator only for specific ROMs, if you have different needs for different games.

The above steps are fairly quick and easy. If they meet your needs, consider the job done! If it’s still not quite the performance you need, the situation gets more involved…

**These next steps _require_ a network connection.** On a Model A+ or Pi Zero, that usually requires a USB hub and an Ethernet or WiFi adapter, along with some configuration (the RetroPie 4.1 configuration menu includes WiFi setup). Alternately, if you have a spare Model B+ around, that’s easy to get on an Ethernet network…move the SD card over there for setup, then move it back to the target system when done.

#  Installing Additional Emulators

  * [ ![gaming_retropie1.png](https://cdn-learn.adafruit.com/assets/assets/000/038/230/medium640/gaming_retropie1.png?1483739426) ](/assets/38230)
  * [ ![gaming_retropie1.png](https://cdn-learn.adafruit.com/assets/assets/000/038/230/thumb160/gaming_retropie1.png?1483739426) ](/assets/38230)
  * [ ![gaming_retropie2.png](https://cdn-learn.adafruit.com/assets/assets/000/038/232/thumb160/gaming_retropie2.png?1483739441) ](/assets/38232)
  * [ ![gaming_manage.png](https://cdn-learn.adafruit.com/assets/assets/000/038/290/thumb160/gaming_manage.png?1483746396) ](/assets/38290)
  * [ ![gaming_optional.png](https://cdn-learn.adafruit.com/assets/assets/000/038/291/thumb160/gaming_optional.png?1483746412) ](/assets/38291)
  * [ ![gaming_quicknes.png](https://cdn-learn.adafruit.com/assets/assets/000/038/292/thumb160/gaming_quicknes.png?1483746423) ](/assets/38292)
  * [ ![gaming_binary.png](https://cdn-learn.adafruit.com/assets/assets/000/038/293/thumb160/gaming_binary.png?1483746430) ](/assets/38293)

Some “bleeding edge” emulators might offer better performance than the stock options provided by RetroPie. As with the “Alternate Emulators” above, it sometimes comes with a tradeoff in accuracy (hence their non-inclusion), so you’ll need to experiment and decide if it’s worth it.

From the RetroPie configuration screen, select “RetroPie Setup,” which switches to another of these keyboard-based menus.

Select “Manage packages,” then either “Manage optional packages” or “Manage experimental packages.” You’ll get a list of various emulators and/or games that aren’t normally installed by default. _lr-quicknes_ was an optional package for NES emulation…it’s faster than the others…_too_ fast, in fact, so I ended up not using it…but that’s all part of the experimentation process.

Choose the “**Install from binary**” option to install the selected package. Don’t bother with the “source” option…it’s _very_ time consuming and usually provides no benefit.

#  Updating Emulators to Latest Versions

Sometimes you just need the newest-and-shiniest version of an installed emulator to provide the best available performance…

  * [ ![gaming_retropie1.png](https://cdn-learn.adafruit.com/assets/assets/000/038/238/medium640/gaming_retropie1.png?1483739487) ](/assets/38238)
  * [ ![gaming_retropie1.png](https://cdn-learn.adafruit.com/assets/assets/000/038/238/thumb160/gaming_retropie1.png?1483739487) ](/assets/38238)
  * [ ![gaming_retropie2.png](https://cdn-learn.adafruit.com/assets/assets/000/038/239/thumb160/gaming_retropie2.png?1483739502) ](/assets/38239)
  * [ ![gaming_updateall.png](https://cdn-learn.adafruit.com/assets/assets/000/038/240/thumb160/gaming_updateall.png?1483739522) ](/assets/38240)

From the RetroPie configuration screen, select “RetroPie Setup.” This brings up the keyboard-driven menu again. Choose the “Update all installed packages” option to make a sweep through the system that’ll update _everything_ to the latest release, including the kernel.

**This system-wide update can be extremely time-consuming…possibly an hour or so, depending on processor and network speeds.**

Even the default lr-fceumm on a non-overclocked Pi ran great after updating!

**If using a PiTFT display, think twice before trying this option.** Perhaps make a **backup** of your SD card first. Kernel updates have been known to break PiTFT support in some circumstances, and you’d have to start all over.

[ Your browser does not support the video tag.  ](https://www.adafruit.com/product/2510)

Pocket PiGRRL Pack Build your own Pi Game Emulator!

