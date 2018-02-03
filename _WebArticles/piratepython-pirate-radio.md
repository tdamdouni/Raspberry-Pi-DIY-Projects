# PiratePython - Pirate Radio

_Captured: 2018-02-01 at 16:10 from [forums.pimoroni.com](https://forums.pimoroni.com/t/piratepython-pirate-radio/7058)_

This is a little unzip-to-your-SD-card software image for Pirate Radio, designed to make it simple and easy to get your new radio kit set up. If you don't want to make customisations to your radio, and you don't want to spend hours setting up Raspbian and our software from scratch, then this is the OS for you!

This is still very much a beta release, but it's coming along nicely! Features include:

  * VU and button support for the pHAT BEAT included in the Pirate Radio kit
  * Ability to play internet radio stations, and also MP3 files stored on the SD card
  * An HTTP interface to control your radio- <http://pirateradio.local:8080> (password: `p1rat3`)
  * Stateless RAM disk image, so it should _never_ corrupt when powered off
  * Slightly better VU meter response/scaling (more improvements to come)

To get started, grab the zip file from below and extract it onto a blank SD card. Some users have reported problems with larger cards, so ideally try 8GB or 16GB, but this OS will also fit on a 2GB or 1GB card!

http://get.pimoroni.com/pirateradio-v20180201.zip
