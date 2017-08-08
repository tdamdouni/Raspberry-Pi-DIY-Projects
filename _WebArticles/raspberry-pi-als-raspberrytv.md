# Raspberry PI als RaspberryTV

_Captured: 2017-05-06 at 16:53 from [www.welzels.de](http://www.welzels.de/blog/projekte/raspberry-pi/raspberry-pi-als-raspberrytv/)_

Eigentlich sollte, es seit RaspBMC, kein Problem mehr sein sich ein AppleTV Klone mit einem Raspberry PI zu basteln. Aber dennoch beschreibe ich hier mal wie ich es gemacht habe und wie ich die Problem die dann doch aufgetreten sind gelost habe.

## Die Installation

Zuerst benotigt man ein Image, das bei [RaspBMC](http://www.raspbmc.com) unter [Downloads](http://www.raspbmc.com/download/) geladen werden kann. Ich habe mich fur das „Standalone Image" entschieden ([raspbmc-rc5-prebuilt.img.gz](http://download.raspbmc.com/downloads/bin/filesystem/prebuilt/raspbmc-rc5-prebuilt.img.gz)). Die Installation ist identisch wie unter: [Raspberry PI - Die Installation / Download und vorbereiten der SD-Karte](http://www.welzels.de/blog/projekte/raspberry-pi/raspberry-pi-die-erste-installation/):

1234567 
Linux:~/Downloads # unzip raspbmc-rc5-prebuilt.img.gz~/Downloads # sudo dd bs=4M if=sd.img of=/dev/sdbMac OS X:~/Downloads $ unzip raspbmc-rc5-prebuilt.img.gz~/Downloads $ dd bs=4M if=sd.img of=/dev/disk2

Die SD-Karte sicher entfernen und in den SD-Kartenleser des Raspberry Stecken. Netzwerk und Spannungsversorgung anschließen und warten bis er gestartet ist. Ein Terminal offnen und eine SSH-Verbindung zu dem Raspberry PI herstellen. Sollte nun die IP-Adresse oder der Name unbekannt sein, das habe ich unter „[Raspberry PI - Netzwerk und Wlan konfigurieren](http://www.welzels.de/blog/projekte/raspberry-pi/raspberry-pi-netzwerk-und-wlan-konfigurieren/)" beschreiben. Der Standard Name des Raspberry PI lautetet bei mir „xbmc-d3f3" und mit diesem Namen habe ich auch die Verbindung hergestellt:

Der Benutzername ist hier ebenfalls „pi" und das Passwort lautet „raspberry".

Nach der ersten Anmeldung erscheint ein Konfigurationsdialog, beginnend mit der Sprachauswahl. Ich fuge hier die Deutsche Sprache hinzu:

![RaspBMC01](http://www.welzels.de/blog/wp-content/uploads/2013/01/RaspBMC01-300x205.png)

![RapBMC02](http://www.welzels.de/blog/wp-content/uploads/2013/01/RapBMC02-300x205.png)

Danach wird noch der Standort bzw. Zeitzone festgelegt, also Europa und Berlin:

![RaspBMC03](http://www.welzels.de/blog/wp-content/uploads/2013/01/RaspBMC03-300x205.png)

![RaspBMC04](http://www.welzels.de/blog/wp-content/uploads/2013/01/RaspBMC04-300x205.png)

Bevor nun das System weiter konfiguriert wird, solle die Paketdatenbank, sowie das System aktualisiert werden:

## Wlan einrichten

Nach dem alles auf den neuesten Stand gebracht wurde, installiere ich erst ein mal Wlan. Wer hier die Moglichkeit besitzt LAN und HDMI gleichzeitz berteiben zu konnen, kann das Wlan auch uber XBMC konfigurieren. Da ich in der Nahe meines Fernsehers kein kabelgebundenes LAN zur Verfugung habe. Fuhre ich die Installation des Wlan wie bereites in, „[Raspberry PI - Netzwerk und Wlan konfigurieren / Wireless Adapter konfigurieren](http://www.welzels.de/blog/projekte/raspberry-pi/raspberry-pi-netzwerk-und-wlan-konfigurieren/#Wireless_Adapter_konfigurieren)„, beschrieben durch. Dies funktioniert auch unter RaspBMC bis auf eine Kleinigkeit. Das Wlan startet nicht automatisch. Wieso das so ist kann ich nicht sagen. Ich habe daher ein kleines Init-Skript geschrieben um die Karte zu starten. Es lasst sich wie folgt einbinden:

Erzeugen der Init-Datei:

Diesen Inhalt in die Datei kopieren:

Dann die Datei ausfuhrbar machen:

Und als Service registrieren:

Nach einem Reboot oder dem absetzen des Befehls pi@raspbmc:~$ sudo service wifi start ist das Wlan verfugbar. Der Raspbery PI kann nun ausgeschaltet werden.

## Der erste Start

An den Fernseher anschließen, mit Spannung versorgen, XBMC startet automatisch und man gelangt zu den folgenden Menu:

![raspBMC06](http://www.welzels.de/blog/wp-content/uploads/2013/01/raspBMC06-300x167.jpg)

Jedoch erwartet einen hier ein weiters Problem. Wahrend ein AppleTV eine reelle Fernbedienung mitbringt, hat RaspBMC nur eine virtuelle. Also entweder eine Tastatur anschließen oder die virtuelle Fernbedienung, mittels Laptop, Smartphone bzw. Tablet, durch Eingabe der IP-Adress des Raspberry PI (Hostname geht auch) in einem Browser aufrufen. Man gelangt so auf ein Web-Frontend mit dem sich XBMC steuern lasst.

![RspBMC05](http://www.welzels.de/blog/wp-content/uploads/2013/01/RspBMC05-300x217.png)

Jedoch ist bei der Benutzung eines Smatphone oder Tablet die Anwendung Official XBMC Remote aus dem [App Store](https://itunes.apple.com/de/app/official-xbmc-remote/id520480364?mt=8) oder [Google Play](https://play.google.com/store/apps/details?id=org.xbmc.android.remote) zu empfehlen. XBMC lasst sich hiermit sehr eifach steuern.

![XBMCRemote01](http://www.welzels.de/blog/wp-content/uploads/2013/01/XBMCRemote01-200x300.png)

![XBMCRemote02](http://www.welzels.de/blog/wp-content/uploads/2013/01/XBMCRemote02-200x300.png)

![XBMCRemote03](http://www.welzels.de/blog/wp-content/uploads/2013/01/XBMCRemote03-200x300.png)

![XBMCRemote04](http://www.welzels.de/blog/wp-content/uploads/2013/01/XBMCRemote04-200x300.png)

![XBMCRemote05](http://www.welzels.de/blog/wp-content/uploads/2013/01/XBMCRemote05-200x300.png)

![XBMCRemote06](http://www.welzels.de/blog/wp-content/uploads/2013/01/XBMCRemote06-200x300.png)

## Weitere Einstellungen

Da ich nun kein XBMC Tutorial schreibe, sondern eines zu RaspianTV, erlautere ich nur die wesentlichen Einstellungen.

  * Unter **System** - **Settings** - **Appeareance** - **International**, erst ein mal die Sprache, Region und die Zeitzone auf deutsch stellen.
  * Unter **System** -** Netzwerk**: 
    * **Allgemein**: Den Geratename in z.B. RaspberryTV andern, es wird nicht der Hostname ubernommen.
    * **UPnP**: Sofern auf Mediendateien auf dem Raspberry PI gespeichert werden sollen, kann hier der UPnP Server gestartet werden, der diese Dateien im Netzwerk verteilen kann.
    * **AirPlay:** Damit er ein echter Apple TV Klon wird muss diese Option eingeschaltet werden, somit kann von einem iPad, iPhone oder iTunes, Musik und Video an das RaspberryTV gesendet werden. Leider nur bis iTunes 10, Version 11 verweigert den Zugriff, obwohl es angezeigt wird.
    * **SMB Client**: Um die Mediendateien auch auf den RaspberryTV zu bekommen, sollte auch dieser aktiviert werden.

Das sind eigentlich die Einstellungen, die fur den Betrieb ausreichen und da genugende Tutorials im Netz existieren, verweise ich fur die weiteren Einstellungen auf diese.

## Fazit

Fur alle die noch kein Apple TV besitzen oder auch keines wollen, eine gunstige alternative. Das ganze kostet, so wie ich es verwendet habe, rund 55€. Spielt Musik, Videos und so weiter. Es ist ein offenes System, auf dem weiter Anwendungen, sowohl innerhalb von XBMC als auch auf der Raspbian Ebene, installiert werden konnen.

Es ist auch ideal fur Bastler, die ihr Apple TV hauptsachlich mit Jailbreak und XBMC verwenden oder dies gerne mit ihrem ATV3 tun wurden. Die den Macken von XBMC und dem, fur mich unubersichtlichen, Bedienungskonzept leben konnen.

Da ich bereits ein Apple TV besitze, von dem Bedienungskonzept uberzeugt bin und es bereits soweit in mein Infrastruktur integriert habe, dass keine Wunsche offen bleiben (auch ohne Jailbreak), bleibe ich beim Apple TV. Das liegt aber jetzt nicht am Raspberry PI, sondern an XBMC, mit dem ich auch auf anderen Plattformen noch nie warmgeworden bin.
