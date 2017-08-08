# Funksteckdosen mit dem Raspberry Pi nutzen

_Captured: 2016-11-07 at 11:03 from [www.tecchannel.de](http://www.tecchannel.de/a/funksteckdosen-mit-dem-raspberry-pi-nutzen,2064837)_

Funksteckdosen sind im Dreier- oder Sechserpack samt Fernbedienung in fast jedem Baumarkt erhaltlich, oft schon fur wenige Euro. Fur sich alleine sind die Steckdosen begrenzt interessant: Die mitgelieferte Fernbedienung ist nie zur Hand, wenn man Sie braucht, und ist so klein, dass sie gerne zwischen den Sofaritzen verschwindet. Mit einem gunstigen Sender und ein wenig Software machen Sie den Raspberry zur Schaltzentrale, die Steckdosen per Browser, Makro oder Handy von uberall her steuert. Was Sie dafur benotigen, ist ein Funkmodul mit 433 MHz. Ein Set mit Sender und Empfanger kostet bei Ebay oder Amazon zwischen 1 Euro (aus China) und rund 4 Euro (aus Deutschland) und ist uber eine Suche nach „RF Link Arduino" schnell zu finden. Die Sets werden in erster Linie fur den Arduino-Mikro- Controller verkauft, funktionieren aber mit einer entsprechenden Software-Bibliothek auch am Raspberry Pi.

  1. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,2)  
Kano: Bis auf den Bildschirm umfasst das uber Kickstarter finanzierte Einsteigerset alles, um einen Computer mit dem enthaltenen Raspberry Pi zusammenzusetzen. Der Preis liegt bei 99 US-Dollar.
  2. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,3)  
Raspberry Pi als Internet- Radio: Als Player fur eine Liste von vorbereiteten Streaming-URLs dient MPD. Dieser kann in diesem Projekt auch uber die beiden Taster Radiostationen wechseln.
  3. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,4)  
H2O IQ: Das grune Gehause beherbergt Feuchtigkeitssensor, Funkmodul und servogesteuerertes Ventil zur Bewasserung Ein Raspberry Pi dient als zentraler Bewasserungscomputer.
  4. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,5)  
Ein Gehause als PDF einfach ausdrucken: Aus Pappe lasst sich diese Einfassung namens „Punnet" fur den Raspberry Pi anfertigen, um die Platine vorerst provisorisch zu verstauen.
  5. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,6)  
Per Kopfdruck scannen und verschicken: Diese Scanner-Steuerung uber das Raspberry Pi nimmt Dokumente uber den USB-Port entgegen und leitet sie per E-Mail weiter.
  6. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,7)  
Hobby-Brauerei: Ein Mikro-Controller behalt die Sensoren der Fermentierung im Blick, und ein Raspberry Pi sorgt fur die richtige Temperatur wahrend des Brauens.
  7. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,8)  
Lego Mindstorms mit dem Raspberry Pi als Schaltzentrale: Das Modul Brickpi vereinigt die Robotik-Plattform von Lego uber eine separate Aufsteck-Platine mit dem Raspberry Pi.
  8. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,9)  
Kameramodul aus einer USB-Webcam: Viele der Billigkameras verstehen sich auch mit dem Raspberry PI beziehungsweise mit der dort installierten Linux-Distribution Raspbian.
  9. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,10)  
Raspberry Pi im Hohenrausch: Das Gehause in der passenden Form einer Himbeere (englisch „Raspberry") schutzt die Elektronik gegen die rauen Minustemperaturen auf 4 000 Metern.
  10. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,11)  
Zeitraffer und Dolly-Steuerung mit dem Raspberry Pi: Fur beeindruckende Videos aus Einzelbildern lasst dieser Aufbau eine Kamera mit Motorsteuerung langsam uber eine Schiene gleiten.
  11. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,12)  
Fernbedienung fur den Raspberry Pi: Anstatt einen USB-Port mit einem IR-Receiver zu belegen, kann ein Sensor auch direkt an den GPIO-Pins der Platine angeschlossen werden.
  12. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,13)  
Blick uber Sudwest-England aus 40 Kilometern Hohe: An einem Wetterballon reiste der Raspberry Pi samt Kamera und CB-Funk-Transmitter in die Stratosphare und wurde nach der Landung uber GPS-Ortung geborgen.
  13. **[Raspberry Pi in der Praxis **](http://www.tecchannel.de/g/raspberry-pi-in-der-praxis,37728,14)  
Tablet mit dem Raspberry Pi: Als Display kommt ein kapazitiver Touchscreen mit 10 Inch Bildschirmdiagonale zum Einsatz. Das Gehause besteht aus Birke und Kohlefaser und der Rahmen ist passgenau aus Sperrholz gefrast.

## Auswahl: Nicht jede Funksteckdose ist geeignet 

Funksteckdosen gibt es inzwischen nicht nur optisch, sondern auch technisch in großer Vielfalt. Fast alle Arten lassen sich auch mit dem Raspberry steuern. Am einfachsten und zuverlassigsten funktionieren Steckdosen, die sich uber zehn Dipschalter einstellen lassen, die hinter einer kleinen Klappe mit kleiner Kreuzschlitzschraube verborgen sind. Steckdosen ohne Dipschalter, insbesondere die aktuell oft als Billigware verkauften selbstlernenden Dosen, lassen sich uber den Raspberry oft nur nach langeren Versuchen ansteuern und erfordern je nach Hersteller Software-Anpassungen auf dem Raspberry Pi.

![Dankbares Einstiegsmodell: Die verbreitete Funksteckdosen-Variante mit zehn Dipschaltern ist das am einfachsten anzusteuernde und empfehlenswerte Modell zur Hausautomatisierung.](http://images.cio.de/images/computerwoche/bdb/2518803/840x473.jpg)

> _Dankbares Einstiegsmodell: Die verbreitete Funksteckdosen-Variante mit zehn Dipschaltern ist das am einfachsten anzusteuernde und empfehlenswerte Modell zur Hausautomatisierung._

Ein weiterer Nachteil der Billigware ist, dass viele Modelle nach einem Stromausfall oder auch nur einem Wechsel der Steckdose ihre Codierung vergessen und dann neu eingelernt werden mussen. Wir raten deshalb deshalb zu Steckdosenmodellen, das sich mit zehn Dipschaltern programmieren lassen. Je nach Hersteller sind die Dipschalter mit 1 bis 10 oder mit 1 bis 5 und A bis D beschriftet - beide Versionen sind gleichermaßen nutzbar. Aktuell kostet ein Dreierset etwa bei Online-Versandhausern [rund 10 Euro](http://www.pollin.de/shop/dt/MzMzOTQ0OTk-/Haustechnik/Funkschaltsysteme/Funksteckdosen_Set_mit_3_Steckdosen.html).

Zunachst sollten Sie Fernbedienung und Steckdosen aufeinander abstimmen. Dazu wird an den funf Dipschaltern der Fernbedienung und den linken funf Dipschaltern der Steckdosen der Systemcode eingestellt, uber den die Dosen erreichbar sind. Vorsicht: Die Verwendung von 00000 oder 11111 als Systemcode bietet gute Chancen, dass einer Ihrer Nachbarn denselben Code verwendet und damit unter Umstanden Ihre Steckdosen schaltet. Funktioniert die Steckdose mit der Fernbedienung, kann die Einrichtung des Raspberry Pi als Schaltzentrale beginnen.

  


Die Steckdosen uber eine SSH-Konsole schalten zu konnen ist ein nettes Spielzeug, fur eine echte Anwendung aber etwas unpraktisch - weder kann man ubers Netz schalten noch kann man externe Gerate einbinden. Interessanter wird es, wenn man den in Rasberry Remote enthaltenen Server startet. Dazu mussen Sie den Quellcode etwas anpassen. Verwenden Sie den Befehl nano ~/raspberry-re mote/daemon.cpp und andern Sie die Zeile „nPlugs=10" zu „nPlugs=1110"

![Belegung der GPIO-Pins: Diese hat sich zwischen den Raspberry-Pi-Revisionen und Versionen geringfügig geändert. Der hier vorgestellte Aufbau funktioniert aber mit allen Versionen des Raspberry Pi.](http://images.cio.de/images/computerwoche/bdb/2518805/840x473.jpg)

> _Belegung der GPIO-Pins: Diese hat sich zwischen den Raspberry-Pi-Revisionen und Versionen geringfugig geandert. Der hier vorgestellte Aufbau funktioniert aber mit allen Versionen des Raspberry Pi._

Standardmaßig ist der Server im Netzwerk uber den Port 11337 erreichbar. Wem Sie dies andern wollen, tragen Sie eine andere Nummer hinter „Port" im ubersichtlichen Quellcode von daemon.h ein. Mit sudo make daemon wird der Hintergrundprozess (Daemon) dann kompiliert. Mit

sudo ./daemon >/dev/null &

starten Sie den Server als Hintergrundprozess. Bedient wird der Damon uber eine simple TCP-Netzwerkverbindung, zum Beispiel uber Netcat oder ahnliche Programme. Um beispielsweise eine Steckdose anzuschalten, geben Sie auf der Kommandozeile an:

echo -en "Codierung"|nc -w 1 <ip> <port>

Als IP geben Sie die IP-Nummer ihres Raspberry Pi an und als Port den TCP-Port, auf den der Server lauscht. „Codierung" besteht aus dem Systemcode wie bei send, gefolgt von „0" und der Dosennummer. In unserem Fall ware das etwa

echo -en "1000101"|nc -w 1 192.168.178.25 11337

wobei der Parameter „-w" dafur sorgt, dass Netcat die Verbindung zum Damon nach einer Sekunde selbsttatig wieder trennt. Damit ist die Funksteckdose also schon mal am Netz und kann von beliebigen Applikationen ein- und ausgeschaltet werden, sofern diese TCP-Socket- Verbindungen aufbauen konnen. Sinnvoll ist diese Art der Ansteuerung in erster Linie fur Script-Sprachen wie Python oder Perl, die man auf diese Weise zum Steuern von Funksteckdosen uber das lokale Netzwerk oder das Internet verwendet. Es besteht jedoch ein gewisses Risiko, wenn man den Port des Damons fur das gesamte Internet freigibt. Ein Missbrauch konnte unter Umstanden das Raspberry-Pi- System samt dem dahinterliegenden Netzwerk fur einen Angreifer offenlegen. Wenn Sie das System also in einem fremden Netz oder dem Internet uber TCP-Sockets erreichbar machen, sollten Sie unbedingt den Zugriff uber IP-Tables oder ein VPN auf autorisierte Kommunikationspartner beschranken.

![Schalten der Funksteckdosen über den Browser: Eine simple Weboberfläche zum Ein- und Ausschalten von Funksteckdosen ist auf dem Raspberry Pi in wenigen Minuten installiert.](http://images.cio.de/images/computerwoche/bdb/2518806/840x473.jpg)

> _Schalten der Funksteckdosen uber den Browser: Eine simple Weboberflache zum Ein- und Ausschalten von Funksteckdosen ist auf dem Raspberry Pi in wenigen Minuten installiert._

## Universelles Schalten: Ein und Aus per Browser 

Die Socket-Verbindung des Damons bringt die Funksteckdosen ans Netz, die Bedienung erfordert aber immer noch ein wenig Programmierung oder den Aufruf hasslicher Befehlszeilen auf der Konsole. Raspberry Remote hat auch hier Abhilfe: Im Verzeichnis „./webinterface" finden Sie eine Weboberflache, mit der man die Funksteckdosen in den Browser bringt. Die Weboberflache benotigt einen Webserver wie Apache und PHP. Dies lasst sich mit dem Kommando

sudo apt-get install apache2 php5

installieren, falls noch nicht vorhanden. Bringen Sie dann das Script-Verzeichnis in das Wurzelverzeichnis des Webservers:

mv ~/raspberry-remote/ webinterface/*/var/www/funk

und passen Sie dort die Konfigurationsdatei an:

nano /var/www/funk/config.php

Wenn der Damon auf dem selben Raspberry Pi lauft wie der Webserver, setzen Sie

$target=$_SERVER['SERVER_ADDR']

Laufen Webserver und Damon auf verschiedenen Rechnern, geben Sie hier die IP-Nummer des Damons an, den der Webserver ansprechen soll. Die Variable „$port" setzen Sie auf die Portnummer, unter welcher der Damon erreichbar ist. Unter „$config" konnen Sie in einem Array beliebig viele Schaltaktoren definieren. Sie geben wie gehabt als Parameter den Systemcode, die Dosennummer und eine frei wahlbare Textbeschreibung fur diese Dose an. Nun konnen Sie uber den Browser unter http://<ip>/funk das Kommando-Interface zum Schalten aufrufen.

Mit der Weboberflache ergibt sich die Moglichkeit, das Schalten auf anderen, tastaturlosen Geraten wie etwa einem Smartphone oder einem Tablet zu erledigen. Sie konnen dafur einfach ein Lesezeichen auf dem Desktop des Gerates hinterlegen. Fur kleinere Displays konnen Große und Layout der Schalterquadrate im Quellcode leicht verandert werden, so dass bei Bedarf auch mehr Gerate auf das Handydisplay passen.

Auch uber das Webinterface kann nicht nur per Fingerzeig oder Mausklick, sondern auch ganz direkt geschaltet werden. Geben Sie dafur einfach gleich beim Aufruf die Parameter in der URL an. Ein Beispiel:

http://<ip>/funk/index.php?group= 10001&switch=01&action=1

Die Parameter sind dieselben wie oben, „action= 1" heißt, dass die Steckdose eingeschaltet wird. Dafur gibt es dafur viele nutzliche Anwendungen: So konnen Sie etwa den Strom an Peripheriegeraten wie Scanner, Drucker oder externer Festplatte einschalten, indem Sie die URL in einer Verknupfung ablegen Tipp: Eine alternative Methode mit Android- App und Sprachsteuerung ist[ in diesem Blog](http://www.pcwelt.de/w89l) beschrieben.

_Dieser Artikel basiert auf einem Beitrag der TecChannel-Schwesterpublikation [PC-Welt](http://www.pcwelt.de/ratgeber/Funksteckdosen_mit_dem_Raspberry_Pi_einrichten-Schalten___walten-8655824.html)._
