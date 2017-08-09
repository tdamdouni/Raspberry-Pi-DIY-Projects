# Node.js auf dem Raspberry Pi Zero W

_Captured: 2017-08-08 at 17:38 from [stefanreimers.wordpress.com](https://stefanreimers.wordpress.com/2017/03/18/node-js-auf-dem-raspberry-pi-zero-w/)_

Ich habe in der vergangenen Zeit haufig Node.js auf unterschiedlichen Raspberry Pi Versionen installieren mussen, zumeist um meine Hausautomatisierung voran zu treiben (z.B. mit [NodeRED](https://nodered.org/) oder [node-eq3ble](https://www.npmjs.com/package/eq3ble)). Aber jedes Mal schlage ich im Internet die notigen Installationsschritte nach. Damit das zukunftig uberflussig wird, hier nun eine kurze Anleitung fur (mich selbst und andere) Leidensgenossen.

Der Raspberry Pi Zero (W), der zuletzt zu meiner Infrastruktur dazu gekommen ist, setzt mit dem [Broadcom BMC2835](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bcm2835/README.md) auf denselben Prozessor wie die Vorgangermodelle A, B und B+. Beim RPi Zero ist der SingleCore standarmaßig auf 1GHz getaktet. Aufgrund der Prozessorwahl sind die _*-linux-arm6l_ Builds von Node.js zu verwenden. Die Build von Nodesource, die man haufig in Installationsanleitungen findet, funktionieren nicht. Einen entsprechenden Hinweis bekommt man angezeigt, wenn man es trotzdem versucht.

Den notwendigen aktuellen Build bekommt man direkt bei Node.js im Code-Repository (beispielhaft fur die [Version 7.7.3](https://nodejs.org/dist/v7.7.3/)). Die Installation ist dann ein Vierzeiler, mit dem das Paket heruntergeladen, entpackt und an seinen endgultigen Ort kopiert wird:
    
    
    wget https://nodejs.org/dist/v7.7.3/node-v7.7.3-linux-armv6l.tar.gz
    tar -xvf node-v7.7.3-linux-armv6l.tar.gz
    cd node-v7.7.3-linux-armv6l
    sudo cp -R * /usr/local/

Dass die Installation funktioniert hat, lasst sich mit den beiden Kommandos zur Versionsabfrage von Node.js und NPM uberprufen:
    
    
    node -v
    npm -v
