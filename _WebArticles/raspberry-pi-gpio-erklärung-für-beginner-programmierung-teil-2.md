# Raspberry Pi GPIO Erklärung für Beginner + Programmierung (Teil 2)

_Captured: 2017-09-03 at 13:15 from [tutorials-raspberrypi.de](https://tutorials-raspberrypi.de/raspberry-pi-gpio-erklaerung-beginner-programmierung-lernen/)_

![Raspberry Pi GPIO steuern - Programmieren Lernen](https://tutorials-raspberrypi.de/wp-content/uploads/2017/03/Raspberry-Pi-Programmieren-Lernen-GPIOs-steuern.jpg)

Eine der Besonderheiten des Raspberry Pi's sind die programmierbaren Input-Output Pins. Diese sog. GPIOs konnen einfach uber ein Programm geschaltet werden, was wir in diesem Tutorial durchgehen. Dafur schreiben wir ein Python Programm, womit wir einerseits Eingaben erfassen und andererseits die Raspberry Pi GPIO Pins schalten, um so andere Module und Sensoren schalten zu konnen. Daruber hinaus erklare ich in diesem Tutorial die Funktionsweise eines Breadboards / Steckbrett.

Falls du den [ersten Teil](https://tutorials-raspberrypi.de/programmieren-lernen-raspberry-pi-einfuehrung) noch nicht gelesen und evtl. noch Probleme mit den Basics hast, wurde ich raten das zunachst durchzugehen. Fur alle, die bereits Programmiererfahrung haben, aber noch nicht mit den GPIOs gearbeitet haben, konnen auch direkt hiermit starten.

Übrigens: Fur die weiteren Teile ware es super, falls ihr Anregungen habt bzw. was euch vor allem interessiert. Ich werde versuchen, das mit einzubauen.

## Zubehor

In diesem Tutorial werden wir ein paar Hardware Bausteine brauchen. Diese sind unter anderem:

Diese Bauteile werden ubrigens immer wieder benotigt. Wenn du noch weitere [Hardware-Projekte](https://tutorials-raspberrypi.de/gpio/) nachbauen willst, wirst du dieses Zubehor definitiv weiter benotigen.

## Funktionsweise eines Breadboards / Steckbretts

Ein Breadboard (deutsch: Steckbrett) ist eine Hilfe um Schaltungen schnell aufbauen zu konnen, ohne diese jedes mal Loten zu mussen. Es bietet vor allem beim Testen und Konzipieren große Vorteile. Dabei gibt es Breadboard in verschiedenen Großen, wobei der Aufbau jedoch meist wie folgt ist:

![Raspberry Pi GPIO Breadboard Steckbrett](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-GPIO-Breadboard-Steckbrett-600x217.png)

In der schematischen Zeichnung sind unten die Verbindungen markiert. Die Linien zeigen dabei auf, welche der Locher miteinander verbunden sind. Unten und oben sind zwei horizonale Leisten zu sehen, an die man normalerweise den Plus- und Minuspol eines Gerats hangt.

Bei den mittleren Pins sind die Verbindungen vertikal. Dabei kann z.B. eine LED in zwei Spalten nebeneinander gesteckt werden. Doch dazu gleich mehr.

## Raspberry Pi GPIO Übersicht

Seit dem Model B+ haben die Raspberry Pi's eine 40 Kopfige Pinleiste. Davon sind nicht alle auslesbar bzw. beschaltbar, da es auch einige Spannungs- und Masseanschlusse gibt. In der folgenden Grafik sind die kompletten Pins inkl. Funktionen und Nummerierung aufgelistet. Die linke (grune) Seite soll dabei die Platine des Raspberry Pi's symbolisieren.

![Raspberry Pi GPIO Pin Belegung](https://tutorials-raspberrypi.de/wp-content/uploads/Raspbery-Pi-GPIO-Pin-Belegung-304x500.png)

> _Raspberry Pi GPIO Pin Belegung_

Alle Pins, welche „GPIO" im Namen haben, konnen programmiert werden. Daruber hinaus gibt es noch „Ground" (=Masseanschluss) und die Spannungspins (3.3V und 5V).

Wie du siehst, gibt es zwei Pin Belegungen: Einmal die aufsteigende Pin Belegung (oben links bei 1 beginnend) und dann noch die recht zufallig gewahlte Nummerierung der GPIOs. Dies ist wichtig, da man uber beide Nummern einen GPIO ansprechen kann.

So entspricht bspw. Pin 15 = GPIO 22. Achte immer darauf, ob von Pin oder GPIO gesprochen wird. In den meisten Tutorials wird jedoch nicht die Pin-Nummerierung, sondern die **GPIO Nummer genutzt**.

## Vorbereitung

Wie [zuvor](https://tutorials-raspberrypi.de/programmieren-lernen-raspberry-pi-einfuehrung) auch offnen wir die Python Konsole uber das Startmenu > Programming.

![](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Startmenu-Programming-Python-600x450.png)

In der geoffneten Python Konsole geben wir nun zunachst folgendes ein:
    
    
    import RPi.GPIO as GPIO

Wir importieren damit eine Bibliothek, womit wir die Raspberry Pi GPIO Pins programmieren konnen. Diese Bibliothek hat alle benoigten Funktionen bereits enthalten, sodass wir keine zusatzlichen Funktionen dafur schreiben mussen.

Weiterhin importieren wir auch noch ein Bibliothek, mit welcher wir das Skript fur kurze Zeit stoppen konnen. Dies wird im Anschluss noch interessant.
    
    
    import time

Anschließend geben wir an, ob wir die GPIOs per Boardnummern (1-40) oder uber ihre GPIO Nummer ansprechen wollen. Da wir letzteres wollen, lautet der Befehl dazu:
    
    
    GPIO.setmode(GPIO.BCM)

## Raspberry Pi GPIO Pins schalten - Ausgabe

Zunachst mochten wir ein paar einfache LEDs mittels der GPIOs schalten. Dazu bauen wir die LEDs entsprechend der nachfolgenden Grafik auf. Als Verbindung zwischen Raspberry Pi und dem Breadboard kannst du die Jumper Kabel nehmen und fur alle anderen Verbindung einfachen Draht. Die Farben spielen keine Rolle und sind nur zur besseren Unterscheidung gedacht.

![Raspberry Pi GPIO Output Steckplatine](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-GPIO-Output-Steckplatine-600x467.png)

Die LED hat zwei unterschiedlich lange Enden. Das langere Ende kommt an die positive 3.3 Volt Spannung des GPIO 23 (Pin 16). Der gewahlte Widerstand ist 330Ω (Ohm).

Nun geht es zuruck in die Python Konsole, in der wir unseren Code eingeben. Zunachst einmal mussen wir den **Pin als Output definieren**:
    
    
    GPIO.setup(23, GPIO.OUT)

Damit stehen nun die Output-Funktionen fur diesen Pin zur Verfugung. Mit den folgenden beiden Befehlen konnen wir die LED erst an- und anschließend wieder ausschalten:
    
    
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)

Mit diesem Befehl wird einfach gesagt, ob eine Spannung von 3.3V (HIGH) oder von 0V (LOW) angelegt werden soll.

Ist doch ziemlich einfach, oder? Wer eine kleine Blinkschaltung bauen mochte, kann dies z.B. folgendermaßen:
    
    
    for i in range(5):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.5)

Damit wird die LED 5 Mal an- und wieder ausgeschaltet, wobei dazwischen jeweils eine halbe Sekunde gewartet wird, bevor der Status geandert wird.

## Raspberry Pi GPIO Pins auslesen - Eingabe

Mit den GPIOs konnen aber nicht nur Strome geschaltet werden, sondern auch ausgelesen werden. Daher erweitern wir nun unsere Schaltung um einen Taster. Der Status soll dazu ausgelesen werden und sobald der Taster gedruckt wird, soll die LED leuchten. Wird der Taster nicht mehr gedruckt, so soll die LED auch aufhoren zu leuchten.

Zunachst erweitern wir die Schaltung. Neben dem Taster benotigen wir einen 10.000Ω Widerstand, welcher von einem Ende des Tasters an Ground verbunden wird. Dazwischen geht eine Verbindung zum GPIO 24 (Pin 18). Das andere Ende des Schalters wird an die 3.3 Volt Spannung angeschlossen:

![Raspberry Pi GPIO Input Steckplatine](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-GPIO-Input-Steckplatine-600x467.png)

Warum das ganze? Solange der Schalter nicht gedruckt ist, ist die Verbindung zwischen der 3.3V Spannung und dem GPIO geschlossen. Damit aber ein eindeutiger Zustand erkannt wird (entweder 0V oder 3.3V) ist die Verbindung uber einen sehr großen Widerstand zum Masseanschluss.  
Sobald der Taster gedruckt wird, schließt sich die Verbindung und am GPIO liegen 3.3V an.

**Hinweis**: Schließe niemals mehr als 3.3V an die GPIOs an, da sie sonst kaputt gehen konnen.

Kommen wir zum Code. Auch hier mussen wir zunachst den Status festlegen, jedoch wird diesmal der Pin als Input definiert:
    
    
    GPIO.setup(24, GPIO.IN)

Nun konnen wir auch schon den Status abfragen:
    
    
    GPIO.input(24)

Dies wird entweder 0 (wenn der Taster nicht gedruckt wurde) oder 1 (Taster gedruckt) ausgeben.

Im letzten Schritt erweitern wir das Programm nun noch folgendermaßen, sodass die LED immer dann an ist, wenn der Taster auch gedruckt wird.
    
    
    # Endlosschleife
    while True:
        if GPIO.input(24) == 0:
            # Ausschalten
            GPIO.output(23, GPIO.LOW)
        else:
            # Einschalten
            GPIO.output(23, GPIO.HIGH)

Abbrechen kannst du den Vorgang ubrigens mit STRG+C.

## Zusammenfassung

Zusammenfassend gibt es hier noch den Code des gesamten Skripts, falls jemand diesen in einer Datei speichern und als Ganzes aufrufen mochte.
    
    
    import RPi.GPIO as GPIO
    import time
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.IN)
    
    for i in range(5):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.5)
    
    # Endlosschleife
    while True:
        if GPIO.input(24) == 0:
            # Ausschalten
            GPIO.output(23, GPIO.LOW)
        else:
            # Einschalten
            GPIO.output(23, GPIO.HIGH)

Falls dir diese Einleitung Spaß gemacht hat, kann ich dir nur das Mini Projekt einer [Ampelschaltung](https://tutorials-raspberrypi.de/ampelschaltung-mit-gpio-teil-1/) empfehlen. Gegliedert in zwei Teile wird darin ein funktionierendes Ampelsystem, bestehend aus Auto- und Fußgangerampel, gebaut.

Weitere Informationen zu diesem Aufbau findest du z.B. [hier](https://up-community.org/wiki/RPi.GPIO).

Mit dem hier vermittelten Wissen kannst du bereits erste kleine Projekte starten. Hier ist ein kleiner Vorgeschmack:

Im [nachsten Teil](https://tutorials-raspberrypi.de/programmieren-lernen-am-raspberry-pi-teil-3-gui-erstellen/) schreiben wir unsere erste GUI (Graphisches User Interface), womit wir die GPIOs auch per Oberflache steuern konnen.
