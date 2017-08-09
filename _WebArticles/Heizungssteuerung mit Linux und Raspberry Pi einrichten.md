# Heizungssteuerung mit Linux und Raspberry Pi einrichten

_Captured: 2016-11-07 at 11:01 from [www.tecchannel.de](http://www.tecchannel.de/a/heizungssteuerung-mit-linux-und-raspberry-pi-einrichten,2061641)_

Autor Thomas Eimers kam schon in der Kindheit mit Elektrotechnik in Beruhrung, der Vater war Rundfunkelektroniker. Beruflich ist Eimers "in einem großeren Umfeld der Softwareentwicklung tatig", beschaftigt sich als begeisterter Bastler in der Freizeit jedoch gern mit der Regel- und Steuerungstechnik. Und er ist, wie er selber sagt, bekennender Opensource-Fan. Hier stellt er sein Projekt einer Fußboden-Heizungssteuerung mit Linux und Raspberry Pi vor.

Die Anforderungen an den Regelkreis sind recht simpel: Der Brenner einer Heizung soll uber die Regelung ein- und ausgeschaltet werden. Ob der Brenner ein- oder ausgeschaltet wird, hangt von den beiden Temperatursensoren (Außentemperatur und Temperatur des zurucklaufenden Wassers) ab. Die Pumpe, die im Wasserkreislauf fur die Stromung sorgt, soll ebenso uber die Regelung gesteuert werden und nur bei Bedarf laufen, was Strom spart.

## Die Benutzer-Schnittstelle

Fur die Heizungssteuerung wird ein 8 bis 10 Zoll großes Touchscreen verwendet werden. Das UI basiert auf jQuery Mobile, um die Bedienung zu vereinfachen. Die Menufuhrung weist den folgenden Aufbau auf:

  * Statistiken

  * Temperaturverlauf/Verbrauch fur diesen Tag

  * Temperaturverlauf/Verbrauch fur diese Woche

  * Temperaturverlauf/Verbrauch fur diesen Monat

  * Temperaturverlauf/Verbrauch fur dieses Jahr

  * Systemkonfiguration

  * Sollwertkurve Rucklauf

  * Pumpenkonfiguration

  * Nachtabsenkung

  * Temperaturfuhler

Die aktuellen Informationen sind in einer Fußzeile auf jeder Seite abzulesen.

## Entscheidung fur den Raspberry Pi

Die Heizungssteuerung direkt unter Linux zu implementieren, bietet viele Vorteile, da man auf ein auf ein komplettes Betriebssystem zuruckgreifen kann. Zu den Vorzugen gehoren der einfache Netzwerkanschluss fur Wartung, die Moglichkeit, Datenbanken fur Temperaturwerte zu verwenden sowie einen Touchscreen als Interface anzuschließen. Fruhere aufwandige Arbeiten wie das Anschließen eines DCF Empfangers (Funkuhr) werden damit unnotig, da hier beispielsweise das NTP des Internets zur Zeitsynchronisierung der Heizungssteuerung herangezogen werden kann.

![Für die Heizungssteuerung wird ein 8 bis 10 Zoll großer Touchscreen verwendet werden. Das UI basiert auf jQuery Mobile, um die Bedienung zu vereinfachen.](http://images.cio.de/images/computerwoche/bdb/2525560/840x473.jpg)

> _Fur die Heizungssteuerung wird ein 8 bis 10 Zoll großer Touchscreen verwendet werden. Das UI basiert auf jQuery Mobile, um die Bedienung zu vereinfachen._

Die Kosten fur einen kompletten PC sind mittlerweile recht gering, besonders wenn es sich um Single-Board-PCs handelt. Der Aufbau mittels Standard-PC-Hardware ermoglicht, die Steuerung noch lange in Betrieb zu halten und auch in 10 Jahren noch auf Ersatzteile zuruckgreifen zu konnen.

## Bezug des Quellcodes

Der Quellcode steht unter der GPL-Lizenz, so dass die Steuerung nach Belieben fur andere Zwecke angepasst werden kann.

  * Das Projekt Fußbodenheizungsteuerung ist auf [Sourceforge](http://sourceforge.net/projects/heatingcontrol/) verfugbar

  * Der komplette [Quellcode](http://sourceforge.net/p/heatingcontrol/code/HEAD/tree/trunk/) fur die neue Heizungssteuerung kann via SVN heruntergeladen werden

## Download eines fertigen Images

Alle nachfolgenden Texte beschreiben die komplette Installation der Heizungssteuerung, die besonders wichtig sind, wenn die Steuerung fur andere Zwecke eingesetzt werden soll. Ein fertiges Image der Steuerung als Download liegt alternativ ebenfalls bereit. Dies ist fur den schnellen Einstieg oder fur Linux- und PHP-Anfanger eine gute Wahl. Das [Image](http://sourceforge.net/projects/heatingcontrol/files/heating_control_2014_02_09_upload.img.bz2/download) ist auf Sourceforge verfugbar. Die Zugangsdaten fur den SSH Login des fertigen Images lauten:

  * Benutzername "pi"

  * Password "raspheat"

Installation des kompletten Images (4-GByte-Speicherkarte notig)

_# Wichtig! /dev/sdX durch die Laufwerksbezeichnung der angeschlossenen Speicherkarte ersetzen_

_# (Liste kann mit "cat /proc/partitions" ermittelt werden)_

_# Der Vorgang dauert einige Minuten und erzeugt erst nach Fertigstellung eine Ausgabe_

`sudo su -`

`cat /proc/partitions`

`bunzip2 -dc dateiname_des_heruntergeladenen_images.img.bz2 | dd bs=1M of=/dev/sdX`

Meldungen wie

"_dd: »/dev/sdd" wird geschrieben: Auf dem Gerat ist kein Speicherplatz mehr verfugbar_"

erfordern den Einsatz einer großeren Speicherkarte. Da nicht alle 4-GByte-Speicherkarten eine einheitliche Speicherkapazitat aufweisen, empfiehlt sich die Verwendung einer 8-GByte-Karte.

  


Einige der verwendeten Tools/Bauteile/Software sind in den folgenden aufgefuhrten Artikeln teilweise ausfuhrlicher beschrieben. Diese zu lesen ist nicht unbedingt erforderlich, sie konnen aber in Problemfallen hinzugezogen werden.

## Die Hardwaresteuerung

Bei der Hardware handelt es sich um die externe Beschaltung (Platine), die die Schnittstelle zwischen dem Raspberry Pi und der Heizung darstellt. Die Platine ist uber ein Flachbandkabel und einen Stecker mit dem Raspberry Pi verbunden. Der Raspberry Pi wird durch die Verwendung von Relais galvanisch getrennt. Über diese digitalen Ausgange sollten Schutze angesprochen werden, die beispielsweise den Anlaufstrom der Pumpen verkraften.

Das Fertigen zweier Platinen ist fur unter 20 Euro moglich. Um sich die Platine herstellen zu lassen, kann die Datei [layout.brd](http://notdefine.de/projects.php?project=heizungssteuerung-mit-linux-ubuntu-arm) an den Ätzservice eines Platinenbelichters gesendet werden, beispielsweise an den Service von [Platinenbelichter.de](http://www.platinenbelichter.de/).

  1. **[Schaltplan fur das Anfertigen einer Platine**](http://www.tecchannel.de/g/heizungssteuerung-mit-linux-und-raspberry-pi-die-hardware,37659)  

  2. **[Schaltplan-Layout fur den Ätzservice**](http://www.tecchannel.de/g/heizungssteuerung-mit-linux-und-raspberry-pi-die-hardware,37659,2)  


Als Basissystem wird auf dem Raspberry Pi Raspbian, eine Debian-Variante, verwendet. Die Laufzeitumgebung ist eine typische LAMP-Umgebung, bestehend aus dem Apache Webserver, Mysql Datenbank, und PHP als Programmiersprache. Dies alles kann problemlos auf einer 4 GByte großen SD-Speicherkarte abgelegt werden.

## Basissystem einrichten

Nun folgt die Einrichtung des Betriebssystems. Die einzelnen Schritte auf der Console konnen direkt unter Linux ausgefuhrt werden. An Stellen, an denen eventuelle Anpassungen vorgenommen werden mussen, erscheint ein entsprechender Vermerk.

`wget "http://downloads.raspberrypi.org/raspbian_latest"`

`unzip raspbian_latest`

_# Ergebnis ist ein Image, mit einem Dateinamen ahnlich wie: 2014-01-07-wheezy-raspbian.img_

_# Wichtig! /dev/sdX durch die Laufwerksbezeichnung der Speicherkarte ersetzen_

_# (Liste der Speicherlaufwerke kann mit "cat /proc/partitions" angezeigt werden)_

_# Der folgende Vorgang dauert einige Minuten und erzeugt erst eine Ausgabe, wenn er fertig ist._

`sudo dd bs=1024k if=2014-01-07-wheezy-raspbian.img of=/dev/sdX`

Nun wird die erstellte SD-Karte in den Raspberry eingesteckt. Der Raspberry Pi verbindet sich mit dem Netzwerk, bootet und erhalt dann uber DHCP, etwa von einer Fritzbox, eine IP fur das lokale Netzwerk. Der Netzwerkname ist mit "raspberrypi" voreingestellt. Das Passwort von Raspbian ist "raspberry", der SSH Benutzer ist "pi".

_# auf den Raspberry uber das Netzwerk verbinden, und_

_# mit dem Benutzer "raspberry" und dem Passwort "pi" anmelden_

`ssh -lpi raspberrypi`

_# Initiale Konfiguration_

`sudo raspi-config`

_#einmal "Expand Filesystem" aufrufen und einmal "Internationalisation Options", dort unter "Change Locale" de_DE.UTF-8 UTF-8_

_# stellen. Danach nochmal "Internationalisation Options" und dann "Change Timezone" auf "Europe/Berlin" stellen._

_# danach das Passwort andern "Change User Password" (im verfugbaren fertigen Image wurde dies auf 'raspheat' gestellt)._

_# dann im Hauptmenu Advanced Options - Hostname den Namen des Systems auf "heating" setzen._

_#_

_# danach "Finish" und den Raspberry einmal neu starten lassen._

_# erneut auf den Raspberry via Netzwerk verbinden_

`ssh -lpi heating`

`sudo rpi-update`

`sudo apt-get update; sudo apt-get upgrade`

`sudo apt-get install mc rrdtool owfs-fuse`

_# mit der Mysql-Installation wird das Mysql-Root-Passwort vergeben ('raspheat' habe ich genommen, bei mir im Image)_

`sudo apt-get install mysql-server-5.5`

_# als Server fur phpmyadmin den Apache2 wahlen. Konfiguration phpmyadmin mit dbconfig-common_

_# im Image wurde erneut das Passwort raspheat vergeben_

`sudo apt-get install htop apache2 libapache2-mod-php5 phpmyadmin php-pear php-apc secure-delete`

_# ist riesengroß und wird nicht gebraucht_

`sudo apt-get purge wolfram-engine`

Der Apache-Webserver und phpmyadmin sind ab diesem Zeitpunkt verfugbar. Die Zugangsdaten fur den phpmyadmin sind der Benutzer "root" und das Passwort "raspheat".

  


## Temperatursensoren vorbereiten

Die Sensoren werden mittels owfs ausgelesen. Hierzu gibt es einen eigenen Artikel, [Temperaturmessung mit Linux mittels DS9490R-USB](http://notdefine.de/projects.php?project=temperaturmessung-mit-linux-DS9490R-USB), der ausfuhrlich auf die Details eingeht. Der USB-Adapter und der Temperaturfuhler sind vorab anzuschließen.

`sudo mkdir /media/1-wire`

`sudo owfs --allow_other -u /media/1-wire`

`ls -lah /media/1-wire/`

`cat /media/1-wire/*/temperature`

Eine Meldung, ahnlich dem folgenden Beispiel, erscheint.

`pi@raspberrypi /media/l-wire $ cat /media/l-wire/*/temperature;`

`24.875 13.72321 _`

![Raspberry Pi mit einem DS1820 Temperaturfühler sowie dem DS9490R USB-Adapter](http://images.cio.de/images/computerwoche/bdb/2525564/840x473.jpg)

> _Raspberry Pi mit einem DS1820 Temperaturfuhler sowie dem DS9490R USB-Adapter_

Im vorliegenden Beispiel ist lediglich ein Sensor angeschlossen, der gerade 28.875 Grad misst. Es gibt auch Sensoren, die stets ausgelesen werden, unabhangig davon, ob ein Temperaturfuhler angeschlossen ist. Dieser Sensor, der moglicherweise eingebaut ist, liefert immer unterschiedliche Temperaturen und ist zu ignorieren.

Hier ein Beispiel fur den Raspberry Pi mit einem DS1820 Temperaturfuhler sowie dem DS9490R USB Adapter:

  


Um die eingerichteten Temperaturfuhler sinnvoll zu verwenden, wird nur der Quellcode des Projekts aus einem SVN Repository geladen.

`sudo apt-get install subversion`

`cd ~`

`mkdir heating`

`cd heating`

Wenn nur lesend auf das Project heatingcontrol zugegriffen werden soll:

`svn checkout svn://svn.code.sf.net/p/heatingcontrol/code/trunk heatingcontrol-code`

Wenn auch schreibender Zugriff auf das Projekt gewunscht ist (Sourceforge-Account vorausgesetzt):

`svn checkout --username=euer_sourceforge_name svn+ssh://notdefine@svn.code.sf.net/p/heatingcontrol/code/trunk heatingcontrol-code`

## Konfiguration des Apache-Webservers

Im Folgenden ist der Inhalt der Datei "/etc/apache2/sites-available/default" dargestellt. Dieser Inhalt kann beispielsweise mit dem Befehl "sudo mcedit /etc/apache2/sites-available/default" angepasst werden, nachdem eine Verbindung mit dem Raspberry via SSH aufgebaut wurde.

`<VirtualHost *:80>`

`ServerAdmin webmaster@localhost`

`DocumentRoot /home/pi/heating/www`

`<Directory />`

`Options FollowSymLinks`

`AllowOverride None`

`</Directory>`

`<Directory /home/pi/heating/www/>`

`Options Indexes FollowSymLinks MultiViews`

`AllowOverride None`

`Order allow,deny`

`allow from all`

`</Directory>`

`ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/`

`<Directory "/usr/lib/cgi-bin">`

`AllowOverride None`

`Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch`

`Order allow,deny`

`allow from all`

`</Directory>`

`ErrorLog ${APACHE_LOG_DIR}/error.log`

`# Possible values include: debug, info, notice, warn, error, crit,`

`# alert, emerg.`

`LogLevel warn`

`CustomLog ${APACHE_LOG_DIR}/access.log combined`

`</VirtualHost>`

Der Apache-Webserver benotigt schreibenden Zugriff auf das temp-Verzeichnis:

`cd ~/heating/www/common/temp`

`chmod 777 * -R .`

  


Im Folgenden wird eine Verbindung zur Mysql-Datenbank als Root aufgebaut und danach ein Datenbankbenutzer inklusive Datenbank und dessen Tabellen angelegt.

`mysql --user=root mysql --password`

Folgender Befehl ist nun auszufuhren:

_CREATE DATABASE `heating` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;_

_CREATE USER 'pi'@'localhost' IDENTIFIED BY 'raspheat';_

_GRANT SELECT , INSERT , UPDATE , DELETE , CREATE , DROP , FILE ,_

_INDEX , ALTER , CREATE TEMPORARY TABLES , CREATE VIEW , EVENT,_

_TRIGGER, SHOW VIEW , CREATE ROUTINE, ALTER ROUTINE,_

_EXECUTE ON * . * TO 'pi'@'localhost' IDENTIFIED BY 'raspheat' WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0 ;_

_GRANT ALL PRIVILEGES ON `pi\\_%` . * TO 'pi'@'localhost';_

_USE heating;_

_SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";_

_SET time_zone = "+00:00";_

_CREATE TABLE IF NOT EXISTS `desired_values` (_

_`id` int(11) NOT NULL AUTO_INCREMENT,_

_`outside_temp` int(11) NOT NULL,_

_`return_flow_temp` float NOT NULL,_

_PRIMARY KEY (`id`),_

_UNIQUE KEY `outside_temp` (`outside_temp`)_

_) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Ruecklauftemperatur in abhaengigkeit der aussentemperatur.' AUTO_INCREMENT=61 ;_

_INSERT INTO `desired_values` (`id`, `outside_temp`, `return_flow_temp`) VALUES_

_(1, -35, 36), (2, -34, 36), (3, -33, 36), (4, -32, 36), (5, -31, 36), (6, -30, 36), (7, -29, 36), (8, -28, 36), (9, -27, 36), (10, -26, 36), (11, -25, 36),_

_(12, -24, 36), (13, -23, 36), (14, -22, 36), (15, -21, 36), (16, -20, 36), (17, -19, 36), (18, -18, 36), (19, -17, 36), (20, -16, 36), (21, -15, 36), (22, -14, 36),_

_(23, -13, 36), (24, -12, 36), (25, -11, 36), (26, -10, 36), (27, -9, 36), (28, -8, 36), (29, -7, 36), (30, -6, 36), (31, -5, 36), (32, -4, 36), (33, -3, 35),_

_(34, -2, 34), (35, -1, 32), (36, 0, 32), (37, 1, 32), (38, 2, 32), (39, 3, 32), (40, 4, 32), (41, 5, 31), (42, 6, 30), (43, 7, 30), (44, 8, 29), (45, 9, 29),_

_(46, 10, 28), (47, 11, 28), (48, 12, 27), (49, 13, 27), (50, 14, 26), (51, 15, 26), (52, 16, 26), (53, 17, 25), (54, 18, 25), (55, 19, 25), (56, 20, 25),_

_(57, 21, 11), (58, 22, 11), (59, 23, 11), (60, 24, 11);_

_CREATE TABLE IF NOT EXISTS `sensor_values` (_

_`id` int(11) NOT NULL AUTO_INCREMENT,_

_`name` varchar(100) COLLATE utf8_bin NOT NULL,_

_`value` float NOT NULL,_

_`unit` varchar(100) COLLATE utf8_bin NOT NULL,_

_`timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,_

_PRIMARY KEY (`id`),_

_KEY `name` (`name`),_

_KEY `timestamp` (`timestamp`)_

_) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=2657335 ;_

_CREATE TABLE IF NOT EXISTS `settings` (_

_`id` int(11) NOT NULL AUTO_INCREMENT,_

_`name` varchar(255) COLLATE utf8_bin NOT NULL,_

_`unit` varchar(255) COLLATE utf8_bin NOT NULL,_

_`value` text COLLATE utf8_bin NOT NULL,_

_PRIMARY KEY (`id`),_

_UNIQUE KEY `name` (`name`)_

_) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=6 ;_

_INSERT INTO `settings` (`id`, `name`, `unit`, `value`) VALUES_

_(1, 'heater', 'bool', '1'),_

_(2, 'pump_follow_up_time', 'minutes', '45'), (3, 'slider_nighly_temperature_sink_substract', 'celsius', '13'),_

_(4, 'slider_nighly_temperature_sink_to', 'hour', '23'), (5, 'slider_nighly_temperature_sink_from', 'hour', '6');_

_quit_

  


## Cronjobs konfigurieren

Die Heizungssteuerung muss automatisch jede Minute aktiv werden, um die Temperaturen zu erfassen und gegebenenfalls einzugreifen. Zudem werden Diagramme in einem regelmaßigen Turnus generiert. Dafur wird das auf Linux-Systemen verfugbare Cronjob-Management verwendet. Folgend eine Liste der Cronjobs und deren Aufgaben:

• Watchdog - Pruft ob die Steuerung noch Werte ermitteln kann und startet das System im Fehlerfall neu.

• Cleanup - Beschrankt die in der Datenbank abgelegten gemessenen Werte und loscht Altdaten.

• Temperatur eintragen - Misst aktuelle Temperaturwerte und tragt diese in die Datenbank ein.

• Graphen erstellen - Erstellt mittels RRD-Tool die verschiedenen Temperaturgraphen (fur den aktuellen Tag, fur die Woche, usw.).

Die genauen Funktionen konnen im SVN-Quellcode angesehen werden.

Die Cronjobs des Benutzer pi kann man sich mit folgendem Befehl anzeigen lassen "crontab -l". Bearbeitet werden diese Cronjobs mit dem Befehl "crontab -e". Um diese Cronjobs nun auf den Raspberry zu ubernehmen, mussen folgende Eintrage (mittels "crontab -e") erganzt werden:

_#*/2 * * * * cd /home/pi && ./heating/watchdog.sh --> Inaktiv bis # entfernt wird, dass sollte gemacht werden, wenn alles komplett eingerichtet ist_

_0 2 * * * cd /home/pi && ./heating/cleanup.sh_

_* * * * * cd /home/pi && ./heating/insert_new_temp.sh >> /dev/null_

_*/5 * * * * cd /home/pi && ./heating/create_graph_quick.sh >> /dev/null_

_5 */2 * * * cd /home/pi && ./heating/create_graph_slow.sh >> /dev/null_

Ob die Cronjobs auch aufgerufen werden, kann mit dem Befehl "tail -f /var/log/syslog" gepruft werden. Diese Logdatei zeigt jede Ausfuhrung eines Cronjobs an.

## RRD-Tool auf Jahres-, Wochen- und Tagesstatistiken vorbereiten

Um die gemessenen Werte grafisch darzustellen, wird das bekannte [RRD-Tool](http://notdefine.de/projects.php?project=diagramme-mit-rrdtool-unter-linux) verwendet.

Die Datenbank der Temperaturwerte wird so eingerichtet, dass sie die Werte der letzten zwei Jahre beinhaltet. Die gemessenen Werte werden alle zwei Minuten eingetragen (120*24*365*2=525600 Anzahl der zu speichernden Temperaturwerte fur den Zeitraum von zwei Jahren). Das Skript 'init_rrdtool.sh' legt die dafur notige RRDTool Datenbank an.

`cd heating/jobs`

`./init_rrdtool_db.sh`

  


Eine Liste aller Sensoren erhalt man mit folgenden Befehlen:

`cd heating/jobs`

`./list_sensors.sh`

Dies sollte eine Liste wie diese hier anzeigen. Hiermit kann man bestimmen, welcher Sensor welche Temperatur misst:

`/media/1-wire/05.4AEC29CDBAAB Sensortyp: DS2405`

`/media/1-wire/10.49EE82020800 Sensortyp: DS18S20 Temperatur: 22.125`

`/media/1-wire/10.49EE83020800 Sensortyp: DS18S20 Temperatur: 32.125`

`/media/1-wire/10.49EE83020900 Sensortyp: DS18S20 Temperatur: 4.125`

`/media/1-wire/10.67C6697351FF Sensortyp: DS18S20 Temperatur: 63.5712`

`/media/1-wire/81.323132000000 Sensortyp: DS1420`

Die einzelnen Sensoren weist man (leider etwas unkomfortabel) direkt im Cronjob zu. Hierzu bearbeitet man dieDatei insert_new_temp.sh mit "mcedit ~/heating/jobs/insert_new_temp.sh".

## Tests einrichten

Um die Steuerungssoftware automatisiert zu testen, wird [PHPUnit ](http://www.phpunit.de/)verwendet. Die Einrichtung ist fur den Betrieb der Steuerung optional, aber fur professionelle Softwareentwicklung unverzichtbar, besonders wenn Modifikationen an der Software gemacht werden sollen.

`sudo apt-get install phpunit`

Unleserliche xdebug "var_dump()" Befehle konnen durch den Eintrag der Konfigurationsvariablen

`'xdebug.overload_var_dump=0' in die PHP Serverkonfigurationsdatei '/etc/php5/apache2/php.ini'`

abgeschaltet werden. Die Tests (phpunit) werden mit folgenden Befehlen ausgefuhrt:

`cd ~/heating/tests`

`phpunit`

  


Um die externe Beschaltung auf der Platine ansprechen zu konnen, mussen die GPIO-Ports eingerichtet werden. Damit man ohne Super-User-Rechte auf die GPIO-Ports zugreifen kann (InterfaceGpio.class.php), sind zwei Schritte erforderlich:

1\. Den Benutzer "www-data "in die Gruppe "gpio" eintragen.

2\. Die "/etc/rc.local" anpassen.

`sudo usermod -aG gpio www-data`

Es muss folgender Code in die /etc/rc.local eingetragen werden:

`# Print the IP address`

`_IP=$(hostname -I) || true`

`if [ "$_IP" ]; then`

`printf "My IP address is %s\n" "$_IP"`

`fi`

`/home/pi/heating/jobs/init_boot.sh`

`exit 0`

## Fertig - glucklich sein!

Die Steuerung ist nun komplett eingerichtet und kann an die Heizung angeschlossen werden. Bei mir lauft sie seit einem Jahr ohne Ausfalle im Betrieb.

## Backup der Steuerung erstellen und Wiederherstellen

Heruntergeladene Pakete loschen:

`sudo apt-get clean`

`sudo rm /var/log/*.gz`

`sudo rm /var/log/*.1`

`sudo rm /var/log/apache2/*.gz`

`sudo rm /var/log/apache2/*.1`

`cd ~`

_# Freien Speicherplatz mit "0" uberschreiben, damit das Image kleiner gepackt werden kann_

`sfill -ll -f -z .`

Backup erstellen

`sudo dd bs=1M if=/dev/sdd of=heating_control_2014_02_09.img`

Backup wieder herstellen

`sudo dd bs=1M if=heating_control_2014_02_09.img of=/dev/sdd`

_([PC-Welt](http://www.pcwelt.de/ratgeber/Heizungssteuerung_mit_Linux_und_Raspberry_Pi_einrichten-Projekt_Fussbodenheizung-8740849.html)/ad)_
