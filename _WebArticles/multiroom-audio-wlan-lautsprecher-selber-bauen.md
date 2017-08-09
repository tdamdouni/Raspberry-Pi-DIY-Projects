# Multiroom-Audio: WLAN-Lautsprecher selber bauen

_Captured: 2017-05-01 at 17:07 from [indibit.de](http://indibit.de/multiroom-audio-wlan-lautsprecher-selber-bauen/)_

Wie ich das Thema Multiroom-Audio bei mir umgesetzt habe, habe ich ja [hier](http://indibit.de/multiroom-audio-meine-umsetzung/) schon erklart. In diesem Beitrag mochte ich Euch nun zeigen, wie ich meine WLAN-Lautsprecher selber gebaut habe. Im Grunde ist da auch nicht viel dabei: Wir nutzen idealerweise einen Lautsprecher, den wir noch irgendwo herumfliegen haben und bauen da zwei Netzteile, einen Raspberry Pi, Verstarker und noch ein paar Kleinigkeiten ein. Dann haben wir das Grobste geschafft.

![Selbstgebauter WLAN-Lautsprecher](https://i0.wp.com/indibit.de/wp-content/uploads/2016/10/ls_lautsprecher_vh2.jpg?resize=560%2C509)

Im Ergebnis erhalten wir dann einen aktiven WLAN-Lautsprecher, der sich per Logitech Media Server und den zugehorigen Apps ansteuern lasst, ein AirPlay-Empfanger fur Apple-Gerate und ein DLNA-Renderer fur andere Gerate liefert. Außerdem konnen die Grundfunktionen mit einer IR-Fernbedienung gesteuert werden. Um Stromkosten zu sparen, wird der Verstarker abgeschaltet, wenn er nicht benotigt wird.

  * [Hardware](http://indibit.de/multiroom-audio-wlan-lautsprecher-selber-bauen/)
  * [Software](http://indibit.de/multiroom-audio-wlan-lautsprecher-selber-bauen/)

Beginnen wir mit dem benotigten Material. Das Ganze ist lediglich als Vorschlag zu verstehen und kann nach belieben angepasst werden. Ich habe viel Wert auf die Balance zwischen Preis und Leistung gelegt, immerhin soll der WLAN-Lautsprecher ja auch bezahlbar bleiben. Insbesondere das Kleinmaterial findet sich bestimmt in der ein oder anderen Schublade bei Euch zuhause.

![Lautsprecher auna Line 501 Hifi](https://i2.wp.com/indibit.de/wp-content/uploads/2016/10/ls_lautsprecher.jpg?resize=560%2C371)

Als ich den ersten WLAN-Lautsprecher gebaut habe, habe ich als Verstarker gleich mehrere [TDA7498 100W Stereo Power Amp](http://indibit.de/recommends/tda7498-100w-stereo-power-amp_ebay/) von Sure Electronics bestellt. Dieses Angebot gibt es jedoch nicht mehr, dafur jede Menge gute Alternativen. Zur Auswahl eines passenden Verstarkers folgende Tipps:

  * Die Angegebenen Leistungen sind in der Regel Spitzenleistungen, die nur bei extremen Spitzen und Lautsprechern mit 4Ω Impedanz erreicht werden.
  * Die tatsachliche Leistung ist auch von der Hohe der Spannung abhangig, mit der der Verstarker betrieben wird. Oft sind Bereiche von 9…30V DC, oder 14…36V DC angegeben. Je hoher die Spannung, desto hoher die Leistung.
  * Hilfreich ist immer ein Blick ins Datenblatt. Da sind meist Diagramme drin, mit denen man den optimalen Arbeitspunkt bestimmen kann.
  * Der Arbeitspunkt sollte so gewahlt werden, dass die Verzerrung (THD) nicht zu hoch ist.
  * Mit der Spannungsversorgung wird der Arbeitspunkt dann festgelegt. Fur meinen Verstarker und meine Anspruche sind 28V optimal.
  * Netzteile, die 28V liefern, gibt es kaum. Man kann jedoch die Ausgangsspannung vieler 24V-Netzteile einstellen. Bei meinem ist die Obergrenze 27,6V. Die habe ich auch eingestellt.

Nach nunmehr uber einem Jahr kann ich sagen, dass ich mit den Verstarkern von Sure Electronics sehr zufrieden bin. Es gab bisher keinerlei Ausfalle, Überhitzungen oder sonstige Probleme an meinen WLAN-Lautsprechern. Den Lufter, der auf dem Kuhlkorper montiert ist, hab ich ubrigens abgeklemmt. Zum einen ist der recht laut und erzielt innerhalb eines geschlossenen Gehauses kaum einen Effekt. Zum anderen wird der Verstarker auch nicht ubermaßig warm, sodass ich darauf verzichten kann.

Ich habe schon verschiedene Komponenten verbaut und manchmal musste ich recht lange nach einer passenden oder preisgunstigen Losung suchen. Deshalb nachfolgend noch 4 Dinge, die ich im ersten WLAN-Lautsprecher verbaut hatte. Damals noch mit einem Raspberry Pi Modell A. Vielleicht konnt Ihr ja etwas davon gebrauchen.

Fangen wir also an. Wenn das Material beschafft ist, zerlegen wir den Lautsprecher in samtliche Einzelteile. Ich habe zudem das Anschlussterminal komplett zerlegt. Darin sollen spater Stromanschluss und WLAN-Antenne montiert werden.

![Lautsprecher in seine Einzelteile zerlegt](https://i1.wp.com/indibit.de/wp-content/uploads/2016/02/mra_lautsprecher_zerlegt.jpg?resize=1024%2C678)

Danach muss man einen Weg finden, wie man die ganzen Einzelteile am besten im Gehause unterbringt. Das kann relativ langwierig sein, wenn wenig Platz vorherrscht. Alle Teile mussen so gedreht werden, dass man sie nachher auch noch anschließen kann. Ganz wichtig dabei: man sollte in der Lage sein, die SD-Karte vom Raspberry Pi auszutauschen, ohne alles komplett zerlegen zu mussen.

Bei den von mir verwendeten Teilen ist folgende Anordnung sinnvoll (Gehause liegt wie oben abgebildet):

  * Ruckwand: Netzteile (links oben und links unten)
  * Linke Seitenwand: Raspberry Pi + PHAT DAC
  * Rechte Seitenwand: Frequenzweiche
  * Unten: Verstarker und Relais-Modul

Das Audiokabel stellt die Verbindung zwischen der Soundkarte und dem Verstarker her. Wir nehmen zwei Drahte und loten sie zuerst am Chinch-Stecker an. Der Draht des inneren Kontaktes wird dann mit dem innern Kontakt des Klinkensteckers verbunden. Anschließend werden die beiden außeren miteinander verbunden. Am Klinkenstecker bleibt der Kontakt, der zwischen dem inneren und dem außeren liegt, frei, da es sich bei diesem WLAN-Lautsprecher um ein reines Mono-Gerat handelt. Sonst musste man ein Y-Kabel bauen (oder kaufen). Nicht vergessen, die Gehause der Stecker uber die Drahte zu schieben, bevor der zweite Stecker angelotet wird.

Im Anschlussterminal werden die C8-Buchse fur den Stromanschluss, sowie das Antennenkabel montiert. Mit einer [RJ45-Kupplung](http://indibit.de/recommends/rj45-kupplung-30cm-kabel-amazon/) kann man den Lautsprecher auch perfekt fur ein Netzwerkkabel vorbereiten. Die Umrisse habe ich auf der Ruckseite angezeichnet, mit einem Bohrer in die Ecken gebohrt und den Rest mit [Nadelfeilen](http://indibit.de/recommends/nadelfeilen_amazon/) weggefeilt.

![C8-Einbaubuchse](https://i2.wp.com/indibit.de/wp-content/uploads/2016/10/ls_c8-buchse.jpg?resize=560%2C371)

![Antennenkabel mit RP-SMA-Stecker und RP-SMA-Einbaubuchse](https://i2.wp.com/indibit.de/wp-content/uploads/2016/10/ls_antennenkabel.jpg?resize=560%2C371)

![RJ45-Kupplung](https://i0.wp.com/indibit.de/wp-content/uploads/2016/10/ls_rj45-kupplung.jpg?resize=560%2C371)

Wer auf eine richtige Werkstatt verzichten muss und stattdessen alles nur am heimischen Schreibtisch machen kann, dem empfehle ich diesen [Mini-Schraubstock](http://indibit.de/recommends/mini-schraubstock_amazon/).

Um Platz im Gehause zu schaffen, wird die Frequenzweiche an einer neuen Stelle montiert. Die angeloteten Kabel sind dafur leider etwas zu kurz, daher habe ich die alten Drahte entfernt und neue angelotet. Weiß ist hier die Masse, die farbigen Drahte jeweils das Signal. Braun = Audiosignal vom Verstarker, Grau = Signal zum Tieftoner, Orange = Signal zum Hochtoner.

![Frequenzweiche mit den alten Drähten](https://i1.wp.com/indibit.de/wp-content/uploads/2016/10/ls_frequenzweiche1.jpg?resize=560%2C371)

![Frequenzweiche mit neuen, längeren Drähten](https://i2.wp.com/indibit.de/wp-content/uploads/2016/10/ls_frequenzweiche2.jpg?resize=560%2C371)

Die Seite mit dem normalen USB-Stecker wird abgeschnitten (benotigen wir auch nicht mehr). Vom verbleibenden Kabelende (das mit dem Micro-USB-Stecker) entfernen wir ein Stuck von der Ummantelung und schneiden den Schirm, den weißen und den gelben Draht ab. Vom roten und schwarzen Draht wird etwas Isolierung entfernt und Aderendhulsen aufgepresst.

![Micro-USB-Kabel](https://i1.wp.com/indibit.de/wp-content/uploads/2016/10/ls_micro-usb-kabel1.jpg?resize=560%2C371)

![Micro-USB-Kabel](https://i1.wp.com/indibit.de/wp-content/uploads/2016/10/ls_micro-usb-kabel2.jpg?resize=560%2C371)

Die zwei Stiftleisten werden jeweils auf den Raspberry Pi Zero, sowie den PHAT DAC gelotet. Die zweipolige Anschlussklemme ist fur den Verstarker gedacht, der fur die Spannungsversorgung nur einen Hohlstecker besitzt. Direkt daneben befinden sich jedoch die Lotpunkte fur ein Schraubterminal.

## Komponenten einbauen und verkabeln

Wenn die Vorbereitungen abgeschlossen sind, machen wir uns an den Einbau und die Verdrahtung der Komponenten. Wie zu erkennen ist, habe ich die Soundkarte nicht huckepack auf den Raspberry Pi gesetzt, sondern daneben gesetzt beide mit Drahten verbunden. Dies schien mir angesichts dessen, dass noch weitere Komponenten an die GPIO angeschlossen werden mussen, die einfachste Losung.

![Verdrahtung der Komponenten im WLAN-Lautsprecher](https://i0.wp.com/indibit.de/wp-content/uploads/2016/10/ls_verdrahtung-1.png?resize=833%2C537)

> _Verdrahtung der Komponenten im WLAN-Lautsprecher_

Es gilt nun, alle Komponenten im Lautsprechergehause einzubauen. Je nach Große des Gehauses kann einen das schon zur Verzweiflung bringen. Daher noch ein paar Tipps, wie es etwas einfacher geht:

  * Drahte einseitig anschließen und das jeweils andere Ende frei hangen lassen, bevor man die Komponenten einbaut. So muss man nur das jeweils andere Drahtende innerhalb des Gehauses anschließen.
  * Komponenten, die im hinteren Teil des Gehauses montiert werden sollen, zuerst einbauen.
  * Teilweise ist es einfacher, wenn man die Locher ohne die Komponenten erstmal vorbohrt. Das geht auch mit den Schrauben, mit denen die Teile nachher befestigt werden sollen.

Der mechanische Teil unseres WLAN-Lautsprechers ist nun weitestgehend fertig. Kommen wir also zur Software.

Im Beitrag [Raspberry Pi: meine Standardkonfiguration](http://indibit.de/raspberry-pi-meine-standardkonfiguration/) habe ich die schonmal recht ausfuhrlich erlautert beschrieben, wie ich meine Raspberry Pi einrichte. Da der Schwerpunkt hier jedoch auf einem funktionierenden WLAN-Lautsprecher liegt, beschranken wir uns hier auf das Wesentliche und nutzen die Boardmittel.

Statt des offiziellen Images von der Raspberry Pi-Downloadseite verwenden wir hier eines, das den benotigten Player bereits beinhaltet. Es gibt da verschiedene zur Auswahl, die je nach Geschmack und Anspruch gewisse Vorteile bieten.

  * [piCorePlayer](https://sites.google.com/site/picoreplayer/home): Basiert auf Tiny Core Linux und ist extrem schlank und schnell, sehr ubersichtlich und Komfortabel, lauft selbst auf der schwachsten Hardware und den altesten Speicherkarten. Einziger Nachteil fur mich: keine `python-lirc`-Bibliothek verfugbar. Somit funktioniert mein Script mit der Fernbedienung leider nicht. Das Image ist nur 78 MB groß.
  * [Max2Play](https://www.max2play.com): Basiert auf Raspbian und liefert entsprecht auch alles mit, was man gewohnt ist. Fur verschiedene Soundkarten gibt es auch optimierte Images. Allerdings ist die „beworbene" Oberflache meiner Ansicht nach viel zu unubersichtlich, schlecht erklart, recht durcheinander und keineswegs etwas fur Anfanger, die sich uberhaupt nicht auskennen. Außerdem muss selbst fur recht einfache Dinge eine Lizenz erworben werden.

Die PHAT DAC Soundkarte besitzt den gleichen Soundchip wie die HiFiBerry DAC/DAC+ Light, deshalb verwende ich das fur HifiBerry optimierte Image von Max2Play. Da ich keine der sonst angebotenen Features benotige, komme ich auch ohne Lizenz aus.

Wenn der Download abgeschlossen ist, [spielen wir das Image auf](http://indibit.de/raspberry-pi-meine-standardkonfiguration/#Installation).

Wer wie ich einen Raspberry Pi Zero benutzt, hat nun erstmal das Problem, dass dieser keinen LAN-Port besitzt und WLAN erst noch konfiguriert werden muss. Dafur gibt es verschieden-einfache Wege:

  1. Falls der WLAN-Stick eine WPS-Taste besitzt, kann die WPS-Funktion von Max2Play genutzt werden.
  2. Die SD-Karte in einen normalen Raspberry Pi stecken, diesen per Kabel ins Netzwerk holen, die WLAN-Einstellungen vornehmen, und die Karte dann in den Pi Zero packen.
  3. Den Pi Zero zusammen mit einem USB-Hub, sowie WLAN-Stick, Tastatur und/oder Maus an einen Bildschirm anschließen und die Daten direkt einstellen.

Fur mich ist Variante 2 die einfachste, und mit der geht es auch weiter.

Die Einstellungen nehmen wir per Weboberflache vor. Diese ist in der Regel unter [max2play.local](http://max2play.local) zu erreichen. Alternativ findet Ihr die IP-Adresse uber den Router. Anschließend navigieren wir zum Menupunkt „WLAN & LAN", geben SSID und Passwort des Netzwerkes ein, oder nutzen die Scan-Funktion.

![Max2Play: WLAN-Einstellungen](https://i0.wp.com/indibit.de/wp-content/uploads/2016/10/ls_m2p01_wifi.png?resize=560%2C360)

> _Max2Play: WLAN-Einstellungen_

In dem von mir verwendeten HifiBerry-Image kann man direkt auf der Startseite den entsprechenden Typen der Soundkarte auswahlen.

![Max2Play: HifiBerry-Karte auswählen](https://i2.wp.com/indibit.de/wp-content/uploads/2016/10/ls_m2p02_dac.png?resize=560%2C360)

> _Max2Play: HifiBerry-Karte auswahlen_

Im Standardimage wird die Soundkarte unter dem Menupunkt „Raspberry Einstellungen" ausgewahlt, sofern man eine Lizenz besitzt. Besitzt man diese nicht, kann man unter dem Menupunkt „Audioplayer" lediglich zwischen den vorkonfigurierten wahlen. Alternativ konnen Soundkarten per Kommandozeile eingestellt werden. Dafur benotigt man keine Lizenz.

`$ sudo nano /boot/config.txt`

Am Ende der Datei kann per dtoverlay die Soundkarte eingestellt werden. Bei meiner sahe das so aus:

Als nachstes geben wir dem WLAN-Lautsprecher einen vernunftigen Namen, mit dem er dann auch im Logitech Media Server angezeigt wird. Dies geschieht im Menu „Einstellungen / Reboot". Hier konnen auch Sprache und Zeitzone eingestellt werden.

![Max2Play: Playernamen einstellen](https://i1.wp.com/indibit.de/wp-content/uploads/2016/10/ls_m2p03_name.png?resize=560%2C360)

> _Max2Play: Playernamen einstellen_

Beim Benennen des Players wird gleichzeitig auch der Hostname angepasst. Mir personlich gefallt das nicht so gut, deshalb werde ich diesen spater nochmal uber die Kommandozeile anpassen.

Dann noch das obligatorische Expandieren des Dateisystems. Die passende Schaltflache befindet sich auf der gleichen Seite etwas weiter unten.

![Max2Play: Dateisystem expandieren](https://i0.wp.com/indibit.de/wp-content/uploads/2016/10/ls_m2p04_exp-ds.png?resize=560%2C360)

> _Max2Play: Dateisystem expandieren_

Fur die Steuerung unseres WLAN-Lautsprechers per Apple Remote (oder einer anderen Fernbedienung) und das Abschalten des Verstarkers, wenn dieser nicht benotigt wird, mussen wir auf der Kommandozeile noch ein paar Einstellungen vornehmen. Dazu [verbinden wir uns per SSH](http://indibit.de/ssh-ein-paar-grundlagen/) und loggen uns mit dem Benutzernamen `pi` und dem Passwort `raspberry` ein.

Optional: Bei Bedarf das Passwort andern:

`$ sudo passwd pi`

Optional: Um dem Raspberry Pi einen anderen Hostname zu geben, begeben wir uns uber die aktive SSH-Verbindung in die Konfigurationsoberflache…

`$ sudo raspi-config`

…wahlen `9 Advanced Options` -> `A2 Hostname` und tragen hier den neuen Hostname ein. Wir verlassen die Oberflache und starten neu.

Über das Thema LIRC, und wie man Python-Scripte mittels Fernbedienung steuert, hatte ich [hier](http://indibit.de/raspberry-pi-mit-apple-remotelirc-python-scripte-steuern/) schon einmal sehr ausfuhrlich geschrieben. Daher machen wir hier einen Schnelldurchlauf. Zuerst installieren wird LIRC:

`$ sudo apt-get update`

`$ sudo apt-get install lirc python-lirc`

Nach Abschluss der Installation machen wir uns an die Konfiguration. Als erstes der „Autostart" von LIRC.

`$ sudo nano /etc/modules`

Die markierten Zeilen werden einfach unten angehangen.

123456789
`# /etc/modules: kernel modules to load at boot time.``#``# This file contains the names of kernel modules that should be loaded``# at boot time, one per line. Lines beginning with "#" are ignored.``# Parameters can be specified after the module name.``lirc_dev``# GPIO in BCM-Zahlweise``lirc_rpi gpio_in_pin=23`

Auf Zeile 9 geben wir in BCM-Zahlweise an, welchen GPIO wir mit LIRC nutzen wollen - also die GPIO-Nummer, nicht die Pin-Nummer. Danach passen wir die Hardware-Konfiguration von LIRC an.

`$ sudo nano /etc/lirc/hardware.conf`

Hier tragen wir fur `LIRCD_ARGS`, `DRIVER`, `DEVICE` und `MODULES` die Werte wie abgebildet ein.

1234567891011121314151617181920212223
`# /etc/lirc/hardware.conf``#``# Arguments which will be used when launching lircd``LIRCD_ARGS=``"\--uinput"``#Don't start lircmd even if there seems to be a good config file``#START_LIRCMD=false``#Don't start irexec, even if a good config file seems to exist.``#START_IREXEC=false``#Try to load appropriate kernel modules``LOAD_MODULES=``true``# Run "lircd --driver=help" for a list of supported drivers.``DRIVER=``"default"``# usually /dev/lirc0 is the correct setting for systems using udev``DEVICE=``"/dev/lirc0"``MODULES=``"lirc_rpi"``# Default configuration files for your hardware if any``LIRCD_CONF=``""``LIRCMD_CONF=``""`

Zuletzt mussen wir noch einen Eintrag in der Datei `/boot/config.txt` erganzen.

`$ sudo nano /boot/config.txt`

Hier passen wir Zeile 51 wie folgt an:

Wer eine andere Fernbedienung als die Apple Remote nutzen mochte, startet den Raspberry Pi jetzt neu und macht an [dieser Stelle](http://indibit.de/raspberry-pi-mit-apple-remotelirc-python-scripte-steuern/#Tasten-Mappingfuer_die_Fernbedienung_erzeugen_lircdconf) weiter. Alle mit Apple Remote konnen mein Tasten-Mapping einfach ubernehmen.

`$ sudo nano /etc/lirc/lircd.conf`

Die Datei befullen wir, je nach verwendetem IR-Empfanger, mit folgendem Inhalt:

12345678910111213141516171819202122232425262728293031323334353637383940414243
`# Please make this file available to others``# by sending it to <lirc@bartelmus.de>``#``# this config file was automatically generated``# using lirc-0.9.0-pre1(default) on Tue Aug 18 19:23:09 2015``#``# contributed by``#``# brand:                       /home/pi/lircd.conf``# model no. of remote control:``# devices being controlled by this remote:``begin remote``name  appleremote``bits            8``flags SPACE_ENC|CONST_LENGTH``eps            30``aeps          100``header       9058  4422``one           624  1595``zero          624   497``ptrail        623``repeat       9058  2194``pre_data_bits   16``pre_data       0x77E1``post_data_bits  8``post_data      0x4E``gap          107798``toggle_bit_mask 0x0``begin codes``KEY_UP                   0xD0``KEY_DOWN                 0xB0``KEY_LEFT                 0x10``KEY_RIGHT                0xE0``KEY_OK                   0xBA 0x20``KEY_MENU                 0x40``KEY_PLAYPAUSE            0x7A 0x20``end codes``end remote`

12345678910111213141516171819202122232425262728293031323334353637383940414243
`# Please make this file available to others``# by sending it to <lirc@bartelmus.de>``#``# this config file was automatically generated``# using lirc-0.9.0-pre1(default) on Sun Oct 16 17:40:15 2016``#``# contributed by``#``# brand:                       /home/pi/lircd.conf``# model no. of remote control:``# devices being controlled by this remote:``begin remote``name  appleremote``bits            8``flags SPACE_ENC|CONST_LENGTH``eps            30``aeps          100``header       9057  4419``one           600  1616``zero          600   525``ptrail        600``repeat       9058  2190``pre_data_bits   16``pre_data       0x77E1``post_data_bits  8``post_data      0x4E``gap          107804``toggle_bit_mask 0x0``begin codes``KEY_UP                   0xD0``KEY_DOWN                 0xB0``KEY_LEFT                 0x10``KEY_RIGHT                0xE0``KEY_OK                   0xBA 0x20``KEY_MENU                 0x40``KEY_PLAYPAUSE            0x7A 0x20``end codes``end remote`

Damit beim Tastendruck auch etwas passiert, werden Aktionen definiert. In unserem Fall wollen wir lediglich die Information, welche Taste gedruckt wurde, per String an unser Steuer-Script ubergeben. Dazu erzeugen wir uns die Datei `lircrc` …

`$ sudo nano /etc/lirc/lircrc`

…und packen folgenden Inhalt rein:

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556
`# ~/.lircrc``#``# button: Name der Taster (wie angelernt)``# prog:   Ziel, wohin die Information ubergeben werden soll (Socket oder Programm)``# config: Übergebener String``# Apple Remote``# KEY_UP``# KEY_DOWN``# KEY_LEFT``# KEY_RIGHT``# KEY_OK``# KEY_MENU``# KEY_PLAYPAUSE``begin``button = KEY_UP``prog = appleremote``config = KEY_UP``end``begin``button = KEY_DOWN``prog = appleremote``config = KEY_DOWN``end``begin``button = KEY_LEFT``prog = appleremote``config = KEY_LEFT``end``begin``button = KEY_RIGHT``prog = appleremote``config = KEY_RIGHT``end``begin``button = KEY_OK``prog = appleremote``config = KEY_OK``end``begin``button = KEY_MENU``prog = appleremote``config = KEY_MENU``end``begin``button = KEY_PLAYPAUSE``prog = appleremote``config = KEY_PLAYPAUSE``end`

Damit ist LIRC fertig eingerichtet und der WLAN-Lautsprecher soweit vorbereitet. Sollte es spater irgendwelche Probleme mit LIRC geben, findet Ihr in oben genanntem Beitrag auch Moglichkeiten, die Teilschritte einzeln zu testen.

Zum Abschluss starten wir den Raspberry Pi neu.

## Steuerscript fur den WLAN-Lautsprecher

Damit die Fernbedienung den WLAN-Lautsprecher steuern kann und der Verstarker beim Abspielen von Musik auch eingeschaltet wird, benotigen wir noch ein Script, das mit dem Server kommuniziert und die entsprechenden Informationen besorgt, bzw. weiterleitet. Eins auf diesen Lautsprecher zugeschnittenes findet Ihr unten. Vom Grunde her konnt Ihr das Script auch 1:1 ubernehmen.

Wir erzeugen also die Script-Datei…

`$ nano ~/squeezebox-control.py`

…und packen folgenden Inhalt hinein:

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151152153154155156157158159160161162163164165166167168169170171172173174175176177178179180181182183184185186187188189190191192193194195196197198199200201202203204205206207208209210211212213214215216217218219220221222223224225226227228229230231232233
`#!/usr/bin/env python``#coding: utf-8 ``####################################################################``# squeezebox-control.py``# Script zur Steuerung eines WLAN-Lautsprechers``# von Sebastian Kohler - <http://indibit.de>``#``# LETZTE ÄNDERUNG:    17.04.2016``####################################################################``import` `fcntl, socket, struct    ``# fur MAC-Adresse``import` `lirc``import` `RPi.GPIO as GPIO``import` `sys``import` `telnetlib``import` `thread``import` `time``# ----------------------------------------------------------------------------``#  Konfiguration``# ----------------------------------------------------------------------------``HOST            ``=` `"192.168.243.5"` `# IP-Adresse des LMS``PORT            ``=` `"9090"` `# CLI-Port des LMS``OFF_DELAY       ``=` `180` `# Verstarker-Abschalt-Verzogerung (in Sekunden)``VOL_NORM        ``=` `50` `# Lautstarke, die nach beim Einschalten eingestellt werden soll``# ----------------------------------------------------------------------------``#  sonstige Variablen``# ----------------------------------------------------------------------------``mac ``=` `''       ``# MAC-Adresse``status ``=` `''    ``# Status des Players``tn ``=` `''        ``# Telnet-Verbindung``lastPlay ``=` `0` `# Zeit, wann der Player das letzte Mal gespielt hat``# ----------------------------------------------------------------------------``#  MAC-Adresse auslesen``# ----------------------------------------------------------------------------``def` `getMAC(ifname):``s ``=` `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)``info ``=` `fcntl.ioctl(s.fileno(), ``0x8927``,  struct.pack(``'256s'``, ifname[:``15``]))``return` `'%3A'``.join([``'%02x'` `%` `ord``(char) ``for` `char ``in` `info[``18``:``24``]])``# ----------------------------------------------------------------------------``#  Telnet-Verbindung herstellen``# ----------------------------------------------------------------------------``def` `tn_connect():``global` `tn``try``:``tn ``=` `telnetlib.Telnet(HOST,PORT)``player(``"startup"``)``except``:``time.sleep(``10``)``# ----------------------------------------------------------------------------``#  WLAN-Lautsprecher bei Start initialisieren``# ----------------------------------------------------------------------------``def` `startup():``setGPIO(``"startup"``,"")``tn_connect()``# ----------------------------------------------------------------------------``#  Fernbedienung/LIRC abfragen``# ----------------------------------------------------------------------------``def` `remote():``while` `True``:``try``:``codeIR ``=` `lirc.nextcode()``if` `codeIR !``=` `[]:``if` `codeIR[``0``] ``=``=` `'KEY_UP'``:``player(``'vol_up'``)            ``elif` `codeIR[``0``] ``=``=` `'KEY_DOWN'``:``player(``'vol_down'``)``elif` `codeIR[``0``] ``=``=` `'KEY_LEFT'``:``player(``'back'``)``elif` `codeIR[``0``] ``=``=` `'KEY_RIGHT'``:``player(``'next'``)``elif` `codeIR[``0``] ``=``=` `'KEY_OK'``:``pass``elif` `codeIR[``0``] ``=``=` `'KEY_MENU'``:``player(``'playlist'``)``elif` `codeIR[``0``] ``=``=` `'KEY_PLAYPAUSE'``:``if` `status ``=``=` `"play"``:``player(``'pause'``)``else``:``player(``'play'``)``time.sleep(``0.05``)``except``:``time.sleep(``0.1``)``# ----------------------------------------------------------------------------``#  Befehle senden, Status abfragen``# ----------------------------------------------------------------------------``def` `player(cmd):``p0 ``=` `""``p1 ``=` `""``p2 ``=` `""``if` `cmd ``=``=` `"startup"``:``try``:``player(``"stop"``)``#tn.write("subscribe play,pause,stop,playlist\r")``tn.write(mac ``+` `" mode ?\r"``)``resetVol()``except` `(EOFError, socket.error):``tn_connect()``else``:``if` `cmd ``=``=` `"play"``:               ``# Wiedergabe``p0 ``=` `"play"``elif` `cmd ``=``=` `"pause"``:            ``# Pause``p0 ``=` `"pause"``elif` `cmd ``=``=` `"stop"``:             ``# Stop``p0 ``=` `"stop"``elif` `cmd ``=``=` `"back"``:             ``# Titel zuruck``p0 ``=` `"playlist"``p1 ``=` `"index"``p2 ``=` `"-1"``elif` `cmd ``=``=` `"next"``:             ``# Titel uberspringen``p0 ``=` `"playlist"``p1 ``=` `"index"``p2 ``=` `"%2B1"``elif` `cmd ``=``=` `"vol_up"``:           ``# Lauter``p0 ``=` `"mixer"``p1 ``=` `"volume"``p2 ``=` `"%2B5"``elif` `cmd ``=``=` `"vol_down"``:         ``# Leiser``p0 ``=` `"mixer"``p1 ``=` `"volume"``p2 ``=` `"-5"``elif` `cmd ``=``=` `"playlist"``:         ``# Playlist abspielen``p0 ``=` `"playlist"``p1 ``=` `"play"``p2 ``=` `"smooth_jazz.m3u"``else``:``p0 ``=` `""``p1 ``=` `""``p2 ``=` `""``if` `p0 !``=` `"":``try``:``tn.write(mac ``+` `" "` `+` `p0 ``+` `" "` `+` `p1 ``+` `" "` `+` `p2 ``+` `"\r"``)``except` `(EOFError, socket.error):``tn_connect()``p0 ``=` `""``p1 ``=` `""``p2 ``=` `""``def` `getStatus():``while` `True``:``global` `status``try``:``tn.write(mac ``+` `" mode ?\r"``)``q ``=` `tn.read_until(``'\r'``)``s ``=` `q.split(``'\r'``)[``0``].split(``' '``)``if` `s:``if` `s[``0``] ``=``=` `mac:``if` `s[``1``] ``=``=` `"mode"``:``status ``=` `s[``2``]``except` `(EOFError, socket.error):``tn_connect()``except` `KeyboardInterrupt:``getOut()``time.sleep(``0.1``)``# ----------------------------------------------------------------------------``#  Verstarker am WLAN-Lautsprecher ein-/ausschalten``# ----------------------------------------------------------------------------``def` `ampOnOff():``global` `lastPlay``if` `status ``=``=` `"play"``:``setGPIO(``"amp"``,``"on"``)``lastPlay ``=` `time.time()``else``:``if` `time.time() ``-` `lastPlay >``=` `OFF_DELAY:``if` `status ``=``=` `"pause"``:``resetVol()``player(``"stop"``)``setGPIO(``"amp"``,``"off"``)``def` `setGPIO(channel,state):``amp ``=` `22``on  ``=` `GPIO.LOW``off ``=` `GPIO.HIGH``if` `channel ``=``=` `"startup"``:``GPIO.output(``22``, GPIO.HIGH)``#GPIO.output(24, GPIO.HIGH)``else``:``if` `(channel ``in` `locals``()) ``and` `(state ``in` `locals``()):``GPIO.output(``locals``()[channel], ``locals``()[state])``# ----------------------------------------------------------------------------``#  Standard-Lautstarke setzen``# ----------------------------------------------------------------------------``def` `resetVol():``try``:``tn.write(mac ``+` `" mixer volume "` `+` `str``(VOL_NORM) ``+` `" \r"``)``except` `(EOFError, socket.error):``tn_connect()``# ----------------------------------------------------------------------------``#  Script beenden``# ----------------------------------------------------------------------------``def` `getOut():``GPIO.cleanup()``sys.exit(``0``)``# ----------------------------------------------------------------------------``#  Hauptprogramm``# ----------------------------------------------------------------------------``if` `__name__ ``=``=` `'__main__'``:``#GPIO.setwarnings(False)``GPIO.setmode(GPIO.BOARD)                            ``# Zahlweise der Pins festlegen``GPIO.setup(``22``, GPIO.OUT)                            ``# Pin 22 (GPIO 25) = Verstarker-Relais 1``#GPIO.setup(24, GPIO.OUT)                           # Pin 24 (GPIO  8) = Verstarker-Relais 2``sockid``=``lirc.init(``"appleremote"``, blocking ``=` `False``)   ``# Fernbedienung einbinden``mac ``=` `getMAC(``'wlan0'``)``startup()``thread.start_new_thread(getStatus,())``thread.start_new_thread(remote,())``while` `True``:``try``:``ampOnOff()``n ``=` `True``time.sleep(``0.1``)``except` `KeyboardInterrupt:``getOut()`

Auf den Zeilen 23 bis 26, und 133 musst Ihr die fur Euch zutreffenden Daten eintragen.

  * Zeile 23 (`HOST`): Die IP-Adresse des Computers/NAS ein, auf dem der Logitech Media Server lauft.
  * Zeile 24 (`PORT`): Der Port fur die Steuerung per Telnet. Den Findet Ihr so heraus: Im LMS -> Einstellungen -> Erweitert -> Befehlszeilenschnittstelle (CLI) [oben links im Dropdown-Menu auswahlen].
  * Zeile 25 (`OFF_DELAY`): Zeit, die verstreichen muss, bis der Verstarker abgeschaltet wird, wenn die Wiedergabe pausiert wird.
  * Zeile 26 (`VOL_NORM`): Lautstarke die automatisch eingestellt wird, wenn der Verstarker sich ausschaltet (STOP) oder bei Neustart des Raspberry Pi, bzw. LMS
  * Zeile 133: Hier konnt Ihr eine Playlist festlegen, die beim Drucken auf die Menu-Taste an der Apple-Remote abgespielt wird.

Die Tasten auf der Fernbedienung sind in diesem Script wie folgt belegt:

  * hoch/runter: lauter/leiser
  * links/rechts: nachster/vorheriger Titel
  * Mitte: nicht belegt
  * Menu: spielt voreingestellte Playlist ab
  * Play/Pause: befindet sich der Player im Ruhezustand, wird das abgespielt, was zuletzt wiedergegeben wurde. Pause pausiert, anschließend Play setzt die Wiedergabe fort

Das Script muss noch ausfuhrbar gemacht…

`$ chmod +x ~/squeezebox-control.py`

…und dem Autostart hinzugefugt werden, sodass es auch nach Stromausfall oder Neustart wieder lauft:

`$ sudo nano /etc/rc.local`

Hier fugen wir ganz unten, vor `exit 0`, folgende Zeilen ein:

Nach einem letzten Neustart ist der WLAN-Lautsprecher nun vollstandig betriebsbereit. Viel Spaß
