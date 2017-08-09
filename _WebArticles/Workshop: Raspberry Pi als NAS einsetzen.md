# Workshop: Raspberry Pi als NAS einsetzen

_Captured: 2015-12-25 at 10:16 from [www.tecchannel.de](http://www.tecchannel.de/pc_mobile/peripherie/2057273/workshop_mikrocomputer_raspberry_pi_als_nas_einsetzen/)_

An [NAS](http://www.tecchannel.de/storage/nas/)-Netzwerkspeichern (Network Attached Storage), die mit Linux reibungslos zusammenarbeiten, herrscht kein Mangel. Und die im Handel angebotenen Losungen stellen eine Menge zusatzlicher Funktionen zur Verfugung. Ob diese auch alle benotigt werden, steht auf einem ganz anderen Blatt. Wer in einer Schublade eine USB-Festplatte herumliegen hat und gerne bastelt, stellt sich ein individuelles NAS fur knapp 60 Euro zusammen. Moglich wird dies durch den inzwischen millionenfach verkauften Einplatinen-Computer Raspberry Pi.

### **Vorab: **

In Sachen Übertragungsgeschwindigkeit kann das System mit den Profilosungen aus dem Fachhandel nicht ganz mithalten. Dies liegt weniger an der Ausstattung an Arbeitsspeicher oder der Prozessorgeschwindigkeit, sondern vielmehr an der Beschrankung der aufgeloteten [Ethernet](http://www.tecchannel.de/netzwerk/lan/)\- Buchse. Wahrend NAS-Boxen im Handel mit Gigabit-Schnittstellen protzen, ist auf der Platine ein 100-MBit-Anschluss integriert. Andererseits werden Sie kein System finden, das Ihren Geldbeutel beim Stromverbrauch ahnlich schont. Der Rechner verbraucht rund 3,5 Watt, dazu kommt dann noch der Verbrauch einer angeschlossenen externen Festplatte. Selbst bei großzugiger Kalkulation verbrauchen Sie nur ein Viertel des Stroms, den ein kommerzielles NAS benotigt.

### Die Einkaufsliste

Was brauchen Sie, um loszulegen? Zunachst einmal das Board. Das Raspberry Pi in der Revision B kostet im Handel rund 40 Euro (39,95 € etwa bei [www.conrad.de](http://www.conrad.de/)). Es verfugt uber 512 MB an RAM, besitzt eine Ethernet- Schnittstelle und zwei USB-Ports. Wenn Sie der Platine etwas Gutes tun und vor dem Einstauben schutzen wollen, kaufen Sie zusatzlich noch ein passendes Kunststoffgehause. Technisch notwendig ist das allerdings nicht. Solche durchsichtigen Boxen gibt es fur 10 bis 25 Euro (die schicke Raspbox bei [www.yoctopuce.com](http://www.yoctopuce.com/) fur 12 Euro plus relativ hohe Versandkosten). Strom bezieht der **Raspberry** uber den Mikro-USB-Anschluss. Dort mussen funf Volt anliegen. Besitzen Sie ein [Handy](http://www.tecchannel.de/kommunikation/handy_pda/)-Ladegerat mit der notwendigen Leistung, das Sie nicht benotigen, konnen Sie dieses verwenden. Andernfalls mussen Sie ein solches Ladegerat beim Einkauf berucksichtigen.

Unbedingt notig ist ferner eine SDKarte, auf der Sie das Betriebssystem unterbringen. Vier GB genugen hier. Generell konnten Sie den Taschencomputer vollstandig uber einen Remote-Zugang konfigurieren und pflegen. Wem das nicht liegt, benotigt eine externe Tastatur, die sich per USB anschließen lasst, außerdem einen Monitor, der mittels eines HDMI-Kabels mit dem Computer verbunden werden kann. Schließlich ist fur die Nutzung als NAS naturlich externer Datenspeicher erforderlich, also eine USB-Festplatte oder ein groß dimensionierter USB-Stick.

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2389047/522x294.png)

> _Raspberry Pi als Arcade-Automat_

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2389048/522x294.png)

### Das sollten Sie wissen

In diesem Artikel geht es in erster Linie um die grundlegende Konfiguration der Hardware und des Betriebssystems, damit aus dem Kleinstcomputer ein NAS wird. Sie sollten bereits Erfahrungen mit der Einrichtung von Nutzern und Nutzergruppen unter Linux gesammelt haben, damit spater auch nur die berechtigten Personen auch Daten auf dem System ansehen konnen. Damit das funktioniert, muss das Paket "acl" auf dem System installiert werden. Die Benutzung des Befehls _adduser_und die Vorlagendatei "adduser.conf" spielen ebenfalls eine Rolle.

### Die Erstkonfiguration

Damit Sie Ihr [NAS](http://www.tecchannel.de/storage/nas/) in Betrieb nehmen konnen, braucht der Computer ein Betriebssystem. Inzwischen gibt es eine Reihe von Linux-Derivaten, die Sie verwenden konnen. Besuchen Sie dazu die Seite [www.raspberrypi.org/downloads](http://www.raspberrypi.org/downloads). In diesem Beispiel wird die spezielle Debian-Version fur den Kleinst-Computer verwendet. Laden Sie sich die ISO-Datei (Raspbian Wheezy) auf Ihren Rechner. Wahrend das ZIP-Archiv heruntergeladen wird, mussen Sie erst einmal herausfinden, unter welchem internen Namen Ihr Linux eine eingelegte SD-Karte anspricht. Dazu benotigen Sie ein Terminal. Dort geben Sie ein:

`sudo ls /dev/sd*`

Nach der Eingabe des Systemkennworts erhalten Sie von Ihrem Computer eine Reihe von Kurzeln angeboten. Legen Sie jetzt die Speicherkarte ein, warten Sie einen Moment, und fuhren Sie das Kommando erneut aus. Die Liste der Eintrage sollte jetzt langer sein. Wahrscheinlich werden Sie dort jetzt einen zusatzlichen Wert "/dev/sdb1" bemerken.

Um das OS auf die SD-Karte kopieren zu konnen, darf der Datentrager nicht eingehangt sein. Im Terminal geben Sie daher

`sudo umount /dev/sdb1`

ein. Passen Sie "sdb1" an das bei Ihnen verwendete Laufwerkskennung-Kurzel an. Nachdem der Download abgeschlossen ist, klicken Sie im Dateimanager doppelt auf das ZIP-Archiv. Im Archivmanager markieren Sie die IMGDatei und klicken auf "Entpacken". Danach wahlen Sie einen Ordner aus, in den Sie die Datei kopieren wollen.

Jetzt kopieren Sie das Image auf die SD-Karte, damit das Raspberry Pi damit gestartet werden kann. Dieser Vorgang kann etwas dauern, immerhin mussen einige Gigabyte auf die Karte geschaufelt werden. Dabei erhalten Sie keine Anzeige uber den Fortschritt - also einfach abwarten, bis Sie wieder auf der Kommandozeile landen.

Das Kopieren ubernimmt das Kommando "dd". Sie brauchen fur die Arbeit root Rechte. Vor allen Dingen mussen Sie sorgfaltig arbeiten, damit Sie nicht aus Versehen einen anderen Datentrager uberschreiben und damit Ihr System beschadigen. Im Terminal geben Sie dann _sudo dd if=Speicherort.img of=/dev/Kurzel_SD_Karte_ein, also in einem konkreten Beispiel:

`sudo dd if=/home/sla/2013-09-25-wheezy-raspbian.img of=/dev/sdb1`

Wenn das Betriebssystem auf die SDKarte kopiert wurde, konnen Sie sich an die Starvorbereitungen machen. Legen Sie die SD-Karte in den Raspberry Pi ein, verbinden Sie die Tastatur mit dem USB-Port, den Monitor uber HDMI und das Netzwerkkabel mit Ihrem [Router](http://www.tecchannel.de/netzwerk/lan/). Schalten Sie den Monitor ein. Verbinden Sie erst jetzt den Mikro-USB-Port mit einer Stromquelle, um den Computer zu starten.
### System starten und Zugang einrichten

Damit sollte das System starten und eine Reihe von Meldungen auf dem Bildschirm ausgeben. Am Ende gelangen Sie in den Dialog fur die Konfiguration des Systems ("raspi-config"). Aktivieren Sie dort zum einen die Option "Expand filesystem". Damit wird die Root-Partition auf die maximale Große geandert. Unter "Advanced" aktivieren Sie den Zugang per SSH. Das hat den großen Vorteil, dass Sie nicht standig einen Monitor an der Box anschließen mussen, sondern sich uber das eigene interne [Netzwerk](http://www.tecchannel.de/netzwerk/) mit dem Rechner verbinden konnen. Der Verzicht auf einen Monitor kommt auch der Energiebilanz des Systems zugute.

Besuchen Sie die Konfigurationsoberflache Ihres Routers (zum Beispiel der Fritzbox), und schauen Sie in den DHCP-Einstellungen nach, welche Clients angemeldet sind. Sie sollten dort den Raspberry PI mit einer IPAdresse finden. Wenn Sie sich Arbeit sparen wollen, konfigurieren Sie den DHCP-[Server](http://www.tecchannel.de/server/) des Routers so, dass der Raspberry immer die gleiche IP-Adresse zugewiesen bekommt. Jetzt konnen Sie versuchen, sich erstmals mit dem System zu verbinden. Starten Sie ein Terminal und geben Sie dort ein:

`ssh -l pi IP-Adresse`

Damit melden Sie den Nutzer pi am System ein. Sie mussen explizit mit "Yes" antworten, um die Verbindung fortzusetzen. Als Passwort nutzen Sie das voreingestellte "raspberry". Danach werden Sie vom Prompt des Systems begrußt.

Zur Einrichtung des Systems als [NAS](http://www.tecchannel.de/storage/nas/) benotigen Sie einige Programme. Aktualisieren Sie am besten zunachst die Paketquellen und das System. Wie unter Ubuntu nutzen Sie die folgenden beiden Kommandos auf dem entfernten System:

`sudo apt-get updatesudo apt-get upgrade`

### Externe Datentrager anschließen und vorbereiten

Ist das System auf dem neuesten Stand, konnen Sie an die Einrichtung der externen Festplatte gehen. Geben Sie zunachst das Kommando _ls /dev/_ein. Schließen Sie nun die externe Platte an, und verbinden Sie diese mit der Stromversorgung. Fuhren Sie dann das Kommando erneut aus: Damit ermitteln Sie, uber welchen Namen das System die Platte anspricht. Dies durfte in den meisten Fallen "/dev/sda" sein.

**Avahi und Netatalk:** Richtig konfiguriert erscheint der Raspberry Pi im Finder aller Macs im gleichen Netzwerk als externe Platte.

Geben Sie _sudo fdisk /dev/sda_ein. Mit Taste P sehen Sie sich an, welche Partitionen auf der Platte vorhanden sind. Am besten, Sie formatieren die externe Platte vollstandig neu. Drucken Sie zunachst Taste D, um eine vorhandene Partition zu loschen, danach Taste N, um eine neue Partition anzulegen. Anschließend belassen Sie es am besten mit den Vorgabewerten, bestatigen also immer nur mit der Enter-Taste. Dieser Partition spendieren Sie anschließend ein Dateisystem. Dazu genugt der Befehl

`sudo mkfs.ext4 /dev/sda1`

Jetzt mussen Sie nur noch dafur sorgen, dass die Platte automatisch nach dem Systemstart eingebunden wird. Im Falle einer USB-Platte mussen Sie dazu die sogenannte UUID herausfinden. Geben Sie den Befehl

`sudo blkid`

ein, und achten Sie bei der Ruckgabe auf die Ruckmeldung Ihrer Platte. Kopieren Sie dann die Zeichenfolge in Klammern. Nun offnen Sie im Editor Nano die Datei "fstab" (File System Table):

`sudo nano /etc/fstab`

In die Datei schreiben Sie dann als neuen Eintrag (Beispiel):

Speichern Sie die Datei, und starten Sie das System neu.
### Freigaben fur Windows- und Apple-Rechner

Sobald das automatische Mounten der externen Platte gelingt, haben Sie die meiste Arbeit bereits hinter sich. Nun geht es um das Einrichten der Freigaben: Wenn Sie per [Windows](http://www.tecchannel.de/pc_mobile/windows/)-Rechner auf freigegebene Verzeichnisse zugreifen wollen, mussen Sie einen Samba-[Server](http://www.tecchannel.de/server/) aufsetzen und einrichten. Lesen Sie dazu den Artikel "Netzwerken mit Samba" in diesem Heft, ab Seite 36. Um uber ein Apple-[Netzwerk](http://www.tecchannel.de/netzwerk/) auf freigegebene Verzeichnisse zugreifen zu konnen, installieren Sie die beiden Programmpakete "netatalk" und "avahi-daemon":

`sudo apt-get install avahi-daemonsudo apt-get install netatalk`

Nach erfolgreicher Installation offnen Sie mit dem Editor Nano die Konfigurationsdatei "afpd.conf" fur den Apple-Dienst:

`sudo nano /etc/netatalk/afpd.conf`

Tragen Sie dort die nachfolgende Zeile ein - die Position spielt keine Rolle, zumal in der Datei vermutlich keine weiteren Eintrage vorhanden sind.

\- -tcp -noddp -uamlist uams_dhx.so,uams_dhx2_passwd.so-nosavepassword

Speichern Sie die Datei. Öffnen Sie jetzt die Konfigurationsdatei fur die einzelnen Freigaben, die auf den Apple-Rechnern zu sehen sein sollen:

`sudo nano /etc/netatalk/AppleVolumes.default`

Tragen Sie dort vor der Zeile "End of File" folgendes ein (Beispiel):

`#Public folder/share/Public Public options:upriv perm:0776`

Damit haben Sie die Freigabe "Public" angelegt. Das Protokoll kennt noch eine Reihe von weiteren Optionen. Die Einzelheiten sind recht vollstandig etwa unter <http://wiki.ubuntuusers.de/netatalk> erklart.

Noch komfortabler wird das Ganze im Zusammenspiel mit dem Avahi- Daemon. Er publiziert eine Freigabe in einem Apple-Netz, so dass Mac-Computer schneller darauf zugreifen konnen. Dafur ist ein kleiner Eingriff in die Konfigurationsdatei "afpd.service" des Dienstes erforderlich:

`sudo nano /etc/avahi/services/afpd.service`

`<?xml version="1.0" standalone='no'?><!--*-nxml-*-->  
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">  
<service-group>  
<name replace-wildcards="yes">%h</name>  
<service>  
<type>_afpovertcp._tcp</type>  
<port>548</port>  
</service>  
</service-group>`

Nach dem Speichern starten Sie den Dateidienst und Avahi neu:

`sudo service avahi-daemon restartsudo service netatalk restart`

Wenige Augenblicke spater sollten alle Macs im Finder unter "Freigaben" den Raspberry sehen konnen. Die Kombination von Netatalk und Avahi erlaubt es auch, die am Raspberry Pi angeschlossenen Platten als Ziel fur das [Backup](http://www.tecchannel.de/storage/backup/) mit Time Machine zu nutzen.
### Erweitern durch zusatzliche Komponenten

Bislang gibt es keine auf dem Raspberry lauffahige Variante von Free [NAS](http://www.freenas.org/) oder [NAS4Free](http://www.nas4free.org/). Probleme bereitet unter anderem das ZFS-Dateisystem, das im auf BSD basierenden Betriebssystem fur Speicherboxen enthalten ist und nicht auf Debian und damit dem hier vorgestellten Derivat lauft.

Deswegen mussen viele der weiteren Moglichkeiten, die fertige [NAS](http://www.tecchannel.de/storage/nas/)-Systeme bereithalten, mit Hilfe von einzelnen Komponenten nachgerustet werden.

Die gezeigte Konfiguration eignet sich etwa auch als Medienserver. Dazu mussen Sie etwa das Paket "minidlna" auf dem System installieren und einrichten. Danach streamt der kleine Computer bei Bedarf Musik oder Videos direkt auch andere Gerate im Netz. Auch die Verwendung als Drucker-[Server](http://www.tecchannel.de/server/) ist nach einer Installation von Cups moglich.

### Schnellere Installation fur Windows-Nutzer

Wer noch ein zusatzliches [Windows](http://www.tecchannel.de/pc_mobile/windows/) im Einsatz hat, kann seine SD-Karte schneller zum Startmedium fur seinen Raspberry Pi machen. Besuchen Sie die Seite des Projekts, und laden Sie sich dort die Noobs-Edition auf Ihren Rechner.

Diese Out-of-the-Box-Version braucht nur auf die Karte kopiert zu werden und enthalt eine Auswahl von Distributionen und Programmen, die auf dem Winzig-Rechner laufen konnen. Dementsprechend geduldig mussen Sie allerdings wahrend der Übertragung sein. Denn immerhin mussen hier mehr als drei Gigabyte auf die Speicherkarte kopiert werden.

Unter _www.sdcard.org/downloads/formatter_4/_besorgen Sie sich inzwischen das Formatierungswerkzeug fur SD-Karten. Sie installieren es unter Windows wie gewohnt. Danach konnen Sie jederzeit mit wenigen Mausklicks eine SD-Karte formatieren. Ist dieser Schritt erfolgt, entpacken Sie das ZIP-Archiv von Noobs und kopieren den Inhalt auf die SD-Karte. Wenn Sie das Raspberry Pi damit booten, konnen Sie zwischen den angebotenen Distributionen jene auswahlen, welche Sie installieren wollen. Ist dieser Schritt erfolgt, verhalt sich der Mini-Computer genauso wie im Haupttext des Artikels beschrieben.
