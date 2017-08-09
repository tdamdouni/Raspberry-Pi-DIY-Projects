# Raspberry Pi: Kamera einrichten und verwenden 

_Captured: 2017-04-23 at 23:30 from [www.netzmafia.de](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_Kamera.html)_

Seit Mai 2013 ist fur den Raspberry Pi ein winziges, aber leistungsfahiges Kamera-Modul erhaltlich. Anfang 2014 kan ein zweites Modell hinzu, das Nachtaufnahmen mit Infrarot-Beleuchtung erlaubt. Die technischen Daten sind in der folgenden Tabelle zusammengefasst:

Abmessungen
25 mm x 20 mm x 9 mm

Sensor
5 Megapixel mit Fixfokusobjektiv

Fotoauflosung
bis 2592 x 1944 Pixel

Videoauflosung
1920 x 1080 / 30 Frames  
1280 x 720 / 60 Frames  
640 x 480 / 60 oder 90 Frames

Kabellange
ca. 150 mm

Versionen
Raspberry Pi Kamera  
Raspberry Pi Kamera Infrarot
![](http://www.netzmafia.de/skripten/hardware/RasPi/cam1.jpg)

Das Kamera-Modul wird in einem Antistatikbeutel mit vormontiertem Flachbandkabel geliefert. Der Anschluss der Kamera erfolgt uber die 15-polige serielle MIPI-Schnittstelle (CSI - Camera Serial Interface) auf dem Raspberry Pi. Der Vorteil dieser Schnittstelle gegenuber USB besteht in der direkten Verbindung von Kamera-Modul und dem Broadcom BCM2835 (SoC). Die Infrarot-Version (NoIR) kann "im Dunklen sehen", zeigt aber bei Tageslicht eine leichte Farbverfalschung. Hier wird besser die "Normalversion" verwendet - oder man spendiert einen Infrarotfilter.

Da hier nur die wichtigsten Optionen und Moglichkeiten von Kamera und Software besprochen werden, sei jetzt schon auf die Dokumentation im Web verwiesen: 

  * [ Ausfuhrliche Dokumentation als Open-Office-Dokument](https://github.com/raspberrypi/userland/blob/master/host_applications/linux/apps/raspicam/RaspiCamDocs.odt)
  * [Python-Software-Paket](https://pypi.python.org/pypi/picamera)
  * [Dokumentation dazu](http://picamera.readthedocs.org/en/release-1.2/index.html)

Das naturlich auf den Webseiten des Raspberry Pi selbst auch etwas uber die Kamera steht, brauche ich wohl nicht mehr zu erwahnen.

### Kamera anschliessen

Die CSI-Schnittstelle befindet sich zwischen der HDMI- und der Ethernet-Buchse. Um das 15-polige Flachbandkabel vom Kamera-Modul mit dem Board zu verbinden zieht man den oberen Teil des CSI-Steckverbinders etwas nach oben, steckt dann das Flachbandkabel mit der blauen Markierung zum Ethernet-Anschluss hin ein und druckt den Verschluss wieder nach unten. Nun ist der Kontakt hergestellt und das Kabel sitzt fest.

![](http://www.netzmafia.de/skripten/hardware/RasPi/cam3.jpg)

Nun muss noch der Kamera-Support in Raspbian aktiviert werden, was am Einfachsten uber das Konfigurationstools raspi-config erledigt wird. Dort einfach die Kamera auf "Enable" setzen. Zum Abschluss muss der Raspberry Pi noch rebootet werden, damit die Kamera genutzt werden kann.

![](http://www.netzmafia.de/skripten/hardware/RasPi/cam2.jpg)

Wenn Sie die rote Aufnahme-LED stort, konnen Sie diese deaktivieren. Dazu ist ein neuer Eintrag in der Datei /boot/config.txt mit anschließendem Neustart notwendig:
    
    
    disable_camera_led=1
    

Einmal mit der obigen Methode deaktiviert, lasst sich die LED uber den GPIO 5 steuern (naheres uber das Ansprechen des GPIO finden Sie z. B. im Kapitel [Raspberry Pi: GPIO per Shell-Kommando ansteuern](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_GPIO.html)). Der GPIO wird aktiviert mit:
    
    
    sudo echo "5" > /sys/class/gpio/export
    sudo echo "out" > /sys/class/gpio/gpio5/direction
    sudo chmod 666 /sys/class/gpio/gpio5/value
    

Danach konnen Sie die LED einschalten mit dem Kommando
    
    
    echo "1" > /sys/class/gpio/gpio5/value
    

und wieder ausschalten mit
    
    
    echo "0" > /sys/class/gpio/gpio5/value
    

### Einzelbilder oder Bildsequenzen aufnehmen

Das Kamera-Modul wird uber die beiden Programme raspistill (fur Bilder) und raspivid (fur Videos) angesprochen, die uber zahlreiche Optionen verfugen. Auch eine Python-Bibliothek ist verfugbar. raspivid speichert Videos ausschließlich im H264-Format ab. Die Datei muss daher fur die meisten Zwecke zuerst in ein gebrauchliches Format konvertieren werden (etwa mit gpac). Das Aufnehmen von Bildern ist recht einfach, wie die folgenden Beispiele zeigen:
    
    
    # Aufnahme im JPG-Format (default)
    raspistill -o image.jpg
    
    # Aufnahme in anderen Formaten mit -e <Format>
    # möglich sind: jpg, bmp, gif und png, z. B.
    raspistill –e png -o image.png
    
    # Aufnahme ohne Preview mit -n oder --nopreview
    raspistill -n -o image.jpg
    
    # Zeitverzögerte Aufnahme mit -t <Millisekunden>
    # ACHTUNG: Default ist -t 5000, wenn es schnell gehen
    # soll, dann -t 0 verwenden
    raspistill  -t 2000 -o image.jpg
    
    # Aufnahme in einer niedrigeren Auflösung mit -w und -h
    # z. B. 640 x 480 pixel
    raspistill  -w 640 -h 480 -o image.jpg
    
    # Aufnahme in einer niedrigeren Qualität (Angabe in %-Werten)
    raspistill -q 50 -o image.jpg
    

Die Vorschaubilder lassen sich ebenfalls an- und abschalten: liefert eine Vorschau im Vollbildmodus, unterdruckt die Vorschau. Die Große der Vorschau kann mittels eingestellt werden. Naturlich konnen Sie auch Werte wie Helligkeit, Kontrast, Bildscharfe oder Farbsettigung steuern. Aufschluss uber die Moglichkeiten bietet der Parameter . Geben Sie (verbose) an, erzahlt Ihnen das Programm, was es gerade macht.

#### Zeitraffer-Aufnahmen

raspistill kann auch fur **Zeitraffer-Aufnahmen** genutzt werden. Dazu muss beim Dateinamen ein Zahler festgelegt werden. Das geschieht durch einen Platzhalter, wie er bei der C-Funktion printf oder auch beim time-Kommando verwendet wird. Er hat die Form "%xxd", wobei fur xx die Zahl der Dezimalstellen eingesetzt wird. Damit spater beim Sortieren kein Mist entsteht, mussen alle Zahlenwerte gleich lang sein, denn sonst kommt "10" nach "1" und nicht die "2". Das wird durch eine fuhrende "0" erreicht. Fur beispielsweise vier Stellen schreibt man "%04d". Das ergibt dann insgesamt z. B. einen Dateiangabe wie "bild_%04d.jpg", die zu den Namen "bild_0001.jpg", "bild_0002.jpg" usw. fuhrt.

Im Fall von Zeitrafferaufnahmen wird mit -t die gesamt-Aufnahmedauer angegeben und mit -tl die Wartezeit zwischen zwei Aufnahmen (alle erfolgen wieder in Millisekunden). Mit dem folgendem Befehl wird eine Stunde lang (-t 3600000) alle 10 Sekunden (-tl 10000) ein Bild aufgenommen:
    
    
    raspistill -tl 10000 -t 3600000 -o camera/bild_%04d.jpg
    

Fur langere Sessions empfiehlt es sich, einen USB-Stick anzuschließen und die Bilder dort zu speichern, denn die SD-Karte ist unter Umstanden schnell voll.

Bei langeren Intervallen, z. B. nur eine Aufnahme pro Stunde verwendet man besser ein Shellscript, das per crontab aktiviert wird. Ein derartiges Script konnte etwa folgendermaßen aussehen:
    
    
    #!/bin/bash
    
    # Bilderverzeichnis
    IMGDIR='/home/pi/images'
    
    # Zeitstempel fuer Dateinamen generieren,
    # %s: Sekunden seit 1970-01-01 00:00:00 UTC
    TIME=$(date +%s)
    
    # Dateinamen erzeugen
    FILENAME=$IMGDIR/${TIME}.jpg
    
    # Foto erstellen,  die Parameter -w und -h
    # reduzieren die Dateigroesse
    raspistill -o $FILENAME -w 1024 -h 768 -n
    

Die zeitliche Planung der einzelnen Fotos wird per erledigt. Dazu geben Sie das Kommando ein und fugen ans Ende der Daten eine neue Zeile ein. Um beispielsweise alle halbe Stunde ein Foto zu machen, geben Sie ein:
    
    
    0,30 * * * * /home/pi/bin/zeitraffer.sh
    

Mehr Infos uber das -Kommando finden Sie im [UNIX-Skript](http://www.netzmafia.de/skripten/unix/unix4.html#4.3).

Aus den Einzelbildern soll nun ein Video entstehen. Es ist schon moglich, das Video auch auf dem Raspberry Pi erstellen zu lassen. Jedoch ist es sinnvoll, bei diesem Schritt einen etwas schnelleren Linux-Rechner zu verwenden - sofern verfugbar. Denn die Aufgabe erfordert einiges an Prozessorleistung.

Eine Moglichkeit, ein Zeitraffer-Video zu bekommen, ist aus den vielen Einzelbildern mittels ffmpeg ein Video erzeugen:
    
    
    ffmpeg -qscale 5 -r 4 -b 9600 -i camera/bild_%04d.jpg camera/filmchen.mp4
    

Eine weitere Moglichkeit bietet das Programm mencoder. Sie installieren dies und die entsprechenden Abhangigkeiten mit dem Kommando
    
    
    sudo apt-get -y install mencoder
    

Nun konnen Sie damit direkt auf dem Raspberry Pi das entsprechende Video erstellen. Das Kommando ist etwas langlich (auf drei Zeilen umbrochen):
    
    
    mencoder "mf://*.jpg" -mf type=jpg:fps=25 -ovc lavc -lav copts\
    vcodec=mpeg4:mbd=2:trell:vbitrate=8000 -vf scale=1280:720 -oac\
    copy -o filmchen.mp4
    

Beachten Sie, dass nach dem Backslash (\\) am Zeilenende kein weiteres Zeichen folgt, sondern nur die Enter-Taste gedruckt wird. Damit Sie nicht immer das ganze Kommando eingeben mussen, konnen Sie es auch in einem Shellscript verewigen.

Hinter dem Parameter "fps=" steht die Anzahl der Bilder pro Sekunde (Frames per Second). Ein Fernseher liefert 25 Bilder pro Sekunde, deshalb steht oben dieser Wert. Je hoher dieser Wert ist, desto mehr Bilder benotigen Sie fur die gleiche Dauer des Films. "scale=" legt die Auflosung des Videos fest. Im Beispiel wurde das Zeitraffervideo im HD-Format von 1280 x 720 Pixel vorliegen. Fur Full HD mussten Sie "1920:1080" angeben. Die Qualitat des Videos beeinflust die Zahl hinter "vbitrate=". Hier mussen Sie einfach etwas herumprobieren, bis der Film Ihren Anspruchen genugt.

Mit mencoder kann man eigentlich alles machen, was im Bereich Videobearbeitung moglich ist, nicht nur Zeitrafferfile erzeugen. Einige Beispiele sind die Umwandlung eines Videoformates in ein anderes, das Rippen von DVDs und Video-CDs, das separate Rippen einer Audiospur, die Aufzeichnung von TV-Sendungen uber eine TV-Karte, die Reskalierung von Filmen und vieles mehr. Einige Infos liefern folgende Webseiten:

  * [MEncoder Scripts](http://www.wiki.csoft.at/index.php/MEncoder_Scripts)

### Videos aufnehmen

Fur die Aufnahme von Videos wird raspivid verwendet. Das Programm kennt viele der Bildbarameter von raspistill, darunter -v, -w, -h, -o oder die Einstellungen von Kontrast, Helligkeit etc. Die Framerate kann mit -fpr (frames per second) eingestellt werden. Mit dem Parameter -t gibt man die Aufnahmezeit in Millisekunden an. Fur eine beliebig lange Aufnahme (z. B. fur einen Stream) wird der Wert auf 0 gesetzt (Default: 5 Sekunden). Das voreingestellte Videoformat ist 1080p (1920 x 1080 Pixel). Abgespeichert wird, wie erwahnt, im H264-Format. Die folgenden Beispiele erklaren die wichtigsten Parameter:
    
    
    # 10-Sekunden-Video in 1080p (1920 x 1080)
    raspivid  -t 10000 -o video.h264
    
    # 10-Sekunden-Video in 720p (1280 x 720)
    raspivid -t 10000 -w 1280 -h 720 -o video.h264
    
    # 10-Sekunden-Video mit individueller Bitrate (3 MBits/s)
    raspivid -t 10000 -b 3000000 -o video.h264
    
    # 10-Sekunden-Video mit individueller Framerate (10 Frames/Sekunde)
    raspivid -t 10000 -f 10 -o video.h264
    
    # 10-Sekunden-Videostream an stdout schicken (Dateiname ist "-")
    raspivid -t 10000 -o -
    

Um das erzeugte H264-Video in das gebrauchlichere MPEG4-Format umzuwandeln, greifen wir auf das Zusatzpaket gpac zuruck, das sich unter Raspbian mittels apt-get installieren lasst. Die Konvertierung erfolgt dann z. B. mit:
    
    
    MP4Box -fps 30 -add video.h264 video.mp4
    

Die Homepage von ist [ gpac.wp.mines-telecom.fr/](http://gpac.wp.mines-telecom.fr/). Das Paket besteht aus einem Multimedia-Player, der "Osmo4" bzw. "MP4Client" heisst, einem Multimedia-Packager, "MP4Box", der oben zur Anwendung kommt und einigen Servertools.

#### ffmpeg einrichten

Zum Codieren von AVI-Videos nach MP$ (H.264) wird gerne das Kommandozeilenprogramm ffmpeg verwendet, das leider beim RasPi nicht als fertiges Binary verfugbar ist (Stand: Anfang 2017). Deshalb muss man sich das Programm aus den Quelltexten selber bauen. Zuerst holen und compilieren Sie die H.264-Bibliothek und anschliessend ffmpeg. Fur die Quelldateien etc. richten Sie am Besten ein eigenes Arbeitsverzeichnis ein (eventuell mussen Sie zuvor auch noch git per apt-get install git einrichten). Beachten Sie, dass nach dem '\' am Zeilenende nur noch das Newline folgen darf (keine Leerzeichen):
    
    
    # Arbeitsverzeichnis einrichten
    mkdir -p ~/Work
    
    # Bibliothek bauen
    cd ~/Work
    git clone --depth 1 git://git.videolan.org/x264
    cd x264
    sudo ./configure \
        --host=arm-unknown-linux-gnueabi\
        --enable-static\
        --disable-opencl
    make -j 4
    sudo make install
    
    # ffmpeg bauen
    cd ~/Work
    git clone --depth 1 git://source.ffmpeg.org/ffmpeg.git
    cd ffmpeg
    sudo ./configure \
        --arch=armel\
        --target-os=linux\
        --enable-gpl\
        --enable-libx264\
        --enable-nonfree
    make -j 4
    sudo make install
    

Das kann auf dem RasPi 3 eine gute halbe Stunde dauern, auf dem RasPi 1 mussen Sie mit mehr als zwei Stunden rechnen. Bei letzteren helfen auch die viel parallelen Jobs nicht (), weil es nur einen Kern gibt.

### Streaming auf ein anderes System

Sie konnen, falls der RasPi ohne Grafik lauft, die Videos auch gleich auf einen anderen Linux-Rechner streamen. Dafur kommt das "Schweizer Taschenmesser des Internets", Netcat zum Einsatz. Netcat kann auch wieder mit apt-get installiert werden. Auf dem Raspberry wird der Video-Stream in Netcat (nc) geleitet, das fur die Übertagung zum fernen Client mit der IP-Adresse 10.1.1.1 sorgt. Als Portnummer wird hier 4711 verwendet:
    
    
    raspivid  -w 1280 -h 720 -t 0 -o - | nc 10.1.1.1 4711
    

Auf dem Linux-Client wird zusatzlich zu Netcat der Videoplayer MPlayer (oder VLC oder was auch immer) installiert, um den Stream direkt auf der grafischen Oberflache anzuzeigen. Netcat lauft hier im Servermodus und wartet auf dem Port 4711 auf die Anfrage des RasPi (beim mplayer wird die Standardeingabe durch den Dateinamen "-" reprasentiert):
    
    
    nc -l -p 4711 | mplayer -fps 31 -cache 1024 -
    

Übrigens wurde die Darstellung auch auf einer Windows-Kiste funktionieren, weil Netcat und Mplayer/VLC auch fur Windows verfugbar sind.

### Programmierung

Im Prinzip reichen die beiden Kommandozeilentools vollkommen aus. Will man die Kamera jedoch in eigene Programme einbinden ist es manchmal lastig und nicht zuletzt fehleranfalliger, mit Systemaufrufen zu hantieren. So ist es erfreulich, dass im Python-Modul "Picamera" alle Optionen der Kamera vollstandig implementiert. Die Links [im ersten Abschnitt](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_Kamera.html) fuhren zur Software und zur Dokumentation. Zu installieren ist das Paket python-picamera. Danach steht dann die Library picamera zur Verfugung.

Die Library bietet nicht nur viele Konfigurationsmoglichkeiten (brightness, contrast, saturation, image effects, exposure modes etc.) sondern erlaubt auch das Kamerabild live anzuzeigen. Naturlich sind, wie auf der Kommandozeile auch Captures und Videos moglich. Ich gestehe auch, dass die Beispiele von der Dokumentation des Moduls inspiriert wurden.
    
    
    camera.sharpness = 0
    camera.contrast = 0
    camera.brightness = 50
    camera.saturation = 0
    camera.ISO = 0
    camera.video_stabilization = False
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    camera.rotation = 0
    camera.hflip = False
    camera.vflip = False
    camera.crop = (0.0, 0.0, 1.0, 1.0)
    

Die komplette Dokumentation fur finden Sie unter [picamera.readthedocs.org](http://picamera.readthedocs.org/).

Beim ersten Python-Programm handelt es sich um ein Pendant des Kommandozeilenaufrufs oben. Nach dem Importieren der benotigten Module wird ein Kamera-Objekt erzeugt, die Auflosung eingestellt und ein Bild geschossen:
    
    
    import picamera
    from time import sleep
    
    cam = picamera.PiCamera()
    cam.resolution = (640, 480)
    cam.start_preview()
    time.sleep(5)
    cam.stop_preview()
    cam.capture('bild.jpg')
    cam.close()
    

Falls bei der Aufnahme auftretende Fehler abgefangen werden sollen (wenn beispielsweise die Kamera deaktiviert ist, kann man einen try-Block verwenden:
    
    
    import picamera
    from time import sleep
    
    cam = picamera.PiCamera()
    try:
       cam.resolution = (800, 600)
       cam.start_preview()
       time.sleep(2)
       cam.stop_preview()
       cam.capture('bild.jpg')
    finally:
       cam.close()
    

Oder Sie verwenden das context manager protocol und mussen so keine KameraInstanz anlegen. In folgenden Beispiel wird angenommen, dass die Kamera kopfunter an der Decke hangt - kein Problem, wir vertauschen einfach oben und unten sowie rechts und links:
    
    
    import picamera
    from time import sleep
    
    with picamera.PiCamera() as cam:
    try:
       cam.vflip = True
       cam.hflip = True
       cam.resolution = (800, 600)
       cam.start_preview()
       time.sleep(2)
       cam.stop_preview()
       cam.capture('bild.jpg')
    finally:
       cam.close()
    

Sie konnen auch einmal mit Kameraparametern experimentieren und sich ansehen, was geschieht, wenn Sie die Helligkeit von 0 auf 100 Prozent hochregeln:
    
    
    import picamera
    from time import sleep
    
    with picamera.PiCamera() as cam:
       cam.resolution = (800, 600)
       cam.start_preview()
       for i in range(100):
          cam.brightness = i
          time.sleep(0.2)
       cam.stop_preview()
       cam.close()
    

Mit Python konnen Sie aber noch wesentlich mehr anfangen. Das folgende Beispiel skizziert, wie sich das Kamerabild weiter nutzen lasst. Mit Hilfe des Moduls pygame haben Sie ruck-zuck ein Bildschirmfenster, in dem dann das gerade geschossene Bild angezeigt und mit dem Aktuellen Datum nebst Uhrzeit beschriftet wird. Erweiterungen seien Ihrer Phantasie uberlassen:
    
    
    import picamera
    import time
    import pygame
    
    # Voreinstellungen
    WIDTH=1280
    HEIGHT=1024
    FONTSIZE=50
    
    # Kamera initialisieren
    camera = picamera.PiCamera()
    camera.vflip = False
    camera.hflip = False
    camera.brightness = 60
    
    # Bildschirmfenster aufbauen, Hintergrund schwarz, Schrift weiss
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    black = pygame.Color(0, 0, 0)
    textcol = pygame.Color(255, 255, 0)
    screen.fill(black)
    
    while True:
        # Bild machen, als GIF speichern, gleiche Größe wie Fenster
        camera.start_preview()
        sleep(1)
        camera.capture('image.gif', format='gif', resize=(WIDTH,HEIGHT))
        camera.stop_preview()
    
        # altes Bild löschen
        screen.fill(black)
        pygame.display.update()
    
        # Bild einlesen und anzeigen
        img = pygame.image.load('image.gif')
        screen.blit(img, (0, 0))
    
        # Datum und Uhrzeit darüber legen
        font = pygame.font.Font('freesansbold.ttf', FONTSIZE)
        text = time.strftime("%d.%m.%Y um %H:%M:%S Uhr")
        font_surf = font.render(text, True, textcol)
        font_rect = font_surf.get_rect()
        font_rect.left = 100
        font_rect.top = 100
        screen.blit(font_surf, font_rect)
        pygame.display.update()
    
        # etwas warten
        sleep(5)
    
    # aus die Maus
    camera.close()
    pygame.quit()
    

Die Aufzeichnung von Videos erfolgt nach einem ahnlichen Schema. Hierzu bauen wir den Kommandozeilenaufruf fur die Videoaufzeichnung nach. Die Methoden start_recording() und stop_recording() steuern die Aufzeichnung. Auch hier mussen Sie, sofern gewunscht, ein Vorschaufenster explizit anfordern und wieder schließen. Die Aufnahmedauer wird uber wait_recording() eingestellt. Die Methode pruft auch kontinuierlich, ob der Speicherplatz auf der SD-Karte fur die Aufzeichnung noch ausreicht, und bricht die Aufnahme notfalls ab. Das folgende Beispiel zewichnet 30 Sekunden auf:
    
    
    import picamera
    from time import sleep
    
    with picamera.PiCamera() as cam:
       cam.start_preview()
       cam.start_recording('filmchen.h264')
       cam.wait_recording(30)
       cam.stop_recording()
       cam.stop_preview()
       cam.close()
    

Mit den bisher vorgestellten Programmen entstehen unter Umstanden Unmengen total uninteressanter Bilder oder sinnlose Videos. Man konnte als Kriterium fur Bewegungen vor der Kamera deutliche Änderungen in der beobachteten Szene heranziehen, also wenn zwei aufeinanderfolgende Bilder sich deutlich unterscheiden. Leichtes "flattern" von Blattern eines Baums oder die Nachbarkatze sollen aber unbeachtet bleiben.

Bei vielen Webcams kann man mit der [ Software Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) arbeiten, die auf dem Standard-Linux-Videostack Video4linux basiert. Scheinbar unterstutzte die Picam das aber nicht. Jedoch gibt es ein Python-Programm ([ http://www.raspberrypi.org/phpBB3/viewtopic.php?t=45235](http://www.raspberrypi.org/phpBB3/viewtopic.php?t=45235)), das zwar sehr viel einfacher gehalten ist, aber in der Regel ausreicht. Das Programm nimmt Bilder auf und speichert sie mit einemZeitstempel im Dateinamen. Dann vergleicht es in einem niedrig auflosenden Stream immer zwei aufeinanderfolgende Bilder. Überschreiten die Veranderungen einen Schwellenwert, speichert der Pi das entsprechende hochauflosendes Bild.

Wenn man externe Programme ausnutzt, laßt sich auch ein Zeitlupeneffekt realisieren. Zunachst wird mit raspivid ein Video mit der hochstmoglichen Framerate aufgezeichnet (beim RasPi sind dies 90 Bilder pro Sekunde). Weitere Parameter des Programmaufrufs sind '-w' und '-h' fur die Bildgroße, '-t' fur die Dauer, '-o' fur die Ausgabedatei im H264-Format und naturlich '-fps' fur die Framerate. Die so erzeugte Datei myvid.h264 wird danach mit dem Programm MP4Box ins MP4-Format konvertiert.
    
    
    import os
    import time
    
    print("Aufnahme gestartet - 30 s.")
    os.system("raspivid -w 640 -h 480 -fps 90 -t 30000 -o myvid.h264")
    print("Aufnahme beendet")
    print("Konvertierung gestartet.")
    os.system("rm -f myvid.mp4")
    os.system("MP4Box -add myvid.h264 myvid.mp4")
    print("Konvertierung abgeschlossen.")
    

Wie Sie sehen, ist auch die Programmierung des Kamera-Interfaces mit Python nicht allzu schwierig. Viel Spass beim Experimentieren.

### Die NoIR-Kamera

Fur den RasPi gibt es ja zwei Kamera-Module, die normale Kamera und die NoIR-Kamera mit schwarzer Platine. "NoIR" steht fur "No Infra Red (Filter)". Normalerweise haben Kameras einen eingebauten Infrarot-Filter, der die infraroten Anteile des Bildes unterdruckt und die deshalb Fotos liefern, die naturliche Farben wiedergeben. Die NoIR-Kamera ermoglicht Fotoeffekte, die auf dem Infrarot-Anteil des Lichts setzen. Der fehlende Infrarotfilter und ist vor allem fur die Fotografie bei schlechten Lichtverhaltnissen oder fur Infrarotaufnahmen in der Dunkelheit geeignet. Man kann sie aber auch fur atmospharische Bilder bei Tageslicht einsetzen.

Fur Infrarot-Effekte bei Tageslicht braucht man aber wieder einen entsprechenden Filter vor dem Objektiv, der einerseits moglichst viel Normallicht aussperrt und auf der anderen Seite einen moglichst hohen IR-Anteil durchlasst. Die NoIR-Kamera lasst einen genugend großen Anteil von Infrarotlicht zu ihrem Bildsensor passieren. Somit gelangt alles Infrarotlicht auf den Sensor, und die Belichtungszeiten werden nicht so hoch wie bei anderen Kameras mit IR-Filter. So kann man auch draussen fotografieren, wenn es nicht ganz windstill ist. Als Filter kommt u. a. der Polaroid Filter IR720 in Frage. Er filtert das meiste Licht unterhalb und oberhalb der Wellenlange von 720 Nanometern (Nah-Infrarot), also das meiste sichtbare Licht. So lassen sich sogar Falschfarben-Aufnahmen machen. Gegebenenfalls muss der Weissabgleich nachtraglich mit einer Bildverarbeitungssoftware gemacht werden.

### Neue Raspberry-Pi-Kamera

Die Raspberry Pi Foundation hat im Mai 2016 eine neue Version der Kamera fur den RasPi vorgestellt. Der Grund dafur liegt darin, dass die bislang in der Kamera eingebauten OmniVision-OV5647-Sensoren mit funf Megapixeln seit Ende 2014 nicht mehr hergestellt werden. Im neuen Kameramodul V2.1 kommt der Sensor IMX219 von Sony zum Einsatz, der acht Megapixel Auflosung hat und zudem bessere Farben und eine hohere Bildqualitat liefert.

![](http://www.netzmafia.de/skripten/hardware/RasPi/cam4.jpg)

> _(Bild: Raspberry Pi Foundation)_

Die Kamera sitzt wie schon das erste Modell auf einer winzigen Platine und wird durch ein Flachbandkabel mit dem CSI-Port des Raspberry Pi verbunden. Das Modul soll mit denModellen 2 und 3 sowie den alteren Modellen A+ und B+ kompatibel sein. Neben der normalen Kamera ist auch wieder eine NoIR-Version erhaltlich. Die neue Kamera beherrscht auch einen automatischen Weißabgleich. Er wird durchgefuhrt, wahrend die rohen Sensordaten die Image Sensor Pipeline (ISP) durchlaufen dabei in Digitalbilder umgewandelt werden. Es sollen dabei auch Objektivverzerrungen, Rauschen oder fehlerhaften Pixel korrigiert werden. Einzelbilder sind mit einer Auflosung von maximal 3280 x 2464 Pixeln moglich. Videos mit 1080p kann die Kamera mit 30 Frames pro Sekunde (fps) aufnehmen, bei 720p liegt die maximale Bildrate bei 60 fps.  
Quelle: [ www.raspberrypi.org/blog/new-8-megapixel-camera-board-sale-25](https://www.raspberrypi.org/blog/new-8-megapixel-camera-board-sale-25/)

Bei einigen Kameramodulen zeigten sich Unscharfen bei der Abbildung. Der Raspberry-Pi-Grunder Eben Upton merkte dazu an, die ausgelieferten Exemplare des neuen Kameramoduls fur den Einplatinenrechner seien alle fur sich gesehen in Ordnung, nur jeweils unterschiedlich fokussiert. Inzwischen hat der Raspberry-Pi-Forums-Nutzer _caerandir_ eine einfache Losung demonstriert, mit der man den Fokus der Kamera anpassen kann. Prinzipiell geht es dabei darum, die Linse aus ihrer festen Verklebung zu befreien. Dazu bediente er sich einer Plastikkarte, bohrte ein ca. 5 Millimeter großes Loch hinein und versah es mit kleinen Aussparungen fur die Noppen an der Linse. Durch etwas Druck mit der modifizierten Plastikkarte auf die Linse kann man sie losdrehen. Anschließend kann man sie vorsichtig mit einer kleinen Zange fokussieren. Das Bild zeigt verschiedene Varianten das "Wekzeugs". Wie man sieht, kommt es nicht auf Schonheit an.

![](http://www.netzmafia.de/skripten/hardware/RasPi/kamera_justage.jpg)

### Infrarot-Scheinwerfer

Nachdem das zweite Kameramodell fur Infrarotlicht geeignet ist, soll sie auch nachts etwas "sehen"? Dabei hilft ein kleiner Infrarot-Scheinwerfer. Der hier vorgestellte Eigenbau-Infrarot-Scheinwerfer besteht aus 40 preiswerten Infrarot-LEDs und acht Widerstanden. Er lasst sich auch vom Lotanfanger ganz einfach auf einer Lochrasterplatte aufbauen. Profis machen sich naturlich eine Platine, insbesondere wenn mehr als ein Scheinwerfer gebraucht wird. Bei 12 V Versorgungsspannung nimmt der Scheinwerfer ca. 200 mA auf, er sollte also ggf. vom Computer aus ein- und ausgeschaltet werden konnen (per Relais oder MOSFET-Schalttransistor). Die Schaltung des Scheinwerfers ist so einfach, das im folgenden Bild nur die Verdrahtung gezeigt werden muss. Es werden jeweils 5 LEDs und ein 100-Ohm-Widerstand in Reihe geschaltet.

Fur den Außeneinsatz muss dann noch ein passendes Gehause mit Klarsichtdeckel spendiert werden.

### Die Pi-Cam-Optik aufrusten

#### Kamera- und Optik-Grundlagen

Bei der Objektivauswahl bildet der Kameraanschluss und damit der Abstand des Bildsensors zur Auflagekante der Kamera (**Auflagemass**) ein wichtiges Kriterium. Die bildseitige Schnittweite, der Abstand der Bildebene von der hintersten optischen Flache des Objektivs, muss immer großer als das Auflagemass der Kamera sein. Ware sie kleiner, wurde immer vor dem Bildsensor fokussiert werden. Die Schnittweite ist durch das verwendete Grunddesign der Optik vorgegeben. Die meisten Kameraund Objektivhersteller haben sich auf ein oder mehrere Anschlusssysteme festgelegt.

Fur industrielle Objektive gibt es mehrere Standards. Die **C- und CS-Mount**-Anschlusse besitzen ein Gewinde mit 1"x32 TPI (tracks per inch) Steigung. Nach amerikanischer Norm (ANSI) wird dieses Gewinde auch mit 1-32UN-2B angegeben. Die Objektive besitzen das Gegenstuck mit der Bezeichnung 1-32UN-2A. Die Anschlusse C- und CS-Mount unterscheiden sich allein durch das Auflagemaß. Der C-Mount hat ein Auflagemaß von 17,53 mm, wahrend der CS-Mount 5 mm kurzer ist, und damit 12,53 mm von der Mechanikkante zum Sensor misst.

Das **S-Mount**-Feingewinde M12x0,5 eignet sich besonders fur Miniaturkameras oder abgesetzte Kamerakopfe. Diese Kameras werden uberwiegend in Kombination mit sehr kurzbrennweitigen Objektiven eingesetzt. Das Objektiv hat auch eine kurze bildseitige Schnittweite, somit muss das Objektiv sehr nahe am CCD-Chip sitzen. Über das Feingewinde lasst sich das Auflagemaß des Objektivs zur Kamera exakt einstellen und ist leicht uber einen Konterring zu fixieren. Einen genormten Abstand zum CCD-Sensor gibt es nicht.

Der **F-Mount**-Anschluss bezeichnet das Bajonett-System der Fa. Nikon, das bereits Ende der 50er Jahre entwickelt wurde. Das Auflagemaß betragt hier 46,5mm. Der F-Mount-Anschluss wird vor allem fur High Tech-Kameras mit besonders großen Sensoren benotigt, die eine besonders hohe Auflosung bei großen Pixeln bieten. Dies gilt fur industrielle Flachen- und Zeilenkameras.

Die folgende Tabelle fasst die Auflagenmaße zusammen.

C-Mount
17,5 mm

CS-Mount
12,5 mm

F-Mount
46,5 mm

S-Mount
undef.

Objektive enden von den Abmessungen her selten an der Auflageflache der Kamera, sondern tauchen daruber hinaus mit der letzten Linsengruppe in das Kameragehause ein (siehe Bild oben). Die **Schnittweite** bezeichnet hierbei das Maß vom Scheitelpunkt der letzten Linse bis zum Bildsensor. Besonders bei weitwinkligen tritt das haufig auf.

Ein Objekt vor der Kamera wird nur innerhalb bestimmter Grenzen scharf abgebildet. Die **Scharfentiefe** ist der Motivraum, der auf dem von der Kamera erzeugten Bild ausreichend scharf erscheint. In der folgenden Grafik wurde die Optik so fokussiert, dass das Objekt 1 scharf als Bild 1 auf dem Sensor abgebildet wird. Ein Gegenstand, der sich naher an der Optik befindet, erzeugt einen Scharfepunkt, der hinter dem Sensor liegt und daher ein unscharfes Bild. Ein ideal scharfes Pixel verschwimmt zu einem großeren Lichtfleck, dem Unscharfebereich (Unscharfekreis). Durch ein Nachfokussieren auf diesen Arbeitsabstand wurde die Linsengruppe vom Sensor wegbewegt, um wieder ein scharfes Bild zu erzeugen. Beim S-Mount kann das Nachfokussieren sehr einfach durch Heraus- oder Hineinschrauben des Objektivs erreicht werden.

Fur ein Kamerasystem mit festen mechanischen Dimensionen hat dagegen ausschließlich die Objektivblende einen Einfluss auf die Scharfentiefe. Schließt man die Blendenoffnung des Objektivs, nimmt die Scharfentiefe zu. Eine hohere Blendenzahl (= kleinere Öffnung) hat jedoch eine langere Belichtungszeit zur Folge. Die internationale Blendenskala ist so konzipiert, dass jede Stufe eine Halbierung bzw. Verdoppelung der der Belichtungszeit bedeutet. Durch Abblenden der Optik wird der Unscharfebereich auf dem Bildsensor kleiner. Die Objekte 1 und 2 konnen jetzt also viel weiter raumlich auseinander liegen, um denselben Unscharfebereich zu erzeugen.

Die Scharfentiefe ist umso großer

  * je weiter ein Objekt von der Kamera entfernt ist (fast parallele Lichtstrahlen fur beide oben gezeigten Abbildungsfalle), 
  * je kleiner die Brennweite der Optik ist. (es gilt auch: je kleiner der Sensor ist, desto kleinere Brennweiten benotigt er), 
  * je kleiner die eingestellte Blendenoffnung ist (siehe Bilder oben). 

Die exakte Berechnung der Ausdehnung der Scharfentiefe erfordert betrachtliche Rechnerei. Die folgenden Gleichungen sind bereits vereinfachte Naherungsgleichungen. Die Bildscharfe und Scharfentiefe hangen stark von der optischen Konstruktion und ggf. optischen Fehlern ab.

Die **hyperfokale Distanz:** bezeichnet die Gegenstandsweite, bei der im Unendlichen liegende Objekte gerade noch mit einer akzeptablen Scharfe abgebildet werden, wenn genau auf diese Gegenstandsweite scharf gestellt wurde. Die Scharfentiefe reicht dann von der halben hyperfokalen Distanz bis Unendlich. Fur die nachfolgenden Formeln muss zuerst die hyperfokale Distanz berechnet werden:

**hyperfokale Distanz:** H = (f´* f´) / (N * c) + f´

Mit Hilfe von H konnen die folgenden Werte berechnet werden:

**Nahpunkt fur akzeptable Bildscharfe:** gn = G * (H - f´) / (H + g - 2 * f´)

**Fernpunkt fur akzeptable Bildscharfe:** gf = G * (H - f´) / (H - g)

**Gesamte Scharfentiefe:** gn \- gf

Dabei sind:

H
Hyperfokale Distanz in mm  


gn
Nahdistanz bei akzeptabler Bildscharfe in mm  


gf
Ferndistanz bei akzeptabler Bildscharfe in mm  


G
Gegenstandsweite  


f´
Brennweite des Objektivs in mm

N
Blendenzahl der Optik

c
Unscharfekreis in mm, typischerweise zweifache Pixelgroße

Quelle: Greenleaf, Allen R.: Photographic Optics, The MacMillan Company.

#### Die Pi-Cam umbauen

Informationen uber die Kamera des Raspberry Pi inklusive der Justierung der Kameralinse finden Sie weiter oben. Um nun die Kamera mit einem neuen Objektiv auszurusten ist etwas Bastelei erforderlich. Am besten eigen sich die S-Mount-Objektive mit M12-Gewinde, die recht preiswert (etwa 5 - 20 Euro) bei diversen Herstellern und auch bei Amazon oder Ebay erhaltlich sind. Fur diese Objektive gibt es auch Halter aus Kunststoff, die auf dem Kamerasensor befestigt werden. Auf dem folgenden Bild sehen Sie zwei Typen, die beide nach etwas Nacharbeit fur die Pi-Cam geeignet sind, wobei die unteren Typen mit abgeschragten Ecken noch etwas besser passen.

Doch zuerst muss die alte Optik entfernt werden. Wie das Abschrauben funktioniert, steht weiter oben unter "Neue Raspberry-Pi-Kamera". Achten Sie beim Abmontieren der Originaloptik darauf, dass der Sensor unbeschadigt bleibt. Der neue Objektiv-Anschluss passt wie fur die Pi-Cam gemacht, es lassen sich sogar die Befestigungslocher auf der Pi-Cam zm Fixieren des Gewindes verwenden.

Bevor Sie den M12-Anschluss auf die Pi-Cam setzen konnen, ist noch etwas Nacharbeit notwendig: Auf der Seite des Flachkabel-Anschlusses muss der M12-Anschluss etwas ausgespart werden. Mit einer feinen Feile wird eine Vertiefung in die eine Seitenwand des Anschlussgehauses eine Aussparung gefeilt, sodass das M12-Gehause plan auf der Platine aufliegt.

Beim quadratischen M12-Anschluss muss ggf. auch noch auf einer Ecke etwas gefeilt werden, damit die Bauteile R9 und D1 nicht gequetscht werden. Das M12-Gehause mit abgeschragten Ecken erfordert hier keine Nacharbeit.

Ob Sie den M12-Anschluss dann auf das Pi-Cam-Board kleben oder mit den seitlichen Ösen festschrauben, bleibt Ihnen uberlassen. Nun kann das Wunsch-Objektiv eingeschraubt und scharfgestellt werden. Zum Fixieren des Objektivs in der gewunschten Scharfeposition reicht in der Regel ein Tropfchen Nagellack auf Gewinde und Gehause. Wenn sich gar kein scharfes Bild einstellen lasst, hift entweder ein M12-Zwischenring (Objektiv weiter weg vom Sensor) oder Abfrasen eine Stucks vom Gewindeteil (Objektiv naher am Sensor). Das ist aber nur bei ganz exotischen Anwendungen notig.

Duch das M12-Gewinde kann man auch zwischen Weitwinkel-, Tele- oder Makroobjektiv wechseln - je nach Anwendungsfall. Fur diee Beleuchtung in Nhbereich kann man sich dann noch ein Ringlicht aus weißen LEDs basteln.

### Links

Allgemeine und weiterfuhrende Informationen zum Betrieb von Webcams unter Linux und zu M12-Objektiven finden Sie unter

_Copyright (C) Hochschule Munchen, FK 04, Prof. Jurgen Plate_
