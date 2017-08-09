# Geänderte SSH-Server-Konfiguration von Raspbian

_Captured: 2017-05-06 at 10:14 from [pi-buch.info](https://pi-buch.info/geaenderte-ssh-server-konfiguration-von-raspbian/)_

Wenn Sie in der Vergangenheit Raspbian installierten, egal, ob mit NOOBS oder durch die direkte Übertragung des Raspbian-Images auf eine SD-Karte, war der SSH-Server standardmaßig aktiv. Jeder, der eine Netzwerkverbindung zum Raspberry Pi herstellen konnte, konnte sich als `pi` mit dem bekannten Passwort `raspberry` einloggen und hatte dann per `sudo` uneingeschrankte Rechte. Es wird naturlich uberall empfohlen (auch in allen Auflagen unseres Raspberry-Pi-Buchs), das Default-Passwort von `pi` sofort zu andern, aber wen kummern schon solche Empfehlungen :-(

Immer mehr Pis sind so in Netzwerke integriert, dass sie auch aus dem Internet erreichbar sind. Unter dem Eindruck der Sicherheitskatastrophen der letzten Monate (z.B. [Verwundbare Router](https://heise.de/-3519042) oder [Botnets aus gehackten Webcams](https://krebsonsecurity.com/2016/10/hacked-cameras-dvrs-powered-todays-massive-internet-outage/)) haben sich die Raspbian-Entwickler endlich zu ein klein wenig mehr Sicherheit per Default entschlossen: Bei aktuellen Raspbian-Images ist der SSH-Dienst zwar installiert, aber standardmaßig nicht aktiv. Wie Sie SSH weiterhin verwenden konnen, erklart dieser Beitrag.

### SSH-Server bei einer Desktop-Installation aktivieren

Um den SSH-Server bei einer Desktop-Installation zu installieren, fuhren Sie im Startmenu _Preferences / Raspberry Pi Configuration_ bzw. bei deutschen Spracheinstellungen _Einstellungen / Raspberry Pi Konfiguration_ aus und

  * andern **zuerst** (!) das Passwort fur den Benutzer `pi`
  * und aktivieren dann SSH

Zum Ändern des Passworts mussen Sie einmal das alte Passwort (also `raspberrypi`) und zweimal ein sicheres, neues Passwort angeben. Der Dialog gibt sich freilich nicht mit jedem Passwort zurecht. Geben Sie also ein sicheres Passwort mit zumindest 8 Zeichen an!

![Hier ändern Sie das Passwort des Benutzers »pi«.](https://kofler.info/wp-content/uploads/ssh-config1-600x216.png)

> _Hier andern Sie das Passwort des Benutzers »pi«._

![So aktivieren Sie den SSH-Server.](https://kofler.info/wp-content/uploads/ssh-config2-600x362.png)

> _So aktivieren Sie den SSH-Server._

Wenn Sie SSH aktiviert haben, das `pi`-Passwort aber nicht verandert haben, erscheint in Zukunft nach jedem Login ein Warndialog.

![Wenn SSH aktiviert ist und das Passwort des Benutzers pi nicht verändert wurde, erscheint diese Warnung.](https://kofler.info/wp-content/uploads/ssh-warning-600x107.png)

> _Wenn SSH aktiviert ist und das Passwort des Benutzers pi nicht verandert wurde, erscheint diese Warnung._

### SSH-Server bei einer Lite-Installation aktivieren

Wenn Sie eine Lite-Installation durchgefuhrt haben, fehlt die grafische Benutzeroberflache. Zur Konfiguration konnen Sie nun das Konfigurationsprogramm `sudo raspi-config` verwenden, das im Textmodus lauft. Zuerst Punkt 2 _Change Password_, danach Punkt 7 _Advanced Options_, Unterpunkt A4 _SSH_. Wer mit Linux vertraut ist, kann das Passwort naturlich auch mit `passwd pi` andern und den SSH-Server mit `systemctl start/stop/enable/disable ssh` starten, stoppen, fur zukunftige automatische Starts zu kennzeichnen bzw. diese Kennzeichnung wieder zu losen.

![Passwort ändern mit »raspi-config«](https://kofler.info/wp-content/uploads/raspi-config-600x140.png)

> _Passwort andern mit »raspi-config«_

### SSH-Server bei einer Headless-Installation aktivieren

Von einer Headless-Installation spricht man, wenn der Raspberry Pi immer ohne Tastatur (und in der Regel auch ohne Monitor) betrieben wird, auch wahrend der Installation. In so einem Fall wird das raspbian-Image zuerst auf einem Computer auf die SD-Karte ubertragen, danach wird der Raspberry Pi damit in Betrieb genommen. Alle weiteren Konfigurationsarbeiten erfolgen im lokalen Netz via SSH.

Und genau hier hakt es naturlich: Wie die Erstkonfiguration durchfuhren, wenn SSH von Anfang an gar nicht aktiv ist? Um dieses Henne-Ei-Problem zu losen, mussen Sie auf dem Rechner, auf dem Sie die SD-Karte fur den Raspberry Pi vorbereiten, in der boot-Partition die Datei `ssh` einrichten. Unter Windows konnen Sie die neue Datei im Explorer einrichten, unter Linux und osX reicht `touch /<mountverzeichnis>/ssh`.

Beim nachsten Start des Raspberry Pi wird der SSH-Server gestartet und auch fur die Zukunft aktiviert. Die Datei `/boot/ssh` wird anschließend geloscht. Somit konnen Sie via SSH eine Verbindung zum Raspberry Pi herzustellen (`ssh pi@raspberrypi`). Dann fuhren Sie aus:
    
    
    sudo passwd pi
      (sicheres Passwort einstellen!!)
    

Alternativ konnen Sie naturlich auch `raspi-config` verwenden. Idealerweise sollten Sie das Passwort des Benutzers `pi` andern, _bevor_ Ihr Raspberry Pi mit dem Internet verbunden ist; auf jeden Fall aber so bald wie moglich.

### SSH mit fail2ban weiter absichern

Wenn Ihr Raspberry Pi dauerhaft aus dem Internet erreichbar ist, sollten Sie noch einen Schritt weitergehen und den SSH-Dienst durch fail2ban absichern. Wenn jemand Ihren Raspberry Pi anzugreifen versucht, wird er vermutlich versuchen, durch wiederholte SSH-Login-Versuche Ihr Passwort zu erraten. Der Dienst `fail2ban` unterbindet das sehr wirkungsvoll: Nach mehreren fehlerhaften Login-Versionen wird die IP-Adresse, von der die Logins erfolgen, fur 10 Minuten gesperrt.

Um den SSH-Server durch fail2ban abzusichern, reicht die simple Installation des Pakets.
    
    
    apt-get install fail2ban
    fail2ban-client status ssh
    
      Status for the jail: ssh
      |- filter
      |  |- File list:  /var/log/auth.log 
      |  |- Currently failed: 1
      |  `- Total failed:     2
      `- action
         |- Currently banned: 0
         |  `- IP list: 
         `- Total banned:     0
    

Wenn Sie von der Standardkonfiguration abweichende Einstellungen vornehmen mochten, kopieren Sie `/etc/fail2ban/jail.conf` nach `/etc/fail2ban/jail.local` und nehmen dort die gewunschten Änderungen vor. Anschließend starten Sie `fail2ban` mit `systemctl restart fail2ban` neu.

### Quellen / Links
