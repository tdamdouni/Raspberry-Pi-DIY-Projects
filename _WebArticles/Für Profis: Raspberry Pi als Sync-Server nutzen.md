# Für Profis: Raspberry Pi als Sync-Server nutzen

_Captured: 2016-11-07 at 11:05 from [www.tecchannel.de](http://www.tecchannel.de/a/fuer-profis-raspberry-pi-als-sync-server-nutzen,2073712)_

Wir alle haben uns langst daran gewohnt, auf jedem Endgerat stets unsere aktuellen Termine und die Adressen von Freunden und Bekannten einsehen zu konnen. Die von Apple und Google unterhaltenen Infrastrukturen machen das moglich. Aber wer nicht mochte, dass die Nachrichtendienste dieser Welt auf Kontaktdaten zugreifen, braucht eine personliche Cloud, die er selbst im Griff im hat.

## Statt Owncloud das schlanke Baikal

Owncloud zahlt zu den bekanntesten Losungen, wenn es darum geht, eine private Cloud einzurichten. Das System bietet weit mehr als nur den Abgleich zwischen Kalendern. Dafur ist aber der Aufwand fur Installation und Pflege recht hoch. Eine schlanke Alternative ist Baikal, das seit zwei Jahren entwickelt wird. Ein wenig Software-Bastelei durfen Sie aber auch hier nicht scheuen. Die Software ist dazu gedacht, Kalender- und Kontaktdaten zentral zur Verfugung zu stellen und somit als Basis zur Synchronisation mit externen Geraten zu dienen. Die Anforderungen an den eingesetzten Server sind bescheiden, so dass sich Baikal perfekt zum Einsatz auf dem Raspberry Pi eignet. Sollten Sie jedoch vorhaben, auch Dokumente zentral uber einen Server anzubieten, ist Baikal nicht die favorisierte Losung.

**Baikal installieren: **Starten Sie die grafische Oberflache Ihres Raspberry, und offnen Sie dort ein Terminal. Die Verknupfung zum „LX Terminal" direkt auf dem Desktop fuhrt Sie in eine Konsole. Geben Sie zunachst

`sudo -i`

ein. Damit erhalten Sie die Rechte des Systemverwalters. Die Rechte benotigen Sie, damit Sie die Installationsdateien an die korrekten Stellen kopieren durfen. Selbstverstandlich konnen Sie sich auch fur jedes Kommando eigens die root-Rechte beschaffen, indem Sie bei den nachfolgenden Eingaben stets ein `sudo`voranstellen.

Im ersten Schritt mussen Sie auf dem Raspberry einen Webserver installieren. Sie haben hier mehrere Moglichkeiten. Die einfachste und schlankste Variante ist „lighttpd". Baikal selbst kann optional auch mit einem My-SQL-Server kommunizieren. Aber aus Grunden der Leistung soll in diesem Fall darauf verzichtet werden. Geben Sie im Terminal

`apt-get install lighttpd`

ein. Jetzt benotigen Sie noch einige zusatzliche Komponenten, damit Baikal auch dynamische HTML-Seiten erzeugen kann:

`apt-get install php5-common php5-cgi php5`

Ist die Installation erfolgreich, gilt es, die Ausfuhrung von PHP auf dem System zu erlauben. Dies geschieht mit dem Kommando

`lighty-enable-mod fastcgi-php`

Danach starten Sie den Server erstmals neu:

`service lighttpd restart`

![Nach der Ersteinrichtung: Beim Aufruf der IP-Adresse des kleinen Computers begrüßt Sie nach der Installation von lighttpd eine Platzhalterseite.](http://images.cio.de/images/computerwoche/bdb/2584754/840x473.jpg)

> _Nach der Ersteinrichtung: Beim Aufruf der IP-Adresse des kleinen Computers begrußt Sie nach der Installation von lighttpd eine Platzhalterseite._

Dies quittiert der Raspberry mit einem Herunterfahren des Dienstes und der Ruckmeldung, wenn der Webserver wieder gestartet ist. Der Raspberry Pi hat im internen Netzwerk vom Router bereits eine IP-Adresse zugewiesen bekommen. Um die Adresse herauszufinden, verwenden Sie im Terminal _ifconfig_. Das System meldet jetzt eine Menge an Informationen zuruck. Suchen Sie dort nach einem Eintrag „eth0", wenn die Verbindung per Kabel hergestellt wird. Die Ziffernfolge neben „inet addr" ist die gesuchte IP-Adresse. Öffnen Sie dann einen Browser auf einem anderen PC in Ihrem Netzwerk, und geben Sie dort die IP-Adresse des Raspberry ein. Sie sollten nun eine Begrußungsseite des Webservers sehen.

Wechseln Sie im Terminal mit _cd /var/www_in das Verzeichnis fur die Webdokumente. Dort liegen zum Beispiel statische HTML-Seiten, wenn Sie den kleinen Computer als Webserver betreiben. Nun geben Sie ein:

`wget http://baikal-server.com/get/baikal-flat-0.2.7.zip`

Das Tool wget sollte eigentlich immer installiert sein. Ist das nicht der Fall, so installieren Sie es mit _apt-get install wget_nach. wget holt die Installationsdateien von Baikal auf Ihren Rechner. Falls es zu einer Fehlermeldung kommt, besuchen Sie die Projektseite _http://baikal-server.com/_und kontrollieren, ob sich moglicherweise die Versionsnummer der Software geandert hat. Ist die Übertragung abgeschlossen, entpacken Sie mit

`unzip baikal-flat-0.2.7.zip`

das heruntergeladene Archiv. Dessen Inhalt verschieben Sie jetzt in ein Verzeichnis, dessen Namen Sie sich einpragen. Ist der Ort bereits passend, genugt das Umbenennen des entpackten Ordners. Das folgende Beispiel geht davon aus, dass der Ort passt und dass Sie die Installation spater im Ordner „kalender" erreichen wollen:

`mv baikal-flat kalender`

`cd /kalender`/

`mkdir db`

Damit die Installationsroutine starten kann, wird eine zusatzliche Datei benotigt. Diese legen Sie mit

`touch Specific/ENABLE_INSTALL`

Jetzt gilt es noch, einen speziellen Benutzer und eine passende Gruppe einzurichten

`sudo groupadd www-data`

sudo adduser www-data www-data

`sudo usermod -a -G` `www``-data` `www-data`

und abschließend die Rechte am Verzeichnis zu andern:

`chown -R www-data:www-data /var/www/kalender`

Statt „kalender" benutzen Sie den Verzeichnisnamen, den Sie sich vorher ausgesucht haben. Ab sofort konnen Sie Ihren neuen Server besuchen. Dazu nutzen Sie die IP-Adresse des Raspberry und fugen nach einem Schragstrich den Namen des Verzeichnisses hinzu. Ihr Server sollte Sie mit der Startseite der Installation begrußen.

  


## Baikal einrichten

![Baikal-Assistent: Die Dialoge zur Einrichtung sind sehr übersichtlich. Meist können Sie alle Vorgaben übernehmen.](http://images.cio.de/images/computerwoche/bdb/2584755/840x473.jpg)

> _Baikal-Assistent: Die Dialoge zur Einrichtung sind sehr ubersichtlich. Meist konnen Sie alle Vorgaben ubernehmen._

Nachdem Sie alle Programmkomponenten auf den Server ubertragen haben, beginnen Sie mit der Einrichtung der Installation. Im ersten Dialog des Assistenten vergeben Sie ein Passwort fur das Benutzerkonto des Administrators. Die weiteren Optionen lassen Sie am besten unangetastet. Es sei denn, Sie konnen bereits abschatzen, dass Sie nur die Synchronisation von Terminen nutzen wollen. Dann deaktivieren Sie das Carddav-Protokoll. Klicken Sie auf „Save Changes". Auf der nachfolgenden Seite geht es um die Einrichtung der Datenbank. Auch hier mussen Sie keine Änderungen vornehmen. Der Schritt ist vorwiegend fur Nutzer, die einen My-SQL-Server verwenden. Damit ist die Installation bereits abgeschlossen. Sie besuchen die Log-in-Seite nach einem Klick auf „Start".

Loggen Sie sich nun als Administrator in Ihre Installation ein. Wahlen Sie dort aus der oberen Navigation den Eintrag „Users and resources", und klicken Sie danach in der oberen Ecke auf „Add user". Es mussen nur wenige Felder gefullt werden. Mit „Save Changes" legen Sie den Nutzer an. Jeder Nutzer kann auf einen oder mehrere Kalender zugreifen. Welche das sind, bestimmen Sie mit einem Klick auf „Calendars" neben dem Benutzernamen. Über den Link konnen Sie auch neue Kalender einrichten. Sobald Sie den Kalender zugewiesen oder einen neuen angelegt haben, steht dieser auf dem Server zur Verfugung.

  


Damit Sie von jedem Ort auf die Daten des Raspberry Pi zugreifen konnen, sind drei weitere Arbeiten erforderlich. Am Router stellen Sie ein, dass Ihr Raspberry Pi stets die gleiche IP-Adresse zugewiesen bekommt. Dazu mussen Sie sich in aller Regel nur die gerade verbundenen Gerate ansehen, den Raspberry identifizieren und sich dessen MAC-Adresse notieren. In den Optionen des DHCP-Servers des Routers suchen Sie sich dann eine freie Adresse aus. Das Zuweisen einer festen IP-Adresse bietet den Vorteil, dass Sie etwa aus Wartungsgrunden im internen Netz die Admin-Oberflache stets unter der gleichen Adresse erreichen. Außerdem konnen Sie das Netzwerk so konfigurieren, dass Datenzugriffe von außen stets an diese Adresse weitergereicht werden.

Dies ist dann auch bereits die zweite Arbeit, die Sie erledigen mussen: Die meisten Router verfugen uber eine Firewall, die keine Zugriffe von außen zulasst. Das mussen Sie, zumindest fur die IP-Adresse des Raspberry, andern.

Schließlich buchen Sie ein kostenloses Konto bei einem Anbieter fur dynamische DNS-Dienste (wie [www.noip.com](http://www.noip.com/)). Viele Router wie die Fritzbox oder Gerate von Dlink halten bereits die Eingabe der Zugangsdaten fur solche Dienste bereit. Damit bleibt Ihr Raspberry stets unter dem Domain-Namen erreichbar (den Sie beim Anbieter eingerichtet haben), obwohl Ihr Provider Ihnen einmal pro Tag eine neue externe IP-Adresse zuweist.

  
![App für Android: Das kostenpflichtige Caldav Sync vereinfacht für einen kleinen Preis die Synchronisation erheblich.](http://images.cio.de/images/computerwoche/bdb/2584756/840x473.jpg)

> _App fur Android: Das kostenpflichtige Caldav Sync vereinfacht fur einen kleinen Preis die Synchronisation erheblich._

Steht die Infrastruktur, richten Sie die Kalender auf Ihren mobilen Geraten ein. Auf iPhone oder iPad wechseln Sie dazu in die „Einstellungen". Unter „Mail, Kontakte, Kalender" wahlen Sie unter „Accounts" die Option, um ein neues Konto hinzuzufugen. Im nachfolgenden Dialog markieren Sie „Andere". Nutzen Sie nun „CalDAV-Account".Als Angaben benotigen Sie Benutzernamen und Passwort, wie Sie diese als Admin fur das jeweilige Konto eingerichtet haben.

Zum anderen brauchen Sie den Zugriff auf den Server. Die URL zum Server sieht zur Einrichtung eines Kalenders im Prinzip so aus:

`http://www.[server].tld/[baikal_ordner]/cal.php/principals/[benutzer]`

Sobald Sie alle Angaben gemacht haben, pruft das Gerat den Zugriff automatisch. Android besitzt keine unmittelbare Unterstutzung fur das Caldav-Protokoll. Die Funktion mussen Sie also bei Bedarf mit einer Dritt-Software nachrusten, zum Beispiel mit Caldav Sync, das zum Preis von rund 2,50 Euro im Google Playstore zu bekommen ist.

Die Installation von Baikal ist auch dazu in der Lage, Aufgaben zu speichern. Ob diese sich mit Ihrem Gerat oder Computer abgleichen lassen, ist eine Frage der eingesetzten Software.

  


## Adressbucher anlegen

Wenn Sie wollen, richten Sie auf dem Server auch zentrale Adressbucher ein. Sie mussen Sie dazu den Admin-Bereich aufrufen, den Sie durch ein der Server-URL nachgestelltes _/admin_erreichen. Über „Users and ressources" rufen Sie die Benutzerverwaltung auf. Jeder Nutzer hat zumindest Zugriff auf ein personliches (default) Adressbuch. Dessen Eigenschaften andern Sie einfach mit einem Klick auf „Adress Books" neben dem Namen der Person.

Das Einrichten der Adressbucher funktioniert bei Android und iOS wieder unterschiedlich. Auf dem Mac und iOS-Geraten ist der Weg wie beim Kalender beschrieben. Fur Android besorgen Sie sich eine App wie Carddav-Sync aus dem Google Playstore, und Sie geben als Pfad

`http://[servername].tld/[baikal_ordner]/card.php/addressbooks/[benutzer]/default`

zu Ihrem Adressbuch ein.

  


## Betriebssystem installieren

Dieser Beitrag geht davon aus, dass Sie bereits einen Raspberry Pi besitzen, auf dem Debian Wheezy lauft. Wenn nicht, ist das auch kein Problem: Besorgen Sie sich einen Raspberry Pi, eine SD-Speicherkarte und am besten ein USB-Netzteil. Eine USB-Tastatur, eine Maus sowie einen Monitor, den Sie per HDMI-Kabel anschließen, vervollstandigen die Ausstattung.

Auf der Seite des Projekts ([www.raspberrypi.org/downloads/](http://www.raspberrypi.org/downloads/)) laden Sie Noobs herunter, entpacken das Archiv und kopieren den Inhalt vollstandig auf die SD-Karte. Stecken Sie danach die Karte in den Raspberry, verkabeln Sie alles und starten Sie den Rechner durch das Anschließen an die Stromquelle.

Nach einigen Augenblicken werden Sie von einem Auswahlmenu begrußt. Hier entscheiden Sie sich dann fur die Installation von Raspbian. Sie mussen nur noch den Anweisungen auf dem Bildschirm folgen, und schon ist der Minirechner bereit fur die weiteren Schritte. Wenn Sie sich an der Eingabeaufforderung befinden, dann genugt der Befehl _startx_, um den grafischen Desktop zu starten.

([PC-Welt/](http://www.pcwelt.de/ratgeber/Fuer_Profis__Raspberry_Pi_als_Sync-Server_nutzen-Kalender-Synchronisation-8922704.html)ad)
