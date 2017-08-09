# Mit dem Raspberry Pi ein Raumüberwachungssystem aufbauen

_Captured: 2015-12-25 at 10:08 from [www.tecchannel.de](http://www.tecchannel.de/pc_mobile/peripherie/2059766/mit_dem_raspberry_pi_ein_raumueberwachungssystem_aufbauen/)_

Die Open-Source-Software Motion befindet sich in den Repositories der Linux-Distribution [Raspbian](http://www.raspbian.org/). Nach der Installation ist das Programm in wenigen Schritten eingerichtet. Wir zeigen Ihnen, wie Sie mit wenig Geld ein hervorragend funktionierendes Überwachungssystem auf die Beine stellen. Wir gehen in diesem Artikel davon aus, dass Raspbian bereits auf Ihrem Raspberry Pi lauft und sich auf dem aktuellen Stand befindet.

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2389047/522x294.png)

> _Raspberry Pi als Arcade-Automat_

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2389048/522x294.png)

### 1\. Kameras für das Überwachungssystem

Dass Sie fur diese Anleitung einen Raspberry Pi und eine Kamera benotigen, versteht sich von selbst. Bei der Wahl der Kamera ist jedoch Voraussetzung, dass diese mit dem V4L-Treiber (Video for Linux) kompatibel ist und als Gerat in der Form "/dev/videoX" auftaucht. Das X steht fur die Systemnummer der Kamera, und die Zahlung beginnt bei 0. Die erste Kamera am System ware "/dev/video0", die zweite "/dev/video1" und so weiter. In der Regel unterstutzt V4L fast jede handelsubliche Webcam. Eine Liste geeigneter Webcams findet sich auf http://elinux.org/RPi_USB_Webcams. Sie sollten die Webcam uber einen USB-Hub mit eigenem Netzteil anschließen, da der kleine Raspberry selbst die Kamera sonst nicht in jedem Fall ausreichend mit Strom versorgen kann.

Das fur den Raspberry Pi speziell entwickelte Kameramodul erscheint derzeit nicht als V4LGerat. Es gibt aber bereits Unterstutzung dafur, und die Entwickler arbeiten daran, diesen Umstand zu adressieren. Wir zeigen Ihnen, wie Sie das Kameramodul fur den Winzling mit V4L und damit Motion fit machen.

Nachdem Sie die Webcam an den Raspberry Pi angesteckt haben, sollten Sie prufen, ob diese ordnungsgemaß funktioniert. Dazu fuhren Sie direkt nach Einstecken der Kamera nachfolgenden Befehl aus:

`dmesg | tail `

Sie konnen das Vorhandensein der Kamera auch testen, indem Sie diesen Befehl nutzen:

`ls -ltrh /dev/video*`

Damit uberprufen Sie einfach, ob das Gerat im System vorhanden ist. Sie erhalten eine Ausgabe mit entsprechenden Informationen. Sollte mehr als eine V4L-fahige Kamera am Computer hangen, sind in der Auflistung auch mehrere Videogerate enthalten.

### 2\. Überwachungs-Software Motion installieren

Die Open-Source-Software Motion spricht das Gerat "/dev/videoX" an und beobachtet den Video-Stream. Sie konnen ein Limit fur sich andernde Pixel festgelegen. Wird die Grenze dieser Pixelzahl uberschritten, wertet Motion das als Bewegung und kann je nach Konfiguration entsprechend reagieren. Sie konnen Motion via Kommandozeile installieren. Öffnen Sie dafur ein Terminal, und geben Sie folgende zwei Zeilen ein:

`sudo apt-get update sudo apt-get install motion`

Bei der Installation weist Sie das Paket darauf hin, dass Motion nicht automatisch startet. Wie das geht, lesen Sie im folgenden (optionalen) Abschnitt. Zunachst einmal starten wir den Daemon nicht und kummern uns um die Konfiguration.

**Vorarbeiten:** Motion befindet sich im Raspbian-Repository, und Sie konnen es uber apt-get installieren. Das Programm selbst ist zwar nur klein, allerdings werden automatisch noch einige Video-Codecs nachinstalliert.

**Alternative Startvariante**

Motion lasst sich auch uber ein Init-Script starten, das nach der Installation des Programms bei Raspian unter "/etc/init.d/motion" zu finden ist. Fur den automatischen Start zusammen mit dem System bearbeiten Sie die Datei "/etc/default/motion". Ersetzen Sie das "no" hinter "start_motion_ daemon" durch yes. Wie bei Init-Scripts unter dieser Version von Debian ublich, konnen Sie in einem Terminalfenster uber die Zeile

`sudo /etc/init.d/motion stop`

Motion jederzeit manuell beenden, dann Änderungen in der Konfiguration vornehmen und das Programm anschließend mit

`sudo /etc/init.d/motion start`

Wenn Sie das Kameramodul fur den Raspberry Pi verwenden, mussen Sie noch eine kleine Änderung vornehmen. Öffnen Sie die Datei "/etc/init.d/motion" als Benutzer root in einem Editor. An den Anfang des Codes fugen Sie uber "Name=motion" die folgende Zeile ein:

`export LD_PRELOAD=/usr/lib/uv4l/uv4lext/armv6l/libuv4lext.so`
### 3\. Die Funktion von Motion ausprobieren

Sie konnen die Überwachungskamera sofort in Betrieb nehmen, indem Sie Motion handisch starten. Fur einen schnellen Check ist das außerdem gar keine schlechte Idee. Geben Sie dazu auf der Kommandozeile folgenden Befehl ein:

`sudo motion`

Das Vorangestellte sudo ist in diesem Fall notwendig, da nur der Administrator root die Standardkonfigurationsdatei lesen kann. Legen Sie eine conf-Datei dagegen in Ihrem Home-Verzeichnis an, konnen Sie Motion auch als Anwender ohne root-Rechte starten.

Nach Aufruf des Befehls sehen Sie diverse Zahlen uber den Bildschirm laufen. Wichtig ist die letzte Zeile. Bei korrekter Konfiguration lautet diese: "[1] Started stream webcam server in port 8081".

Somit wissen wir zwei Dinge. Erstens funktioniert unsere Hardware. Bewegen Sie nun die Kamera, reagiert die Software auch sofort und teilt uns die Namen der gespeicherten Bilder mit. In der Standardkonfiguration legt Motion diese unter "/tmp/motion" ab.

Zweitens konnten wir das Bild auch mit einem Streaming-Client oder in einem beliebigen Webbrowser betrachten. Dafur ist Port 8081 zustandig. Per Standard ist Motion allerdings so konfiguriert, dass dies nur mit dem lokalen Rechner moglich ist. Stoppen Sie zunachst das laufende Motion mit der Tastenkombination Strg-C. Danach offnen Sie die Standardkonfigurationsdatei "/etc/motion/motion.conf" mit einem Editor Ihrer Wahl, zum Beispiel Nano: sudo nano /etc/motion/motion.conf

**Kontrolle:** Ob Sie einen Browser oder VLC fur die Überprufung verwenden, ist nicht relevant. Diese Methode lasst sich auch hervorragend fur die Einrichtung des Bildausschnittes verwenden.

Die Datei ist ziemlich umfangreich, und wir werden sie spater noch weiter anpassen. Fur den Moment suchen Sie nach der Zeile webcam_ localhost on und andern diese in webcam_ localhost off. Der Parameter befindet sich in der Sektion "Live Webcam [Server](http://www.tecchannel.de/server/)", die relativ mittig liegt.

Starten Sie das Programm noch einmal mit sudo motion. Nun konnen Sie von jedem Rechner im gleichen [Netzwerk](http://www.tecchannel.de/netzwerk/) den Stream in einem Browser mit Eingabe der URL http://IP-Adresse Raspberry Pi:8081 einsehen, beispielsweise http://192.168.100.108:8081. Die IP-Adresse bekommen Sie auf der Kommandozeile uber den Befehl ifconfig heraus. Haben Sie beispielsweise [VLC](http://www.videolan.org/) installiert, ist das Nutzen dieses Streams ebenfalls moglich. Klicken Sie dazu auf "Medien > Netzwerkstream offnen", geben die URL wie im Browser ein und klicken auf "Wiedergabe".

Sie konnen jetzt das Bild kontrollieren und die Kamera so positionieren, dass ein fur die Überwachung optimales Areal erfasst wird.
### 4\. Konfigurationsdatei individuell anpassen

In diesem Abschnitt kummern wir uns um die wichtigsten Parameter der Konfigurationsdatei. Sie werden diese Datei im Laufe der Zeit des Öfteren anpassen. Alles zu erklaren wurde den Rahmen dieses Artikels sprengen. Allerdings sind einige Parameter essenziell, und diese mochten wir Ihnen kurz darlegen.

Relativ am Anfang finden Sie die Zeile "videodevice /dev/video0". Sollte nur eine Kamera am Raspberry Pi hangen, ist das so in Ordnung, und Sie mussen das nicht andern. Wenn Sie zusammen mit Motion mehrere Kameras einsetzen mochten, verwenden Sie mehrere Konfigurationsdateien. Sie starten dann Motion mehrmals mit dem Schalter "-c" und geben dahinter jeweils die Konfigurationsdatei an. Die Kommandozeile kann dann beispielsweise so aussehen:

`motion -c /home/pi/motion/motion. conf   
`

Das ist jedoch nur in der Testphase sinnvoll. Wenn Sie spater Motion automatisch starten oder im Hintergrund laufen lassen wollen, verwenden Sie fur mehrere Kameras eine andere Methode. Am Ende der Datei "/etc/motion/ motion.conf" finden Sie vier mit einem ";" auskommentierte Zeilen. Bei zwei Kameras entfernen Sie das Semikolon vor den ersten beiden und passen den Pfad zur Konfigurationsdatei an. Das Ergebnis sieht dann so aus

`thread /etc/motion/thread1.confthread /etc/motion/thread2.conf   
`

Öffnen Sie die beiden conf-Dateien in einem Editor. Passen Sie die Angaben hinter "videodevice", "target_dir" und "webcam_port" fur jede Kamera an. Verwenden Sie fur eine Kamera den Port 8081 und fur die andere 8082. "target_dir" sollte ebenfalls auf unterschiedliche Verzeichnisse verweisen. Fur die anderen Einstellungen nehmen Sie sich die Eintrage in der "motion.conf" zum Vorbild. Kommentieren Sie alles aus, was Sie nicht benotigen. Wenn Sie Motion dann starten, konnen Sie den Stream der Kameras jeweils uber den konfigurierten Port im Browser betrachten.

**Stream abgreifen:** Mit dem VLC Media Player konnen Sie zum Beispiel den Stream von Motion abgreifen. Damit lasst sich auch eine Live-Überwachung der Gebiete realisieren, auf die die Kamera gerichtet ist.

Bild einstellen: Ein Stuckchen weiter unten finden Sie in der Datei "motion.conf" die beiden Zeilen "width 320" und "height 240". Das sind Breite und Hohe des Bildes, das Motion ausgibt. Sie sollten die maximalen Werte der eingesetzten Kamera kennen und die Werte entsprechend nicht uberschreiten. Passen Sie auch auf, dass die Bilder nicht zu groß werden. Ansonsten geht Ihnen bei viel Bewegung irgendwann der Speicher auf dem Datentrager aus. Wir empfehlen klein anzufangen und die Großen in kleinen Schritte anzupassen.

Direkt darunter finden Sie "framerate 2". Die Zahl ist die maximale Bildanzahl, die pro Sekunde aufgenommen wird. Je hoher die Zahl, desto mehr Bilder und desto mehr Speicher werden benotigt. Auch hier sollten Sie vorsichtiges Fein-Tuning walten lassen.

Der Parameter "auto_brightness" steht per Standard auf "off". Billige Webcams bringen keine automatische Justierung der Helligkeit mit sich. Sollten Sie deswegen Probleme haben, konnen Sie Motion diese Einstellung uberlassen. Direkt darunter finden Sie die Parameter "brightness", "contrast", "saturation" und "hue". Auch damit konnen Sie experimentieren und das Bild optimal einstellen.

### Motion mit Zeitsteuerung

**Herzstuck der Bewegungserkennung:** Das ist die Sektion "Motion Detection Settings". Hier legen Sie fest, wie viele Pixel sich andern mussen, damit Motion dies als Bewegung erkennt.

Wollen Sie Motion zum Beispiel nur nachts laufen lassen oder ab einer bestimmten Uhrzeit, konnen Sie Motion auch mit Hilfe eines Cronjobs zeitsteuern. Das Programm bietet dafur eine Fernsteuerfunktion, die standardmaßig auf http://localhost:8080 lauscht. Damit sich diese per Cron nutzen lasst, installieren Sie mit sudo apt-get install libwww-perl zuerst einige notige Pakete nach. Einen Cronjob erstellen Sie mit dem Befehl sudo crontab -e. Geben Sie in den Editor die zwei Zeilen

`0 8 * * * root /usr/bin/lwp-request http://localhost:8080/0/detection/ start > /dev/null0 18 * * * root /usr/bin/lwp-request http://localhost:8080/0/detection/ pause > /dev/null`

ein und speichern Sie die Definition mit Strg-O. Die Bewegungserkennung startet dann jeden Tag um 8:00 Uhr und pausiert ab 18:00 Uhr.
### 5\. Bewegungserkennung konfigurieren

Sehr wichtig in der Konfigurationsdatei ist die Sektion "Motion Detection Settings". Der erste Parameter, "threshold", bestimmt, wie viele Pixel sich in einem Bild andern mussen, um als Bewegung wahrgenommen zu werden. Per Standard steht das auf "1500". Behalten Sie im Hinterkopf, dass bei Änderung der Breite und Hohe die Gesamtzahl der Pixel wachst.

Bei den Standardeinstellungen haben wir 76.800 Pixel pro Bild (320 x 240). Setzen Sie das zum Beispiel auf 640 und 480, waren das 307.200 Pixel. Eine Änderung ist fur die Software aber weiterhin 1500 Pixel. Die Sache wird also wesentlich sensibler.

**Überredungskunst:** Das kleine Kameramodul fur den Raspberry Pi funktioniert standardmaßig nicht mit Motion. Ein Entwickler stellt jedoch einen Treiber bereit, der die Kamera zur Zusammenarbeit bewegt.

Sobald Motion eine Bewegung erkennt, speichert es Dateien per Standard im JPG-Format. Zusatzlich wird nach jeder Bewegungssequenz per Standard eine SWF-Datei als kleiner Film erstellt. Wo diese Dateien hinterlegt werden, konfigurieren Sie uber den Parameter "target_dir". Per Standard ist das "/tmp/motion". Sie sollten das Verzeichnis jedoch andern, wenn Sie die Dateien auch uber einen Neustart hinaus behalten mochten. "/tmp/" wird bei vielen Linux-Systemen nach einem Neustart geloscht. Direkt darunter finden Sie "snapshot_ filename". Damit legen Sie den Dateinamen fest. Die Standardeinstellung ist aber bereits sehr gut, da die Dateien anhand eines Zeitstempels abgelegt werden.

Weiter gibt es in der Konfigurationsdatei eine Sektion, die mit "External Commands, Warnings and Logging" beginnt. Dort konnten Sie bei Erkennung einer Bewegung, sowohl bei Start als auch Ende, externe Befehle ausfuhren lassen. Denkbar ist zum Beispiel das Senden einer [E-Mail](http://www.tecchannel.de/index.cfm?pid=458) oder das Abspielen eines Klangs.
### 6\. Das Kameramodul des Raspberry Pi

Besitzen Sie ein Kameramodul fur das Raspberry Pi, war ein Einsatz mit Motion bis vor kurzer Zeit schwierig. Es gab eine speziell angepasste Version von Motion, mit der einige Leute Erfolg hatten. In der Zwischenzeit wurde allerdings [ein Treiber](http://www.pcwelt.de/oz5n) entwickelt, der das Kameramodul als "/dev/video0" einbindet.

Dieser funktioniert, es ist aber etwas Handarbeit notwendig. Öffnen Sie ein Terminal und fuhren Sie folgende Befehlszeile aus

`wget http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc && sudo apt-key add ./lrkey.asc`

`deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ wheezy main a`

m Ende der Datei "/etc/apt/sources.list" ein. Nun folgen die drei Zeilen:

`sudo apt-get updatesudo apt-get install uv4l uv4l-raspicamsudo apt-get install uv4lraspicam- extras`

damit ist der Treiber installiert.

Manuell binden Sie den Treiber nach Systemstart so ein:

`uv4l --driver raspicam --autovideo_ nr --width 640 --height 480 --encoding jpeg `

Die Breite und Hohe konnen Sie naturlich nach Belieben einbinden. Die maximale Auflosung des Kameramoduls betragt 2592 x 1944 oder funf Megapixel. An dieser Stelle testen wir, ob der Treiber funktioniert, und fuhren dazu diese Zeile aus:

`dd if=/dev/video0 of=bild.jpeg bs=11M count=1`

Wenn alles funktioniert, sollte sich danach eine JPG-Datei mit dem Namen "bild.jpeg" in dem Verzeichnis befinden, in dem Sie den Befehl ausgefuhrt haben.

Um den Treiber wieder zu entladen, beenden Sie uv4l uber den Befehl pkill aus: Dazu geben Sie folgenden Befehl ein. pkill uv4l

**Zusammenspiel mit Motion:**Der Treiber funktioniert auch mit Motion. Allerdings brauchen wir dafur die Variable LD_PRELOAD vor dem Start der Überwachungs-Software. Der Befehl, um Motion zu starten:

`sudo LD_PRELOAD=/usr/lib/uv4l/ uv4lext/armv6l/libuv4lext.so motion`

Rufen Sie nun die URL des Raspberry Pi mit Port 8081 auf, sollte das Bild erkennbar sein. Auch auf Bewegung reagiert das Kameramodul, und die Software nimmt brav alles auf. Laden Sie die Bibliothek vorher nicht, reagiert das Kameramodul ebenso. Allerdings nimmt es keine Bilder auf und funktioniert somit nicht wirklich. Ein automatischer Start von Motion mit Kameramodul und einer individuellen Konfigurationsdatei konnte in der Datei "/etc/ rc.local" so aussehen:

`uv4l --driver raspicam --autovideo_ nr --width 640 --height 480 --encoding jpegsleep 3LD_PRELOAD=/usr/lib/uv4l/uv4lext/ armv6l/libuv4lext.so /usr/bin/ motion -c /home/pi/motion/ motion.conf`

Ob das sleep 3 unbedingt notwendig ist, muss man ausprobieren. Auf jeden Fall verzogert es den Start von Motion um drei Sekunden, und der Treiber hat Zeit, sich zu laden. Damit Motion im Hintergund startet, editieren Sie die Konfigurationsdatei und suchen nach der Zeile "daemon=off". Diese befindet sich ziemlich am Anfang. Ein Änderung von off auf on bewirkt, dass beim handischen Start oder uber rc.local das Terminal wieder freigegeben wird und das Programm im Hintergrund lauft. Mit pkill motion konnen Sie Motion bei Bedarf jederzeit beenden. (hal)
