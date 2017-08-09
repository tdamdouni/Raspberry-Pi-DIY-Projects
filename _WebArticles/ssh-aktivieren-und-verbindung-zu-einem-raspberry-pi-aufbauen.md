# SSH aktivieren und Verbindung zu einem Raspberry Pi aufbauen

_Captured: 2017-05-06 at 15:21 from [www.elektronik-kompendium.de](https://www.elektronik-kompendium.de/sites/raspberry-pi/1906281.htm)_

_Mit Raspbian Jessie gepruft._

Um ohne Bildschirm den Raspberry Pi in Betrieb zu nehmen ist es erforderlich aus der Ferne uber das Netzwerk auf den Raspberry Pi zuzugreifen. Deshalb ist es erforderlich, dass der Raspberry Pi mit einem RJ45-Patchkabel mit dem lokalen Netzwerk verbunden ist.

Hinweis: Seit dem Raspbian-Jessie-Image vom 2016-11-25 ist SSH aus Sicherheitsgrunden standardmaßig deaktiviert. Das bedeutet, dass man zwangsweise bei der ersten Inbetriebnahme Monitor und Tastatur, sowie Maus anschließen muss, um in der Raspberry-Pi-Konfiguration oder auf der Kommandozeile SSH zu aktivieren.

Um eine Verbindung zu einem Raspberry Pi per SSH aufbauen zu konnen benotigt man einen SSH-Client und die IPv4-Adresse des Raspberry Pi. Bei Computersystemen mit Mac OS und Linux ist der SSH-Client bereits auf der Kommandozeile integriert. Hier muss man nur noch ein Terminal-Programm aufrufen.  
Unter Windows muss man zusatzlich einen SSH-Client (z. B. PuTTY) installieren.

### Aufgabe

  1. Aktivieren Sie bei Bedarf SSH auf dem Raspberry Pi.
  2. Installieren Sie sich bei Bedarf einen SSH-Client auf Ihrem lokalen System.
  3. Stellen Sie eine Verbindung zum Raspberry Pi her. Verwenden Sie den Benutzernamen „pi" und das Passwort "raspberry".

### Losung 1: SSH per "raspi-config" aktivieren

Auf der Kommandozeile gibt man folgendes Kommando ein:
    
    
    sudo raspi-config

Zum Aktivieren von SSH folgt man dem Menu-Verlauf "Interfacing Options / SSH". Hier bestatigt man die Frage mit "Yes/Ja"

### Losung 2: Datei "ssh" in der Boot-Partition

Wenn man keine Moglichkeit hat, den Raspberry Pi per Tastatur, Maus und Bildschirm in Betrieb zunehmen, dann kann man auf der SD-Speicherkarte in der Boot-Partition eine leere Datei mit dem Namen "ssh" erstellen. Wenn man das mit Windows macht, dann muss man darauf achten, dass keine Dateiendung hinzugefugt wird.  
Wenn Raspbian gestartet wird, dann wird SSH aktiviert und die Datei automatisch geloscht.

### Losung 3: SSH auf der Kommandozeile aktivieren

Die folgende Losung ist auf den ersten Blick komplizierter, eroffnet dafur die Steuerungsmoglichkeiten von Diensten auf der Kommandozeile. Das heißt, was in diesem Fall bei SSH funktioniert, funktioniert auch bei anderen Dienste.

SSH starten:
    
    
    sudo systemctl start ssh

SSH stoppen:
    
    
    sudo systemctl stop ssh

SSH soll in Zukunft automatisch starten:
    
    
    sudo systemctl enable ssh

SSH soll in Zukunft NICHT mehr automatisch starten:
    
    
    sudo systemctl disable ssh

Gibt aus, ob SSH automatisch gestartet wird:
    
    
    systemctl is-enabled ssh

Status zu SSH anzeigen:
    
    
    sudo systemctl status ssh

Ausfuhrlicher Status zu SSH anzeigen:
    
    
    sudo systemctl show ssh

### Losung mit Mac OS oder Linux: SSH-Verbindung aufbauen

Zuerst ruft man ein Terminal-Programm auf. In der Kommandozeile gibt man dann ein:
    
    
    ssh pi@{IPv4-Adresse des Raspberry Pi}

Sofern eine Verbindung zur der IPv4-Adresse moglich ist und der Standard-Benutzer "pi" existiert muss man das Passwort "blind" eingeben. Damit ist gemeint, dass die Tastatureingabe nicht dargestellt wird. Es sieht so aus, als ob nichts eingegeben wird.
    
    
    raspberry

Danach muss man die Annahme des Zertifikats bestatigen (einmalig). Anschließend ist die SSH-Verbindung erfolgreich hergestellt.

Hinweis: Wenn man den Benutzernamen nicht gleich mit in die Adressierung eingibt (pi@...), dann versucht sich der SSH-Client mit dem lokalen Benutzer anzumelden. Das funktioniert in der Regel nicht, weil man hier in der Regel nicht mit dem selben Benutzer angemeldet ist.

### Losung unter Windows: SSH-Verbindung aufbauen

Hier empfiehlt sich die Installation von PuTTY, dass es auch als ausfuhrbares Programm ohne Installation gibt. Nach dem Starten von PuTTY gibt man die IPv4-Adresse des Raspberry Pi und Benutzername "pi" sowie das Passwort "raspberry". Es sollte "SSH" und der Port 22 ausgewahlt sein. Anschließend startet man den Verbindungsaufbau mit "Connect". Nach der Annahme des Zertifikats (einmalig) ist dann die SSH-Verbindung erfolgreich hergestellt.

### Die weiteren Schritte

### Weitere verwandte Themen:

### Produktempfehlungen
