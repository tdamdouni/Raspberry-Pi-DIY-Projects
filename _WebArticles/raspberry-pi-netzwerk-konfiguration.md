# Raspberry Pi: Netzwerk-Konfiguration

_Captured: 2017-05-06 at 15:47 from [www.netzmafia.de](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_Network.html)_

**Vorbemerkung:** Oft liegen Netzwerk-Probleme beim Raspberry Pi an einer instabilen Stromversorgung. So kann bei einer zu geringen Betriebsspannung (unter 5 V) der RasPi zur Stabilisierung den Stromverbrauch reduzieren indem er einzelne Komponenten abschaltet. Geschieht dies beim USB-Controller, der intern auch noch den Ethernet-Port bedient (Modelle A und B), betrifft das auch die Netzwerk-Verbindung. Diese geht bei stabiler Betriebsspannung wieder in Betrieb, aber setzt bei Belastungsspitzen aus. Daher sollte man bei sporadischen Ausfallen und Netzwerk-Problemen zuerst das Netzteil austauschen. Vor allem dann, wenn die Netzwerk-Konfiguration schon mal funktioniert hat, und dann auf einmal nicht mehr.

Da der Raspberry Pi fur Embedded-Anwendungen oft ohne grafische Oberflache im Dauerbetrieb lauft und dazu ggf. Server-Dienste anbietet, sollte er auch eine statische IP Adresse im Netzwerk erhalten. Per Default bezieht er seine IP-Adresse automatisch per DHCP (Dynamic Host Configuration Protocol) - beispielsweise vom heimischen DSL-Router. Die so erhaltene IP-Adresse gibt der Raspberry Pi beim Booten preis (siehe Eintrag in der Datei /etc/rc.local). Die IP-Adresse konnen Sie aber auch mit den Kommandos ip oder ifconfig herausfinden:
    
    
    ip addr
    
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
        link/ether b8:27:eb:aa:37:2f brd ff:ff:ff:ff:ff:ff
        inet 172.20.1.99/24 brd 172.20.1.255 scope global eth0
    

Die per DHCP zugewiesene IP-Adresse des Pi lautet also 172.20.1.99. Bei diesem Beispiel und auch bei den folgenden haben alle System im lokalen Netz Adressen aus dem Bereich 172.20.1.x. Die Parameter und Adressen der Beispiele mussen Sie naturlich Ihrem eigenem Netzwerk anpassen.

## Initiale IP-Adresse

Wenn Sie den Raspberry Pi erstmals im Netz ohne Tastatur und Bildschirm betreiben, konnen Sie ihn ja nur per SSH von einem anderen Rechner aus ansprechen. Normalerweise ist er so eingestellt, dass er seine IP-Adresse automatisch per DHCP vom Router bezieht. Normalerweise hat jeder Router einen DHCP-Server aktiviert (daruber wird jedem Gerat die Netzwerkeinstellungen automatisch zugewiesen). Je nachdem, wie groß der IP-Bereich des DHCP-Servers eingestellt ist, musste man dann erstmal nach dem Kleinen suchen. Manchmal kann man die vergebenen Adressen uber das Webinterface des Routers auslesen. Alternativ ginge das mittels ping-Kommando, ist aber ziemlich nervig.

Auf der Seite [RasPi_Install.html](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_Install.html) ist beschrieben, wie man uber die Datei /boot/comdline.txt in der vFat-Partition der SD-Karte dem Raspberry Pi eine initiale IP-Konfiguration mitgeben kann. Danach bekommt er dann per SSH eine statische IP-Adresse wie unten beschrieben.

## Statische Netzwerkadresse vergeben

Um eine statische Adresse festzulegen, offnen Sie als root-User die Datei /etc/network/interfaces. Sie hat zwei Eintrage:
    
    
    auto lo
    iface lo inet loopback
    
    auto eth0
    iface eth0 inet dhcp
    

Der erste Eintrag ist fur das Loppback-Interface (localhost) und bleibt unberuhrt. Um der Ethernetschnittstelle eth0 nun die IP-Adresse 172.20.1.99 zuzuweisen, andern Sie den Inhalt der Datei folgendermaßen:
    
    
    # das loopback-Interface
    auto lo
    iface lo inet loopback
    
    # eigente Netzadresse
    auto eth0
    iface eth0 inet static
    address 172.20.1.99
    netmask 255.255.255.0
    broadcast 172.20.1.255
    # das eigene Netz
    network 172.20.1.0
    gateway 172.20.1.254
    # dns-* options are implemented by the resolvconf package, if installed
    dns-nameservers 172.20.1.254
    

Die unter "gateway" angegebene Adresse ist die IP-Adresse des ROuters, der in die große, weite Welt des Internets fuhrt. Damit die Änderungen wirksam werden, muss der Raspberry Pi nicht extra neu gestartet werden (wie man oft lesen kann). Es genugt das Kommando (als root):
    
    
    /etc/init.d/networking restart
    

Sollten Sie die Arbeiten uber SSH erledigt haben, fliegen Sie nun raus, weil der Raspberry Pi ja eine neue IP-Adresse bekommt. Sie mussen sich also wieder einloggen - diesmal mit der neuen Adresse.

Wenn das Paket "resolvconf" installiert ist, sorgt die letzte Zeile auch fur den Eintrag des DNS-Servers in der Datei /etc/resolv.conf, andernfalls mussen Sie das selbst durch Editieren der Datei erledigen. Der Eintrag ist ganz einfach:

Prinzipiell konnen Sie beliebig viele Adressen von DNS-Servern angeben. Im Beispiel habe ich noch die Adresse des Google-Nameservers hinzugefugt (was zweischneidig ist, denn oft wird diese Adresse auch von Malware verwendet, um festzustellen, ob der Trojaner etc. ins Internet kommt).

Wenn Sie gerade dabei sind, konnen Sie dem Pi auch noch einen neuen Namen verpassen. Der wird einfach in der Datei /etc/hostname eingetragen. Der gleiche Name muss auch noch in die Datei /etc/hosts eingetragen werden. Die Default-Datei hat folgenden Inhalt:
    
    
    ::1 raspberry localhost6.localdomain6 localhost6
    127.0.1.1 raspberry
    
    
    127.0.0.1 localhost
    ::1 localhost ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
    

Dort ersetzen Sie den Namen "raspberry" durch Ihren Wunschnamen. Sie konnen auch noch eine Domain hinzufugen und weitere Systeme eintragen. Wenn all Ihre Raspberrys die gleiche -Datei haben, konnen Sie sich gegenseitig nicht nur bei der IP-Adresse, sondern auch beim Namen rufen. Im folgenden Beispiel ist auch die statische IP-Adresse erfasst:
    
    
    127.0.0.1    localhost
    127.0.1.1    pipibox
    172.20.1.99  pipibox pipibox.local
    172.20.1.88  www     www.local
    
    ::1 pipibox localhost6.localdomain6 localhost6
    ::1 localhost ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
    

Im Beispiel wird bei den IP-Adresse 172.20.1.x nicht nur der Name, sondern auch ein Domainname eingetragen (es sind ubrigens auch mehrere Namen fur eine IP-Adresse moglich). Wenn Sie keine eigene Domain besitzen, kommen folgende Top-Level-Domains in Frage:

  * example: reserviert fur Beispiele (z. B. in Buchern) 
  * invalid: reserviert fur offensichtlich ungultige Dateinamen 
  * test: reserviert fur Tests 
  * local: Pseudo-TLD fur Link-lokale Namen 
  * dd: Lander-TLD der DDR (Verwendung ohne Gewahr) 

## WLAN einrichten

### WLAN bei den Modellen 2 mit WLAN-Stick

Das Einbinden des Raspberry Pi ins WLAN kann mehr oder weniger aufregend sein - je nachdem, welchen WLAN-Stick Sie verwenden ist die Einrichtung einfach oder kompliziert. Der Grund dafur liegt in den unterschiedlichen Chipsatzen der WLAN-Sticks. Überall empfohlen wird der WLAN-Stick von Edimax, der EDIMAX EW-7811UN Wireless USB Adapter, 150 Mbit/s, IEEE802.11b/g/n. Er wird von Raspbian automatisch erkannt und eingebunden, da der Kernel den passenden Treiber (RTL8192CU) bereits mitbringt.

Sobald der Stick eingesteckt wurde, wird er von Raspbian auch schon erkannt. Dies kann mit dem Befehl dmesg uberpruft werden. Sie sollten sehen, dass ein WLAN-Adapter von Realtek erkannt wurde und der passende Treiber (rtl8192cu) geladen wurde:
    
    
    [  124.008618] usb 1-1.2: New USB device found, idVendor=7392, idProduct=7811
    [  124.008653] usb 1-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [  124.008672] usb 1-1.2: Product: 802.11n WLAN Adapter
    [  124.008692] usb 1-1.2: Manufacturer: Realtek
    [  124.008709] usb 1-1.2: SerialNumber: 00e04c000001
    [  124.397563] usbcore: registered new interface driver rtl8192cu
    

Nachdem der Stick erfolgreich erkannt wurde, taucht auch ein neues Netzwerk-Device namens "" auf. Das konnen Sie mittels uberprufen. Dabei sehen Sie auch, dass dem Interface noch keine IP-Adresse zugeteilt wurde:
    
    
       ...
    
    wlan0     Link encap:Ethernet  Hardware Adresse 80:1f:02:e1:81:e8
              UP BROADCAST MULTICAST  MTU:1500  Metrik:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              Kollisionen:0 Sendewarteschlangenlänge:1000
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
    

Gegebenenfalls sollten Sie die Stromsparfunktion des Edimax-Treibers deaktivieren. Sonst kann es geschehen, dass eine Verbindung bei Inaktivitat unterbrochen wird. Dazu legen Sie eine Konfigurationsdatei fur den Treiber an. In die Datei wird die folgende Zeite geschrieben:
    
    
    options 8192cu rtw_power_mgnt=0 rtw_enusbss=0
    

Danach muss wieder mal die Datei bearbeitet werden. Statt ist diesmal dran:
    
    
    auto lo
    iface lo inet loopback
    iface eth0 inet dhcp
    
    auto wlan0
    iface wlan0 inet dhcp
    allow-hotplug wlan0
    wpa-ap-scan 1
    wpa-scan-ssid 1
    wpa-ssid "NAME-DES-WLAN"
    wpa-psk "DER-GEHEIME-WLAN-KEY"
    

Naturlich konnte auch hier eine statische Adresse vergeben werden. Das lauft dann genauso ab, wie oben bei der -Adresse.
    
    
    auto lo
    iface lo inet loopback
    
    iface eth0 inet static
    address 172.20.0.2
    netmask 255.255.255.0
    gateway 172.20.0.1
    
    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet static
    address 172.20.0.3
    netmask 255.255.255.0
    gateway 172.20.0.1
    wpa-ap-scan 1
    wpa-scan-ssid 1
    wpa-ssid "NAME-DES-WLAN"
    wpa-psk "DER-GEHEIME-WLAN-KEY"
    

Der WPA-Supplicant ist eine Software, die das Einrichten unterschiedlicher WLAN-Zugange vereinfachen will. Hier werden alle WLAN-spezifischen Daten in eine Konfigurationsdatei geschrieben und nicht in die Datei /etc/network/interfaces. Dort steht dann nur eine Zeile zusatzlich:
    
    
    auto wlan0
    iface wlan0 inet dhcp
            wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    

Wer diese Features verwenden will, sollte die [Anleitung bei Ubuntu](http://wiki.ubuntuusers.de/WLAN/wpa_supplicant) durcharbeiten.

### WLAN beim Modell 3

Das Modell 3 besitzt WLAN im 2,4 MHz-Band (und Bluetooth) on Bord uber den Broadcom-Chip BCM43438. Die Einrichtung erfolgt fast genauso, wie oben beschrieben - nur dass kein WLAN-Stick benotigt wird. Die Anbindung des WLAN-Moduls erfolgt nicht uber USB, sondern uber den SDIO-Input. Das WLAN-Modul benotigt bei der Einrichtung auch keine Extra-Treiber, es ist lediglich der Energiesparmodus zu beachten.

Auf der Platinenunterseite des Raspberry Pi 3 ist ein Lotpad fur eine UF.L-Antennenbuchse (Miniatur-Antennenstecker) vorgesehen (J 13). Das ist z. B. wichtig, wenn das Board in einem Metallgehause landet, das die Funksignale abschirmt. Dann kann man die Antenne nach aussen verlegen.

![](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi3_wlan.jpg)

Die aktuellen Raspian-Versionen ab Release 2016-02-26 unterstutzen den WLAN-Chip. Der Raspberry Pi sollte fur die Konfiguration entweder per Ethernet mit dem Netz verbunden werden, damit sich eine SSH-Verbindung aufbauen lasst, oder er kann mit einem Monitor, Maus und Tastatur bedient werden.

Mit dem Befehl ifconfig -a uberprufen Sie zunachst, ob der interne WLAN-Adapter des Raspberry Pi 3 von Raspbian erkannt wurde und betriebsbereit ist. In der Ausgabe mußte ein Netzwerk-Device namens "wlan0" auftauchen,das Onboard-WLAN des RasPi. Sollte neben "lo" und "eth0" kein weiteres Netzwerk-Device auftauchen, mussen Sie das Raspbian-Betriebssystem aktualisiert und dann den Rechner neu starten. Nach dem Neustart sollte die interne Wlan-Schnittstelle dann verfugbar sein. Der Update erfolgt mit der Kommandofolge:
    
    
    sudo apt-get update
    sudo apt-get dist-upgrade
    sudo shutdown -r now
    

Standardmaßig sind beim Raspberry Pi 3 die WLAN-Kanale 12 und 13 deaktiviert, da diese in den USA nicht zugelassen sind. Um dies zu andern, mussen Sie die landerspezifischen Einstellungen anpassen. Das Konfigurationswerkzeug raspi-config enthalt bereits einen entsprechenden Menupunkt (Internationalisation Options -> Change Wi-Fi Country), so dass der Landercode problemlos angepasst werden kann. In Deutschland sollte die Einstellung "DE Germany" lauten.

![](http://www.netzmafia.de/skripten/hardware/RasPi/WLAN3-1.gif)

![](http://www.netzmafia.de/skripten/hardware/RasPi/WLAN3-2.gif)

Danach checken Sie, welche Netzwerke in Reichweite sind. Die Netzwerke sind absteigend nach Signalstarke geordnet und jeweils in der Zeile mit "ESSID" befindet sich der Netzwerkname, den Sie in den kommenden Schritten benotigen. Den WLAN-Scan fuhren Sie mit dem folgenden Kommando durch:
    
    
    sudo iwlist wlan0 scan
    

Nun sind die Vorarbeiten erledigt.

Nun muss fur das gewunschte WLAN der geheime Schlussel hinterlegt werden. Dieser Eintrag erfolgt am Ende der Datei /etc/wpa_supplicant.conf. Solche Eintrage konnen dort auch mehrfach hinterlegt werden, falls mehrere WLANS gespeichert werden sollen. Der Eintrag lautet (SSID = WLAN-Name, PSK = WLAN-Passwort):
    
    
    network={
        ssid="MeinWLAN"
        psk="DasGeheimeWlanPasswort"
        key_mgmt=WPA-PSK
    }
    

Abschließend werden die Änderungen der Datei gespeichert und der kompletten Netzwerkdienst neu gestartet:
    
    
    sudo service networking restart
    

Alternativ (z. B. wenn Sie per SSH am RasPi eingeloggt sind) konnen Sie das WLAN am Raspberry Pi erst deaktivieren und anschließend wieder aktivieren:
    
    
    sudo ifconfig wlan0 down
    sudo ifconfig wlan0 up
    

Damit ist die Einrichtung der WLAN-Verbindung abgeschlossen. Das System sollte nach einem Neustart der Netzwerkfunktionen (s. o.) automatisch eine Verbindung zum konfigurierten WLAN aufbauen und sich via DHCP eine IP-Adresse vom Router holen.

Wichtig ist, dass fur die Dauer der Aktivierung des WLAN-Moduls dessen Energiesparmodus deaktiviert ist, da es sonst vorkommen kann, dass sich der Raspberry Pi vom Netzwerk trennt. Um das zu erreichen, fugen wir folgende zwei Zeilen am Ende der WLAN-Definition in der Datei /etc/network/interfaces ein:
    
    
    pre-up iw dev wlan0 set power_save off
    post-down iw dev wlan0 set power_save on
    

Soll der WLAN-Schnittstelle eine statische IP-Adresse im Netz zugewiesen werden, muss der Inhalt der Datei /etc/network/interfaces geandert werden. Innerhalb der Datei findet man den Eintrag zum WLAN-Interface wlan0 der z. B. folgendermaßen lautet:
    
    
       .
       .
       .
    iface wlan0 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
       .
       .
       .
    

Dieser Eintrag wird nun folgendermaßen geandert (die angegebenen IP-Adressen ersetzen Sie durch jene Ihres Netzes):
    
    
       .
       .
       .
    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet static
    address 10.10.10.252
    netmask 255.255.255.0
    gateway 10.10.10.254
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    
    pre-up iw dev wlan0 set power_save off
    post-down iw dev wlan0 set power_save on
       .
       .
       .
    

### Hostnamen andern

Grundsatzlich sollte man das Tool raspi-config zum Ändern des Hostnamens verwenden. Es gibt in der Regel vier Dateien, in denen der Hostname eingetragen sein kann:
    
    
    /etc/hostname
    /etc/mailname
    /etc/hosts
    /etc/resolv.conf (selten)
    

Die Dateien lassen sich mit einem Editor andern, die zusatzlich mit dem Kommando . Zum Ändern des Hostnamens mussen alle Dateien aktualisiert werden. Wenn Sie die Änderung irgendwo vergessen, erscheinen Fehlermeldungen wie "Hostname xyz kann nicht aufgelost werden" oder "unable to resolve host xyz". In der Datei kann der Hostname (z. B. "himbeere") durch die folgende Zeile am Ende der Datei eingetragen werden:
    
    
    127.0.1.1  himbeere
    

### Routing prufen

Funktioniert das lokale Netz (uberprufen mit dem -Kommando), gibt es aber keine Verbindung zum Internet, kann es am Routing liegen. Das sogenannte Standard-Gateway ist in einem Netz der Router in das Internet - also die Netzkomponente, die haufig vom Internet-Provider zur Verfugung gestellt wird. Die Verbindung ins Internet ist nur dann moglich, wenn ein Host die IP-Adresse des Standard-Gateways kennt. Überprufen konnen Sie dies mit dem - oder -Kommando:
    
    
    $ route -n
    Kernel-IP-Routentabelle
    Ziel            Router          Genmask         Flags Metric Ref    Use Iface
    0.0.0.0         10.27.1.1       0.0.0.0         UG    0      0        0 eth0
    10.10.0.0       0.0.0.0         255.255.0.0     U     0      0        0 eth0
    10.27.0.0       0.0.0.0         255.255.0.0     U     0      0        0 eth0
    
    $ netstat -r
    Kernel-IP-Routentabelle
    Ziel            Router          Genmask         Flags   MSS Fenster irtt Iface
    default         10.27.1.1       0.0.0.0         UG        0 0          0 eth0
    10.10.0.0       *               255.255.0.0     U         0 0          0 eth0
    10.27.0.0       *               255.255.0.0     U         0 0          0 eth0
    

Die Standard- bzw. Default-Route (die immer dann gilt, wenn der Host die Route zur Ziel-Adresse nicht kennt) ist in der aufgelisteten Routing-Tabelle daran zu erkennen, dass sie mit "0.0.0.0" oder "default" beginnt. Gibt es keine Zeile mit "0.0.0.0" oder "default" oder ist hier eine falsche IP-Adresse eingetragen, wird in der Regel keine Verbindung ins Internet moglich sein. Der Grund fur das Fehlen des Standard-Gateways ist eine unvollstandige bzw. fehlerhafte manuelle IP-Konfiguration - oder es fand uberhaupt keine IP-Konfiguration statt.

Enthalt die Tabelle eine Standard-Route, entspricht die angegebene IP-Adresse der des Standard-Gateways und es ist trotzdem keine Internet-Verbindung moglich, hat das Standard-Gateway moglicherweise keine Verbindung zum Internet oder es ist ausgeschaltet. Das kann man mit einem Ping auf das Standard-Gateway klaren. Ist das Standard-Gateway selbst erreichbar, dann stimmt zumindest die Konfiguration bezuglich des Standard-Gateways. Zum Test kann man eine Route auch manuell eintippen:
    
    
    sudo route add default gw 10.27.1.1
    

### Netzwerk einrichten ab Raspbian "Jessie"

Mit dem Release von "Jessie" wird Debian um das Startsystem systemd erweitert, was sich nicht nur auf etliche Systemdienste, sondern auch auf die Netzwerkkonfiguration auswirkt. Rein prinzipiell konnen Sie das Netz wie oben beschrieben uber die Datei /etc/network/interfaces einrichten und das Netz uber das Script im Verzeichnis /etc/init.d nach bisheriger System-V-Tradition starten. Ab der Version "Jessie" der Debian/Raspbian-Distribution eroffen sich aber zwei neue Moglichkeiten. Es kann trotzdem Grunde dafur geben, dass Sie weiterhin die IPv4-Konfiguration uber die Datei /etc/network/interfaces vornehmen wollen. Dann mussen Sie aber auch den dhcpcd-Daemon außer Betrieb nehmen, wie es im folgenden Abschnitt geschildert wird.

#### Netzwerkkonfiguration uber dhcpcd

Raspbian verwendet fur die Netzwerkkonfiguration auch bei der Vergabe statischer Adressen den DHCP-Client-Dienst , der zum Problem werden kann, wenn man die IPv4-Konfiguration auf diese Weise vornimmt. Eignetlich ist er nur bei komplexen Anwendungen notwendig.

Wenn man diesen DHCP-Client definitiv nicht braucht, dann sollte man ihn deaktivieren. Entweder man schaltet den Daemon aus (empfohlen). Bei Raspbian Wheezy:
    
    
    sudo service dhcpcd stop
    sudo update-rc.d -f dhcpcd remove
    

Bei Raspbian Jessie: pre> sudo service dhcpcd stop sudo systemctl disable dhcpcd Wenn man radikal sein will, dann entfernt man den komplett:
    
    
    sudo service dhcpcd stop
    sudo apt-get remove dhcpcd5
    

Um die Änderungen zu ubernehmen, folgt hier ein Reboot.

Wollen Sie den DHCPCD nicht deaktivieren, weil er fur ein bestimmtes Interface benotigt wird, konnen Sie die Konfiguration durch den dhcpcd fur ein bestimmtes Interface ausschließen. Dazu tragen Sie in die Konfigurations-Datei /etc/dhcpcd.conf eine Zeile ein, die das Interface von der Konfiguration durch den dhcpcd ausschließt, z. B.:
    
    
    denyinterfaces eth0
    

Diese Zeile klammert das betreffende Interface aus der Netzwerk-Konfiguration aus. Die Netzwerk-Konfiguration fur dieses Interface muss dann in der Datei erfolgen.

Alternativ konnen Sie die IPv4-Konfiguration aber auch komplett in den dhcpcd verlagern. Ab "Jessie" verwendet Raspbian fur die Netzwerkkonfiguration auch bei der Vergabe statischer Adressen den DHCP-Client. Zuvor sollten Sie feststellen, ob der "hcpcd uberhaupt aktiv ist.
    
    
    sudo service dhcpcd status
    

Zeigt der Status einen installierten, aber abgeschalteten an, mussen Sie diesen einschalten. Erst dann konnen Sie die Konfiguration vornehmen.
    
    
    sudo service dhcpcd start
    sudo systemctl enable dhcpcd
    

Fur die Ethernet-Schnittstelle erzwingen Sie mit den folgenden Zeilen eine feste IP-Adresse. Dazu hangen Sie die Angaben an die vorhandene Datei an. Die IP-Adressen sind nur beispielhaft; Sie mussen diese an Ihr Netz anpassen. Bei der Vergabe der IP-Adresse achten Sie darauf, solche Adressen zu wahlen, die bis dahin _nicht_ verwendet werden und sich auch nicht im Adress-Pool eines DHCP-Servers befinden. Sonst kommt es zu Verbindungsproblemen im Netz.
    
    
    interface eth0
    
    static ip_address=10.10.0.10/24
    static routers=10.10.0.1
    static domain_name_servers=10.10.0.1
    
    interface wlan0
    
    static ip_address=10.10.0.11/24
    static routers=10.10.0.1
    static domain_name_servers=10.10.0.1
    

Die Angabe "/24" hinter der IP-Adresse ist eine Verkurzte Angabe der Netzmaske. Sie besagt, dass von den 32 Bit der IP-Adresse 24 Bit dem Netzwerk zugeordnet sind. Das entspricht der Netzmaske 255.255.255.0 (also ein C-Netz).

**Wichtig:** Die Konfiguration in der Datei /etc/network/interfaces muss wieder in den Ursprungszustand versetzt werden:
    
    
    # Please note that this file is written to be used with dhcpcd
    # For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
    # Include files from /etc/network/interfaces.d:
    source-directory /etc/network/interfaces.d
    
    auto lo
    iface lo inet loopback
    
    iface eth0 inet manual
    
    allow-hotplug wlan0
    iface wlan0 inet manual
       wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    
    allow-hotplug wlan1
    iface wlan1 inet manual
       wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    

Um die Änderungen zu ubernehmen, folgt auch hier ein Reboot.

Stort Sie nicht, dass mit dem dhcpcd ein zusatzlicher Dienst lauft, und haben Sie auch keine weiteren Anforderungen an die Netzwerkkonfiguration, konnen Sie es bei den oben beschriebenen Änderungen belassen. Übrigens erzeugt der dhcpcd beim Booten eine langere Wartezeit, wenn kein Netz zur Verfugung steht. Man kann die Wartezeit verkurzen, indem man in der Datei /etc/dhcpcd.conf die folgende Zeile eintragt (Angabe in Sekunden):
    
    
    timeout 5
    

#### Netzwerk-Konfiguration uber Systemd

Eine saubere Konfiguration, die auch auf weiteren Linux-Systemen bzw. bei spateren Versionen des Raspian funktioniert, ermoglicht jedoch erst ein Umstieg auf die Dienste von Systemd. Systemd ist inzwischen auf vielen Linux-Systemen fur den Bootvorgang und die damit einhergehenden Initialisierungen aller Dienste verantwortlich. Das bisherige SysV-Init erledigte alle Aufgaben immer nacheinander. Das stellte sicher bei den fruhen UNIX- und Linux-Systemen kein Problem dar, weil nur relativ wenige Dinge zu initialisieren und starten waren. Auch konnte die Reihenfolge der Startscripte recht einfach deterministisch festgelegt werden. Inzwischen ist der Startvorgang aber immer vielschichtiger und komplexer geworden. Systemd versucht maximale Parallelisierung der Startprozesse und erreicht damit sehr schnelle Boot-Zeiten. Zum Systemd gibt es viele Infos und Tutorials im Netz (siehe Links am Ende des Textes).

Der erste Schritt zu einer sauberen Netzwerkkonfiguration besteht darin, alle Dienste zu entfernen, die hier Probleme bereiten konnten. Man sollte die Umstellung auf systemd-networkd auch nicht per SSH machen. Falls es dabei eine Unterbrechung der Verbindung geben sollte, bekommt man die Verbindung ggf. nicht wieder aufgebaut. Alle folgenden Arbeiten werden als Administrator (root) ausgefuhrt (-> sudo su).

Zuerst prufen Sie, ob der Dienst systemd-networkd vorhanden ist. Das ist die Voraussetzung fur alle weiteren Arbeiten. Ab Raspbian Jessie sollte das funktionieren. Der Dienst fur die Namensauflosung, systemd-resolved, sollte ebenfalls verfugbar sein.
    
    
    systemctl status systemd-networkd
    systemctl status systemd-resolved
    

Beidesmal sollte dort "Loaded: loaded" gemeldet werden.

Zunachst werden die alten Network- oder Networking-Komponenten zumindest deaktiviert. Deinstallation und Loschen empfiehlt sich nicht, weil man sonst nur schwer wieder auf den alten Zustand zuruckkehren kann (wobei man den dhcpcd loschen kann, falls er nicht gebraucht wird).
    
    
    # dhcpcd stoppen und loeschen
    systemctl stop dhcpcd
    systemctl disable dhcpcd
    apt-get -y remove dhcpcd5 openresolv
    
    # SysV-Networking stoppen
    systemctl disable networking.service
    # bzw.  update-rc.d networking remove
    # falls der Netzwork Manager laeuft:
    systemctl disable NetworkManager
    

In den Status-Zeilen "Loaded: loaded" sollte hinten "enabled" stehen.

Damit sind die Vorarbeiten abgeschlossen. Nun geht es darum, eine Netzwerk-Konfiguration anzulegen. Diese kann auf mehrere Dateien verteilt sein, die sich alle im selben Verzeichnis befinden. Um Netzwerkgerate mit systemd-networkd zu konfigurieren, mussen Sie die Informationen in Textdateien mit der Endung ".network" ablegen. Diese Konfigurationsdateien werden dann im Verzeichnis /etc/systemd/network gespeichert. Wenn mehrere Dateien, die auf ".network" enden, ladt und verarbeitet sie der Systemd nacheinander in lexikalischer Reihenfolge. Sie konnen also ahnlich wie bei den Prafixen der SysV-Init-Links die Reihenfolge durch den Namen festlegen. Beachten Sie, dass Systemd-Dienstdateien auch unterhalb des Verzeichnisses /usr/lib/systemd/ liegen konnen. Die Dateien in /etc/systemd/ habe jedoch hohere Prioritat.

Ist das Verzeichnis /etc/systemd/network/ leer, konnen Sie es einfach anlegen. Gibt es das Verzeichnis dagegen schon, informieren Sie sich uber die Namen der bereits vorhandenen Dateien - gegebenenfalls konnen sie eine bereits vorhandene Datei andern. Sonst legen Sie fur jedes Inrerface eine neue Datei an. Der Dateiname ist dabei relativ egal. Er muss nur auf ".network" enden. Trotzdem empfiehlt es sich, sinnvolle Dateinamen zu wahlen, um sich im Fehlerfall oder bei spateren Änderungen leichter zurecht zu finden. Derzeit gibt es drei Arten von Konfigurationsdateien: ".link", ".network" und ".netdev".

Angenommen, das Device "eth0" soll mit einer statischen IP-Adresse ans Netz. Dann erstellen Sie eine neue Datei, z. B. eth0.network, und tragen dort die Konfiguration ein:
    
    
    # Fuer was soll die Konfiguration vorgenommen werden?
    [Match]
    # Wildcards sind möglich! "Name=eth*" für die gleichzeitige Konfiguration vieler 
    # Interfaces waere denkbar, ist aber nur selten sinnvoll
    Name=eth0
    
    [Network]
    # Die Netzwerkkonfiguration
    Description=RasPi eth0 static
    Address=10.10.0.10/24
    Gateway=10.10.0.1
    DNS=10.10.0.1
    

Alternativ: Eintrag fur eine IP-Konfiguration mit DHCP:
    
    
    [Match]
    Name=wlan0
    
    [Network]
    Description=RasPi wlan0 dhcp
    DHCP=yes
    

Das ist eigentlich schon alles. Im Verzeichnis /etc/systemd/network/ sind außer den ".network"-Dateien wie oben erwahnt auch noch ".netdev"\- und ".link"-Dateien moglich. ".link"-Dateien beschreiben Eigenschaften eines Netzwerkgerates, etwa MAC-Adresse, Duplex-Modus etc. Normalerweise sind sie nicht notwendig. ".link"-Dateien enthalten einen [Match]-Block, in dem die Eigenschaften des Netzwerk-Devices festgelegt werden. Streng genommen sind diese Dateien nicht Teil des networkd, sondern eine Erganzung fur udev. Sie bieten eine einfache und selbsterklarende Syntax anstelle der Regeln fur die komplexe Syntax und Logik von udev. Zum Beispiel wird ein Interface auf eine MTU von 1500 Bytes, Full Duplex Gigabit und Wake-on-LAN gesetzt:
    
    
    [Match]
    MACAddress=A8:30:44:33:11:22
    
    [Link]
    MTUBytes=1500
    BitsPerSecond=1G
    Duplex=full
    WakeOnLan=magic
    

".netdev"-Dateien erstellen virtuelle Gerate, z. B. Bridges, VLANs etc.

In einigen Fallen muss auch noch ein neuer Service eingefuhrt werden, z. B. beim Wake-on-LAN (WOL), wo das Interface noch fur WOL freigegeben werden muss. Das ist dann aber schon Standard-Systemd-Steuerung. Trotzdem gestalt sich der Service recht einfach und selbsterklarend. Die Datei /etc/systemd/system/wol@.service lautet:
    
    
    [Unit]
    Description=Wake-on-LAN for %i
    Requires=network.target
    After=sys-subsystem-net-devices-%i.device
    
    [Service]
    ExecStart=/usr/sbin/ethtool -s %i wol g
    Type=oneshot
    
    [Install]
    WantedBy=multi-user.target\
    

Doch zuruck zur Basisinstallation. Nach dem Erstellen der Konfigurationsdatei(en) werden die Netzdienste gestartet:
    
    
    # Systemd-Netzwerkdienst starten
    systemctl enable systemd-networkd.service
    systemctl start systemd-networkd.service
    
    # Prüfen, ob der Dienst laeuft:
    systemctl status systemd-networkd
    

Der Parameter "enable" aktiviert den Systemd-Netzwerkdienst dauerhaft, so dass er bei jedem Bootvorgang gestartet wird. "start" startet den Dienst aktuell. Mit den Kommandos oder kann nun uberpruft werden, ob die Netzwerk-Konfiguration geklappt hat.

Den Zugang zum WLAN regelt nach wie vor das Programm wpa_supplicant. Damit das Programm schon aktiv ist, wenn das Netzwerk startet, erstellen Sie zuerst die Konfigurationsdatei /etc/wpa_supplicant/wpa_supplicant-wlan0.conf (die zweite Datei nenen Sie dann /etc/wpa_supplicant/wpa_supplicant-wlan1.conf usw.). In der Datei konnen Sie beliebig viele WLANs definieren; das Programm wahlt automatisch aus den verfugbaren WLANs das Netz mit der hochsten Prioritat aus. Der Inhalt der Datei lautet:
    
    
    ctrl_interface=/var/run/wpa_suppticant
    eapol_version=l
    ap_scan=1
    fast_reauth=l
    
    network={
      ssid="das_wlan"
      psk="GeheimesPasswort"
      priority=l
    }
    
    network={
      ssid="anderes_wlan"
      psk="AnderesGeheimesPasswort"
      priority=2
    }
    

Des Weiteren brauchen Sie einen Dienst, der fur die Schnittstelle startet. Dazu erstellen Sie die Datei mit der Service-Definition. Es handelt sich um einen generischen Dienst, dessen Enable- und Startkommando das folgende Listing zeigt:
    
    
    [Unit]
    Descriptiom=WPA supplicant daemon
    Before=network.target
    Wants=network.target
    
    [Service]
    type=simple
    ExecStart=/sbin/ip l set %i up
    ExecStart=/sbin/wpa_supplicant -B -i %i -c /etc/wpa_supplicant/wpa_supplicant-%i.conf
    ExecStop=/usr/sbin/ip link set dev %i down
    
    [Install]
    Alias='multi-user.target.wants/wpa_supplicant@%i.service
    

Dann muss dieser Dienst noch dauerhaft eingebunden und gestartet werden:
    
    
    systemctrl enable wpasupplicant@wlan0.service
    systemctrl start wpasupplicant@wlan0.service
    

Im Anschluss an diese Arbeiten sollte auch das WLAN nach dem Booten bereitstehen.

#### DNS-Konfiguration uber Systemd

Nun muss noch der DNS-Dienst systemd-resolved konfiguriert werden. Die Datei /etc/resolv.conf wird vom networkd nicht verwendet. Stattdessen kommt der Dienst resolved zum Einsatz, der eine dynamische Variante der Datei generiert. Zum Aktivieren sind folgende Kommandos notwendig:
    
    
    # DNS-Dienst systemd-resolved aktivieren und starten:
    systemctl enable systemd-resolved.service
    systemctl start systemd-resolved.service
    
    # Prüfen, ob der Dienst laeuft:
    systemctl status systemd-resolved
    

In der Status-Zeile "Loaded: loaded" sollte hinten "enabled" stehen.

Einmal gestartet, erstellt der Systemd seine eigene Datei resolv.conf unterhalb von /run/systemd. Es ist jedoch ublich, DNS-Resolver-Informationen in der Datei /etc/resolv.conf zu speichern, und viele Anwendungen verlassen sich immer noch auf diese Datei. Fur die Kompatibilitat erstellen Sie einen symbolischen Link zu /etc/resolv.conf:
    
    
    mv /etc/resolv.conf /etc/resolv.conf.ORIG 
    ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf
    

Die Konfiguration erfolgt durch Bearbeiten der Datei /etc/systemd/resolved.conf. Dort genugt ein Eintrag:
    
    
    [Resolve]
    DNS=10.10.10.1 8.8.8.8
    

Alle hier definierten DNS-Server liegen in ihrer Prioritat hinter denen, die in einer ".network"-Datei festgelegt wurden. Die Eintrage werden jedoch als alternative Nameserver verwendet (8.8.8.8 ist ubrigens die Adresse des Google-Nameservers). Dazu ein Beispiel: Es wird ein statischer DNS 192.168.127.1 in einer der ".network"-Dateien definiert. Ausserdem stehen die o. a. Server in der Datei . Insgesamt erhalt man dann die DNS-Server:
    
    
        192.168.127.1
        10.10.10.1
        8.8.8.8
    

Anschliessende den Dienst noch einmal neu starten:
    
    
    systemctl restart systemd-resolved.service
    

Übrigens: Wenn man einen Service aktiviert bzw. deaktiviert, konnte man den Zusatz ".service" ggf. auch weglassen. Systemd nimmt immer die Erweiterung ".service" an, wenn nichts weiter definiert wurde. Man findet derartig verkurzte Kommandos manchmal in irgendwelchen Anleitungen. Es ist trotzdem sinnvoll, wichtige Systemkommandos immer vollstandig anzugeben.

### Links

  * Systemd-Manualpages: [ https://www.freedesktop.org/software/systemd/man/](https://www.freedesktop.org/software/systemd/man/)
  * Systemd - Debian Wiki: [ https://wiki.debian.org/systemd](https://wiki.debian.org/systemd)
  * Systemd - freedesktop: [ http://freedesktop.org/wiki/Software/systemd/](http://freedesktop.org/wiki/Software/systemd/)
  * Networkd commits: [ http://lists.freedesktop.org/archives/systemd-commits/2013-November/004659.html](http://lists.freedesktop.org/archives/systemd-commits/2013-November/004659.html)
  * systemd-networkd: [ https://wiki.archlinux.org/index.php/Systemd-networkd#network_files](https://wiki.archlinux.org/index.php/Systemd-networkd#network_files)
  * Introduction to networkd: [ https://coreos.com/blog/intro-to-systemd-networkd/](https://coreos.com/blog/intro-to-systemd-networkd/)
  * Autorun a Python Script on Boot: [ http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/](http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)
  * Simple Systemd File: [ http://neilwebber.com/notes/2016/02/10/making-a-simple-systemd-file-for-raspberry-pi-jessie/](http://neilwebber.com/notes/2016/02/10/making-a-simple-systemd-file-for-raspberry-pi-jessie/)

_Copyright (C) Hochschule Munchen, FK 04, Prof. Jurgen Plate_  
Letzte Aktualisierung: 10/20/2016 13:15:01
