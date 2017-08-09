# Print-Server mit CUPS und AirPrint auf dem Raspberry Pi einrichten

_Captured: 2017-08-04 at 22:32 from [www.elektronik-kompendium.de](https://www.elektronik-kompendium.de/sites/raspberry-pi/2007081.htm)_

_Mit Raspbian Jessie gepruft._

CUPS (Common Unix Printing System) ist ein auf mehreren Standards basierendes Open-Source-Drucksystem, welches fur Unix-artige Betriebssysteme entwickelt wurde und von Apple fur das Betriebssystem Mac OS X unterstutzt wird.  
Mit CUPS kann man einen Drucker-Server (Print-Server) im Netzwerk betreiben, an dem einer oder mehrere USB-Drucker angeschlossen und somit im Netzwerk erreichbar sind. Dafur eignet sich ein stromsparender Raspberry Pi besonders gut. CUPS berucksichtigt dabei auch die Besonderheiten von Windows- und Apple-Netzwerken. So ist zum Beispiel auch Apples AirPrint in CUPS integriert und funktioniert automatisch. Dadurch konnen auch iPhones und iPads im Netzwerk drucken. Fur Windows-Clients wird ein Samba-Client verwendet.

Fast alle Drucker werden von CUPS unterstutzt. Fur die Modelle, die nicht unterstutzt werden, gibt es generische Treiber, die Grundfunktionen zur Verfugung stellen. Nur spezielle Funktionen benotigen einen Treiber des Herstellers.  
Da Hewlett Packard ein eigenes Open-Source-Projekt betreibt, werden HP-Drucker besonders gut von CUPS unterstutzt.

### Aufgaben

  1. Installieren Sie CUPS und richten es anschließend ein.
  2. Installieren Sie den Drucker-Treiber, falls notwendig.
  3. Richten Sie den Drucker unter CUPS ein.
  4. Drucken Sie eine Datei auf der Kommandozeile aus.

### Losung: Installation und Einrichtung von CUPS

Zuerst fuhren wir ein Update der Paketlisten und ein Upgrade des Systems durch.
    
    
    sudo apt-get update
    sudo apt-get upgrade

Dann installieren wir CUPS.
    
    
    sudo apt-get install cups

Je nach System kann der Installationsprozess mehrere Pakete mit uber 100 MByte umfassen. So werden neben CUPS auch Teile von Samba, Avahi, Perl und verschiedene Bibliotheken installiert. Bis alles herunterladen und anschließend installiert ist, kann es einige Zeit dauern.

Nach dem alles installiert ist, mussen an der CUPS-Konfigurationsdatei einige Änderungen vorgenommen werden.
    
    
    sudo nano /etc/cups/cupsd.conf

CUPS lauscht standardmaßig auf Port 631, allerdings nur auf dem Localhost. Wenn man uber das Netzwerk darauf zugreifen mochte, muss man das zuerst freigeben.

Die Zeile:
    
    
    Listen localhost:631

andern in:
    
    
    Port 631

Dann soll der Print-Server alle angeschlossenen Drucker im Netzwerk bekannt machen. Dazu fugen wir noch folgende Zeile ein:
    
    
    BrowseAddress @LOCAL

Der Wert "BrowseAddress" gibt an, an welche Hosts Druckerinformationen "gebroadcastet" werden. "@LOCAL" steht in dem Fall fur "alle" Hosts im lokal angeschlossenen Netzwerk.

Dann suchen Sie nach folgenden Zeilen und fugen jeweils ein "Allow @Local" ein.
    
    
    # Restrict access to the server...
    <Location />
    Order allow,deny
    Allow @LOCAL
    </Location>  
    
    # Restrict access to the admin pages...
    <Location /admin>
    Order allow,deny
    Allow @LOCAL
    </Location>
      
    # Restrict access to configuration files...
    <Location /admin/conf>
    AuthType Default
    Require user @SYSTEM
    Order allow,deny
    Allow @LOCAL
    </Location>

"@LOCAL" steht fur alle lokal am Druckserver angeschlossenen Netze. Davon ausgenommen sind Dial-Up-Verbindungen.

Nach den Änderungen muss man die Datei speichern und schließen: Strg + O, Return, Strg + X.

Dann mussen wir noch einen Benutzer der Benutzergruppe "lpadmin" hinzufugen. Das kann der Standard-Benutzer "pi" sein. Man kann dafur auch einen neuen Benutzer anlegen, sofern man das mochte. Das ist aber nicht zwingend erforderlich.
    
    
    sudo usermod -aG lpadmin pi

Danach ist ein Restart des CUPS-Servers notwendig.
    
    
    sudo service cups restart

Das ist immer dann notwendig, wenn die Konfigurationsdatei von CUPS geandert wurde.

### Losung: Drucker-Treiber installieren

Je nach Hersteller und Drucker-Modell ist die Installation von Drucker-Treibern mal mehr oder weniger einfach. Fur gangige Modelle bringt CUPS bereits Drucker-Treiber mit. Aber eben nicht fur alle. Am besten funktioniert es immer noch mit HP-Druckern. Ohne Werbung zu machen, HP stellt fur seine Drucker Open-Source-Drucker-Treiber zur Verfugung. Das heißt, einen HP-Drucker bekommt man mit CUPS in der Regel immer zum Laufen. Andere Hersteller sind hier nicht so freigiebig, weshalb man hier mehr Aufwand hat. Manchmal kommt man um das Kompilieren des Treibers nicht herum.

Fur HP-Drucker gibt es eine große Auswahl an Drucker-Treibern, die sich leicht installieren lasst.
    
    
    sudo apt-get install hplip

Fur manche Samsung-Modelle gibt es offene Drucker-Treiber, die in einem Paket zusammengefasst sind.
    
    
    sudo apt-get install splix

Das Herunterladen und die Installation der Pakete kann etwas langer dauern. Also hier etwas Geduld mitbringen.

Bei anderen Herstellern bedarf es anderer Vorgehensweisen, die sich von Modell zu Modell unterscheiden. Es empfiehlt sich fur das entsprechende Drucker-Modell den richtigen Weg zu suchen.

Nachdem man Pakete oder Drucker-Treiber installiert hat, empfiehlt sich ein Restart von CUPS.
    
    
    sudo service cups restart

Manchmal ist auch ein Reboot des Systems erforderlich.

### Losung: Drucker unter CUPS einrichten und verwalten

Hinweis: Man tut sich beim Einrichten von Druckern unter CUPS leichter, wenn die notwendigen Drucker-Treiber installiert sind.

Jetzt geht es darum, Drucker unter CUPS einzurichten. Dazu muss man den oder die Drucker am USB des Raspberry Pi jetzt anschließen.  
Anschließend konfigurieren wir CUPS. Zu diesem Zweck bringt CUPS seinen eigenen Webserver mit und lasst sich bequem uber ein Web-Interface konfigurieren. Dazu benotigen wir die IP-Adresse des Raspberry Pi, die zusammen mit der Portnummer "631" in die Browser-Adresszeile eingegeben werden muss.
    
    
    https://192.168.1.2:631

Es erwartet einen das Web-Interface. Fur die Einrichtung eines Druckers geht man wie folgt vor:

Unter dem Menupunkt "Verwaltung" klickt man auf den Button "Drucker hinzufugen". In der Regel wird man nach Benutzername und Passwort gefragt. Und zwar von dem Benutzer, den man der Gruppe "lpadmin" hinzugefugt hat.

##### Drucker hinzufugen (Schritt 1/5)

Danach werden die angeschlossenen und erkannten Drucker aufgelistet (Lokale Drucker), aus der man den Drucker auswahlt, den man einrichten mochte.  
Achtung, hier werden alle erkannten Drucker aufgelistet, auch die, die man schon eingerichtet hat.

##### Drucker hinzufugen (Schritt 3/5)

Hier kann man den Drucker-Namen und die Beschreibung den eigenen Wunschen anpassen. Das muss man aber nicht. Im Prinzip kann man die Vorgabe so lassen, weil diese Bezeichnung meist korrekt ist und spater auch auf den Client-Systemen verwendet wird.  
Wichtig ist hier nur, einen Haken unter "Freigabe" zu setzen. Denn nur so wird dieser Drucker im Netzwerk verfugbar gemacht. Ist der Haken nicht gesetzt, dann ist der Drucker nur lokal nutzbar.

##### Drucker hinzufugen (Schritt 5/5)

Hier muss man den Hersteller bzw. die Marke auswahlen und anschließend moglichst genau die Modellbezeichnung.  
An dieser Stelle ist es hilfreich, wenn der Druckertreiber vorher installiert wurde. Wenn nicht, dann kann man das jetzt tun, CUPS neu starten und den Hersteller erneut auswahlen. Dann wird die Liste mit den Modell-Bezeichnungen aktualisiert.

Nach dem wir das richtige Modell ausgewahlt haben, mussen noch die Standard-Einstellungen festgelegt werden. Wobei man da in der Regel nichts andern muss. Die Vorgaben sind zum Drucker-Modell schon passend vorausgewahlt.

Nach dem der Drucker eingerichtet ist, kann man noch eine Testseite drucken. Dazu wahlt man im Feld "Wartung" einfach "Testseite drucken" aus. Der Testdruck startet dann automatisch.

### Losung: Netzwerkdrucker auf einem Client einrichten

Grundsatzlich stehen die eingerichteten Drucker per AirPrint zum Beispiel fur Mac OS, auf dem iPhone und iPad zur Verfugung. Unter Linux und Windows muss man die Drucker jeweils noch als Netzwerk-Drucker einrichten. Die Einrichtungsdialoge sind hier meist selbsterklarend.

### Losung: Drucken von der Konsole

Grundsatzlich kann man auch direkt von der Konsole aus einen Druckauftrag abschicken. Dafur braucht man den Druckernamen. Wenn man das nicht auswendig weiß, dann kann man in der Druckerliste nachsehen.
    
    
    lpstat -a

Dort wahlen wir fur das folgende Kommando den Druckernamen aus und geben noch den Pfad einer Text-Datei an, die ausgedruckt werden soll.
    
    
    lp –d <Druckernamen> </Pfad/zur/Textdatei>

Den Status fur den aktuellen Druckauftrag, sofern das Dokument noch nicht fertig gedruckt ist, bekommt man so:
    
    
    lpstat -p

### Troubleshooting

Das Einrichten eines Druckers gelingt in der Regel ohne Probleme. Doch manchmal, je nach Hersteller und Druckermodell, hakt es dann doch. Um das Problem zu losen empfiehlt sich eine Schritt-fur-Schritt-Vorgehensweise, auch wenn das Problem vielleicht irgendwo dazwischen liegt.

Zuerst klaren wir, ob der oder die Drucker uberhaupt am USB erkannt werden. Dazu benotigen wir die "usbutils", die eventuell nachinstalliert werden mussen.
    
    
    sudo apt-get install usbutils

Ist das Paket "usbutils" installiert, dann prufen wir, ob der oder die Drucker am USB erkannt wurden.
    
    
    lsusb

Dieses Kommando ist mal mehr, mal weniger auskunftsfreudig. Typischerweise werden die Drucker mit dem Hersteller-Namen, vielleicht sogar mit der Modell-Bezeichnung ausgewiesen.  
Es ist ein gutes Zeichen, wenn der oder die Drucker am USB erkannt werden. Wenn nicht, dann gibt es andere systembedingte Probleme. Eventuell hilft ein Blick in "dmesg".
    
    
    dmesg

Die dort verzeichneten Fehlermeldung deuten auf Probleme hin, die Einzelfalle sind. Die konnen wir hier leider nicht auflosen. Eventuell hilft die Suche mit der Fehlermeldung bei der bevorzugten Suchmaschine.

### Weitere verwandte Themen:

### Produktempfehlungen
