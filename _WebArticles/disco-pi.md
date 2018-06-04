# Disco-pi

_Captured: 2018-02-23 at 16:59 from [www.instructables.com](http://www.instructables.com/id/Disco-pi/)_

## Introduction: Disco-pi

![Picture of Disco-pi](https://cdn.instructables.com/FBJ/RIVV/JACTTQYL/FBJRIVVJACTTQYL.LARGE.jpg)[ ](https://cdn.instructables.com/FBJ/RIVV/JACTTQYL/FBJRIVVJACTTQYL.LARGE.jpg)

This instructable shows how to use a [Raspberry Pi](https://www.raspberrypi.org) to control a coloured LED strip, based on music played from a web browser.

It shows how to create a basic website using [Node.js](https://nodejs.org) over HTTPS and use [socket.io](https://socket.io) over WSS (Secure Websocket).

The website has a single page which has a very basic layout. The webpage populates a drop down list with music files, which are located in the public/audio folder on the server. Selecting an option in the list plays the music file in the webpage using the [HTML 5 audio element](https://www.w3schools.com/html/html5_audio.asp). While playing the music file, the webpage uses the [AudioContext](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext) interface to analyse the music, which is then sent to the server over a secure websocket connection.

The server running on a Raspberry Pi uses the [Node RPI WS281x Native](https://github.com/beyondscreen/node-rpi-ws281x-native) library (wrapping Jeremy Garff's [WS281X](https://github.com/jgarff/rpi_ws281x) library) to change the colours of the LEDs on a WS2811 LED strip, based on the data sent through the websocket.

The example code can be found here: [disco-pi](https://github.com/haydockjp/disco-pi)

## Step 1: Equipment

  1. **Raspberry Pi **\- I used a Raspberry Pi 2B that I had laying around, but you can get a [Raspberry Pi 3 Starter Kit](https://goo.gl/UAQ92Z) for around **CAD 100**
  2. **WS2811 LED Strip** \- I was playing with [ALITOVE 16.4ft 150 Pixels WS2811](https://goo.gl/BhWDX9). This comes with a controller and a power supply for about **CAD 45-50**
  3. **Barrel Jack Connector** \- I bought one from my local electronics shop, something like [this](https://goo.gl/Z8diR1). Just make sure if fits your power supply 
  4. **Jumper Connectors / Wire** \- I had some [Female to Male connector cables](https://goo.gl/dfE7mx) and some [22 Gauge Solid hook up wire lying](https://goo.gl/8khnTF) around

## Step 2: Setting Up the Raspberry Pi

### Operating System

I normally use the latest [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) build. Download the image and write it to the SD Card. If you are using a Windows computer, you can use [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/) to write the image to the SD Card.

### Node.js

Install the latest version of Node.js. At the time of writing I am using 8.9.1
    
    
    curl -sL <a href="https://deb.nodesource.com/setup_8.x" rel="nofollow"> https://deb.nodesource.com/setup_8.x </a> | sudo -E bash -
    sudo apt-get install nodejs

### Install git
    
    
    sudo apt-get install git

![Picture of Connecting the Hardware](https://cdn.instructables.com/FZA/US11/JACTTQXG/FZAUS11JACTTQXG.LARGE.jpg)[ ](https://cdn.instructables.com/FZA/US11/JACTTQXG/FZAUS11JACTTQXG.LARGE.jpg)![Picture of Connecting the Hardware](https://cdn.instructables.com/FNA/DW3D/JACTTQXH/FNADW3DJACTTQXH.MEDIUM.jpg)[ ](https://cdn.instructables.com/FNA/DW3D/JACTTQXH/FNADW3DJACTTQXH.LARGE.jpg)![Picture of Connecting the Hardware](https://cdn.instructables.com/FR7/F585/JACTTQXE/FR7F585JACTTQXE.MEDIUM.jpg)[ ](https://cdn.instructables.com/FR7/F585/JACTTQXE/FR7F585JACTTQXE.LARGE.jpg)Show All 7 Items

![Picture of Website Code](https://cdn.instructables.com/FMP/CMDX/JACTU2AA/FMPCMDXJACTU2AA.LARGE.jpg)[ ](https://cdn.instructables.com/FMP/CMDX/JACTU2AA/FMPCMDXJACTU2AA.LARGE.jpg)
