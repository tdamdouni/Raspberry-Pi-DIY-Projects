# Raspberry Pi Grundeinrichtung ohne Tastatur und Monitor 

_Captured: 2015-12-20 at 14:16 from [www.sweetpi.de](https://www.sweetpi.de/blog/1/raspberry-pi-grundeinrichtung)_

Da der Raspberry Pi bei mir als reines Netzwerkgerat genutzt werden soll habe ich mich entschlossen die Grundeinrichtung auch gleich ohne Monitor durchzufuhren.

## Was wird benotigt?

  * Raspberry Pi
  * SD-Speicherkarte (mindestens 2GB)
  * USB-Stromversorgung (hier mein Netzwerkrouter mit USB-Anschluss)
  * Router
  * Linux-Rechner

## 1\. Download und Vorbereitung von Raspbian „wheezy"

Ich verwende das empfohlene Raspbian „wheezy" als Distribution fur meinen Pi. Der Download findet sich auf der [offiziellen Seite der Raspberry Pi Foundation](http://www.raspberrypi.org/downloads). Nach dem Download muss das Image von einem auf die SD-Karte kopiert werden. Das geht unter Linux mit dem Kommandozeilenwerkzeug [dd](http://en.wikipedia.org/wiki/Dd_%28Unix%29) oder auch unter [Windows uber andere Programme](http://elinux.org/RPi_Easy_SD_Card_Setup#Easy_way).

Zuerst mussen wir herausfinden, unter welchem Namen die SD-Karte ansprechbar ist. Dazu kann die Karte einfach eingesteckt werden und mit Hilfe von df alle eingeahngten Datentrager ausgegeben werden. (Dies geht naturlich nur wenn die SD-Karte automatisch eingehangt wird).

user@desktop:~/pi$ df -h  
Filesystem Size Used Avail Use% Mounted on  
/dev/sda1 165G 148G 8,9G 95% /  
udev 1,8G 4,0K 1,8G 1% /dev  
tmpfs 726M 996K 725M 1% /run  
none 5,0M 0 5,0M 0% /run/lock  
none 1,8G 452K 1,8G 1% /run/shm  
/dev/mmcblk0p1 56M 19M 38M 34% /media/3312-932F

Die erste Partition der SD-Karte ist also `/dev/mmcblk0p1` und damit ist die Karte `/dev/mmcblk0`.

Die SHA-1 Checksumme uberprufen und entpacken:

user@desktop:~/pi$ sha1sum 2013-02-09-wheezy-raspbian.zip  
b4375dc9d140e6e48e0406f96dead3601fac6c81 2013-02-09-wheezy-raspbian.zip  
user@desktop:~/pi$ unzip ./2013-02-09-wheezy-raspbian.zip  
Archive: ./2013-02-09-wheezy-raspbian.zip  
inflating: 2013-02-09-wheezy-raspbian.img

Partition mittels umount aushangen und raspbian mit dd ubertragen:

user@desktop:~/pi$ umount /dev/mmcblk0p1  
user@desktop:~/pi$ sudo dd bs=4M if=./2013-02-09-wheezy-raspbian.img of=/dev/mmcblk0  
462+1 records in  
462+1 records out  
1939865600 bytes (1,9 GB) copied, 392,513 s, 4,9 MB/s

Da dd von sich aus keinen Fortschritt zuruck meldet, kann dieser folgendermaßen abgefragt werden:

Wenn dd fertig ist konnen wir nun unserem Pi eine feste Netzwerkadresse zuweisen. Dazu die SD-Karte kurz entfernen und wieder einlegen. Nun sollten 2 Partitionen automatisch eingehangt werden. Nun die Datei `/etc/network/interfaces` mit root-Rechten bearbeiten:

und die Zeile: `iface eth0 inet dhcp` durch folgendes ersetzten und gegebenenfalls die IP-Adressen anpassen:

Das der SSH-Server schon installiert ist und auch standardmaßig gestartet wird kann alles weitere dann direkt uber SSH konfiguriert werden. Nun die SD-Karte auswerfen, entfernen und in den Pi Einlegen. Dann Netzwerkkabel und die USB-Stromverbindung anschließen.

![Raspberry Pi mit Speicherkarte, Netzwerkkabel und Stromversorgung durch den USB-Port. ](https://www.sweetpi.de/blog/wp-content/uploads/2013/02/pi-connected-1024x768.jpg)

> _Raspberry Pi mit Speicherkarte, Netzwerkkabel und Stromversorgung durch den USB-Port._

## 2\. Einrichtung von Raspbian „wheezy"

Nun konnen wir nachdem der Raspberry Pi gestartet ist (ein bisschen Geduld) uns per ssh einloggen. Das Standard Passwort ist der Download-Seite zu entnehmen.

Die Konfiguration wird nun uber raspi-config gestartet.

![raspi-config](https://www.sweetpi.de/blog/wp-content/uploads/2013/02/raspi-config-300x205.png)

> _Konfigurationstool raspi-config fur die Grundeinrichtung von Raspbian „wheezy"_

Hier sollte man zuerst uber „change_local" seine Spracheinstellungen auf `de_DE.UTF-8 UTF-8` setzten. Dann uber „change_timezone" die Zeitzone einstellen. Ganz wichtig ist es nun das Standardpasswort uber „change_pass" in ein eigenes andern. Zu guter Letzt sollte noch uber „expand_rootfs" die Partition auf die volle SD-Kartengroße ausgeweitet werden.

Nach dem Beenden des Tools und einem Neustart konnen wir die Distribution noch auf den aktuellen Stand bringen. Nicht vergessen zuerst wieder per ssh zu verbinden und dann die Paketquellen aktuallisieren:

Sowie die Pakete updaten:

Nach etwas Geduld ist die Grundeinrichtung des Raspberry Pi als Server beendet.
