# Raspberry Pi 2 B / 3 B + Raspian + Kodi Media Center

_Captured: 2017-05-19 at 11:29 from [www.opendisplaycase.de](https://www.opendisplaycase.de/tutorials/raspberry-pi-2-raspian-kodi-media-center.html)_

![RPi Raspian Kodi](https://www.opendisplaycase.de/fileadmin/images/opendisplaycase/logos/rpi_debian_kodi.png)

> _RPi Raspian Kodi_

Anfang 2014 hatte ich einige Artikel zum Thema Kodi (XBMC) auf dem Raspberry Pi gelesen. Beim ausprobieren der Distribution XBian, OpenELEC etc. konnten diese mich nicht uberzeugen - zu viele Fehler z.B. Booted nicht, kein CEC und andere Einschrankungen. Zeitgleich bin ich auf die Webseite XBMC fur Raspberry Pi von Michael Gorven gestoßen. Er bietet fertige Debian-Pakete von Kodi fur Raspbian Wheezy & Jessie an. Die XBMC Frodo Version zu dieser Zeit liefen auf dem [Raspberry Pi B](https://www.amazon.de/gp/product/B00T2U7R7I?tag=odc-tutorials-21) sehr stabil und ohne Probleme. Mittlerweile gibt es auch uber die Offiziellen Raspbian Jessie Repository Kodi in der aktuellen Version.

Die Installation lasst sich in wenigen Schritten bewerkstelligen:

### Installation: Kodi - Raspbian Jessie Repository

#### 1\. Setup fur Raspbian Jessie & Jessie (Lite)

    
    
    pi@raspberrypi ~ $ sudo apt-get update
    pi@raspberrypi ~ $ sudo apt-cache madison kodi
          kodi | 2:17.1-1~jessie | http://archive.raspberrypi.org/debian/ jessie/main armhf Packages

#### 2\. Installiere Kodi

    
    
    pi@raspberrypi ~ $ sudo apt-get install kodi

#### 3\. Gruppen-Einstellung für den Benutzer kodi & pi überprüfen

    
    
    pi@raspberrypi ~ $ sudo usermod -a -G audio,video,input,dialout,plugdev,tty pi
    
    

#### 4\. Einstellung udev-Regeln

    
    
    pi@raspberrypi ~ $ sudo nano /etc/udev/rules.d/99-input.rules
    
    SUBSYSTEM=="input", GROUP="input", MODE="0660"
    KERNEL=="tty[0-9]*", GROUP="tty", MODE="0660"

#### 5\. Einstellungen: GPU Ram

  * Advanced Options ->Memory Split -> 256

    
    
    pi@raspberrypi ~ $ sudo raspi-config
    pi@raspberrypi ~ $ sudo reboot

#### 6\. Starte

    
    
    pi@raspberrypi ~ $ kodi
