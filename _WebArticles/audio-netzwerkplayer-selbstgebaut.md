# Audio-Netzwerkplayer selbstgebaut

_Captured: 2017-05-01 at 17:34 from [www.acoustic-design-magazin.de](https://www.acoustic-design-magazin.de/2016/10/21/audio-netzwerkplayer-selbstgebaut/)_

Ich bin ein Vertreter der 70er Generation, daher habe ich den Wandel der Tontrager erlebt und mitgemacht. Von den Vinyl-Scheiben in meiner Kindheit angefangen, habe ich mich als heranwachsender Teenager mit der "compact cassette" angefreundet und mit der CD als Musik-Medium lange glucklich gelebt. Und wenn ich kein Album komplett horen wollte, dann kam das Band in der Kassette zum Einsatz. Ja, genau Mix Tapes also sowas wie eine Playlist, nur mit viel mehr Liebe und Sorgfalt zusammengestellt.

Irgendwann kam die Musik im MP3 Format und plotzlich war es egal, ob MixTape 90 oder 60 Minuten dauerte oder die verflixte CD 72 Minuten Spielzeit hatte. Heute sind MP3 Dateien DAS Tontragermedium fur den digitalen Alltag, man kann es mitnehmen oder sich auf sein Gerat streamen lassen. Wer seine Musik moglichst nah am Original genießen mochte, wird ein anderes Datenformat bevorzugen, das ohne Verlust beim Komprimieren auskommt (wie z.B. FLAC).

Nun, der Haken an der Sache ist, dass die digitale Dateien-Sammlung schneller wachst als das Vinyl-Archiv oder die Silberling-Sammlung. Dazu noch die verschiedenen Formate der Musik-Dateien und neuerdings die „High Resolution Files", die alle moglichst sehr gut wiedergegeben werden sollen.

Eine Eierliegendewollmilchsau muss her, um der digitalen Musik-Flut Herr zu werden. Das dafur notwendige Stuck Technik kannst Du fertig kaufen. Doch kann es mit dem USB Stick, der externen Festplatte und dem heimischen Datei-Server oder mit gestreamten Inhalten von Windows Phone, Eifone und Android zurecht kommen? Und auch fur weniger als 100 Euro? Der audiophil veranlagte Horer verlangt dazu noch eine sehr gute Qualitat der Wandlung der digitalen Daten in analoge Signale.

### ![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Player.jpg)

> _Abbildung 1 : Netzwerkplayer (HiFiBerry) im Heimnetzwerk_

Naturlich bietet die Industrie eine recht große Anzahl von Geraten an, die sich leider immer wieder als einsame Inseln der proprietaren Technik entpuppen, um vom Hersteller nach zwei oder drei Jahren „vergessen" zu werden. Dann klappt es plotzlich nicht mehr mit der App oder das neue Musikformat wird nicht unterstutzt. Denn es gibt keine Software-Updates mehr. Damit ist das gute Stuck reif fur den Elektroschrott-Container.

Nun warum nicht mal einen audiophilen Musik-Netzwerk-Player selbst frickeln? Die Hardware kostet nicht die Welt und das Projekt bekommst Du in etwa 2 - 3 Stunden fertig. Da ist manchmal das Kleben von Lautsprecherboxen schwieriger (vor allem, wenn man die Locher selber machen muss).

**A****lso los! Hier die Anleitung fur eine HiFi Beere. **

Ähm. Stop. Ich schreibe noch ein paar Wort zur Auswahl der Komponenten. Falls es Dich nicht interessiert, dann kannst Du weiter scrollen, bis zur Anleitung. Fur die Auswahl der Komponenten fur den DIY Network-Player ist es mir wichtig, dass diese zu Mainstream gehoren. Exotische Teile haben (vielleicht) etwas, was sie besonders oder irgendwie besser macht. Doch am Ende ist es mit Ihnen wie mit den proprietaren Inseln der Industrie. Das Interesse des Entwicklers erlahmt und es wird nicht mehr gepflegt und verschwindet in dem Meer der Vergessenheit.

Eine der einfachsten und weit verbreiteten Plattformen ist Raspberry Pi. Diesen Einplatinen-Computer gibt es mittlerweile in mehreren erfolgreichen Varianten: A und B, A+ und B+, 2 und die neuste Kreation ist die 3.

![rb3](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/RB3.jpg)

> _Abbildung 2: Raspberry Pi 3, Quelle Wikipedia, Urherber Jose.gil_

Im Prinzip reichen die ersten Versionen A oder B um Musik abzuspielen. Da der Raspberry Pi 3 derzeit am einfachsten zu beschaffen ist, wird er fur den Netzwerkplayer verwendet. Naturlich braucht der kleine Computer etwas Strom, nicht viel, mit einem 5 V Steckernetzteil mit einem mikroUSB-Anschluss (wie fur viele Smartphones) kann er schon versorgt werden. Ich wahle lieber ein etwas kraftigeres Modell, dass wirklich 2A bis 3A dauerhaft liefern kann, ohne dabei heiß zu werden. Denn die Hersteller der Stecker-Netzteile haben es in der Regel nicht vorgesehen, dass das Ding in 24/ 7 Betrieb lauft. Meistens geben die Hersteller der Steckernetzteile eh nur den kurzfristig verfugbaren Spitzenstrom an. Damit ist kein stabiler Dauerbetrieb moglich. Und saubere Spannung konnen die [besseren Steckernetzteile](http://www.crazy-audio.com/2013/09/raspberry-pi-power-supply-noise-on-the-5v-rails/) auch.  
Wer seinen DAC zu klanglichen Hochstleistungen verhelfen will, der kauft ein sehr gutes Netzteil, das die Spannung exakt einhalt. Ein Beispiel dafur ist das Netzteil der Firma [Tomanek](http://tomanek.dbv.pl/viewpage.php?page_id=85). Es wurde im ADW Forum unter dem Namen „Strom" bekannt. Wer es kaufen mochte, der moge im ADW Forum [diesen Beitrag](https://www.acoustic-design-magazin.de/Lautsprecher-selber-bauen/Thema/netzteil-fuer-hifi-berry/#post-4567) lesen.

Auch wenn der Raspi spater nur uber WLAN laufen soll, fur den ersten Start muss er mit einem LAN Kabel am Netzwerk angeschlossen werden. Da jeder Computer ein Betriebssystem braucht, das auf einem Datentrager gespeichert ist, nimmt der Raspi 3 eine microSD Karte als Festplattenersatz. Das verwendete Betriebssystem beansprucht nicht viel Platz, man kommt bereits mit 4GB bestens zurecht. Da der Raspi 3 einiges an Geschwindigkeit zugelegt hat lohnt sich sogar die Investition in eine schnelle microSD Karte (Class 10). Zum Dank bootet der Raspi 3 schneller.Weil das Ziel ein gut klingender Player ist, wird noch eine Art Soundkarte benotigt. Der Kopfhorer-Ausgang eignet sich allerhochstens, um System-Sounds in schlechter Qualitat auszugeben. Die Soundkarte beim Raspi wird als DAC bezeichnet (Digital Analog Converter). Auch wenn der Raspberry Pi uber USB Ports verfugt, ist ein USB DAC nicht geeignet. Die Ursache liegt in der internen Anbindung des USB Busses. Hier kommt es ofters zu Datenstau und damit zu Aussetzern beim Abspielen.

Bei den verfugbaren DACs fur den Raspberry Pi 3 gibt es eine nahezu undurchsichtige Vielfalt, meine Wahl ist auf eine Platine aus der Schweiz gefallen. Die HiFiBerry DAC+ Platine ist einer der bekanntesten DACs und wird von fast jeder Software fur den Raspi unterstutzt. Die Platine hat Daniel Matuschek entwickelt, der bereits fruher mit seiner ausgezeichneten DIY Phono-Vorstufe fur Aufsehen sorgte.

Die DAC Platine selbst ist sehr ubersichtlich. Dennoch ist es Daniel gelungen, durch intelligente Beschaltung des DAC Bausteins, das Maximum an Klang raus zu holen. Klar gibt es bessere DACs, diese sind jedoch erheblich teurer.

### ![dac](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/DAC.jpg)

Abbildung 3: HiFiBerry DAC fur Raspberry Pi A+, B+ und 3 (Quelle: HiFiBerry)

Die HiFiBerry DAC+ Platine gibt es wahlweise mit CINCH Anschlussen, ohne Anschlusse nur mit Lotpads oder mit 3,5mm Stereo Buchse zu kaufen. Fur mich ist die Cinch Ausfuhrung am praktischsten.

**Anleitung beginnt hier**

Die benotigte Hardware:  
- Raspberry Pi 3  
- 5V Netzteil (und ggf. ein Kabel mit microUSB Stecker)  
- microSD Karte mit 4GB Kapazitat (oder mehr, Hauptsache Class 10)  
- USB WLAN Dongle (optional, wenn das eingebaute WLAN nicht ausreichen sollte. Ich nutze im Altbau ein Dongle mit guter Antenne: gibt es z.B. bei [Amazon](https://www.amazon.de/gp/product/B007H5WXB0/?ie=UTF8&camp=1638&creative=6742&linkCode=ur2&site-redirect=de&tag=wwwacousticde-21))  
- HiFiBerry DAC+

Der Aufbau der Hardware ist simpel: HifiBerry DAC+ Karte draufstecken (die beiliegenden Plastikabstandshalter nicht vergessen), LAN Kabel (und falls vorhanden WLAN Stick) einstecken. Fur das Gehause reichen ein paar LEGO Bausteine. Das Netzteil wird spater angeschlossen.

![lego](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Lego.jpg)

> _Abbildung 4: HiFiBerryDAC mir RaspberryPi in bekannten Bauklotzchen-Gehause_

Wie ein Golem einen Zauberspruch auf magischem Papier in seinem Kopf brauchte, um zu erwachen, so muss auch die Hardware durch Software belebt werden. Nun gab es fur die „Aktivierung" eines Golems eine Menge an Zauberspruchen, genauso gibt es recht viele Software-Losungen fur Netzwerkplayer. Die mehr oder weniger bekannten Namen der verschiedenen Software-Distributionen sind:

- Pi MusicBox  
- P Core Player  
- Volumio  
- Rune Audio  
- Max2Play (Kostenpflichtig)  
- Moode

Daniel Matuschek, der Entwickler der HiFiBerry Platine, hat die Treiber-Software fur Linux gebaut. Diese Treiber haben es in die „Core"-Distribution von Raspberry Pi Linux geschafft. Damit wird die HiFiBerry Platine von fast jeder Software-Distribution „Out-Of-the-Box" unterstutzt.

Ich habe mich fur „Moode Audio Player for Raspberry Pi" von [moodeaudio](http://moodeaudio.org/) entschieden. Aber wer weiß, da sich alle Software-Distributionen in permanenter Weiterentwicklung befinden, kann es in der Zukunft passieren, dass ich eine andere nehme.

Nun ein wenig Magie, damit der Netzwerkplayer zum Leben erwacht. Bitte nimm jetzt die Tastatur und Computer-Maus, offne einen Internet Browser und tippe Folgendes in die Adresszeile ein: http://moodeaudio.org/. Dann ein Klick oben auf „Download". Jetzt musst Du die Zip-Datei in ein Verzeichnis deiner Wahl entpacken.

Als nachstes brauchst Du noch ein Werkzeug um Moode Player auf die microSD Karte zu installieren, denn ein einfaches Kopieren hilft hier nicht. Die entpackte Datei ist ein Foto von den Daten der SD-Karte - nein, naturlich nicht! Es ist eine bitgenaue Abbildung der Daten auf der SD Karte. Damit die einzelnen Bits exakt an der vorgesehen Stelle wieder landen, wird ein Programm benotigt, der die Bits fein sauberlich an die richtigen Stellen kopiert. Das Programm ist „Win32 Disk Imager". Das Tool kannst Du am besten auf sourceforge.net herunterladen, dort ist immer die neueste Version zu haben. Dieses Programm muss nicht installiert werden, es reicht, es in ein Verzeichnis zu entpacken.

Die nachsten Schritte sind auch von einem Computer-Legastheniker zu bewerkstelligen. Als erstes steckst Du die MicroSD-Karte in einen passenden Slot (ggf. Adapter benutzen) am Computer. Den Dialog von Explorer/ Windows kannst Du schließen. Jetzt startest Du das Programm „Win32DiskImager.exe" und klickst auf das Blaue-Symbol neben dem leeren Feld (unter „Image File"). Ein Datei-Auswahl-Fenster wird geoffnet und Du wahlst die zuvor entpackte Moode-Datei.

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/DiskImager.jpg)

Als nachstes wahlst Du unter „Device" die SD-Karte aus. ACHTUNG! Prufe nochmal im Explorer, ob du den richtigen Laufwerksbuchstaben ausgewahlt hast, bevor Du auf den Knopf „Write" klickst!

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/DiskImager_2.jpg)

Beim Schreiben der Daten wird auf dem ausgewahlten Laufwerk ALLES uberschrieben. Die gleiche Frage, wird Dir auch „Win32 DiskImager" stellen. Nachdem die Daten erfolgreich auf die microSD-Karte geschrieben worden sind, kannst Du erstmal im Windows unten rechts, den Punkt „Hardware sicher entfernen" ausfuhren, bevor Du die Karte rausnimmst.

Hier die Zusammenfassung der benotigten Software und Tools:

- Moode Image Datei  
- Win32 DiskImager

Jetzt bitte den Erweckungs-Zauber, nee, die beschriebene microSD Karte in Raspberry Pi mit HiFiBerry DAC einstecken. Vergiss bitte nicht, den Rasberry Pi 3 mit einem LAN Kabel mit deinem Router zu verbinden. Nun darfst Du die Stromversorgung anschließen und dem Blinken der LED's auf dem Raspberry Pi eine Weile zusehen. Nach ein paar Minuten gehst Du zu deinem Rechner und offnest einen Internet-Browser deiner Wahl (Internet Explorer, Chrome oder Firefox oder …)

Die Browser haben oben ein Adressfeld. In diese Adresszeile tippst Du "http://moode" ein. WICHTIG! Hinter moode darf nichts stehen (weder ein „.org" noch was anderes)   
Jetzt druckst Du auf „Enter". Wenn alles geklappt hat offnet sich diese Seite:

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_1.jpg)

Falls es nicht auf Anhieb geklappt hat, nicht verzagen. Oft klappt die Namensauflosung nicht richtig. In diesem Fall musst Du die IP Adresse von deinem Moode-Player auf deinem Router (SpeedPort, Easybox, Fritzbox usw.) nachschlagen. Dann gibst Du statt "http://moode" z.B. "http://192.168.200.212" ein (Beispiel aus meinem Heimnetzwerk, dein Moode Audio Player hat eine andere IP-Adresse!).

Bevor Du Musik horen kannst (Cinch-Kabel schon angeschlossen?), musst Du noch ein wenig Konfigurationsarbeit leisten. Aber auch das ist sehr einfach! Oben, in der rechten Ecke ist der Knopf fur das Menu. Wenn Du drauf klickst, erscheint Du diese Auswahl:

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_2.jpg)

Mein erster Schritt ist der Punkt „Configure". Dann zeigt sich diese Auswahl:

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_2_a.jpg)

Der erste Schritt ist der Klick auf „System". Hier stellst Du ein, dass der HiFiBerry DAC+ die verwendete Soundkarte ist. Einfach aus der Liste den HiFiBerryDAC auswahlen. Nebenbei kannst Du die Zeitzone und den Namen fur den Player setzen. Immer schon einzeln, denn der „SET" Knopf gilt immer nur fur EIN Eingabefeld.

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_4.jpg)

Das ALSA Volumen kannst Du auf 100 setzen, wenn Du einen HiFiBerryDac+ hast. Ansonsten lass es auf dem voreingestellten Wert stehen. Die Steuerung der Lautstarke erfolgt per Software. Den Unterschied zwischen Software- und Hardware-Steuerung kannst Du [hier](http://www.crazy-audio.com/2014/01/hardware-vs-software-volume-control/) nachlesen.

Danach scrollst Du im Fenster einige Eintrage weiter runter. Dort kannst Du unter dem Begriff „Services" einstellen, ob der Moode Player Empfanger fur Airplay oder UPnP ist (Ob „und" geht, habe ich nicht probieren konnen. Hier kannst Du selbst experimentieren). Damit kannst Du von deinem Smartphone im gleichen WLAN/LAN Musik auf den Moode Player streamen. Mit einem Apple iPhone 6 hat das Airplay bei mir ohne Probleme funktioniert. Den Namen fur deinen Moode Airplay kannst Du selbstverstandlich selbst wahlen. Als nutzlich hat sich erwiesen „Airplay metadata" einzuschalten. Dann wird (sofern im Stream vorhanden) das Cover im Moode Player angezeigt.

Wenn Du ein Gerat mit Android hast, dann ist der Schalter UPnP/DLNA auf on zu stellen. Allerdings brauchst Du auf deinem mobilen Gerat noch eine passende Abspiel-App, die UPnP kann.

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_5.jpg)

Nach dem Setzen der Settings empfiehlt sich ein Neustart. Dazu in der oberen rechten Ecke die drei Balken anklicken und „Restart" auswahlen.

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_7.jpg)

Der Neustart dauert bei mir ein paar Minuten - Zeit genug, um mir einen frischen Kaffee zu gonnen. Bei der Gelegenheit schau ich auf meiner Fritzbox nach, dass das Hackchen bei „Diesem Netzwerkgerat immer die gleiche IPv4-Adresse zuweisen." gesetzt ist. Dann muss ich nicht jedes Mal nach der neuen IP Adresse suchen.

Als nachstes:

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_8.jpg)

Meine Erfahrung ist, dass es bei der Nutzung von WLAN zu Aussetzern kommen kann. Hier hilft ein großerer Daten-Buffer. Du kannst selbst experimentieren, welche Werte bei Dir am besten funktionieren.

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_9.jpg)

> _Zum Schluss nicht vergessen nach oben zu scrollen und „Apply" zu drucken._

Der nachste Punkt auf der Arbeitsliste ist die Einrichtung von WLAN (falls gewunscht und vorhanden). Das WLAN hat einen weiteren „audiophilen" Aspekt. Wie Daniel Matuschek durch [Messungen ](http://www.crazy-audio.com/2013/10/tracking-down-noise-sources-on-a-raspberry-pi/)festgestellt hat, bringt das LAN Kabel etwas Sauerei in das Ausgangssignal. Also wech damit! Im Menu den Eintrag „Network" auswahlen und wenn ein USB-WLAN Adapter eingesteckt ist, erscheint unterhalb vom „ETH0" Balken (LAN-Kabel) ein „WLAN0" Balken. Das WLAN Passwort eingeben (WPS geht hier nicht) und auf „Save Profile" klicken.

Nun hast Du auch WLAN eingerichtet. Das LAN Kabel kannst Du aber noch nicht abziehen! Das WLAN wird erst nach einem Neustart OHNE LAN-Kabel aktiv.

Wenn Du mochtest, kannst Du jetzt direkt einen USB Stick mit Musik oder eine USB-Festplatte mit eigener Stromversorgung (eigenes Netzteil) anschließen. Je nach Große der Musiksammlung dauert es eine gewisse Zeit, bis unten links die Schaltflache „Library" zur Verfugung steht. Deine Musik findest Du uber die große Schaltflache „USB storage (1)"

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_18.jpg)

Du siehst auf der rechten Seite jeder Zeile drei kurze Balken. Wenn Du darauf klickst kannst den Inhalt einer Zeile (ein Lied oder ein Ordner) zu der Playlist hinzufugen.

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_15.jpg)

Die USB Sticks fassen große Mengen Musik. Doch richtig viel Platz gibt es nach wie vor auf Festplatten. Die aktuellen Router verfugen meistens uber mindestens eine USB Buchse, oft sind es mehr. Du kannst eine USB Festplatte dann an deinem Router anschließen und auf den Inhalt uber das Heimnetzwerk zugreifen oder vielleicht hast Du eine NAS Kiste. Dann schau dir die nachsten Schritte an, um zu lernen, wie Du die Musik von NAS in den Netzwerkplayer einbinden kannst.

Im Menu oben rechts wahlst Du „Sources", dann kommst Du auf die nachfolgende Seite.   
Ich habe meine Musiksammlung in meinem Heimnetzwerk auf einer Netzwerkfestplatte abgelegt. Damit diese auch im Moode Player verfugbar wird, klicke ich Oben Rechts auf die drei waagerechte Balken und wahle „Configure" aus. Als nachstes klicke ich auf „Sources". Um ein weiteres, neues Musikverzeichnis hinzuzufugen, klickst Du bitte auf „NEW". Es wird dir ein Formular zur Einrichtung angezeigt. Fur „Source name" kannst Du irgendwas eintragen, doch ist es praktischer, wenn im Verzeichnis hauptsachlich Rock-Bands sind, den Mount z.B. „Rockiges" zu nennen. Das „Fileshare protocol" solltest Du belassen wie es ist. Unter „IP adress" tragst Du die Adresse von deinem NAS ein (wenn Du nicht weißt, welche Adresse es hat, dann musst Du das auf deinem Router nachsehen). In „Remote directory" tragst Du Netzwerkpfad zu deinem Musikverzeichnis z.B. "\\\Musiksammlung\Rock".

Wenn Du mit der Eingabe fertig bist, klickst Du bitte auf „SAVE". Jetzt musst Du nur noch warten, bis die HiFi Beere die Bibliothek erstellt hat, danach kannst Du aus deiner Sammlung was zum Abspielen auswahlen. Die Einrichtung geht schnell. Der Screenshot ist schon fast selbsterklarend.

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_11.jpg)

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_12.jpg)

![Netzwerkplayer](https://www.acoustic-design-magazin.de/wp-content/uploads/2016/10/Screenshot_17.jpg)

Die paar Stunden Zeit fur die Frickelei haben sich doch gelohnt. dein Audio-Netzwerkplayer muss sich nicht vor seinen kommerziellen Freunden verstecken. Du hast mit einem uberschaubaren Aufwand einen Player gebaut, der sicher ein langes Leben hat und nicht mit dem Erscheinen neuer Hardware-Version obsolet wird. Dein Player hat noch einen Vorteil: Wenn Dir das Bedienungskonzept oder Farben nicht mehr gefallen, eine zweite microSD zum Spielen kostet fast nix und es gibt noch andere Software… (Die erste legst Du zur Seite, falls das Experiment mit neuer/anderer Software scheitern sollte, kannst Du quasi mit einem Handgriff auf das vorherige, lauffahige System wechseln)

Peter Gawrych  
aka Rincewind
