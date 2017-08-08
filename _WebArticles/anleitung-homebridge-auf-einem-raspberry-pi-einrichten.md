# Anleitung: Homebridge auf einem Raspberry Pi einrichten

_Captured: 2017-05-06 at 15:39 from [smartapfel.de](https://smartapfel.de/anleitung-homebridge-auf-einem-raspberry-pi-einrichten/)_

![Raspberry Pi HomeKit](https://smartapfel.de/wp-content/uploads/2016/02/raspberry-pi-homekit-696x232.jpg)

Obwohl immer mehr Hersteller die Entwicklung von HomeKit kompatiblen Produkten ankundigen, gibt es in Deutschland bislang nur wenige.

Wir empfehlen euch einen Abstecher in unsere [HomeKit Produktubersicht](https://homekit.tips/offizielle-homekit-produkte/), um einen Überblick uber erhaltliche Produkte zu erhalten.

Um bereits vorhandene, aber nicht kompatible Gerate in HomeKit einzubinden, kann Homebridge eingesetzt werden.

Bislang haben wir euch zur Installation auf den Blog unserer sehr geschatzten Freunde von [meintechblog.com](http://meintechblog.com) weitergeleitet. Allerdings zeigt Jorg vorwiegend die Integration von FHEM in Homebridge.

Heute mochten wir euch eine Anleitung bereitstellen, die euch die Installation von Homebridge auf dem Raspberry Pi erklart. Außerdem mochten wir euch zeigen, wie man Plugins installiert, um die einzelnen Gerate schlussendlich einzubinden.

## Benotigte Komponenten

Bevor ihr mit der Anleitung beginnen konnt, musst ihr euch naturlich einen Raspberry Pi, ein Netzteil, eine SD Karte und optional ein Gehause zulegen. Im folgenden eine Übersicht der Komponenten, die wir in dieser Installation verwenden. Die Links fuhren euch direkt zu den Produkten bei Amazon.

## Vorbereitung des Raspberry Pi

Zunachst muss ein Betriebssystem auf der SD Karte installiert werden. Dazu kann ganz einfach [noobs](https://www.raspberrypi.org/downloads/noobs/) verwendet werden. Es reicht ubrigens aus, wenn ihr noobs lite verwendet.

Naturlich konnt ihr euch auch fur ein anderes Betriebssystem als Raspbian entscheiden und das Ganze anders installieren. Allerdings ist noobs, wie der Name schon sagt, fur die ganz einfache Installation entwickelt worden.

Verbindet die SD Karte mit eurem Computer und formatiert diese. Ein Tool zum Formatieren findet ihr [hier](https://www.sdcard.org/downloads/formatter_4/eula_mac/).

Anschließend kopiert ihr die entpackten Dateien von noobs auf die SD Karte. Ganz wichtig: Sollten die Dateien in einem Ordner entpackt sein, dann kopiert nur die Dateien und nicht einfach den Ordner auf die SD Karte.

Das Ganze sollte dann ungefahr so aussehen:

![noobs Dateien auf der SD Karte](https://smartapfel.de/wp-content/uploads/2016/02/noobs-sd-karte.jpg)

Danach konnt ihr die SD Karte in eurem Raspberry Pi einlegen und diesen mit dem Netzwerkkabel und einer Maus verbinden. Anschließend noch ein HDMI Kabel fur den Monitor oder Fernseher anschließen und das Netzteil einstecken.

Nach einigen Sekunden solltet ihr folgenden Dialog sehen, in dem ihr das Betriebssystem auswahlen konnt. Wir haben uns fur Raspbian entschieden.

![noobs Installationsdialog](https://smartapfel.de/wp-content/uploads/2016/02/noobs-install.jpg)

Solltet ihr noobs lite auf die SD Karte kopiert haben, dauert die Installation nun ein wenig, da die benotigten Dateien aus dem Internet heruntergeladen werden.

## Mit dem Raspberry Pi verbinden

Ab jetzt trennen wir die Maus und das HDMI Kabel vom Raspberry Pi und schalten uns von unserem Computer auf den Raspberry Pi auf. Die folgenden Schritte konntet ihr aber auch direkt auf dem Raspberry Pi ausfuhren.

Wir finden es jedoch bequemer vom Schreibtisch aus zu arbeiten und den Raspberry Pi beim Router stehen zu lassen. Außerdem fehlt uns eine USB Tastatur

Ihr benotigt nun die IP-Adresse des Raspberry Pi. Dazu konnt ihr einfach in eurem Router nachsehen. Auf dem Mac konnt ihr auch das kostenlose Programm [LanScan](https://itunes.apple.com/de/app/lanscan/id472226235?mt=12) verwenden.

Bei uns lautet die IP Adresse 10.0.1.5. Ihr musst in den folgenden Schritten die IP Adresse entsprechend anpassen.

Wenn ihr die IP Adresse herausgefunden habt, konnt ihr auf dem Mac das Terminal offnen oder unter Windows das kostenlose Programm [Putty](https://www.google.de/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwi0sdTLp4bLAhWF2ywKHTOzCyIQFgglMAE&url=http%3A%2F%2Fwww.chiark.greenend.org.uk%2F~sgtatham%2Fputty%2Fdownload.html&usg=AFQjCNEawi7s0aRUeJP3qKnncgvPiSqZYA&sig2=yKhRKd0SqBoOekvjWSUTeA) verwenden.

Im Terminal konnt ihr euch nun mit folgendem Befehl mit dem Raspberry Pi verbinden.

Sollte bei euch eine Fehlermeldung erscheinen, muss der folgende Befehl eingegeben und anschließend der obige Login Befehl erneut ausgefuhrt werden.

Das Standardpasswort lautet _raspberry_. Nun seid ihr mit dem Raspberry Pi verbunden und konnt direkt Befehle ausfuhren.

Zunachst sollte mit dem folgenden Befehl das Standardpasswort geandert werden.

Dazu musst ihr das alte Passwort _raspberry_ und danach zweimal das neue Passwort eingeben.

Nun muss noch die richtige Zeitzone eingestellt werden. Der folgende Befehl offnet dazu eine grafische Benutzeroberflache.

## Installation der benotigten Pakete

Jetzt konnen zunachst die Standard System Pakete auf den neuesten Stand gebracht werden.

Damit ihr Homebridge installieren konnt, musst ihr noch NodeJS installieren.

Homebridge benotigt außerdem Avahi, ein DNS Discovery Tool.

## Installation von Homebridge

Nun konnen wir uns endlich um die eigentliche Installation von Homebridge mit dem folgenden Befehl kummern.

Die Installation dauert ein wenig. Doch anschließend konnt ihr Homebridge schon starten.

Allerdings erhaltet ihr noch eine Fehlermeldung, da ihr bislang kein Plugin installiert habt.

Doch zunachst musst ihr noch die Konfigurationsdatei anpassen. Dazu erstellt ihr den benotigten Ordner und offnet die Konfigurationsdatei.

Nun tragt ihr eine Grundkonfiguration in die Datei ein.

Mit ctrl + o speichert und mit ctrl + x schließt ihr die Konfigurationsdatei wieder.

Startet ihr Homebridge mit dem Befehl _homebridge_ erneut, erscheint nun der Code mit dem ihr Homebridge mit HomeKit verbinden konnt. Dazu konnt ihr einfach eine HomeKit App, wie beispielsweise [myHome](https://homekit.tips/app-store-neuzugang-myhome-im-test/) oder [Home](https://homekit.tips/app-getestet-home-einfache-hausautomatisierung/) verwenden.

Einfach ein neues Gerat uber die App hinzufugen und den Code scannen oder manuell eingeben.

![HomeKit Code](https://smartapfel.de/wp-content/uploads/2016/02/homekit-code.jpg)

Fertig. Homebridge ist nun installiert und kann verwendet werden. Fur die weiteren Befehle mussen wir das Ganze jedoch uber ctrl + c erst noch einmal abbrechen.

## Homebridge automatisch starten

Damit Homebridge jedes Mal beim Starten vom Raspberry Pi automatisch mit gestartet wird, musst ihr noch ein paar Befehle ausfuhren.

Schließlich mochtet ihr euch beispielsweise nach einem Stromausfall nicht erst wieder auf den Raspberry Pi aufschalten mussen und Homebridge manuell starten.

Fur den automatischen Start wird forever benotigt.

Nun konnt ihr das Script anpassen.

Dazu einfach folgenden Code per Copy and Paste einfugen.

Die Datei kann wieder mit ctrl + o gespeichert und mit ctrl + x geschlossen werden.

Mit dem folgenden Befehl werden noch die notigen Rechte eingeraumt.

Jetzt muss der automatische Start nur noch aktiviert werden.

Nun wird Homebridge automatisch beim Starten des Raspberry Pi ausgefuhrt und kann uber den Befehl _sudo service homebridge __start_ manuell gestartet, bzw. uber _sudo service homebridge __stop_ gestoppt werden.

## Installation von Homebridge Plugins

So wirklich machtig wird Homebridge naturlich erst durch Plugins. Es gibt fur die unterschiedlichsten Gerate und Dienste welche. Ihr konnt einfach mal auf [dieser Seite](https://www.npmjs.com/search?q=homebridge-plugin) ein wenig stobern.

Da wir einen [Logitech Harmony Hub](https://www.amazon.de/Logitech-Harmony-Control-Fernbedienung-schwarz/dp/B00C80JGGO?tag=hktips-2016-02-20-raspberrypi-21) haben, mochten wir kunftig unseren Fernseher auch mit Siri steuern und installieren das [Harmony Plugin](https://www.npmjs.com/package/homebridge-harmonyhub). Ihr konnt naturlich auch jedes andere Plugin installieren.

Um das Harmony Plugin zu installieren, reicht folgender Befehl.

Nun musst ihr nur noch Homebridge in der Konfigurationsdatei mitteilen, dass ihr das Plugin verwenden mochtet. Dazu offnet ihr die Datei erneut mit dem folgenden Befehl.

Ihr musst zwischen die eckigen Klammern von _„platforms":_ diese Zeilen hinzufugen.

Dabei konnt ihr den Namen frei wahlen. Die erste Zeile durft ihr jedoch nicht verandern.

Die Datei sollte dann ungefahr so aussehen.

![Config Datei](https://smartapfel.de/wp-content/uploads/2016/02/config-file.jpg)

Mit ctrl + o speichert und mit ctrl + x schließt ihr die Datei wieder.

Wenn ihr jetzt die HomeKit App erneut offnet, solltet ihr schon eure Harmony Aktivitaten sehen. Falls nicht, startet Homebridge oder den Raspberry Pi einfach noch einmal neu.

Bei den Plugins ist immer eine Installationsanleitung mit dabei. So konnt ihr Homebridge beispielsweise um ein Plugin fur [IFTTT](https://www.npmjs.com/package/homebridge-ifttt), [Netatmo](https://www.npmjs.com/package/homebridge-netatmo), [Wemo](https://www.npmjs.com/package/homebridge-wemo) oder viele andere Gerate und Dienste erweitern.
