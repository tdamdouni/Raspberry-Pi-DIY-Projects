# Fahrzeugdaten übertragen mit dem Raspberry Pi

_Captured: 2017-05-11 at 22:04 from [www.raspberry-pi-geek.de](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi)_

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/02/fahrzeugdaten-uebertragen-mit-dem-raspberry-pi/aa_fsa-jr13.jpg/16347-1-ger-DE/AA_FSA-jr13.jpg_large.jpg)

Mess- und Steuergerate in Fahrzeugen kommunizieren uber den sogenannten CAN-Bus miteinander. Auf den kann man auch unter Linux zugreifen - und was liegt da naher, als einen Raspberry Pi dafur zu verwenden?

Bei der Formula Student handelt es sich um einen internationalen Konstruktionswettbewerb. Um daran teilzunehmen, muss ein Team aus Studenten ein Rennfahrzeug nach dem Formula-SAE-Reglement konstruieren und fertigen. Der Wettbewerb umfasst die statischen Disziplinen Engineering Design, Cost Analysis und Business Presentation sowie die dynamischen Disziplinen Skid Pad, Acceleration, Autocross, Endurance und Fuel Efficiency.

Die meisten Punkte lassen sich beim Engineering Design sammeln, bei dem eine Experten-Jury die Konstruktion des Fahrzeuges beurteilt. Dabei stellen die Punkterichter nicht nur Fragen zu den konstruierten Bauteilen, sondern diskutieren auch die Konstruktionsmethoden, wie etwa den Einsatz moderner, rechnergestutzter Konstruktionshilfsmittel. Neben der Konstruktion bespricht und bewertet die Jury auch die Testphase der Einzelkomponenten sowie des Gesamtfahrzeugs.

Fur die Cost Analysis gilt es, vorab eine Kostenaufstellung einzureichen, die jedes Einzelteil des Fahrzeugs sowie dessen Preis nachweist. Als Basis dient dabei eine standardisierte Tabelle, die jedes Team verwenden muss. Zum Preis eines Bauteils tragen neben dem Rohmaterial auch Maschinenstunden zur mechanischen Bearbeitung sowie eventuelle Nachbearbeitungszeiten (etwa fur das Schleifen von Lagersitzen) bei. Stoßen die Juroren auf fehlende oder falsch gelistete Teile, hagelt es Strafpunkte.

Die Business Presentation stellt ein Geschaftsmodell fur die Vermarktung des Fahrzeugs vor, wobei Amateur-Rennfahrer als Zielgruppe dienen. Die Jury nimmt bei der Beurteilung die Position von Produzenten und Investoren ein.

Die Beschleunigungsleistung der Fahrzeuge gilt es, bei der Disziplin Acceleration auf einer 75 Meter langen Strecke zu beweisen. Der Start erfolgt aus dem Stand, jedes Team darf vier Mal antreten. Dabei mussen mindestens zwei unterschiedliche Fahrer zum Einsatz kommen. Die beste gefahrene Zeit fließt dann in die Wertung ein.

Bei der Disziplin Skid Pad muss der Rennwagen zwei Kreise je zweimal durchfahren. Dabei decken die hohe konstante Kurvengeschwindigkeit und der Lastwechsel beim Wechsel in den zweiten Kreis jede Fahrwerksschwache gnadenlos auf.

Zum Autocross geht es auf eine rund 800 Meter lange Strecke mit unterschiedlichem Start und Ziel. Dabei geht es nicht nur um Punkte fur diese Disziplin, sondern auch um die Qualifikation fur den abschließenden Endurance-Wettbewerb ([Abbildung 1](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi)), bei dem es die meisten Punkte zu gewinnen gibt.

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/02/fahrzeugdaten-uebertragen-mit-dem-raspberry-pi/abbildung-1/16350-1-ger-DE/Abbildung-1_large.jpg)

> _Abbildung 1: Der jr13 der Grazer Rennteams auf der Strecke. (Bild: Michael Trzesniowski / joanneum racing graz)_

Die Endurance-Strecke ahnelt jener fur den Autocross, weist aber andere Slalom-Passagen auf und ist als Rundkurs mit geschlossenem Start und Ziel ausgelegt. Bei dieser Prufung starten die Fahrzeuge in der umgekehrten Reihenfolge des Autocross-Ergebnisses und mussen eine Distanz von 22 Kilometern absolvieren. Das Reglement schreibt nach halber Distanz einen Fahrerwechsel vor, bei welchem der Rennwagen fur funf Minuten abgestellt werden muss.

Der Kraftstoffverbrauch bei den Prufungen fließt in die Fuel-Economy-Wertung ein, die daneben auch die Zeit erfasst, die das Fahrzeug fur die Endurance-Disziplin benotigt hat. Damit geht es hier nicht nur um eine reine Verbrauchswertung, sondern vielmehr um die Effizienz des Rennfahrzeuges.

Einen Eindruck uber die Wertigkeit der einzelnen Disziplinen gibt [Abbildung 2](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi) am Beispiel eines Formula-Student-Wettbewerbs am Hockenheimring (hier steht [stat] fur statische Prufungen, [dyn] fur dynamische). Bei anderen Wettbewerben kann die Verteilung der Punkte leicht abweichen, die Schwerpunkte liegen aber in den statischen Disziplinen stets beim Engineering Design und in den dynamischen auf der Endurance.

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/02/fahrzeugdaten-uebertragen-mit-dem-raspberry-pi/abbildung-2/16353-1-ger-DE/Abbildung-2_large.png)

> _Abbildung 2: Die Punkteverteilung der Formula Student Germany im Jahr 2013._

#### Anforderungen

Die wichtigsten Anforderungen an rennfahrzeugtaugliche Hardware fallen immer gleich aus: Die Komponenten mussen moglichst klein sein, durfen nicht zu viel Gewicht auf die Waage bringen und mussen Stoße und Vibrationen klaglos wegstecken. All diese Eigenschaften sprechen gegen normale PCs - aber stark fur den Einsatz eines Raspberry Pi.

Schon lange vor dem eigentlichen Wettbewerb muss ein Formula-Student-Rennfahrzeug schon auf der Teststrecke seine Fahigkeiten beweisen. Das geht nicht ohne eine Datenubertragung vom Fahrzeug an die Box, denn nur so kann der Renningenieur standig alle Fahrzeugdaten im Auge behalten. Damit auch Experten im Entwicklungslabor die Werte laufend einsehen konnen, gilt es, diese zudem via Internet zu ubertragen ([Abbildung 3](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi)).

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/02/fahrzeugdaten-uebertragen-mit-dem-raspberry-pi/abbildung-3/16356-1-ger-DE/Abbildung-3_large.png)

> _Abbildung 3: Die Gesamtarchitektur des Monitoring-Projekts im Überblick._

Dabei ubernimmt der Raspberry Pi die Aufgabe, im Fahrzeug Messdaten uber den CAN-Bus auszulesen und uber einen Webserver bereitzustellen. Dazu liest er die Daten mithilfe eines Programms aus und speichert sie in eine Datenbank.

Ein modernes Formula-Student-Fahrzeug wimmelt formlich vor Sensoren, die unzahlige Daten erfassen. Als wichtigste Messwerte fur die ersten Tests dienen Öldruck, Wasser- und Öltemperatur des Motors: Laufen sie aus dem Rahmen, droht ein Motorschaden. Sind diese Grundfunktionen des Fahrzeugs erfolgreich getestet, kann es an die Motor- und Fahrwerksabstimmung gehen. Hier interessieren dann Sensorwerte wie Bremsdruck, Reifentemperatur, Beschleunigung und viele andere.

Der in diesem Artikel beschriebene Rennwagen wurde von Fahrzeugtechnik-Studierenden selbst entwickelt - die Betreiber wissen also genauestens, welche Gerate verbaut und am CAN-Bus angeschlossen wurden.

Einen solchen Bus gibt es hochstwahrscheinlich auch in Ihrem Pkw - da liegt die Idee nahe, die hier demonstrierten Techniken auch einmal am eigenen fahrbaren Untersatz auszuprobieren. Das ware allerdings eine extrem schlechte Idee, mit moglicherweise katastrophalen Folgen.

Der CAN-Bus bietet namlich keinerlei Authentifizierungsmechanismen, sodass Sie mit CAN-Nachrichten problemlos beispielsweise die Kuhlwasserpumpe abschalten konnten. Schon eine einzige versehentlich gesendete Nachricht konnte also zu Motorschaden fuhren oder im schlimmsten Fall zu einem Unfall.

Lassen Sie also besser die Finger von der Fahrzeugelektronik - auf jeden Fall bei Pkws, mit denen Sie am offentlichen Straßenverkehr teilnehmen wollen.

#### CAN-Bus

Über den [CAN-Bus](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8) des Rennfahrzeugs laufen alle relevanten Daten zwischen den Steuergeraten. Fur die Telemetrie fangt ein CAN-Adapter der Firma Peak System alle Nachrichten ab. [Listing 1](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi) verdeutlicht, wie die entsprechenden Daten aussehen.

Der CAN-Bus kennt vier verschiedene Frame-Typen. Ein reiner Daten-Frame enthalt bis zu 8 Daten-Bytes. Ein Remote-Frame ubermittelt eine Datenanforderung eines anderen Bus-Teilnehmers, ein Error-Frame signalisiert Fehlerzustande. Mit einem Overload-Frame schließlich lasst sich eine Zwangspause zwischen Daten- und Remote-Frames einrichten.

Beim Formula-Student-Renner greift der CAN-Adapter lediglich passiv Datenpakete am CAN-Bus ab, es interessieren also nur Daten-Frames wie der in [Listing 1](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi) gezeigte.

Listing 1
    
    
    $ ./candump can0
    can0 0x713 [8] 2C EB C2 4A 65 0D EB 00
    can0 0x5C4 [8] AE 65 0D 3B C2 4A 65 0D
    can0 0x5C2 [8] 5A EB C2 4A EB C2 4A 30

Die unterschiedlichen Sensorwerte landen in einem oder mehreren Bytes der CAN-Nachricht, je nach Auflosung und Messbereich des Sensors. Die Bedeutung der einzelnen Bytes in der Nachricht mit der ID `0x713` zeigt die [Tabelle "CAN-Daten der ID 0x713"](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi).

Byte

Bedeutung

0

Öldruck

4

Kraftstofftemperatur

5

Öltemperatur

7

Wassertemperatur

Bei der Zuteilung der Messsignale an die Nachrichten gilt es, Signale nach Prioritaten zusammenzufassen, um nicht mehr unterschiedliche CAN-Nachrichten zu generieren, als unbedingt notwendig. Das halt die Busauslastung so gering wie moglich.

  


#### Hardware

Fur so eine Aufgabe mochte man einen leistungsfahigen Server verbauen. Im Renneinsatz relevant sind aber in erster Linie die Große, das Gewicht, der Stromverbrauch und nicht zuletzt der Preis. Da bietet sich fast zwangslaufig ein Raspberry Pi an. Auch im neuesten Rennfahrzeug von _joanneum racing graz_ [[1]](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8) sammelt ein solcher die Messdaten, wertet sie aus und stellt sie dem Boxenteam bereits wahrend des Rennens zur Verfugung.

Daneben kommen ein aktiver USB-Hub, ein WLAN-Stick, eine WLAN-fahige Kamera, ein CAN-USB-Adapter sowie ein UMTS-Stick zur Datenubertragung an die Box zum Einsatz - und unvermeidlicherweise ein paar Kabel ([Abbildung 4](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/2)).

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/02/fahrzeugdaten-uebertragen-mit-dem-raspberry-pi/abbildung-4/16359-1-ger-DE/Abbildung-4_large.jpg)

> _Abbildung 4: Die Hardware-Komponenten im Testaufbau._

#### CAN unter Linux

Der Linux-Kernel bringt bereits etliche Treiber fur den CAN-Bus mit, als einheitliche Abstraktionschicht lassen sich diese als Netzwerk-Devices ansprechen ([Abbildung 5](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/2)). Die Treiber beweisen ubrigens, dass nicht nur private Kernel-Hacker und IT-Firmen am freien Betriebssystemkern mitprogrammieren - der Code wurde von Volkswagen Group Electronic Research beigetragen.

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/02/fahrzeugdaten-uebertragen-mit-dem-raspberry-pi/abbildung-5/16362-1-ger-DE/Abbildung-5_large.png)

> _Abbildung 5: SocketCAN im Linux Kernel. (Bild: Wikimedia Commons)_

Auch der verwendete Treiber fur den USB-CAN Adapter der Firma Peak ist eigentlich in dem Linux-Kernel enthalten - allerdings nicht beim Standard-Raspbian. Man muss daher das Modul selbst kompilieren, aber auch das erweist sich als nicht ganz einfach: Im Standard-Raspbian-Image [[2]](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8) versieht ein von der Raspberry Pi Foundation modifizierter, speziell optimierter Kernel (3.6.11+) den Dienst, der im Repository weder die passenden Kernel-Sourcen noch die zugehorigen Header fuhrt.

Es gilt also, erst einmal auf den Standard-Kernel von Raspbian zu wechseln ([Listing 2](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/2), Zeile 1) und anschließend in der Datei `/boot/config.txt` den neuen Kernel einzutragen (`kernel=vmlinuz-3.6-trunk-rpi`). Nach einem anschließenden Neustart fehlt zwar noch der Peak-Treiber [[3]](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8) ([Listing 2](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/2), Zeile 2), aber es liegen zumindest die passenden Header-Files vor, sodass man den Treiber nun ubersetzen und installieren kann ([Listing 3](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/2)).

Listing 2
    
    
    $ sudo apt-get install linux-image-3.6-trunk-rpi linux-headers-3.6-trunk-rpi libpopt-dev
    $ grep CAN_PEAK /boot/config-3.6-trunk-rpi
    # CONFIG_CAN_PEAK_USB is not set

Listing 3
    
    
    $ wget http://www.peak-system.com/fileadmin/media/linux/files/peak-linux-driver-7.9.tar.gz
    $ tar xvzf peak-linux-driver-7.9.tar.gz
    $ cd peak-linux-driver-7.9
    $ make PCI=NO_PCI_SUPPORT USB=USB_SUPPORT
    $ sudo make install
    $ sudo depmod -a

Damit liegt das Modul nun einsatzbereit vor. Man ladt es entweder selbst mit `sudo modprobe pcan` oder steckt den CAN-Adapter ein - das Modul wird dann automatisch geladen. Im Fall eines Kernel-Updates darf man allerdings nicht vergessen, den CAN-Treiber wieder zu kompilieren und neu zu installieren.

Der PCAN-Treiber legt bei der Installation automatisch die Datei `/etc/modprobe.d/pcan.conf` an. Um die Bitrate des CAN-Busses auf 1 Mbit/s zu erhohen, muss man bei diesem Modul die Geschwindigkeit beim Laden des Moduls angeben - automatisiert klappt das beispielsweise mit `options pcan bitrate=0x0014` in dieser Datei. Werte fur andere Geschwindigkeiten finden Sie in der [Tabelle "PCAN-Modul: Geschwindigkeiten"](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/2) (entnommen aus dem PCAN-Quellcode). Bei anderen CAN-Modulen erreichen Sie dasselbe mit folgendem Befehl:
    
    
    # ip link set can0 type can bitrate 1000000

Bitrate

Moduloption

1000 kbit/s

0x0014

500 kbit/s

0x001C

250 kbit/s

0x011C

125 kbit/s

0x031C

100 kbit/s

0x432F

50 kbit/s

0x472F

20 kbit/s

0x532F

10 kbit/s

0x672F

5 kbit/s

0x7F7F

Zum Zugriff auf das CAN-Netzwerk-Device gibt es im Userspace die Can-Utilities [[4]](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8), die man nach dem Herunterladen des Quellcodes mit `make; sudo make install` installiert. Zum Auslesen des CAN-Busses dient das Tool `candump` (siehe [Listing 1](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/0)). Ein Datenpaket auf dem CAN-Bus besteht aus einer 11 Bit langen CAN-ID, es folgen eine Langenangabe (1 bis 8 Byte) sowie die Daten. Bei Bedarf ließen sich mit `cansend` sogar eigene Nachrichten in den CAN-Bus schreiben.

  


#### Netzanbindung

Zur Datenubertragung aus dem Rennwagen auf einen Laptop kommt eine Internetverbindung via 3G-Datenstick zum Einsatz. Der Raspberry Pi erkennt den Stick beim Einbinden automatisch als Datenspeicher, was unter Windows zwar den Installationsvorgang erleichtert, unter Linux aber nichts bringt. Um hier auf den Netzwerkmodus umzuschalten, gilt es, einen SCSI-Code an den Stick zu senden. Dazu dient das Programm `sg_raw` aus dem Paket _sg3_utils_:
    
    
    $ /usr/bin/sg_raw /dev/sr0 11 06 20 00 00 00 00 00 01 00

Alternativ klappt die Umstellung auch mit dem Programm `usb_modeswitch` [[5]](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8). Nach der Umstellung bleibt der Stick im neuen Modus. Der Windows-Treiber allerdings lasst sich nun nicht mehr erreichen - mochten Sie den Stick auch auf einem Windows-Rechner nutzen, mussen Sie den Treiber vorher herunterkopieren.

Unter Linux lasst sich der UMTS-Stick nach der Umstellung uber das Device `/dev/ttyUSB0` ansprechen, mittels `wvdial` stellt man eine Netzwerkverbindung her. Um den Vorgang zu automatisieren, tragen Sie in `/etc/network/interfaces` die Zeilen aus [Listing 4](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/4) ein.

Die Datei `/etc/wvdial.conf` nimmt dabei die providerspezifische Konfiguration auf. Hier darf man durchaus mehrere Provider eintragen. Bei einem Formula-Student-Wettbewerb im Ausland lasst sich dann einfach eine landesspezifische SIM-Karte einsetzen und der Providername in `/etc/network/interfaces` andern.

Nun besitzt der RasPi uber den UMTS-Stick eine Internetanbindung. Um die offentliche IP-Adresse des Minirechners herauszufinden, wurde ein einfacher Redirect-Service programmiert: Der RasPi ruft mit `wget` eine externe Webseite auf, diese speichert die IP-Adresse, und eine weitere Webseite leitet mit dem PHP-Befehl `header("Location: http://$ip/");` (wobei `$ip` die gespeicherte IP enthalt) auf den RasPi weiter. Ein (offentlicher oder selbst programmierter) [DynDNS](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8)-Dienst konnte Ähnliches leisten.

Die Telemetriedaten erscheinen benutzerfreundlich aufbereitet auf einer Webseite. Dazu lauft auf dem Raspberry Pi ein Apache-Webserver. Dieser lasst sich mitsamt aller benotigten Pakete mit dem Befehl aus [Listing 5](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/4) einrichten

Listing 5
    
    
    $ sudo apt-get install apache2 php5-mysql libapache2-mod-php5 mysql-server

Ein per Stecker mit dem CAN-Bus und der Stromversorgung des Fahrzeuges verbundenes Gehause schutzt alle verwendeten Hardware-Komponenten vor Wasser und Staub. Beim Einschalten des RasPi muss dieser selbststandig alle Programme laden und mit der Datenaufzeichnung in der Datenbank beginnen - er kommt im Fahrzeug ja ohne Tastatur und Monitor zum Einsatz.

#### Jr_candump

Das Startskript aus [Listing 6](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/4) nimmt beim Hochfahren des RasPi alle notwendigen Schritte vor. Die erste Zeile des Skripts aktiviert die Netzwerkschnittstelle des CAN-Adapters. Anschließend startet das modifizierte Candump-Programm `jr_candump` mit den dazugehorigen Parametern.

Dieses Programm wurde so abgeandert, dass sich die empfangenen Daten uber die neue Option `-D` in eine Datenbank [[6]](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8) schreiben lassen. Nach dem Programmstart erstellt Jr_candump eine Datenbank, legt in dieser mit dem SQL-Statement aus Zeile 1 von [Listing 7](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/4) eine Tabelle an und bereitet dann das SQL-Statement aus Zeile 2 fur das Speichern der Daten vor.

Listing 7
    
    
    CREATE TABLE if not exists candata(ID float, TIMESTAMP float, YAWRATE varchar(4), ACCY varchar(4), ROLLRATE varchar(4), ACCX varchar(4), ACCZ varchar(4), FUELTEMP varchar(4), WATERTEMP varchar(4), OILPRESSURE varchar(4), OILTEMP varchar(4)) ENGINE = MEMORY
    INSERT INTO candata (ID, TIMESTAMP, YAWRATE, ACCY, ROLLRATE, ACCX, ACCZ, FUELTEMP, WATERTEMP, OILPRESSURE, OILTEMP) VALUES (?,?,?,?,?,?,?,?,?,?,?)

Wie der Schluss von Zeile 1 zeigt, liegt die Datenbank im Hauptspeicher des RasPi: Fur das direkte Speichern auf der SD-Card laufen die Daten zu schnell ein. Abschließend verknupft Jr_candump die richtigen Variablen mit den entsprechenden Platzhaltern im `INSERT`-Statement aus Zeile 2. Nach dem Vorbereiten der Datenbank ruft Jr_candump bei jedem Empfang einer CAN-Nachricht eine Funktion zu deren Auswerten auf - den Kernteil davon sehen Sie in [Listing 8](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/4).

Listing 8
    
    
    switch (frame.can_id) {
      case 0x713:
        sprintf(fueltemp,    "%02x", frame.data[4]);
        sprintf(watertemp,   "%02x", frame.data[7]);
        sprintf(oilpressure, "%02x", frame.data[0]);
        sprintf(oiltemp,     "%02x", frame.data[5]);
        InsertCANframe();
        break;
      /* nächste CAN-ID ... */
    }

Die Auswerteroutine unterscheidet uber eine Switch-Anweisung die CAN-ID der eingehenden Nachricht und schreibt entsprechend die aktuell empfangenen Daten in die richtigen Variablen. Es folgt ein Aufruf der Funktion `InsertCANframe()`. Diese erhoht den Zahler der ID, welche die einzelnen Datensatze der Datenbank nummeriert, und schreibt die Werte der Variablen mit dem zuvor vorbereiteten Statement in die Datenbank.

  


#### Visualisierung der Daten

Auf dem RasPi lauft ein Apache-Webserver, der mit einer kleinen PHP-Anwendung die Daten aus der Datenbank ausliest und online darstellt. Die Daten werden dabei mit [Ajax](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8) standig aktualisiert und mittels des jQuery-Frameworks [[7]](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8) jqPlot [[8]](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8) visualisiert ([Abbildung 6](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/6)). Das Team an der Box erhalt damit online Zugriff auf alle relevanten Parameter.

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/02/fahrzeugdaten-uebertragen-mit-dem-raspberry-pi/abbildung-6/16365-1-ger-DE/Abbildung-6_large.png)

> _Abbildung 6: Die Darstellung der Telemetriedaten im Webbrowser._

Das Laden der Messwerte aus der Datenbank ubernimmt ein per Ajax in Abstanden von drei Sekunden aufgerufenes PHP-Skript, das die Daten in Form einer JSON-Datei ubergibt. Eine etwas gekurzte Version dieses Skripts zeigt [Listing 9](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/6). Wie Sie dort sehen, ubergibt der Code bei jedem Aufruf des Skripts die letzte bereits empfangene ID (`$maxID`), um nur die neuen Daten abzufragen.

Listing 9
    
    
    <?php
    $maxID = $_GET["maxID"];
    $mysqlhost="localhost";
    $mysqluser="user";
    $mysqlpwd="****";
    $mysqldb="jr_data";
    $connection=mysql_connect($mysqlhost, $mysqluser, $mysqlpwd);
    mysql_select_db($mysqldb, $connection);
    $sql="SELECT * FROM candata WHERE ID > ".$maxID;
    $result = mysql_query($sql);
    $cnt = 0;
    while ($row = mysql_fetch_object($result)) {
      $ID[$cnt] = $row->ID;
      $TIMEST[$cnt] = $row->TIMESTAMP;
      $FUELTEMP[$cnt] = hexdec($row->FUELTEMP);
      $WATERTEMP[$cnt] = hexdec($row->WATERTEMP);
      $OILPRESSURE[$cnt] = hexdec($row->OILPRESSURE);
      $OILTEMP[$cnt] = hexdec($row->OILTEMP);
      $cnt++;
    }
    $result = array(
      "NEWid" => $ID,
      "NEWtime" => $TIMEST,
      "NEWfueltemp" => $FUELTEMP,
      "NEWwatertemp" => $WATERTEMP,
      "NEWoilpressure" => $OILPRESSURE,
      "NEWoiltemp" => $OILTEMP
    );
    print(trim(json_encode($result)));
    ?>

Als Ergebnis erscheinen die aktuellen Daten mit drei bis funf Sekunden Verzogerung auf der Webseite. Dabei bietet jqPlot sehr umfangreiche Moglichkeiten - ein sehr einfaches Beispiel fur das Darstellen eines Javascript-Arrays zeigen [Listing 10](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/6) und [Abbildung 7](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/6).

Listing 10
    
    
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
              "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
      <title>Öltemperatur-Plot</title>
      <script type="text/javascript" src="jquery.min.js"></script>
      <script type="text/javascript" src="jquery.jqplot.min.js"></script>
      <link rel="stylesheet" type="text/css" href="jquery.jqplot.css" />
    </head>
    <body>
    <div id="chartdiv" style="height:200px;width:500px; "></div>
    <script type="text/javascript">
      var oeltemperatur = new Array(50,53,55,50,52,60,60,50,53,50);
      $.jqplot('chartdiv', [oeltemperatur], {
        axes:{
          xaxis:{
            label:'Zeit'
          },
          yaxis:{
            label:'Öltemperatur'
          }
        }
      });
    </script>
    </body>
    </html>

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2014/02/fahrzeugdaten-uebertragen-mit-dem-raspberry-pi/abbildung-7/16368-1-ger-DE/Abbildung-7_large.png)

> _Abbildung 7: Ein einfacher Plot der Daten aus einem Javascript-Array mittels jqPlot._

#### Erweiterungen

Neben dem Auslesen und Auswerten von Fahrzeugdaten uber den CAN-Bus ubernimmt der RasPi im Rennwagen noch weitere Aufgaben: So bindet er beispielsweise eine WLAN-fahige, im Fahrzeug montierte Action-Cam ans Internet an (Details siehe [Kasten "Live-Video"](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/6)). Damit kann das Boxen-Team das Rennen auch aus der Sicht des Fahrers live mitverfolgen.

Fur eine (minimale) Feedback-Funktion ins Cockpit steuert der RasPi via GPIO LEDs an, die dem Fahrer Zustande wie "System einsatzbereit" und Ähnliches signalisieren. Um die gefahrene Strecke sowie die aktuelle Position des Rennfahrzeuges auf dem Kurs in eine Karte einzuzeichnen, liefert ein am RasPi via USB angeschlossenes GPS-Modul die Positionsdaten. Auch diese landen wie die Sensorwerte von CAN-Bus in der Datenbank und werden dann via Google Maps auf der Webseite dargestellt.

Fur die Live-Video-Funktion kommt eine WLAN-fahige Action-Cam zum Einsatz, mit welcher der RasPi via WLAN-Stick kommuniziert, um den Verkabelungsaufwand im Fahrzeug zu senken. Damit das Boxenteam von extern (uber den UMTS-Stick) auf das "interne" Netz zugreifen kann, ließe sich beispielsweise mit Iptables ein Port-Forwarding auf die Kamera einrichten.

Da aber sowieso bereits der Webserver Apache lauft, wurde hier einfach ein [Reverse-Proxy](http://www.raspberry-pi-geek.de/Magazin/2014/02/Fahrzeugdaten-uebertragen-mit-dem-Raspberry-Pi/\(offset\)/8) eingerichtet: Apache leitet alle Anfragen an eine bestimmte URL an die Webcam weiter. Dazu aktivieren Sie das Apache-Proxy-Modul mit folgender Konfiguration:
    
    
    ProxyPass /live/ http://10.5.5.9:8080/live/
    ProxyPassReverse /live/ http://10.5.5.9:8080/live/

Damit leiten Sie Anfragen an die UMTS-Webadresse des RasPi an die interne URL der Kamera (im Beispiel `http://10.5.5.9:8080/live/`) um. Auf ahnlichem Weg lasst sich auch eine Authentifizierung per Username und Passwort einrichten, falls die Webcam das nicht unterstutzt.

  


#### Erster Einsatz

Diese Telemetrielosung wurde im Rahmen einer Diplomarbeit von Helmut Hammerschmied im Studiengang Fahrzeugtechnik an der FH Joanneum GmbH entwickelt. Sie ist im Rennfahrzeug _jr13-evo_ verbaut und wird beim Formula-Student-Wettbewerb in Detroit im Mai 2014 ihren ersten "scharfen" Renneinsatz absolvieren.

CAN-Bus

    

CAN steht fur Control Area Network. Dieses serielle Bussystem entwickelte Bosch 1983 fur die Vernetzung von Steuergeraten in Automobilen. Inzwischen hat sich CAN zum ISO-Standard entwickelt.

DynDNS

    

Eine Technik, bei der Nameserver-Eintrage dynamisch modifiziert werden, um Rechner erreichbar zu machen, deren IP-Adresse sich haufig andert.

Ajax

    

Asynchronous Javascript and XML. Hierbei holt sich eine Webanwendung via Javascript laufend aktuelle Daten vom Server und stellt sie auf einer Webseite dar.

JSON

    

Javascript Object Notation. Ein kompaktes, textbasiertes, fur Mensch und Rechner (per `eval()`) einfach lesbares Datenaustauschformat.

Reverse-Proxy

    

Ein solcher reicht Anfragen aus dem Internet an definierte interne Server weiter. Dadurch kann er die interne Server-Infrastruktur verbergen und zudem Aufgaben wie etwa Verschlusselung oder Authentifizierung ubernehmen.

  1. Team _joanneum racing graz_: <http://www.joanneum-racing.at>
  2. RasPi-OS-Images: <http://www.raspberrypi.org/downloads>
  3. CAN-Utilities: <https://gitorious.org/linux-can/can-utils/>
  4. USB-Modeswitch: <http://www.draisberghof.de/usb_modeswitch/>
  5. SQLite-Workshop: Wolfgang Dautermann, "Schmuckstuck", LinuxUser 03/2012, S. 81, <http://www.linux-community.de/24991>
  6. Javascript-Framework jQuery: <http://www.jquery.com>

Wolfgang Dautermann arbeitet als Systemadminstrator an der FH Joanneum. Er zahlt zu den Organisatoren der Grazer Linux-Tage. Helmut Hammerschmied studiert Fahrzeugtechnik an der FH Joanneum und hat die vorgestellte Losung im Rahmen seiner Diplomarbeit entwickelt.
