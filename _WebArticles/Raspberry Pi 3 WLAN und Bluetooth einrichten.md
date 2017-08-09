# Raspberry Pi 3 WLAN und Bluetooth einrichten 

_Captured: 2016-12-03 at 22:53 from [raspberry.tips](https://raspberry.tips/raspberrypi-tutorials/raspberry-pi-3-wlan-und-bluetooth-einrichten/)_

Der [Raspberry Pi](https://raspberry.tips/lexikon/raspberry-pi/) 3 hat nun ein WLAN Chip auf der Platine sodass kein USB Dongle fur WiFi mehr notwendig ist, der verbaute BCM43438 Chip beherrscht WLAN auf 2.4 GHz Basis nach IEEE 802.11 a/b/g/n, mit 150MBit Datenrate Brutto reicht die Geschwindigkeit des WLAN fur die meisten Bedurfnisse aus.

Um euch mit eurem WLAN zu verbinden benotigt ihr naturlich zwei Dinge, den Namen des Netzwerks (auch SSID genannt) und das entsprechende Passwort. Zusatzlich naturlich den Pi 3 mit aktuellem Raspbian Betriebssystem.

## WLAN einrichten uber den Desktop

Da Raspbian nach der Installation mittlerweile im Standard auf den Desktop bootet werden viele von euch diese Methode bevorzugen, [schreibt das aktuelle Raspbian Image also via Win32Disk Imager](http://raspberry.tips/raspberrypi-einsteiger/raspberry-pi-einsteiger-guide-vorbereitung-teil-2/) auf eure SD-Karte und startet den Pi mit angeschlossener Tastatur, Maus und Bildschirm.

Nach dem Starten landet ihr direkt auf dem Desktop, dort konnt ihr nun das WLAN Netzwerk einrichten. Klickt hierzu mit der **Maus auf das Netzwerksymbol** in der rechten oberen Ecke.

![raspberry pi wlan einrichten](https://cdn.raspberry.tips/2016/03/raspberry-pi-wlan-einrichten-300x195.png)

**Wahlt** dann aus der Liste mit verfugbaren WLAN -Netzwerken** euer Netz aus **

Gebt euer** Passwort (Pre Shared Key)** ein und bestatigt mit **OK**. Der Schlussel fur euer WLAN ist oft auf eurem Router aufgedruckt oder via Router Konfiguration einseh- und anderbar.

![raspberry pi netzwerkschluessel eigeben](https://cdn.raspberry.tips/2016/03/raspberry-pi-netzwerkschluessel-eigeben-300x225.png)

Wenn alles geklappt hat andert sich das Icon und zeigt euch die Signalstarke an, beim Mouseover erhaltet ihr detaillierte Informationen

![raspberry pi aktive wlan verbindung](https://cdn.raspberry.tips/2016/03/raspberry-pi-aktive-wlan-verbindung-300x183.png)

## WLAN einrichten mit der Kommandozeile

Die Einrichtung uber die Kommandozeile ist ebenfalls recht einfach:

  * oder verwendet einen beliebigen [SSH](https://raspberry.tips/lexikon/ssh/)-Client um das ganze uber eine bereits vorhandene LAN Verbindung zu konfigurieren (z.B. [Putty](http://www.putty.org/)) 

Scrollt ans Ende der Datei und gebt folgende Zeilen ein, andert folgendes:

  * NameDesNetzwerks -> Name eures WLANs, auch SSID genannt
  * PreSharedKey -> Den Schlussel fur euer Netz
  * WPA-PSK -> Die Methode mit welchem euer WLAN verschlusselt wird, meistens WPA-PSK. Bei anderen Verschlusselungen konnt ihr im [Ubuntu WiKi](https://wiki.ubuntuusers.de/WLAN/wpa_supplicant/) nachlesen.

Zum Speichern verwendet ihr die Tastenkombination **STRG+X**, mit **Y** Bestatigen und Enter. Jetzt kann die WLAN Verbindung aktiviert werden:  
Mit iwconfig konnt ihr euch anzeigen lassen ob die Verbindung geklappt hat

![raspberry pi iwconfig](https://cdn.raspberry.tips/2016/03/raspberry-pi-iwconfig.png)

## Wie aktiviere ich Bluetooth und verbinde Gerate?

Um Bluetooth verwenden zu konnen ist entweder das neueste [Raspbian Image](https://www.raspberrypi.org/downloads/raspbian/) notwendig oder ihr solltet vorher ein Upgrade durchgefuhrt haben. Zusatzlich benotigen wir etwas Software und einen Neustart

Ich verwende ein aktuelles [Bluetooth Keyboard](http://www.amazon.de/gp/product/B00DN4ZNU2/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00DN4ZNU2&linkCode=as2&tag=raspbertipps-21) fur meine Test.

Wie bei Bluetooth ublich mussen Gerate miteinender verbunden werden, die meisten Gerate haben hierfur einen "Connect" Button, auch mein Keyboard. Um alle in der nahe befindlichen Bluetooth Gerate anzuzeigen gebe ich in einem Terminal oder via SSH folgendes Kommando ein:

Wahrend der Scan Vorgang lauft solltet ihr den** Connect Button** an eurem Gerat drucken, bei mir werden zwei bereite Gerate gefunden.

**Notiert euch die Adresse** des Gerats, bei mir AA:00:00:00:AA:AA Wir offnen das Tool **bluetoothctl **um das Pairing mit dem Gerat zu starten

Wir machen noch einige Grundeinstellungen fur den Bluetooth Agent innerhalb von blietoothctl

Jetzt Verbinden wir die Gerate (u.U. musst ihr noch mal den Connect Butto drucken) mit dem folgenden Befehl. Ersetzt naturlich die Adresse mit der eures Gerats

![raspberry pi bluetooth pair](https://cdn.raspberry.tips/2016/03/raspberry-pi-bluetooth-pair.png)

Gebt an eurem Gerat den angezeigten PIN Code ein und bestatigt diesen (Bei meiner Tastatur mit Enter). Jetzt vertrauen wir dem Gerat noch mit:

![raspberry pi bluetooth trust](https://cdn.raspberry.tips/2016/03/raspberry-pi-bluetooth-trust.png)

> _Jetzt konnt ihr euer Gerat verwenden und bluetoothctl mit exit verlassen._

### Gepairte Gerate erneut Verbinden

Leider muss man u.U. das Gerat nach einem Reboot immer wieder Verbinden, das erledigen wir wieder mit

Listet euch alle bereits gepaarten Gerate auf (nur diese konnen wir ohne erneutes Pairing verbinden)

Jetzt konnen wir das Gerat wieder verbinden, ersetzt die Adresse durch eure.

Wie Gerate nach einem Reboot automatisch verbunden werden konnen zeige ich euch im nachsten Beitrag.
