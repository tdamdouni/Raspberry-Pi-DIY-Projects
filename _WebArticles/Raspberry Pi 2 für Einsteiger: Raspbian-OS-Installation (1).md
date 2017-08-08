# Raspberry Pi 2 für Einsteiger: Raspbian-OS-Installation 

_Captured: 2016-11-06 at 22:30 from [weblogit.net](http://weblogit.net/raspberry-pi-2-fuer-einsteiger-raspbian-os-installation-96177/)_

![Raspberry Pi 2 für Einsteiger: Raspbian-OS-Installation](http://static.weblogit.net/wp-content/uploads/2015/03/xraspi-noobs-installation-raspbian-cover.jpg.pagespeed.ic.W4Q4NxxjsX.jpg)

> _Artikel teilen Artikel tweeten_

Ohne Betriebssystem [auf der microSD-Karte](http://weblogit.net/2015/02/27/raspberry-pi-2-fuer-einsteiger-sinnvolles-zubehoer-23888/) tut sich beim Raspberry Pi & Raspberry Pi 2 herzlich wenig. In diesem kleinen Guide zeigen wir Euch, wie man eine microSD-Karte vorbereitet und mit NOOBS bestuckt, dem einfachen Installer fur die aktuellen Betriebssysteme inklusive Raspbian, der performanten ersten Wahl fur Bastler, Coder und Einsteiger.

![raspberry-pi-2-microsd](http://static.weblogit.net/wp-content/uploads/2015/02/xraspberry-pi-2-microsd-620x349.jpg.pagespeed.ic.Rtq9NA-2Ru.jpg)

**Auf dem Raspberry Pi 2 laufen verschiedene fur den Quad Core ARM-Prozessor optimierte Betriebssysteme & Images (teilweise kombinierbar) fur die SD-Karte des Pi, darunter: **

  * **Raspbian** (basiert auf Debian Linux und ahnelt somit auch Ubuntu - [Link](http://www.raspberrypi.org/downloads/) )
  * **Arch Linux** (eine tolle Linux-Lernerfahrung, aber etwas hardcore fur Einsteiger - [Link](http://archlinuxarm.org/platforms/armv7/broadcom/raspberry-pi-2) )
  * **Snappy Ubuntu Core** (eine Distribution fur IoT/Cloud-Entwickler - [Link](http://www.raspberrypi.org/downloads/) )
  * **Risc OS** (ein benutzerfreundliches, britisches Betriebssystem - [Link](https://www.riscosopen.org/content/downloads/raspberry-pi) )
  * **OpenELEC ab 5.0.1+** (ein auf XBMC bzw. Kodi basierendes Media Center Image - [Link](http://openelec.tv/get-openelec) )
  * **RetroPie** (Retro-Emulation von SNES/N64/etc mit Hammer-Features - Link )

Wir wollen fur den Einstieg eine Probefahrt in **Raspbian** machen, denn Raspbian Wheezy (letzterer Titel bezieht sich auf die aktuelle Version von Debian) sticht bislang durch uberlegene Geschwindigkeit und naturlich hohe Einsteigerfreundlichkeit hervor.

Mit **Raspbian** kann man wunderbar die Moglichkeiten des Raspberry Pi 2 auskundschaften und das neue Gadget beschnuppern, daruber hinaus ist die Installation mit NOOBS (steht fur _"New Out oOf the Box Software"_) ein Klacks. Los geht's!

### Installer herunterladen - Torrent oder ZIP?

Zuerst mussen wir entweder die ZIP-Datei von NOOBS vom [HTTP-Server](http://downloads.raspberrypi.org/NOOBS_latest) oder als [Torrent](http://downloads.raspberrypi.org/NOOBS_latest.torrent) herunterladen. Der Torrent ist ubrigens vollig legal und dank Peer-to-Peer oftmals schneller, Mac-User konnen hierfur den [Transmission](http://www.transmissionbt.com/download/)-Client benutzen - unter Windows empfiehlt sich [Deluge](http://deluge-torrent.org/). Einfach die .torrent-Datei damit offnen und dem Fortschrittsbalken voller Vorfreude zuschauen. Ansonsten geht naturlich auch einfach der HTTP-Download.

### Vorbereitung der µSD-Karte (microSD)

Wahrend der NOOBS-Installer durch die Leitung reinkommt, packen wir schon mal unsere microSD-Karte mit mindestens 4 GB oder besser 8 GB (und mehr) aus und schließen sie per Kartenleser am PC oder Mac an. Wer ubrigens keinen Kartenleser hat, sollte sich z.B. [so einen hier](http://www.amazon.de/gp/product/B009D79VH4/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B009D79VH4&linkCode=as2&tag=wbi-21) besorgen. Ob man nun USB 3.0 oder USB 2.0 nimmt, das ist aktuell nicht so wild. Aber langfristig lohnt sich naturlich der aktuellere Standard, falls die Ports dafur vorhanden sind.

Damit es mit der SD-Karte klappt, empfiehlt die Raspberry Pi Foundation eine ordentliche Formatierung mit dem offiziellen SD-Formatter. Diesen gibt es hier fur den PC oder Mac - wahlt einfach den passenden Laufwerksbuchstaben/Titel fur die Karte als Ziel aus und lasst das Tool seine Magie verrichten. Fortgeschrittene Nutzer benutzen einfach die evtl. bestehende Partitionstabelle und formatieren die Datenpartition als FAT.

Ist die Karte erfolgreich formatiert, gilt es nun die Daten aus dem Archiv von NOOBS in das sogenannte Wurzelverzeichnis der Karte zu kopieren. Wenn ihr NOOBS entpackt, sieht die Struktur so aus (siehe Bild) und muss als Kopie exakt so auch auf der SD-Karte landen:

![Noobs-Ordnerstruktur](http://static.weblogit.net/wp-content/uploads/2015/03/Noobs-Ordnerstruktur-620x301.png.pagespeed.ce.oKLTBfuUm5.png)

> _Hat soweit alles geklappt? Kopiervorgang abgeschlossen?_

Jetzt kannst Du die SD-Karte auswerfen. Schiebe sie in den SD-Port des Raspberry Pi 2, bis es horbar aber leise klickt und die Karte eingerastet ist. Stopsele die [passenden Eingabegerate und ein Videokabel](http://weblogit.net/2015/02/27/raspberry-pi-2-fuer-einsteiger-sinnvolles-zubehoer-23888/) an. Verbinde nun das [Netzteil](http://weblogit.net/2015/02/27/raspberry-pi-2-fuer-einsteiger-sinnvolles-zubehoer-23888/) oder ein USB-Kabel mit dem Port fur den Saft.

![raspi-b-plus-ports](http://static.weblogit.net/wp-content/uploads/2015/03/xraspi-b-plus-ports-620x437.png.pagespeed.ic.x4-j5kUioe.png)

> _Die Ports des Raspberry Pi 2 Model B+ sind identisch mit dem Modell 1 B+_

### Wir booten den NOOBS-Installer

Die von mir verwendete NOOBS-Version brachte beim Hochfahren die folgenden Optionen: Raspbian, Datenpartition anlegen, Rasbpian - Boot to Scratch. Letztere Option lasst das Betriebssystem direkt in die visuelle Programmiersuite Scratch (ideal fur Kids, aber auch spaßig fur Programmiereinsteiger und Bastler) booten.

Unten lasst sich die Sprache bzw. das Tastaturlayout auswahlen.

![noobs-interface](http://static.weblogit.net/wp-content/uploads/2015/03/xnoobs-interface-620x465.png.pagespeed.ic.anXM_A1z7p.png)

Ich wahle Raspbian und die Datenpartition, die ich spater auf die komplette SD-Karte expandieren lasse. Das ist spater auch nochmals mit `raspi-config` moglich, das Tool startet bei der Erstinstallation und ist spater auch abrufbar.

![piconfig](http://static.weblogit.net/wp-content/uploads/2015/03/xpiconfig-620x221.jpg.pagespeed.ic.TVxUSQ9vzl.jpg)

Jetzt richtet sich das Dateisystem wie von alleine ein, Dateien werden kopiert und wir schauen uns je nach Geschwindigkeit der SD-Karte etwas langer oder kurzer den Fortschrittsbalken an. Das kennt ihr vielleicht von einer anderen Betriebssysteminstallation.

Beim ersten Boot sind dann vier Himbeeren zu sehen, gefolgt von reichlich textformigen Ausgaben des Systems. Liebe Windows-Nutzer, keine Sorge, das muss so und ist vollig normal.

**Schließlich begrußt uns der sogenannte Prompt, der nach Login und Kennwort fragt. Standardmaßig ist beides mit `pi` zu beantworten.**

Achtung: typischerweise sieht man [keine Sternchen](http://weblogit.net/2015/01/29/passwort-im-terminal-eingeben-bleibt-leer-reagiert-nicht-75843/) bei der Passworteingabe.

![raspberry-pi-prompt](http://static.weblogit.net/wp-content/uploads/2015/03/xraspberry-pi-prompt-620x465.jpg.pagespeed.ic.yXZ_9payIs.jpg)

Wer sich schon ein wenig mit Linux befasst hat, findet sich schnell zurecht unter Raspbian. Einsteiger mochten vermutlich zunachst einmal die grafische Oberflache starten, dafur ist der folgende Befehl geeignet: `startx`

Wer sein Kennwort vorher andern mochte, kann dies mit dem Befehl `passwd` tun. Ab hier kann das Erforschen losgehen, in der oberen linken Ecke der grafischen Oberflache finden sich Verknupfungen zu Programmen sowie dem Browser. Im nachsten Guide schauen wir uns an, wie man auf unterschiedlichen Wegen Software auf dem Pi installieren kann.

Hast Du den ersten Artikel der Raspi2-Serie verpasst? Hier gibt es ihn nochmals zum Nachlesen: **[Raspberry Pi 2 fur Einsteiger: Was kann man damit machen?](http://weblogit.net/2015/02/25/raspberry-pi-2-fuer-einsteiger-was-kann-man-damit-machen-75295/)**

**Übrigens:** Wenn Du keine Neuigkeiten, Produkt-Tests oder Artikel von uns verpassen willst, dann folge uns am besten auf [Facebook](http://weblogit.net/out/facebook-bottompost) oder [Twitter](http://weblogit.net/out/twitter-bottompost).
