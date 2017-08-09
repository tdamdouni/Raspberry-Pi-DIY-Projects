# Raspberry Pi: meine Standardkonfiguration 

_Captured: 2017-05-01 at 17:22 from [indibit.de](http://indibit.de/raspberry-pi-meine-standardkonfiguration/)_

Jahrelang ging der [Raspberry Pi](http://indibit.de/recommends/rpi_amazon/) irgendwie an mir vorbei. Ich hatte naturlich mitbekommen, dass es da so einen kleinen Computer fur schmales Geld gibt, aber mir erschloss sich irgendwie nicht, was ich damit machen soll. Kurzlich hat sich das geandert. Ich hab mir so ein Teil gekauft, und dann gleich noch einen. Dazu fliegen hier 4 Speicherkarten herum, wobei ich jede wahrscheinlich schon 5 mal mit einem Image bespielt habe. Da kommt Routine rein.

![Raspberry Pi Modell B+](https://i1.wp.com/indibit.de/wp-content/uploads/2015/06/Raspberry_Pi.jpg?resize=800%2C488)

> _Raspberry Pi Modell B+_

Mit diesem Post mochte ich gern meine Standardkonfiguration teilen.

Den Mini-Computer, nebst Speicherkarte und Netzteil habt ihr sicher schon. Was wir aber noch brauchen ist ein Betriebssystem, zum Beispiel Raspbian von der [offiziellen Raspberry Pi-Seite](http://www.raspberrypi.org/downloads) ([Direktdownload der neuesten Version](http://downloads.raspberrypi.org/raspbian_latest)). Außerdem ein Netzwerkkabel.

Zu aller erst muss das Betriebssystem, das in Form eines Image heruntergeladen wurde, auf die SD-Karte geschoben werden.

Unter Mac OS X verwendet man am einfachsten ein Tool wie den [Pi Filler](http://ivanx.com/raspberrypi/) ([Direktdownload](http://ivanx.com/raspberrypi/files/PiFiller.zip)).

Die Sache erklart sich eigentlich von selbst:

  1. Pi Filler starten
  2. alle SD-Karten entfernen
  3. Image auswahlen
  4. SD-Karte einstecken und in `RASPBERRY` umbenennen (optional)
  5. `Erase SD Card` anklicken
  6. Passwort eingeben
  7. warten
![Pi Filler: Daten werden auf die SD-Karte geschrieben](https://i2.wp.com/indibit.de/wp-content/uploads/2015/06/pi_filler_erase_SD.png?resize=800%2C488)

> _Pi Filler: Daten werden auf die SD-Karte geschrieben_

Windows-User greifen zu [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/?source=typ_redirect) ([Direktdownload](http://sourceforge.net/projects/win32diskimager/files/latest/download)). Auch hier ist der Vorgang denkbar einfach:

  1. SD-Karte einstecken
  2. Win32 Disk Imager starten
  3. Image auswahlen
  4. Ziellaufwerk auswahlen
  5. Warnhinweis bestatigen
  6. warten
![Win32 Disk Imager: Daten werden auf die SD-Karte geschrieben](https://i0.wp.com/indibit.de/wp-content/uploads/2015/06/win32diskimager.png?resize=421%2C213)

> _Win32 Disk Imager: Daten werden auf die SD-Karte geschrieben_

Wenn der Vorgang abgeschlossen ist, werfen wir die SD-Karte aus, stecken sie direkt in den SD-Reader des Raspberry Pi, verbinden ihn mit dem Netzwerk und schließen das Netzteil an.

Nach kurzer Zeit sollte die rote LED am Raspberry Pi leuchten und die grune blinken. Sollte etwas schiefgegangen sein, einfach das Image nochmal neu auf die Speicherkarte bringen.

[Per SSH verbinden wir uns](http://indibit.de/ssh-ein-paar-grundlagen/) auf den Raspberry Pi. Welche IP-Adresse dieser derzeit hat zeigt die Weboberflache Eures Routers an. Sonst erreicht man ihn oft auch unter `raspberrypi` (variiert je nach verwendetem Image) oder sucht ihn mittels [Pi Finder](http://ivanx.com/raspberrypi/) ([Direktdownload](http://ivanx.com/raspberrypi/files/PiFinder.zip)).

Ebenfalls abhangig vom verwendeten Image sind Standard-Benutzername und Passwort. Viele verwenden als Benutzer `pi` und als Passwort `raspberry`.

Schritt 1 bei der Konfiguration ist das Ändern des Passwortes. Der passende Befehl dafur lautet

`$ passwd`

Hier greifen die System-Richtlinien, wie Passworter gewahlt werden mussen. Da grundsatzlich keines meiner Gerate von Außen uber das Internet erreichbar ist, bevorzuge ich bei unkritischen Anwendungen auch eher einfachere Passworter. Das erreichen wir mit

`$ sudo passwd pi`

Nun kann man ein beliebiges Passwort wahlen.

Damit der Raspberry Pi die richtige Uhrzeit bekommt, muss die Zeitzone korrekt eingestellt werden:

`$ sudo dpkg-reconfigure tzdata`

Als erstes wird hier die Region, anschließend die nachst großere Stadt ausgewahlt und mit der Eingabetaste bestatigt.

![tzdata: Zeitzone einstellen](https://i0.wp.com/indibit.de/wp-content/uploads/2015/06/rpi_ssh_zeitzone_stadt.png?resize=800%2C514)

> _tzdata: Zeitzone einstellen_

Es gibt noch ein paar weitere Einstellungen, die man sich anschauen sollte:

`$ sudo raspi-config`

![raspi-config: Startbildschirm](https://i2.wp.com/indibit.de/wp-content/uploads/2015/06/rpi_ssh_raspi-config1.png?resize=800%2C514)

> _raspi-config: Startbildschirm_

Damit spater der gesamte Speicherplatz auf der Karte zur Verfugung steht, muss das Dateisystem expandiert werden. Macht man dies nicht, sind irgendwann die 2 GB, die so zur Verfugung stehen, voll und der Raspberry Pi bekommt Probleme.

_TIPP: Wer spater ein Backup machen mochte (siehe ganz unten), uberspringt diesen Schritt erstmal und macht ihn nach dem Backup. Das hat den Vorteil, dass Ihr das Backup dann auch auf einer kleineren Speicherkarte nutzen konnt._

Wir wahlen also `Expand Filesystem`.

![raspi-config: Dateisystem expandieren](https://i1.wp.com/indibit.de/wp-content/uploads/2015/06/rpi_ssh_raspi-config_expand_filesystem.png?resize=800%2C514)

> _raspi-config: Dateisystem expandieren_

Beim nachsten Neustart wird die Aktion durchgefuhrt. Anschließend steht der volle Speicherplatz zur Verfugung.

Wenn wir einmal hier im Menu sind, stellen wir noch schnell die Sprache um. Viele Programme und einiges an Terminal-Ausgaben sind von da an in Deutsch. Wir hangeln uns uber `Internationalisation Options` zu `Change Locale`, wahlen `de_DE.UTF-8 UTF-8` mit der Leertaste aus, und `en_GB.UTF-8 UTF-8 ab`.

![raspi-config: Sprache auswählen](https://i1.wp.com/indibit.de/wp-content/uploads/2015/06/rpi_ssh_raspi-config_internationalisation_options_1.png?resize=800%2C514)

> _raspi-config: Sprache auswahlen_

Nach dem Betatigen der Eingabetaste wird nach der Standardsprache gefragt. Hier wahlen wir `de_DE.UTF-8` aus.

![raspi-config: Standardsprache festlegen](https://i0.wp.com/indibit.de/wp-content/uploads/2015/06/rpi_ssh_raspi-config_internationalisation_options_2.png?resize=800%2C514)

> _raspi-config: Standardsprache festlegen_

Wir bestatigen wiederum mit der Eingabetaste und warten, bis die Änderungen an den Spracheinstellungen ubernommen wurden.

Spatestens wenn man sich den zweiten Raspberry Pi zulegt wird es unubersichtlich. Also verpassen wir ihm gleich einen neuen Namen. Das geht ebenfalls uber `raspi-config `und ist unter `Advanced Options -> Hostname` zu finden.

![raspi-config: Hostname festlegen](https://i2.wp.com/indibit.de/wp-content/uploads/2015/06/rpi_ssh_raspi-config_hostname.png?resize=800%2C514)

> _raspi-config: Hostname festlegen_

Alternativ fuhrt der Weg uber die Kommandozeile:

`$ sudo nano /etc/hostname`

Den Inhalt aus Zeile 1 loschen und den neuen Namen eintragen. Anschließend mit STRG+X beenden und die Frage, ob die Änderungen gespeichert werden sollen, durch drucken der J-Taste, gefolgt von der Eingabetaste bestatigen.

`$ sudo nano /etc/hosts`

In Zeile 8 wird `raspberrypi` gegen den gewunschten Namen ausgetauscht.

Hat man den Hostname uber `raspi-config` geandert, fragt es direkt danach. Ansonsten:

`$ sudo reboot`

Sobald das System wieder verfugbar ist, loggen wir uns erneut per SSH ein, bringen die Paketverwaltung `apt-get` auf den aktuellen Stand, aktualisieren installierte Paket und werfen unnotiges von Board - alles in einem Rutsch. Wieder gefolgt von einem Neustart:

`$ sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove -y && sudo reboot`

Das dauert jetzt eine Weile.

Wer feste IP-Adressen in seinem Netzwerk bevorzugt, kann diese wie folgt einstellen:

`$ sudo nano /etc/network/interfaces`

Es lassen sich sowohl fur LAN, als auch fur WLAN, feste IP-Adressen einstellen. In der Konfigurationsdatei werden die benotigten Informationen zur IP-Adresse, Subnet-Maske und dem Gateway ins Internet einfach eingetragen.

In meinem Beispiel sieht das so aus:

12345678
`auto lo``iface lo inet loopback``iface eth0 inet static``address 192.168.243.20``netmask 255.255.255.0``gateway 192.168.243.1``dns-nameservers 192.168.243.1`

Wenn der Raspberry Pi per WLAN ins Netz gebracht wird, kann es nicht schaden, die LAN-Schnittstelle auf DHCP zu stellen. So kommt man immer ohne Muhe an das System, falls mal der WLAN-Schlussel geandert wird. Naturlich ist es auch moglich, fur LAN und WLAN gleichzeitig feste IP-Adressen zu verwenden.

123456789101112131415161718
`auto lo``iface lo inet loopback``iface eth0 inet dhcp``allow-hotplug wlan0``auto wlan0``#iface wlan0 inet dhcp``iface wlan0 inet static``address 192.168.243.30``netmask 255.255.255.0``broadcast 192.168.243.255``network 192.168.243.0``gateway 192.168.243.1``dns-nameservers 192.168.243.1``wpa-ap-scan 1``wpa-scan-ssid 1``wpa-ssid ``"der Name des WLAN-Netzwerkdes"``wpa-psk ``"Passwort des WLAN-Netzwerkes"`

Sind alle Eintragungen angepasst/erganzt, verlassen wir den Editor mit STRG+X und bestatigen das Speichern der Änderungen wieder mit der J-Taste, gefolgt von der Eingabetaste. Anschließend starten wir den Netzwerkdienst neu:

`$ sudo service networking restart`

Wenn sich die SSH-Verbindung aufhangt - einfach neu verbinden. Alternativ einfach einen Neustart durchfuhren:

`$ sudo reboot`

Der Raspberry Pi sollte nach der obigen Konfiguration nun per WLAN erreichbar sein. Allerdings kann es passieren, dass die Verbindung lahmt oder der kleine Computer einfach standig nicht erreichbar ist. Das kann seine Ursache im aktivierten Energiesparmodus haben. Den Status kann man mittels

`$ iwconfig`

abfragen. Allerdings gibt es da einen kleinen Haken:  
Die Angabe `Power Management:off` zeigt lediglich, dass das Betriebssystem keinen Energiesparmodus aktiviert hat. Was der Treiber macht, geht daraus nicht hervor.

![iwconfig: Power Management:off](https://i1.wp.com/indibit.de/wp-content/uploads/2015/06/rpi_ssh_iwconfig_powermanagement.png?resize=800%2C514)

> _iwconfig: Power Management:off_

Der Energiesparmodus des Treibers lasst sich wie folgt abfragen:

`$ cat /sys/module/8192cu/parameters/rtw_power_mgnt`

Wobei `8192cu` fur einen sehr weit verbreiteten Chipsatz des WLAN-Moduls steht. Als Antwort bekommen wir `1`, was so viel bedeutet wie, dass Power Management (auf Treiberebene) eingeschaltet ist.

Sollte Euch der Chipsatz unbekannt sein, so ist das meist kein Beinbruch, denn es gibt noch den `8188eu`, der ebenfalls sehr weit verbreitet ist. Wenn wir jetzt einfach bei beiden den Energiesparmodus deaktivieren, stehen die Chancen gut, erfolgreich zu sein.

Um den Energiesparmodus abzuschalten, editieren wir die Konfigurationsdateien mit dem Befehl

`$ sudo nano /etc/modprobe.d/8192cu.conf`

und fugen folgendes ein:

Im Zweifel passen wir fur den anderen Chipsatz ebenfalls die Konfiguration an:

`$ sudo nano /etc/modprobe.d/8188eu.conf`

und fugen dabei folgendes ein:

Nach einem Neustart werden die Änderungen aktiv.

`$ sudo reboot`

Sobald der Raspberry Pi wieder gestartet und per SSH erreichbar ist, konnen wir den aktuellen Status abfragen:

`$ cat /sys/module/8192cu/parameters/rtw_power_mgnt`

Wenn als Antwort `0` kommt, ist alles gut gegangen.

Zuweilen kann es vorkommen, dass die WLAN-Verbindung getrennt wird. So zum Beispiel bei einem Neustart des Routers. Der Raspberry Pi verbindet sich dann mit den Standardeinstellungen nicht automatisch neu, sodass nur ein Neustart oder Ziehen und Stecken des WLAN-Sticks Abhilfe schaffen.

Das beheben wir, indem wir das dafur verantwortliche Script gegen eines austauschen, das diese Funktion beinhaltet. Dazu erzeugen wir als erstes ein Backup des alten Scripts:

`$ sudo mv /etc/ifplugd/action.d/ifupdown /etc/ifplugd/action.d/ifupdown.old`

Anschließend kopieren wir das funktionierende Script an die alte Stelle…

`$ sudo cp /etc/wpa_supplicant/ifupdown.sh /etc/ifplugd/action.d/ifupdown`

…und starten den Raspberry Pi neu:

`$ sudo reboot`

Der Midnight Commander sollte auf keinem System fehlen. Er ist das Linux-Pendant vom Norton Commander, der zu DOS-Zeiten wohl auf den meisten Computern zu finden war. Installiert wird er mit

`$ sudo apt-get install mc`

und lasst sich von uberall auf der Kommandozeile mittels

`$ mc`

starten. Wer lieber mit dem internen Editor arbeitet, statt mit `nano`, findet diese Einstellung unter

`Optionen -> Einstellungen:`  
`[ ] Internen Editor benutzen`

Mit der Leertaste wird die Option aktiviert. Anschließend offnet sich nach dem betatigen der F4-Taste der interne Editor.

![Midnight Commander: Internen Editor benutzen](https://i0.wp.com/indibit.de/wp-content/uploads/2015/06/rpi_ssh_mc_editor.png?resize=800%2C514)

> _Midnight Commander: Internen Editor benutzen_

Fur die Freigabe von Netzwerkordnern fur Windows-Computern wird der SAMBA-Server benotigt. Den installieren wir mit

`$ sudo apt-get install samba samba-common-bin`

Anschließend mussen noch ein paar Einstellungen vorgenommen und Freigaben eingerichtet werden.

`$ sudo nano /etc/samba/smb.conf`

Es empfiehlt sich, die Passwortabfrage zu aktivieren. Dazu suchen wir die Zeile mit dem Inhalt

und entfernen die `#`, die diesen Eintrag auskommentiert.

Am Ende der Datei werden die Freigaben eingetragen. Bei mir ist immer das Verzeichnis `/opt` dabei, um schnell auf die installierte Software zugreifen zu konnen.

Weitere Freigaben werden nach dem gleichen Schema einfach unten angefugt. Anschließend muss noch ein Benutzer nebst Passwort fur den Zugriff angelegt werden:

`$ sudo smbpasswd -a pi`

Nach einem Neustart des Dienstes steht die Dateifreigabe zur Verfugung:

`$ sudo /etc/init.d/samba restart`

Wenn man mit einem oder mehreren Mac-Computern auf den Raspberry Pi zugreifen mochte, ist AFP die bessere Wahl. Zwar versteht sich der Mac auch mit einem SAMBA-Server, aber AFP lauft einfach flussiger.

`$ sudo apt-get install netatalk`

Nach dem die Installation durchgelaufen ist, mussen auch hier noch ein paar Sachen konfiguriert werden. Fur etwas bessere Performance schalten wir zu aller erst die Abwartskompatibilitat zu Mac OS-Versionen vor OS X (also OS 9 oder fruher) aus:

`$ sudo nano /etc/default/netatalk`

Dabei setzen wir folgende Eintrage:

Anschließend werden die Dateifreigaben eingerichtet:

`$ sudo nano /etc/netatalk/AppleVolumes.default`

Eine Freigabe ist schon enthalten:

Sie reprasentiert die Freigabe des home-Verzeichnisses, welches jeder Nutzer vom System zugewiesen bekommt. Wir erganzen unsere eigenen Freigaben. In meinem Fall wieder `/opt`:

Weitere Informationen zu den Parametern, die man in dieser Datei setzen kann, findet man [hier](http://netatalk.sourceforge.net/2.0/htmldocs/AppleVolumes.default.5.html). Zum Abschluss des Vorganges muss der Netatalk-Dienst neu gestartet werden:

`$ sudo /etc/init.d/netatalk restart`

Solltet Ihr noch Perl benotigen:

`$ sudo apt-get install perl libdevice-serialport-perl libio-socket-ssl-perl libwww-perl libxml-simple-perl`

Manche Pakete/Software bekommt man als .deb-Datei aus dem Internet. Zur Installation werden diese in ein beliebiges Freigabeverzeichnis auf dem Raspberry Pi geschoben und mit dem Befehl

`$ sudo dpkg -i <debfile>`

installiert.

Wenn man viel ausprobiert geht auch mal was kaputt. Um nicht jedes Mal wieder bei null anfangen zu mussen, machen wir noch schnell ein Backup.

Mac-User verwenden dafur [Pi Copier](http://ivanx.com/raspberrypi/) ([Direktdownload](http://ivanx.com/raspberrypi/files/PiCopier.zip)). Auch dieses Prozedere ist denkbar einfach:

  1. Raspberry Pi herunter fahren:  
`$ sudo shutdown -h now`
  2. SD-Karte aus dem Raspberry Pi entfernen
  3. Pi Copier starten
  4. Verzeichnis auswahlen, wohin das Backup gespeichert werden soll
  5. Dateinamen angeben (oder Vorschlag einfach bestatigen)
  6. Entscheiden, ob das Backup komprimiert werden soll
  7. SD-Karte einstecken
  8. `Backup now` anklicken
  9. Passwort eingeben
  10. warten
![Pi Copier: Backup läuft](https://i1.wp.com/indibit.de/wp-content/uploads/2015/06/pi_copier_running.png?resize=800%2C455)

> _Pi Copier: Backup lauft_

Hier verwenden wir das gleiche Tool wie oben, den Win32 Disk Imager. Diesmal wahlen wir jedoch kein vorhandenes Image aus, sondern legen ein neues an. Der Ablauf:

  1. SD-Karte einstecken
  2. Win32 Disk Imager starten
  3. Bei `Image File` selber einen Pfad + Dateinamen festlegen
  4. Quelllaufwerk auswahlen
  5. `Read` anklicken
  6. Warten
