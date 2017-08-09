# Kamerazentrale mit motionEye

_Captured: 2017-05-11 at 18:56 from [klenzel.de](https://klenzel.de/3689)_

In [diesem Artikel](https://klenzel.de/3691) habe ich gezeigt, wie eine lokale Kamera mittels _motion _und in [diesem Beitrag](https://klenzel.de/3779) mittels _mjpg-streamer_ im Netz bereitgestellt werden kann. Nennt man mehrere [Raspberry](https://klenzel.de/empfehlung/raspberry-pi-2) und/oder [IP-Cams](https://klenzel.de/empfehlung/ipkamera-dlink-932l) sein eigen, ware es nutzlich, alle Streams auf einer einzelnen Seite betrachten zu konnen. Hier kommt _[motioneye](https://github.com/ccrisan/motioneye) _ins Spiel, das mit einer eigenen motion-Instanz eine Webseite mit den gewunschten Funktionen bereitstellt.

![Netzteil für Raspberry Pi 2A](https://klenzel.de/wp-content/uploads/2015/02/netzteil2a.png)

> _Netzteil fur Raspberry Pi 2A_

![Raspberry Pi 2](https://klenzel.de/wp-content/uploads/2015/02/rbp2.jpg)

> _[Raspberry Pi 2](https://klenzel.de/empfehlung/raspberry-pi-2)_

![screenshot](https://klenzel.de/wp-content/uploads/2015/11/screenshot-300x147.png)

> _Quelle: http://www.howtoembed.com/projects/raspberry-pi/95-motioneye-with-raspberry-pi_

Es spielt in diesem Beitrag keine große Rolle, ob _motioneye_ auf einem Raspberry oder einem (virtuellen) Linux-Server installiert wird, die Vorgehensweise ist ahnlich. Ich wurde jedoch empfehlen, _motioneye_ nicht auf einem Raspberry zu betreiben, insbesonders wenn fur mehrere Kameras die Bewegungserkennung genutzt werden soll. Dieser Vorgang ist verstandlicherweise sehr rechenintensiv und konnte eventuell auf einem Raspberry Version 2 laufen. Bei mir wird _motioneye_ auf einem virtuellen Linux Server im Keller betrieben, da 5 Kameras eingebunden werden welche (zeitweise) auf Bewegung uberwacht werden. Ausprobieren geht naturlich immer.

### Aktualisierung

Zunachst aktualisieren wir unser System mit:

und starten das System ggf. neu.

### Abhangigkeiten installieren

Nun installieren wir mit einem Paketmanager die benotigten Abhangigkeiten mit dem Aufruf von

Wenn auf dem System, auf dem wir _motioneye_ einsetzen, keine lokale Kamera angeschlossen ist, dann reichen die folgenden Pakete:

### Motioneye „installieren"

Das Herunterladen und die Installation wird mit dem Python-Installationsprogramm „_pip_" durchgefuhrt:

Bei meinem System wollte _motioneye_ wegen eines fehlenden Python-Moduls nicht starten, eine manuelle Installation half bei diesem Problem:

Wir kopieren die Demo-Konfigurationsdatei in ein neu erstelltes Verzeichnis fur _motioneye_ unter „_/etc_„:

Die Konfigurationsdatei editieren wir mit einem Texteditor der personlichen Vorliebe, hier sei beispielhaft _nano_ genannt:

Als grundlegende Konfiguration konnen die meisten Einstellungen ubernommen werden, lediglich den Port sowie das Prufungsintervall, ob der motion-Prozess noch lauft, sollte angepasst werden. In meinem Fall verwende ich den Port _88 _sowie ein Prufungsintervall von _20_ Sekunden, so dass sich die beiden folgenden, geanderten Zeilen ergeben:

Den Editor _nano_ konnen wir mit der Tastenkombination _STRG+x_ verlassen und bestatigen die Frage, ob die Änderungen gespeichert werden sollen.

Letztlich erstellen wir das Medienverzeichnis fur _motioneye_:

### Automatischer Start

#### Mittels system.d (z.B. Debian 8)

Damit _motioneye_ beim Systemstart automatisch geladen wird, kopieren wir ein bei der Installation mitgeliefertes system.d-Startscript in den dafur vorgesehenen Order und aktivieren den Autostart:

#### Mittels sysvinit (z.B. Debian 7)

Auf sysvinit-basierenden Systemen realisieren wir den automatischen Start von _motioneye_ wie folgt:

Alternativ zu einem Neustart konnen wir _motioneye_ zunachst testweise mittels

bzw. unter systemd-basierten Systemen mit

starten und mit „ps" prufen, ob der motioneye-Prozess lauft:

![motioneye4](https://klenzel.de/wp-content/uploads/2015/11/motioneye4-300x53.png)

Nun konnen wir das Webinterface auf dem vorher festgelegten Port in einem Browser offnen:

Beim ersten Start wird der Nutzer „_admin_" ohne Passwort zum Anmelden verwendet, diese Anmeldedaten sollten naturlich als erstes geandert werden.

Jede Änderung an der Konfiguration muss mit dem Button „_Apply_" bestatigt werden, dies kann jedoch auch nach einer Reihe von Änderungen erfolgen:

![motioneye5](https://klenzel.de/wp-content/uploads/2015/11/motioneye5-300x223.png)

Nun ist es an der Zeit, die erste(n) Webcam(s) hinzuzufugen. Dazu offnen wir die Konfigurationsleiste mit dem folgenden Button:

Dort andern wir, wenn noch nicht geschehen, unter den „_General Settings_" das Passwort fur die Nutzer „_admin_" und „_user_„. In der Auswahlleiste neben dem gezeigten Button wahlen wir den Menupunkt „_add camera_„.

Im Fenster, das als Overlay erscheint, geben wir nun die Daten fur unsere erste Webcam ein.

![motioneye3](https://klenzel.de/wp-content/uploads/2015/11/motioneye3.png)

Im Fall einer motion-Instanz, wie sie in [diesem Beitrag](https://klenzel.de/3691) eingerichtet wurde, wurde die Adresse wie folgt lauten:

Nachdem die Kamera eingerichtet wurde, kann fur diese individuell festgelegt werden, ob eine Bewegungserkennung aktiv ist oder nicht, ob ein Text uber das Bild gesetzt werden soll und wo erstellte Videos und Fotos gespeichert werden sollen.

![motioneye8](https://klenzel.de/wp-content/uploads/2015/11/motioneye8-167x300.png)

### motioneye akutalisieren

Dank des Python-Installers ist das Aktualisieren von _motioneye_ ein kurzer Prozess:

Je nachdem, ob beim eigenen System systemd oder sysvinit eingesetzt wird, wird _motioneye_ durch

oder

neu gestartet.
