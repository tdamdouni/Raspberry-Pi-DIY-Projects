# Raspberry Pi: WS2801 RGB LED Streifen anschließen und steuern

_Captured: 2017-09-03 at 13:12 from [tutorials-raspberrypi.de](https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/)_

![Raspberry Pi WS2801B RGB LED Streifen anschließen und steuern](https://tutorials-raspberrypi.de/wp-content/uploads/2016/11/Raspberry-Pi-WS2801B-RGB-LED-Streifen-anschließen-und-steuern.jpg)

Eines der vielen Raspberry Pi Projekte stellt die Beleuchtung von Raumen oder Objekten dar. Besonders dafur geeignet sind LED Streifen, wo viele einzelne LEDs aneinander gereiht sind und jede einzelne Diode alle RGB Farben darstellen kann. Damit konnen einige Projekte wie Raumbeleuchtung, Ambilight oder z.B. eine Weihnachtsbaumbeleuchtung realisiert werden. Die Effekte der farbenfrohen Lichter sind beeindruckend.

In diesem Artikel wird die generelle Benutzung vom WS2801B am Raspberry Pi gezeigt. Dabei erstellen wir ein Beispiel, in dem LEDs des Streifens gesetzt werden (Regenbogenfarben) und die Helligkeit gedimmt wird. Im Video am Ende des Tutorials siehst du das ganze noch einmal in Aktion.

## Zubehor

Die RGB LED Streifen gibt es in verschiedenen Langen und mit unterschiedlicher Anzahl an LEDs pro Meter (32, 60 und 144). Alle diese Streifen benotigen eine Eingangsspannung von 5V. Die gunstigste Variante mit 32 LEDs/m ist meiner Meinung nach fur die allermeisten Anwendungen vollkommen ausreichend, da der Abstand zwischen den LEDs nur 2.5 cm betragt:

Dabei gibt es auch Versionen, welche Staub- und Wasserfest (IP67) sind. Jede der einzelnen LEDs hat einen Stromverbrauch von ca. 60 mA. Bei einem Meter sind das knapp 2A. Dies ist einiges mehr, als die GPIOs des Raspberry Pi's liefern konnen. Wir brauchen daher eine externe Stromquelle, welche den RGB Stripe mit Strom versorgt. Je nachdem, wie lang dein Streifen ist, muss die maximale Stromstarke hoher sein. Bei 5 Metern sollte das Netzteil also 10A bereitstellen konnen.  
Du hast dabei die Auswahl zwischen zwei Moglichkeiten:

![DC Steckeradapter](https://tutorials-raspberrypi.de/wp-content/uploads/2016/10/DC-Steckeradapter-CCTV.jpg)

> _Mit einem Steckeradapter und Netzteil konnen sehr einfach Plus- und Minuspol an die LED Streifen verbunden werden._

Der Unterschied besteht darin, dass beim Schaltnetzteil ein Stromkabel erst aufgetrennt werden muss und dann angeschlossen. Da mit Hochspannung gearbeitet wird, kann dies gefahrlich sein und ist fur Einsteiger nicht zu empfehlen. Fur ein Netzteil (ahnlich zu den Laptop Ladegeraten) benotigt man lediglich noch einen zusatzlichen Power Jack Adapter, damit man die beiden Spannungspole abzwacken kann.

Zu guter letzt werden noch [Jumper Kabel](http://www.ebay.de/sch/i.html?_from=R40&_sacat=0&_nkw=jumper+kabel&rt=nc&LH_PrefLoc=1) und ein [Breadboard](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=Breadboard) benotigt.

#### WS2801B vs. WS2812B

Im Internet findet man haufig auch die WS2812 LED Streifen, welche auch etwas gunstiger als die WS2801 Modelle sind. Allerdings eignen diese sich nicht all zu gut fur den Raspberry Pi, da damit u.a. die Onboard Audioausgabe des Raspberry Pi's nicht verwendet werden kann. Falls du einen WS2812B Streifen dennoch nutzen willst, kannst du dies nach [folgendem Tutorial](https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/).

WS2801B Streifen besitzen zwei Datenleitungen (Data und Clock), wodurch einzelne LEDs uber den integrierten SPI Bus des Raspberry Pi's angesprochen werden konnen. Anders sieht dies bei den WS2812B Modellen aus. Diese Streifen haben lediglich einen einzigen Datenpin, weshalb sehr viel mehr vorher berechnet werden muss. Aus diesem Grund sind die **WS2801B** RGB LED Streifen den WS2812 fur die Nutzung am Raspberry Pi vorzuziehen, trotz ihrer vermeintlich geringeren „Seriennummer".

## Schaltnetzteil fur WS2801 anschließen

Bevor wir starten, mussen wir erst einmal die Stromquelle anschließen (nur fur das Steckernetzteil). Falls du die erste Variante - ein Ladegerat-ahnliches Netzteil - gewahlt hast, kannst du zum nachsten Punkt springen. Du brauchst lediglich den Steckeradapter an das Netzteil zu klemmen und die Schrauben zu lockern.

![Netzkabel für Raspberry Pi WS2801](https://tutorials-raspberrypi.de/wp-content/uploads/Netzkabel-für-Raspberry-Pi-WS2801-180x142.jpg)

> _Achte darauf, dass das Netzkabel auch 10A vertragt._

Vorerst der **Hinweis**: Arbeiten mit 230V Spannung kann todlich sein! Wahrend du Änderungen vornimmst, mussen alle Verbindungen zur Steckdose getrennt sein! Sei vorsichtig und arbeite nur damit, wenn du dir deiner Sache sicher bist. Falls dies nicht der Fall ist, rate ich zum erster genannten [Netzteil](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=AC DC Adapter 5V 10A).

Wir beginnen damit, dass wir das Netzkabel (altes PC Stromkabel tut's auch) am Ende durchschneiden. Im Inneren befinden sich zwei bzw. drei Kabel. Diese mussen vorsichtig um ca. 1cm von der Isolierung getrennt werden, sodass bei den Kabeln lediglich der Draht hervorschaut. Das Schaltnetzteil hat auf der linken Seite drei Anschlusse. Zum einen „L" (Phase/Außenleiter) und „N" (Neutralleiter), welche mit AC (Wechselstrom) gekennzeichnet sind und ein [Erdungssymbol](https://de.wikipedia.org/wiki/Liste_der_Schaltzeichen_\(Elektrik/Elektronik\)#Elektrische_Schaltzeichen). Sollte dein Kabel lediglich zwei kleinere Kabel enthalten, kommen diese an die Anschlusse von AC. Sind drei vorhanden, musst du zusatzlich das Erdungskabel identifizieren und an Anschluss mit Erdungssymbol / „PE" anschließen.

Da die Farben der inneren Kabel bei alteren Stromkabeln abweichen, hier eine kurze Übersicht, welche Farbe woran kommt:

  * Das **schwarze** bzw. **braune** Kabel kommt an den Außenleiter **„L"**.
  * Das **blaue** Kabel kommt an den Neutralleiter **„N"**.
  * Das **grun-gelbe** Kabel kommt an den Schutzleiter **„PE"** bzw. **Erdungssymbol**.
![Aufgeschnittenes Netzkabel mit abgetrennter Isolation](https://tutorials-raspberrypi.de/wp-content/uploads/Aufgeschnittenes-Netzkabel-mit-abgetrennter-Isolation-600x275.jpg)

> _Aufgeschnittenes zweiadriges Netzkabel mit abgetrennter Isolation._

Zum verbinden mussen die Schrauben des Netzteils gelockert werden und die Kabel darunter angebracht werden. Achte darauf, dass sie gut verschraubt sind und die Kabel sich nicht losen konnen. Normalerweise haben diese Gerate noch eine kleine Schutzklappe, damit man nicht aus versehen daran fasst. Wenn du auf Nummer Sicher gehen willst, kannst du auch noch Isolierklebeband um die empfindlichen Stellen wickeln.

Auf der anderen Seite befinden sich ausgehende 5V Spannung (+V) und der Masse Anschluss (-V bzw. COM). Als Test kannst du mit einem [Multimeter](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=Multimeter) die Spannung nachmessen, wie hier zu sehen ist:

![Multimeter am Schaltnetzteil des WS2801 LED Strip](https://tutorials-raspberrypi.de/wp-content/uploads/Multimeter-am-Schaltnetzteil-des-WS2801-LED-Strip-339x500.jpg)

> _Die Ausgangsspannung des Schaltnetzteils sollte ca. 5V betragen._

## Verkabelung zwischen Raspberry Pi, WS2801 und Stromquelle

Normalerweise kommen die LED Streifen mit angeloteten Steckern, welche u.a. zum Verbinden von mehreren WS2801 Streifen gedacht sind. Daneben ist i.d.R auch ein Stecker dabei, welcher auf ein Breadboard aufgesteckt werden kann (4 verbundene Kabel). Weiterhin gehen oft auch zwei weitere Kabel fur die externe Stromverbindung vom LED Strip ab (rot und schwarz).

Da die Farbbelegung der Kabel nicht unbedingt den Standards entspricht, solltest du genau darauf achten, welches Kabel zu welcher Verbindung auf dem Streifen fuhrt. Eine falsche Verkabelung am Raspberry Pi konnte zu Überhitzen oder einem Kurzschluss fuhren.

![WS2801 RGB LED Streifen](https://tutorials-raspberrypi.de/wp-content/uploads/WS2801-RGB-LED-Streifen-500x500.jpg)

> _Die LEDs auf einem Meter sind nummeriert (1 - 32). Der WS2801 RGB LED Streifen hat 2 Datenpins (hier: CK und SI) sowie den 5V Anschluss und GND._

Wenn du dir im Klaren bist, welches Kabel zu welchem Anschluss fuhrt, konnen wir sie anschließen. Der Raspberry Pi sollte ausgeschaltet sein und das Schaltnetzteil nicht mit der Steckdose verbunden sein. Die Kabel werden folgendermaßen angeschlossen:

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

Fur den Anschluss an das Schaltnetzteil kannst du auch die beiden zusatzlichen Kabel (sofern vorhanden) verwenden. Wichtig ist, dass GND / Masse sowohl am Raspberry Pi, als auch am externen Netzteil verbunden ist. Schematisch sieht der Aufbau nun folgendermaßen aus:

![Raspberry Pi WS2801B RGB LED Stripe Schaltplatine](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2801B-RGB-LED-Stripe-Schaltplatine-600x296.png)

## Raspberry Pi WS2801 RGB LED Bibliothek installieren

Zum Ansteuern des LED Stripes nutzen wir eine Python Bibliothek von [Adafruit](https://github.com/adafruit/Adafruit_Python_WS2801/blob/master/Adafruit_WS2801/WS2801.py). Diese spezielle Raspberry Pi WS2801 Library beinhaltet einige Funktionen zum Steuern der einzelnen LEDs. Das gute daran ist, dass jede LED einzeln angesprochen werden kann und jede mogliche [RGB Farbe](https://de.wikipedia.org/wiki/RGB-Farbraum) moglich ist.

Die Bibliothek benotigt den SPI Bus, den wir erst aktivieren mussen (falls nicht bereits vorher geschehen). Dazu rufen wir folgendes auf:
    
    
    sudo raspi-config

Unter „Advanced Option" findet sich ein Punkt fur „SPI". Diesen aktivieren wir und beenden das Konfigurationsmenu.

Die Installation funktioniert nun ganz einfach uber den Python Paket Manager aus der normalen Konsole / Terminal. Sicherheitshalber aktualisieren wir vorher noch die Paketquellen und installieren PIP (dies ist auf den Raspbian Lite Versionen nicht standardmaßig enthalten):
    
    
    sudo apt-get update
    sudo apt-get install python-pip -y
    sudo pip install adafruit-ws2801

![Raspberry Pi WS2801B Weihnachtsbaumbeleuchtung](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2801B-Weihnachtsbaumbeleuchtung-120x180.jpg)

> _Weihnachtsbaum Beleuchtung mit dem WS2801._

Falls du eine Lite Version hast, bzw. SpiDev bei dir nicht standarmaßig installiert ist, folge dieser [Anleitung](http://tightdev.net/SpiDev_Doc.pdf), um es zu installieren und aktivieren. Auf aktuellen Raspbian Versionen sollte es allerdings bereits vorinstalliert sein.

Da das angegebene Beispiel der Entwickler anscheinend nicht auf allen (frischen) Raspbian Versionen funktioniert, habe ich jenes verandert und erweitert.

## Beispielcode zum Helligkeit dimmen der WS2801 LEDs

Das folgende Beispiel kann fur eigene Projekte verwendet und erweitert werden. Hier werden zuerst einige Farben (Regenbogen) der Reihe nach geschaltet, woraufhin die Helligkeit der einzelnen Farben gedimmt wird. Dazu muss gesagt werden, dass auch die Helligkeit einer Farbe mit dem RGB Wert definiert werden kann (siehe [RGB Color Picker](http://www.w3schools.com/colors/colors_picker.asp) dazu).

Erstellen wir nun also eine Datei:
    
    
    sudo nano ws2801_example.py

Folgender Inhalt sollte eingefugt werden:

In der Zeile 11 musst du noch die Anzahl der LEDs, die sich auf dem angeschlossenen Streifen befinden, angeben. Bei einem Meter Lange sollten dies 32 sein. Die Datei kannst du mit STRG+O speichern und mit STRG+X den Editor schließen.

Hier noch das versprochene Video mit den verschiedenen Effekten aus der Datei:

Mich wurde interessieren, welche Projekte ihr damit vorhabt (Adventsbeleuchtung, Weihnachtsbaumdeko, Zimmer aufpeppen, „Infinite Mirror Table", etc.)? Gibt es vielleicht sogar Wunsche zu bestimmten Tutorials, die sich auf die Raspberry Pi WS2801B Steuerung beziehen? Ich habe schon ein paar Ideen, aber wurde auch gerne eure Meinung horen
