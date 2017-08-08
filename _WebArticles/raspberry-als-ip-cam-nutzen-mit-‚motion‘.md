# Raspberry als IP-Cam nutzen mit ‚motion‘

_Captured: 2017-05-11 at 18:58 from [klenzel.de](https://klenzel.de/3691)_

In diesem Beitrag mochte ich zeigen, wie sich ein [Raspberry Pi](https://klenzel.de/empfehlung/raspberry-pi-2) als Kameraserver einsetzen lasst. Dazu konnen entweder Webcams verwendet werden, die via USB mit dem Raspberry verbunden werden oder direkt eine Cam fur die spezielle Kameraschnittstelle des Raspberry. Nach diesem Beitrag sind wir in der Lage, via URL die am Raspberry angeschlossene oder via Netzwerk erreichbare Kamera zu betrachten sowie die Bewegungserkennung ein- und auszuschalten.

![Netzteil für Raspberry Pi 2A](https://klenzel.de/wp-content/uploads/2015/02/netzteil2a.png)

> _Netzteil fur Raspberry Pi 2A_

![Raspberry Pi 2](https://klenzel.de/wp-content/uploads/2015/02/rbp2.jpg)

> _[Raspberry Pi 2](https://klenzel.de/empfehlung/raspberry-pi-2)_

![Webcam Microsoft VX-5000](https://klenzel.de/wp-content/uploads/2015/02/msvx5000.jpg)

### System aktualisieren

Vorbereitend aktualisieren wir unser System, wie vor jedem neuen Projekt:

Nach der Aktualisierung und ggf. einem Neustart des Systems schließen wir die Kamera an einen freien USB-Port des [Raspberry](https://klenzel.de/empfehlung/raspberry-pi-2). Dabei sollte beachtet werden, dass ein solches Multimedia-Device eine gewisse Leistung benotigt und das [5V-Netzteil](https://klenzel.de/empfehlung/netzteil-5v-2a-microusb) dementsprechend dimensioniert ist. Ich bin fur dieses System mit einem 1,5A Netzteil bisher gut ausgekommen.

Nach dem Anschließen prufen wir mit

ob die Kamera vom System erkannt wurde.

![motion3](https://klenzel.de/wp-content/uploads/2015/11/motion3.png)

Wurde die Kamera vom System erfolgreich erkannt, prufen wir mit

unter welchem Pfad die Kamera im System eingebunden wurde. Diesen Pfad benotigen wir gleich fur die Konfiguration.

![motion4](https://klenzel.de/wp-content/uploads/2015/11/motion4.png)

### motion installieren

Anschließend installieren wir das Programm _motion_ mittels des Debian-Paketinstallers.

Wollen wir Videos aufzeichnen, benotigen wir noch das Paket „_ffmpeg_„, welches wir leider nicht in einemRepository vorfinden. Daher installieren wir dieses handisch mit:

### Autostart konfigurieren

Nun konfigurieren wir unser System so, dass _motion_ beim Systemstart ebenfalls gestartet wird. Dazu offnen wir die Datei „_/etc/default/motion_" mit einen Texteditor unserer Wahl, beispielsweise _nano_…

…und andern hier den Eintrag

auf

Haben wir dafur den Texteditor _nano_ verwendet, konnen wir diesen mit der Tastenkombination _STRG+x_ verlassen und bestatigen die Abfrage, ob die Dateianderungen gespeichert werden sollen mit _Ja_.

### Grundkonfiguration

Die hauptsachliche Konfiguration findet in der Datei „_/etc/motion/motion.conf_" statt. Eine komplette [Auflistung aller moglichen Konfigurationsmoglichkeiten](http://www.lavrsen.dk/foswiki/bin/view/Motion/ConfigFileOptions) findet man direkt beim [Entwickler](http://www.lavrsen.dk/foswiki/bin/view/Motion/ConfigFileOptions).

Wir verwenden in diesem Beitrag die Webcam „[Microsoft VX-5000](https://klenzel.de/empfehlung/webcam-microsoft-vx5000)„, welche via USB angeschlossen ist. Hierfur zeige ich eine mogliche Grundkonfiguration von _motion_. Zuvor sichern wir jedoch die bereits vorhandene Standardkonfiguration mit

und erstellen eine neue Konfiguration mittels

mit folgendem Inhalt:

1234567891011121314151617181920 
daemon onprocess_id_file /var/run/motion/motion.pidvideodevice /dev/video0v4l2_palette 8input 8norm 0width 640height 480framerate 2output_all offffmpeg_cap_new offoutput_motion offoutput_normal offquality 100target_dir /tmp/motiontext_rightwebcam_port 8081webcam_quality 100webcam_maxrate 2webcam_localhost off

Zur Erlauterung einzelner Konfigurationszeilen:

daemon on  
process_id_file /var/run/motion/motion.pid  
videodevice /dev/video0  
v4l2_palette 8  
input 8  
norm 0  
width 640  
height 480  
framerate 2  
output_all off  
ffmpeg_cap_new off  
output_motion off  
output_normal off  
quality 100  
target_dir /tmp/motion  
webcam_port 8081  
webcam_quality 100  
webcam_maxrate 2  
webcam_localhost off
motion wird als Hintergrundprozess gestartet  
hier wird die Prozess-ID angegeben  
welches Video-Device soll verwendet werden? (siehe „Kamera anschließen")es handelt sich um eine USB-Cam  
wir nutzen die PAL-Norm  
Breite des Ausgabevideos  
Hohe des Ausgabevideos  
Anzahl der Bilder pro Sekunde, die von der Cam empfangen werden sollen  
Es werden keine Bilder kontinuierlich gespeichert  
Es werden keine Videos erstelltEs werden keine Bilder bei erkannter Bewegung erstellt  
Die JPEG-Qualitat wird auf 100% belassen  
Der Speicherort der zu speichernden Bilder  
Der Port, uber den motion erreichbar ist und das Kamerabild anzeigt  
Die Bildqualitat in Prozent, die uber den Webserver ausgegeben wird  
Die Bilder pro Sekunde, die uber den Webserver ausgegeben werden  
Deaktivierung der Option, dass der Webserver nur uber „localhost" erreichbar ist.

Mit den zusatzlichen Optionen

lasst sich uber das Bild der Webcam ein Text ausgeben. Im angegeben Beispiel wird links ein statischer Text und auf der rechten Seite das Datum mit Uhrzeit angezeigt.

Mit der bisherigen Konfiguration konnen wir nun bereits _motion_ mittels

starten und mit

prufen, ob der Prozess lauft.

![motion1](https://klenzel.de/wp-content/uploads/2015/11/motion1.png)

War der Start erfolgreich, konnen wir bereits jetzt das Bild der Kamera im Browser mit folgender Adresse betrachten:

![motion2](https://klenzel.de/wp-content/uploads/2015/11/motion2-300x224.png)

### Bewegungserkennung ohne Aufnahme

motion bietet die Moglichkeit, Bewegungen im Bild zu erkennen. Bei erkannten Bewegungen konnen Bilder oder Videos erstellt werden, die an einem zuvor definierten Speicherort hinterlegt werden. Oder es besteht die Moglichkeit, bei einer Bewegung ganze Befehle oder eigene Scripts zu starten.

Dazu ist es notwendig, die Konfiguration zu erweitern bzw. anzupassen.

Threshold legt dabei die Anzahl der Pixel fest, mit der sich ein Bild vom vorhergehenden Bild unterscheiden muss, damit eine Bewegung als solche interpretiert wird. Mit diesem Wert muss ein wenig herumgespielt werden, im Innenbereich mag dieser passen, jedoch ware ein Wert von _1500_ fur den Außeneinsatz zu empfindlich.

Mit den Zeilen „_on_event_start_" und „_on_event_stop_" lassen sich Befehle und Scripte definieren, welche bei einer erkannten Bewegung bzw. nach einer gewissen Zeit der Ruhe ausgefuhrt werden. In unserem Beispiel werden lediglich die Woter „_An_" und „_Aus_" in die Datei „_/tmp/motion.txt_" geschrieben, um den Erfolg zu prufen. Denkbar waren hier jedoch unzahlige Moglichkeiten, wie beispielsweise das Versenden einer eMail oder das Setzen eines Status bei [openHAB](https://klenzel.de/2668).

Nach jeder Änderung der Konfigurationsdatei ist es notwendig, motion mittels

neu zu starten.

### Bewegungserkennung mit Aufnahme

Soll motion bei einer erkannten Bewegung ein Video vom Geschehen aufzeichnen, andern wir in unserer Konfiguration die Zeile

und erganzen unsere Konfiguration mit folgenden Zeilen:

Nun wird bei jeder Bewegung ein Video im Format eines Flash-Movies im Ordner_ /tmp/motion/_ erstellt und mit der Uhrzeit des Geschehens benannt. Denkbar ware hier eine Einbindung eines NAS-Systems mittels _NFS_ oder _SMB_ und die Konfiguration von _motion_ zur Speicherung in den eingebundenen Ordner.

Auch hier ist die Option

anzuwenden und motion nach Änderung der Konfiguration mittels

neu zu starten.

![motion5](https://klenzel.de/wp-content/uploads/2015/11/motion5.png)

### Externe Steuerung

motion lasst sich zusatzlich von außen steuern. Mochten wir beispielsweise die Bewegungserkennung aktivieren oder deaktivieren, erganzen wir unsere Konfiguration durch folgende Zeilen:

Damit richten wir einen Kontrollschnittstelle auf Port 8080 ein und lassen die Steuerung auch außerhalb von _localhost_ zu.

Nun ist es moglich, von einem externen System die Bewegungserkennung mit dem Aufruf von

zu pausieren und mit dem Aufruf von

wieder zu reaktivieren.

### Mehrere Kameras verwalten

Es besteht die Moglichkeit, auch mehr als eine Kamera mit _motion_ zu betreiben. Dabei prufen wir zunachst wie Eingangs gezeigt, unter welchen Pfaden unsere Kameras im System eingebunden wurden und reduzieren die Hauptkonfiguration _/etc/motion/motion.conf_ auf das folgende:

1234567 
daemon onprocess_id_file /var/run/motion/motion.pidcontrol_port 8080control_localhost offthread /etc/motion/cam1.conf

Nun erstellen wir fur jede Kamera eine seperate Konfigurationsdatei und verweisen in der _motion.conf_ auf diese:

Eine Konfigurationsdatei konnte beispielhaft (z.B. _/etc/motion/cam1.conf_) wie folgt aussehen:

123456789101112131415161718192021222324252627 
videodevice /dev/video0width 640height 480framerate 2output_all offffmpeg_cap_new onoutput_normal offquality 100text_right %d.%m.%Y - %H:%M:%Stext_left Klenzel::Demothreshold 1500target_dir /tmp/motion/cam1movie_filename %v-%Y%m%d%H%M%Sffmpeg_video_codec swfauto_brightness onthreshold 6000noise_tune onminimum_motion_frames 2webcam_port 8081webcam_quality 100webcam_maxrate 2webcam_localhost offon_event_start curl --max-time 2 --connect-timeout 2 --header "Content-Type: text/plain" \--request PUT --data "ON" http://openhab/rest/items/MOTION_CAM1/stateon_event_end curl --max-time 2 --connect-timeout 2 --header "Content-Type: text/plain" \--request PUT --data "OFF" http://openhab/rest/items/MOTION_CAM1/state

Dabei ist naturlich zu beachten, dass die Zeilen „_videodevice_„, „_target_dir_" und „_webcam_port_" fur alle Kameras individuell angepasst werden mussen. Soll eine Bewegungserkennung eingerichtet werden, ist die Zeile „_threshold_" naturlich wieder mit anzugeben.

### Einbinden einer vorhandenen IP-Cam

Aus verschiedenen Grunden kann es interessant sein, keine lokale USB-Kamera sondern eine bereits vorhandene Netzwerkkamera in _motion_ einzubinden. Moglicherweise unterstutzt die IP-Kamera keine Bewegungserkennung und das soll nun mittels _motion_ nachgerustet werden.

In diesem Fall wird die Zeile

durch die folgende Einbindung ersetzt:

Die genaue Adresse fur seine IP-Cam findet man meistens im Internet, beispielsweise lautet diese fur eine [D-Link DCS932L](https://klenzel.de/empfehlung/ipkamera-dlink-932l) wie folgt:

### Weitere Moglichkeiten

Eine weitere Moglichkeit, mehrere Kamera(quellen) zu verwalten und in einer netten Weboberflache anzuzeigen, zeigt [dieser Artikel uber motioneye](https://klenzel.de/3689).

Mochte man auf eine Bewegungserkennung verzichten und lediglich die lokal angeschlossene Kamera streamen (z.B. an eine ubergeordnete motion-Instantz), so konnte sich eine Alternative mittels _mjpg_streamer_ anbieten, was in [diesem Beitrag](https://klenzel.de/3779) beschrieben ist.
