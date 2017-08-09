# Raspberry Pi 3 – Bluetooth verbinden 

_Captured: 2016-12-03 at 22:49 from [www.datenreise.de](https://www.datenreise.de/raspberry-pi-3-bluetooth-verbinden/)_

![Raspberry Pi 3 - Bluetooth verbinden](https://www.datenreise.de/wp-content/uploads/2016/03/raspberry_pi_bluetooth-636x310.jpg)

Der Raspberry Pi 3 bringt neben WLAN auch Bluetooth von Haus aus gleich mit. Das integrierte Bluetooth Modul erspart so den Kauf eines zusatzlichen Bluetooth-USB-Sticks. Nachfolgend erklare ich die einzelnen Schritte, wie eine Bluetooth-Verbindung auf der Konsole aufgebaut werden kann.

## Bluetooth-Verbindung einrichten

Um das integrierte Bluetooth-Modul des Raspberry Pi 3 verwenden zu konnen ist entweder das neueste Raspbian Image notwendig oder es sollte vorher ein Upgrade durchgefuhrt werden:
    
    
    $ sudo apt-get update
    $ sudo apt-get dist-upgrade
    $ reboot

#### Pairing

Damit zwei Gerate aneinander gebunden werden konnen, mussen diese einander zunachst bekannt gemacht werden. Bei neu zu konfigurierenden Bluetooth-Geraten muss dazu der Pairing-Knopf (z.B. bei Tastatur / Maus / etc.) gedruckt werden. Dadurch ist das Gerat bereit fur den Verbindungsaufbau und signalisiert diesen Zustand oftmals durch eine blinkende LED.

Das Pairing mit anderen Bluetooth-Geraten erfolgt uber den Befehl _bluetoothctl_. Nach dem Start gelangen wir in den Kommandomodus:
    
    
    $ sudo bluetoothctl

Zuerst aktivieren wir einen Bluetooth-Agenten, der sich um die Autorisierung neuer Gerate kummert. Mit dem Befehl _scan on_ konnen nun anschließend alle in Reichweite befindlichen Bluetooth-Gerate angezeigt werden:
    
    
    [bluetooth]# agent on
    [bluetooth]# default-agent
    [bluetooth]# scan on

![raspberry_bluetooth_scan](https://www.datenreise.de/wp-content/uploads/2016/03/raspberry_bluetooth_scan.jpg)

Mit dem Befehl _pair_, gefolgt von der MAC-Adresse des Gerates, kann nun der Verbindungsaufbau initiiert werden. Am zu verbindenden Gerat werden wir nun aufgefordert, den angezeigten PIN Code einzugeben:
    
    
    [bluetooth]# pair xx:xx:xx:xx:xx:xx

![raspberry_bluetooth_pairing](https://www.datenreise.de/wp-content/uploads/2016/03/raspberry_bluetooth_pairing.jpg)

#### Gerat vertrauen

Nach erfolgreicher Koppelung, sollten wir das Gerat noch als vertrauenswurdig markieren. Dadurch muss die Verbindung nicht jedes Mal wieder manuell durchgefuhrt werden (z. B. nach einem Neustart). Anschließend konnen wir das Bluetooth-Tool verlassen:
    
    
    [bluetooth]# trust xx:xx:xx:xx:xx:xx
    [bluetooth]# exit

**Artikel bewerten:**

4,59/5 (17 Bewertungen)

Raspberry Pi 3 - Bluetooth verbinden 4,59 out of 5 based on 17 ratings
