# Raspberry PI als AirPrint Server 

_Captured: 2017-03-05 at 11:48 from [www.welzels.de](http://www.welzels.de/blog/projekte/raspberry-pi/raspberry-pi-als-airprint-server/)_

Eigentlich bin ich recht zufrieden mit meinem Drucker, sei es von der Qualitat oder auch von der Ausstattung. Es handelt sich um ein sogenanntes Multifunktionsgerat, das sogar uber eine integrierte Netzwerkkarte verfugt, so dass bequem uber das LAN darauf zugreifen. Selbst auf de Scanner kann uber ein Webinterface zugegriffen werden. Aber dennoch merkt man, dass er in die Jahre gekommen ist; AirPrint unterstutzt er nicht.

Aber das lasst sich dank Raspberry PI andern.

Zuerst wie immer wenn man etwas neues installiert sudo apt-get update und sudo apt-get upgrade ausfuhren, damit alles auf dem neuesten Stand ist.

Danach mussen ein paar Pakete installiert werden:

Nach dem alles installiert ist, mussen an der CUPS Konfigurationsdatei einige Änderungen vorgenommen werden.

CUPS lauscht standardmaßig auf Port 631, allerdings nur auf dem Localhost. Dies soll er aber LAN ubergreifend tun, dazu muss Zeile 20 wie folgt geandert werden:

Dann die Markierten Zeilen einfugen:

35363738394041424344454647484950515253 
# Restrict access to the server...<Location />Order allow,denyAllow @Local</Location># Restrict access to the admin pages...<Location /admin>Order allow,denyAllow @Local</Location># Restrict access to configuration files...<Location /admin/conf>AuthType DefaultRequire user @SYSTEMOrder allow,denyAllow @Local</Location>

Damit die Änderungen ubernommen werden, muss CUPS neugestartet werden:

Um Änderungen an CUPS vornehmen zu konnen, muss nun der Benutzer _pi_, oder irgend ein anderer Nutzer, in die Gruppe _lpadmin_ aufgenommen werden (_sudo_ funktioniert hier nicht):

Danach erfolgt der Zugriff auf das Web-Interface von CUPS, durch Eingabe von https://[PI-IP-Adress]:631:

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/cups01-300x225.png)

Die Option „Freigeben von Druckern welche mit diesem System verbunden sind" aktivieren und „Einstellungen Ändern" drucken.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/cups02-300x225.png)

Es erscheint eine Anmeldeaufforderung, an der man sich mit _pi_ und dem Passwort fur _pi_ (sofern noch nicht geandert _raspberry_) anmeldet. Der CUPS-Server wird neu gestartet.

Jetzt gibt es zwei Moglichkeiten:

  * Der Drucker wird uber den USB-Port direkt an den Raspberry PI angeschlossen. Dann sollte er nun angeschlossen und angeschaltet sein.
  * Der Drucker ist bereits im Netzwerk, uber seine integrierte Netzwerkschnittstelle, innerhalb des LANs verfugbar (keine Druckerfreigabe am PC). Er sollt auch eingeschaltet sein.

Welche Moglichkeit gewahlt wurde ist fur das weitere vorgehen egal, es muss aber eine erfullt sein. Auf „Verfugbare Drucker auflisten" klicken und „diesen Drucker hinzufugen" wahlen.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/cups03-300x225.png)

In meinem Fall ist das ein „HP Photosmart C5180 All-in-One" der uber seine Netzwerkschnittstelle im LAN vorhanden ist. Nun entsprechend die Beschreibung und den Ort anpasse, „Diesen Drucker freigeben" aktivieren und weiter drucken.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/cups04-300x225.png)

Danach muss der Drucker Hersteller und das Modell angegeben werden, da dieser nun fur jeden Hersteller und Modell verschieden ist, verzichte ich auf ein Beispiel. Die Standardeinstellungen konnen eigentlich einfach ubernommen werden. Der Drucker ist nun eingerichtet, es empfiehlt sich noch eine Testseite zu drucken.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/cups05-300x225.png)

Nun zum Eigentlichen AirPrint.

**Update:** AirPrint ist mittlerweile in CUPS integriert und ab hier funktioniert es auch schon!

Es gibt hierfur nichts in der Regularen Raspbian Repository, allerdings gibt es in GitHub ein Python Skript das diesen Service erzeugt. Da es sich hierbei nicht um ein Teil des Regularen Raspbian handelt lege ich es in das Verzeichnis „/opt/AirPrint" (kann sein, dass es zu einem spateren Zeitpunkt noch benotigt wird). Der Download und die Installation wird wie folgt durchgefuhrt:

Wurde nichts in der Konsole ausgegeben (wie oben beschreiben), hat alles funktioniert und der Drucker steht zur Verfugung, sobald _avahi-daemon_ und _cups_ neu gestartet wurden.

Ist die Konsolenausgabe jedoch wie folgt:

Mussen noch zwei Dateien erzeugt und das Python Script erneut ausgefuhrt werden. Die erste Datei erzeugen:

Und den folgenden Inhalt eintragen:

Danach die zweite Datei erzeugen:

Und diesen Inhalt hinzufugen:

Das Script erneut ausfuhren und _avahi-daemon_ und _cups_ neu starten:

Nun sollte der Drucker verfugbar sein.
