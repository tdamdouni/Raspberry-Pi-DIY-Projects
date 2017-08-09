# Dropbox-Alternative fürs Heimnetzwerk

_Captured: 2017-05-06 at 16:35 from [www.golem.de](https://www.golem.de/news/owncloud-dropbox-alternative-fuers-heimnetzwerk-1404-105843.html)_

Nach dem NSA-Skandal und dem Bekanntwerden des Heartbleed-Bugs sind Sorgen um die Sicherheit der eigenen Daten im Netz berechtigt. Dropbox ist als Cloud-Speicher umso weniger attraktiv geworden, seit Bushs ehemalige Sicherheitsberaterin Condoleezza Rice - die in dieser Funktion eng mit den Geheimdiensten zusammenarbeitete - [in den Vorstand berufen wurde](http://www.handelsblatt.com/politik/international/empoerung-bei-nutzern-condoleezza-rice-wird-mitglied-im-dropbox-verwaltungsrat/9748450.html). Wer sich Sorgen um die Sicherheit seiner Daten im Netz macht, sollte sie lieber auf seinem eigenen Server speichern. Es gibt genugend Alternativen. Fur einen Cloud-Speicher im Heimnetzwerk eignet sich beispielsweise Owncloud. Wir erklaren, wie die Dropbox-Alternative auf einem Raspberry Pi installiert und sicher konfiguriert werden kann. Die Anleitung lasst sich auch auf anderen Rechnern mit Debian oder Ubuntu nachvollziehen.

![](https://www.golem.de/fileadmin/tx_bbcampaigns/3639--ad/wm_kpmg_pilot3_17q2_vorbereiten_statt_hoffen_300x250.png)

  * ![Das Anmeldefenster von Owncloud \(Screenshots: Golem.de\)](https://scr3.golem.de/screenshots/1404/owncloud/thumb620/01_owncloud.png)

> _Das Anmeldefenster von Owncloud (Screenshots: Golem.de)_

Das Raspberry Pi haben wir auch ausgewahlt, weil der Rechner portabel ist; er lasst sich leicht von zu Hause zur Arbeitsstelle transportieren und dort wieder ans Netz zur Synchronisierung hangen. Außerdem bringt Owncloud Clients fur Windows, Mac OS X und Linux mit. Notfalls konnen die Daten auch uber einen Browser abgerufen werden.

### Raspberry Pi vorbereiten

Wir haben uns fur die Linux-Distribution Raspbian entschieden, die auf Debian basiert. Das Image lasst sich von der [offiziellen Webseite des Projekts herunterladen](http://www.raspbian.org/). Die Datei wird anschließend unter Windows beispielsweise mit [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/) auf eine SD-Karte schreiben. Unter Linux reicht das Kommandozeilenwerkzeug _dd_ aus. Der Geratename der SD-Karte wird mit _fdisk -l_ ermittelt.

Je nachdem, wie viele Daten spater uber Owncloud synchronisiert werden sollen, sollte entweder eine genugend große SD-Karte gewahlt oder zusatzlich eine externe Festplatte uber USB angeschlossen werden. Wie eine externe Festplatte eingebunden werden kann, erklaren wir spater in einem Zwischenschritt.

### Konfiguration des Raspberry Pi

Jetzt starten wir das Rasberry zunachst einmalig mit einem angeschlossenen Monitor, um es zu konfigurieren. Dazu melden wir uns als Benutzer "pi" mit dem Kennwort "raspberry" an. Anschließend geben wir den Befehl sudo _raspi-config_ ein. Unter Punkt 4 richten wir die deutschen Zeichensatze de_DE.UTF-8 und de_DE.ISO-8859-1 ein und setzen im darauffolgenden Dialogfeld de_DE.UTF-8 als Standard. Nochmals unter Punkt 4 andern wir noch die Zeitzone unter "Europa" auf "Berlin" und schließlich sicherheitshalber noch die Tastatureinstellungen, die bereits durch die Umstellung auf den deutschen Zeichensatz erfolgt sein sollten.

Jetzt sollten wir unter Punkt 2 das Passwort neu setzen und so das Raspberry zunachst einmal nach außen absichern. Anschließend erweitern wir das Dateisystem uber Punkt 1 auf die gesamte SD-Karte. Danach ist ein Neustart des Raspberry Pi fallig. Nach dem Neustart und der anschließenden erneuten Anmeldung als normaler Benutzer "pi" melden wir uns fur die weitere Konfiguration mit _sudo -s_ als Administrator an, denn der sudo-Befehl, mit dem die darauffolgende Befehlseingabe mit Administratorrechten ausgefuhrt wird, versagt in einigen Fallen. Danach sollte das System mit _apt-get update_ und dann mit _apt-get dist-upgrade_ auf den aktuellen Softwarestand gebracht werden. Damit erhalten wir auch eine aktuelle Version der Kryptobibliothek Openssl, in der der Heartbleed-Bug behoben ist (Version 1.0.1e-2+rvt+deb7u6).

  


In den offiziellen Softwarequellen der Linux-Distribution Raspbian fur das Raspberry Pi gibt es zwar bereits eine Owncloud-Version, die ist allerdings veraltet und funktioniert mit aktuellen Versionen des Owncloud-Clients nicht. Stattdessen verwenden wir die Version fur Debian 7 alias Wheezy, fur die wir mit

_echo 'deb http://download.opensuse.org/repositories/isv:ownCloud:community/Debian_7.0/ /' >> /etc/apt/sources.list.d/owncloud.list_

![](https://www.golem.de/fileadmin/tx_bbcampaigns/3619--ad/appian_whitepaper_how_to_avoid_anti_money_laundering_vulnerabilities_wm_300x250.jpg)

zunachst die Quelle fur Apt nachreichen. Mit

_wget http://download.opensuse.org/repositories/isv:ownCloud:community/Debian_7.0/Release.key_

und

_apt-key add - < Release.key_

sichern wir die Softwarequelle noch mit einem Schlussel ab. Dann folgt die eigentliche Installation mit _apt-get update_ und _apt-get install owncloud_. Damit werden fast alle benotigten Komponenten automatisch installiert, etwa der Apache-Webserver.

### Datenbank auswahlen

Es fehlt aber noch die Datenbank. Owncloud lasst sich sowohl mit Sqlite als auch mit Postqresql oder Mysql verwenden. Allerdings ist Sqlite deutlich weniger performant als Mysql oder Postgresql, vor allem bei großen Datenmengen und mehreren Benutzern. Aus Bequemlichkeit entscheiden wir uns fur Mysql, das immer noch weit verbreitet ist. Mysql-Server installieren wir also nachtraglich mit _apt-get install mysql-server_. Wahrend der Installation muss ein beliebiges Administratorpasswort fur die Datenbank gesetzt werden.

Aus Sicherheitsgrunden verwenden wir fur unsere Owncloud-Installation jedoch einen eigenen Mysql-Benutzer, den wir noch anlegen mussen. Dazu rufen wir den Kommandozeilenmodus der Datenbank mit _mysql -uroot -p_ auf und geben das zuvor gesetzte Administratorpasswort ein. Mit den Zeilen

_CREATE USER 'owncloud'@'localhost' IDENTIFIED BY 'meinpasswort';_

_CREATE DATABASE IF NOT EXISTS owncloud;_

_GRANT ALL PRIVILEGES ON owncloud.* TO 'owncloud'@'localhost' IDENTIFIED BY 'meinpasswort';_

werden der Benutzer und die neue Datenbank namens "owncloud" angelegt und mit einem beliebigen Passwort versehen. Die Kommandozeile des Mysql-Servers verlassen wir mit _quit_.

  


Fur die weitere Konfiguration ist moglicherweise die Installation des Dateimanagers Midnight Commander sinnvoll. Über den lasst sich durch das Dateisystem hangeln, er ist nach der Installation mit dem Texteditor Nano verknupft. Mit Alt-F4 lassen sich so Konfigurationsdateien im Midnight Commander direkt zum Editieren offnen. In Nano lasst sich mit Strg-W nach Zeichenketten suchen. Mit Strg-O werden die Änderungen gespeichert.

Im Apache-Webserver mussen noch einige Anpassungen vorgenommen werden. Die Voreinstellungen verhindern beispielsweise, dass keine Dateien hochgeladen werden konnen, die großer sind als 2 MByte. Dafur muss in der Konfigurationsdatei _/etc/php5/apache2/php.ini_ die Zeile _upload_max_filesize_ angepasst werden. Hier kann ein beliebig sinnvoller Wert gesetzt werden, auf die Leistung von Owncloud hat das keinen Einfluss.

### Große Dateien speichern

Wir haben uns fur den Wert 4G entschieden, damit wir maximal 4 GByte große Dateien speichern konnen. Parallel dazu muss in der gleichen Konfigurationsdatei die Zeile _post_max_size_ mit dem identischen Wert versehen werden. Schließlich muss noch der Wert _output_buffering_ aktiviert und auf _= 4096_ gesetzt werden. Das auf dem Raspberry Pi verwendete Dateisystem Ext4 kann durchaus mit Dateien in dieser Große umgehen, allerdings sollte hier die doch recht schwache Hardware des Raspberry Pi berucksichtigt werden. Bei kleinen Dateien spielt sie kaum eine Rolle, bei großen Dateien ist der kleine Rechner einfach nicht leistungsfahig genug, was die Schreibgeschwindigkeit betrifft.

Damit die Daten zwischen Clientbrowser und dem Owncloud-Server im Netz verschlusselt uber SSL ubertragen werden, mussen noch entsprechende Zertifikate bereitgestellt werden. Hier gibt es zwei Moglichkeiten. Es konnen selbst erstellte Zertifikate verwendet oder offizielle etwa bei einem kostenlosen Dienst bestellt werden.

### Eigenes Zertifikat erstellen

Selbst erstellte Zertifikate eignen sich vornehmlich dann, wenn das Raspberry Pi immer im eigenen Netzwerk verwendet werden soll. Sowohl Owncloud-Clients als auch Browser beschweren sich naturgemaß uber eigene Zertifikate. Sie lassen sich aber dennoch meist auf dem Clientrechner installieren und nutzen. Googles Chromium ist da eine Ausnahme, hier gelang es uns nicht, das Zertifikat nachzureichen.

Eine Verschlusselung ist allerdings zwingend notwendig, selbst im eigenen Netz und besonders wenn die Verbindung uber unverschlusseltes WLAN erfolgt. Denn sonst konnen Angreifer sowohl ubertragene Passworter als auch die Daten im Klartext abgreifen. Zunachst aktivieren wir mit _a2enmod ssl_ das SSL-Modul in Apache2 und erstellen mit _mkdir -p /etc/apache2/ssl_ das Verzeichnis, in dem die Zertifikate abgelegt werden.

Wir generieren jetzt sicherheitshalber ein eigenes Zertifikat, das speziell fur Owncloud bestimmt ist, kein Passwort benotigt und fur ein Jahr gultig ist. Dazu geben wir folgenden Befehl ein:

_openssl req -newkey rsa:4096 -sha512 -x509 -days 365 -nodes -keyout /etc/apache2/ssl/owncloud.key -out /etc/apache2/ssl/owncloud.crt_

Da wir Owncloud im lokalen Netzwerk verwenden, konnen hier beliebige Eingaben gemacht werden. Bei Common Name muss der Name des Rechners - in unserem Fall "raspberrypi" \- verwendet werden, der auch in der Datei _/etc/hosts_ steht. Sonst funktioniert Webdav mit Owncloud nicht.

  


### Apache konfigurieren

Wir kopieren im Verzeichnis _/etc/apache2/sites-available_ die Konfigurationsdatei _default-ssl_ mit dem Befehl _cp_ nach _owncloud_. In dieser fugen wir unter der Zeile "ServerAdmin" die Zeile "ServerName raspberrypi" ein. Dann passen wir die Pfade in den Zeilen SSLCertificateFile und SSLCertificateKeyFile so an, dass sie zu den eben generierten owncloud.crt (das Zertifikat) und owncloud.key (der Schlussel) zeigen. Vor den letzten beiden Zeilen legen wir noch folgenden Abschnitt an:

![](https://www.golem.de/fileadmin/tx_bbcampaigns/3623--ad/appian_whitepaper_digitale_transformation_wm.jpg)

_<Directory /var/www/owncloud>_   
_Options Indexes FollowSymLinks MultiViews_   
_AllowOverride All_   
_Order allow,deny_   
_Allow from all_   
_Satisfy Any_   
_</Directory>_

Anschließend mussen noch die Befehle _a2enmod rewrite_ und _a2enmod headers_ ausgefuhrt werden, damit die Änderungen ubernommen werden. Außerdem muss das Dav-Modul mit _a2enmod dav_fs_ aktiviert werden. Der neue virtuelle Server wird mit _a2ensite owncloud_ aktiviert. Schließlich wird der Webserver mit _service apache2 restart_ neu gestartet.

### Owncloud starten und einrichten

Jetzt lesen wir die IP-Adresse des Raspberry Pi mit dem Befehl _ifconfig_ aus. Diesen geben wir im Firefox-Browser eines weiteren Rechners im lokalen Netz ein beginnend mit _https://_. Es folgt die Aufforderung, dem Zertifikat zu vertrauen. Da wir das Zertifikat selbst erstellt haben, bestatigen wir die Abfrage.

Anschließend wird Owncloud konfiguriert. Zunachst wird ein Administratorkonto samt Passwort angelegt. Unter dem Dropdownmenu "Fortgeschritten" wahlen wir Mysql aus und geben dort die Werte ein, die wir zuvor bei der Einrichtung der Datenbank festgelegt haben. Unter Datenbank-Host muss "localhost" eingetragen werden.

  


Danach ist die Owncloud-Oberflache im Browser zu sehen. Rechts oben befinden sich der Benutzername und ein Dropdownmenu mit dem Eintrag Administration. Dort lassen sich Feineinstellungen vornehmen und Fehlermeldungen einsehen. Links unten im Fenster ist ein Pluszeichen, uber das sich weitere Apps installieren lassen. Bereits installiert ist die Erweiterung "Encryption", die dort aktiviert werden kann. Dann werden samtliche Dateien verschlusselt, die bei Owncloud hochgeladen werden. Anschließend ist eine Neuanmeldung fallig. Im Adminstrationsbereich lasst sich noch ein Wiederherstellungsschlussel aktivieren, damit auch im Notfall die Daten wieder entschlusselt werden konnen. Wem der Speicherplatz auf der SD-Karte zu knapp wird, kann dort auch externe Datentrager einbinden, die uber USB an das Raspberry Pi angeschlossen sind.

Damit das Raspberry Pi immer unter der gleichen IP-Adresse erreichbar ist, kann noch die Textdatei /etc/network/interfaces angepasst werden. Statt des Eintrags _iface eth0 inet dhcp_ mussen dann folgende Zeilen eingetragen werden:

_iface eth0 inet static_   
_address *mit ifconfig ausgelesene IP-Adresse*_   
_netmask 255.255.255.0_   
_ gateway *IP-Adresse des Routers*_.

Danach wird das Netzwerk-Subsystem des Raspberry Pi mit dem Befehl _/etc/init.d/networking restart_ neu gestartet. Eine feste IP-Adresse stort den DHCP-Server im Netzwerk nicht, solange die feste IP-Adresse nicht bereits von einem anderen Gerat verwendet wird. Ein weiterer Vorteil einer festen IP-Adresse: Wir konnen das Raspberry Pi jetzt einfach uber SSH verwalten, ohne muhsam die IP-Adresse zu ermitteln. Von Windows aus lasst sich das beispielsweise mit [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) erledigen.

### Auch im Internet erreichbar

Wer seinen Owncloud-Server im Internet erreichbar haben will, muss sich zunachst einen eigenen Domainnamen besorgen, etwa beim Dyndns-Anbieter No-IP. Dieser muss sowohl im Zertifikat als auch in den Apache-Konfigurationsdateien und in der Datei _/etc/hosts_ eingetragen werden. Außerdem muss das Raspberry Pi bei Änderungen der IP-Adresse diese dem Dnydns-Hoster mitteilen. Die meisten Dyndns-Anbieter bieten solche Skripts oder entsprechende Anleitungen an. Außerdem muss im Router eine Weiterleitung zum Raspberry Pi auf Port 80 und 443 eingerichtet werden.

[Clients](http://owncloud.org/sync-clients/) gibt es fur Windows, Mac OS X, zahlreiche Linux-Distributionen sowie Android, iOS und weitere mobile Plattformen. Owncloud ist inzwischen nicht nur als Dateiserver verwendbar. Es lassen sich beispielsweise Kalenderdaten, Kontakte und Bookmarks synchronisieren. Außerdem gibt es zahlreiche Apps von Drittanbietern, etwa fur die Synchronisierung von Mozillas Firefox. [Ein ausfuhrliches Handbuch](http://doc.owncloud.org/server/6.0/admin_manual/contents.html) erklart die Installation und weitergehende Konfiguration.

Owncloud ist indes nicht der einzige Anbieter. Auch [Seafile](http://seafile.com/en/home/) und [Sparkleshare](http://sparkleshare.org/) sind ebenfalls Open Source und bieten einen ahnlichen Konfigurationsumfang. Beide werden wir uns in einem spateren Artikel noch ansehen.
