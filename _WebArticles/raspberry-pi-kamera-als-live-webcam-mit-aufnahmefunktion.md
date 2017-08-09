# Raspberry Pi Kamera als Live-Webcam mit Aufnahmefunktion

_Captured: 2017-05-19 at 11:39 from [www.sweetpi.de](https://www.sweetpi.de/blog/783/raspberry-pi-kamera-als-live-webcam-mit-aufnahmefunktion)_

Nach den [ersten Tests mit der Raspberry Pi Kamera](https://www.sweetpi.de/blog/765/testen-der-raspberry-pi-kamera) und der Suche nach eine Losung zum Live-Streamen des Kamerabildes in den Browser bin ich auf das [RPi Cam Web Interface](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=43&t=63276) Projekt gestoßen. Damit lasst sich die Raspberry Pi Kamera bequem uber den Browser bedienen und das aktuelle Bild fast ohne Verzogerung in den Browser streamen.

## Die Features:

  * Live-Bild der Kamera
  * Video und Bild Aufnahmefunktion
  * direkter Download der Aufnahmen
  * Bewegungesdetektion
![Das  RPi Cam Web Interface](https://www.sweetpi.de/blog/wp-content/uploads/2014/03/rpi-cam-control.png)

> _Das RPi Cam Web Interface_

## Installation

Ihr musste die [Raspberry Pi Kamera](http://www.amazon.de/gp/product/B00E1GGE40/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00E1GGE40&linkCode=as2&tag=sweetpi-21) angeschlossen und [wie bereits erklart](https://www.sweetpi.de/blog/765/testen-der-raspberry-pi-kamera) aktiviert haben. Dann aktualisiert Ihr die Paketquellen und installierte Packete:

und lades das Installationscript herunter und fuhrt es aus:

1  
2  
3  
4  

git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git  
cd RPi_Cam_Web_Interface  
chmod u+x RPi_Cam_Web_Interface_Installer.sh  
./RPi_Cam_Web_Interface_Installer.sh install

## Autostart

Danach musst Ihr euch nur noch entscheiden wie und ob das ganze beim Starten des Raspberry Pi gestartet werden soll:

**Option 1: Das Interface startet und ubernimmt die Kontrolle uber die Kamera.**

**Option 2: Das Interface startet nicht mit dem Raspberry Pi. Ihr musst es manuell starten.**

Danach muss der Raspberry Pi neu gestartet werden und ihr erreicht das Webinterface uber dessen IP-Adresse. Wer noch, wie ich, den Port andern will kann dies in der Datei `/etc/apache2/ports.conf` tun:

und die beiden Zeilen:

entsprechend anpassen, sowie in der Datei `/etc/apache2/sites-enabled/000-default` den Port auch andern.

## Weitere Infos:
