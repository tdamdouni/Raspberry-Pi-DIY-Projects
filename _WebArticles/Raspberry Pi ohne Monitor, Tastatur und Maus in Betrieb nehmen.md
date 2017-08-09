# Raspberry Pi ohne Monitor, Tastatur und Maus in Betrieb nehmen 

_Captured: 2015-12-20 at 14:10 from [www.interaktionsdesigner.de](http://www.interaktionsdesigner.de/2014/raspberry-pi-ohne-monitor-tastatur-und-maus-in-betrieb-nehmen/)_

Ein Artikel von [Paul Lunow](http://www.paul-lunow.de), erschienen 2014 auf [Interaktionsdesigner.de](http://www.interaktionsdesigner.de).

## Vorwort

Vorweg sei gesagt das der kleine Computer wirklich einen tollen Einstieg bietet in die wunderbare Welt der Minicomputer mit den unbegrenzten Moglichkeiten. Auch als an grafische Benutzeroberflachen gewohnter Benutzer kommt man schnell hinter die Mechanismen und Tricks der Konsole. Damit man uberhaupt dort ankommt muss allerdings ein Betriebssystem auf einer SD Karte platziert und installiert werden.

## Ausrustung

Zum Starten benotigt man einen Raspberry Pi und eine mind. 4GB große SD Karte. Ein Mini USB Kabel zur Stromversorgung und ein Netzwerkkabel liegen bestimmt in der Kabelkiste rum. Von der [offiziellen Raspberry Pi Seite](http://www.raspberrypi.org/downloads) ladt man sich die neuste Version des **NOOBS** Betriebssystems herunter.

## Vorbereitung

Die SD Karte sollte man als FAT32 Partition formatieren. Das Festplattendienstprogramm tut das ausgezeichnet. Ist die Karte leer kopiert man den Inhalt des Noobs Archivs darauf. Dieses bringt eine ganze Reihe von verschiedenen Linux Distributionen mit. Startet man den Pi kann man eine Auswahl treffen. Ohne Bildschirm, Tastatur und Maus allerdings sehr schwierig.

## Durchfuhrung

Deshalb soll Noobs das passende System **automatisch** und **headless** installieren! Auf der SD Karte mussen die folgenden Vorbereitungen getroffen werden:

  1. Im Verzeichnis `os/` liegen alle verfugbaren Distributionen. Hier loscht man alle mit Ausnahme der zu verwendenden. Wenn man keine Ahnung hat, dann am besten **Raspbian** behalten.
  2. Jetzt in das ubrig gebliebene Verzeichnis wechseln (z.B. `os/Raspbian`) und die Datei `flavours.json` offnen. Auch hier darf nur ein Eintrag ubrig bleiben.
  3. Im Rootverzeichnis der SD Karte liegt die Datei `recovery.cmdline` \- diese enthalt eine Zeile an dessen Ende, mit Leerzeichen getrennt, das Wort `silentinstall` angefugt wird.

Fertig!

## Ergebnis

Die so praparierte SD Karte in den Pi stecken, Strom anschließen und warten. Die Installation dauert 30 bis 40 Minuten.

Jetzt fehlt nur noch die IP Adresse. Der einfachste Weg ist sich in den eigenen Router einzuloggen und dort eine **DHCP Tabelle** zu suchen. Wenn alles geklappt hat findet sich hier ein Eintrag mit der IP Adresse, gefolgt vom Namen des neuen Computers: `raspberrypi`.

Hat man die IP Adresse offnet man ein Terminal und gibt den Befehl `ssh pi@IP_ADRESSE` ein. Die folgende Warnung bestatigt man durch eintippen von `yes`. Das Passwort lautet `raspberry`.

Fertig! Jetzt ubernehmen andere Tutorials.

## Kontakt

Ich habe eine Firma gegrundet, um allen Menschen die Moglichkeit zu geben, von den digitalen Vorzugen zu profitieren. Wir entwickeln neue Oberflachen, die Inhalte besser zuganglich machen. Großartige Menschen, tolle Technologie und eine spannende Aufgabe! Deine Chance bei einem Startup dabei zu sein, das noch komplett unter dem Radar lauft. [Mehr Informationen](http://nepos.io/jobs).
