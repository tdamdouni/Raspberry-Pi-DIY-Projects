# Kodi auf dem Raspberry Pi installieren

_Captured: 2017-05-19 at 11:26 from [klein-gedruckt.de](https://klein-gedruckt.de/2016/12/kodi-auf-dem-raspberry/)_

Gerade die neueren Versionen des Raspberry Pi eignen sich hervorragend um damit ein Home-Entertainment-System zu realisieren. Die Software der Wahl ist dabei [Kodi](https://kodi.tv/) (vorher XBMC) dass sich uber die Jahre bereits etabliert hat. Damit kann sogar noch ein alter Rohrenfernseher zum SmartTV umfunktioniert werden. Es muss lediglich Kodi auf dem Raspberry installiert werden.

## 1| Mediacenter-Distributionen

Wenn der Raspberry Pi ausschließlich als Mediacenter fungieren soll, kann am einfachsten eine fertige Mediacenter-Distribution (z.B. [OpenELEC](http://openelec.tv/), [OSMC](https://osmc.tv) oder [XBIAN](http://www.xbian.org/)) verwendet werden. Der Aufwand fur die Einrichtung ist dabei minimal: Image runterladen, auf die Karte schreiben und Booten. In der Regel steht dann schon eine fertige Kodi-Umgebung zur Verfugung. Dabei sind die fertigen Mediacenter-Distributionen auf den Kodi-Betrieb optimiert, was zu Problemen fuhren kann, wenn der Raspberry auch noch andere Aufgaben ubernehmen soll. Daher habe ich mich entschieden meinen [Kodi](https://kodi.tv/) auf einem standard [Raspian Jessie Lite](https://www.raspberrypi.org/downloads/raspbian/) aufzusetzen.

## 2| Die Richtige Version auswahlen

In den offiziellen Raspbian-Repository sind momentan leider nur die etwas altere Version 15.2 oder die Beta-Version (17.0-Beta X) von [Kodi](https://kodi.tv/) verfugbar. Die aktuelle, stabile Version von Kodi (Version 16.x) ist leider nur in einem 3rd-Party-Repository von [pplware](http://pipplware.pplware.pt/) verfugbar.

Da ich ein halbwegs zuverlassiges aber auch aktuelles System haben mochte, verzichte ich auf Experimente mit Beta-Versionen. Das stretch-Repository ist somit raus. Da ich nach einer kurzen Recherche bisher nichts negatives uber [pplware](http://pipplware.pplware.pt/) gelesen habe, habe ich mich daher fur die 16er-Version von [pplware](http://pipplware.pplware.pt/) entschieden.

**Hinweis:** Auf die Grundinstallation von Raspbian Jessie Lite gehe ich hier nicht mehr ein.

Bevor mit der Installation begonnen wird, empfiehlt es sich ein Backup der SD-Karte anzulegen.

## 3| Kodi auf dem Raspberry

Also zunachst das Repository eintragen und den zugehorigen Schlussel importieren:

Danach kann Kodi wie ublich per apt-get installiert werden:

## 4| Benutzergruppen

Anschließend muss sichergestellt werden, dass die Gruppe "input" existiert und der Standardbenutzer fur Kodi in den entsprechenden Benutzergruppen ist:

12345678910 
addgroup --system inputaddgroup --system kodiusermod -g kodi kodiusermod -a -G audio kodiusermod -a -G video kodiusermod -a -G input kodiusermod -a -G dialout kodiusermod -a -G plugdev kodiusermod -a -G tty kodiusermod -a -G users kodi

## 5| Device-Berechtigungen

Damit kodi spater richtig lauft mussen die Berechtigungen fur einige Devices angepasst werden. Deshalb werden zwei Config-Files fur udev angelegt:

123456789101112 
cat >> /etc/udev/rules.d/10-permissions.rules << EOF# inputKERNEL=="mouse*|mice|event*", MODE="0660", GROUP="input"KERNEL=="ts[0-9]*|uinput", MODE="0660", GROUP="input"KERNEL==js[0-9]*, MODE="0660", GROUP="input"# ttyKERNEL=="tty[0-9]*", MODE="0666"# vchiqSUBSYSTEM=="vchiq", MODE="0660", GROUP="video"EOF

## 6| Boot-Config

Anschließend muss sichergestellt werden, dass in der Datei /boot/config.txt ausreichend GPU-Speicher zugeordnet ist und die [MPEG2](http://www.raspberrypi.com/mpeg-2-license-key/) und [VC1-Lizenzen](http://www.raspberrypi.com/vc-1-license-key/) fur den Raspberry installiert sind:

123456789 
# Sets the memory split between the CPU and GPU depending on Model# The CPU gets the remaining memory.gpu_mem_256=128gpu_mem_512=160gpu_mem_1024=256# Add Licences for Hardware Support for MPG2 und VC1decode_MPG2=<your_license_here>decode_WVC1=<your_license_here>

Um ganz sicherzugehen kann die Aktivierung der der Hardware-Dekodierung zusatzlich wie folgt gepruft werden.

Wird hier fur einen oder beide Codecs "disabled" angezeigt, dann ist vermutlich die falsche Lizenz in der Datei /boot/config.txt eingetragen

Da ich Kodi an einem alten Rohrenfernseher betreibe, muss ich in der config.txt zusatzlich noch sicherstellen, dass die Video-Ausgabe uber den Composite aktiviert ist:

## 7| Autostart

Zu guter Letzt soll beim Booten kodi direkt gestartet werden. Dazu muss in der Datei /etc/default/kodi lediglich der Eintrag "ENABLED=1" eingefugt und ggf. dein Eintrag "USER" auf den Wert "kodi" abandern, sodass die Datei anschließend so aussehen sollte:

12345678 
# Set this to 1 to enable startupENABLED=1# The user to run Kodi asUSER=kodi# Adjust niceness of Kodi (decrease for higher priority)NICE=-5

Wenn alles passt, sollte nach einem Reboot kodi automatisch unter dem Benutzer kodi gestartet werden. Im nachsten Teil gehe ich auf einige Anpassungen an der Kodi-Config ein, die ich vorgenommen habe.

## 8| Quellen
