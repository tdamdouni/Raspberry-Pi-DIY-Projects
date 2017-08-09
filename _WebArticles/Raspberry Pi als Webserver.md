# Raspberry Pi als Webserver 

_Captured: 2015-12-15 at 11:46 from [www.raspberry-pi-geek.de](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver)_

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-webserver/aa_himbeeren-loeffel_123rf-20613856_volodymyrkrasyuk_123rf.jpg2/2745-1-ger-DE/AA_himbeeren-loeffel_123rf-20613856_VolodymyrKrasyuk_123RF.jpg_large.jpg)

> _(C) Volodymyr Krasyuk, 123RF_

Nicht umsonst entwarf die Raspberry Pi Foundation ihren Minicomputer fur Ausbildungszwecke - gerade auch fur den Anwendungsfall eines Webservers eignet er sich hervorragend. Die nur begrenzt leistungsfahige Hardware erlaubt anschaulich zu lernen, welche Vorgehensweisen zu viel Last erzeugen und somit einen weitaus starkeren Server bei einer großen Nutzerzahl ebenfalls in die Knie zwingen wurden - beispielsweise schlecht programmierte PHP-Skripte.

Dennoch ist der RasPi machtig genug, um die grundlegenden Konfigurationsschritte innerhalb des fur Webserver typischen Debian-Systems zu uben. So kann man eigene Webseiten erstellen und testen, ohne den Gefahren von Angriffen ausgesetzt zu sein: Die NAT-Firewall des heimischen Routers beschutzt den Raspberry Pi. Und wenn man den kleinen Rechner zwischendurch doch wieder fur etwas anderes verwenden mochte, bootet man ihn einfach von einer anderen SD-Karte.

Ein Raspberry Pi im Server-Einsatz muss "headless" funktionieren, also ohne Monitor. Die Verwaltung erfolgt uber eine SSH-Verbindung von einem anderen Rechner im LAN aus. Dazu gehen Sie wie im vorigen Artikel [[1]](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver/\(offset\)/4) ab Seite 42 beschrieben vor: Sie schalten bei einer frischen Raspbian-Installation den Desktop aus, aktivieren den SSH-Server und melden sich uber die vorher ermittelte IP-Adresse des Raspberry mit einer SSH-Verbindung an.

Haben Sie jedoch keinen PC in Reichweite und mochten stattdessen den Raspberry Pi nicht nur als Webserver einsetzen, sondern auf ihm auch im Webbrowser die Seiten betrachten, dann verzichten Sie auf die im vorigen Artikel beschriebenen Schritte. Stattdessen geben Sie im Browser als IP-Adresse die 127.0.0.1 an, also die Referenz fur den lokalen PC (sprich: den RasPi).

#### Apache & Co

Apache ist mit Abstand der beliebteste Webserver: Anfang 2013 benutzten ihn 53 Prozent aller Internet-Sites, der nachste Konkurrent erreichte nur einen Wert von unter 20 Prozent [[2]](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver/\(offset\)/4). Schon diese Verbreitung macht Apache zu einer guten Wahl: So fallt es etwa bei Problemen leicht, in Internet-Foren eine Losung zu finden, falls die ausfuhrliche Dokumentation keine Antwort bietet. Dennoch gibt es Falle, in denen ein anderer Webserver die bessere Wahl darstellt - dazu spater noch mehr.

Residiert auf der SD-Karte des RasPi die neueste Raspbian-Version, installieren Sie als erstes uber das Kommando `sudo apt-get install apache2` den Webserver. Bei alteren Versionen fuhrte dies zu einem Installationsfehler, weil dort die notige Benutzergruppe www-data noch nicht vorhanden war. Falls Sie aus irgendeinem Grund eine altere Raspbian-Installation nutzen, mussen Sie deswegen vor dem Einrichten von Apache den Befehl `sudo groupadd www-data` aufrufen.

Sobald Sie nach der Apache-Installation die IP-Adresse des Raspberry Pi in einen Browser eingeben, erscheint die voreingestellte `index.html` mit dem Schriftzug It works! ([Abbildung 1](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver)). Diese Seite befindet sich auf dem Raspberry Pi im Verzeichnis `/var/www/`. Editieren Sie testweise den angezeigten Text mit `sudo nano /var/www/index.html` und laden Sie die Page im Browser neu. Sie sollten die Änderungen sofort sehen konnen.

[ ![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-webserver/abbildung-12/2748-1-ger-DE/Abbildung-1_large.png) ](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-webserver/abbildung-12/2748-1-ger-DE/Abbildung-1_lightbox.png)

> _Abbildung 1: Nach der Apache-Installation sieht die Index-Seite zunachst noch recht karg aus._

#### PHP & MySQL

Eine statische Webseite mutet wie ein Relikt aus der Internet-Steinzeit an. Deswegen peppen Sie nun den Webserver mit PHP und MySQL auf. Die hierzu notwendigen Pakete installiert folgender Befehl:
    
    
    $ sudo apt-get install php5 libapache2-mod-php5 mysql-server mysql-client php5-mysql

Lehnen Sie sich nach dem Eintippen zuruck und trinken Sie erst einmal einen Kaffee. Der Minirechner hat jetzt einiges zu tun, weil er viele Pakete mit installieren muss, von denen die Installationskandidaten abhangen. Im Zug der Einrichtung fragt ein Textdialog nach dem Passwort fur den MySQL-Root-Benutzer. Fur Übungszwecke genugt vorerst eines, das Sie sich leicht merken konnen, wie etwa `raspberry`.

Nach dem Abschluss der Installation legen Sie nun mithilfe eines Texteditors unter `/var/www/` ein Skript namens `firsttest.php` an. Die Datei erhalt als Inhalt den Dreizeiler aus [Listing 1](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver). Rufen Sie nun das Skript uber die IP-Adresse des RasPi ab, beispielsweise via `http://192.168.2.131/firsttest.php`, erhalten Sie eine Ausgabe wie in [Abbildung 2](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver). Hier sehen Sie auch, mit welchen Optionen PHP zur Zeit konfiguriert ist.

[ ![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-webserver/abbildung-22/2751-1-ger-DE/Abbildung-2_large.png) ](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-webserver/abbildung-22/2751-1-ger-DE/Abbildung-2_lightbox.png)

> _Abbildung 2: Das Skript firsttest.php gibt Informationen zur PHP-Installation aus._

Installieren Sie spater einmal ein Skript, das aus Konfigurationsgrunden denn Dienst versagt, konnen Sie anhand der `firsttest.php`-Seite nachforschen, welcher Parameter dafur moglicherweise verantwortlich zeichnet. So haben Sie die Moglichkeit, diesen in der Datei `/etc/php5/apache2/php.ini` zu andern.

Es empfiehlt sich, mittels des Befehls `sudo apt-get install phpmyadmin` zusatzlich PHPMyAdmin zu installieren. Es hilft dabei, die Inhalte der MySQL-Datenbank komfortabel uber den Browser zu verwalten. Sofern Sie selbst PHP-Skripte schreiben, konnen Sie mit PHPMyAdmin auch kontrollieren, ob diese fehlerfrei sind und die Daten wie beabsichtigt ablegen. Um die Oberflache aufzurufen, melden Sie sich im Browser uber die URL `http://192.168.2.131/phpmyadmin` an ([Abbildung 3](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver)), wobei Sie die IP-Adresse durch jene Ihres RasPi ersetzen. Fur das Login lautet der Benutzername root, das Passwort entspricht dem bei der MySQL-Installation angegebenen.

[ ![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-webserver/abbildung-32/2754-1-ger-DE/Abbildung-3_large.png) ](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-webserver/abbildung-32/2754-1-ger-DE/Abbildung-3_lightbox.png)

> _Abbildung 3: PHPMyAdmin vereinfacht die Administration von MySQL-Datenbanken._

Nun konnen Sie nach Herzenslust HTML/PHP-Seiten erstellen und mit Ihrem eigenen RasPi-Webserver verwenden. Die Pages erstellen Sie wahlweise direkt auf dem Pi unter `/var/www/` oder mit einer Entwicklungsumgebung Ihrer Wahl auf einem PC. In letzterem Fall ubertragen Sie die Dateien anschließend per SFTP auf den Raspberry Pi ubertragen. In diesem Fall muss der SFTP-Benutzer allerdings ausreichende Zugriffsrechte fur das Webseiten-Verzeichnis besitzen.

Dies erreichen Sie am einfachsten, indem Sie das Benutzerkonto pi der Gruppe www-data hinzufugen ([Listing 2](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver), Zeile 1) und allen Mitgliedern dieser Gruppe Schreibrechte fur das Homepage-Verzeichnis einraumen (Zeile 2). Um fur Dateiubertragungen einen anderen Nutzer als Pi zu verwenden, mussen Sie diesen gesondert anlegen (Zeile 3).

Listing 2
    
    
    $ sudo usermod -a -G www-data pi
    $ sudo chmod 775 /var/www
    $ sudo adduser Benutzer www-data

  


#### Auf Diat

In manchen Fallen erweist sich der Raspberry Pi als zu schwach fur den umfangreich ausgestatteten Apache-Server - etwa, in mehrere Personen gleichzeitig auf den Webserver zugreifen. Das setzt die schlanke Hardware gehorig unter Last, wodurch sich die Seiten im Browser nur langsam aufbauen. Peilen Sie also ein solches Szenario an, sollten Sie einen genugsameren Webserver [[3]](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver/\(offset\)/4) verwenden, der mehr aus den Ressourcen des Mini-Rechners herausholt.

Ein guter Kandidat fur diesen Zweck ist Lighttpd. Falls Sie vor dessen Installation bereits Apache verwendet haben, gilt es diesen samt seinen Zusatzpaketen zunachst zu entfernen:
    
    
    $ sudo apt-get remove apache2 php5 libapache2-mod-php5 php5-mysql

Dann richten Sie Lighttpd uber den Befehl `sudo apt-get install lighttpd` ein. Die MySQL-Installation erfolgt auf die gleiche Weise wie bei einer Apache-Umgebung. Nur bei PHP gibt es einen Unterschied: Sie mussen es hier als CGI-Modul einbinden. Die Befehle dazu zeigen die ersten beiden Zeilen von [Listing 3](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver/\(offset\)/2). Zu guter Letzt gestatten Sie dem Webserver noch explizit, PHP-Skripte zu parsen (Zeile 3). Nach einem Neustart von Lighttpd (Zeile 4) ist diese Einstellung aktiv: Die Seite `firsttest.php` zeigt nun eine ahnliche Ausgabe wie fur Apache in [Abbildung 2](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver/\(offset\)/0).

Listing 3
    
    
    $ sudo apt-get install php5-common php5-cgi php5
    $ sudo apt-get install php5-mysql
    $ sudo lighty-enable-mod fastcgi-php
    $ sudo service lighttpd force-reload

#### Content-Management

Fruher war es gang und gabe, bei jeder Änderung einer Webseite die entsprechenden Daten per FTP neu hochzuladen, mittlerweile ermoglichen Content-Management-Systeme ein effizienteres Vorgehen: So konnen Sie nun via Browser von jedem Gerat aus schnell neue Inhalte auf die eigene Homepage stellen und sich obendrein die Arbeit mit Anderen teilen. Betreiben Sie etwa mit mehreren Bekannten zusammen die Website eines Vereins, kann jeder der Beteiligten uber ein ein eigenes Redakteurskonto selbststandig neue Inhalte einstellen, wahrend Sie nur fur sich selbst als Technikverantwortlichen weitergehende Zugriffsrechte einraumen.

Der Markt an unterschiedlichen CMS scheint schier unerschopflich, doch viele Anfanger vertrauen auf Wordpress --eigentlich kein CMS, sondern eine Blogging-Software. Aufgrund seiner ubersichtlichen Bedienoberflache ist es auch keine schlechte Wahl. Trotzdem sollten Sie besser auf eine echte CMS-Losung setzen, wie etwa Joomla. Letzteres bietet weitaus mehr Moglichkeiten als Wordpress, weist aber dennoch eine durchdachte, intuitiv erlernbare Bedienoberflache auf.

Zur Installation von Joomla laden Sie dieses als Zip-Archiv von der offiziellen Homepage [[4]](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver/\(offset\)/4) herunter und ubertragen es via SFTP in das Verzeichnis `/var/www/` auf dem RasPi. Dort entpacken Sie das Archiv und loschen anschließend die nun nicht mehr benotigte ZIP-Datei. Geben Sie nun die IP-Adresse des Raspberry in den Browser eines PCs ein, leitet Joomla Sie mittels mehrerer Dialoge durch die Erstkonfiguration des CMS.

Falls die Webkonfiguration fehlschlagt, mussen Sie noch die Zugriffsrechte der Joomla-Version fur die Verzeichnisse und Dateien anpassen. Dies erledigen Sie auf dem Pi, indem Sie in das Verzeichnis `/var/www/` wechseln und dort die Befehl aus [Listing 4](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Webserver/\(offset\)/2) ausfuhren. Anschließend starten Sie die Konfiguration erneut.

Listing 4
    
    
    $ find . -type f -exec chmod 644 {} \;
    $ find . -type d -exec chmod 755 {} \;

  


#### Ausblick

Nun verfugen Sie uber einen reichhaltig ausgestatteten Heim-Webserver. Soll Ihre Website irgendwann das Test- und Experimentierstadium verlassen, gilt es die Daten fur den Produktivbetrieb ins World Wide Web hochzuladen. Fur kleine bis mittelgroße Sites genugt hierfur preisgunstiger Webspace. In der Regel unterstutzt die Konfiguration der Webhosting-Unternehmen gangigste CMS wie Joomla - die FAQ des Hosters sollte hieruber weitere Auskunft geben.

Das Anmieten eines VServers oder gar eines kompletten Root-Servers will gut uberlegt sein: Hier mussen Sie die Administration komplett selbst ubernehmen, und einen offen im Netz stehenden Rechner gilt es weitaus starker gegen Angriffe zu sichern werden als einen RasPi im heimischen LAN. Unternehmen Sie diesen Schritt also lieber erst, wenn Sie Erfahrungen mit den unterschiedlichsten Bereichen der Administration und Server-Sicherheit gesammelt haben.

Alle fur diesen Schritt notwendigen Fertigkeiten - etwa das Konfigurieren einer Firewall mithilfe von Iptables oder das "Einsperren" von Verzeichnissen mittels Chroot - konnen Sie auf jeden Fall vorab wunderbar am Raspberry Pi erlernen und uben.

  1. RasPi als File- und Print-Server: Marko Dragicevic, "Zentrallager", RasPi Geek 05/2013, S. 42, <http://www.raspi-geek.de/29875>
  2. Verbreitung unterschiedlicher Webserver: <http://news.netcraft.com/archives/category/web-server-survey/>
  3. Lightweight-Webserver: Tim Schurmann, "Kleine Kellner", LinuxUser 04/2011, S. 20, <http://www.linux-community.de/22927>
  4. Joomla-Download: <http://www.joomla.org/download.html>
