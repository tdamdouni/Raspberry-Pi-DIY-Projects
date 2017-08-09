# Homebridge kinderleicht auf einem Raspberry Pi installieren

_Captured: 2017-05-06 at 15:41 from [smartapfel.de](https://smartapfel.de/homebridge-kinderleicht-auf-einem-raspberry-pi-installieren/)_

![Anleitung: Homebridge installieren](https://smartapfel.de/wp-content/uploads/2017/01/homebridge-installieren-696x232.jpg)

Immer mehr HomeKit Gerate sind auch auf dem deutschen Markt verfugbar. Trotzdem hat der ein oder andere noch nicht-kompatible Hardware Zuhause liegen oder mochte ein Gerat in HomeKit einbinden, fur das es noch kein offizielles Produkt gibt. Wir verwenden beispielsweise den [Logitech Harmony Hub](https://www.amazon.de/Logitech-915-000262-Harmony-Hub-Schwarz/dp/B014GXQ9YW?tag=hktips-2017-01-08-raspberrypi-21) um uber HomeKit unseren Fernseher einzuschalten.

Aus diesem Grund haben wir vor knapp einem Jahr eine [Anleitung zur Installation von Homebridge auf einem Raspberry Pi](https://smartapfel.de/anleitung-homebridge-auf-einem-raspberry-pi-einrichten/) veroffentlicht. Unsere Anleitung war fur die Technikversierten unter euch gedacht.

Mit dieser Neuauflage unserer beliebten Anleitung kann wirklich jeder Homebridge installieren. Der Entwickler Niklas von Weihe hat namlich eine App veroffentlicht, die nicht nur fur euch die Installation von Homebridge selbst und einigen Plugins ubernimmt, sondern auch eine Oberflache zur einfachen Verwaltung bietet.

Mit einem Klick kann der Raspberry Pi oder Homebridge neu gestartet, die Identitat gewechselt oder eine Konsole geoffnet werden. Wir haben versucht, die Anleitung so kleinschrittig wie moglich zu schreiben. Sollte dennoch irgendetwas unklar sein, konnt ihr das gerne in die Kommentare schreiben.

Solltet ihr Homebridge bereits einsetzen und ihr mochtet die App trotzdem nutzen, empfehlen wir euch eine Neuinstallation. Die Erfahrung hat gezeigt, dass es bei der Einbindung von bestehenden Installationen zu Problemen kommen kann.

## Die benotigten Komponenten

Bevor wir loslegen konnen, benotigt ihr naturlich noch die entsprechende Hard- und Software. Die folgenden Links fuhren euch direkt zu Amazon bzw. in den App Store. Wahlweise konnt ihr auch auf [dieses Starterset](https://www.amazon.de/Vilros-Raspberry-Pi-Complete-Kit-Enthalt/dp/B01DC6MKAQ?tag=hktips-2017-01-08-raspberrypi-21) zuruckgreifen. Darin ist alles enthalten und ihr benotigt dann nur noch die App.

## SD Karte vorbereiten

Bevor uns die App nun den großten Teil der Arbeit abnehmen kann, mussen wir zunachst die SD Karte vorbereiten. Dazu mussen wir diese mit dem Format „MS-DOS(FAT)" formatieren.

Auf dem Mac konnt ihr das im Festplattendienstprogramm, das ihr im _Programme_ Ordner unter _Dienstprogramme_ findet, machen. Dort einfach die SD Karte auswahlen, auf _Loschen_ klicken, als Name _RaspberryPi_ eingeben, als Format _MS-DOS Dateisystem (FAT)_ auswahlen und erneut auf _Loschen_ klicken.

![Mac SD Karte formatieren](https://smartapfel.de/wp-content/uploads/2017/01/mac-formtieren-1.jpg)

Unter Windows konnt ihr das im Windows Explorer erledigen. Dort einfach einen Rechtsklick auf die SD Karte machen, _Formatieren_ auswahlen, als Format _FAT32_ selektieren, als Name _RaspberryPi_ eingeben und auf _Start_ klicken.

Nun fehlt noch das vorbereitete Betriebssystem. Das konnt ihr einfach [hier](https://sharing.nvw-dev.com/Homebridge/NOOBS.zip) herunterladen. Nach dem Download einfach den Inhalt entpacken und alle Dateien aus dem Ordner auf die SD Karte kopieren. Sollten die Boardmittel nicht ausreichen, konnt ihr zum Entpacken auf dem Mac [The Unarchiver](https://geo.itunes.apple.com/de/app/the-unarchiver/id425424353?mt=12&at=1001l8it) und unter Windows [WinRAR](http://www.win-rar.com/download.html?&L=1) verwenden. Fertig.

## Kinderleichte Installation dank der Homebridge App

Solltet ihr euch die [App von Niklas von Weihe](https://itunes.apple.com/de/app/homebridge-fur-raspberrypi/id1123183713?mt=8&at=1001l8it) noch nicht installiert haben, dann ist jetzt der richtige Zeitpunkt. Bevor die App allerdings alles installieren kann, musst ihr naturlich die SD Karte in den Raspberry Pi einlegen, ein Ethernet Kabel anschließen und das Netzteil einstecken.

Nun ist es ganz wichtig, dass ihr ungefahr 20 Minuten wartet. Solange passiert namlich noch etwas Magie auf dem Raspberry Pi, bevor die App dann die eigentliche Einrichtung vornehmen kann.

Öffnet nach 20 Minuten die App und geht ganz unten auf _Fortfahren_. Auf der nachsten Seite wird euch noch einmal angezeigt, wie der Raspberry Pi nun angeschlossen sein sollte. Das konnt ihr einfach mit _Check_ bestatigen.

Nun musst ihr aus der Liste euren Raspberry Pi auswahlen. Solltet ihr ihn nicht finden, schaut am besten auf der Benutzeroberflache eures Routers, welche IP Adresse der Raspberry Pi bekommen hat und gebt diese manuell ein. In der Regel sollte euch der Raspberry Pi jedoch angezeigt werden.

Im nachsten Fenster musst ihr noch ein neues Passwort vergeben, ansonsten konnt ihr nicht auf _Speichern_ gehen. Anschließend konnt ihr auf _Betankung starten_ drucken und die App updatet das Betriebssystem und installiert Homebridge. Dieser Schritt dauert noch einmal ungefahr 10-20 Minuten. In der Zwischeneit konnt ihr beispielsweise in unseren [Reviews](https://smartapfel.de/category/reviews/) stobern.

Damit der Raspberry Pi nicht immer uber ein Ethernet Kabel mit dem Router verbunden sein muss, konnt ihr nun noch das WLAN konfigurieren. Anschließend wird der Raspberry Pi neugestartet und ist einsatzbereit.

## Homebridge zu HomeKit hinzufugen

Die Installation von Homebridge ist nun vollstandig abgeschlossen. Das einzige das noch fehlt, ist das Hinzufugen zu HomeKit und naturlich die Installation von Plugins.

Der HomeKit Code, den ihr zum Hinzufugen benotigt, wird in der App oben rechts angezeigt. Öffnet einfach eine beliebige HomeKit App, z.B. Home von Apple, und fugt ein neues Gerat hinzu. Wahlt nun einfach Homebridge aus und gebt den HomeKit Code aus der Homebridge App ein.

![Homebridge HomeKit Code](https://smartapfel.de/wp-content/uploads/2017/01/homebridge-code-300x300.jpg)

Sollte eure Homebridge nicht angezeigt werden, konnt ihr in der App unter _Aktionen_ die _Identitat wechseln_. Danach den Raspberry Pi neustarten und schon solltet ihr Homebridge zu HomeKit hinzufugen konnen.

## Plugin aus Auswahl installieren

Niklas von Weihe stellt in seiner App bereits eine Auswahl an Plugins zur Verfugung. Diese konnen ganz bequem uber die App hinzugefugt werden. Dafur geht ihr einfach in der Navigation auf _Add Accessories_ und wahlt das entsprechende Plugin aus.

![Homebridge Add Accessories](https://smartapfel.de/wp-content/uploads/2017/01/homebridge-add-300x300.jpg)

Falls noch etwas konfiguriert werden muss, konnt ihr das auf der darauffolgenden Seite machen. Ein Klick auf _Installieren_ erledigt dann den Rest.

So konnt ihr beispielsweise den [Logitech Harmony Hub](https://www.amazon.de/Logitech-915-000262-Harmony-Hub-Schwarz/dp/B014GXQ9YW?tag=homekitips-21) zur Steuerung eures Fernsehers mit nur zwei Klicks zu HomeKit hinzufugen.

Auch das People Plugin, mit dem ihr eine Anwesenheitserkennung in HomeKit einbinden konnt, kann uber die Auswahl kinderleicht installiert werden. Dazu wahlt ihr einfach die Gerate (Idealerweise pro Bewohner das passende Smartphone) aus und fugt diese hinzu. Schon konnt ihr in HomeKit sehen, ob sich das Smartphone des Bewohners im Netzwerk befindet.

## Manuell Plugins installieren

Die App wird zwar standig um neue Plugins erweitert, es kann aber vorkommen, dass ihr ein Plugin installieren wollt, das noch nicht dabei ist. Eine Liste mit Plugins findet ihr [hier](https://www.npmjs.com/browse/keyword/homebridge-plugin). Auch das ist kein Problem, kann aber je nach Konfigurationsdatei etwas muhsam und schwieriger sein.

Ihr konnt entweder ein Plugin uber das _Generische Plugin_ in der App installieren oder euch uber SSH auf den Raspberry Pi aufschalten.

### Plugin uber die App hinzufugen

Fur die Variante uber die App wahlt ihr einfach _Generisch_ unter _Add Accessories_ aus. Anschließend musst ihr den vollstandigen Paketnamen, den Schlussel und den Typ angeben.

Der Paketname beginnt immer mit _homebridge_. Den Schlussel und den Typ findet ihr in der Beispiel-Konfiguration auf den entsprechenden Plugin Seiten. Fur das [IFTTT Plugin](https://www.npmjs.com/package/homebridge-ifttt) wurde es demnach wie folgt aussehen.

![Homebridge IFTTT](https://smartapfel.de/wp-content/uploads/2017/01/homebridge-ifttt-300x300.jpg)

Jetzt wird es tatsachlich etwas schwieriger. Die Konfigurationsdatei von IFTTT ist namlich etwas großer. Daran lasst sich jedoch sehr gut zeigen, welche Typen nun angelegt werden mussen.

Unter _Plattform_ sollte im _Experten_ Tab nun das IFTTT Plugin angezeigt werden. Falls nicht, konnt ihr den Eintrag uber das kleine Plus neben _Plattform_ hinzufugen. _Generic_ kann einfach in den Anzeigenamen umbenannt werden. _RcSwitch_ muss immer durch den Schlussel ersetzt werden. In beiden Fallen konnen wir hierbei einfach _IFTTT_ verwenden.

![Homebridge Plugin IFTTT](https://smartapfel.de/wp-content/uploads/2017/01/homebridge-plugin-ifttt-300x300.jpg)

Nun mussen wir uns die Beispielkonfiguration mal genauer ansehen. In der App konnen wir _Strings_, _Arrays_ und _Dictionaries_ anlegen. Diese Typen finden wir auch in der Konfigurationsdatei wieder. Eckige Klammern ergeben immer ein _Array_, geschweifte Klammern ein _Dictionary_ und Text ist immer ein _String_.

Fur die IFTTT Beispielkonfiguration musstet ihr das folgendermaßen anlegen. Den IFTTT Maker Key findet ihr ubrigens [hier](https://ifttt.com/services/maker/settings) (Die URL ohne _https://maker.ifttt.com/use/_).

![Homebridge App Erklärung](https://smartapfel.de/wp-content/uploads/2017/01/Homebridge-Anleitung.jpg)

Die Einruckung gibt an, wo ihr die jeweiligen Zeilen erzeugen musst. Zeile 8-10 z.B. in dem Array, das ihr in Zeile 7 hinzugefugt habt. Zeile 11 in dem Array, das ihr in Zeile 10 hinzugefugt habt und Zeile 12-14 in dem Dictionary aus Zeile 11.

Am Ende sollte die Konfiguration in etwa so aussehen.

![IFTTT Plugin Konfiguration](https://smartapfel.de/wp-content/uploads/2017/01/ifttt-konfiguration-1024x614.jpg)

Wie gesagt, die Konfiguration so anzulegen ist gerade bei großen Konfigurationsdateien sehr muhsam. Dafur musst ihr euch jedoch nicht per SSH aufschalten, sondern konnt alles uber die App erledigen.

### Plugin uber SSH hinzufugen

Um ein Plugin uber SSH hinzuzufugen mussen wir uns naturlich zunachst aufschalten. Auf dem Mac konnt ihr einfach das Terminal verwenden und unter Windows das kostenlose Programm [Putty](https://www.google.de/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwi0sdTLp4bLAhWF2ywKHTOzCyIQFgglMAE&url=http%3A%2F%2Fwww.chiark.greenend.org.uk%2F~sgtatham%2Fputty%2Fdownload.html&usg=AFQjCNEawi7s0aRUeJP3qKnncgvPiSqZYA&sig2=yKhRKd0SqBoOekvjWSUTeA).

Die IP-Adresse musst ihr in den folgenden Schritten entsprechend anpassen. Über den folgenden Befehl konnt ihr euch verbinden.

Sollte bei euch ein Fehler auftreten, konnt ihr den folgenden Befehl eingeben und es danach erneut versuchen.

Nun konnt ihr beliebige Plugins aus [dieser Liste](https://www.npmjs.com/browse/keyword/homebridge-plugin) installieren. Fur das IFTTT Plugin lautet der Befehl zur Instalation wie folgt.

Nun musst ihr noch die Konfigurationsdatei anpassen. Da die App Homebridge als root installiert hat, findet ihr die Konfiguration unter einem anderen Pfad als bei der alten Anleitung. Zum Öffnen gebt ihr einfach folgenden Befehl ein.

Anschließend konnt ihr die Konfiguration entsprechend anpassen. Ob der Inhalt der Konfigurationsdatei valide ist, konnt ihr [hier](http://jsonlint.com/) uberprufen. Kopiert dazu einfach den kompletten Inhalt der Datei in das entsprechende Feld der Webseite und klickt auf _Validate JSON_. Fehler, wie z.B. vergessene oder falsch gesetzte Klammern, werden euch dann angezeigt.

Mit ctrl + o speichert und mit ctrl + x schließt ihr die Konfigurationsdatei wieder. In der App konnt ihr noch schnell Homebridge uber den _Aktionen_ Tab neu starten. Fertig.

## Fehlerbehebung

Sollte Homebridge mal nicht starten, kann es sinnvoll sein unter _Aktionen_ die _Konsole_ zu offnen. Dort konnt ihr versuchen mit dem folgenden Befehl Homebridge manuell zu starten.

In der Regel sollte euch dann eine Fehlermeldung um die Ohren fliegen, mit der man entweder etwas anfangen oder danach googlen kann.

Ansonsten schadet es naturlich auch nicht mal den Stecker des Raspberry Pi zu ziehen und wieder einzustecken.
