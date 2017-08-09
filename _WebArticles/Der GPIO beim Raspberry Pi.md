# Der GPIO beim Raspberry Pi

_Captured: 2015-11-14 at 13:53 from [www.netzmafia.de](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_GPIO.html)_

Zusatzlich zu USB, Ethernet, Audio, Video und HDMI bietet hat der Raspberry Pi verschiedene digitale Ein-/Ausgabeleitungen, die GPIOs (General Purpose Input/Output). Sie sind uber die Stiftleiste P1 zuganglich. _Beachten Sie, dass alle Signale der GPIO-Pins mit einem Logikpegel von 3,3 V arbeiten und nicht 5-V-tolerant sind._ Einige Pins konnen auch als SPI-, I2C- oder UART-Schnittstelle verwendet werden.

![](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi1.jpg)

Das folgende Bild zeigt prinzipiell die Innenschaltung eines GPIO-Pins. Man erkennt deutlich die vielen Moglichkeiten, einen Pin ganz nach Wunsch zu konfigurieren, wobei nicht alle Moglichkeiten auf Betriebssystemebene zuganglich sind. Bei Konfiguration eines Pins als Ausgang, wird der Ausgangstreiber freigegeben. Der Ausgangsstrom kann in Schritten von 2 mA von 2 mA bis 16 mA eingestellt werden. Per Default liefern jeder Pin nur einen Strom von 8 mA bei maximal 3,3 V.

Ist der Pin als Eingang konfiguriert, wird eine Spannung von weniger als 0,8 V sicher als "0", eine Spannung von mehr als 2,0 V sicher als "1" erkannt. Die Konfiguration erlaubt auch den Betrieb des Eingangs mit Schmitt-Trigger-Charakteristik. Außerdem kann ein Widerstand am Eingang wahlweise als Pullup- oder Pulldown-Widerstand geschaltet werden (der Wert vom 50k ist ein Schatzwert). Wer sicher gehen will, verlaßt sich besser auf einen externen Pullup- oder Pulldown-Widerstand.

![](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi8.jpg)

Die folgenden Tabelle zeigt das Pinout des Raspberry Pi Revision 1.0 (Modelle A und B):

3,3V
1
2
5V

GPIO 0 (SDA)
3
4

GPIO 1 (SCL)
5
6
GND

GPIO 4 (GPCLK0)
7
8
GPIO 14 (TxD)

9
10
GPIO 15 (RxD)

GPIO 17
11
12
GPIO 18 (PCM_CLK)

GPIO 21 (PCM_DOUT)
13
14

GPIO 22
15
16
GPIO 23

17
18
GPIO 24

GPIO 10 (MOSI)
19
20

GPIO 9 (MISO)
21
22
GPIO 25

GPIO 11 (SCLK)
23
24
GPIO 8 (CE0)

25
26
GPIO 7 (CE1)

Die zweite Tabelle zeigt das geanderte Pinout des Raspberry Pi Revision 2.0, der an den neu hinzugekommenen Bohrlochern erkannt werden kann (Änderungen fett). Das ist auch das Modell, das hier verwendet wird:

3,3V
1
2
5V

**GPIO 2 (SDA1)**
3
4

**GPIO 3 (SCL1)**
5
6
GND

GPIO 4 (GPCLK0)
7
8
GPIO 14 (TxD)

9
10
GPIO 15 (RxD)

GPIO 17
11
12
GPIO 18 (PCM_CLK)

**GPIO 27**
13
14

GPIO 22
15
16
GPIO 23

17
18
GPIO 24

GPIO 10 (MOSI)
19
20

GPIO 9 (MISO)
21
22
GPIO 25

GPIO 11 (SCLK)
23
24
GPIO 8 (CE0)

25
26
GPIO 7 (CE1)

Beim Raspberry Pi Revision 2.0, gibt es einen weiteren GPIO-Anschluss, P5, der aber nicht bestuckt ist. Er ist vorgesehen fur eine Stiftleiste, die auf der **Unterseite** des Boards eingesetzt wird. Das Verloten der Pins erfolgt dann von der Oberseite der Platine. Daher ist die Nummerierung der Pins ebenfalls von der **Unterseite** her zu sehen (Pin 1 hat ein rechteckiges Lotpad):

5V
1
2
3,3V

GPIO28 (SDA0)
3
4
GPIO29 (SCL0)

GPIO30
5
6
GPIO31

GND
7
8
GND

Die GPIO-Pins 28/29 werden auch fur die Kamera-Schnittstelle (CSI) verwendet.

Das ist auch das Modell, das hier verwendet wird: 

Beim Modell B+" sind weitere GPIO-Pins hinzugekommen, die Belegung der Pins 1 - 26 ist gleich geblieben:

3,3V
1
2
5V

**GPIO 2 (SDA1)**
3
4

**GPIO 3 (SCL1)**
5
6
GND

GPIO 4 (GPCLK0)
7
8
GPIO 14 (TxD)

9
10
GPIO 15 (RxD)

GPIO 17
11
12
GPIO 18 (PCM_CLK)

**GPIO 27**
13
14

GPIO 22
15
16
GPIO 23

17
18
GPIO 24

GPIO 10 (MOSI)
19
20

GPIO 9 (MISO)
21
22
GPIO 25

GPIO 11 (SCLK)
23
24
GPIO 8 (CE0)

25
26
GPIO 7 (CE1)

(GPIO 0) ID_SD
27
28
(GPIO 1) ID_SC

GPIO 5
29
30

GPIO 6
31
32
GPIO 12

GPIO 13
33
34

GPIO 19
35
36
GPIO 16

GPIO 26
37
38
GPIO 20

39
40
GPIO 21

Wie Sie von der Bash aus auf die GPIO-Ports zugreifen konnen, wird ausfuhrlich im Kapitel [GPIO-Programmierung in der Shell](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_GPIO_Shell.html) behandelt. Aber die weiter unten folgenden kleinen Beispiele lassen sich auch ohne die dort besprochenen Feinheiten verstehen.

**Achtung: ** Die meisten Pins der Steckerleiste sind direkt mit der Broadcom-CPU verbunden. Sie sollten daher beim Anschluss von Peripheriekomponenten sorgfaltig zu Werke gehen, denn es besteht immer das Risiko, dass Sie den Raspberry Pi irreparabel beschadigen. Vermeiden Sie Kurzschlusse, Verdrahtungsfehler und zu hohe Eingangsspannungen. Oft reicht schon ein Multimeter, zum Überprufen der Verdrahtung, bevor Sie den Pi einschalten.

### Das Test- und Demo-Board

Damit mal schon einmal mit den Ports spielen kann, hat Matthias Stonebrink ein kleines Aufsteckboard fur den Raspberry Pi entworfen, das vier LEDs und zwei Taster enthalt. Die Schaltung ist recht einfach. Fur jede LED ist ein Schalttransistor vorhanden, um den Port nicht ubermaßig zu belasen. Die Taster liefern eine logische "1", wenn sie gedruckt sind; bei offenem Taster sorgen Pull-Down-Widerstande fur einen eindeutigen Pegel.

![](http://www.netzmafia.de/skripten/hardware/RasPi/Raspberry-Board-Schaltung.gif)

Fur Selbermacher gibt es auch die Eagle-Dateien zum Herunterladen: [Schaltplan](http://www.netzmafia.de/skripten/hardware/RasPi/Raspberry-Board.sch) und [Platinenlayout](http://www.netzmafia.de/skripten/hardware/RasPi/Raspberry-Board.brd). Das Board wird einfach auf den Raspberry Pi aufgesteckt und ist sofort betriebsbereit. Die Stromversorgung erfolgt uber den Portsteckern. In der einen Ecke des Boards befindet sich eine Bohrung. Dor kann entweder eine Distanzschraube mit 10 mm Hohe eingebaut werden, die auf dem Board des Raspberry Pi lose aufliegt oder man verschraubt das Board mit dem Pi unter Zwischenlage einer Distanzhulse von 10 mm Hohe (im Bild rot umrandet). Schraube bzw. Hulse nehmen den Druck auf, der beim Betatigen der Taste entsteht. Sonst wurde der Portstecker immer leicht gebogen.

### Erste Schritte bei der Shell-Programmierung

Damit sind Sie fit fur ein erstes Shell-Script, das zum einen die beiden Taster abfragt und deren Wert in der Shell ausgibt und dann mit allen vier LEDs blinkt. Fur das Blinken gibt es eine Shell-Funktion, die den Wert toggelt und eine Kontrollausgabe erzeugt.
    
    
    #!/bin/sh
    
    toggle()
      {
      # Zustand des Pins einlesen
      LedVal=$(cat /sys/class/gpio/gpio$1/value)
      # LED toggeln
      if [ $LedVal -eq "0" ]; then
        LedVal="1"
      else
        LedVal="0"
      fi
      # Kontrollausgabe auf der Konsole
      echo "Port $1 := $LedVal"
      # Pin auf 0 oder 1 setzen
      echo $LedVal > /sys/class/gpio/gpio$1/value
      }
    
    while :
    do
      # Taster einlesen und anzeigen
      for Port in  17 27
      do
        LED=$(cat /sys/class/gpio/gpio${Port}/value)
        echo "Port $Port = $LED"
      done
    
      # mit den LEDs blinken
      for Port in 22 23 24 25
      do
        toggle $Port
      done
      echo ""
      sleep 1
    done
    

Durch Schreiben der GPIO-Nummer in die virtuelle Datei /sys/class/gpio/unexport kann der GPIO wieder deaktiviert werden. Auch diese Aktion darf nur 'root' ausfuhren. Das folgende Script deaktiviert die Ports vollstandig:
    
    
    #!/bin/sh
    for Port in 22 23 24 25
      do
      echo "0" > /sys/class/gpio/gpio${Port}/value
      echo "$Port" > /sys/class/gpio/unexport
    done
    

### Weiterfuhrende Links

  * [GPIO-Programmierung in der Shell](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_GPIO_Shell.html)

_Copyright (C) Hochschule Munchen, FK 04, Prof. Jurgen Plate_
