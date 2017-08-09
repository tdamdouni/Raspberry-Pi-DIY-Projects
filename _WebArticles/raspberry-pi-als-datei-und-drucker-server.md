# Raspberry Pi als Datei- und Drucker-Server

_Captured: 2017-05-06 at 16:38 from [www.raspberry-pi-geek.de](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server)_

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-datei-und-drucker-server/aa_po-24794-binkski_123rf.jpg3/2838-1-ger-DE/AA_PO-24794-binkski_123RF.jpg_large.jpg)

> _(C) binkski, 123RF_

## Zentrallager

Dank seines geringen Stromverbrauchs eignet sich der RasPi optimal fur den Einsatz als rund um die Uhr laufender Home-Server. Dabei lasst er sich innerhalb kurzester Zeit sehr flexibel an die eigenen Wunsche anpassen.

Selbst Privathaushalte sind heutzutage vernetzt: Über das lokale Wireless-Netz tauschen nicht nur die Desktop-PCs von Familien- oder WG-Mitgliedern untereinander Daten aus, sondern auch Tablets und Smartphones interagieren daruber. Da mutet es eher anachronistisch an, wenn man einen gemeinsamen Drucker nur nutzen kann, indem man einen USB-Stick mit den benotigten Dokumenten fullt und zum Drucker bringt. Selbst in Privatwohnungen haben sich deswegen inzwischen Print-Server durchgesetzt.

Doch mit welcher Losung setzt man dies alles schnell, kostengunstig und im Bedarfsfall trotzdem flexibel auf? Dafur stellt der Raspberry Pi eine gute Losung dar: Seine Anschaffungskosten kann man vernachlassigen, die Stromaufnahme bleibt gering. Die gewunschten Datei- und Druckdienste konfigurieren Sie mit wenig Zeitaufwand und einer handvoll Konsolenkommandos.

#### Grundlage

Laden Sie die neueste Version von Raspbian von <http://www.raspberrypi.org/downloads> herunter und flashen diese auf eine SD-Karte. Fur die allerersten Konfigurationsschritte sollten Sie der Einfachheit halber den RasPi an einen Monitor anschließen. Beim ersten Booten von der frisch beschriebenen SD-Karte landen Sie in einem Dialog, der ein paar grundlegende Einstellungen anbietet. Sie konnen ihn zu einem spateren Zeitpunkt jederzeit erneut uber den Konsolenbefehl `sudo raspi-config` aufrufen.

Bei jeder Raspbian-Neukonfiguration empfiehlt es sich, das Root-Passwort uber den Menupunkt change_pass zu andern sowie den Speicherplatz der SD-Karte mittels des Punkts expand_rootfs komplett auszunutzen. Da Sie einen Server aufsetzen, ist jedoch auch der Punkt Boot Behaviour wichtig: Setzen Sie hier Boot straight to desktop nicht auf No setzt, verbraten Sie unnotig Ressourcen. Bei der Auswahl ssh rat es sich daruber hinaus an, Enable SSH-Server auszuwahlen, damit Sie den RasPi von nun an "headless" nutzen konnen, also ohne Monitor.

Damit Sie wissen, unter welcher IP-Adresse der RasPi im LAN zu erreichen ist, geben Sie noch `ifconfig` ein und notieren die Angabe hinter inet addr:. Fahren Sie nun das Gerat herunter und platzieren Sie es an seinem kunftigen Platz - beispielsweise neben dem Router, an den es dann mittels Netzwerkkabel angeschlossen wird. Ansonsten benotigt der RasPi nur noch ein Stromkabel zur Spannungsversorgung. Nach dem Einschalten des Raspberrys setzen Sie sich an einen Client im Netz und melden sich von dort aus auf dem Minicomputer ein:
    
    
    $ ssh pi@192.168.2.129)

Die IP-Adresse in obigen Beispiel ersetzen Sie durch jene, die Sie eben als Ausgabe von `ifconfig` notiert haben. Falls Sie das Standard-Passwort des Benutzers pi geandert haben sollten, verwenden Sie dieses statt der Raspian-Vorgabe `raspberry` bei der Anmeldung.

Denken Sie auch daran, im Router des LANs einzustellen, dass dessen DHCP-Server dem RasPi von nun an immer dieselbe IP-Adresse zuteilen soll. Im den folgenden Beispielen gehen wir davon aus, dass die IP 192.168.2.129 lautet. Ersetzen Sie diese immer jeweils durch die in Ihrem LAN gultige.

#### Externer Speicher

Theoretisch konnten Sie fur den File-Server ausschließlich den Platz auf der SD-Karte verwenden, von der auch das System bootet. Der durfte allerdings in den meisten Fallen nicht ausreichen, insbesondere, wenn Sie auch Videos, Musik oder Backups ablegen mochten. Dieses Problem losen Sie mit einem permanent angeschlossenen USB-Stick beziehungsweise einer externen USB-Festplatte.

Dazu formatieren Sie das externe Speichermedium mit einem von Linux unterstutztem Dateisystem wie Ext4. Nach dem Anstopseln des Massenspeichers an den USB-Port des Raspberry Pi rufen Sie auf der Konsole `dmesg` auf. Dies liefert den aktuellen Message Buffer des Kernels zuruck. Gegen Ende der Ausgabe finden Sie eine Zeichenkette des Strickmusters `sda: sda1` (siehe [Abbildung 1](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server)). Sie zeigt an, unter welchem Kurzel (in unserem Beispiel `sda1`) das Betriebssystem die Partition auf dem USB-Stick anspricht.

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-datei-und-drucker-server/abbildung-13/2841-1-ger-DE/Abbildung-1_large.png)

> _Abbildung 1: Das Kommando dmesg hilft beim Finden des USB-Sticks._

Rufen Sie nun `sudo mkdir /mnt/ExternalStorage` auf sowie anschließend `sudo nano /etc/fstab` auf. In der Datei `fstab` tragen Sie die nun die zusatzliche Zeile aus [Listing 1](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server) ein, wobei Sie `sda1` durch die Angabe ersetzen ist, die Sie vorhin nach der Eingabe von `dmesg` erhielten.

Auf die Weise bindet Raspbian den externen Massenspeicher bei jedem Systemstart automatisch im Dateibaum unter `/mnt/ExternalStorage/`, sodass Sie bei den folgenden Konfigurationsschritten von der Existenz dieses Verzeichnisses ausgehen konnen. Damit spater alle Dienste und Nutzer diesen Speicherbereich problemlos beschreiben und lesen konnen, fuhren Sie noch folgenden Befehl aus:
    
    
    $ sudo chmod -R ugoa+rwx /mnt/ExternalStorage

Falls Sie statt eines USB-Sticks eine externe Festplatte verwenden, sollten Sie dafur sorgen, dass diese nicht zu viel Strom verbraucht - der RasPi selbst benotigt nur sehr wenig Energie. Hierbei hilft das Programm Hdparm. Tragen Sie hierzu in die Datei `/etc/hdparm.conf` die Zeile `sudo hdparm -S 12 /dev/sda` ein (und ersetzen Sie dabei gegebenenfalls `/dev/sda` durch den passenden Geratenamen). Dieser bewirkt, dass nach 60 Sekunden ohne Zugriffe die Festplatte automatisch einen stromsparenden Spindown vornimmt. Die Zahl hinter dem Parameter `-S` ergibt, mit funf multipliziert, die Anzahl Sekunden, die vergehen mussen, um dies auszulosen (in diesem Fall also 12 mal 5 gleich 60).

Nun gilt es noch Dienste fur alle Übertragungsprotokolle zu installieren, welche die Nutzern im LAN verwenden. Handelt es sich um ein gemischtes Netzwerk aus Windows-, Linux- und Mac-OS-Rechnern handelt, bietet sich aus Kompatibilitatsgrunden Samba an. Dazu installieren Sie zunachst einmal den Dienst und editieren anschließend dessen Konfigurationsdatei ([Listing 2](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server)).

Listing 2
    
    
    $ sudo apt-get install samba samba-common-bin
    ...
    $ sudo nano /etc/samba/smb.conf

Verwenden die Rechner, die auf den RasPi zugreifen sollen, einen bestimmten Workgroup-Namen, passen Sie die Zeile `workgroup = WORKGROUP` entsprechend an. Fur den Fall, dass Sie nicht generell jedem im LAN Zugriff auf den File-Server gestatten mochten, lasst sich die Authentifizierung ganz einfach aktivieren. Dazu suchen Sie die Zeile mit der Angabe `security = user` und loschen das Doppelkreuz, mit der diese auskommentiert wurde. Scrollen Sie nun an das Ende der Datei und fugen Sie die Zeilen aus [Listing 3](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server) an.

Listing 3
    
    
    [public]
     comment = Public
     path = /mnt/ExternalStorage/
     valid users = @users
     force group = users
     create mask = 0660
     directory mask = 0771
     read only = no

Nun speichern Sie die Datei und starten anschließend den Dienst mit `sudo /etc/init.d/samba restart` neu, damit die Änderungen wirksam werden. Ein Benutzerkonto legen Sie nun zunachst einmal fur die Shell an. Falls sich also beispielsweise die anderen Rechner mittels des Benutzernamens fileserver authentifizieren sollen, geben Sie `sudo useradd fileserver -m -G users` an und andern das Shell-Passwort via `sudo passwd fileserver` an.

Mittels `sudo smbpasswd -a fileserver` teilen Sie dann dem Benutzer noch ein Samba-Passwort zu, mit dem nun der eigentliche Zugriff auf den Dienst erfolgt. Andere Rechner konnen jetzt in ihren jeweiligen Dateimanagern das LAN nach Netzlaufwerken durchsuchen und den Speicher des RasPi einbinden.

Alternativ lasst sich fur Dateiubertragungen auch SFTP nutzen. Da Sie den SSH-Server bereits aktiviert haben, erfordert dies keine zusatzlichen Konfigurationsschritte: Die aktuelle Raspian-Version erlaubt bereits in der Grundkonfiguration SFTP-Übertragungen.

  


#### Backup

Um den RasPi-Server auch fur Backups der Arbeitsdaten zu nutzen bietet sich Rsync an: Dieses Programm synchronisiert Daten zwischen zwei Netzwerkstandorten derart, dass es nur die Dateien mit einem neueren Zeitstempel ubertragt - also diejenigen, die sich seit dem letzten Sync-Vorgang geandert haben. Da es sich um ein Shell-Kommando handelt, konnen Sie es bei Bedarf in einen Cron-Job einbinden. Installieren Sie Rsync auf dem RasPi und rufen Sie im Editor die Konfigurationsdatei fur den Rsync-Daemon auf ([Listing 4](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server/\(offset\)/2)).

Listing 4
    
    
    $ sudo apt-get install rsync
    ...
    $ sudo nano /etc/rsyncd.conf

In der Regel enthalt `rsyncd.conf` noch keinerlei Text. Sie fugen nun die Angaben aus [Listing 5](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server/\(offset\)/2) ein. Diese bewirken, dass jeder aus dem IP-Bereich des heimischen LANs Synchronisationsvorgange auf dem USB-Stick am RasPi vornehmen darf. Haben Sie in Ihrem Router einen anderen IP-Adressbereich als 192.168.2.0 fur das LAN eingestellt, mussen Sie diese Angabe entsprechend anpassen. Folgender Befehl ladt anschließend alle Dateien und Unterverzeichnisse aus `~/workspace/*` auf den RasPi hoch, die seitdem letzten Backup verandert wurden:
    
    
    rsync -avz ~/workspace/* rsync://192.168.2.129/public

Listing 5
    
    
    use chroot = true
    hosts allow = 192.168.2.0/24
    transfer logging = true
    log file = /var/log/rsyncd.log
    log format = %h %o %f %l %b
    [public]
    comment = Public
    path = /mnt/ExternalStorage/
    read only = no
    list = yes
    uid = nobody
    gid = nogroup

Sollen nur bestimmte Anwender Backups vornehmen durfen? Dann erganzen sie die Datei `rsyncd.conf` noch um die Zeilen `auth users=Backup` (nur der User Backup darf Rsync benutzen) und `secrets file=/etc/rsyncd.scrt` (das Passwort fur diesen Benutzer steht in der Datei `/etc/rsyncd.scrt`). Letztere mussen Sie dann nur noch anlegen und dort eine Zeile in der Form `Backup:_Passwort_` eintragen.

#### Printserver

An den zweiten USB-Port des Raspberry Pi schließen Sie nun einen Drucker an, damit alle LAN-Gerate ihre Ausdrucke uber diesen absetzen konnen. Nach der Installation des Common Unix Print Servers Cups ([Listing 6](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server/\(offset\)/2), Zeile 1) geben Sie diesen erst einmal fur das Netzwerk frei (Zeile 2). Durch den Zusatz `\--remote-admin` lasst sich der Print-Server auch vom PC aus via Webbrowser verwalten. Zunachst mussen Sie dazu noch dem Standard-Benutzer pi den Druckerzugriff gestatten (Zeile 3).

Listing 6
    
    
    $ sudo apt-get install cups
    $ sudo cupsctl --share-printers --remote-printers --remote-admin
    $ sudo usermod -a -G lpadmin pi

Anschließend geben Sie im Webbrowser auf einem PC die Adresse des RasPi ein, in unserem Beispiel `https://192.168.2.129:631/admin`. Nun erscheint die Konfigurationsoberflache von Cups ([Abbildung 2](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server/\(offset\)/2)). Hier wahlen Sie Drucker hinzufugen und geben anschließend das entsprechende Druckermodell an. Bei der Authentifizierungsabfrage tragen Sie die Benutzerdaten des Pi-Benutzers ein. Nun erscheint unter Lokale Drucker der via USB an den Raspberry Pi angeschlossene Drucker ([Abbildung 3](http://www.raspberry-pi-geek.de/Magazin/2013/05/Raspberry-Pi-als-Datei-und-Drucker-Server/\(offset\)/2)). Wahlen Sie diesen aus und klicken Sie auf Weiter.

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-datei-und-drucker-server/abbildung-23/2844-1-ger-DE/Abbildung-2_large.png)

> _Abbildung 2: Den Druckerdienst Cups verwalten Sie via Webbrowser auch aus der Ferne._

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/raspberry-pi-als-datei-und-drucker-server/abbildung-33/2847-1-ger-DE/Abbildung-3_large.png)

> _Abbildung 3: Den an den RasPi angeschlossene Drucker finden Sie unter dem Punkt Lokale Drucker._

Im folgenden Konfigurationsschritt geben Sie die URI fur den Drucker an. Diese hangt von dessen Hersteller und Modell ab. Über den auf der Seite angegebenen Hilfe-Link Netzwerk Drucker finden Sie die richtige URI heraus. Nach einem Klick auf Weiter mussen Sie noch einen Namen fur den Drucker vergeben sowie eine Beschreibung fur dessen Standort eintippen. Dann wahlen Sie das Kastchen Diesen Drucker freigeben aus und klicken schließlich auf Weiter. Nun wahlen Sie noch einmal den konkret verwendeten Druckertyp aus, damit auch intern der richtige Treiber Anwendung findet. Ein Mausklick auf Drucker hinzufugen schließt die Konfiguration ab.

Mochten Sie den Drucker auch von einem Windows-Rechner aus benutzen, gilt es die die Samba-Konfiguration entsprechend anzupassen. Dazu offnen Sie erneut die Datei `/etc/samba/smb.conf`, loschen die auskommentierenden Strichpunkte vor den Zeilen `printing = cups` sowie `printcap name = cups` und starten Samba mit `sudo /etc/init.d/samba restart` neu. Auf Windows-Systemen lasst sich der Drucker nun wie ein normaler Netzwerkdrucker hinzufugen.

  


Nun verfugen Sie uber einen eigenen Datei- und Druckserver. Falls Sie irgendeinen Dienst nicht benotigen, sollten Sie diesen abschalten, um Ressourcen zu sparen und potenzielle Angriffstore zu schließen. Umgekehrt konnen Sie bei Bedarf weiter Server-Dienst hinzufugen. Da es sich bei Raspbian um ein vollwertiges Debian-Derivat handelt, stehen Ihnen hier alle Moglichkeiten offen.
