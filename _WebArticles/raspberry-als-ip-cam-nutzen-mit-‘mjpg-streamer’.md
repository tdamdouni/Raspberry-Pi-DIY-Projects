# Raspberry als IP-Cam nutzen mit ‘mjpg-streamer’

_Captured: 2017-05-11 at 18:57 from [klenzel.de](https://klenzel.de/3779)_

In [diesem Beitrag](https://klenzel.de/3691) habe ich gezeigt, wie wir Kameras in das lokale Netzwerk mittels _motion_ streamen konnen. _motion_ bietet dazu noch die Moglichkeit, Bewegungen zu erkennen und daraufhin Videos aufzuzeichnen und/oder benutzerdefinierte Aktionen auszufuhren. Wer lediglich eine lokal angeschlossene [Webcam](https://klenzel.de/empfehlung/webcam-microsoft-vx5000) als Webstream anbieten mochte, kann auf _motion_ verzichten und alternativ _mjpg-streamer_ nutzen. Die Umsetzung mit _mjpg-streamer_ zeigt nun dieser Artikel.

![Netzteil für Raspberry Pi 2A](https://klenzel.de/wp-content/uploads/2015/02/netzteil2a.png)

> _Netzteil fur Raspberry Pi 2A_

![Raspberry Pi 2](https://klenzel.de/wp-content/uploads/2015/02/rbp2.jpg)

> _[Raspberry Pi 2](https://klenzel.de/empfehlung/raspberry-pi-2)_

![Webcam Microsoft VX-5000](https://klenzel.de/wp-content/uploads/2015/02/msvx5000.jpg)

Wie vor jedem Projekt aktualisieren wir unser System mittels

### Pakete installieren

Nun installieren wir alle Abhangigkeiten und laden die neuste Version von _mjpg-streamer_ mittels _Subversion_ herunter durch:

Wir wechseln in das neu entstandene Verzeichnis „_mjpg-streamer_" und kompilieren den Code:

### Programm verschieben

Nach dem Kompilieren und der parallel getrunkenen Tasse Kaffee verschieben wir das Programm an einen etwas „sprechenderen" Ort, wie z.B. nach „_/opt_„:

### Startscript erstellen

Nun erstellen wir ein Bash-Script, welches den doch recht langen Befehlsaufruf von _mjpg-streamer_ beinhaltet. Dieses konnen wir beispielsweise mit dem Texteditor „_nano_" erledigen:

Der Inhalt der Datei sieht wie folgt aus:

Nun erlauben wir abschließend noch die Ausfuhrung des Scripts mit

und verlinken es in den Ordner der init-Scripte:

Nun aktivieren wir die Ausfuhrung unseres Scripts beim Systemstart:

### mjpg-streamer starten

Nach einem Neustart oder der manuellen Ausfuhrung von

ist unsere Kamera nun uber die Adresse

erreichbar. Weitere Moglichkeiten, das Kamerabild abzurufen, werden auf der Übersichtsseite

angezeigt.

Der Kamerastream kann nun in einem Webbrowser betrachtet oder in eine zentrale motion-Instanz eingebunden werden. Wie das funktioniert, zeigt [dieser Beitrag](https://klenzel.de/3689).
