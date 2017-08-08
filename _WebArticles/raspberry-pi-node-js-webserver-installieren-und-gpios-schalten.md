# Raspberry Pi Node.js Webserver installieren und GPIOs schalten

_Captured: 2017-08-08 at 17:39 from [tutorials-raspberrypi.de](https://tutorials-raspberrypi.de/raspberry-pi-nodejs-webserver-installieren-gpios-steuern/)_

![Raspberry Pi Node.JS Logo](https://tutorials-raspberrypi.de/wp-content/uploads/2016/10/Raspberry-Pi-Node.JS-Logo-1024x627.png)

Node.JS ist eine Server Platform, welche Javascript verwendet. Ursprunglich fur Googles Chrome Browser entwickelt, ist es sehr resourcensparend, was vor allem den EInsatz eines Raspberry Pi Node.JS Webservers interessant werden lasst. Zusatzlich zu den Vorteilen asynchroner Anwendungen bietet Node mit dem internen Paketmanager „npm" eine sehr einfache aber machtige Methode, um verschiedene Plugins bzw. Bibliotheken zu installieren und zu verwenden.

In diesem Tutorial wird das Aufsetzen und Konfigurieren eines Raspberry Pi NodeJS Servers gezeigt. Zusatzlich habe ich ein kleines Programm fur Node geschrieben, womit die GPIOs des Raspberry Pi's geschaltet werden konnen.

Ein NodeJS Server ist Voraussetzung fur viele verschiedene Anwendungen, wie bspw. [HomeBridge](https://github.com/nfarina/homebridge). Auch viele andere Projekte, wofur ein Server benotigt wird, konnen mit einem Raspberry Pi und NodeJS realisiert werden.

## Benotigte Hardware

Aufgrund der besseren Leistung im Vergleich zu den Vorgangern und insbesonders wegen der ARMv8 Architektur empfehle ich einen [Raspberry Pi 3](http://www.amazon.de/gp/product/B01CEFWQFA?ie=UTF8&linkCode=as2&camp=1634&creative=6738&tag=754-21&creativeASIN=B01CEFWQFA). Daneben muss dein Router Portforwarding unterstutzen, falls du die Anwendungen auch außerhalb deines Heimnetzwerks aufrufen willst. Ich empfehle hierfur eine [FRITZ!Box](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=FRITZ!Box) o.a.

Um das kleine Beispiel am Ende nachbauen zu konnen, wird zusatzlich noch benotigt:

Sofern du deinen Raspberry Pi nicht per Netzwerkkabel angeschlossen hast und das WLAN noch nicht konfiguriert ist, kannst du diesen Tutorials folgen, um es einzurichten ([hier](http://tutorials-raspberrypi.de/raspberry-pi-3-wlan-einrichten-bluetooth/) fur Raspberry Pi 3, [hier](http://tutorials-raspberrypi.de/wlan-stick-installieren-und-einrichten/) fur vorherige Modelle).

Zusatzlich empfehle ich die Verwendung des [SSH Zugriffs](http://tutorials-raspberrypi.de/raspberry-pi-ssh-windows-zugriff-putty/), sowie optimal von einem [FTP Service](http://tutorials-raspberrypi.de/webserver-installation-teil-5-ftp-server/), um einfach Dateien auf den Raspberry Pi zu ubertragen.

## Installation von Node.JS auf dem Raspberry Pi

Bevor wir Node installieren, updaten wir die Pakete und Paketquellen, um alles benotigte auf dem aktuellen Stand zu haben:
    
    
    sudo apt-get update
    sudo apt-get full-upgrade

Der Vorgang kann etwas dauern. Da Node.JS nicht in den vordefinierten Paketquellen ist, mussen wir es zuerst hinzufugen. Die aktuellste LTS Version kannst du auf der [Node.JS Website](https://nodejs.org/en/download/) einsehen und dementsprechend anpassen.
    
    
    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

Nun konnen wir Node ganz einfach uber den internen Paketmanaager installieren, wobei dies ein wenig dauern kann:
    
    
    sudo apt-get install -y nodejs

## Erster Test

Wenn die Installation soweit ohne Probleme durchgelaufen ist, konnen wir in der Konsole einfach folgendes ausfuhren, um zu sehen, ob alles geklappt hat:
    
    
    node --version

Es sollte nun die [aktuellste Version](https://nodejs.org/en/download/) angezeigt werden.

Nun wollen wir mit einem kleinen [Hello-World!](https://howtonode.org/hello-node) Programm starten. Wir erstellen eine neue Datei.
    
    
    sudo nano hello-world.js

Darin fugen wir folgenden Inhalt ein:

1234567891011121314 
// Load the http module to create an http server.var http = require('http');// Configure our HTTP server to respond with Hello World to all requests.var server = http.createServer(function (request, response) {response.writeHead(200, {"Content-Type": "text/plain"});response.end("Hello World\n");});// Listen on port 8000, IP defaults to 127.0.0.1server.listen(8000);// Put a friendly message on the terminalconsole.log("Server running at http://127.0.0.1:8000/");

Anschließend speichern und beenden wir den Editor (STRG+O, STRG+X). Du kannst den Server nun einfach starten, indem du im Terminal folgendes eingibst:
    
    
    node hello-world.js

Im Webbrowser kann die Seite nun bereits im Browser aufgerufen werden. Dazu gibst du entweder die IP deines Pi's im Netzwerk inkl. Port an (z.B. 192.168.1.68:8000) oder (sofern dein Router das unterstutzt) einfach den Namen des Hosts inkl. Port. Bei mir ist dies <http://raspberrypi:8000/>

![node-js-hello-world-preview](https://tutorials-raspberrypi.de/wp-content/uploads/2016/10/Node.js-Hello-World-Preview.png)

PS: Wir nutzen in diesem Beispiel Port 8000. Der Standardport fur Webserver ist 80. Allerdings benotigt Node.js fur Ports, welche unter 1000 liegen, [Rootrechte](http://stackoverflow.com/questions/18947356/node-js-app-cant-run-on-port-80-even-though-theres-no-other-process-blocking-t).

Falls du dauerhaft von außerhalb deines Heimnetzwerks auf den Server zugreifen willst, macht es Sinn einen [DNS Server zu installieren](http://tutorials-raspberrypi.de/webserver-installation-teil-6-dns-server-via-no-ip/). Naturlich mussen die ausgewahlten Ports auch in deinem Router per Port-Forwarding / Weiterleitung fur die interne IP Adresse deines Raspberry Pi's ausgewahlt und freigeschaltet werden.

## NPM - NodeJS Package Manager

Mit Hilfe des [NPM](https://www.npmjs.com/) (Node.js Package Manager) konnen sehr einfach zusatzliche Bibliotheken installiert werden und diese in einem Node Projekt verwendet werden. Üblicherweise hat ein erstelltes Projekt im Basisverzeichnis eine Datei namens „package.json". In dieser Datei werden unter „dependencies" jene verwendeten Pakete inkl. (minimal geforderter) Version eingetragen. Wenn bspw. ein Projekt spater weitergegeben wird, mussen die erforderlichen Pakete erst installiert werden. Dazu wechselt man in das Verzeichnis, worin sich die package.json befindet und gibt ein:
    
    
    npm install

Alle notwendigen Pakete werden installiert. Es ist allerdings nicht unbedingt notwendig, dass man seine verwendeten Pakete per Hand eintragt. Mochte man ein neues Paket verwenden (in unserem Fall sei es [rpio](https://www.npmjs.com/package/rpio)) kann man den Parameter `\--save` mit angeben und das Paket wird automatisch der package.json Datei hinzugefugt:
    
    
    npm install rpio --save

Fur weitere Befehle und Erlauterungen kannst du einen Blick in die [NPM Dokumentation](https://docs.npmjs.com/) werfen.

## Raspberry Pi GPIOs per Weboberflache schalten

Sollte deine Beispieldatei noch laufen, kannst du sie mittels STRG+C beenden.

Ich habe eine kleine Anwendung geschrieben, mit der man seine GPIOs per Weboberflache (Desktop PC Browser, Smartphone, Tablet) steuern kann. Da dies nur als kleines Beispiel dienen soll, ist damit lediglich der Output steuerbar. Allerdings ist es recht einfach auch GPIOs als Input zu definieren und diese auszulesen. Als Grundlage habe ich das NPM Package [rpio](https://www.npmjs.com/package/rpio) genommen.

Fur einen einfachen Test kannst du das Paket von Github klonen:
    
    
    git clone https://github.com/tutRPi/Raspberry-Pi-Simple-Web-GPIO-GUI
    cd Raspberry-Pi-Simple-Web-GPIO-GUI

Bevor wir den Server starten, mussen die weiteren Pakete installiert werden:
    
    
    npm install

Anschließend kann der Raspberry Pi Node.JS Server gestartet werden. Da wir die GPIOs nutzen ist zwingender maßen der Aufruf per sudo notig. Daher habe ich mich zusatzlich entschieden, den Server auf Port 80 laufen zu lassen, da wir so einfach uber den Hostnamen bzw. interner IP des Pi's darauf zugreifen konnen, ohne den Port anzugeben. Voraussetzung dafur ist, dass nichts anderes auf diesem Port lauft (wie bspw. [Apache2](http://tutorials-raspberrypi.de/webserver-installation-apache2/)). Wir starten also nun:
    
    
    sudo npm start

Zuruck im Browser erscheint das User Interface zum Steuern der GPIOs (keine Portangabe notig). Dazu muss gesagt werden, dass die GPIOs anfanglich alle als „OFF" angezeigt werden, auch wenn eine andere Anwendung davor einen der Pins angeschaltet hat. Das kommt daher, dass die Bibliothek leider nicht den Output Zustand der GPIOs auslesen kann. Zwar konnte man beim Starten der Web-App alle GPIOs auf den niedrigen Pegel setzen, aber darauf habe ich verzichtet. Wen dies stort, dem steht es naturlich frei das anzupassen.

![Raspberry Pi Node.js Webserver installieren und GPIOs schalten](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Node.js-Webserver-GPIOS-403x500.png)

Weiterhin habe ich das ganze mal aufgezeichnet, um zu zeigen, wie die Steuerung per Weboberflache aussehen wurde. Wer den Aufbau der Beispielsschaltung sehen mochte, kann dies hier tun. Im Grunde ist es aber recht simpel, da einfach nur an die einzelnen (steuerbare) GPIOs eine LED mit Vorwiderstand gehangt wurde.

## Autostart des Raspberry Pi Node.js Servers

Als letztes wollen wir den Server noch automatisch nach dem Boot des Raspberry Pi's starten lassen. Ansonsten wurde sich der Server beim Herunterfahren beenden und musste erneut per Hand aktiviert werden.

Bevor wir den Eintrag zum automatischen Starten von unserer Server Applikation erstellen konnen, mussen wir den Pfad, in dem sich Node befindet herausfinden (Standardmaßig ist dies `/usr/bin/node`).
    
    
    pi@raspberrypi:~ $ which node
    /usr/bin/node

Nun brauchen wir noch den kompletten Pfad, in dem sich unsere Javascript Datei (`app.js`) befindet. Mittels `ls` konnen wir uns die Dateien anzeigen lassen, die im Ordner vorhanden sind und mittels `pwd` den Pfad.

Diese beiden Werte kopieren wir, um gleich einen Eintrag erstellen zu konnen:
    
    
    sudo crontab -e

Am Ende dieser Datei konnen Eintrage hinzugefugt werden, welche z.B. nach einem Neustart oder zu einem gewissen Zeitpunkt ausgefuhrt werden sollen. Um unsere Anwendung nach dem Neustart automatisch starten zu lassen, fugen wir ans Ende der Datei folgende Zeile hinzu (ggf. Pfade anpassen):
    
    
    @reboot sudo /usr/bin/node /home/pi/Raspberry-Pi-Simple-Web-GPIO-GUI/app.js &

Gespeichert wird mit STRG+O und beendet mit STRG+X (Nano Editor). Um zu uberprufen, ob alles funktioniert hat, kannst du den Raspberry Pi neustarten (`sudo reboot`) und danach noch einmal die URL aufrufen. Sollte die Seite angezeigt werden, hat alles geklappt.

Die Anwendungen, die du im Endeffekt auf deinem Raspberry Pi Node.JS Server laufen lassen kannst, sind fast unbegrenzt. Von der reinen GPIO Steuerung, uber eine Oberflache zur Hausautomatisierung hin zum Überwachungsserver fur einzelne Dienste oder Sensoren. Durch den geringen Stromverbrauch des Raspberry Pi's und dennoch vergleichsweise hohen Leistungsfahigkeit ist der Raspberry Pi ein idealer Server fur kleine (Hobby-)Projekte.
