# WS2812 RGB LED Streifen per Raspberry Pi steuern

_Captured: 2017-09-03 at 13:09 from [tutorials-raspberrypi.de](https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/)_

![Raspberry Pi WS2812 RGB LED Streifen](https://tutorials-raspberrypi.de/wp-content/uploads/2017/03/Raspberry-Pi-WS2812-RGB-LED-Streifen-WS2811.jpg)

Wer nach RGB LED Streifen sucht wird wohl oder ubel auf den WS2812 oder den WS2801 stoßen. Diese beiden LED Strips sind sehr unterschiedlich, aber beide mit dem Raspberry Pi ansteuerbar. Nachdem wir in einem vorherigen Tutorial letzteren[bereits verwendet](https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/) haben und auch in unserem [Ambilight](https://tutorials-raspberrypi.de/raspberry-pi-ambilight-fuer-alle-geraete-selber-bauen/) genutzt haben, geht es in diesem Tutorial um die Ansteuerung des Raspberry Pi WS2812 RGB LED Strips.

Die Modelle WS2812B sowie WS2811 sind ebenfalls kompatibel und konnen mit dieser Anleitung angesprochen werden.

Dazu muss gesagt werden, dass man sich von der „geringeren" Modellnummer des [WS2801](https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/) nicht tauschen sollte. Dieser hat - abgesehen vom Preis - ein paar Vorteile, auf welche unten genauer eingegangen wird.

## Zubehor

![DC Steckeradapter](https://tutorials-raspberrypi.de/wp-content/uploads/DC-Steckeradapter-CCTV-180x165.jpg)

> _Ein Steckeradapter macht das Verbinden der Spannungskabel zum Netzteil sehr einfach._

Wer schon einen RGB LED Streifen (z.B. als Ambilight) verwendet hat, kann das Zubehor daraus weiter verwenden. Dazu zahlt neben einem [Raspberry Pi](http://www.amazon.de/gp/product/B01CEFWQFA?ie=UTF8&linkCode=as2&camp=1634&creative=6738&tag=754-21&creativeASIN=B01CEFWQFA) folgendes:

Die maximale Starke des Netzteils ist abhangig von der Anzahl der LEDs. Laut Datenblatt braucht eine LED unter Volllast (= maximale Helligkeit) ca. 60mA. Bei 5m und 30 LEDs/m sind dies 9 Ampere. Ein Netzteil, welches bis zu 10A ist also geeignet. Solltest du mehr LEDs im Einsatz haben, kann es sein, dass du mehr als ein Netzteil benotigst (dazu spater mehr).

Daruber hinaus wird naturlich noch der eigentliche RGB LED Streifen vom Typ WS2812(B) bzw. WS2811 (auch NeoPixel genannt) benotigt. Diese gibt es in drei unterschiedlichen Varianten, welche sich in der Anzahl der LEDs pro Meter unterscheiden:

Die Lange sollte dabei abhangig vom umzusetzenden Projekt gewahlt werden. Meist sind aber 5m Rollen heruntergerechnet etwas gunstiger. Meine **Empfehlung** ist die mittlere Version mit **60 LEDs/m**. Diese haben eine hohere Dichte an Lichtern und somit hohere eine hohere Helligkeit. Vom Preis her sind diese jedoch noch unter einem vergleichbar langem WS2801 Band mit lediglich 32 LEDs

## NeoPixel WS2812B / WS2811 vs. WS2801 am Raspberry Pi

![Raspberry Pi WS2812 RGB LED Detailansicht](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2812-RGB-LED-Detailansicht-180x120.jpg)

> _Mit nur einer Datenleitung muss die Frequenz hoher sein, um die selbe Menge an Daten zu ubertragen._

In einem [vorherigen Tutorial](https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/) haben wir bereits gesehen, wie man einen WS2801 RGB LED Streifen ansteuert. Dieser unterscheidet sich vom WS2812B bzw. WS2811 und hat einige Vorteile, die ich hier zunachst auflisten mochte:

  * Durch **zwei Datenleitungen** sind weniger Berechnungen notig.
  * Dadurch kann ebenfalls eine **hohere Frequenz** erreicht werden.
  * Die **Helligkeit** des WS2801 ist hoher.
  * Es ist gleichzeitig moglich den WS2801 zu steuern und Musik abzuspielen, was mit dem WS2812 nicht moglich ist (mehr dazu weiter unten)

Nun stellt sich die Frage, warum man dennoch am Raspberry Pi einen WS2812 RGB LED Streifen nutzen sollte, wenn der WS2801 doch einige Vorteile bringt? Die Antwort ist recht einfach: Der **gunstigere Preis**. Im Vergleich ist ein Meter des WS2801 recht teuer, weshalb man damit eher sparsam umgehen mochte. Bei den im verhaltnismaßig gunstigen Preisen fur mehrere Meter WS2812 Kabel, kann auch ein großes Projekt ohne riesiges Budget realisiert werden.

Allerdings muss dazu gesagt werden, dass es leider nicht moglich ist, gleichzeitig Tone per Raspberry Pi Onboard Soundkarte wiederzugeben und den Streifen zu steuern. Dies liegt daran, dass der Raspberry Pi kein Echtzeitsystem wie der Arduino ist. Fur die Tonwiedergabe wird PWM genutzt, welches ebenfalls zum Steuern des WS2812 am Raspberry Pi benotigt wird. Beides gleichzeitig ist nicht moglich, weshalb jemand der auf die Soundwiedergabe angewiesen ist, eben lieber den [WS2801](https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/) nehmen sollte.

## Anschluss der NeoPixel WS2812 am Raspberry Pi

Bevor wir den Raspberry Pi mit dem WS2812 LED Strip verbinden, machen wir das Netzteil fertig. Wenn dein Streifen weniger als 20-30 LEDs hat, ist eine externe Stromversorgung nicht zwingend notig. Sollte er mehr LEDs haben, reicht der Strom des Pi's allerdings nicht mehr und ein Netzteil ist erforderlich.

Beim Netzteil selbst kommt es auf die gewahlte Art an. Bei einem Netzteil mit Adapter (Einsteiger) muss lediglich der DC Adapter angeschlossen werden, woran im nachsten Schritt die Spannungskabel des WS2812B kommen. Hast du diese Methode gewahlt, kannst du zum nachsten Punkt springen. Ein Schaltnetzteil (fur Erfahrene) muss allerdings etwas aufwandiger versorgt werden.

Vorher allerdings noch der Hinweis: **Beim Arbeiten mit 230V ist Vorsicht geboten, da Lebensgefahr besteht! Lass dir von einem Elektriker helfen oder greife auf die sichere Version des normalen Netzteil zuruck! Fuhre alle Arbeiten bei getrennter Netzverbindung durch.  
**

Zunachst brauchen wir ein gewohnliches Stromkabel, welches 10A vertragt. Meist ist auf der Unterseite des Steckers ein entsprechender Hinweis (230V, 10A). Dieses trennen wir vorsichtig mit einem Teppichmesser o.a. auf. Darin sind zwei bzw. drei Kabel mit unterschiedlichen Farben enthalten. Auch diese Kabel mussen vorsichtig abisoliert werden.

![Aufgeschnittenes Netzkabel mit abgetrennter Isolation](https://tutorials-raspberrypi.de/wp-content/uploads/Aufgeschnittenes-Netzkabel-mit-abgetrennter-Isolation-600x275.jpg)

> _Netzkabel mit abgetrennter Isolation und zwei inneren Kabeln (schwarz => L, blau => N)._

Mein Kabel hat nur zwei innere Kabel, was aber ausreicht. Zum Anschluss an das Schaltnetzteil, dienen die Farben der inneren Kabel als Orientierung. Das Schaltnetzteil hat die Anschlusse „L", „N" und „PE" bzw. ein Erdungssymbol.

  * Das **schwarze** bzw. **braune** innere Kabel kommt an den Außenleiter **„L"**.
  * Das **blaue** innere Kabel kommt an den Neutralleiter **„N"**.
  * Das **grun-gelbe** innere Kabel kommt an den Schutzleiter **„PE"** bzw. **Erdungssymbol**.
![Multimeter am Schaltnetzteil des WS2801 LED Strip](https://tutorials-raspberrypi.de/wp-content/uploads/Multimeter-am-Schaltnetzteil-des-WS2801-LED-Strip-122x180.jpg)

> _Die Spannung sollte ca. 5V betragen._

Nachdem die Feststellschrauben angezogen sind, kann das Netzkabel in die Steckdose gesteckt werden und die Spannung am Netzteil testweise mit einem Multimeter gemessen werden. Dies ist zwar keine Pflicht, aber kann als Absicherung gemacht werden. Dabei wird VCC an V+ angeschlossen und GND an COM. Sollte die Spannung nicht exakt 5V betragen, ist dies kein Problem.

Theoretisch ist es auch moglich den Raspberry Pi aus diesem Netzteil mit Strom versorgen. Dies haben (laut Kommentaren im WS2801 Tutorial) auch einige User gemacht. Aus Platzgrunden wird darauf hier aber nicht eingegangen.

### Verbindung zwischen Raspberry Pi und WS2812 NeoPixel Streifen

Ist das Netzteil soweit eingerichtet, schließen wir den Raspberry Pi an den WS2812 RGB LED Streifen an. Das (Schalt-)Netzteil muss vorher **vom Strom getrennt werden**.

Da nur eine Datenleitung vorhanden ist, brauchen wir auch nur einen Pin (GPIO 18). Wichtig ist, dass die Masseanschlusse des Raspberry Pi's und des Schaltnetzteil verbunden werden, allerdings **nicht** die 5V Spannungen! Insgesamt fuhren nur zwei Kabel vom Raspberry Pi zum WS2812 LED Strip: GPIO 18 (an DIN) und GND an COM des Netzteils sowie GND des Streifens.

![Raspberry Pi WS2812 Steckplatine](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2812-Steckplatine-600x361.png)

> _Schematische Verbindung zwischen Raspberry Pi, WS2812 und dem externen Netzteil_

Je nach Lange des LED Streifen sollte die externe Stromverbindung an mehreren Orten angebracht werden. Im Idealfall wird ca. jeden Meter VCC und GND mit dem Schaltnetzteil parallel verbunden (sodass viele Kabel zum Netzteileingang fuhren).

**Hinweis**: Bei Langen unter 1m kann das Netzteil auch weggelassen werden und die Eingangsspannung vom 5V Pin des Raspberry Pi's kommen.

## Vorbereitung & Installation

Bevor wir dir Raspberry Pi Bibliothek fur die WS2812 LEDs installieren, mussen einige Vorbereitungen getroffen werden:

  1. Die Paketquellen werden aktualisiert: 
    
        sudo apt-get update

  2. Wir installieren die benotigten Pakete (mit Y bestotigen): 
    
        sudo apt-get install gcc make build-essential python-dev git scons swig

  3. Die Audioausgabe muss deaktiviert werden. Dazu bearbeiten wir die Datei 
    
        sudo nano /etc/modprobe.d/snd-blacklist.conf

Hier fugen wir folgende Zeile hinzu:
    
        blacklist snd_bcm2835

Anschließend wird die Datei durch Drucken von STRG+O gespeichert und mit STRG+X wird der Editor geschlossen.

  4. Außerdem mussen wir die Konfigurationsdatei bearbeiten: 
    
        sudo nano /boot/config.txt

Unten befindet sich Zeilen mit folgendem Inhalt (mit STRG+W kannst du suchen):
    
        # Enable audio (loads snd_bcm2835)
    dtparam=audio=on

Diese untere Zeile wird mit einer Raute/Hashtag **#** am Zeilenanfang auskommentiert: `#dtparam=audio=on`

  5. Wir starten das System neu 
    
        sudo reboot

Nun konnen wir die Bibliothek laden.
    
    
    git clone https://github.com/jgarff/rpi_ws281x

In diesem Verzeichnis sind nun einerseits einige C Dateien enthalten, welche einfach kompiliert werden konnen. Der Beispielcode dafur ist gut verstandlich. Damit wir diese in Python verwenden konnen, mussen wir sie kompilieren:
    
    
    cd rpi_ws281x/
    sudo scons

Wir interessieren uns allerdings in diesem Tutorial vor allem fur die Python Variante und wechseln daher in den Python Ordner:
    
    
    cd python

Hier fuhren wir nun noch die Installation aus:
    
    
    sudo python setup.py build
    sudo python setup.py install

Damit konnen wir im nachsten Schritt bereits einen ersten Test ausfuhren.

## Testen des Raspberry Pi WS2812 RGB LED Streifen

Im Example-Ordner sind einige Beispieldateien, womit die LED Streifen getestet werden konnen. Daruber hinaus konnen sogar zwei WS2801 LED Streifen unabhangig voneinander per Raspberry Pi gesteuert werden (`multistrandtest.py`).

Wir interessieren uns aber zunachst fur die einfache Version. Dafur mussen wir vor dem Test noch ein paar Angaben vervollstandigen und bearbeiten daher die Beispieldatei.
    
    
    sudo nano examples/strandtest.py

Die Datei sieht folgendermaßen aus, wobei wir in erster Linie `LED_COUNT` (Anzahl der anzusprechenden LEDs) und `LED_PIN` (bei uns 18) angeben mussen.

Anschließend speichern wir (STRG+O) und kehren zuruck ins Terminal (STRG+X). Nun lasst sich die Datei ausfuhren (die Übergabe des Pfads zu den kompilierten Dateien ist wichtig):
    
    
    sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python examples/strandtest.py

Die LEDs des WS2812 Streifen sollten wie im unteren Video aufleuchten. Im oberen Code sind nur einige Effekte (Regenbogen, etc.) definiert, allerdings konnen auch problemlos analog dazu weitere Effekte erstellt werden (wer mochte kann gerne seinen Code fur Effekte als Kommentar posten).

### Weiteres

Die WS2812 NeoPixel LEDs werden auch in vielen anderen (hauptsachlich fur Arduino konstruierten) Projekten genutzt, weshalb man sicherlich einige davon auch portieren kann.

Daruber hinaus hat der Raspberry Pi Shop Pimoroni einen Aufsatz fur das Model B (ab Version B+) und den Raspberry Pi Zero hergestellt und nennt diesen [Unicorn pHAT](http://www.amazon.de/gp/product/B00OKIGY9O?ie=UTF8&linkCode=as2&camp=1634&creative=6738&tag=754-21&creativeASIN=B00OKIGY9O). Dieses RGB LED Matrix nutzt allerdings eine [eigene Software](https://github.com/pimoroni/unicorn-hat) zur Bedienung.

Die von mir genutzte Bibliothek wird ubrigens auch von einem anderen Entwickler als [Serveranwendung](https://github.com/tom-2015/rpi-ws2812-server) angeboten.
