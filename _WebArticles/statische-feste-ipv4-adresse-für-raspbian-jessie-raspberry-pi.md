# Statische/feste IPv4-Adresse für Raspbian Jessie (Raspberry Pi)

_Captured: 2017-05-06 at 15:24 from [www.elektronik-kompendium.de](https://www.elektronik-kompendium.de/sites/raspberry-pi/1912151.htm)_

Wer den Raspberry Pi zum ersten Mal in Betrieb nimmt und darauf per SSH zugreifen mochte, der muss zuerst einmal die IPv4-Adresse herausfinden. Geschickterweise zeigt der Raspberry Pi nach dem Boot-Vorgang seine IPv4-Adresse auf dem Bildschirm an, sofern man ihn mit Tastatur und Bildschirm in Betrieb nimmt. Leider andert sich die IPv4-Adresse immer mal wieder, weil bei der IPv4-Adressvergabe durch den DHCP-Server im lokalen Netzerk nicht immer die gleiche Adresse zugeteilt wird, sondern dynamisch irgendeine aus seinem Adress-Pool.

Sofern man den Raspberry Pi als Client benutzt, ist das kein Problem. Doch wenn man den Raspberry Pi als Server innerhalb des lokalen Netzwerk betreiben mochte oder ofter mal per SSH darauf zugreifen will, dann ist eine feste IPv4-Adresse von Vorteil. Hinweis hierbei: Man kann die Verbindung auch uber den Hostnamen z. B. "raspberrypi.local" aufbauen. Nur funktioniert das nicht immer.

Hinweis: In der Fachsprache spricht man nicht von einer "festen IP-Adresse", sondern von einer "statischen IP-Adresse", weil es im Gegensatz dazu dynamische IP-Adressen gibt, die von einem DHCP-Server zugewiesen werden. Im Falle einer "statischen IP-Adresse" spricht man von einer manuellen IP-Konfiguration.

**Hinweis: Wenn man statische IP-Adressen konfiguriert, dann sollten diese nicht aus dem DHCP-Pool eines DHCP-Servers kommen. **

### Mehr zum Thema IPv4-Adressen und DHCP

### Aufgabe

  1. Ermitteln Sie eine freie IPv4-Adresse und die weitere IP-Konfiguration.
  2. Stellen Sie die IPv4-Konfiguration auf statisch um.
  3. Prufen Sie die IPv4-Konfiguration.
  4. Prufen Sie die Netzwerk-Verbindung auf Funktion.

### Übersicht

Es gibt nicht nur eine, sondern gleich mehrere Varianten, wie man eine funktionierende Netzwerk-Konfiguration vornehmen kann. Welche man verwendet hangt von den Anforderungen und der personlichen Bevorzugung ab.

  1. IPv4-Konfiguration in der Datei "/etc/network/interfaces"
  2. IPv4-Konfiguration per DHCP Client Deamon (DHCPCD)
  3. Interface durch DHCPCD ausschließen (Kombination)
  4. IPv4-Konfiguration im Router zuweisen (zentrale IP-Konfiguration)
  5. IPv4-Konfiguration per systemd-networkd

Offiziell wird die IP-Konfiguration fur Raspbian Jessie uber den DHCPCD empfohlen (Losung 2). Grundsatzlich spricht allerdings nichts dagegen, eine statische IP-Konfiguration uber die Datei "/etc/network/interfaces" vorzunehmen (Losung 1). Man kann auch beide Losungen miteinander kombinieren (Losung 3).  
Der zukunftige Weg erfolgt uber "systemd-networkd", uber das ebenfalls die IP-Konfiguration erfolgen kann (Losung 5). Der einfachste Weg ware sicherlich, die IP-Zuweisung im Router zu machen (Losung 4). Dabei musste man keine Änderung am Raspberry Pi vornehmen.

### Troubleshooting: Netzwerk-Konfiguration

Probleme bei der Netzwerk-Konfiguration sind nicht ausgeschlossen. Deshalb gleich zu Anfang ein paar Hinweise zur Problemlosung.

### Losung (Variante 1): IPv4-Konfiguration in der Datei "/etc/network/interfaces"

Konfigurations-Datei fur die Netzwerk- bzw. IP-Konfiguration offnen:
    
    
    sudo nano /etc/network/interfaces

Eine vollstandige IPv4-Konfiguration sieht wie folgt aus:
    
    
    # Ethernet
    auto eth0
    allow-hotplug eth0
    iface eth0 inet static
    address 192.168.1.2
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 192.168.1.1

Es handelt sich hierbei um eine Beispiel-Konfiguration. Diese kann funktionieren, muss aber nicht. Sie einfach auszuprobieren ist nicht sinnvoll. Man sollte vorher klaren, was man hier eintragen muss und nicht irgendwie herumprobieren. Hilfreich ist es, wenn man nachschaut, was andere Clients im eigenen Netzwerk haben bzw. was beispielsweise schon per DHCP zugeteilt wurde.

Bei der Vergabe der IPv4-Adresse muss man jedoch darauf achten, dass man eine Adresse wahlt, die noch NICHT verwendet wird und sich auch NICHT im Adress-Pool eines DHCP-Servers (z. B. Internet-Router) befindet. Ansonsten kann es zu Verbindungsproblemen im Netzwerk kommen.

Nachdem man die Änderungen vorgenommen hat kann man die Datei speichern und schließen: Strg + O, Return, Strg + X.

**Hinweis: In Raspbian Wheezy ab 2015-05-05 und in Raspbian Jessie ist standardmaßig ein DHCP Client Daemon (DHCPCD) aktiv, der zum Problem werden kann, wenn man die IPv4-Konfiguration auf diese Weise vornimmt.**

Wenn man diesen DHCP-Client definitiv nicht braucht, dann sollte man ihn deaktivieren.

Bei Raspbian Wheezy:
    
    
    sudo service dhcpcd stop
    sudo update-rc.d -f dhcpcd remove

Bei Raspbian Jessie:
    
    
    sudo service dhcpcd stop
    sudo systemctl disable dhcpcd

Um die Änderungen zu ubernehmen empfiehlt sich hier ein Reboot.
    
    
    sudo reboot

Weniger radikal ist es, das "networking" neu zu starten. Das ist aber nur sinnvoll, wenn man NICHT per SSH mit dem Raspberry Pi verbunden ist.
    
    
    sudo service networking restart

Alternativ kann man das Interface "eth0" aus- und wieder einschalten. Auch das ist nur dann sinnvoll, wenn man NICHT per SSH verbunden ist, sondern lokal mit Bildschirm und Tastatur am Raspberry Pi sitzt.
    
    
    sudo ifdown eth0
    sudo ifup eth0

Dadurch wird das Interface "eth0" beendet und neu gestartet. Beim Start werden die Einstellungen ubernommen. Danach musste der Raspberry Pi mit seiner statischen IPv4-Adresse erreichbar sein.

Anschließend ist die Netzwerk-Konfiguration zu prufen.

### Losung (Variante 2): IPv4-Konfiguration per DHCP Client Deamon (DHCPCD)

In Raspbian Jessie ist standardmaßig ein DHCP Client Daemon (DHCPCD) aktiviert. Der offiziell empfohlene Weg eine IPv4-Konfiguration vorzunehmen, ist uber den DHCPCD, der dafur eine Konfigurationsdatei bereithalt.

Hierzu ist es wichtig festzustellen, ob der "dhcpcd" uberhaupt aktiv ist.
    
    
    sudo service dhcpcd status

Liefert der Status einen installierten, aber abgeschalteten "dhcpcd", dann empfiehlt es sich diesen einzuschalten. Erst dann sollte man die Konfiguration uber den "dhcpcd" vornehmen.
    
    
    sudo service dhcpcd start  
    sudo systemctl enable dhcpcd

Bevor man an die Konfiguration uber den "dhcpcd" vornimmt, sollte man [den Original-Zustand der Datei "/etc/network/interfaces" wieder herstellen](https://www.elektronik-kompendium.de/sites/raspberry-pi/2008011.htm). Die Schnittstellen mussen in der Option "iface" auf "manual" gesetzt sein.

Zur statischen IPv4-Konfiguration offnet man die Datei "/etc/dhcpcd.conf".
    
    
    sudo nano /etc/dhcpcd.conf

Hier tragt man beispielhaft folgende Zeilen ein:
    
    
    interface eth0
    static ip_address=192.168.1.2/24
    static routers=192.168.1.1
    static domain_name_servers=192.168.1.1

Es handelt sich hierbei um eine Beispiel-Konfiguration. Diese kann funktionieren, muss aber nicht. Sie einfach auszuprobieren ist nicht sinnvoll. Man sollte vorher klaren, was man hier eintragen muss und nicht irgendwie herumprobieren. Hilfreich ist es, wenn man nachschaut, was andere Clients im eigenen Netzwerk haben bzw. was beispielsweise schon per DHCP zugeteilt wurde.

Bei der Vergabe der IP-Adresse muss man jedoch darauf achten, dass man eine wahlt, die noch NICHT verwendet wird und sich auch nicht im Adress-Pool eines DHCP-Servers befinden. Ansonsten wird es zu Verbindungsproblemen im Netzwerk kommen.

Die Zeile "static ip_address=192.168.1.2/24" gibt die IPv4-Adresse "192.168.1.2" mit der Subnetzmaske "255.255.255.0" an. Die Angabe "24" ist eine Kurzschreibweise fur die Subnetzmaske.

Nachdem man die Änderungen vorgenommen hat kann man die Datei speichern und schließen: Strg + O, Return, Strg + X.

Man hat jetzt nur die Datei geandert. Die Änderungen wurden aber noch nicht in die aktuelle Netzwerk-Konfiguration ubernommen. Grundsatzlich empfiehlt sich hier ein Reboot, wenn man per SSH die Konfiguration vorgenommen hat.
    
    
    sudo reboot

Weniger radikal ist es, das "networking" neu zu starten. Das ist aber nur sinnvoll, wenn man NICHT per SSH mit dem Raspberry Pi verbunden ist.
    
    
    sudo service networking restart

Alternativ kann man das Interface "eth0" aus- und wieder einschalten. Auch das ist nur dann sinnvoll, wenn man NICHT per SSH verbunden ist, sondern lokal mit Bildschirm und Tastatur am Raspberry Pi sitzt.
    
    
    sudo ifdown eth0
    sudo ifup eth0

Dadurch wird das Interface "eth0" beendet und neu gestartet. Beim Start werden die Einstellungen ubernommen. Danach musste der Raspberry Pi mit seiner statischen IPv4-Adresse erreichbar sein.

### Losung (Variante 3): Interface durch DHCPCD ausschließen (Kombination)

Wenn man den DHCPCD nicht deaktivieren will, weil man ihn fur ein Interface braucht, dann kann man die Konfiguration durch den DHCPCD fur ein Interface ausschließen oder explizit freigeben.

Dazu offnen wir die Konfigurations-Datei des DHCPCD und tragen dort noch eine Zeile ein.
    
    
    sudo nano /etc/dhcpcd.conf

Netzwerk-Interface von der Konfiguration durch den DHCPCD ausschließen:
    
    
    denyinterfaces eth0

Diese Zeile klammert das betreffende Interface aus der Netzwerk-Konfiguration aus. Die Netzwerk-Konfiguration fur dieses Interface muss dann in der Datei "/etc/network/interfaces" erfolgen.

Interface explizit freigeben:
    
    
    allowinterfaces eth0

Nachdem man die Änderungen vorgenommen hat kann man die Datei speichern und schließen: Strg + O, Return, Strg + X.

Die Änderungen wurden aber noch nicht in die aktuelle Netzwerk-Konfiguration ubernommen. Grundsatzlich empfiehlt sich hier ein Reboot, wenn man per SSH die Konfiguration vorgenommen hat.
    
    
    sudo reboot

Weniger radikal ist es, das "networking" neu zu starten. Das ist aber nur sinnvoll, wenn man NICHT per SSH mit dem Raspberry Pi verbunden ist.
    
    
    sudo service networking restart

Alternativ kann man das Interface "eth0" aus- und wieder einschalten. Auch das ist nur dann sinnvoll, wenn man NICHT per SSH verbunden ist, sondern lokal mit Bildschirm und Tastatur am Raspberry Pi sitzt.
    
    
    sudo ifdown eth0
    sudo ifup eth0

Dadurch wird das Interface "eth0" beendet und neu gestartet. Beim Start werden die Einstellungen ubernommen. Danach musste der Raspberry Pi mit seiner statischen IPv4-Adresse erreichbar sein.

### Losung (Variante 4): IPv4-Konfiguration im Router zuweisen (zentrale IP-Konfiguration)

Wenn man dem Raspberry Pi eine statische IP-Konfiguration mit fester IPv4-Adresse verpassen, aber dessen Netzwerk-Konfiguration nicht anfassen mochte, dann kann man sich auch einer Funktion im Internet-Router bedienen. Manche dieser Gerate haben eine Funktion, die es ermoglicht, dass die IPv4-Adresse auf die MAC-Adresse festgelegt wird. In dem Fall ware die MAC-Adresse der Netzwerk-Schnittstelle zu ermitteln, der man im Router eine IPv4-Adresse fest zuteilt. Die Netzwerk-Konfiguration holt sich der Raspberry Pi weiterhin per DHCP. Nur bekommt er dann immer die selbe IPv4-Adresse zugewiesen.  
Diese Losung hat den unausweichlichen Charme, dass man den Raspberry Pi dafur nicht anfassen muss. Nachteil dieser Losung ist, dass dazu der DHCP-Server aktiv sein muss, wenn sich der Raspberry Pi die IP-Konfiguration per DHCP holt. Wenn nicht, dann steht der Raspberry Pi ohne IPv4-Adresse da.

### Losung (Variante 5): IPv4-Konfiguration per systemd-networkd

Neben der alten Konfiguration per "/etc/network/interfaces" oder "dhcpcd" gibt es noch die systemd-Variante. In zukunftigen Raspbian-Versionen wird "systemd" die Netzwerk-Konfiguration ubernehmen.

Man sollte die Umstellung auf "systemd-networkd" nicht per SSH machen. Gibt es eine Verbindungsunterbrechung, dann bekommt man die Verbindung unter Umstanden nicht wieder aufgebaut.

Zuerst prufen wir, ob der Dienst "systemd-networkd" vorhanden ist. Das ist die Voraussetzung, dass diese Losung uberhaupt moglich ist. Ab Raspbian Jessie sollte das funktionieren.
    
    
    systemctl status systemd-networkd

Dort sollte stehen "Loaded: loaded".

Zuerst geht es darum, alte Network- oder Networking-Komponenten zumindest zu deaktivieren. Deinstallieren und loschen empfiehlt sich nicht, weil man sonst nur schwer wieder zuruckkehren kann.
    
    
    sudo update-rc.d networking remove
    sudo systemctl stop dhcpcd
    sudo systemctl disable dhcpcd

Den Dienst fur die Namensauflosung "systemd-resolved" aktivieren und starten:
    
    
    sudo systemctl enable systemd-resolved
    sudo systemctl start systemd-resolved

Prufen, ob "systemd-resolved" lauft:
    
    
    sudo systemctl status systemd-resolved
    

In der Zeile "Loaded: loaded" sollte hinten "enabled" stehen.

Dann setzen wir noch einen symbolischen Link fur die Datei mit der Adresse des Nameservers. Wenn dieser Link fehlt, dann kann es sein, dass die Namensauflosung nicht funktioniert.
    
    
    sudo ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf

Dann geht es darum, eine Netzwerk-Konfiguration anzulegen. Die kann in mehreren Dateien verteilt sein, die sich alle im selben Verzeichnis befinden.
    
    
    ls /etc/systemd/network/

Wenn das Verzeichnis leer ist, dann muss man die notwendigen Dateien erst noch anlegen. Der Dateiname ist dabei unerheblich. Er muss nur auf ".network" enden. Trotzdem empfiehlt es sich, sinnvolle Dateinamen zu wahlen, um sich im Fehlerfall leichter zurecht zu finden.

Beispiel fur eine statische IPv4-Konfiguration fur das Interface "eth0":
    
    
    sudo nano /etc/systemd/network/eth0.network

Eintrag fur eine statische IPv4-Konfiguration:
    
    
    [Match]
    Name=eth0
    
    [Network]
    Address=192.168.1.2/24
    Gateway=192.168.1.1  
    DNS=192.168.1.1

Alternativ: Eintrag fur eine IP-Konfiguration mit DHCP:
    
    
    [Match]
    Name=eth0
    
    [Network]
    DHCP=yes

Speichern und schließen mit Strg + O, Return, Strg + X.

Den Dienst "systemd-networkd" aktivieren und starten:
    
    
    sudo systemctl enable systemd-networkd
    sudo systemctl start systemd-networkd
    

Prufen, ob "systemd-networkd" lauft:
    
    
    sudo systemctl status systemd-networkd
    

In der Zeile "Loaded:" sollte hinten "enabled" stehen und die Schnittstelle sollte konfiguriert sein. In diesem Fall "eth0 : link configured".

Danach das System neustarten:
    
    
    sudo reboot

Nach dem Neustart sollte das System mit "systemd-networkd" laufen.

### Losung: Netzwerk-Konfiguration prufen

Ob die IPv4-Einstellungen korrekt ubernommen wurden, sollte man prufen.

Die IP-Adresse kann man wie folgt prufen.
    
    
    ip a

Das Interface "eth0" muss dann in der Zeile mit "inet-Adresse" die statische konfigurierte IPv4-Adresse bekommen haben.

Dann pruft man, ob das Standard-Gatway bzw. die Default-Route eingetragen ist. Die ist wichtig, damit man uberhaupt ins Internet kommt.
    
    
    ip r

Wenn "default" auf die richtige IPv4-Adresse des Standard-Gateways zeigt, dann ist alles in Ordnung.

Jetzt fehlt noch der DNS-Server. Der ist notwendig, damit die Namensauflosung funktioniert und Verbindungen ins Internet uber die ermittelten IP-Adressen uber das Standard-Gateway moglich sind.
    
    
    cat /etc/resolv.conf

Steht hinter "nameserver" die IPv4-Adresse des DNS-Servers, dann ist auch hier alles in Ordnung.

### Troubleshooting: Doppelte IPv4-Adresse

Grundsatzlich gilt, dass ein Interface (eth0, wlan0, usw.) nur eine IPv4-Adresse haben darf. Die Prufung der Netzwerk-Konfiguration ergab, dass die IPv4-Adresse doppelt vergeben wurde. Das kann zu Problemen fuhren.
    
    
    ip a
    

Eine beispielhafte Ausgabe:
    
    
    inet 192.168.1.2/24 brd 192.168.1.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet 192.168.1.132/24 brd 192.168.1.255 scope global secondary eth0
       valid_lft forever preferred_lft forever

Wie man sieht, hat das Interface "eth0" zwei IPv4-Adressen, was zu Problemen im Netzwerk fuhren kann. Manche Router reagieren allergisch, wenn ein Host unter zwei IPv4-Adressen erreichbar ist.

Hier spuckt uns der DHCP Client Daemon in die Suppe. Wenn man diesen DHCP-Client definitiv nicht braucht, dann sollte man ihn deaktivieren.
    
    
    sudo systemctl stop dhcpcd
    sudo systemctl disable dhcpcd

Um die Änderungen zu ubernehmen empfiehlt sich ein Reboot.

  * [Weitere Netzwerk-Probleme beim Raspberry Pi losen](https://www.elektronik-kompendium.de/sites/raspberry-pi/2008011.htm)

### Troubleshooting: Kein Hostname mehr

Wenn man die Netzwerk-Konfiguration nach Losung 1, 2 oder 3 einstellt, dann ergibt sich das Problem, dass man den Hostnamen des Raspberry Pi nicht mehr im Internet-Router angezeigt bekommt. Nur wenn man die Einstellungen im Urzustand belasst erscheint im Router der Hostname "raspberrypi" (Grundeinstellung).  
Der Grund dafur ist die statische Netzwerk-Konfiguration. In dem Fall findet keine aktive Kommunikation zwischen Raspberry Pi und dem Router statt. Und somit erfahrt der Router auch nicht den Hostnamen des Raspberry Pi.  
Man kann das Problem mit Variante 4 losen. Hier findet dann die Kommunikation mit DHCP statt und der Raspberry Pi teilt auf diese Weise seinen Hostnamen mit.  
Die Voraussetzung, damit das funktioniert ist, dass in der Datei "/etc/dhcpcd.conf" in einer Zeile "hostname" steht.

### Erweiterung: IPv4-Konfiguration mit dem Netzwerk-Manager "wicd-curses"

"wicd-curses" ist ein grafischer Netzwerk-Manager, der alle wichtigen Informationen in einer Benutzeroberflache darstellt, die mit der Tastatur bedient werden muss. Wer sich mit dem Editieren von Text-Dateien schwer tut, fur den kann das eine Alternative sein.

  * [IPv4-Konfiguration mit dem Netzwerk-Manager wicd-curses (Raspberry Pi)](https://www.elektronik-kompendium.de/sites/raspberry-pi/2007091.htm)

### Erweiterung: Über den Hostnamen auf den Raspberry Pi zugreifen (Zeroconf/Bonjour/Avahi)

Wer nicht mit IP-Adressen und deren Konfiguration hantieren mochte, kann das Problem auch mit Zeroconf losen. Mit Zeroconf, auch Bonjour oder Avahi genannt, kann man innerhalb des lokalen Netzwerks eine Verbindung zum Raspberry Pi mit seinem Hostnamen aufbauen. Das heißt, statt der IP-Adresse, die man vielleicht gar nicht weiß, nimmt man einfach den Hostnamen, den man sich viel einfacher merken kann. Das funktioniert sowohl im Browser als auch per SSH.

### Weitere verwandte Themen:

### Produktempfehlungen
