# Raspberry Pi Ambilight für alle Geräte mit OSMC selber bauen

_Captured: 2017-09-03 at 13:17 from [tutorials-raspberrypi.de](https://tutorials-raspberrypi.de/raspberry-pi-ambilight-fuer-alle-geraete-selber-bauen/)_

![Raspberry Pi Ambilight selber bauen](https://tutorials-raspberrypi.de/wp-content/uploads/2017/02/Raspberry-Pi-Ambilight-selber-bauen.jpg)

Neuere TV's haben das sog. Ambilight, wobei sich die Beleuchtung den Bildfarben anpassen. Mit unserem eigenem Raspberry Pi Ambilight konnen wir diesen Effekt nachstellen. Und es kommt noch besser: Wir konnen dabei jegliches Gerat, welches einen HDMI Ausgang hat, anschließen und den Farbeffekt bewundern.

In diesem Tutorial schließen wir zunachst alle Komponenten sachgemaß an und konfigurieren dann das Betriebssystem OSMC so, dass das Raspberry Pi Ambilight nach unseren Wunschen funktioniert. Anschließend konnen DVD-Player, Heim-PC, die Konsole usw. das Selstbau Ambilight nutzen.

Besonders eindrucksvoll ist dieser Effekt bei Blockbustern, wenn der Raum abgedunkelt ist und auch beim Fußball hat es einen schonen Nebeneffekt.

## Raspberry Pi Ambilight Zubehor

Ein TV mit Ambilight und anderen Features kostet einiges mehr als vergleichbare Gerate. Der Raspberry Pi bietet dazu eine kostengunstige Alternative, welche noch einiges mehr kann. Um das Raspberry Pi Ambilight nachzubauen, sind folgende Teile notig:

  * [micro SD Karte](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=micro SD) (16 GB+)
  * [USB Netzteil](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=USB Netzteil)
  * optimal: [Gehause](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=Raspberry Pi Case)
  * [WS2801 LED Streifen](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=WS2801 32 LED) (3 bis 5 Meter, je nach TV Große), nicht wasserfest
  * [5V Schaltnetzteil](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=5V Schaltnetzteil 10A) (6A bzw. 10A)
  * [USB Video Grabber](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=Mumbi video grabber)
  * [Cinchstecker](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=Cinchstecker 3x) (male-male)
  * [HDMI Verdoppler](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=hdmi 1 stecker 2 buchsen) (1 Stecker in, 2 Buchsen out)
  * Lotutensilien

Wie lang der WS2801 LED Streifen sein sollte kannst du berechnen, indem du die vier Kanten deines Fernsehers addierst. Falls dein TV unten ein breiteres Standbein hat, kannst du diese Lange anziehen. Bei meinem 42″ Fernseher waren ungefahr 2,80 Meter LED Streifen notig. Bei einem 56 Zoll Fernseher waren ca. 3,80 bis 4 Meter notig. Die Streifen lassen sich einfach durchtrennen und wieder verloten.

## Vorbereitung - Aufbau des WS2801 LED Streifen

![WS2801 RGB LED Streifen](https://tutorials-raspberrypi.de/wp-content/uploads/WS2801-RGB-LED-Streifen-180x180.jpg)

> _Zwischen den Lotstellen kann der LED Streifen durchtrennt werden._

Bevor wir die Software auf den Raspberry Pi aufspielen, kleben wir zunachst den LED Streifen an den TV, worauf ich gleich naher eingehe. Vorher kannst du deinen [WS2801 LED Streifen noch testen](https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/). Sofern der kurze Test funktioniert hat bzw. du ihn uberspringen mochtest, beginnen wir mit dem Aufbau.

Zunachst mussen wir den selbstklebenden WS2801B Streifen am TV anbringen. Drehe dazu den Fernseher um und fange an einer Ecke an (z.B. links unten) und bringen den Streifen horizontal entgegen dem Uhrzeigersinn an. Sobald wir an der Kante angelangt sind, schneiden wir den LED Streifen an der markierten Stelle zwischen den Lotpunkten durch. An der angekommenen (rechten) Ecke setzen wir den Streifen wieder an und bringen ihn diesmal vertikal nach oben an. Gleiches machen wir fur die obere und linke Kante. Achte aber darauf, dass du den LED Streifen nicht aus versehen verkehrtherum nimmst, da das Signal nur in eine Richtung ubertragen werden kann (i.d.R. haben die LED Streifen einen Pfeil als Markierung oder IN/OUT Hinweise).

Der Rand deines Fernsehers sollte nun vom LEDs bedeckt sein:

Allerdings sind wir noch nicht fertig. Die durchgeschnittenen Enden mussen verlotet werden. An jeder Ecke mussen die 4 Lotstellen entsprechend miteinander verbunden werden (GND an GND, usw.). Aber Achtung: Das Ende des Streifens **darf nicht** an den Anfang verbunden werden!

Übrigens: In welche Richtung du den WS2801 LED Streifen anbringst und wo du beginnst, kannst du spater noch einstellen und ist daher nicht entscheidend. Es bietet sich z.B. an, statt in einer Ecke, unten in der Mitte anzufangen (wie im Video zu sehen), da dann spater der Raspberry Pi mittig am Fernseher platziert werden kann.

## Anschluss des Raspberry Pi's

Nun schließen wir den Raspberry Pi und das Schaltnetzteil noch an. Lies dir dazu die ausfuhrliche Anleitung mit [Hinweisen zum WS2801 LED Streifen](https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/) durch. Sobald das Netzteil angeschlossen ist (**vom Strom trennen!**), schließen wir die GPIOs des Raspberry Pi's an:

WS2801 LED Streifen Raspberry Pi (Schalt-) Netzteil

5V
--
+V

CK / CI
Pin 23 (SCKL)
--

SI / DI
Pin 19 (MOSI)
--

GND
Pin 6 (GND)
-V bzw. COM

Das Netzteil wird dabei an den 5V Anschluss desWS2801 Streifens angeschlossen, sowie an den GND Anschluss, welcher ebenfalls am Pi angeschlossen ist.

![Raspberry Pi WS2801B RGB LED Stripe Schaltplatine](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2801B-RGB-LED-Stripe-Schaltplatine-600x296.png)

Die Belegung der GPIOs [findest du hier](https://tutorials-raspberrypi.de/raspbery-pi-gpio-pin-belegung/).

Achtung: Beim Arbeiten mit Netzspannung ist immer Vorsicht geboten, da diese todlich sein kann! Fuhre alle Schritte mit Sorgfalt durch und lass dir ggf. von einem Elektriker helfen. Ich kann dafur keine Verantwortung ubernehmen!

Nun fehlt nur noch der Anschluss des Videograbbers. Schließe diesen zunachst per USB an einen freien Port des Raspberry Pi's an. Das andere Ende hat drei weibliche Cincheingange (rot, weiß, gelb). Mit dem Male-Male Cinchkabel verbindest du den USB Videograbber an den HDMI2AV Konverter. Der Konverter braucht noch eine zusatzliche Stromverbindung per USB. Du kannst dafur ein externes USB Netzteil nutzen oder einen weiteren USB Port des Pi's belegen.

Der HDMI Doppler wird an das eigentliche Gerat, wovon das Bild kommt, angeschlossen (Playstation, Konsole, TV oder Satelliten Receiver, usw.). Von den beiden ausgehenden HDMI Kabeln kommt eines an den Fernseher und das andere an den HDMI2AV Konverter.

![Raspberry Pi Ambilight Verbindung](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Ambilight-Verbindung-600x90.png)

## Vorbereitung - Raspberry Pi Ambilight Software

Die Basis der Raspberry Pi Ambilight Steuerung bildet das „[Hyperion](https://hyperion-project.org/)" Projekt. Dieses kann auf gangigen Raspbian Versionen und weiteren Linux Distributionen installiert werden. Der Einfachheit halber nutzen wir eine frische Version von [OSMC](https://osmc.tv/), wodruch wir den Raspberry Pi zusatzlich als Mediencenter nutzen konnen.

Dazu befolgen wir diese Schritte:

  1. Gehe auf die [OSMC Download Seite](https://osmc.tv/download/).
  2. Klicke ganz unten auf „Disk Images" und lade das neuste Release fur „Raspberry Pi 2 / 3". Entpacke es danach mit WinRar, 7Zip o.a.
  3. Übertrage das heruntergeladene und entpackte Image (Dateityp: .img) auf deine micro SD Karte ([hier zur Anleitung fur Windows Nutzer](https://tutorials-raspberrypi.de/raspbian-os-auf-eine-sdkarte-bertragen-windows/)).
  4. Nach Übertragung kannst du die Micro SD Karte in den Raspberry Pi stecken.
  5. Schließe HDMI des Fernsehers, Tastatur und Maus an den Raspberry Pi an und starte ihn (durch verbinden des micro USB Stromanschlusses).
  6. Nach kurzem Warten kannst du die Sprach-, Tastur- und Zeiteinstellungen festlegen.
  7. Lasse den Hostnamen auf „osmc" und aktiviere SSH („SSH Service is enabled"). Akzeptiere anschließend die Lizenzbedingungen.
  8. Wahle das OSMC Theme (nicht Classic).
  9. Den Newsletter musst du nicht auswahlen.
  10. Beende das Setup.
  11. Optimal: Wahle unter Programme -> My OSMC -> Network -> Wireless -> Enable Adapter dein WLAN aus und gib das Passwort ein. Sonst ist eine Verbindung per LAN Kabel mit deinem Netzwerk notig (zumindest temporar).
  12. Finde unter Einstellungen -> Systeminfo -> Netzwerk -> IP-Adresse die lokale IP-Adresse des Raspberry Pi's in deinem Netzwerk heraus (192.168.x.x).

## Hyperion installieren

Ab jetzt werden die externen Peripheriegerate nicht mehr gebraucht, da wir uns per SSH einloggen. In Windows geht dies am einfachsten per Putty ([hier erklart](https://tutorials-raspberrypi.de/raspberry-pi-ssh-windows-zugriff-putty/)). Der Hostname ist „osmc" (sofern du ihn nicht geandert hast) bzw. die IP Adresse, die du eben in Schritt 12 ausgelesen hast. Falls die Verbindung damit nicht funktioniert, obwohl sich der PC im selben Netzwerk befindet, musst du in deinem Router die interne IP Adresse (192.168.x.x) herausfinden.

Der Standard-**Username** ist **osmc**, ebenso wie das **Passwort** standardmaßig **osmc** ist.

Nach dem Login muss zunachst SPI aktiviert werden, wozu wir eine Datei bearbeiten mussen:
    
    
    sudo nano /boot/config.txt

Am Ende der Datei fugen wir folgende Zeile hinzu:

Damit die Änderungen ubernommen werden, muss der Raspberry Pi neu gestartet werden:
    
    
    sudo reboot

Dabei wird die SSH Verbindung unterbrochen. Du musst dich erneut verbinden.

Wir uberprufen nun noch, ob der SPI Datenbus wirklich aktiviert wurde. Dafur geben wir ein:
    
    
    ls /dev/spidev*

Es sollten nun die verfugbaren Pfade angezeigt werden. Falls nichts angezeigt wird, wurde SPI nicht aktiviert.

Die nachsten Schritte finden von unserem PC / Mac / Linuxcomputer statt. Wichtig ist, dass eine [aktuelle Java Version](https://java.com/de/download/) installiert ist (auf dem PC, nicht auf dem Raspberry Pi), denn ohne dies konnen wir Hyperion nicht ubertragen und konfigurieren.  
Ist dies bereits der Fall, konnen wir das Hyperion Projekt als ausfuhrbare Java-Datei (.jar) [von hier herunterladen](https://sourceforge.net/projects/hyperion-project/files/hypercon/HyperCon.jar/download). Öffne anschließend die HyperCon.jar Datei. Es offnet sich folgendes Fenster:

![Raspberry Pi Ambilight Hyperion Konfiguration](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Ambilight-Hyperion-Konfiguration-600x333.png)

### Hyperion Konfigurieren

Auf der linken Seite befinden sich die Einstellmoglichkeiten. Oben befinden sich die verschiedenen Tabs, welche wir nun Schritt fur Schritt durchgehen werden. Nach jeder Änderung solltest du deine aktuelle Konfiguration speichern. Dies geht, indem du unten auf „Speichern" druckst und einen Speicherort wahlst. Spater kannst du die Einstellungen auch wieder importieren.

  1. **Allgemein**
    * Typ: WS2801
    * Ausgabe: /dev/spidev0.0
    * Baudrate: 1.000.000
    * Die Einstellungen zu der Anzahl der LED's musst du individuell anpassen. Die Änderungen werden am großen Bildschirm angezeigt. Mit „LED Anfang" kannst du die Start-LED verschieben. Achte darauf, dass die Richtung gespiegelt ist, da hier die Vorderseite gezeigt wird. Wir haben den LED Streifen entgegen dem Uhrzeigersinn angebracht, also wird er hier im Uhrzeigersinn angezeigt.
  2. **Verarbeitung**
    * hier brauchen wir vorerst nichts andern. Dies kann ggf. spater individualisiert werden.
  3. **Grabber**
    * deaktiviere den Internen Grabber
    * aktiviere den externen Grabber [V4L2] 
      * Gerat: /dev/video0
      * Eingang: 0
      * Videoformat: PAL
      * 3D Modus: 2D
      * den Rest lassen wir vorlaufig unverandert.
  4. **Extern**
    * keine Veranderung
  5. **SSH**
    * System: Alle Systeme (nicht OE/LE)
    * Ziel IP: diese findest du im OSMC Bildschirm unter Einstellungen -> Systeminfo -> Netzwerk -> IP-Adresse oder alternativ in deinem Router (beginnend mit 192.168…).
    * Port: 22
    * Benutzername: osmc
    * Passwort: osmc
![Raspberry Pi Hyperion SSH Einstellungen](https://tutorials-raspberrypi.de/wp-content/uploads/2017/02/Raspberry-Pi-Hyperion-SSH-Einstellungen.png)

> _Nach dem erfolgreichen Verbinden per SSH, kann Hyperion installiert und gestartet werden._

Falls du ein anderes System als OSMC verwendest, kannst du [hier](https://hyperion-project.org/wiki/Installation-on-all-systems) die standardmaßig gesetzten Zugangsdaten der gangigen Systeme (XBMC, Raspbian, OpenELEC, etc.) einsehen.

Diese Einstellungen sind derweil nicht in Stein gemeißelt und konnen spater noch verfeinert werden.

Drucke nun im Tab SSH auf **Connect**. Sofern die Angaben richtig sind und der Raspberry Pi verbunden ist, sollte keine Fehlermeldung erscheinen und der Buttontext sich auf Disconnect andern. Wahle nun den Button „**Inst./Akt. Hyperion**„. Dieser Schritt wird etwas dauern und die **GUI lasst sich zwischenzeitlich nicht bedienen**. Schließe das Programm **nicht**!

### Konfigurationsdatei ubertragen

Nachdem die Installation fertig ist, konnen wir die Einstellungen senden. Speichere die Konfigurationsdatei dazu unten unter „Generiere Konfiguration fur Hyperion" an einem Ort deiner Wahl und drucke nun weiter oben unter „SSH - Sende Konfiguration" auf **Senden**. Wenn du nun in die Konsole bzw. in Putty zuruckkehrst, kannst du prufen, ob die Datei auch wirklich ubertragen wurde, da es manchmal der Fall ist, dass die Datei nicht erstellt wurde. Rufe dazu folgendes im Terminal auf:
    
    
    ls /etc/hyperion

Sofern dir hier die Datei „hyperion.config.json" angezeigt wird, ist alles in Ordnung und wir konnen fortfahren. Falls dies nicht der Fall ist, so mussen wir sie manuell anlegen. Fuhre dazu dies aus:
    
    
    sudo nano /etc/hyperion/hyperion.config.json

Hier fugst du den Inhalt der vorher gespeicherten Datei ein. Die Datei kannst du mit jedem Texteditor offnen und den Inhalt kopieren. Anschließend speicherst du mit STRG+O und beendest den Editor mit STRG+X.

Zum testen stoppen wir Hyperion nun noch im HyperCon Programm und starten es danach erneut. Die LEDs sollten anfangen zu leuchten. Durch das Auswahlen einer Farbe und „Sende Farbe" konnen wir bereits andere Farben anzeigen lassen. Teste mehrere Farben und versichere dich, dass diese stimmen. Falls dies soweit geklappt hat, konnen wir fortfahren und die eigentliche Funktionalitat testen und falls du die Farbeinstellungen noch im Nachhinein bearbeiten willst, kannst du dies unter der Menukarte „Verarbeitung".

## Video Grabber testen

Nachdem wir wissen, dass die LEDs soweit funktionieren, mussen wir noch das Zusammenspiel aus USB Video Grabber testen. Dazu schließen wir den HDMI Verdoppler einmal an ein aktives HDMI Gerat an. Einer der ausgehenden Anschlusse geht an den HDMI2AV Konverter und der andere in einen freien HDMI Anschluss des Fernsehers.

In Hyperion wahlen wir per Rechtsklick auf dem abgebildeten Bildschirm die Option „Hole Bild vom Grabber…"

![Hyperion Rechtsklick](https://tutorials-raspberrypi.de/wp-content/uploads/2017/02/Hyperion-Rechtsklick.png)

Es sollte nun automatisch der Frame des angeschlossenen HDMI Gerats angezeigt werden. In meinem Fall habe ich den PC angeschlossen und bekomme folgendes zu sehen:

![](https://tutorials-raspberrypi.de/wp-content/uploads/Hyperion-Aktueller-Frame-600x387.png)

Wie dir vielleicht aufgefallen ist, ist am rechten und linken Rand ein schwarzer Streifen zu sehen. Das wurde die Farben beeinflussen, weshalb ich in HyperCon unter dem Tab **Grabber** noch weitere Einstellungen vornehme (Entfernung Pixel links/rechts: +10) und meine Konfiguration erneut sende. Hole ich anschließend das Bild erneut, so ist der schwarze Rand verschwunden.

Nach diesem Test mussen wir Hyperion erneut stoppen und wieder starten. Anschließend wird sich das Raspberry Pi Ambilight dem Bild automatisch anpassen. Dabei spielt es keine Rolle, ob ein Blueray-Player, eine Konsole, der PC oder ein anderes HDMI-fahiges Gerat das Bild ausgibt.  
Übrigens kannst du auch den Raspberry Pi als Eingabe verwenden (z.B. wenn du OSMC als Mediencenter nutzt). Dazu brauchst du den Videograbber nicht und aktiviert im Tab Grabber den internen Grabber.

Solltest du ein nicht bekanntes Problem haben, hilft oft ein Blick ins sehr ausfuhrliche [Wiki von Hyperion](https://hyperion-project.org/wiki/Main). Alternativ kannst du deine Frage hier, im [Hyperion Forum](https://hyperion-project.org/) oder auch im [Github Forum](https://github.com/hyperion-project/hyperion/issues) stellen.
