# Verbindung zur grafischen Benutzeroberfläche per SSH aufbauen

_Captured: 2017-05-06 at 15:20 from [www.elektronik-kompendium.de](https://www.elektronik-kompendium.de/sites/raspberry-pi/2011111.htm)_

Ein SSH-Server kann nicht nur die Kommandozeile zur Verfugung stellen, sondern auch eine grafische Benutzeroberflache, die allerdings nicht zwangslaufig wie die auf dem entfernten System aussehen muss.  
Eine Display-Umleitung bzw. X-Forwarding kann ein SSH-Server durchfuhren. Allerdings bekommt man bei dieser Losung nicht den aktuellen, sondern einen eigenen Desktop angezeigt.

### Aufgabe

  1. Display-Umleitung einrichten.
  2. Panel installieren.
  3. Verbinden Sie sich per SSH mit der grafischen Benutzeroberflache.

### Losung: Display-Umleitung einrichten

Die Display-Umleitung nennt sich X-Forwarding. Damit das funktioniert muss der betreffende SSH-Server entsprechend konfiguriert sein. Dazu offnen wir die Konfigurationsdatei:
    
    
    sudo nano /etc/ssh/sshd_config
    

Dort tragen wir folgende Zeile ein, die standardmaßig vorhanden sein sollte.
    
    
    X11Forwarding yes

Anschließend speichern und schließen: Strg + O, Return, Strg + X.

Der SSH-Server muss neu gestartet werden (nur wenn man die Datei geandert hat).
    
    
    sudo service ssh restart

### Losung: Panel installieren

Die Display-Umleitung bringt nichts, wenn man kein Panel (Startmenu, Programm-Leiste, ...) hat, uber das man den Desktop steuern kann. Ein Panel ist eine Kontrollleiste, die sich in der Regel vollig frei auf dem Desktop platzieren und mit vielen Applets und Plugins erweitern lasst. Zum Beispiel Programmstarter oder Akku-, Netzwerk- oder Festplatten-Monitor.  
Deshalb installieren wir uns erst ein Panel.
    
    
    sudo apt-get install lxpanel

Weitere Panels sind tint2, fspanel, xfce4-panel, visibility, kicker, barpanel und noch einige andere mehr.

### Losung: Verbindung per SSH aufbauen

Danach kann man direkt im SSH-Client folgendes Kommando eingeben.
    
    
    ssh -X pi@192.168.1.2 lxpanel

Die entscheidenden Parameter sind "-X" (großes X) fur die Display-Umleitung und "lxpanel" fur das Panel.  
Die IP-Adresse ist entsprechend des eigenen Raspberry Pi anzupassen.

### Alternative: Remote-Desktop per RDP

In der Windows-Welt ist VNC weniger gelaufig. Hier spricht man von Remote-Desktop-Unterstutzung per RDP. Sofern man mit Windows-Clients arbeitet, ist die Einrichtung eines RDP-Servers auf dem Raspberry Pi eine denkbare Alternative zu VNC.

  * [XRDP-Remote-Desktop auf dem Raspberry Pi einrichten](https://www.elektronik-kompendium.de/sites/raspberry-pi/2109031.htm)

### Weitere verwandte Themen:

### Produktempfehlungen
