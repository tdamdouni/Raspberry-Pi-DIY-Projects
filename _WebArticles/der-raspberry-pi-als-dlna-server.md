# Der Raspberry Pi als DLNA-Server

_Captured: 2017-05-06 at 16:40 from [kofler.info](https://kofler.info/der-raspberry-pi-als-dlna-server/)_

DLNA steht fur _Digital Living Network Alliance_ ([Wikipedia](https://de.wikipedia.org/wiki/Digital_Living_Network_Alliance)). Die in dieser Gruppe vereinten Hersteller von Unterhaltungselektronik haben sich auf diverse Standards geeinigt. So konnen DLNA-konforme Gerate beispielsweise unkompliziert im lokalen Netzwerk verfugbare Mediendateien (Bilder, Musik, Videos) anzeigen oder abspielen. Dieser Beitrag zeigt, wie Sie mit minimalem Aufwand aus einem Linux-Rechner einen DLNA-tauglichen _Digital Media Server_ (DMS) machen.

Ausgangspunkt fur die Anleitung ist ein Raspberry Pi mit installiertem Raspbian Jessie und einer Verbindung in das lokale Netzwerk. Ich habe meine Tests mit einem Pi Zero durchgefuhrt, der uber einen USB-WLAN-Adapter mit meinem WLAN zuhause verbunden ist. Die Medien-Dateien -- in meinem Fall ausschließlich Audio-Dateien -- befinden sich direkt auf der SD-Karte.

### ReadyMedia/MiniDLNA

Der vermutlich am einfachsten zu konfigurierende DLNA-Server fur Linux heißt [ReadyMedia](http://sourceforge.net/projects/minidlna/) (ehemals MiniDLNA). Unter Raspbian installieren Sie das Programm einfach mit
    
    
    apt-get install minidlna
    

Die Konfiguration erfolgt durch die Datei `/etc/minidlna.conf`. Mit der Ausnahme weniger Einstellungen konnen Sie alle Voreinstellungen belassen. Das folgende Listing fasst nur die Zeilen zusammen, die Sie ublicherweise hinzufugen bzw. andern mussen:
    
    
    # Datei /etc/minidlna.conf
    ...
    # Audio-, Video- und Picture-Verzeichnisse angeben
    media_dir=A,/mymedia/musik
    media_dir=A,/mymedia/hoerbuecher
    media_dir=V,/mymedia/filme
    media_dir=P,/mymedia/fotos1
    media_dir=P,/mymedia/fotos2
    
    # Name, der auf DLNA-Geräten angezeigt wird
    friendly_name=MyMediaServer
    
    # Änderungen in der Medienbibliothek selbstständig erkennen
    # mit no muss nach dem Hinzufügen neuer Mediendateien
    #   service minidlna restart
    # ausgeführt werden
    inotify=yes
    

Damit die Änderungen wirksam werden, starten Sie den DLNA-Server neu:
    
    
    service minidlna restart
    

### Cache-Verzeichnis

Falls der DLNA-Server auf einem Read-Only-System laufen soll (dann naturlich mit `inotify=no`), ist noch ein Problem zu losen: ReadyMedia alias MiniDLNA legt standardmaßig im Verzeichnis `/var/cache/minidlna` eine Datenbank fur alle Mediendateien sowie fur die Cover-Bilder von MP3-Tracks an. Dazu muss das Programm in diesem Programm naturlich Schreibrechte haben.

Es gibt dafur zwei Losungsansatze:

  * Sie sehen ein Temporares Dateisystem fur `/var/cache/minidlna` vor.
  * Sie platzieren das Cache-Verzeichnis im Dateisystem fur die Mediendateien und lassen den DLNA-Server nach jedem Update der Mediendateien zumindest einige Minute im rw-Modus laufen, damit die Datenbank aktualisert wird.

Im Folgenden stelle ich beide Varianten etwas naher vor.

#### Cache im temporaren Dateisystem
    
    
    service minidlna stop
    mount -o remount,rw /
    rm -rf /var/cache/minidlna/*
    

Jetzt fugen Sie in `/etc/fstab` die folgende Zeile hinzu:
    
    
    # Datei /etc/fstab
    ...
    tmpfs   /var/cache/minidlna     tmpfs   nodev,nosuid    0       0
    

Zuletzt starten Sie Ihren Minirechner mit `reboot` neu. Nach dem Neustart dauert es nun je nach Große der Mediathek etliche Minuten, bis `minidlna` uber eine komplette Datenbank aller Titel verfugt. Der Platzbedarf fur das temporare Dateisystem im RAM ist uberschaubar. Bei meinen rund 30 GByte Musikdateien beansprucht das Cache-Dateisystem ca. 25 MByte.

#### Cache-Verzeichnis im Medien-Dateisystem

Im Folgenden gehe ich davon aus, das im Verzeichnis `/mymedia` ein Dateisystem fur die Mediendateien eingebunden ist. In diesem Dateisystem soll nun auch das Cache-Verzeichnis eingerichtet werden. (Alle weiteren Kommandos sind mit `sudo` auszufuhren.)
    
    
    service minidlna stop
    mount -o remount,rw /
    mount -o remount,rw /mymedia
    rm -rf /var/cache/minidlna
    mkdir /mymedia/cache
    chown minidlna.minidlna /mymedia/cache
    ln -s /mymedia/cache /var/cache/minidlna
    service minidlna start
    

Jetzt beobachten Sie mit `top` den Prozess `minidlna`. Er wird fur einige Minuten mit hoher CPU-Belastung das gesamte Medienarchiv durchforsten und die Datenbank einrichten. (Bei mir dauert das fur 30 GByte Musikdateien rund vier Minuten -- also etwas mehr als eine Minute pro 10 GByte Mediendateien.) Wenn `minidlna` von den vorderen Rangen der `top`-Liste verschwindet, ist die Medien-Datenbank aktuell. Jetzt konnen Sie das System neu im Read-Only-Modus starten.

Wenn Sie in Zukunft Mediendateien hinzufugen, fuhren Sie neuerlich `mount -o remount,rw /mymedia` aus und geben `minidlna` dann einige Minuten Zeit, um seine Datenbank zu aktualisieren. Anschließend konnen Sie das System wieder in den Read-Only-Modus rebooten.

Der Vorteil dieser Vorgehensweise besteht darin, dass `minidlna` nach einem Neustart sofort Zugriff auf die fertige Mediendatenbank hat.

### Praxis

Bei mir zuhause lauft MiniDLNA auf einem Pi Zero mit einer [128-GByte-SD-Karte](https://kofler.info/raspbian-auf-eine-128-gbyte-sd-karte-installieren/) und in [Read-Only-Konfiguration](https://kofler.info/raspbian-lite-fuer-den-read-only-betrieb/). Die Medien-Dateien befinden sich in einem eigenen Dateisystem (auch Read-Only, außer wenn ich per SSH neue Mediendateien hinzufuge). Das Cache-Verzeichnis habe ich ebendort eingerichtet (gemaß der zweiten Cache-Konfigurationsvariante von oben).

Den Pi-Zero habe ich an die Ruckseite des Netzwerk-Lautsprecher [Sony SRS-X77](http://www.amazon.de/gp/product/B00VIC2W4Q/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00VIC2W4Q&linkCode=as2&tag=michaelkofler) geklebt. Der Minicomputer bezieht seine Stromversorgung von der USB-Buchse des Gerats, die eigentlich zum Laden von Smartphones gedacht ist. Sehr praktisch :-)

![Der Pi Zero ist auf die Rückwand eines Sony-Netzwerklautsprechers geklebt](https://kofler.info/wp-content/uploads/pi-zero-dlna-600x298.jpg)

> _Der Pi Zero ist auf die Ruckwand eines Sony-Netzwerklautsprechers geklebt_

Jedes Smartphone/Tablet im Haushalt, auf das/dem eine DLNA-Player-App installiert ist, kann nun Musik aus der DLNA-Bibliothek auswahlen und wahlweise direkt auf dem Smartphone/Tablet oder aber via Bluetooth/AirPlay/Google Cast auf dem Funklautsprecher abspielen.

Jetzt stort nur noch die hohe Stand-by-Leistungsaufnahme des Gerats (ca. 5 Watt). Da es -- wie bei modernen Geraten leider ublich -- keinen richtigen Ein/Aus-Schalter gibt, werde ich das Netzkabel des Gerats mit einem Schalter versehen. Damit wird dann aber auch die Stromversorgung des Raspberry Pi im laufenden Betrieb gekappt. Dank der Read-Only-Konfiguration sind dabei glucklicherweise keine Datenverluste zu erwarten.

### Quellen
