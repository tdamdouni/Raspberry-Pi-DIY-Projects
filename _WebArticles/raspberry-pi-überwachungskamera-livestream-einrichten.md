# Raspberry Pi: Überwachungskamera Livestream einrichten

_Captured: 2017-03-04 at 23:25 from [tutorials-raspberrypi.de](https://tutorials-raspberrypi.de/raspberry-pi-ueberwachungskamera-livestream-einrichten/)_

![Raspberry Pi Überwachungskamera Livestream](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Überwachungskamera-Livestream-700x432.png)

Nachdem wir mit (USB) Kameras / Webcams bereits [einzelne Bilder aufnehmen](http://tutorials-raspberrypi.de/raspberry-pi-ueberwachungskamera-webcam/) konnen, wollen wir auch Live Bilder ansehen. Dies kann entweder am Smartphone stattfinden oder an einem PC außerhalb des heimischen Netzwerks. Dazu konfigurieren wir mit der Raspberry Pi Überwachungskamera einen Livestream. Das Tolle daran ist, dass fast jede USB Kamera (also auch Webcams) benutzt werden konnen. Je nach Platzierung, kann z.B. eine Kamera ohne Infrarot Filter sinnvoll sein, um so bessere Nachtaufnahmen zu ermoglichen.

## Zubehor

![Raspberry Pi Überwachungskamera Livestream NoIR](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Überwachungskamera-Livestream-NoIR-180x120.jpg)

> _Der fehlende IR Filter sorgt fur eine hohere Lichtempfindlichkeit._

Falls wir eine USB Kamera anschließen wollen, muss unser [Raspberry Pi](https://tutorials-raspberrypi.de/goto/Raspberry_Pi/3439/) naturlich einen freien USB Port besitzen. Allerdings konnen wir auch die offizielle Kamera nutzen, welche es in zwei Ausfuhrungen gibt:

  * [Standardvariante](https://tutorials-raspberrypi.de/goto/Standardvariante/4161/) (grun), welche u.a. 8MP hat und u.a. Videos in 1080p aufnehmen kann. Da ein Infrarot Filter eingebaut ist, eignet sie sich besonders fur Tageslicht Aufnahmen bzw. fur Orte mit genugend Lichteinstrahlung.
  * [NoIR Variante](https://tutorials-raspberrypi.de/goto/NoIR_Variante/4163/) (schwarz): Die Spezifikationen (Auflosung, etc.) sind identisch, allerdings ist kein IR Filter eingebaut, wodurch Aufnahmen mit wenig Licht besser erscheinen. Dies empfiehlt sich besonders bei dunklen Szenen.

Beide Kameras konnen direkt uber den CSI Anschluss auf der Platine [angeschlossen werden](http://tutorials-raspberrypi.de/aufnahmen-mit-dem-offiziellen-kamera-modul-des-raspberry-pi/), wodurch kein USB Port belegt wird. Die neueren Zero Modelle (ab Generation 2) besitzen nun auch CSI Ports.

Alternativ kann auch eine beliebige [USB Webcam](https://tutorials-raspberrypi.de/goto/USB_Webcam/4164/) benutzt werden, solange entsprechende Treiber fur Linux vorhanden sind. Dies ist aber bei fast allen neueren Kameras der Fall. Sollte unser Raspberry Pi keinen integrierten [WLAN Adapter](https://tutorials-raspberrypi.de/goto/WLAN_Adapter/4165/) haben, brauchen wir ggf. noch einen solchen, da eine Netzwerk- bzw. Internetverbindung unumganglich ist.

## Vorbereitungen fur den Livestream treffen

Bevor wir den Stream unserer Raspberry Pi Kamera bzw. USB Webcam anlegen, mussen wir die Pakete aktualisieren:
    
    
    sudo apt-get update
    sudo apt-get upgrade

Anschließend kann das Tool [Motion](http://lavrsen.dk/foswiki/bin/view/Motion/WebHome) installieren, welches den Livestream moglich macht.
    
    
    sudo apt-get install motion -y

Die Installation wird nun ein wenig dauern.

Hat soweit alles geklappt, so kann die Kamera angeschlossen werden (falls nicht bereits geschehen). Falls du eine USB Webcam nutzt, kannst du prufen, ob sie erkannt wurde:
    
    
    lsusb

Sofern keine speziellen Treiber notwendig sind, sollten mit folgendem Befehl alle angeschlossenen Videogerate / Kameras angezeigt werden:
    
    
    ls /dev/video*

Falls du eine der offizielen Kamera Module verwendest, ist es wichtig folgendes auszufuhren, damit die Kamera gleich angezeigt wird (am besten per [Autostart](http://raspberrypi.stackexchange.com/questions/27737/unable-to-open-video-device-and-grey-screen)):
    
    
    sudo modprobe bcm2835-v4l2

Ist nur eine einzige Webcam / Raspberry Pi Kamera angeschlossen, sollte Device `/dev/video0` angegeben sein. Falls du mehrere Gerate angeschlossen hast, musst du im folgenden das Gerat auswahlen, welches den Stream ubertragen soll.

## Raspberry Pi Livestream konfigurieren

Fur die weiteren Schritte, in denen wir einige Einstellungen festlegen, schauen wir uns die Kamera Details an:
    
    
    v4l2-ctl -V

Fur meine USB Webcam habe ich folgende Ausgabe erhalten. Die Informationen zur Auflosung usw. werde ich gleich in der Konfigurationsdatei angeben.
    
    
    pi@raspberrypi:~ $ v4l2-ctl -V
    Format Video Capture:
            Width/Height  : 640/480
            Pixel Format  : 'YUYV'
            Field         : None
            Bytes per Line: 1280
            Size Image    : 614400
            Colorspace    : SRGB
            Flags         :

Bearbeiten wir also die Konfigurationsdatei von Motion:
    
    
    sudo nano /etc/motion/motion.conf

Folgende Zeilen mussen angepasst werden (die Variable kann mit STRG+W gesucht werden, die hinteren Werte wurden geandert):
    
    
    # Start in daemon (background) mode and release terminal (default: off)
    **daemon on**
    ...
    # Restrict stream connections to localhost only (default: on)
    **stream_localhost off**
    ...
    # Target base directory for pictures and films
    # Recommended to use absolute path. (Default: current working directory)
    **target_dir /home/pi/Monitor**

Folgene Zeilen sind optimal und sollten auch geandert werden (haben wir vorher ausgelesen):
    
    
    **v4l2_palette 15**     # Nummer aus der Tabelle davor entnehmen, 15 enstpricht YUYV
    ... 
    # Image width (pixels). Valid range: Camera dependent, default: 352 **
    width 640** 
    
    # Image height (pixels). Valid range: Camera dependent, default: 288 
    **height 480** # Maximum number of frames to be captured per second. 
    
    # Valid range: 2-100. Default: 100 (almost no limit). 
    **framerate 10 **

Gespeichert wird mit STRG+O und geschlossen mit STRG+X. Weitere Optionen (Port, etc.) konnen auch noch im Nachhinein angepasst werden (erfordert einen Neustart). Die Kurzbeschreibung der Einstellungen ist dabei aber recht aufschlussreich.

Jetzt mussen wir nur noch den Daemon aktivieren, damit wir den Service gleich laufen lassen konnen:
    
    
    sudo nano /etc/default/motion

Hier ersetzen wir „no" mit „yes", womit folgender Text dort steht (ohne Kommentar):
    
    
    start_motion_daemon=yes

Nun mussen wir den Ordner, den wir vorher als Speicherort fur die aufgenommen Frames angegeben haben, noch erstellen und diesem die notigen Schreibrechte erteilen:
    
    
    mkdir /home/pi/Monitor
    sudo chgrp motion /home/pi/Monitor
    chmod g+rwx /home/pi/Monitor

Anschließend konnen wir den Service bereits starten:
    
    
    sudo service motion start

## Raspberry Pi Überwachungskamera Livestream testen

Um zu testen, ob unsere Kamera nun auch wirklich Livebilder sendet, haben wir prinzipiell zwei Moglichkeiten: Die eine Moglichkeit ist einfach den Browser (Mozilla Firefox, Chrome, etc.) zu verwenden und den Namen des Raspberry Pi's, gefolgt vom Port (Standard: 8081) anzugeben. Wenn du den Hostnamen und Port nicht geandert hast, solltest du hieruber den Stream sehen konnen: <http://raspberrypi:8081/> (alternativ kann die lokale IP Adresse verwendet werden, wie z.B. 192.168.1.51:8081).

Manche altere Browser unterstutzen diesen Stream allerdings nicht (Internet Explorer lasst grußen ). Jene Nutzer konnen sich den Livestream z.B. uber den [VLC Player](http://www.videolan.org/vlc/) ansehen. Dazu einfach den VLC Player offnen und im Menu unter „Medien" -> „Netzwerkstream offnen" (STRG + N) die oben angegebene Adresse angeben. Dies ist im Übrigen auch im VLC Player fur Smartphones und Tablets ([Android](https://play.google.com/store/apps/details?id=org.videolan.vlc), [Apple](https://itunes.apple.com/de/app/vlc-for-mobile/id650377962?mt=8)) moglich. Dazu im Menu auf „Medienadresse offnen"und die IP Adresse inkl. Port angeben.

Je nach angegebener Framerate (in der Konfigurationsdatei angegeben) ist das Bild flussiger oder eben nicht. Naturlich muss die Kamera das auch entsprechend unterstutzen. Falls die Kamera bspw. maximal 10 Frames pro Sekunde senden kann, bringt es naturlich nichts, falls mehr in der Konfiguration eingestellt wurden.

## Außerhalb des Heimnetzwerks verfugbar machen

Da es kaum Sinn macht die Kamera im eigenen Netzwerk zu beobachten, wollen wir auch von außerhalb darauf zugreifen. Dafur brauchen wir eine feste IP oder aber einen [DNS Service](https://de.wikipedia.org/wiki/Domain_Name_System). Die meisten Telekommunikationsanbieter stellen feste IP Adressen jedoch (wenn uberhaupt) nur gegen Bezahlung zur Verfugung, weshalb wir einen kostenlosen DNS Anbieter nutzen wollen. Naturlich kannst du auch einen anderen Anbieter deiner Wahl nehmen. Falls du bereits eine feste IP Adresse zuhause besitzt, so kannst du diesen Schritt uberspringen.

**Hinweis**: Theoretisch kannst du auch eine nicht-statische IP Adresse verwenden, allerdings hat dies den Nachteil, dass du bei einem Reconnect eine neue IP Adresse bekommst und diese ggf. nicht mehr kennst. Da Provider ca. einmal am Tag (meist Nachts) einen Zwang-Reconnect durchfuhren, ist ein DNS Service sehr zu empfehlen, da sich die DNS Adresse eben nicht andert.

Fur all jene, die keine statische IP haben, habe ich hier gezeigt, wie man den [DNS Service von NoIP installiert und konfiguriert](http://tutorials-raspberrypi.de/webserver-installation-teil-6-dns-server-via-no-ip/).

Außerdem mussen wir noch den gewahlten Port (z.B. 8081) in unserem Router zur Weiterleitung freigeben. Das bedeutet, dass wir von außerhalb des Netzwerks diesen Port ansprechen und uns darauf verbinden konnen. Da dies bei jedem Router etwas unterschiedlich ist, verweise ich auf das entsprechende Handbuch. Unter dem Punkt „Port Forwarding" o.a. kannst du den Port angeben, welcher fur eine bestimmte lokale IP Adresse geoffnet wird. In meinem Router sieht das bspw. folgendermaßen aus:

![Raspberry Pi NoIP PortForwarding](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-NoIP-PortForwarding.png)

Das Menu des Routers ist meistens uber 192.168.1.1 bzw. 192.168.0.1 uber den Browser erreichbar. Sollte das nicht der Fall sein, wird in dem Handbuch aber auch stehen, wie du das Menu finden kannst.

Nutzt du den VLC Player musst du nun naturlich die lokale IP Adresse, die du vorher angegeben hast, mit deiner DNS- bzw. statischen IP Adresse ersetzen (Port ist weiterhin der selbe). Bei manchen Routern kann es sein, dass dies innerhalb des Netzwerks nicht klappt. Um es dennoch zuhause zu testen, kannst du am Handy z.B. kurzzeitig Mobile Daten anschalten (WLAN aus) und schauen, ob du den Livestream der Raspberry Pi Überwachungskamera sehen kannst. Je nach Internetverbindung (Upload Geschwindigkeit) wird das Bild ggf. etwas verzogert sein.
