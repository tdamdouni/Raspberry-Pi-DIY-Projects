# VPN-Server mit dem Raspberry Pi aufbauen

_Captured: 2015-12-25 at 22:19 from [www.tecchannel.de](http://www.tecchannel.de/pc_mobile/peripherie/2065395/vpn_server_mit_dem_raspberry_pi_aufbauen/)_

### 1\.

Ein [VPN](http://www.tecchannel.de/netzwerk/wan/) verschlusselt den gesamten Datenverkehr auf Netzwerkebene. Wer mit dem Mobilgerat oder [Notebooks](http://www.tecchannel.de/pc_mobile/notebook/) in offentlichen WLANs unterwegs ist, kann mit einem VPN den gesamten Datenverkehr verschlusselt uber den VPN-[Server](http://www.tecchannel.de/server/) zu Hause oder im Buro umleiten. Und nicht nur das: Der VPN-Server ist auch ein sicheres Eingangstor zum [Netzwerk](http://www.tecchannel.de/netzwerk/) dahinter. Mit dem richtigen Routing, das der Server dem Client mitteilt, kann der VPN-Server eine Verbindung zum gesamten Netzwerk herstellen. So, als ob Sie sich direkt im lokalen Netzwerk befanden. Diese Losung eignet sich nicht nur fur Reisende und Außendienstmitarbeiter, die unterwegs auf Dokumente im Buro zugreifen mussen. Auch fur Privatanwender ist die Losung ideal, um sicher und verschlusselt von offentlichen WLANs auf den heimischen PC zu kommen.

Der VPN-Server muss dazu von außen erreichbar sein. Er authentifiziert den VPN-Client und stellt die Verbindung zu anderen Rechnern im VPN mittels Routing her. Fur diese Rolle ist der Raspberry Pi pradestiniert, da hier alle Werkzeuge zur Verfugung stehen. Die Leistung der [CPU](http://www.tecchannel.de/server/prozessoren/) und die Geschwindigkeit der 100-MBit- [Ethernet](http://www.tecchannel.de/netzwerk/lan/)-Ports reicht fur ein kleineres Netzwerk, das per DSL an die Außenwelt angebunden wird.

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2525465/522x294.png)

> _Raspberry Pi in der Praxis_

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2518726/522x294.png)

Eine Linux-Distribution wie Raspbian liefert die benotigten Software-Pakete fur den Aufbau eines Virtual Private Networks mit Open VPN. Fur dieses VPN-Protokoll ist nicht nur die Server- Komponente frei, es gibt auch freie Clients fur [Windows](http://www.tecchannel.de/pc_mobile/windows/), Mac-OS, iOS, Android und naturlich fur Linux. Die Hardware-Voraussetzungen sind ebenfalls ubersichtlich: Ein Mini-Linux-System wie der Raspberry Pi wird als Server benotigt und muss an den Internetanbieter uber einen [Router](http://www.tecchannel.de/netzwerk/lan/) angeschlossen sein, der Port-Forwarding unterstutzt. Ein grundlegendes Feature, das die meisten Router - auch ganz einfache Modelle - unterstutzen.

Open VPN ist fur den professionellen Einsatz geschaffen, und die erste Konfiguration des Servers stellt immer eine gewisse Hurde dar, da einige Software-Komponenten des Linux-Systems richtig konfiguriert und aufeinander abgestimmt werden mussen. Dies erfolgt auf dem Raspberry Pi ganz in der Linux-Tradition in der Kommandozeile und mit textbasierenden Konfigurationsdateien. Dabei sind ein paar Netzwerkkenntnisse sowie Linux-Kenntnisse, etwa zur Arbeit als root mit sudo und zum Umgang mit Texteditoren von Vorteil.

Als Linux-Distribution fur den Raspberry Pi eignen sich die Debian-Varianten Raspbian und Raspbmc, die sich uber das Installations-Tool[ Noobs](http://www.pcwelt.de/news/Raspberry_Pi_wird_benutzerfreundlicher_-Noobs-7949701.html) installieren lassen. Die folgende Anleitung bezieht sich auf Raspbian/ Raspbmc. Die Befehle und Paketnamen weichen bei anderen Linux-Distributionen im Detail ab, etwa beim ebenfalls geeigneten Pidora. Die Einrichtung und Konfiguration auf Kommandozeile (Shell) erfolgt wahlweise direkt auf dem Raspberry Pi, an dem dazu Bildschirm und Tastatur angeschlossen sind. Oder auch einfach per SSH uber das Netzwerk mit Hilfe eines SSH-Clients wie [Putty](http://www.pcwelt.de/downloads/Putty-1327610.html).

### 2\.

Der [Router](http://www.tecchannel.de/netzwerk/lan/) muss außerdem wissen, welche Anfragen aus dem Internet durchgelassen werden solleen und welcher Teilnehmer im [Netzwerk](http://www.tecchannel.de/netzwerk/) der Open-[VPN](http://www.tecchannel.de/netzwerk/wan/)-[Server](http://www.tecchannel.de/server/) ist. Zu diesem Zweck richten Sie auf dem Router Port-Forwarding ein, um gezielt nach außen einen einzigen Port zu offnen und an die passende Adresse im [LAN](http://www.tecchannel.de/netzwerk/lan/) weiterzuleiten. Der Port fur Open VPN ist der Port 1194 (UDP). Wenn der Open-VPN-Server im LAN beispielsweise die IP 192.168.1.6 hat, dann leiten Sie vom Router den Traffic vom Typ UDP am Ports 1194 auf die interne IP-Adresse und den dortigen Port 1194 um. Welche IP-Adresse die Netzwerkschnittstelle ([WLAN](http://www.tecchannel.de/netzwerk/wlan/) oder [Ethernet](http://www.tecchannel.de/netzwerk/lan/)) des Raspberry Pi hat, finden Sie dort in der Kommandozeile mit dem Befehl

`/sbin/ifconfig`

heraus. Der Server, der von außen die VPN-Verbindungen akzeptieren soll, muss zudem aus dem Internet erreichbar sein. Und zwar uber eine feste IP-Adresse oder uber einen eindeutigen [DNS](http://www.tecchannel.de/netzwerk/lan/)-Namen.

**Parameter fur Schlussel festlegen:** Legen Sie diese Einstellungen in der Datei "/etc/ openvpn/easy-rsa/vars" fest, damit die Scripts zur Schlusselerzeugung fur Client und Server die Werte ubernehmen.

Bei DSL-Anbindung fallt eine feste IP aus, da bei jedem Verbindungsaufbau der Provider neue IP-Adressen vergibt. Fur diesem Fall kommt ein dynamischer DNS-Dienst wie beispielsweise [Noip](http://www.noip.com/) zur Hilfe, der auch einer sich andernden IP-Adresse feste Host-Namen im DNS zuteilt. Die meisten DSL-Router unterstutzen Noip und teilen dem Dienst nach der Einrichtung automatisch die neue IP des Providers mit.

In der Kommandozeile von Raspbian/Raspbmc dient der Paketmanager APT von Debian zur Installation von Open VPN - man muss nichts selbst kompilieren. Mit den beiden Befehlen

`sudo apt-get update` 
`sudo apt-get install openvpn`

werden die Pakete uber die bestehende Internetverbindung aus dem Software-Verzeichnis der Distribution installiert. Fur die spatere Erstellung der eigenen Zertifikate fur die VPNVerschlusselung gibt es fertige Scripts, die noch an die richtige Stelle kopiert werden mussen:

`sudo cp -r /usr/share/doc/ openvpn/examples/easy-rsa/2.0 / etc/openvpn/easy-rsa`

`cd /etc/openvpn/easy-rsa`

in das Script-Verzeichnis und editieren mit

`sudo nano vars`

die Konfigurationsdatei "vars". Gehen Sie dort zuerst zur Zeile, die mit "export KEY_CONFIG=" beginnt und andern Sie diese zu:

`export KEY_CONFIG=$EASY_RSA/ openssl-1.0.0.cnf`

`export EASY_RSA="/etc/openvpn/ easy-rsa"`

Die nachsten Anpassungen sind nahe am Ende der Datei zu machen, um Namen und Identitat des VPNs anzupassen. Viele dieser Parameter sind zwar nicht unbedingt fur die korrekte Funktion des VPNs relevant, mussen aber trotzdem gesetzt sein:

`export KEY_COUNTRY="DE"`

Landeskurzel, beispielsweise "DE" fur Deutschland.

`export KEY_PROVINCE="BY"`

Ein beliebiger Name fur das Bundesland.

`export KEY_CITY="Muenchen"`

Eine Ortsangabe, die den Standort angibt.

`export KEY_ORG="MeinVPN"`

Ein Firmenname Ihrer Wahl. Kann auch einfach der Domain-Name sein.

`export KEY_EMAIL="pcwelt@googlemail.com"`
`export KEY_EMAIL=pcwelt@googlemail.com`

Zweimalige Angabe einer beliebigen Mailadresse des VPN-Administrators, also meist einfach die eigene Adresse.

`export KEY_CN="example.no-ip.com"`

Der gewunschte Name dieses VPNs. Es sollte hier die Angabe des dynamischen Domain- Namens erfolgen, der zuvor uber Noip eingerichtet wurde.

`export KEY_NAME="MeinVPN"`

Ein beliebiger Name fur den Aussteller der Zertifikate.

`export KEY_OU="MeinVPN"`

Eine Angabe zum Abteilungsnamen, der frei gewahlt werden kann. Die abschließenden beiden Parameter

`export PKCS11_MODULE_ PATH=changeme`
`export PKCS11_PIN=1234`

kommen nicht zum Einsatz und brauchen nicht geändert zu werden.

### 3\. Server: Die Schlussel erzeugen

**Schlusselaustausch mittels Diffie-Hellman:** Bei dieser kryptografischen Methode werden zufallige Diffie-Hellman-Parameter erzeugt, was auf der ARM-CPU des Raspberry Pi eine Weile dauert.

Bevor es daran geht, die Schlussel fur den den [Server](http://www.tecchannel.de/server/) und fur die Clients zu erstellen, ist es erst noch notig, ein eigenes CA-Zertifikat fur die Signatur der Schlussel zu erzeugen. Dies gelingt, indem Sie zuerst mit

`cd /etc/openvpn/easy-rsa`

in das Script-Verzeichnis gehen und dann mit

`sudo -s`

eine Root-Shell offnen. Die folgenden Befehle werden dann gleich mit Root-Rechten ausgefuhrt, und ein vorangestelltes sudo ist nicht notig. Mit

`source ./vars`

lesen Sie zuerst die zuvor gesetzten Variablen der Datei "vars" ein. Dann fuhren Sie die beiden Befehle

`./clean-all`
`./build-dh`

aus, um ein sauberes Schlusselverzeichnis zu erzeugen und die Diffie-Hellmann-Werte, welche fur die Kryptographie-Funktionen des VPNs notig sind. Die Berechnung dieser zufalligen Werte nimmt auf dem Raspberry Pi rund eine Minute in Anspruch.

Bevor Sie nun die Zertifikate fur den Open-[VPN](http://www.tecchannel.de/netzwerk/wan/)-Server sowie die Clients erstellen konnen, ist es notwendig, das CA-Zertifikat zum Signieren der Server- und Client-Zertifikate zu erstellen. Dies fuhren Sie mit den folgenden beiden Befehlen aus:

`./build-ca`  
`./build-key-server MeinVPN`

Es erfolgen jeweils nach jedem Befehl einige Abfragen der bereits festgelegten Parameter, und Sie konnen die Werte in eckigen Klammern einfach durch einen Druck auf die Eingabetaste ubernehmen. Beim letzten Befehl zum Erzeugen der Server-Schlussel erfolgt zudem noch die Ruckfrage nach einem optionalen Passwort, dass Sie leer lassen. Abschließend Beantworten Sie noch die Ruckfragen "Sign the certificate?" und "Commit" mit "y".

Als Nachstes geht es zur eigentlichen Konfiguration des Open-VPN-Servers. Mit dem Befehl

`nano /etc/openvpn/server.conf`

offnen Sie eine neue, noch leere Konfigurationsdatei im Texteditor. Tragen Sie dort die Zeilen ein, die im Kasten "Konfigurationsdatei des Open-VPN-Servers" abgedruckt ist.
### Fur die Clients: Zertifikate und Schlussel

**Serverschlussel erzeugen:** Client und Server bekommen eigene Schlussel, die jeweils mit Scripts aus dem Paket von Open VPN erzeugt werden. Die optionale Passwortabfrage lassen Sie jeweils leer.

Der [Server](http://www.tecchannel.de/server/) hat nun alle benotigten Schlussel und Zertifikate. Damit Sie sich aber mit einem [VPN](http://www.tecchannel.de/netzwerk/wan/)-Client spater verbinden konnen, braucht jeder Client naturlich auch sein eigenes Schlusselbund. Dieses erzeugen Sie in diesem Schritt mit dem Aufruf von

`./build-key client1`

Auch hier konnen Sie wieder die vorgegebenen Werte ubernehmen und lassen "Passwort" leer. Die Client-Dateien werden ebenfalls im Verzeichnis "/etc/openvpn/easy-rsa/keys" abgelegt. Aus diesem Verzeichnis brauchen Sie fur den Client Nummer eins die Dateien "ca. cert", "client1.crt" und "client1.key".

### Routing: Vom VPN ins Netzwerk

Das Linux-System auf dem Raspberry Pi soll den Datenverkehr aus dem VPN ins lokale [Netzwerk](http://www.tecchannel.de/netzwerk/) weiterleiten und zudem noch eine Internetverbindung fur die Clients zur Verfugung stellen. Öffnen Sie wieder eine Root-Shell mit

`sudo -s`

da alle weiteren Befehle wieder Root-Rechte verlangen. Öffnen Sie die Datei "2/etc/sysctl. conf" mittels

`nano /etc/sysctl.conf`

im Texteditor, entfernen das Kommentarzeichen "#" vor der Zeile "#net.ipv4.ip_forward=1" und aktivieren nach dem Speichern der Datei die Änderung mit diesem Befehl:

`sysctl -p /etc/sysctl.conf`

Nun muss noch mit dem Paketfilter iptables, der Teil des Linux-Kernels ist, eine Weiterleitung fur die VPN-Pakete eingerichtet werden. Mit den beiden Befehlen

`iptables -A INPUT -i tun+ -j ACCEPT`
`iptables -A FORWARD -i tun+ -j ACCEPT`

erstellen Sie die Regeln fur das VPN-Netzwerk-Interface und mit den weiteren drei Befehlen

`iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT` 
`iptables -t nat -F POSTROUTING`
`iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE`

legen Sie fest, dass die VPN-Clients auch in das lokale Netzwerk und ins Internet kommen. Damit diese Regeln immer gleich automatisch nach dem Start des Raspberry Pi aktiv werden, geben Sie

`iptables-save > /etc/iptables.up.rules`

ein, um die aktuellen Einstellungen von iptables zu sichern. Erstellen Sie mit

`nano /etc/network/if-pre-up.d/ iptables`

eine neue Script-Datei, der Sie den Inhalt

`#!/bin/bash /sbin/iptables-restore < /etc/ iptables.up.rules`

geben und speichern. Jetzt mussen Sie die Datei nur noch mit

`chmod +x /etc/network/ if-pre-up.d/iptables`

ausführbar machen.

### Konfiguration: Windows als Client

Wer die bisherigen Einrichtungsschritte obskur und umfangreich fand, kann beruhigt sein: Die Konfiguration des Clients fallt deutlich knapper und geradliniger aus. Auf einem [Windows](http://www.tecchannel.de/pc_mobile/windows/)-System als Client installieren Sie [Open VPN 2.3.2](http://www.pcwelt.de/downloads/OpenVPN-570615.html). Kopieren Sie die erzeugten Client-Schlussel "client1.crt" und "client1.key" sowie das allgemeine Zertifikat "ca.crt" nach "C:\Program Files\OpenVPN\config" ("C:\Program Files(x86)\OpenVPN\config" bei 64-Bit-Systemen). Anschließend legen Sie im gleichen Verzeichnis die neue Textdatei mit dem Namen "client.ovpn" an, der Sie den Inhalt geben, wie er im Kasten "Konfigurationsdatei des Open- [VPN](http://www.tecchannel.de/netzwerk/wan/)-Servers" steht.

**Verbindung mit Windows:** Ist alles korrekt konfiguriert, kann sich ein Client - hier etwa Windows 7 - mit dem Raspberry Pi verbinden und kommt uber ihn in das VPN. Ein Statusfenster zeigt den Verbindungsaufbau und eventuelle Fehler.

Nun ist es an der Zeit, den Client zu starten. Dazu bringt Open VPN unter Windows ein Werkzeug fur den unkomplizierten Start bereits mit: Open VPN GUI ist ein Tool, das bei der Installation von Open VPN mit Standard-Einstellungen gleich mit installiert wird. Sie finden es im Startmenu im Ordner "OpenVPN". Es ist wichtig, dieses Tool stets als Administrator auszufuhren, da der Aufbau einer VPN-Verbindung auch neue Routen in den Netzwerkeinstellungen setzt. Um nicht jedes Mal Open VPN per Rechtsklick zu starten, konnen Sie auch in den Eigenschaften der Verknupfung zu Open VPN GUI im Startmenu oder auf dem Desktop im Dialog unter "Kompatibilitat" die Option "Programm als Administrator ausfuhren".

Nach dem Aufruf von Open VPN GUI prasentiert sich im Infobereich neben der Zeitanzeige ein neues Netzwerksymbol, das ohne VPNVerbindung rot eingefarbt ist. Mit einem Rechtsklick auf das Symbol wahlen Sie im Menu den Punkt "Connect" aus. Es offnet sich ein Programmfenster, das Sie mit detaillierten Meldungen uber den Verbindungsaufbau informiert. Nachdem die VPN-Verbindung steht, schließt sich das Fenster, und das Symbol im Infobereich zeigt sich in Grun. Windows fugt auf dem Client die neue virtuelle Netzwerkschnittstelle von Open VPN als "[LAN](http://www.tecchannel.de/netzwerk/lan/)-Verbindung 2" hinzu, und das System fragt, um welche Art von [Netzwerk](http://www.tecchannel.de/netzwerk/) es sich handelt. Wahlen Sie fur das VPN als Typ das Heimnetzwerk oder das Arbeitsplatznetzwerk. Rechner im lokalen Netzwerk erreichen Sie uber deren IP-Adresse, und der gesamte Internet-Traffic geht nun verschlusselt immer uber den Raspberry Pi. Zwar konnen Sie Netzwerkdienste wie Windows- Freigaben vom Open-VPN-[Server](http://www.tecchannel.de/server/) nutzen, der Client antwortet jedoch selbst nicht auf Ping- Anfragen und kann keine Freigaben uber das VPN anbieten.
### Konfigurationsdatei des Open-VPN-Servers

Die folgende Open-[VPN](http://www.tecchannel.de/netzwerk/wan/)-Beispielkonfiguration tragen Sie auf dem Raspberry Pi in der Datei "/etc/openvpn/server.conf" ein. Passen Sie die Dateinamen in den Zeilen "cert" und "key" an, wenn Sie nicht wie im Beispiel "MeinVPN" verwenden.

`dev tun`
`proto udp`
`port 1194`
`ca /etc/openvpn/easy-rsa/keys/ca.crt`
`cert /etc/openvpn/easy-rsa/keys/MeinVPN.crt`
`key /etc/openvpn/easy-rsa/keys/MeinVPN.key`
`dh /etc/openvpn/easy-rsa/keys/dh1024.pem`  
`user nobody`
`group nogroup`
`server 10.8.0.0 255.255.255.0`
`persist-key`
`persist-tun`
`status /var/log/openvpn-status.log`
`verb 3`
`client-to-client`
`push "redirect-gateway def1"``
`push "dhcp-option DNS 208.67.222.222"`
`push "dhcp-option DNS 208.67.220.220"`
`log-append /var/log/openvpn`
`comp-lzo`

### Konfigurationsdatei des Open-VPN-Clients

Die Client-Konfiguration fur Open VPN unter [Windows](http://www.tecchannel.de/pc_mobile/windows/). Die folgenden Zeilen tragen Sie in der Datei "client.ovpn" ein. Anzupassen ist hier nur der Domain-Name "beispiel. no-ip.com" in der Zeile "remote", damit hier der korrekte dynamische Domain- Name des VPN-Servers steht. Die Port-Angabe dahinter muss beibehalten werden.

`dev tun`
`client`
`proto udp`
`remote beispiel.no-ip.com 1194`
`ca ca.crt`
`cert client1.crt`
`key client1.key`
`resolv-retry infinite`
`route-method exe`
`route-delay 30`
`route-metric 512`
`route 0.0.0.0 0.0.0.0`
`nobind`
`persist-key`
`persist-tun`
`comp-lzo`
`verb 3`
