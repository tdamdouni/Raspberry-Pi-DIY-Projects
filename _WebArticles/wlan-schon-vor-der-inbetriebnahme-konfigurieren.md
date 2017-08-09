# WLAN schon vor der Inbetriebnahme konfigurieren

_Captured: 2017-05-06 at 10:13 from [pi-buch.info](https://pi-buch.info/wlan-schon-vor-der-installation-konfigurieren/)_

Mitunter ist es praktisch, wenn Sie einen Raspberry Pi auf Anhieb uber das WLAN via SSH bedienen konnen. Das gibt Ihnen die Moglichkeit, ohne angeschlossene Maus und Tastatur mit der Konfiguration zu beginnen -- zumindest soweit, wie Sie dies via SSH im Textmodus durchfuhren konnen.

Dazu kopieren Sie das Raspbian- oder das Raspbian-Lite-Image wie ublich auf eine SD-Karte, z.B. mit dem Programm [Etcher](https://etcher.io). Danach platzieren Sie (noch auf Ihrem PC) in der Boot-Partition der SD-Karte zwei Dateien:

  * Die leere Datei `ssh` bewirkt, dass SSH sofort aktiviert wird. (Bei aktuellen Raspbian-Versionen ist dies ja nicht mehr der Fall.) 
  * Und die Datei `wpa_supplicant.conf` enthalt die WLAN-Konfiguration. Sie wird beim ersten Start des Raspberry Pi in das Verzeichnis `/etc/wpa_supplicant` kopiert. Die Datei muss die Bezeichnung des WLANs (SSID) und dessen Passwort enthalten. Dabei gilt dieser Aufbau.
    
    
    # Datei wpa_supplicant.conf in der Boot-Partition
    network={
           ssid="wlan-bezeichnung"
           psk="passwort"
           key_mgmt=WPA-PSK
    }
    

Sobald der Raspberry Pi hochgefahren ist, konnen Sie sich mit `ssh pi@raspberrypi` und dem Default-Passwort `raspberry` einloggen. **Anschließend mussen Sie sofort mit `sudo passwd pi` ein neues Passwort fur den Benutzer `pi` einrichten! Ein aktiver SSH-Server in Kombination mit dem Default-Passwort sind ein großes Sicherheitsrisiko!**

> **Nicht mit NOOBS:** Beachten Sie, dass diese Installationsvariante nicht mit NOOBS funktioniert. Sie mussen ein Raspbian-Image selbst auf die SD-Karte schreiben! 

### Quellen
