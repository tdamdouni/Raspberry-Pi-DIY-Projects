# Homebridge auf einem Raspberry Pi installieren

_Captured: 2017-05-06 at 10:10 from [timobihlmaier.de](https://timobihlmaier.de/homebridge-auf-einem-raspberry-pi-installieren/)_

In dem folgendem Artikel bzw. dem angefugten Video zeige ich euch, wie ihr „Homebridge" auf einem Raspberry Pi installiert und dadurch eine Vielzahl von Geraten mit Siri auf seinem iOS-Gerat steuern konnt.

## Was ist eigentlich Homebridge und HomeKit?

Homebridge ist ein NodeJS Server, der in diesem Fall auf einem Raspberry Pi lauft und die HomeKit API von iOS emuliert. HomeKit ist dabei eine Smart-Home Schnittstelle, durch die offiziell von Apple unterstutzte Hardware wie Philips Hue oder Elgato Eve direkt vom iPhone aus mit Siri ferngesteuert werden kann.

## Warum Homebridge?

Der Grund fur die Verwendung ist ganz einfach. Leider bieten nur sehr wenige, meist hochpreisige Gerate die HomeKit Unterstutzung an. Hier kommt nun Homebridge ins Spiel, das eine Vielzahl von Plugins anbieten und offen fur Entwickler steht, sodass auch andere Gerate Problemlos in HomeKit eingebunden werden konnen uns so z.B. ganz einfach per Siri das Garagentor hochgefahren oder der PC/Mac gestartet werden kann.

Wie die Installation nungenau auf dem Raspberry Pi vorgenommen werden kann, zeige ich daher sowohl in dem oben eingebetteten Video und in der folgenden Textanleitung.

## Raspberry Pi aktualisieren

Zunachst musst ihr euch per SSH mit dem Raspberry Pi verbinden und die neuesten Softwarepakete herunterladen. Über folgenden Befehl konnt dies tun:
    
    
    sudo apt-get update && sudo apt-get -y upgrade 
    

Solltet ihr an dieser Stelle Probleme haben und euch noch nicht gut auskennen, kann ich empfehlen, das oben eingebettete Video als Anleitung anzusehen, da hier alles ausfuhrlich gezeigt wird.

Voraussetzung fur die nachfolgenden Schritte ist zusatzlich, dass „gcc" in Version 4.9.2 oder neuer vorliegen muss. Eine Überprufung kann mit
    
    
    g++ -4.9 -v
    

durchgefuhrt werden. Sollte hier eine altere Version als 4.9.2 stehen, so muss das Update manuell nachinstalliert werden.

## NodeJS installieren

Wie bereits zu Beginn des Artikels erwahnt, wird NodeJS dringend benotigt.

Um die neueste Version zu installieren, musst ihr dazu folgende Befehle eingeben.
    
    
    wget http://node-arm.herokuapp.com/node_latest_armhf.deb
    sudo dpkg -i node_latest_armhf.deb
    node -v
    sudo npm update -g npm
    npm -v
    

Die letzten Beiden Befehle sollten jeweils eine Versionsnummer nach Eingabe anzeigen. Dadurch konnt ihr sicherstellen, dass die Pakete korrekt installiert wurden.

[alert style="blue"]/Nachtrag/ Da einige Benutzer Probleme bei der Installation hatten, ist hier nun die aktualisierte Fassung.[/alert]
    
    
    sudo apt-get remove nodered nodejs nodejs-legacy npm

Anschließend muss je nach Pi Gerategeneration anders vorgegangen werden.

**Fur Raspberry Pi 2 und 3:**
    
    
    curl -sL https://deb.nodesource.com/setup_4.x | sudo bash
    sudo apt-get install -y build-essential python-dev nodejs npm
    

**Fur Raspberry Pi 1:**
    
    
    wget http://node-arm.herokuapp.com/node_archive_armhf.deb
    sudo dpkg -i node_archive_armhf.deb
    sudo apt-get install -y build-essential python-dev npm

##  Libavahi und git installieren

Libavahi muss ebenfalls installiert werden, sodass Homebridge spater im Heimnetzwerk fur iOS sichtbar wird. Es kann folgendermaßen installiert werden:
    
    
    sudo apt-get install libavahi-compat-libdnssd-dev
    sudo apt-get install git
    

Es kann sein, dass wahrend der Installation mehrmals mit Y (fur „Yes") die Installation bestatigt werden muss.

## Homebridge installieren

Nachdem nun die Voraussetzungen fur die Installation erfullt sind, kann nun endlich Homebridge installiert werden.
    
    
    sudo npm install -g homebridge
    

In einigem Fallen kommen nach der Installation Fehlermeldungen, durch die spater Probleme auftreten werden. Gebt dazu zusatzlich nach der Installation folgendes ein:
    
    
    sudo npm install -g --unsafe-perm homebridge
    

## Homebridge konfigurieren

Nach der Installation muss ebenfalls eine Konfigurationsdatei im Home-Verzeichnis angelegt werden.

[alert style="yellow"]Hierfur ist es wichtig, dass ihr bereits ins Homeverzeichnis navigiert seid, ansonsten muss der folgende Befehl ggf. angepasst werden.[/alert]
    
    
    sudo nano .homebridge/config.json
    

Kopiert dazu folgenden Inhalt in die Datei:

Als Name kannst du hier nun einen eigenen Name eingeben. Username, Port und Pin sollten unverandert bleiben. Nur sofern Probleme auftreten sollten oder ihr mehrere Homebridges verwenden mochtet, konnt ihr der Username andern.

Anschließend kann die Konfiguration mit STRG+O abgespeichert und mit STRG+X geschlossen werden.

## Automatischen Start konfigurieren

Momentan ist es so, dass Homebridge nur manuell gestartet werden kann und zum Beispiel nach einem Neustart nicht mehr lauft und wieder manuell gestartet werden muss. Daher mussen wir nun einen automatischen Start konfigurieren.

Hierfur erstellen wir zunachst eine Datei im Verzeichnis /etc/init.d/
    
    
    sudo nano /etc/init.d/homebridge
    

Und fugt folgenden Inhalt in die Datei ein:

Mit STRG+O und STRG+X konnt ihr die Datei dann wieder speichern und schließen.

Bitte beachte, dass hier davon ausgegangen wird, dass der Benutzername des Raspberry Pi _pi _heißt. Sofern ihr einen anderen Benutzername verwendet, musst ihr _pi_ entsprechend in der homebridge-Datei durch den eigenen Name ersetzen.

**Nachtrag: **Damit die Datei nun korrekt fur den automatischen Start erkannt wird, musst ihr noch folgenden Befehl eingeben:
    
    
    sudo update-rc.d homebridge defaults

Ab sofort wird Homebridge automatisch gestartet und kann bei Bedarf auch per Befehl beendet (stop), gestartet (start) und neugestartet (restart) oder der aktuelle Status (status) erfragt werden
    
    
    sudo /etc/init.d/homebridge stop|start|restart|status

## Schlusswort und wie es weiter geht

Nun habt ihr erfolgreich euer eigenes HomeKit auf dem Raspberry Pi installiert.

In den nachsten Schritten solltet ihr nun am besten Plugins installieren um eure eigenen Gerate mit SIri zu steuern und bei eurem iOS-Gerat das HomeKit hinzufugen. Wie das genau funktioniert, konnt ihr [hier ](https://timobihlmaier.de/homebridge-plugins-installieren/)sehen.
