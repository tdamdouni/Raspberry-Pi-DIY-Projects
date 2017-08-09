# Eigenbau einer IP-Webcam

_Captured: 2017-05-19 at 11:41 from [robotrack.org](http://robotrack.org/include.php?path=article&contentid=309)_

## Projekt: Eigenbau IP-Webcam 

**### 6 Monate Online-dauertest (24h) erfolgreich bestanden..! ###** im September 2013

Mit der USB-Webcam **Logitech c310 HD** (720p, 1280 × 720 Pixel), und als Steuerplatine, einen (Raspberry PI)  
Es sollte naturlich auch mit anderen USB-Webcams funktionieren.

**Benotigte Anschlusse am Raspberry PI:**  
1.) Wireless USB-Adapter oder LAN-Kabel  
2.) USB-Webcam  
3.) 5V Netzteil

Mit hilfe von** mjpg-Streamer ** war es dann auch erfolgreich unter Linux moglich ein Video der Webcam in einem Browser via Stream, java und javascript in voller Auflosung **(1280px × 720px)** mit dem Raspberry anzuzeigen.

**Installation von MJPG-Streamer mit den folgenden Terminal eingaben**

**Es wird vorausgesetzt das die Aktuelle "wheezy-raspbian" image Version bereits auf der SD-Karte installiert wurde.**

pi@raspberrypi ~ $ **sudo apt-get update**  
pi@raspberrypi ~ $ **sudo apt-get install subversion-tools libjpeg8-dev imagemagick**  
pi@raspberrypi ~ $ **svn co https://mjpg-streamer.svn.sourceforge.net/svnroot/mjpg-streamer mjpg-streamer**  
pi@raspberrypi ~ $ **cd mjpg-streamer/mjpg-streamer**  
pi@raspberrypi ~/mjpg-streamer/mjpg-streamer $ **make**  
pi@raspberrypi ~/mjpg-streamer/mjpg-streamer $ **sudo make install**

**Nach der Installation von "mjpg streamer" mit den folgenden Terminal eingaben starten.**  
pi@raspberrypi ~/mjpg-streamer/mjpg-streamer $ **./mjpg_streamer -i "./input_uvc.so -n -y -f 15 -r 1280x720" -o "./output_http.so -n -w ./www -p 8040"**  
(Ich habe fur meine Cam den Port 8040 im Router zugeordnet.)

![Raspberry Pi](http://robotrack.org/raspi/01_raspi_logi_k.JPG)

![Raspberry Pi](http://robotrack.org/raspi/02_raspi_logi_k.JPG)

![Raspberry Pi](http://robotrack.org/raspi/03_raspi_logi_k.JPG)

> _Display the stream mit Logitech c310 HD am Raspberry PI_

![Von 9:00 bis 11:00h online..!  Raspberry PI](http://robotrack.selfhost.bz:8040/?action=stream)

> _Die USB-Webcam Logitech c310 HD lauft hier mit der max. Auflosung von 720p, 1280px × 720px, (Skaliert auf 640px × 480px)_

Das Cambild ist zur Zeit unscharf, da der Autofokus sich auf Hindernisse im Vordergrund scharf stellt..!

![Webcam am Raspberry Pi](http://robotrack.org/raspi/rascam.JPG)

> _Info Seite Mjpg-Streamer_

**<http://robotrack.selfhost.bz:8040/index.html>**

**Eine statische Momentaufnahme 1280px × 720px**  
**[http://robotrack.selfhost.bz:8040/static_simple.html**](robotrack.selfhost.bz:8040/static_simple.html)

**Anzeige des Stream maximale Große 1280px × 720px**  
**<http://robotrack.selfhost.bz:8040/stream_simple.html>**

**Anzeige des Stream 1280px × 720px**  
**<http://robotrack.selfhost.bz:8040/?action=stream>**

**Anzeige des Stream mit java**  
**<http://robotrack.selfhost.bz:8040/java_simple.html>**

**Anzeige des Stream mit javascript 1280px × 720px**  
**<http://robotrack.selfhost.bz:8040/javascript_simple.html>**

**Anzeige des Stream mit Control**  
**[http://robotrack.selfhost.bz:8040/java_control.html**](robotrack.selfhost.bz:8040/java_control.html)

![Attrappe für Raspberry Pi](http://robotrack.org/raspi/CPU_01.JPG)

Die **CPU Auslastung** beim Raspberry PI mit dem **mjpg-Streamer** liegt **max. bei 30%**

![Attrappe für Raspberry Pi](http://robotrack.org/raspi/01_Attrappe.JPG)

> _[Kamera Dummy Attrappe: mehr...>>>](http://www.ebay.de/itm/250775313957?ssPageName=STRK:MEWAX:IT&_trksid=p3984.m1423.l2648)_

Ein Kamera Dummy ist eventuell als Gehause brauchbar.

**[LogiLink WL0145 USB Wlan Adapter: mehr...>>>**](http://www.ebay.de/itm/130887908426?ssPageName=STRK:MEWNX:IT&_trksid=p3984.m1497.l2648)

###/

**Zugriff vom PC auf dem Raspberry via VNC Server**

**[VNC-Serverinstallation und Konfiguration auf dem Pi:**](http://strobelstefan.org/?p=2731)

![Raspberry Pi auf Windows PC](http://robotrack.org/raspi/raspi_v2.JPG)

> _sudo aptitude install tightvncserver_

Nach der Installtion startet den Server mit  
tightvncserver

Remote auf den Pi via VNC zugreifen:   
vncserver :1 -geometry 1024x728 -depth 24

**Installation von VNC**  
http://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc

**[Wer sich Austauschen mochte oder Verbesserungsvorschlage hat, kann es hier im Forum machen: mehr...>>>**](http://robotrack.org/include.php?path=forumscategory&catid=34)

###/ Vom PC  
PuTTY Loggin pi, PW 0815 f2  
Das herunterfahren vom Raspberry Pi   
sudo shutdown -h now

Neustart Videostream der Webcam.  
pi@raspberrypi ~ $ **sudo shutdown -r now**  
###/

**Weitere Infos:** http://www.gtkdb.de/index_36_2098.html

![Mobil](http://robotrack.org/raspi/RWUA.JPG)

Mobil via UMTS-Surf-Stick auch Unterwegs eine USB-Webcam live ins Internet stellen.

![Mobil](http://robotrack.org/raspi/1und1_1.JPG)

![Mobil](http://robotrack.org/raspi/1und1_2.JPG)

> _Diese Seite wurde zuletzt bearbeitet am: 19. Marz 2017_

Copyright 2013/17
