# Pi MusicBox

_Captured: 2017-08-24 at 23:57 from [www.pimusicbox.com](http://www.pimusicbox.com/)_

### Make your Raspberry Pi stream!

Welcome to the Swiss Army Knife of streaming music using the Raspberry Pi. With Pi MusicBox, you can create a cheap (Sonos-like) standalone streaming music player for Spotify, Google Music, SoundCloud, Webradio, Podcasts and other music from the cloud. Or from your own collection from a device in your network. It won't drain the battery of your phone when playing. The music won't stop if you play a game on your phone.

Connect a 25$ Raspberry Pi to your (DIY) audio system, easily configure MusicBox and go! Control the music from your couch using a phone, tablet, laptop or PC, no tinkering required. AirPlay and DLNA streaming also included!

##  Features

  * Headless audio player based on [Mopidy](http://www.mopidy.com) (no need for a monitor), streaming music from Spotify, SoundCloud, Google Music, Podcasts (with iTunes, gPodder directories), local and networked music files (MP3/OGG/FLAC/AAC), Webradio (with TuneIn, Dirble, AudioAddict, Soma FM directories), Subsonic. 
  * Remote control it using a nice webinterface or using an MPD-client (like MPDroid for Android). 
  * Also includes Spotify Connect, AirTunes/AirPlay and DLNA/OpenHome streaming from your phone, tablet (iOS and Android) or PC using software like BubbleUPnP. 
  * USB Audio support, for all kinds of USB soundcards, speakers, headphones. The sound from the Pi itself is not that good... 
  * Wifi support (WPA, for Raspbian supported wifi-adapters) 
  * No need for tinkering, no need to use the Linux commandline 
  * Play music files from the SD Card, USB, Network. 
  * Last.FM scrobbling. 
  * Several Pi soundcards supported ([HifiBerry](http://www.hifiberry.com), [JustBoom](https://www.justboom.co/), [IQ Audio](http://www.iqaudio.com)) 

##  Screenshots

##  Requirements 

  * Working Raspberry Pi (all models) 
  * Speakers, amplifier or headphones (analog or USB) 
  * SD-Card, 1GB minimum, 2GB+ prefered 
  * Computer with a modern browser; tablet or phone. The webinterface is tested with recent versions of Firefox, Chrome, Internet Explorer and iOS (iPad/iPhone), modern versions of Android (Chrome Mobile, Firefox Mobile). Internet Explorer version 10 works, earlier versions don't. You can also use an [MPD client](http://mpd.wikia.com/wiki/Clients) to connect. 
  * Spotify **Premium**, Google Music (All Access) or SoundCloud account for streaming. 

##  DIY Projects using Pi MusicBox

Pi MusicBox is proud to provide the software for an increasing number of Do It Yourself audioboxes, like these:

## Download

Here you can find an SD card image to use on your Pi. It's around 300MB to download and will fit on a 1GB or larger SD card ([changes](https://github.com/pimusicbox/pimusicbox/blob/master/docs/changes.rst)):

This can take a while, so in the meantime, please spread the word!

## Howto's

Alongside the install steps below, you'll also find more detailed instructions in the [latest manual](https://github.com/pimusicbox/pimusicbox/releases/download/v0.7.0RC5/PiMusicBox.pdf). Additionally, some helpful Pi Musicbox users have submitted their own instructions and guides.

  * [Scavix has a complete howto in English!](http://www.codeproject.com/Articles/838501/Raspberry-Pi-as-low-cost-audio-streaming-box)
  * [This one is in German](http://linuxundich.de/raspberry-pi/raspberry-pi-als-jukebox-fuer-google-music-spotify-oder-musik-vom-nas/)
  * [Or you can create a Boombox](http://www.instructables.com/id/Spotify-Airplay-Boombox-from-a-HK-GoPlay-II/?ALLSTEPS)

## Instructions

Extract the zip-file. Put the resulting image on your sd-card by using the wonderfully simple [Etcher SD card image utility](https://etcher.io/) or by following [ these instructions](http://elinux.org/RPi_Easy_SD_Card_Setup#Flashing_the_SD_Card_using_Windows). The image will fit on a 1GB card, but you should use a larger one if you can as this will leave more space for your music files. The latest manual is included in the download archive.

#### Configuration

  1. You can edit all settings in the new settings page from the webclient. To access it, you need a network connection. To enable Wifi, you can either first connect the Pi using a cable and use the settings page, or fill in the wifi-settings in the ini file on the SD Card. For that: 
  2. Put the SD-card into your computer. Open the contents of the 'config' folder of SD-Card in your Finder/Explorer. 
  3. Add your Wifi network and password to the file (and edit other settings if you want) ` settings.ini ` It has instructions on what to put where. 
  4. MusicBox will autodetect usb audiocards/speakers/boxes and hdmi. It's possible to override this in the settings. For example if you want to use analog out while having hdmi connected. 

Detailed instructions can be found in the [manual](https://github.com/pimusicbox/pimusicbox/releases/download/v0.7.0RC5/PiMusicBox.pdf).

#### Start me up!

  1. Put the card in the Pi 
  2. Connect cables (You don't have to connect a monitor to the Pi if you don't want to) 
  3. To use Wifi and USB-Audio you have to plugin the devices before you start the Pi. Restart if you plug them in later. 
  4. Power on your Pi 
  5. Wait for a while... So in the meantime, follow us!  
  
[Follow @pimusicbox on Twitter](https://twitter.com/pimusicbox)  
  


#### Accessing the music

  1. Point your browser to the Pi. Depending on your network and computers, it will be available at this address: ` [http://musicbox.local](http://musicbox.local/) `
  2. Most OS X/iOS and Windows devices probably will find it immediately. If it doesn't work, you could try to install Apple Bonjour/iTunes in Windows to make it work. Linux should also work if Avahi or Samba/Winbind is installed. 
  3. Using Android, you have to point your browser to the MusicBox using the IP-address of your Pi, e.g. ` http://192.168.1.5/ ` (fill in your own!). There is no way to change that for now, unless Android would support it, The IP-address is printed on the screen when MusicBox is started. Connect a monitor/tv to find out. Or use a network/bonjour scanning utility such as [Zentri Discovery](https://play.google.com/store/apps/details?id=discovery.ack.me.ackme_discovery&hl=en_GB). 

## Support & Contact

Please refer to the [Frequently Asked Questions](https://github.com/pimusicbox/pimusicbox/blob/master/docs/faq.rst) and [manual](https://github.com/pimusicbox/pimusicbox/releases/download/v0.7.0RC5/PiMusicBox.pdf) before asking questions.

You can discuss features and problems on the [forum](https://discuss.mopidy.com/c/pi-musicbox). Please report bugs about MusicBox itself at [the repo at Github](https://github.com/pimusicbox/pimusicbox/issues). You can also try the ` #mopidy ` channel on [Freenode](http://webchat.freenode.net/), or the [Raspberry Pi forums](http://www.raspberrypi.org/phpBB3/) for more general Pi issues.

## What's new?

Take a look at the [latest changes](https://github.com/pimusicbox/pimusicbox/blob/master/docs/changes.rst).

## Security

This is system not totally secured. Don't run it outside a firewall!

  * The Mopidy musicserver is not completely protected   

  * Also, the passwords of Spotify and wifi are stored in plain text on the SD-Card. 
  * It's easy to login to the server with the **root** login and the password **musicbox** (remote login is not enabled by default though). 

## Thanks

Pi MusicBox is based on the following great projects:

  * [Raspbian](http://www.raspbian.org) (based on [Debian](http://www.debian.org) (based on [Linux](http://www.linux.org))) 
  * [Mopidy](http://www.mopidy.com/) (+ my own [Mopidy-MusicBox-Webclient](https://github.com/pimusicbox/mopidy-musicbox-webclient)) 
  * [Shairport Sync](https://github.com/mikebrady/shairport-sync)   

  * [upmpdcli (UPnP Audio Media Renderer)](https://www.lesbonscomptes.com/upmpdcli/)   

  * All the projects that are used to create the these projects 
  * All the projects that are used to create the projects that are used to create these projects   

  * All the projects that ... 
  * A lot of people giving solutions on forums...   

  * And of course the work of the guys 'n girls who brought you the [Raspberry Pi ](http://www.raspberrypi.org)   

