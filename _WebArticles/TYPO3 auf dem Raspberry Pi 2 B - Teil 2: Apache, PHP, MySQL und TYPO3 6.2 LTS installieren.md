# TYPO3 auf dem Raspberry Pi 2 B - Teil 2: Apache, PHP, MySQL und TYPO3 6.2 LTS installieren

_Captured: 2015-12-20 at 14:20 from [www.co-operate.net](https://www.co-operate.net/artikel/archive/2015/03/01/article/typo3-auf-dem-raspberry-pi-2-b-teil-2-apache-und-mysql-kopie-1.html)_

Die Rechenpower des neuen Raspberry Pi 2 B reicht tatsachlich fur einen TYPO3-Server zu Test- und Entwicklungszwecken aus. Hier die Schritte fur eine erfolgreiche Installiation von Apache2, MySQL 5.5, PHP 5.4 und TYPO3 6.2 LTS ...

Fur die folgenden Schritte setze ich mal voraus, dass der Raspberry Pi 2 B schon per SSH erreichbar ist. Wer noch nicht soweit ist: Die [unbeaufsichtigte Installation von Raspbian (Debian Wheezy) ganz ohne Monitor und Tastatur hatte ich hier beschrieben](https://www.co-operate.net/artikel/archive/2015/02/25/article/typo3-auf-dem-raspberry-pi-2-b-teil-1-installation-ohne-monitor-und-tastatur.html).

Nach dem SSH-Login per
    
    
    SSH pi@ip.adr.es.se

(Standardpasswort: raspberry) aktualisieren wir erstmal die Paketliste und installieren dann acheinander Apache2, PHP 5.4 und MySQL 5.5:
    
    
    sudo apt-get update
    
    
    sudo apt-get install apache2 -y
    
    
    sudo apt-get install php5 libapache2-mod-php5 -y 
    
    
    sudo apt-get install mysql-server php5-mysql -y

Auch die Bildverarbeitungsfunktionen sollen in TYPO3 nutzbar sein. Dafur installieren wir GraphicsMagick und GDlib:
    
    
    sudo apt-get install graphicsmagick -y
    
    
    sudo apt-get install php5-gd -y

## Aufraumarbeiten: 

  * Die php.ini muss angepasst werden, damit TYPO3 spater nicht meckert:  

    
        sudo pico /etc/php5/apache2/php.ini

In dieser Datei folgende Eintrage suchen (in pico geht das mit: Ctrl-W) und andern: upload_max_filesize auf 10M heraufsetzen, post_max_size ebenfalls auf 10M, und die max_execution_time auf 240.
  * In Apache wird jetzt mod_rewrite aktiviert:  

    
        sudo a2enmod rewrite 

Es sind noch ein paar Anpassungen in der Apache-Konfigurationsdatei motig:  

    
        sudo pico /etc/apache2/sites-available/default

Hier im Abschnitt <Directory /var/www/> mit "/" am Ende die Zeile AllowOverride von None auf All umstellen. Dann durfen alle Webuser mod_rewrite nutzen.
  * Die Änderungen der PHP- und der Apache-Konfigurationen jetzt noch bekannt machen:   

    
        sudo /etc/init.d/apache2 restart

  * Das Root-Verzeichnis des Webservers ist /var/www/. Es gehort root, und das mochte ich nicht, das soll www-data gehoren (Nutzer und Gruppe sind im Zuge der Webserverinstallation bereits angelegt worden). Also das Verzeichnis /etc/www/ mit allem, was bislang darin ist (-R) dem Nutzer und der Gruppe www-data zuweisen:  

    
        sudo chown -R www-data:www-data /var/www

## FTP-Server installieren ...

Auch wenn wir TYPO3 per Shell installieren (das geht viel, viel schneller) soll fur die tagliche Arbeit doch ein Zugriff per FTP vorhanden sein. Dafur gibt's ProFTPD:
    
    
    sudo apt-get install proftpd-basic

Die FTP-Nutzer sollen sich nicht per Shell einloggen durfen. Diese "virtuellen" Nutzer werden in eine eigene Datei ausgelagert. Dazu erst einmal die /etc/proftpd/proftpd.conf anpassen und folgende Zeilen einfugen (bzw. Kommentare entfernen):
    
    
    DefaultRoot ~
    
    
    AuthOrder mod_auth_file.c mod_auth_unix.c
    
    
    AuthPam off
    
    
    RequireValidShell off
    
    
    AuthUserFile /etc/proftpd/ftpd.passwd

Da die FTP-Nutzer im Ordner /var/www/ und nur dort arbeiten durfen, und da die dortigen Dateien www-data gehoren (sollten), mussen die FTP-Nutzer dieselbe User-ID bekommen wie www-data, damit keine Rechteprobleme auftauchen.
    
    
    id www-data

Normalerweise hat www-data die User-ID 33. Aber um sicher zu gehen testen wir das nochmal mit obigem Kommando. Danach den FTP-User mit den gewunschten Daten anlegen und zuletzt ProFTPD neu starten:
    
    
    sudo ftpasswd --passwd --name USERNAME --uid 33 --home /var/www --shell /bin/false
    
    
    /etc/init.d/proftpd restart

Damit kann sich USERNAME am FTP-Server anmelden.

## TYPO3 installieren 

Nach all der Vorarbeit konnen wir auf dem Raspberry Pi endlich TYPO3 installieren. Allerdings nicht per FTP, sondern uber die Shell. Die TYPO3-Sourcen lege ich hier mal ins DocumentRoot. Sie konnen aber auch anderswo in Sicherheit gebracht werden. Lediglich daran denken, den Pfad der Links entsprechend anzupassen:
    
    
    cd /var/www/ 
    
    
    sudo wget get.typo3.org/6.2 -O typo3_src.tgz
    
    
    sudo tar -zxvf typo3_src.tgz

Ich habe mir angewohnt, den TYPO3-Core in einem Verzeichnis ohne Nummer des Patchlevels abzulegen. Bei Updates muss dann nur dieses Verzeichnis aktualisiert werden, die symbolischen Links im Userverzeichniss werden nicht mehr angetastet:
    
    
    sudo mv typo3_src-6.2.xx typo3_src-6.2

Jetzt geht's im Userverzeichnis weiter, im Beispiel nennen wir es typo3.de:
    
    
    sudo mkdir /var/www/typo3.de
    
    
    cd /var/www/typo3.de
    
    
    sudo ln -s ../typo3_src-6.2 typo3_src
    
    
    sudo ln -s typo3_src/typo3 typo3
    
    
    sudo ln -s typo3_src/index.php index.php
    
    
    sudo touch FIRST_INSTALL

Damit ist fast alles getan. Nur gehoren die frisch angelegten Dateien im Ordner /var/www jetzt allesamt root. Das mussen wir noch auf Benutzer www-data und Gruppe www-data andern, damit PHP und die FTP-User die neuen Dateien und Ordner kunftig bearbeiten durfen:
    
    
    sudo chown -R www-data:www-data /var/www

## Weiter im Webbrowser ...

Das war schon alles! Unter

wartet jetzt eine TYPO3-Installation auf uns!
