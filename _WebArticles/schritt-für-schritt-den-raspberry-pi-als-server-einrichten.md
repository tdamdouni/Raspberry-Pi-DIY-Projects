# Schritt für Schritt den Raspberry Pi als Server einrichten

_Captured: 2017-05-06 at 16:36 from [www.elektronik-kompendium.de](https://www.elektronik-kompendium.de/sites/raspberry-pi/2007031.htm)_

Wenn man den Raspberry Pi als Server einrichten will, um ihn anschließend im Headless-Betrieb einzusetzen, dann sind je nach individuellen Vorlieben einige Konfigurationsschritte vorzunehmen.  
Die folgende Schritt-fur-Schritt-Anleitung ist ein Vorschlag, um den Raspberry Pi als Server einzurichten.

Die Reihenfolge der einzelnen Schritte folgt einer inneren Logik. So soll ein mehrmaliges Rebooten vermieden werden und nur dann erfolgen, wenn es nicht anders geht. Selbstverstandlich kann man die Reihenfolge auch andern oder einzelne Schritte weglassen, wenn man sie nicht braucht.

Die Anleitung sieht vor, dass man die Konfiguration per SSH vornehmen kann. Das setzt aber einen aktiven SSH-Server auf dem Raspberry Pi voraus. Selbstverstandlich kann die Konfiguration auch lokal erfolgen.

### Aufgabe

  1. Wahl der Distribution
  2. Installation
  3. Inbetriebnahme
  4. Grundkonfiguration vornehmen
  5. Standard-Passwort andern
  6. Boot-Optionen andern
  7. Hostname andern
  8. Neue SSH-Schlussel erstellen
  9. Dateisystem erweitern
  10. Pakete aktualisieren
  11. Software installieren
  12. Benutzer einrichten
  13. Grundkonfiguration des SSH-Servers
  14. Zusatzliche Sicherheitsmaßnahmen (optional)
  15. Netzwerk-Konfiguration  

  16. Konfiguration abschließen

### Wahl der Distribution

Bei einem Server wird man sich in der Regel fur ein Minimal-Image entscheiden, weil jede vorinstallierte Software uberflussig ist, unnotigerweise Speicherplatz verbraucht und auch Performance- und Sicherheitsrisiken beinhaltet.

### Installation

  * [Betriebssystem fur den Raspberry Pi auf eine SD-Speicherkarte installieren](https://www.elektronik-kompendium.de/sites/raspberry-pi/1905261.htm)

### Inbetriebnahme

  1. Einstecken der SD-Speicherkarte
  2. Anschließen von Bildschirm und Tastatur
  3. Anschließen des Netzwerk-Kabels
  4. Anschließen der Energieversorgung
  * [Erste Inbetriebnahme eines Raspberry Pi](https://www.elektronik-kompendium.de/sites/raspberry-pi/1906261.htm)

### Grundkonfiguration vornehmen

Die ersten Schritte bestehen darin, die Landes-, Sprach- und Zeiteinstellungen vorzunehmen.

Systemsprache, Standort und Zeichensatz einstellen:
    
    
    sudo dpkg-reconfigure locales

Zeitzone einstellen:
    
    
    sudo dpkg-reconfigure tzdata

Tastatur-Layout einstellen (nicht uber SSH):
    
    
    sudo dpkg-reconfigure keyboard-configuration

Oder wenn man es per SSH einstellen will:
    
    
    sudo nano /etc/default/keyboard

Hier andert man den folgenden Wert:
    
    
    XKBLAYOUT="de"

Hinweis: Je nach Distribution gibt es unterschiedliche Wege, diese Grundeinstellungen vorzunehmen. So gibt es unter Raspbian das Tool "raspi-config", mit dem sich die oben genannten Einstellungen sehr bequem durchfuhren lassen.
    
    
    sudo raspi-config

### Standard-Passwort andern

Aus Sicherheitsgrunden muss das Standard-Passwort moglichst fruhzeitig nach der ersten Inbetriebnahme geandert werden. In der Regel sofort. In diesem Fall erst nach den Sprach-Einstellungen, weil man dann eine deutschsprachige Benutzerfuhrung hat, was die Handhabung vereinfacht.
    
    
    passwd

Das Passwort des Benutzers "pi" kann man ebenfalls uber "raspi-config" andern.

Das neue Passwort muss "blind" eingegeben und bestatigt werden.

### Boot-Optionen

Unter Raspbian Wheezy wird standardmaßig die Konsole gestartet. Anschließen muss man sich einloggen. Unter Raspbian Jessie wird standardmaßig die grafische Benutzeroberflache gestartet, was wir nicht unbedingt wollen. Diese Boot-Optionen stellt man am besten mit dem Tool "raspi-config" ein.
    
    
    sudo raspi-config

### Hostname/Computername andern

Standardmaßig hat ein frisches Image einer Linux-Distribution einen vorgegebenen Hostnamen. Bei einem Server-Betrieb mochte man vielleicht einen individuellen Hostnamen vergeben.
    
    
    sudo hostname -b {NEUERNAME}

Oder uber "raspi-config".

Danach kurz prufen:
    
    
    hostname

Unter Umstanden ist es damit allerdings nicht getan. Man sollte noch einen Blick in die hosts-Datei werfen.
    
    
    cat /etc/hosts

Wenn dort noch der alte Hostname drin steht, dann muss man den in dieser Datei auch noch andern.
    
    
    sudo nano /etc/hosts

Danach speichern und schließen: Strg + O, Return, Strg + X.

### Neue SSH-Schlussel erstellen

Spatestens, wenn man den Hostnamen geandert hat, muss man neue SSH-Schlussel erstellen. Zuerst loschen wir alle Dateien, in denen sich die Schlussel befinden. Davon gibt es mehrere. Zum Loschen reicht trotzdem ein Kommando.
    
    
    sudo rm /etc/ssh/ssh_host_*

Anschließend fuhren wir eine Rekonfiguration des SSH-Servers durch:
    
    
    sudo dpkg-reconfigure openssh-server

Die Erstellung der Schlussel-Dateien erfolgt automatisch. Normalerweise sollte auch der SSH-Server automatisch neu gestartet werden. Wenn nicht, dann muss man das handisch machen.
    
    
    sudo service ssh restart

Ein Neustart des Systems ist nicht erforderlich. Allerdings muss man beachten, dass nach einem erneuten Login per SSH die Identitat des Systems neu bestatigt werden muss.

### Dateisystem erweitern

Wenn eine Linux-Distribution frisch auf eine SD-Card geschrieben wurde, dann wird nicht die gesamte Speicherkarte belegt, sondern nur ein Teil davon. Wenn man das Dateisystem auf die ganze Speicherkarte ausdehnen mochte, dann empfiehlt sich per "raspi-config" der Menupunkt "Expand Filesystem".   
Anschließend ist ein Reboot zwingend erforderlich.
    
    
    sudo reboot

Hinweis: Nach einem "Expand Filesystem" muss ein Reboot zwingend erfolgen. Wenn man hier ohne Reboot einfach weitermacht, kann man sich das System zerschießen.

### Pakete aktualisieren

Wenn man ein System neu aufsetzt, dann ist es empfehlenswert die Paketquellen zu uberprufen, aus denen spater uber die Paketverwaltung neue und aktualisierte Pakete bezogen werden. Je nach dem, welche Anforderungen man stellt, sind Anpassungen notig oder auch nicht.

Wenn man eine Standard-Distribution, wie Raspbian verwendet, dann ist das Prufen der Paketquellen nicht zwingend notwendig. Die sind meistens sinnvoll eingestellt. Anders sieht es aus, wenn man ein Image aus einer fremden Quelle hat. Hier sollte man einen Blick drauf werfen.

  * [ Paketquellen prufen](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002201.htm)

Anschließend fuhren wir die Aktualisierung der Paketlisten aus den Paketquellen durch.
    
    
    sudo apt-get update

Und danach laden und installieren wir aktualisierte Pakete.
    
    
    sudo apt-get upgrade

Je nach Aktualitat des Image oder der Distribution kann das auch mal etwas langer dauern.

### Software installieren

Je nach Distribution oder Image kann es nicht schaden ein paar Pakete nachzuinstallieren. Es handelt sich hierbei um einige Tools, die spater helfen das System besser zu bedienen.

Die Installation erfolgt einzeln. Das heißt, bedarfsweise konnen einzelne Pakete weggelassen oder auch spater installiert werden.
    
    
    apt-get install sudo

### Benutzer einrichten

Die folgenden Schritte gelten nur dann, wenn noch kein Benutzer eingerichtet sind. Bei Raspbian ist der Benutzer "pi" schon eingerichtet und deshalb muss kein weiterer Benutzer eingerichtet werden.

Sinnvoll ist die Einrichtung eines weiteren Benutzers zur Administration nur dann, wenn vorher das Paket "sudo" installiert wurde.

Benutzer mit Home-Verzeichnis einrichten:
    
    
    useradd -m {USERNAME}

Passwort festlegen:
    
    
    passwd {USERNAME}

Danach muss das Passwort "blind" eingegeben und anschließend bestatigt werden.

Standard-Bash zuweisen:
    
    
    usermod -s /bin/bash {USERNAME}

Hauptgruppe zuweisen:
    
    
    usermod -g users {USERNAME}

Benutzergruppen zuweisen:
    
    
    gpasswd -a {USERNAME} sudo
    gpasswd -a {USERNAME} ssh

Gruppenzugehorigkeit eines Benutzers prufen:
    
    
    id {USERNAME}

Neuen Benutzer testen:
    
    
    su - {USERNAME}

Benutzer beenden:
    
    
    exit

Berechtigung fur die Benutzergruppe "sudo" setzen:
    
    
    visudo

Hier prufen wir, ob folgende Zeile eingetragen ist. Wenn nicht, dann muss diese Zeile nachgetragen werden.
    
    
    $sudo ALL=(ALL:ALL) ALL

Wenn man sich einen Benutzer fur die Systemadministration eingerichtet hat, ist eine gute Gelegenheit, diesen durch Anmelden zu testen. Dazu meldet man sich als "root" ab und als neuen Benutzer an.

### Grundkonfiguration des SSH-Servers

Im folgenden Schritt geht es darum, den SSH-Server sicherer zu konfigurieren.
    
    
    sudo nano /etc/ssh/sshd_config

Die folgenden Zeilen mussen einzeln betrachtet werden. Teilweise sind die Parameter schon richtig voreingestellt. Andere mussen geandert oder nachtraglich eingefugt werden.
    
    
    Protocol 2
    
    
    AllowGroups ssh
    
    
    PermitEmptyPasswords no
    
    
    PermitRootLogin no

Nach den Änderungen muss die Datei gespeichert und geschlossen werden. Anschließend ist ein Neustart des SSH-Servers notwendig, damit die Änderungen ubernommen werden.
    
    
    sudo service ssh restart

Eine bestehende SSH-Verbindung wird dabei nicht unterbrochen.

### Zusatzliche Sicherheitsmaßnahmen (optional)

Wenn man einen Benutzer fur die Systemadministration eingerichtet hat und der berechtigt ist, "sudo" zu benutzen und eine Verbindung per SSH herstellen kann, dann kann man die Sicherheit des Gesamtsystems zusatzlich verbessern, in dem man das Passwort von "root" loscht.
    
    
    sudo passwd -d root

### Netzwerk-Konfiguration

Bevor die Konfiguration des Gesamtsystems zu Ende gebracht wird, wird man sich noch um die Netzwerk-Konfiguration kummern. Die ist allerdings individuell festzulegen. So wird man in der Regel fur den Server-Betrieb eine statische IPv4-Adresse einrichten. Im einen oder anderen Fall IPv6 aktivieren, was bei einer Neueinrichtung zu empfehlen ist. Und gegebenenfalls wird man weitere Netzwerk-Dienste, wie zum Beispiel Avahi installieren.

### Konfiguration abschließen

Der letzte Neustart. Das ist notwendig, damit man weiß, dass bei einem Neustart auch wirklich alles so funktioniert, wie man es mochte.
    
    
    sudo reboot

### Übersicht: Raspberry Pi als Server

### Übersicht: Fernwartung und Remote-Service

### Weitere verwandte Themen:

### Produktempfehlungen
