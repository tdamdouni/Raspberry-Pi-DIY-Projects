# Raspberry Pi als Synchronisationszentrale

_Captured: 2017-05-06 at 16:33 from [www.raspberry-pi-geek.de](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale)_

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/03/raspberry-pi-als-synchronisationszentrale/aa_ruderer_10202204_123rf_36clicks_resized.jpg2/11150-1-ger-DE/AA_ruderer_10202204_123rf_36clicks_resized.jpg_large.jpg)

> _(C) 36clicks, 123RF_

Den Datenbestand zwischen mobilen und stationaren Rechnern wie Tablets, Smartphones und Laptops konsistent zu halten, erweist sich nicht immer als einfach. Auch Cloud-Anbieter wie Dropbox decken nur einen Teil davon ab. Mit vergleichsweise einfachen Mitteln ubernimmt der Raspberry Pi als Hub diesen Job.

Das alte Microsoft-Motto "ein PC auf jedem Schreibtisch" gilt langst als uberholt, der Zoo an taglich genutzten intelligenten Geraten wachst und wachst. Notgedrungen gilt dasselbe auch fur den Bedarf an Datenaustausch - Datensynchronisation heißt das Zauberwort. Das Problem: Schon bei funf Geraten (Server, Desktop, Laptop, Tablet, Smartphone) gibt es jede Menge mogliche Verbindungen. Ein zentraler Synchronisationsserver ersetzt dann sinnvollerweise die einzelnen Punkt-zu-Punkt-Verbindungen, der Datenaustausch findet asynchron uber einen zentralen Hub statt ([Abbildung 1](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale)).

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/03/raspberry-pi-als-synchronisationszentrale/abbildung-12/11153-1-ger-DE/Abbildung-1_large.png)

> _Abbildung 1: Wer den Datenbestand zwischen verschiedenen Geraten konsistent halten mochte, kommt um einen zentralen Hub zur Synchronisation nicht vorbei._

Der Hub bleibt immer verfugbar, die einzelnen Gerate nicht - damit entfallen nicht nur die vielen Einzelverbindungen, sondern auch die Notwendigkeit, dass die am Datenaustausch beteiligten Gerate gleichzeitig online sind. Die Konsequenz daraus: die Datenaustauschzentrale sollte auf einem moglichst stromsparenden Rechner laufen - jedes Watt kostet bei 27 Cent Stromkosten pro kWh immerhin 2,37 Euro im Jahr. Damit eignet sich ein Minirechner wie der Raspberry Pi ideal als Grundlage fur einen Sync-Server (siehe [Kasten "Wie viel Server braucht es?"](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale))

In vielen Haushalten lauft inzwischen ein NAS (Network Attached Storage), das als Dateiablage dient und immer ofter auch Cloud-Dienste bereitstellt. Zum Teil deckt ein solches System auch Synchronisationsaufgaben ab, einen zusatzlichen Sync-Server benotigen Sie dann nicht mehr.

Falls das NAS mit einem proprietaren OS arbeitet oder Sie es wegen des Stromverbrauchs nur bei Bedarf einschalten, kann ein kleiner Rechner in die Bresche springen. Viel Schreib- und Leseleistung muss er gar nicht bereitstellen, denn bei der Synchronisation wandern in der Regel nur kleine Datenmengen uber die Leitung.

Alle Dienste, die dieser Artikel beschreibt, funktionieren nicht nur auf dem RasPi problemlos, sondern beispielsweise auch mit dem Mini-Router TP-Link MR3020 [[12]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) samt USB-Stick. Die einzige Ausnahme stellt das Backup-Szenario dar - hier dauert ein typischer Lauf beim TP-Link ungefahr vier Mal so lange wie beim Raspberry Pi. Dafur benotigt das Gerat aber auch nur ein Watt und erlaubt daruber hinaus einen mobilen Einsatz.

#### Alternative Dropbox?

Dropbox gilt heute fast als Synonym fur die plattformubergreifende Datensynchronisation. Wer diese nicht dem amerikanischen Hoster uberlassen will, wahlt freie Alternativen wie Owncloud [[1]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) oder Seafile [[2]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8). Beide Losungen laufen auch auf dem Raspberry Pi [[3]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8). Doch nicht immer passt das Schema von Dropbox, samtliche Daten auf allen beteiligten Geraten synchron zu halten, auf das Problem.

Geht es um das Synchronisieren von Daten, die sich gewohnlich in einer Datenbank befinden, versagt Dropbox komplett. Das betrifft beispielsweise das Synchronisieren von Firefox-Daten, Adressbuchern oder Terminkalendern. Aber selbst bei normalen Dateien gibt es Anwendungsfalle, die mit anderen Diensten einfacher funktionieren. Das liegt daran, dass Dropbox es nicht erlaubt, Ordner oder Dateien nur mit bestimmten Geraten zu synchronisieren - sie landen stets auf allen. Mochten Sie beispielsweise bearbeitete und kleingerechnete Bilder per Smartphone vorzeigen, brauchen Sie diese auch nur dort - und nicht etwa auf einem anderen PC.

Der RasPi bietet die Moglichkeit, verschiedene Sync-Losungen parallel zu betreiben. Sie kommen sich nicht ins Gehege, und der Ressourcenbedarf fallt auch nicht so umfangreich aus, dass er den Minirechner uberfordern wurde.

#### Vorarbeiten

Als Ausgangspunkt der vorgestellten Losung dient ein abgespecktes Raspbian-System. Das Deinstallieren aller nicht benotigten Pakete druckt den Platzbedarf der Installation auf deutlich unter 1 GByte, also weniger als ein Drittel der aktuellen Raspbian-Distribution. Damit bleibt genug Speicherplatz fur den Datenaustausch. Um den Artikel nachzuvollziehen, verwenden Sie zunachst aber die Standardversion.

Fur zwei der Losungen benotigt der RasPi einen lauffahigen Webserver samt PHP. Als Vorarbeit installieren Sie mit Root-Rechten die notwendigen Pakete mit dem Skript aus [Listing 1](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale). Wir entschieden uns fur den leichtgewichtigen Webserver Lighttpd; Raspbian bietet mit Apache oder Nginx aber auch Alternativen, die genauso funktionieren.

Listing 1
    
    
    #!/bin/bash
    # Installation Webserver
    apt-get update
    apt-get install lighttpd
    # PHP5 Basisinstallation plus Cache
    apt-get install php5-cgi php-apc
    ln -s /usr/share/doc/php-apc/apc.php /var/www/
    lighttpd-enable-mod fastcgi-php
    /etc/init.d/lighttpd force-reload
    # Systeminfo über PHP
    apt-get install php-sysinfo
    ln -s /usr/share/phpsysinfo /var/www/status
    # Rechte setzen
    chown -R www-data:www-data /var/www

Das letzte Paket, _phpsysinfo_, benotigen Sie nicht zwingend - es zeigt aber auf einen Blick, ob die Installation geklappt hat. Dazu rufen Sie im Browser die URL `http://_RasPi-IP_/status` auf ([Abbildung 2](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale)).

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/03/raspberry-pi-als-synchronisationszentrale/abbildung-22/11156-1-ger-DE/Abbildung-2_large.png)

> _Abbildung 2: Die Status-Seite von Phpsysinfo zeigt auf einen Blick den Zustand des Systems und des Webservers._

Der Artikel geht davon aus, dass der Server nur im Heimnetz lauft und Sie deshalb keine sichere Verbindung via HTTPS benotigen.

  


#### Firefox-Sync

Firefox integriert schon seit Jahren eine eigene Sync-Engine. Mit ihr lassen sich Bookmarks, Cookies, Passworter und so weiter uber verschiedene Installationen synchronisieren. Die Daten liegen dabei auf von Mozilla gehosteten Servern.

Das Verfahren gilt als sicher, da der Browser die Daten auf Client-Seite ver- und entschlusselt. Da Mozilla den Schlussel nicht besitzt, kann es auf die Daten nicht zugreifen. Trotz dieses vorbildlichen Verfahrens spricht vieles dafur, den Sync-Server selbst zu betreiben - nicht zuletzt die Tatsache, dass dies das Ausspionieren der Daten erheblich erschwert.

Der ursprungliche Server ist zwar in Python implementiert, in unserem Fall verwenden wir jedoch die schlanke PHP-Variante FSyncMS (Firefox-Sync Minimal Server) [[4]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) . Dazu entpacken Sie das Paket im Wurzelverzeichnis `/var/www/` des Webservers (siehe Befehle [Listing 2](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/2)). Der Mv-Befehl gestaltet den Pfad etwas eingangiger, `chown` sorgt fur die richtigen Rechte. Gespeichert werden die Daten in einer SQLite3-Datenbank, dafur installiert das Skript auch noch das notwendige PHP-Modul.

Listing 2
    
    
    #!/bin/sh
    # FSyncMS installieren
    wget https://www.dataharbour.de/FSyncMS.tar.gz
    if [ -f FSyncMS.tar.gz ]; then
      tar -xvzpf FSyncMS.tar.gz -C /var/www
      mv /var/www/FSyncMS /var/www/ffsync
      chown -R www-data:www-data /var/www/ffsync
      rm -f FSyncMS.tar.gz
    fi
    # PHP5-Schnittstelle zu SQLite installieren
    apt-get update
    apt-get install php5-sqlite
    /etc/init.d/lighttpd restart

Fur die initiale Konfiguration des Sync-Servers rufen Sie die Seite `http://_RasPi-IP_/ffsync/` auf. Wichtig: Loschen Sie danach die Datei `setup.php` im Installationsverzeichnis. Kontrollieren Sie außerdem den Inhalt der Datei `settings.php`, insbesondere den Pfad des Servers mussen Sie eventuell noch anpassen. Mochten Sie den Server uber das Internet anbinden, sollten Sie noch die SQLite-Datei aus dem Webserver-Verzeichnis verschieben und den neuen Pfad ebenfalls in der Konfigurationsdatei andern.

Die Installation dauert insgesamt nur wenige Minuten. Ob alles geklappt hat, zeigt die Statusseite `http://_RasPi-IP_/ffsync/index.php/`. Als Antwort erhalten Sie zwar eine Fehlermeldung, die Ihnen aber zeigt, dass der Server die Anfrage verarbeitet.

Danach gilt es nur noch, einen Account einzurichten und die Firefox-Browser aller beteiligten Gerate an diesen Account zu binden. Dazu offnen Sie im Browser via _Bearbeiten_ | _Einstellungen…_ die _Firefox-Einstellungen_ und wechseln darin in den Abschnitt _Sync_. Hier klicken Sie auf _Firefox-Sync einrichten_. Im nachsten Dialog wahlen Sie _Neues Benutzerkonto anlegen_ und fullen die Felder entsprechend aus ([Abbildung 3](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/2)).

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/03/raspberry-pi-als-synchronisationszentrale/abbildung-32/11159-1-ger-DE/Abbildung-3_large.png)

> _Abbildung 3: Firefox erlaubt es problemlos, mehrere Installationen uber einen zentralen Server - in unserem Fall auf einem Raspberry Pi - zu synchronisieren._

Neue Gerate fugen Sie auch uber das Sync-Menu hinzu. Hier mussen Sie den bestehenden Account verwenden. Anschließend erhalten Sie einen dreimal dreistelligen Sicherheitscode, den Sie am ersten Rechner unter `Gerat verbinden` eingeben. Eventuell vorhandene Fehlerberichte rufen Sie uber die Pseudo-URL `about:sync-log` direkt im Browser ab.

#### Termine und Adressen

Fast jeder Smartphone-Nutzer synchronisiert seine Termin- und Kalenderdaten mit dem Hersteller seines Betriebssystems, meist Google oder Apple. Damit kommen schutzwurdige Daten in die Hande von Dritten. Verschiedene Open-Source-Projekte versuchen hier eine freie Alternative zu bieten, eine der bekanntesten davon heißt Owncloud.

Allerdings kampft das Projekt seit den ersten Versionen mit Performance- und Stabilitatsproblemen. Statt diese zu losen, bauen die Entwickler von Version zu Version weitere "coole" Features ein - sehr zum Leidwesen der Anwender. Der einzige Vorteil von Owncloud: Diverse Provider bieten Owncloud-Instanzen oder Accounts sehr gunstig an, was im hiesigen Szenario allerdings wenig hilft.

Owncloud wirbt mit der Sicherheit der Daten, die es nur verschlusselt auf den Servern der Provider ablegt. Was die Firma verschweigt: Das gilt nicht fur Termin- und Kalenderdaten. Auf beide greifen Clients mit den Protokollen CalDAV beziehungsweise CardDAV zu, die keinen Support fur die clientseitige Verschlusselung der Daten bieten - der Transport erfolgt per HTTPS.

Grund genug, die Daten selbst zu hosten. Aus Grunden der Performance und Stabilitat bietet sich aber Baikal [[5]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) als bessere Alternative an. Das Tool beherrscht zwar nur das Synchronisieren von Termin- und Adressdaten uber das CalDAV- beziehungsweise CardDAV-Protokoll, dafur aber ohne Fehl und Tadel. Groupware-Funktionen wie offentliche Kalender und Terminplanung uber Kalender hinweg unterstutzt es nicht.

  


#### Baikal installieren

Am einfachsten installieren Sie Baikal mit dem Skript aus [Listing 3](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/4). Dieses ladt das Paket in das Verzeichnis `/var/www/baikal` des Webservers und schaltet die initiale Konfiguration frei. Zeile 10 erzeugt dafur eine leere Datei, die nach der Erstkonfiguration wieder verschwindet.

Listing 3
    
    
    #!/bin/bash
    VERSION="0.2.6"
    # Download und Entpacken
    wget http://baikal-server.com/get/baikal-flat-${VERSION}.zip
    if [ -f baikal-flat-${VERSION}.zip ]; then
      unzip baikal-flat-${VERSION}.zip -d /var/www
      mv /var/www/baikal-flat /var/www/baikal
      touch /var/www/baikal/Specific/ENABLE_INSTALL
      chown -R www-data:www-data /var/www/baikal
      rm -f baikal-flat-${VERSION}.zip
    fi

Die webbasierte Erstkonfiguration erreichen Sie uber den Browser unter `http://_RasPi-IP_/baikal/`. Sie beschrankt sich auf die Eingabe der Zeitzone und des Admin-Passworts. Danach melden Sie sich als Admin unter `http://_RasPi-IP_/baikal/admin/` an und definieren Benutzer und Kalender ([Abbildung 4](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/4)).

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/03/raspberry-pi-als-synchronisationszentrale/abbildung-42/11162-1-ger-DE/Abbildung-4_large.png)

> _Abbildung 4: In der webbasierten Konfigurationsoberflache von Baikal definieren Sie Benutzer und Kalender._

#### Baikal nutzen

Baikal bietet außer der Admin-Oberflache zum Verwalten von Benutzern und Kalendern nichts weiter an. Die Kalender selbst sehen Sie aber mit allen Clients, die das CALDAV-Protokoll unterstutzen, zum Beispiel mit dem Lightning-Plugin fur Thunderbird.

Wunschen Sie sich ein Webfrontend fur Ihren Kalender, dann installieren Sie CalDavZAP [[6]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) auf dem RasPi. Die notwendigen Installationsbefehle zeigt [Listing 4](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/4), das Sie nur noch an Ihre Bedurfnisse anpassen mussen, indem Sie Hostname, Port und Versionsnummer oben eintragen. Das Skript editiert auch automatisch ein paar Zeilen der zwar gut kommentierten, aber trotzdem etwas unubersichtlichen Konfigurationsdatei `config.js` - hier sind auch weitere Anpassungen moglich. Nach der Installation greifen Sie bequem per Browser uber die Seite `http://_RasPi-IP_/cal` auf den Kalender zu.

Listing 4
    
    
    #!/bin/bash
    VERSION="0.10.0.1"
    HOST="localhost"
    PORT="8080"
    # Download und Entpacken
    wget http://www.inf-it.com/CalDavZAP_${VERSION}.zip
    if [ -f CalDavZAP_${VERSION}.zip ]; then
      unzip CalDavZAP_${VERSION}.zip -d /var/www
      mv /var/www/caldavzap /var/www/cal
      sed -i \
       -e "s%var globalInterfaceLanguage='en_US';%var globalInterfaceLanguage='de_DE';%" \
       -e "s%//var globalUseJqueryAuth=false;%var globalUseJqueryAuth=true;%" \
       -e "s%^var globalNetworkCheckSettings%//var globalNetworkCheckSettings%" \
       -e "/http:\/\/lion/s%^//var globalNetworkCheckSettings%var globalNetworkCheckSettings%" \
       -e "s%lion.server.com:8008/principals/users/%${HOST}:${PORT}/baikal/cal.php/principals/%" \
       /var/www/cal/config.js
      chown -R www-data:www-data /var/www/cal
      rm -f CalDavZAP_${VERSION}.zip
    fi

Fur Adressdaten gibt es analog das Tool CardDavMate [[7]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) mit fast identischer Installation und Konfiguration - allerdings scheint es damit nach Benutzermeldungen noch Probleme zu geben.

Wichtiger als der Zugriff per Browser ist der Anschluss von mobilen Geraten. Nutzer der "iWelt" sind hier fein raus, denn die Programme von Apple sprechen nativ die CalDAV- und CardDAV-Protokolle.

Android-Anwender mussen sogenannte Sync-Adapter installieren. Stabil, aber (noch) nicht frei sind die Apps CalDav-Sync und CardDav-Sync. Wer ganz auf Open Source setzen will, der verwendet CalDav-Sync Free Beta oder DavDroid. Beide laden Sie uber den Playstore, F-Droid steht daruber hinaus als Quellcode zum Download bereit [[8]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8). Wahrend beim Autor die erste App seit Monaten ohne Probleme lauft, gilt DavDroid noch nicht als stabil und fehlerfrei.

Egal, welche Software Sie wahlen: Die Zugriffsadressen auf den Baikal-Server lauten fur einen Benutzer mit der ID _tux_, der einen Arbeitskalender und Adressbuch jeweils mit der ID _work_ besitzt, `http://_RasPi-IP_/baikal/cal.php/calendars/tux/work` und `http://_RasPi-IP_/baikal/card.php/addressbooks/tux/work`.

  


#### Rsync: Tipps und Tricks

Lange galt Rsync als der Platzhirsch unter den Sync-Tools fur Unix, wurde aber von Dropbox etwas in den Schatten gestellt. Dabei gilt das kleine Tool als das Schweizer Messer der Synchronisation schlechthin. Optional ubertragt es nur die Änderungen und verifiziert, dass alles richtig ankommt - womit es sich auch beim lokalen Kopieren als außerst nutzlich erweist. Folgender Befehl kopiert das Verzeichnis `/home/pi/src` vom lokalen auf einen zweiten Rechner `pi2`:
    
    
    $ rsync -avz /home/pi/src admin@pi2:/home/admin

Dort erfolgt im Beispiel die Anmeldung als Benutzer _admin_, das Zielverzeichnis lautet `/home/admin`. Quelle und Ziel konnen Sie auch andersherum angeben, dann holt Rsync das Verzeichnis vom entfernten Rechner. Sorgfalt ist bei den Pfadnamen geboten: Bei einem Quellverzeichnis ohne Slash (`/`) am Ende kopiert Rsync das ganze Verzeichnis - im Beispiel `src` - ansonsten nur dessen Inhalt. Beim Zielverzeichnis spielt es keine Rolle, ob ein Schragstrich am Ende steht oder nicht.

Die Option `-v` bedeutet "verbose" und gibt alle ubertragenen Dateien aus, wahrend `-z` fur die Kompression wahrend der Übertragung sorgt. Zum Synchronisieren von Bildern, MP3-Dateien oder anderen bereits komprimierten Formaten eignet sie sich nicht. Rsync bringt aber bereits eine eingebaute Liste mit relevanten Dateiendungen mit und macht im Normalfall alles richtig. Naheres dazu erklart die Manpage.

Dieser einfache Rsync-Befehl mit drei Optionen deckt schon sehr viel ab. Die restlichen 110 Parameter von Rsync kommen in der Regel nur bei Spezialfallen zum Einsatz.

#### Datentransfer uber den Hub

Das in der Einleitung beschriebene Szenario, kleingerechnete Bilder vom Desktop an das Smartphone zu senden, funktioniert mit Rsync, indem der Desktop die Dateien an den Hub schickt, wobei Rsync automatisch die korrekt ubertragenen Dateien loscht:
    
    
    $ rsync -av --remove-source-files /data/bilder hub:/data/

Spater holt das Smartphone die Dateien mit derselben Option wieder ab. Auf dem Hub sammeln sich also nicht unnotig Daten.

Fur Android gibt es passend die freie, aber nicht quelloffene App RSyncBackup. In einem sogenannten Profil legen Sie quasi die Kommandozeile fest und fuhren den Befehl dann mit einem Klick auf das Profil aus - sehr praktisch, wenn Sie immer wieder dieselben Verzeichnisse fur den Datentransfer verwenden.

Rsync beherrscht auch Spiegelung - also die Einweg-Synchronisation von einem Rechner auf einen zweiten. Hier mussen Sie die Option `\--remove-source-files` durch die Option `\--delete` ersetzen. Diese loscht auf dem Zielrechner anstatt auf dem Quellrechner auch Verzeichnisse, was die erste Option nicht unterstutzt.

Benotigen Sie eine Zweiwege-Synchronisation, sollten Sie auch einen Blick auf Unison [[9]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) werfen. Es nutzt den Rsync-Algorithmus, bietet aber neben dem reinen Kommandozeilenbetrieb auch eine schone Oberflache. Unison steht im Raspbian-Repository zur Installation bereit.

  


#### Backup mit Rsync

Rsync eignet sich auch hervorragend fur Backups. Ein RasPi als Hub eignet sich naturgemaß nur bedingt dafur - je nach angeschlossenem Massenspeicher und zu sichernder Datenmenge laufen Datensicherungen sehr lange oder brauchen schlichtweg zu viel Platz. Fur das schnelle Backup wichtiger Konfigurationsdateien in den Verzeichnissen `/home` und `/etc` spart ein Hub aber das Hochfahren des großen Fileservers. Die Sicherungen auf dem Hub holt dann der Fileserver ab, sobald er wieder am Netz ist.

Mit dem Tool Rsnapshot [[10]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) legen Sie automatisierte Backups einschließlich hierarchischer Generationen an - etwa taglich, wochentlich oder monatlich. Die Software steht im Raspbian-Repository zum Abruf bereit. Sie verwendet Rsync als Unterbau und ersetzt dabei mit der Option `\--link-dest` Dateien auf dem Zielverzeichnis durch Hardlinks identischer Dateien der Vorgangergeneration. Dadurch verkleinern sich nicht nur die tatsachlich kopierten Dateimengen, sondern es existieren auch mehrere Generationen von Backups, ohne dass damit der Plattenplatz im gleichen Maße steigt.

Ein Nachteil von Rsnapshot: Es holt zwar Dateien von entfernten Rechnern ab, legt sie aber nur lokal ab. Damit musste es auf dem Hub laufen und alle angeschlossenen Gerate vor dem Start des Backups anfragen. Zwei kleine Bash-Skripte ersetzen deshalb diese Funktionalitat.

Das erste ([Listing 5](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8)) kopieren Sie auf den Hub, das zweite ([Listing 6](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8)) lokal auf die Rechner. [Listing 6](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) ruft [Listing 5](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8) remote auf (Zeilen 8, 11 und 18) und bereitet so das Backup vor, bevor dann Rsync zum Zug kommt (Zeile 14 und 15 in [Listing 5](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8)). Der Rsync-Befehl legt dabei im Zielverzeichnis einen Spiegel des Home-Verzeichnisses an.

Listing 5
    
    
    #!/bin/bash
    HUB="rpi"                               # Hostname des Hubs
    rscript="/usr/local/bin/backup-server"  # Skript auf dem Hub
    turnus="${1:-daily}"                    # Erstes Argument oder daily
    # alte Sicherung rotieren
    ssh "${HUB}" "${rscript}" "rotate" "${HOSTNAME}" "${turnus}"
    # neues Sicherungsverzeichnis erstellen und in "dir" speichern
    dir=$(ssh "${HUB}" "${rscript}" "prepare" "${HOSTNAME}" "${turnus}")
    # Home-Verzeichnis auf dem Hub nach "dir" sichern
    rsync -avz --delete --numeric-ids --relative --delete-excluded \
          --link-dest="${dir/.00/.01}/" "${HOME}" "${HUB}:${dir}"
    # Aufräumen (überflüssige Generation(en) löschen)
    ssh "${HUB}" "${rscript}" "cleanup" "${HOSTNAME}" "${turnus}" "30"

Listing 6
    
    
    #!/bin/bash
    # remote backup support-script
    # rotate: nennt Backups um: name.03->name.04, name.02->name.03 usw.
    # prepare: erstellt neues Backup-Verzeichnis name.00
    # cleanup: löscht alle Backup-Verzeichnisse mit zu hoher Nummer
    # Konfiguration
    backupRoot=/data/backups
    # --- Backups rotieren --------
    rotate() {
      remoteHost=$1
      backupType=$2
      backupDir=${backupRoot}/${remoteHost}
      find ${backupDir}/${backupType}.* -type d -maxdepth 0 | sort -r | while read dir; do
        nr=${dir##*.}
        nr=${nr#0}
        let nr1=nr+1
        nr1=$(printf %02d $nr1)
        mv ${dir} ${backupDir}/${backupType}.${nr1}
      done
    }
    # --- Backup vorbereiten   -------
    prepare() {
      remoteHost=$1
      backupType=$2
      backupDir=${backupRoot}/${remoteHost}
      targetDir=${backupDir}/${backupType}.00
      mkdir -p ${targetDir}
      echo ${targetDir}
      exit 0
    }
    # --- Lösche altes Backup ------
    cleanup() {
      remoteHost=$1
      backupType=$2
      maxGen=$3
      backupDir=${backupRoot}/${remoteHost}
      while [ ${maxGen} -lt 100 ]; do
        nr=$(printf %02d ${maxGen})
        if [ ! -d ${backupDir}/${backupType}.${nr} ]; then
          exit 0
        else
          rm -fr ${backupDir}/${backupType}.${nr}
          let maxGen=maxGen+1
        fi
      done
    }
    # --- Hauptprogramm -------
    func=$1
    # prüfe erlaubte Funktionen
    grep -qw ${func} <<< prepare rotate cleanup || exit 3
    shift
    eval ${func} $@

Damit Sie nicht jeder Aufruf von SSH und Rsync mit einer Passwortabfrage belastigt, erstellen Sie ein Schlusselpaar und kopieren vorher Ihren offentlichen Schlussel auf den RasPi [[11]](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8). Samtliche in diesem Artikel abgedruckten Listings sowie ein Raspbian-Image, das alle notigen Komponenten bereits vorinstalliert mitbringt (siehe [Kasten "Komfortables Image"](http://www.raspberry-pi-geek.de/Magazin/2014/03/Raspberry-Pi-als-Synchronisationszentrale/\(offset\)/8)), finden Sie auf der Heft-DVD.

Auf der Heft-DVD finden Sie im Verzeichnis `/RPG/sync/` ein vorkonfiguriertes Raspbian-Image fur den vorgestellten Sync-Server. Es nutzt Lighttpd als Webserver und SQLite3 als Datenbank. Der Firefox-Sync Minimal Server FSyncMS, der CalDAV/CardDAV-Synchronisierer Baikal und die Skripts fur das Rsnapshot-basierte Backup sind bereits vorinstalliert.

Um das Image auf eine mindestens 2 GByte große SD-Karte aufzuspielen, entpacken Sie das Archiv `raspi-sync.img.zip` und kopieren das Abbild mittels folgenden Befehls auf die SD-Card:
    
    
    # dd if=raspi-sync.img of=/dev/xxx

Dabei setzen Sie fur `_xxx_` den Geratebezeichner der SD-Karte ein, der in den meisten Fallen `sdb` lauten durfte. Windows-Anwender greifen statt zu `dd` zum Win32DiskImager, den Sie im Verzeichnis `\RPG\windows` auf dem Heftdatentrager finden.

Das fur den Headless-Betrieb ausgelegte Image holt sich seine IP-Adresse per DHCP. Sie melden sich per SSH mit dem Benutzernamen _pi_ und dem Passwort `raspberry` am System an. Da das Abbild bereits fur deutsche Nutzer lokalisiert wurde, mussen Sie bei `raspberry` tatsachlich ein Y und nicht etwa ein Z tippen. Weitere Infos, wie etwa die in Baikal vordefinierten Benutzer samt deren Passwortern, stehen in `/etc/motd`, sodass das System sie Ihnen beim Login automatisch anzeigt.

Nach dem ersten Start mussen Sie noch einige Änderungen in Konfigurationsdateien vornehmen, da sowohl Firefox-Sync als auch CalDavZap die Hostnamen wissen mussen, auf denen der Service lauft. Naheres dazu entnehmen Sie bitte dem Artikel.

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/03/raspberry-pi-als-synchronisationszentrale/bablok-bernhard.png2/11165-1-ger-DE/bablok-bernhard.png_large.png)

Bernhard Bablok arbeitet bei der Allianz Managed&Operations Services SE als SAP-HR-Entwickler. Wenn er nicht Musik hort, mit dem Radl oder zu Fuß unterwegs ist, beschaftigt er sich mit Themen rund um Linux und Objektorientierung. Sie erreichen ihn unter `mail@bablokb.de`.
