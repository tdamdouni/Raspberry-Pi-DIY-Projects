# Raspberry Pi Foundation testet PiJuice – tragbarer Strom (Akku) für den Raspberry Pi

_Captured: 2017-11-12 at 21:48 from [www.bitblokes.de](https://www.bitblokes.de/raspberry-pi-foundation-testet-pijuice-tragbarer-strom-fuer-den-raspberry-pi/)_

Bereits im Marz 2015 lief eine [Kickstarter-Kampagne](https://www.kickstarter.com/projects/pijuice/pijuice-a-portable-project-platform-for-every-rasp) fur den PiJuice. Ich kann mich auch noch gut daran erinnern, weil ich fast ebenfalls mit gekickstartert hatte. Das Projekt war mit 1200% mehr als ausreichend finanziert. Ich hatte es damals sein gelassen und mir gedacht - wenn ich doch einen Akku fur den Raspberry Pi brauche, dann kaufe ich das Ding einfach spater.

PiJuice ist dann mit ordentlicher Verspatung nun erhaltlich. Als Grunde fur die Verzogerung werden technische Probleme, Schwierigkeiten bei der Herstellung und Business-Probleme angegeben. Rasenmahen fehlt noch, dann waren alle Bereich des Lebens komplett abgedeckt, oder?

### Raspberry Pi Foundation hat PiJuice gestestet

Den PiJuice gibt es bei [PiSupply](https://www.pi-supply.com/?s=pijuice&post_type=product), aber ich finde die Variante fur 25 Britische Pfund nicht, die bei der Raspberry Pi Foundation angegeben sind. Die gunstigste Variante kostet zirka 40 GBP und die kann man derzeit aber nicht bestellen. Sieht so aus, als wurde man erst die Backer versorgen - das ist auch mehr als fair. Im Shop habe ich auch eine Solar-Version erspat, bei der Du ein 6V Solarpanel dazu bekommst. Kostet knapp 55 GBP, gibt es derzeit aber auch nicht.

Aber egal, beschaftigen wir uns nicht weiter mit dem schnoden Mammon oder etwaigen Lieferengpassen, sondern lauschen wir gespannt, was uns die Pi-Meister zu sagen haben.

Der PiJuice ist mit einem Smartphone-Akku ausgestattet. Genauer gesagt handelt es sich um einen Motorola BP7X mit 1820mAh. Schon an der Sache ist, dass der Akku nicht wust reingedengelt wurde, sondern Du kannst ihn auf Wunsch sehr einfach tauschen. Wer vor 1864 geboren ist, erinnert sich vielleicht noch, wie angenehm das war, als man den Akku beim Mobiltelefon selbst tauschen konnte.

Die Hardware lasst sich, wie Du vielleicht schon richtig vermutet hast, auf die GPIO Pins des Raspberry Pis stecken. Allerdings werden die Stecker durchgeschleift und Du kannst einen weitere HAT montieren. Der PiJuice verwendet lediglich die I2C Pins.

Weiterhin kannst Du den PiJuice mit vier Schrauben am Raspberry Pi festschrauben. Damit ist die Konstruktion doch recht stabil.

![PiJuice: mobiler Strom für den Raspberry Pi \(Quelle: raspberrypi.org\)](https://www.bitblokes.de/wp-content/uploads/2017/11/PiJuice-Battery-Charging-Angle-2.jpg)

> _PiJuice: mobiler Strom fur den Raspberry Pi (Quelle: raspberrypi.org)_

Viele andere mobile Stromversorgungen fur den Raspberry Pi sind nicht so schick.

### Nicht nur schicker, sondern auch schlauer

An dieser Stelle kommen auch noch ein STM32-F0 microcontroller chip, RTC (Real-Time Clock) und Pi-Software zum tragen. Es ist namliche eine Energieverwaltung moglich. Somit wird aus dem PiJuice nicht nur eine mobile Stromversorgung, sondern eine Mini-USV oder eine unterbrechungsfreie Stromversorgung.

Nachdem Du die Software heruntergeladen und installiert hast, zeigt sich in der Taskleiste von Raspbian ein Akku-Symbol. Fahrst Du mit der Maus druber, siehst Du den Ladestand des Akkus. Mit einem Rechtsklick auf das Symbol gibt es umfangreiche Moglichkeiten zur Konfiguration.

Es gibt wohl eine Eigenart, bei der die Ladestandanzeige um 20 Prozent fallt, wenn man die USB-Stromversorgung aussteckt. Das hat irgendwas mit dem Schutzmechanismus bei Li-Ion-Akkus zu tun. Sorgen musst Du Dir laut Hersteller aber keine machen. Außerdem geben LEDs uber den Zustand des Akkus Aufschluss.

### Und wie lange rennt mein Pi nun damit?

Tja, das kommt auf den Pi an. Die Raspberry Pi Foundation hat einen [Raspberry Pi 3](https://www.bitblokes.de/ich-konnte-es-dann-doch-nicht-lassen/) damit versorgt, der einfach nichts getan hat. Damit hat der Strom fur zirka 4 Stunden gereicht. Das ist nicht gerade uppig. Mit einem Rasperry Pi Zero oder einem Pi A+ sollte sich diese Zahl verdoppeln lassen.

Ich selbst habe schon mal einen [Raspberry Pi A+ an eine Powerbank angeschlossen und ebenfalls einfach gemessen](https://www.bitblokes.de/raspberry-pi-a-am-akku-ist-ueber-30-stunden-gelaufen/), wann sich das Ding abgeschalten hat. Meine Powerbank hatte etwas mehr Saft und der A+ ist uber 30 Stunden gelaufen. Dafur war meine Losung auch nicht so schick wie der PiJuice.

![PiJuice von oben \(Quelle: raspberrypi.org\)](https://www.bitblokes.de/wp-content/uploads/2017/11/PiJuice-Battery-Top.jpg)

> _PiJuice von oben (Quelle: raspberrypi.org)_

### Herzschlag-Software

Ebenfalls interessant ist ein Watchdog, der auf den _Heartbeat_ des Pis hort. Meldet sich der Pi nicht mehr, dann wird die Stromzufuhr zuruckgesetzt und der Pi kann neu starten. Das ist sehr sinnvoll, wenn der Raspberry Pi an einer Stelle ist, die man schlecht oder nicht sofort erreichen kann.

Witzig, ich hatte bei meinem [Raspberry Pi B als Wassersensor](https://www.bitblokes.de/das-raspberry-pi-als-wassersensor-benutzen-e-mail-als-benachrichtung/) eine ahnliche Prozedur am Laufen. Damals aber mit einer drahtlosen USB-Netzwerkkarte. Vor ein paar Jahren war das WLAN-Konstrukt noch etwas instabil und manchmal wollte die WLAN-Karte einfach nicht mehr. Hat sich aufgehangt oder irgendwas Treiber. Somit habe ich ein Script laufen lassen, dass jede Minute meinen Router angepingt hat. Gab es keine Antwort, hat sich der Raspberry Pi neu gestartet und die WLAN-Verbindung funktionierte wieder. In der Zwischenzeit ist das obsolet, da die Treiber fur WLAN sehr stabil sind.

Auf der Seite de PiJuice befinden sich außerdem drei Knopfe, die sich individualisieren lassen. Per Standard ist der erste Knopf so konfiguriert, dass Du den Pi damit herunterfahren kannst, wenn Du ihn 10 Sekunden lang druckst. Konfigurieren kannst Du die Aktionen _Drucken / Loslassen, einmal drucken, doppelt drucken _und _zweimal lang drucken_. Dabei ist die Zeit als Parameter anpassbar.

So - nun will ich doch so einen schicken PiJuice. Muss ich wohl ein Auge offen halten, wann es den Akku fur den Winzling wieder gibt.

## Nette Pi-Konstellation

**Du kannst gerne Deinen Senf zu diesem Beitrag geben: [Hier geht es zu den Kommentaren](https://www.bitblokes.de/raspberry-pi-foundation-testet-pijuice-tragbarer-strom-fuer-den-raspberry-pi/)**
