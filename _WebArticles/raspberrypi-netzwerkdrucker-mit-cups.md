# RaspberryPi: Netzwerkdrucker mit CUPS

_Captured: 2017-08-04 at 22:31 from [www.gehaxelt.in](http://www.gehaxelt.in/blog/raspberrypi-netzwerkdrucker-mit-cups/)_

In dem folgenden Blogpost mochte ich erklaren, wie man aus einem RaspberryPi und einem Drucker, einen Netzwerkdrucker bastelt.

### CUPS installieren

Cups ist ein Druckserver, welchen wir zur Verwaltung der Drucker nutzen werden.

Diese installieren wir zunachst auf unserem RaspberryPi:
    
    
    sudo apt-get update && sudo apt-get install cups
    

Das sind dann erstmal eine Menge Pakete und dauert eine kleine Weile.

### Benutzer fur Administration anlegen

Damit wird dann spater Cups uber die Weboberflache administrieren konnen, mussen wir uns zunachst in die Gruppe "lpadmin" hinzufugen.
    
    
    sudo usermod -aG lpadmin pi
    

Es bietet sich außerdem an, einen extra Druck-Benutzer anzulegen:
    
    
    1
    2
    3
    
    
    
    sudo useradd -c Druckuser -M -s /bin/false Drucker
    sudo usermod -aG lpadmin Drucker
    sudo passwd Drucker

Die Option "-M" legt dem Benutzer kein Homeverzeichnis an; die Option "-s /bin/false" verhindert das Einloggen auf der Shell, sodass das Passwort nicht sehr stark sein muss. (Gut fur die Familie zum Merken) "-c Druckuser" ist einfach nur ein Kommentar.

### CUPS konfigurieren

Die Konfigurationsdatei unter /etc/cups/cupsd.conf mussen wir noch ein wenig anpassen.

Da ich den Pi "headless", also ohne grafische Oberflache laufen lasse, muss ich auf das Webpanel von außerhalb des Pis zugreifen konnen.

Dazu lassen wir es auf allen Netzwerkschnittstellen lauschen. Weiter oben in der Konfiguration sollten die "Listen"-Eintrage folgendermaßen abgeandert werden:
    
    
    1
    2
    
    
    
    Listen /var/run/cups/cups.sock
    Port 631

Die Zeile
    
    
    Listen localhost:631
    

wird entfernt.

Das WebInterface sollte auf "Yes" gestellt werden, und die Location-Eintrage folgendermaßen angepast:
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    
    
    
    # Web interface setting...
    WebInterface Yes
    
    # Restrict access to the server...
    <Location />
      Order allow,deny
      Allow from 192.168.2.*
      Require user @SYSTEM
    </Location>
    
    # Restrict access to the admin pages...
    <Location /admin>
      Order allow,deny
      Allow from 192.168.2.*
      Require user @SYSTEM
    </Location>
    
    <Location /classes>
            Order allow,deny
            Allow from 192.168.2.*
            Require user @SYSTEM
    </Location>
    
    <Location /help>
            Order allow,deny
            Allow from 192.168.2*
            Require user @SYSTEM
    </Location>
    
    <Location /jobs>
            Order allow,deny
            Allow from 192.168.2.*
            Require user @SYSTEM
    </Location>
    
    <Location /printers>
            Order allow,deny
            Allow from 192.168.2.*
            #Require user @SYSTEM #Sollte auskommentiert werden, damit Windows den Server findet
    </Location>
    
    
    # Restrict access to configuration files...
    <Location /admin/conf>
      AuthType Default
      Require user @SYSTEM
      Order allow,deny
      Allow from 192.168.2.*
    </Location>
    

Ich nehme an, dass ihr euch im Netz "192.168.2.*" befindet. Die 3. Stelle ist je nach Router unterschiedlich und sollte angepasst werden.

Mit dieser Konfiguration erlauben wir den Zugriff vom gesamten Klasse C Netz, mit der Einschrankung, dass sich die Benutzer anmelden mussen.

Dies konnen wir entweder mit dem Pi-Benutzer und seinem Passwort, oder mit dem erstellten Drucker-Benutzer machen.

Zuletzt CUPS noch neustarten:
    
    
    sudo /etc/init.d/cups restart
    

### Feste IP fur den Pi

Es ist sehr zu empfehlen, wenn nicht sogar notwendig, dass der Pi in dem Heimnetz eine feste IP zugewiesen bekommt.

Dies erreichen wir, in dem wir in /etc/network/interfaces eine statische IP festlegen:
    
    
    1
    2
    3
    4
    5
    6
    7
    
    
    
    auto eth0
    iface eth0 inet static
    address 192.168.2.93
    netmask 255.255.255.0
    network 192.168.2.0
    broadcast 192.168.2.255
    gateway 192.168.2.1

Die Angaben konnen bei euch je nach Router/IP-Bereich abweichen und mussen selbst angegeben werden.

Nach diesem Schritt sollten wir networking neustarten:
    
    
    sudo /etc/init.d/networking restart
    

### Drucker anschließen

Nun konnt ihr, falls ihr es noch nicht habt, den Drucker via USB an den Pi anstecken.

Danach geht ihr auf die Webseite von Cups:
    
    
    http://[IPvomPI]:631/admin
    

Ihr werdet euch anmelden mussen.

Ihr folgt dann den Schritten zum Hinzufugen eines Druckers und wahlt dann dort euren Drucker, welcher an den Pi angeschlossen ist, aus.

Zusatzlich muss die Option "Freigabe" bzw. "Shared" angewahlt werden, da sonst der Drucker spater nicht im Netzwerk auffindbar wird.

Ihr solltet nach Moglichkeit den genauen Treiber (ppd) in der Auswahl auswahlen, oder im Internet suchen und hochladen, damit der Drucker richtig funktionieren kann.

Damit sollte die Konfiguration beim Pi beendet sein.

### Drucker bei den Clients einrichten

Nun musst ihr nur noch den Drucker bei den Clients einrichten.

#### Linux

Unter Linux solltet ihr in eurer /etc/hosts Datei einen neuen Eintrag anlegen, der so ahnlich aussieht:
    
    
    192.168.2.93 raspberrypi.local raspberrypi
    

Dann installiert ihr CUPS, falls noch nicht vorhanden, auf eurem eigenen System. Eine feste IP, sowie die Erreichbarkeit des Webpanels nach Außen ist hier nicht notwendig.

Beim hinzufugen des Druckers sollte bei "Entdeckte Netzwerkdrucker:" bzw. "Discovered Network Printers:" der eben erstellte Drucker auf dem RaspberryPi erscheinen.

Diesen wahlt ihr dann als Ziel aus, und folgt den weiteren Schritten bis zum Ende. Dieser lokale Drucker sollte **nicht** freigegeben werden.

Nachdem ihr wieder den entsprechenden Treiber ausgewahlt bzw. hochgeladen habt, solltet ihr in der Lage sein, eine Datei aus dem Kontextmenu eines Programs zu Drucken.

Ihr wahlt dabei dort den lokalen Drucker aus, welche dann die Daten uber das Netzwerk an den Pi schickt.

### Windows

Unter Windows geht man einfach in die Systemsteuerung und sucht nach der Option "Drucker hinzufugen".

Dann wahlt man die Option "Netzwerkdrucker", und lasst Windows mal suchen. Bei mir scheiterte die Suche immer, sodass man ggf. auch gleich zur manuellen Eingabe wechseln kann.

Dort wahlt man die Option "URL bzw. Netzwerkpfad" (oder so ahnlich) und gibt dann die URL zum Printer an. Diese ist einfach die URL, ohne SSL, des Druckers in der Übersicht.

Zum Beispiel:
    
    
    http://192.168.2.93:631/printers/Samsung_SCX-4300_Series
    

Dann sollte Windows den Drucker erfolgreich finden.

**_Achtung: In manchen Fallen muss der Drucker angeschaltet sein, damit CUPS diesen als "aktiv" listet, und Windows ihn annimmt._**

Ein weiterer Klick auf "Fertigstellen" und der Drucker ist eingerichtet.

### Update: CUPS Drucker reaktivieren

Es gibt eine Moglichkeit, wie ihr Druckauftrage an einen ausgeschalteten Drucker schicken konnt. D.h. Ihr startet den Druckauftrag, und geht dann erst zum Drucker, um ihn einzuschalten.

Ihr musst dazu zwei Anpassungen (am Pi) treffen:

  1. In der /etc/cups/cupsd.conf die folgenden Zeilen anfugen:
    
    
    1
    2
    
    
    
    JobRetryInterval 15
    JobRetryLimit 40

Das probiert den Auftrag alle 15 Sekunden, maximal 40 Mal zu wiederholen. Man hat also rund 10 Minuten Zeit, den Drucker zu starten.

  1. In der /etc/cups/printers.conf die folgende Option setzen:

Zunachst aber cups stoppen mit
    
    
    sudo /etc/init.d/cups stop
    

Und danach die Option
    
    
    ErrorPolicy retry-job
    

setzen.

Danach cups einfach wieder neustarten:
    
    
    sudo /etc/init.d/cups start
    

Nun konnt ihr den Drucker testweise mal ausschalten. Einen Druckauftrag aufgeben, und nach einer Weile den Drucker starten.

Die Seite sollte dann wenige Sekunden spater gedruckt werden.

### Fazit

Ihr solltet nun in der Lage sein, uber das Netzwerk zu drucken.

Gruß

gehaxelt
