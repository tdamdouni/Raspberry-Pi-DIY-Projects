# Raspberry Pi: GPIO-Schnittstelle erklärt

_Captured: 2015-11-14 at 13:50 from [jankarres.de](http://jankarres.de/2015/02/raspberry-pi-gpio-schnittstelle-erklaert/)_

Der Raspberry Pi ist allein schon wegen seines Preises und der darauf laufenden Software interessant. Die Besonderheit des Gerates liegt jedoch viel mehr in den 26 (Raspberry Pi Model B und alter) bzw. 40 (Raspberry Pi B+ und neuer) GPIO-Pins (General Purpose Input/Output Pins). Die Schnittstelle fur elektronische Kontakte kann zur Messung und Steuerung von Geraten verwendet werden. Damit bekommen sowohl Bastler als auch Profis ein Werkzeug fur individuelle Losungen mit dem Raspberry Pi, das ihnen die Entwicklung computergesteuerter Gerate so einfach wie selten zuvor macht.

**Bezeichnungen und verschiedene Versionen**  
Der Raspberry Pi hat sich in seinen verschiedenen Modellen bzgl. der Pin-Belegung im Laufe der Zeit verandert. Im folgenden Artikel werden wir nur auf die Belegungen des Raspberry Pi Model B Rev 2.0 und des Raspberry Pi B+ (ggf. auch neuere Modelle) eingehen. Andere Funktionen und Belegungen aus dem Raspberry Pi Model B Rev 1 (verkauft vor September 2012) werden in diesem Artikel nicht behandelt, da die wenigsten noch ein solches Modell besitzen sollten.

Fur die Pins gibt es verschiedene Nummerierungssysteme, die in der Praxis zur Verwechselung der Pins fuhren kann. Folglich muss man bei Tutorials darauf achten welche Bezeichnungen von dem Autor verwendet werden:

  * Physikalische Pins (Pins): Die einzelnen Steckplatze sind horizontal von oben nach unten (Leserichtung) nummeriert. Die 1 erkennt man daran, dass der Lotpunkt auf der Ruckseite des Raspberry Pis quadratisch ist (alle anderen rund).
  * BCM-Pins (WiringPi): Bezeichnungen, die in der offiziellen Dokumentation der SoCs von Broadcom verwendet werden.
  * Pin-Namen: Von den Raspberry Pi Entwicklern verwendete Bezeichnungen fur die Pins, die deren bestimmte Funktion beschreiben. Pins die keine spezielle Funktion haben tragen hierbei die Bezeichnung _GPIO_ mit einer darauffolgenden Nummer.

Zu erwahnen ist an dieser Stelle, dass die Bezeichnung GPIO-Pins im Grunde genommen nicht ganz korrekt ist, da dies aussagt, dass es sich nur um General Purpose Input/Output Pins handelt, was nicht bei jedem Pin zutrifft. Low-level Peripherals Pins ware meiner Ansicht nach eine bessere Bezeichnung, wobei man in der Regel Artikel unter dem Stichwort _GPIO_ findet.

**Arten und Nutzen der Pins**  
Die verbauten Pins haben verschiedene Funktionen. Neben den allgemein verwendbaren Kontakten (GPIO-Pins genannt) gibt es auch solche fur die Versorgungsspannung (3,3V bzw. 5V) wie auch Masse Pins (auch Ground genannt; 0V). Mit den, auf dem B+ und neueren Modell vorhandenen, 14 Zusatz-Pins wurden weitere bislang nicht verfugbare Funktionen des System-on-a-Chip (B+: BCM2835; 2 Model B: BCM2836) zuganglich.

Damit sind wir dabei, dass es Pins gibt, die vorkonfigurierte Funktionen erfullen. Alle Pins sind jedoch frei programmierbar, auch solche, die eigentlich spezielle Eigenschaften haben. Welche Funktionen welcher Pin konkret erfullt wurde bereits ausfuhrlich im [eLinux Wiki](http://elinux.org/RPi_BCM2835_GPIOs) und ubersichtlich auf [WiringPi.com](http://wiringpi.com/pins/special-pin-functions/) zusammengefasst. Folglich muss man sich vor jedem Projekt, wenn man entsprechend gebundene Funktionen nutzen mochte, fragen auf welchen Pin man welches Gerat anschließt.

WiringPiPin-NamenPinPinPin-NamenWiringPi

-
\+ 3,3 V
**1**
**2**
\+ 5 V
-

8
(SDA1) GPIO 2
**3**
**4**
\+ 5 V
-

9
(SCL1) GPIO 3
**5**
**6**
GND
-

7
(GPIO_GCLK) GPIO 4
**7**
**8**
GPIO 14 (TXD0)
15

-
GND
**9**
**10**
GPIO 15 (RXD0)
16

0
(GPIO_GEN0) GPIO 17
**11**
**12**
GPIO 18 (GPIO_GEN1)
1

2
(GPIO_GEN2) GPIO 27
**13**
**14**
GND
-

3
(GPIO_GEN3) GPIO 22
**15**
**16**
GPIO 23 (GPIO_GEN4)
4

-
\+ 3,3 V
**17**
**18**
GPIO 24 (GPIO_GEN5)
5

12
(SPI_MOSI) GPIO 10
**19**
**20**
GND
-

13
(SPI_MISO) GPIO 9
**21**
**22**
GPIO 25 (GPIO_GEN6)
6

14
(SPI_SLCK) GPIO 11
**23**
**24**
GPIO 8 (SPI_CE0_N)
10

-
GND
**25**
**26**
GPIO 7 (SPI_CE1_N)
11

30
(nur fur I2C) ID_SD
**27**
**28**
ID_SC (nur fur I2C)
31

21
GPIO 5
**29**
**30**
GND

22
GPIO 6
**31**
**32**
GPIO 12
26

23
GPIO 13
**33**
**34**
GND

24
GPIO 19
**35**
**36**
GPIO 16
27

25
GPIO 26
**37**
**38**
GPIO 20
28

GND
**39**
**40**
GPIO 21
29

**Maximale Spannung und Stromstarke**  
Die beiden 3,3V Pins 1 und 17 durfen in der Summe eine Stromstarke von nicht mehr als 50 mA abgeben. Die belegbaren GPIO-Pins zur Steuerung von angeschlossenen Geraten haben ebenfalls eine Spannung von 3,3V. Zusammen mit den 3,3V Pins 1 und 17 sollten diese ebenfalls nicht mehr als 50 mA abgeben. Die 5V Pins 2 und 4 werden uber eine selbstruckstellende Sicherung (Poly Fuse) geleitet. Fließt bei diesen Pins zu viel Strom, so schaltet sich der Raspberry Pi selbst ab.

Die genannten Werte sind keine vom Hersteller maximal erlaubten Werte, sondern Ergebnisse von Raspberry Pi Anwendern bei deren Experimenten.

**Hardware zum komfortablen Basteln**  
Die GPIO-Pins auf dem Raspberry Pi sind nicht beschriftet, sodass man auf ein Abzahlen angewiesen ware um den richtigen Pin zu treffen. Außerdem hat man auf dem kleinen Raum beim direkten Basteln auf dem Raspberry Pi schnell ein Kabelgewirr, sodass weitere kleine Hardware empfehlenswert ist.

Zum Basteln ist ein Breadboard (auch Steckbrett genannt) sehr praktisch, da es ausreichend Platz fur einen ubersichtlichen Aufbau bietet. Außerdem konnen Signale in mehreren Reihen verwendet werden, sodass mit einem Signal bspw. mehrere LEDs angesprochen werden konnen.

Außerdem werden Kabel zum Verbinden der Komponenten (Sensoren, LEDs usw.), sogenannte Jumperwires, benotigt. Diese gibt es in den Ausfuhrungen Male-Male, Female-Female und Male-Female (Endungen der Stecker). Zu empfehlen ist es Male-Male Kabel zum Weiterleiten von Pins zu besitzen. Außerdem benotigt man Male-Female Jumperwires um die meisten Komponenten mit den Stecklochern auf dem Breadboard zu verbinden.

Um ein Breadboard mit dem Raspberry Pi zu verbinden benotigen wir ein Flachbandkabel. Sinnvoll ist es ein T-Cobbler dazwischen zu schalten, da dieser mit den Pin-Namen beschriftet ist und ein umstandliches Nachschlagen uberflussig werden lasst.

Im Folgenden eine Auflistung der Komponenten, die ich beim Basteln verwendet habe:
