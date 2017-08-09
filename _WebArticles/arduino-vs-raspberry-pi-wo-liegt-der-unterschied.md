# Arduino vs. Raspberry Pi: Wo liegt der Unterschied?

_Captured: 2017-05-18 at 09:48 from [www.techtag.de](https://www.techtag.de/it-und-hightech/arduino-vs-raspberry-pi-wo-liegt-der-unterschied/)_

![](https://www.techtag.de/wp-content/uploads/2016/08/raspard.001.jpeg)

> _Vorne: Raspberry Pi 2 Model B und A+; im Hintergrund: Arduino Uno, Pro Mini und LilyPad, (Bilder: Arduino, Multicherry, Florian Frankenberger/Wikipedia, CC-BY-SA 4.0)_

**Die beiden Mini-Computer Raspberry Pi und Arduino werden von vielen als Konkurrenzprodukte betrachtet. Bis zu einem gewissen Grad stimmt das auch. Tatsachlich sind sie aber grundverschieden. Auch das ist ein Grund, wieso beide harmonisch zusammenarbeiten.**

Streng genommen gibt es den oder das Arduino nicht. Einerseits beschreibt der Name, der auf die Lieblingsbar der Erfinder zuruckgeht, das Entwicklungswerkzeug und andererseits die Hardware. Auch diese lasst sich aufspalten in die Boards der US-amerikanischen Arduino LLC und der italienischen Arduino S.R.L. Welches der beiden den Namen tragen darf, daruber streiten sich die beiden Unternehmen derzeit vor Gericht. Grundsatzlich sind die Boards aber kompatibel zueinander. Es scheint darauf hinaus zu laufen, dass der Name Arduino kunftig nur noch in den USA gefuhrt wird, wahrend bautechnisch gleiche Boards im Rest der Welt als Genuino verkauft werden. Unabhangig vom Namensstreit gibt es die Boards in verschiedenen Ausfuhrungen, um so verschiedenen Anforderungen zu entsprechen.

![Arduino](https://www.techtag.de/wp-content/uploads/2016/08/Arduino.jpg)

> _Drei aus der Arduino-Familie: Uno, Pro Mini und LilyPad (Bilder: Arduino)_

[ Arduino Uno: Zum Angebot auf Amazon](https://www.amazon.de/Arduino-Uno-Rev-3-Mikrocontroller-Board/dp/B008GRTSV6/ref=sr_1_2?ie=UTF8&qid=1487851642&sr=8-2&keywords=arduino?utm_source=amazon)

Beim Raspberry Pi ist die Sache deutlich einfacher: Die Hardware heißt Raspberry Pi, das Betriebssystem beispielsweise Ubuntu Mate, Raspbian oder Windows 10 IoT Core. Auch der Raspberry Pi ist in mehreren Varianten erhaltlich.

![Raspberry](https://www.techtag.de/wp-content/uploads/2016/08/Raspberry.jpg)

> _Raspberry Pi 2 Model B und A+ (Bilder: Multicherry, Florian Frankenberger/Wikipedia, CC-BY-SA 4.0)_

[ Raspberry Pi Model B: Zum Angebot auf Amazon](https://www.amazon.de/Raspberry-Pi-Prozessor-Quad-Core-cortex-a53/dp/B01CD5VC92/ref=sr_1_3?ie=UTF8&qid=1487852060&sr=8-3&keywords=raspberry+pi?utm_source=amazon)

## Mikrocontroller vs. Computer

Fur Laien sind ein Raspberry Pi und ein Arduino Board kaum zu unterscheiden. Beide sind in der Standardausfuhrung etwa so groß wie zwei Streichholzschachteln und verfugen uber einen USB-Anschluss sowie mehrere Pins, die zur Programmierung wichtig sind. Wahrend der Arduino aber auf einen Rechner mit Windows, OS X oder Linux angewiesen ist, um Programmiercode zu erhalten, ist der Raspberry Pi ein eigener, kleiner Rechner, der per HDMI mit einem Monitor verbunden und per USB-Maus und -Tastatur gesteuert wird.

![Raspbian-Desktop mit geöffneten Programmen \(Bild: Saschen - Eigenes Werk, CC BY-SA 3.0\)](https://www.techtag.de/wp-content/uploads/2016/08/Raspbian-Desktop_Version_2015-09-25-e1470254826928.png)

> _Raspbian-Desktop mit geoffneten Programmen (Bild: Saschen/Wikipedia, CC BY-SA 3.0)_

So die Theorie. Praktisch bedeutet das, dass ein Arduino in der Lage ist, ein vorher aufgespieltes Programm wiederholt abzuspulen. Beispiel: „Wenn ich auf eine Taste drucke, aktiviere den Rollladenmotor fur zehn Sekunden." Der Prozess ist dabei immer gleich. Der Raspberry als kompletter Rechner vermag hingegen, mehrere Programme parallel und nacheinander auszufuhren. Ein Raspberry konnte dem Rollladen-Programm noch mehrere Variablen hinzufugen: „Wenn ich die Taste drucke und es draußen dunkel ist, schalte das Licht im Haus ein." Die Lichtsteuerung verlangt weitere Berechnungen und die Kombination des Befehls mit der Variable Helligkeit, die uber einen Sensor oder uber eine Programmierschnittstelle abgerufen wird.

![Ein Arduino ist in der Lage ist, ein vorher aufgespieltes Programm wiederholt abzuspulen \(Bild: Wlanowski - Eigenes Werk, CC-BY-SA 4.0\)](https://www.techtag.de/wp-content/uploads/2016/08/Arduino-ide-1.6.0-german.png)

> _Ein Arduino spult ein vorher aufgespieltes Programm wiederholt ab (Bild: Wlanowski/Wikipedia, CC-BY-SA 4.0)_

Bei dem Unterschied stellt sich die Frage, wieso man zu einem Arduino greifen sollte, wenn der Raspberry doch das Gleiche und mehr leistet? Zum einen sind Arduino-Boards ab weniger als funf Euro erhaltlich. Fur einen Raspberry werden Preise ab etwa 20 Euro aufgerufen. Außerdem ist die Programmierung der gleichen Aufgabe mit der Software [Arduino IDE](http://arduino.cc/en/Main/Software#toc1) auf einem Arduino einfacher als auf einem Raspberry, der vorher noch ein komplettes [konfiguriertes Betriebssystem](https://www.raspberrypi.org/downloads/) benotigt. Die einfachere Bedienung eines Arduinos macht den Bausatz ubrigens auch fur Programmier-Einsteiger interessanter.

## Keine Konkurrenz, sondern komplementar

Unter Bastlern werden die Boards nicht selten im Tandem verwendet. Wahrend beispielsweise der Raspberry eine Berechnung ausfuhrt, ubernimmt der Arduino auf Mitteilung des Raspberrys die Steuerung eines Motors. Andersherum ware es denkbar, dass ein Raspberry eine komplizierte Aufgabe erst dann verarbeitet, wenn ein Arduino dazu das Go ubermittelt. Die Verbindung zwischen den Geraten funktioniert sowohl kabelgebunden als auch drahtlos. Das ermoglicht beispielsweise die Steuerung der Rollladen im ganzen Haus ohne Umbauarbeiten durch Kabelkanale. So ware es denkbar, gunstiger Arduino-Boards an samtlichen elektrischen Geraten anzuschließen, wahrend ein Raspberry die zentrale Steuerung ubernimmt.

## Die Bier-Tastatur als Beispiel

Wie die Teamarbeit zwischen Raspberry Pi und Arduino aussehen kann, zeigte der tschechische Bierhersteller Staropramen. Auf der Technikkonferenz Webstock 2012 prasentierte das Unternehmen beruhrungsempfindliche Bierdosen, angeordnet als Tastatur. Die Arduinos in jeder Dose ubernahmen dabei die simple Aufgaben, bei Beruhrung den jeweiligen Buchstaben, Zahl oder Sonderzeichen an den Raspberry zu ubermitteln. Über diesen erfolgte wiederum die Tonausgabe, die Anzeige auf dem Fernseher und die Übermittlung der Daten.
