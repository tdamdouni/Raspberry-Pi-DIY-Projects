# Raspberry Pi als Desktop und Netbook nutzen 

_Captured: 2016-11-07 at 11:07 from [www.tecchannel.de](http://www.tecchannel.de/a/raspberry-pi-als-desktop-und-netbook-nutzen,2068194)_

Dank seiner HDMI-Schnittstelle ist der Raspberry Pi schnell mit externen Displays wie TV-Geraten und Monitoren verbunden. Mit dem richtigen Betriebssystem und etwas Zubehor eignet sich der pfiffige kleine Rechner durchaus als genugsames Arbeitstier.

## 1\. Die Liste der notwendigen Zutaten

Fur die Nutzung des Raspberry als Desktop-Ersatz oder Mobilrechner mussen Sie sich einige Bauteile beschaffen. Neben dem Ein-Platinen-Computer und einer ausreichend dimensionierten SD-Karte (16 GB sind eine annehmbare Große) sollte ein Netzteil mit Mikro-USB-Anschluss angeschafft werden. Außerdem empfehlenswert ist der Kauf eines Gehauses. Hier haben Sie im Handel die Wahl zwischen verschiedenen Modellen, die um die 10 Euro kosten. Sie erleichtern den Transport und schutzen den Rechner auch unterwegs vor Staub und anderen schadlichen Einflussen.

Obligatorisch ist der Kauf eines HDMI- und Ethernet-Kabels. Per HDMI verbinden Sie den Raspberry schnell unterwegs mit allen moglichen externen Anzeigegeraten, und per Ethernet klappt der Internetzugang, sofern kein WLAN zur Verfugung steht. Um Ihre Optionen zu vergroßern, kann sich die Anschaffung eines Kabels lohnen, das HDMI mit DVI verbindet. Damit schaffen Sie auch die Verbindung zu etwas alteren Monitoren. Auch die neuesten Revisionen des Raspberry kommen derzeit noch ohne ein WLAN-Modul aus. Wenn Sie unterwegs per Funknetzwerk auf das Internet zugreifen wollen, schaffen Sie sich am besten einen passenden WLAN-Stick fur die USB-Schnittstelle an. Maus und Tastatur erlauben die komfortable Eingabe - es sei denn, Sie gehoren zu den Bastlernaturen: Dann probieren Sie den Einsatz einer Docking-Station (siehe Kasten: „Fur Ambitionierte: Raspberry als Notebook").

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

## 2\. Das Betriebssystem Raspbian installieren

Es gibt unterschiedliche Wege zum funktionierenden Betriebssystem fur den Raspberry. Sie brauchen auf jeden Fall einen „richtigen" Computer mit einer Leseeinheit fur SD-Karten oder ein externes Modell. Besuchen Sie dann die offizielle Seite des Raspberry-Projekts, und suchen Sie unter „Downloads" nach der aktuellen Version der „New Out Of Box Software" (Noobs). Dabei handelt es sich um ein ZIP-Archiv in der immerhin stattlichen Große von 1,2 GB. Laden Sie die Datei auf Ihren Rechner herunter.

![Raspbian-Installation: Das Setup informiert unter anderem über Standard-User und Standardkennwort.](http://images.cio.de/images/computerwoche/bdb/2524729/840x473.jpg)

> _Raspbian-Installation: Das Setup informiert unter anderem uber Standard-User und Standardkennwort._

Formatieren Sie dann unter Linux die SD-Karte. Stecken Sie die SD-Karte ein, und starten Sie das Partitionierungswerkzeug Gparted. Unter den erkannten Laufwerken sollte die Karte auftauchen. Um darauf arbeiten zu konnen, mussen Sie die Partitionen auf der Karte „aushangen". Dazu genugen in Gparted ein Rechtsklick auf die einzelnen Bereiche und die Wahl des gleichnamigen Befehls aus dem Kontextmenu. Erst wenn die Bereiche ausgehangt wurden, loschen Sie die Datenbereiche auf der Karte. Arbeiten Sie vorsichtig, denn nach dem Loschen sind die Daten unwiederbringlich verloren. Am oberen Rand des Bildschirms sollte sich mit jedem erfolgreichen Loschvorgang der freie Speicherplatz vergroßern.

![Nachinstallieren wie gewohnt: Das Debian-basierte System Raspian nutzt die Debian-Paketquellen. Mit apt-get install holen Sie sich die gewünschte Software.](http://images.cio.de/images/computerwoche/bdb/2524730/840x473.jpg)

> _Nachinstallieren wie gewohnt: Das Debian-basierte System Raspian nutzt die Debian-Paketquellen. Mit apt-get install holen Sie sich die gewunschte Software._

Ist die Karte komplett leer, klicken Sie auf den freien Speicherplatz und entscheiden sich im Kontextmenu fur „Neu". Der nachfolgende Dialog ist selbsterklarend. Sie geben die gewunschte Große der Partition an, wahlen als Dateisystem FAT32 und vergeben optional eine Bezeichnung. Hat Gparted seine Arbeit erfolgreich verrichtet, entpacken Sie den Inhalt des heruntergeladenen Archivs auf die Karte. Achten Sie darauf, dass alle Dateien kopiert werden und dabei auch die Ordnerstruktur erhalten bleibt.

Damit ist die Vorbereitung abgeschlossen. Verbinden Sie jetzt die Peripherie mit dem Raspberry. Legen Sie die Speicherkarte ein, und verbinden Sie das Netzteil. Damit starten Sie das initiale Setup. Aus den angebotenen Optionen entscheiden Sie sich fur „Raspian" als Betriebssystem. Es bietet die meisten Moglichkeiten fur den Desktop- und Notebook-Einsatz. Jetzt startet die eigentliche Einrichtung.

  


Im ersten Setup des Gerats sollten Sie auf jeden Fall in den Optionen „Change User Password" auswahlen, um fur den Standard-Nutzer „pi" ein individuelles Kennwort zu vergeben. Rufen Sie außerdem „Advanced" auf. Auf der nachfolgenden Bildschirmseite entscheiden Sie sich fur „Memory Split". Über diese Option legen Sie fest, wie viel des eingebauten Speichers fur die Grafikeinheit reserviert werden soll. Wenn Sie den Raspberry nur fur Office-Aufgaben und das Surfen im Internet einsetzen wollen, konnen Sie den Wert von den vordefinierten 64 MB ruhig auf 32 MB heruntersetzen. Fatal falsch machen konnen Sie hier nichts, denn diese Werte lassen sich spater jederzeit mit dem Aufruf der Software raspi-config wieder korrigieren.

Haben Sie die Änderungen erledigt, starten Sie den Rechner neu. Nach dem Booten werden Sie vom Prompt begrußt. Hier loggen Sie sich als Benutzer pi mit dem gerade von Ihnen vergebenen Passwort ein. Wenn Sie keine Änderungen vorgenommen haben, lautet das Standardpasswort „raspberry". Um wie am heimischen Rechner Ihre Buroaufgaben erledigen zu konnen, starten Sie mit dem Befehl _startx_die grafische Oberflache.

## 4\. Bessere Software nachinstallieren

Die Oberflache wirkt fur Gnome- oder KDE-Anwender auf den ersten Blick kuhl und spartanisch, unterscheidet sich aber funktional und in der Bedienung kaum von den deutlich mehr Ressourcen verbrauchenden grafischen Aufsatzen. Die mitgelieferte Software ist indes unpraktisch. Da es sich um ein vollwertiges Debian-System handelt, konnen Sie sich aber viele Programme nachtraglich beschaffen, die fur den Office-Alltag besser geeignet sind.

![Neben den Software-Quellen von Debian können Sie auch den Pi-Store nutzen. Dort finden Sie unter anderem eine speziell angepasste Version von Libre Office.](http://images.cio.de/images/computerwoche/bdb/2524731/840x473.jpg)

> _Neben den Software-Quellen von Debian konnen Sie auch den Pi-Store nutzen. Dort finden Sie unter anderem eine speziell angepasste Version von Libre Office._

Beginnen Sie am besten damit, den Internet-Browser auszutauschen. Vorinstalliert ist Midori - ein etwas sperriger Browser, zudem langsam und ungewohnt in der Bedienung. Greifen Sie also besser zu einer schnelleren und bewahrten Alternative. Klicken Sie doppelt auf den Eintrag „LXTerminal", der sich auf dem Desktop befindet. Dort installieren Sie einen flotten Browser - etwa:

sudo apt-get install chromium

Das System fragt Sie, ob Sie die Installation durchfuhren wollen und wie viel Speicherplatz notwendig sein wird. Bestatigen Sie die Nachfrage.

![Beim Zugriff auf moderne Internetseiten wird viel Javascript genutzt. Schalten Sie dies am besten im Browser ab, und nutzen Sie statt Webmail-Clients.](http://images.cio.de/images/computerwoche/bdb/2524732/840x473.jpg)

> _Beim Zugriff auf moderne Internetseiten wird viel Javascript genutzt. Schalten Sie dies am besten im Browser ab, und nutzen Sie statt Webmail-Clients._

Wenn Sie wollen, richten Sie sich auf dem Raspberry eine vollstandige Office-Suite ein. Am Desktop finden Sie das Icon „PI Store" bemerkt. Wie Sie dies von anderen Systemen kennen, bietet der Raspberry auch einen Software-Store an, aus dem Sie speziell angepasste Programmversionen installieren konnen. Wechseln Sie im Store in den Abschnitt „Apps", und wahlen Sie auf der linken Seite des Fensters „Productivity" aus. In der Mitte finden Sie dann den Eintrag „LibreOffice". Der Download und die Installation sind kostenlos. Allerdings mussen Sie sich fur den Shop registrieren. Dazu genugen aber die Angabe einer gultigen Mailadresse und eines Passworts. Download und Installation benotigen eine Weile. Ist die Einrichtung abgeschlossen, nistet sich die Software im Startmenu unter „Buro" ein.

Wenn Sie langer mit dem Raspberry arbeiten, werden Sie bemerken, dass es verhaltnismaßig unpraktisch ist, mit dem Gerat Webmail-Dienste zu nutzen. Google Mail oder auch Outlook.com setzen stark auf den Einsatz von Ajax (also einer gehorigen Portion Javascript), um eine Desktop-Bedienung zu simulieren. Dies ist allerdings nicht sonderlich ressourcenschonend. Verwenden Sie daher besser klassische Mail-Clients fur das System, zum Beispiel Claws-Mail oder Icedove. Beide konnen Sie ebenfalls ganz einfach uber die Kommandozeile installieren:

sudo apt-get install claws-mail  
sudo apt-get install icedove

Zur Anpassung des Debian-Systems an die Architektur steht Ihnen ein breites Spektrum an Programmen offen. Allerdings durfen Sie hier auch nicht zu viel erwarten. Nicht jedes Programm, das unter Ubuntu oder Debian lauft, funktioniert hier problemlos. Die reibungslose Installation muss also nicht notwendigerweise dazu fuhren, dass die Anwendung auch stabil lauft.

  


Noch mobiler wird Ihr kleiner Rechner durch den Einsatz eines WLAN-Adapters. Der Raspberry selbst bietet nur einen Ethernet-Port. Es gibt aber zahlreiche externe WLAN-Adapter fur die USB-Schnittstelle. Besonders zu empfehlen sind fur den Kleinstrechner die Adapter des Herstellers Edimax. Diese basieren auf einem Chipsatz von Realtek, fur den im Kernel des Systems bereits ein Treiber hinterlegt ist. Das macht die Einrichtung auch fur Einsteiger unkompliziert. Da der Raspberry nur zwei USB-Ports besitzt, mussen Sie einen zusatzlichen USB-Hub erwerben, um Maus, Tastatur und WLAN-Adapter parallel betreiben konnen.

![Wenn Sie einen Chipsatz verwenden, dessen Treiber im Kernel vorliegt, ist die Einrichtung von WLAN unkompliziert. Das Tool Wifi Config hilft dabei.](http://images.cio.de/images/computerwoche/bdb/2524733/840x473.jpg)

> _Wenn Sie einen Chipsatz verwenden, dessen Treiber im Kernel vorliegt, ist die Einrichtung von WLAN unkompliziert. Das Tool Wifi Config hilft dabei._

Um WLAN nutzen zu konnen, muss das System die angeschlossene Hardware erkennen. Schließen Sie also den Dongle an eine freie USB-Schnittstelle an. Der Raspberry wird in diesem Moment automatisch neu starten. Nachdem Sie sich dann wieder am System angemeldet haben, offnen Sie ein Terminal. Geben Sie dort den Befehl _dmesg_ein. Sie erhalten eine Liste der an die USB-Schnittstellen angeschlossenen Gerate. Suchen Sie dort nach einem Eintrag „WLAN-Adapter". Der signalisiert, dass das Betriebssystem die Moglichkeiten des Gerats korrekt erkennt. Wenn der Treiber korrekt genutzt wird, sollte das System eine Netzwerkschnittstelle eingerichtet haben. Geben Sie dann im Terminal _ifconfig_ein. Wenn dort ein Eintrag wie „wlan0" ausgegeben wird, konnen Sie sich an die Einrichtung des Netzwerks machen.

Die grafische Oberflache enthalt ein Werkzeug, mit dessen Hilfe Sie WLAN-Verbindungen einrichten und konfigurieren konnen. Klicken Sie doppelt auf „Wifi Config". Im oberen Listenfeld sollte der Adapter zu finden sein, den Sie gerade im Terminal ermittelt haben. Klicken Sie auf „Scan", um ein weiteres Fenster zu offnen. Wenn Sie darin erneut auf „Scan" klicken, untersuchen Sie die Umgebung auf Netzwerke in Reichweite. Das funktioniert nur bei Funknetzwerken, die so konfiguriert sind, dass sie ihre Kennung ausstrahlen und damit sichtbar sind. Mit einem Doppelklick auf einen Eintrag rufen Sie sich die Maske fur die Konfiguration des Netzwerks auf. Dieser Dialog erscheint auch, wenn Sie ein Netzwerk manuell eintragen wollen. Um die Zeilen korrekt fullen zu konnen, benotigen Sie die ublichen Angaben. Dazu gehoren die Art der Verschlusselung sowie die notwendigen Schlussel. Wenn Sie die Eintrage vorgenommen haben, drucken Sie auf „Add". Danach ist die Netzwerkverbindung bekannt und wird in die Liste des Programms Wifi-Config aufgenommen. Netzwerkverbindungen, die sich nicht zu erkennen geben, erreichen Sie mittels „Add" und „Manage Networks". Spatestens mit funktionierendem WLAN haben Sie einen tollen kleinen Computer, der sich vor typischen Netbooks nicht zu verstecken braucht.

**Fazit: **Ja, es ist moglich, mit dem Raspberry Pi zu arbeiten. Schnell etwas im Internet nachschlagen oder den einen oder anderen Text zu bearbeiten, das beherrscht der kleine Computer allemal, und das zu einem unschlagbar gunstigen Preis. Leistungswunder durfen Sie von dem kleinen Rechner aber nicht erwarten.

  


Einfach den Raspberry in die Tasche stecken und an einem beliebigen Ort an einen externen Monitor anschließen: Damit haben Sie damit ein transportables und vollwertiges Linux-System, das nur wenige Gramm wiegt und variabel eingesetzt werden kann. Zu einer vollwertigen mobilen Losung gelangen Sie mit noch etwas mehr Bastelarbeit und der Investition von gut 100 Euro zusatzlich.

![Raspberry 2 Go - Die Platine mobil nutzen](http://images.cio.de/images/computerwoche/bdb/2550057/840x473.jpg)

> _Raspberry 2 Go - Die Platine mobil nutzen_

Atrix ist der Name eines auf Android basierenden Smartphones aus dem Hause Motorola, das im Jahr 2011 vorgestellt wurde, aber keine Verbreitung gefunden hat. Es ist auch nicht das Smartphone, das fur Besitzer eines Raspberry von Interesse ist, sondern ein immer noch erhaltliches Zubehorteil, das aus diesem Smartphone ein Netbook machen sollte. Diese Atrix Docking Station besteht aus einer angemessen großen Tastatur im QUERTZ-Format und einem Farbbildschirm in der Große von 11,5 Zoll. Da die Docking-Station mit einem Netzteil ausgeliefert wird, sind alle Komponenten versammelt, um den Raspberry in ein Netbook zu verwandeln. Die Stromversorgung erfolgt dann wie gewohnt per USB und auch die Verbindung mittels HDMI.

![Mobiler Rechner: Mit dem Motorola Atrix Lapdock machen Sie den Raspberry Pi mobil. Sie können das Gehäuse des Rapberry Pi – wie im Bild zu sehen – an der Rückseite des Lapdock montieren.](http://images.cio.de/images/computerwoche/bdb/2518657/840x473.jpg)

> _Mobiler Rechner: Mit dem Motorola Atrix Lapdock machen Sie den Raspberry Pi mobil. Sie konnen das Gehause des Rapberry Pi - wie im Bild zu sehen - an der Ruckseite des Lapdock montieren._

Wer kein Talent zum Loten besitzt oder sich die Fummelei sparen will, muss sich allerdings noch ein paar Adapterkabel besorgen, da eine direkte Verbindung zwischen Raspberry und Atrix nicht moglich ist, denn das Dock verwendet die jeweiligen Mikro-Formate der Steckverbindungen.

## Hilfe, Sie haben sich verbaut!

Einer der großen Vorteile des Raspberry besteht darin, dass Sie das System jederzeit mit wenig Muhe wieder in den Ausgangszustand zurucksetzen konnen. Betriebssystem und Nutzerdaten liegen gemeinsam auf der SD-Karte. Wenn Sie sich bei der Einrichtung des Systems verrannt haben, mussen Sie nur die Speicherkarte in den Originalzustand zuruckversetzen. Vorher sollten Sie aber Ihre personlichen Daten und Dokumente gesichert haben. Generell ist bei einem auch mechanisch nicht ganz unempfindlichen Gerat zu empfehlen, die personlichen Daten taglich auf ein anderes Medium zu ubertragen. Um in den Ursprungszustand zuruckzukehren, nutzen Sie unter Linux Gparted, um die Speicherkarte zu formatieren. Alternativ besorgen Sie sich unter [www.sdcard.org/downloads/formatter_4/](http://www.sdcard.org/downloads/formatter_4/) das passende Werkzeug fur Windows oder Mac. Mit den Anwendungen formatieren Sie die Karte und kopieren einfach erneut die aktuelle Version der Noobs-Software auf die Karte. Schon konnen Sie von vorn beginnen.
