# Raspberry Pi als UPnP-Server für Multimediainhalte nutzen

_Captured: 2016-11-07 at 11:08 from [www.tecchannel.de](http://www.tecchannel.de/a/raspberry-pi-als-upnp-server-fuer-multimediainhalte-nutzen,2073378)_

Multimedia-Inhalte von einem zentralen Gerat im ganzen Haus zu nutzen, ist ein verbreitetes Anliegen. Solchem Streaming von einer Server-Quelle auf alle Gerate ist der Ein-Platinen-Rechner Raspberry Pi durchaus gewachsen. Wollen Sie unserer Anleitung folgen, brauchen Sie naturlich einen [Raspberry Pi](http://www.tecchannel.de/pc_mobile/peripherie/2059184/raspberry_pi_als_mediacenter_einrichten/index.html). Sie erhalten das Gerat am einfachsten beim Online-Handler Ihres Vertrauens fur circa 35 Euro. Achten Sie unbedingt darauf, das Modell B mit 512 MByte RAM zu bestellen. Das altere A-Modell hat obendrein keinen Ethernet-Anschluss. Als Stromversorgung benotigen Sie einen [Micro-USB](http://www.tecchannel.de/pc_mobile/news/2033761/einheits_netzteil_fuer_handys_praesentiert/index.html)-Adapter.

Da der Raspberry Pi allein stehend laufen soll, kaufen Sie am besten eine Stromversorgung, die einen Netzstecker mit sich bringt (kostet etwa sieben Euro).

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

## Weitere Hard- und Software- Voraussetzungen

Fur das Aufspielen des Betriebssystems ist eine SD-Karte notwendig. Fur die beste Geschwindigkeit raten wir zu einer Class-10-Karte. Wollen Sie viele Mediendateien ubertragen, ohne ein weiteres externes Laufwerk zu verwenden, sollte die SD-Karte mindestens 32 GB fassen (ab 17 Euro).

Der Raspberry Pi (Modell B) sollte moglichst kabelgebunden am Netz arbeiten. Nur im Notfall verwenden Sie eine [WLAN](http://www.tecchannel.de/netzwerk/wlan/)-Karte, und fur diesen Fall empfehlen wir die Edimax EW-7811UN mit 150 MBit/s fur circa acht Euro. Außerdem raten wir zu einem Schutzgehause, das Sie fur weitere sieben Euro aufwarts erhalten. Rechnet man alles inklusive WLAN-Karte zusammen, kommen Sie auf rund 75 Euro. Das Betriebssystem ist kostenlos.

![Noobs macht es sehr einfach, Betriebssysteme parallel für den Raspberry Pi zu installieren. Noobs hat auch die Medienzentralen Open Elec und Rasp BMC in seinem Portfolio.](http://images.cio.de/images/computerwoche/bdb/2531009/840x473.jpg)

> _Noobs macht es sehr einfach, Betriebssysteme parallel fur den Raspberry Pi zu installieren. Noobs hat auch die Medienzentralen Open Elec und Rasp BMC in seinem Portfolio._

Vorubergehend - fur die Einrichtung des Systems - brauchen Sie außerdem Bildschirm, Maus und Tastatur. Der Raspberry Pi ist mit einem [HDMI-Ausgang](http://www.tecchannel.de/pc_mobile/peripherie/2056720/schnittstellen_fuer_displays_im_ueberblick/index.html) bestuckt. Welches Kabel Sie benotigen, hangt vom Eingang des Bildschirms ab. Es ist auch HDMI auf DVI moglich. Ist das System dann komplett konfiguriert, konnen Sie es auch "headless", also ohne Monitor, Tastatur und Maus betreiben.

Am Ende soll ein funktionstuchtiger [UPnP-Server](http://de.wikipedia.org/wiki/Universal_Plug_and_Play) fur das Streaming herauskommen. UPnP steht fur Universal Plug & Play und ist ein weitverbreiteter Standard, den viele moderne Gerate und Software-Player verstehen (Smart-TVs, Tablets, Spielekonsolen, AV-Receiver, Windows- und Linux-Mediaplayer). Diese finden einen UPnP-Server automatisch im Netzwerk. Es kommt allerdings vor, dass Sie UPnP auf Geraten oder in der Player-Software erst explizit aktivieren mussen, so etwa beim Linux-Mediaplayer Banshee. Weiterhin lasst sich bei manchen Routern einstellen, ob UPnP aktiviert sein soll. Sollten Fehler auftreten, konnte das Problem an dieser Router-Einstellung liegen.

  


Die kompletteste Software fur einen Multimedia-Server ist bekanntlich [XBMC,](http://xbmc.org/) und fur den Raspberry Pi gibt es gleich zwei spezialisierte XBMC-Versionen: Open Elec und Rasp BMC. Beide Systeme konnen Sie, wie unten beschrieben, via Noobs installieren ("New Out Of Box Software").

Die meisten SD-Karten werden vorformatiert mit dem Dateisystem FAT32 ausgeliefert. Sollte das nicht der Fall sein, formatieren Sie die Karte entsprechend. Danach besuchen Sie die Website www.raspberrypi.org/downloads des Raspberry Pi und laden dort Noobs herunter. Das vollstandige Paket "Offline and network install" hat 1,3 GByte (die kleine Variante "NetworkInstall Only" kommt nur in Frage, wenn der Raspberry Pi bereits lauft und mit dem Internet verbunden ist). Entpacken Sie das ZIP-Verzeichnis, und kopieren Sie die entpackten Daten auf die SD-Karte.

![In den speziellen Einstellungen für Open Elec ändern Sie das Tastatur-Layout und den Systemnamen. Außerdem bestimmen Sie hier, ob sich die Distribution automatisch aktualisieren soll.](http://images.cio.de/images/computerwoche/bdb/2531010/840x473.jpg)

> _In den speziellen Einstellungen fur Open Elec andern Sie das Tastatur-Layout und den Systemnamen. Außerdem bestimmen Sie hier, ob sich die Distribution automatisch aktualisieren soll._

Nun konnen Sie die SD-Karte in den Raspberry Pi stecken und das Gerat mit Strom versorgen. Noobs initialisiert zunachst automatisch die Partition. Danach durfen Sie das System auf Deutsch umstellen. Im Anschluss stellt Ihnen [Noobs](http://www.raspberrypi.org/tag/noobs/) einige Betriebssysteme zur Auswahl, die Sie einfach per Mausklick installieren konnen. In dieser Liste befinden sich auch Rasp BMC und Open Elec. Sie konnen aus Neugierde auch beide installieren und sich spater entscheiden, welches Ihnen besser gefallt. Open Elec wirkt etwas ausgereifter und hat eine bessere Konfigurationsoberflache. Man merkt dem Projekt an, dass die Entwickler das System schon jahrelang fur x86-Systeme ausgeben. Wir haben uns daher fur Open Elec entschieden.

## Ersteinrichtung von Open Elec

Nachdem Noobs alles fur Sie konfiguriert hat, konnen Sie die [Open-Elec-Variante](http://openelec.tv/) von XBMC starten. Ein Software-Assistent hilft Ihnen bei der grundsatzlichen Einrichtung. Unter anderem wahlen Sie hier die Systemsprache und den Namen fur das System. Weiterhin konnen Sie auf Wunsch gleich Netzwerkkomponenten wie Samba und SSH aktivieren. Fur das Ausliefern von Medien via UPnP ist es allerdings nur erforderlich, die Netzwerkschnittstelle zu bestimmen (Ethernet oder WLAN).

![Unter XBMC können Sie UPnP und somit den maßgeblichen Streaming-Dienst mit einem Mausklick aktivieren.](http://images.cio.de/images/computerwoche/bdb/2531011/840x473.jpg)

> _Unter XBMC konnen Sie UPnP und somit den maßgeblichen Streaming-Dienst mit einem Mausklick aktivieren._

Die hier eingestellte Erstkonfiguration lasst sich spater jederzeit wieder andern. Die Distribution bietet dafur unter "_System_" die Registerkarte "_OpenELEC_". Klicken Sie darauf, offnet sich ein Dialog mit einer weiteren Registerkarte "_System_". Diese sollten Sie in jedem Fall aufsuchen, um die "_Tastaturbelegung_" auf Deutsch ("de") einzustellen. An dieser Stelle durfen Sie auch vorgeben, ob sich Open Elec automatisch aktualisieren durch Updates soll.

  


Wie bereits erwahnt, bringt XBMC den UPnP-Server mit. Sie aktivieren die Funktion, indem Sie auf "_System -> Einstellungen -> Dienste_" klicken. Im nun offnenden Dialog finden Sie die Registerkarte "_UPnP_". Klicken Sie hier auf "_UPnP-Server aktivieren_". Zu empfehlen ist ferner das Einschalten der zweiten Option "_Veroffentliche Bibliothek-Aktualisierungen uber UPnP_". Sollte sich an der Multimedia-Bibliothek etwas andern, informiert dann das Mediencenter des Raspberry Pi sofort die UPnP-verbundenen Gerate.

![Medien übertragen: Um Dateien auf den Raspberry Pi und das XBMC zu kopieren, nutzen Sie am besten den eingebauten Dateimanager. Sie erledigen das hier einfach per Rechtsklick.](http://images.cio.de/images/computerwoche/bdb/2531012/840x473.jpg)

> _Medien ubertragen: Um Dateien auf den Raspberry Pi und das XBMC zu kopieren, nutzen Sie am besten den eingebauten Dateimanager. Sie erledigen das hier einfach per Rechtsklick._

Wie sich der UPnP-Dienst im Netzwerk meldet, bestimmen Sie unter "_Einstellungen -> Dienste -> Allgemein_". Per Standard meldet sich das System als "_xbmc_". Eindeutiger ware etwa die Bezeichnung "_XBMC auf RasPi_". Starten Sie dann das System neu, um den UPnP-Dienst tatsachlich zu aktivieren. Dies erledigen Sie am XBMC-Hauptbildschirm mit dem Shutdown-Symbol links unten. Neben den Optionen "_Neustart_" und "_Herunterfahren_" gibt es hier ubrigens auch noch "_Eigener Ausschalt-Timer_".

## Dateien auf den Raspberry Pi kopieren

Sie konnen das Gerat auf verschiedene Arten mit Daten bestucken. Eine Option ist es, die SD-Karte in einen Computer zu stecken und die Daten dort zu kopieren. Haben Sie mit Noobs installiert, finden Sie die Partition "Storage" auf der Karte. Allerdings sind die Ordner gesperrt und lassen unter Linux nur mit root-Rechten ubertragen.

Eleganter ist daher die Verwendung des Netzwerks und des XBMC-eigenen Dateimanagers. Klicken Sie dazu auf "_System -> Dateimanager_". Hier konnen Sie externe Quellen genauso hinzufugen, wie im Kasten "_XBMC mit NAS verbinden_" beschrieben. Als erste Quelle wahlen Sie hier allerdings den Ordner "_Home_" aus. Dort befinden sich die Ordner "_videos_", "_music_" und so weiter. Im Anschluss fugen Sie die externe Datenquelle hinzu. Mit Hilfe der beiden Fenster konnen Sie mittels Rechtsklick die Dateien kopieren.

Da Open Elec auch [Samba](http://de.wikipedia.org/wiki/Samba_%28Software%29) und [SSH](http://www.tecchannel.de/netzwerk/wan/1782880/ssh_statt_vpn_sicher_und_kostenlos_daten_austauschen/index.html) mitbringt, konnten Sie damit ebenfalls Dateien direkt auf den Raspberry Pi verschieben. Die entsprechenden Dienste laufen nicht standardmaßig und mussen daher in den "Einstellungen" erst aktiviert werden.

  


Sie konnen nun mit jedem UPnP-fahigem Gerat uberprufen, ob der Streaming-Dienst lauft. Viele Linux-Anwender haben etwa den [VLC-Mediaplayer](http://www.vlc.de/) installiert. Haben Sie das Programm nicht, konnen Sie es kostenlos von der Projektseite herunterladen. Neuere VLC-Versionen finden UPnP-Gerate im Netzwerk und spielen davon Medien ab.

Fur einen schnellen Test ist der Mediaplayer erste Wahl: Öffnen Sie VLC, und stellen Sie sicher, dass die Wiedergabeliste angezeigt wird. Ist das nicht der Fall, klicken Sie auf "_Ansicht -> Wiedergabeliste_". Auf der linken Seite finden Sie einen Eintrag "_Lokales Netzwerk_", und ein Doppelklick darauf bringt Sie zur Option "_Universal Plug'n'Play_". Wahlen Sie diesen Punkt, zeigt der VLC alle laufenden UPnP-Server in Ihrem lokalen Netzwerk, darunter nun auch das Raspberry Pi.

## XBMC-Fernsteuerung via Android

Sind Sie im Besitz eines Android-Smartphones oder -Tablets, konnen Sie dieses als Fernbedienung fur XBMC verwenden. Wichtig dafur ist, dass Sie unter "_System -> Einstellungen -> Dienste -> Webserver_" die Option "_Steuerung uber HTTP zulassen_" aktiviert haben. Weiterhin legen Sie hier den Standard-Port fest und einen Benutzernamen und Kennwort. Standard ist "_xbmc_" ohne Kennwort.

![Das kleine Computerboard lässt sich auch ideal als Mini-UPnP-Streaming-Server einsetzen.](http://images.cio.de/images/computerwoche/bdb/2531008/840x473.jpg)

> _Das kleine Computerboard lasst sich auch ideal als Mini-UPnP-Streaming-Server einsetzen._

In Google Play finden Sie die offizielle App XBMC Remote. Eine weitere empfehlenswerte Alternative ist die [Fernsteuerungs-App Yatse](http://yatse.leetzone.org/redmine).

## XBMC mit NAS oder Server verbinden

Haben Sie nicht genug Platz auf der SD-Karte, dann konnen Sie XBMC auch mit einem eventuell vorhandenen NAS-Gerat via Samba verbinden. Zwar bieten [NAS-Gerate](http://www.tecchannel.de/storage/nas/) heute oft ihrerseits UPnP, stoßen aber bei großeren Mediensammlungen schnell an ihre Grenzen.

Im Fall von Videos funktioniert das so: Klicken Sie auf "Videos -> Dateien -> Videos hinzufugen" und im Folgedialog auf "Suchen". Hier stehen nun diverse Quellen zur Auswahl - darunter [UPnP-Devices, Windows-Netzwerk (SMB) und Netzwerk- Dateisystem (NFS)](http://www.tecchannel.de/server/linux/1741563/datenaustausch_zwischen_linux_und_windows_vista/).

Hangeln Sie sich zur gewunschten Quelle durch, und verknupfen Sie diese mit XBMC. Das System fragt nach Anmeldenamen und Passwort, sollte das notwendig sein.

Diese hinzugefugte Videoquelle bietet den Raspberry Pi mit Open Elec nun auch via UPnP an. Sie nehmen den Raspberry Pi sozusagen als Vermittler zwischen [NAS](http://www.tecchannel.de/pc_mobile/peripherie/2057273/workshop_mikrocomputer_raspberry_pi_als_nas_einsetzen/index.html) oder einer anderen [Netzwerkfreigabe](http://www.tecchannel.de/pc_mobile/peripherie/2067920/raspberry_pi_ueberwacht_datenverkehr_im_netzwerk/index.html) und dem entsprechenden UPnP-Client. Sie durfen an dieser Stelle naturlich so viele Quellen hinzufugen, wie Sie mochten. Mit Musik funktioniert das analog. (hal)

_Dieser Artikel basiert auf einem Beitrag unserer Schwesterpublikation [PC-Welt](http://www.pcwelt.de/ratgeber/Raspberry_Pi_als_UPnP-Server_nutzen-Hardware___Netzwerk-8832590.html)._
