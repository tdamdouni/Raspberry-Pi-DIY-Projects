# Musikstreamer mit Hifiberry selbst gebaut

_Captured: 2017-05-01 at 17:25 from [www.lautsprecherbau.de](https://www.lautsprecherbau.de/Magazine/Lautsprecherbau-Magazin-2015/September-2015/_Musikstreamer-mit-Hifiberry-selbst-gebaut_8636,de,901226,12897)_

![Musikstreamer mit Hifiberry selbst gebaut](https://www.lautsprecherbau.de/design/stories/Artikel/2015/September2015/Hifiberry/362-hifiberry_raspberry_pi_bild_36.jpg)

# HiFi-Beere selbstgebaut

Ich bin ein Vertreter der 70er Generation, daher habe ich den Wandel der Tontrager erlebt und mitgemacht. Von den Vinyl-Scheiben in meiner Kindheit angefangen, habe ich mich als heranwachsender Teenager mit der "compact cassette" angefreundet und mit der CD als das Musik-Medium lange glucklich gelebt. Und wenn ich kein Album komplett horen wollte, dann kam das Band in der Kassette zum Einsatz. Ja, genau Mix Tapes also sowas wie eine Playlist, nur mit viel mehr Liebe und Sorgfalt zusammengestellt.

Irgendwann kam die Musik im MP3 Format und plotzlich war es egal, ob MixTape 90 oder 60 Minuten dauerte oder die verflixte CD 72 Minuten Spielzeit hatte…

Heute sind MP3 Dateien DAS Tontragermedium fur den digitalen Alltag, man kann es mitnehmen oder sich auf sein Gerat streamen lassen. Wer seine Musik moglichst nah am Original genießen mochte, wird ein anderes Datenformat bevorzugen, das ohne Verlust beim Komprimieren auskommt (wie z.B. FLAC).

Nun, der Haken an der Sache ist, dass die digitale Dateien-Sammlung schneller wachst als das Vinyl-Archiv oder die Silberling-Sammlung. Dazu noch die verschiedenen Formate der Musik-Dateien und neuerdings die „High Resolution Files", die alle moglichst sehr gut wiedergegeben werden sollen.

Eine Eierliegende Wollmilchsau muss her, um der digitalen Musik-Flut Herr zu werden. Das dafur notwendige Stuck Technik kannst Du fertig kaufen. Doch kann es mit dem USB Stick, der externen Festplatte und dem heimischen Datei-Server oder mit gestreamten Inhalten von Windows Phone, Eifone und Android zurecht kommen? Und auch fur weniger als 100 Euro? Der audiophil veranlagte Horer verlangt dazu noch eine sehr gute Qualitat der Wandlung der digitalen Daten in analoge Signale.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_35.jpg)

Abbildung 1 : Netzwerkplayer (HiFiBerry) im Heimnetzwerk

Naturlich bietet die Industrie eine recht große Anzahl von Geraten an, die sich leider immer wieder als einsame Inseln der proprietaren Technik entpuppen, um dann vom Hersteller nach zwei oder drei Jahren „vergessen" zu werden. Dann klappt es plotzlich nicht mehr mit der Steuerungsapp oder das neue Musikformat wird nicht unterstutzt. Denn es gibt keine Software-Updates mehr.

Nun, warum nicht einen audiophilen Musik-Netzwerk-Player mal selbst frickeln? Die Hardware kostet nicht die Welt und nach zwei oder drei Nachmittagen ist es fertig. Da ist manchmal das Kleben von Lautsprecherboxen schwieriger (vor allen wenn man die Locher selber machen muss).

**Also los! Hier die Anleitung.**

Ähm. Stop. Ich schreibe noch ein paar Wort zur Auswahl der Komponenten. Falls es Dich nicht interessiert, kannst Du bis zur Anleitung weiter scrollen.

Fur die Auswahl der Komponenten fur den DIY Network-Player ist es mir wichtig, dass diese zu Mainstream gehoren. Exotische Teile haben (vielleicht) etwas, was sie besonders oder irgendwie besser macht. Doch am Ende ist es mit Ihnen, wie mit den proprietaren Inseln der Industrie. Das Interesse des Entwicklers erlahmt und es wird nicht mehr gepflegt und verschwindet in dem Meer der Vergessenheit.

Eine der einfachsten und daher weit verbreiteten Plattformen ist Raspberry Pi. Diesen Einplatinen-Computer gibt es mittlerweile in mehreren erfolgreichen Zuchtungen, Sorten …. Ne, Varianten: A und B, A+ und B+, die neuste Kreation ist die 2

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_36.jpg)

Abbildung 2: Raspberry Pi A (Quelle Wikipedia, Urheber SparkFun Electronics)

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_37.jpg)

Abbildung 3: Raspberry Pi B, Quelle Wikipedia, Urherber Philipp Bohk

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_38.jpg)

Abbildung 4: Raspberry Pi B+, Quelle Wikipadia, Urherber Lucasbosch

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_39.jpg)

Abbildung 5: Raspberry Pi 2, Quelle Wikipedia, Urherber Multicherry

Im Prinzip reichen die ersten Versionen A oder B um Musik abzuspielen. Da der Raspberry Pi 2 derzeit am einfachsten zu beschaffen ist, wird er fur den Netzwerkplayer verwendet.

Naturlich braucht der kleine Computer etwas Strom, nicht viel, mit einem 5 V Steckernetzteil mit einem mikroUSB-Anschluss (wie fur viele Smartphones) kann es schon versorgt werden. Ich wahle lieber ein etwas kraftigeres Modell, dass wirklich 1,5A bis 2A dauerhaft liefern kann, ohne dabei heiß zu werden. Denn die Hersteller der Stecker-Netzteile haben es in der Regel nicht vorgesehen, dass das Ding in 24x7 Betrieb lauft. Meistens geben die Hersteller der Steckernetzteile eh nur den kurzfristig verfugbaren Spitzenstrom an. Damit ist kein stabiler Dauerbetrieb moglich. Und saubere Spannung konnen die besseren Steckernetzteile auch.

Der Raspi hat eine Netzwerkbuchse aber keinen WLAN Adapter an Bord. Willst Du einen Raspi am WLAN haben, musst Du einen WLAN Stick kaufen. Aber Vorsicht! Nicht jeder USB-WLAN-Stick vertragt sich mit dem Raspi. Da hilft nur eins: deine bevorzugte Suchmaschine anwerfen und nach einem WLAN Adapter suchen, der sich mit Raspberry Pi 2 vertragt. Auch wenn der Raspi spater nur uber WLAN laufen soll, fur den ersten Start muss er mit einem LAN Kabel am Netzwerk schnorcheln.

Da jederComputer ein Betriebssystem braucht, das auf einem Datentrager gespeichert ist, nimmt der Raspi 2 eine microSD Karte als Festplattenersatz. Da das verwendete Betriebssystem nicht viel Platz beansprucht, kommt man bereits mit 4GB bestens zurecht. Da der Raspi 2 einiges an Geschwindigkeit zugelegt hat (verglichen mit fruheren Modellen) lohnt sich sogar die Investition in eine schnelle microSD Karte (Class 10). Zum Dank bootet der Raspi 2 schneller.

Da das Ziel ein gut klingender Player ist, wird noch eine Art Soundkarte benotigt. Denn der Kopfhorer-Ausgang eignet sich allerhochstens um System-Sounds auszugeben (in schlechter Qualitat). Die Soundkarte beim Raspi wird als DAC bezeichnet (Digital Analog Converter). Auch wenn der Raspberry Pi uber USB Ports verfugt, ist ein USB DAC nicht geeignet. Die Ursache liegt in der internen Anbindung des USB Busses. Hier kommt es ofters zu Datenstau und damit zu Aussetzern beim Abspielen.

Da es bei den verfugbaren DACs fur den Raspberry Pi 2 eine nahezu undurchsichtige Vielfalt gibt, ist meine Wahl auf eine Platine aus der Schweiz gefallen. Die HiFiBerry DAC+ Platine ist einer der bekanntesten DACs und wird von fast jeder Software fur den Raspi unterstutzt. Die Platine hat Daniel Matuschek entwickelt, der bereits fruher mit seiner ausgezeichneten DIY Phono-Vorstufe fur Aufsehen sorgte.

Die DAC Platine selbst ist sehr ubersichtlich. Dennoch ist es Daniel gelungen, durch intelligente Beschaltung des Bausteins das Maximum an Klang raus zu holen. Klar gibt es bessere DACs, diese sind jedoch erheblich teurer.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_40.jpg)

Abbildung 6: HiFiBerry DAC fur Raspberry Pi A und B (Quelle: HiFiBerry)

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_41.jpg)

Abbildung 7: HiFiBerry DAC fur Raspberry Pi A+, B+ und 2 (Quelle: HiFiBerry)

Die HiFiBerry DAC+ Platine gibt es wahlweise mit CINCH Anschlussen, ohne Anschlusse nur mit Lotpads oder mit 3,5mm Stereo Buchse zu kaufen. Fur mich ist die Cinch Ausfuhrung am praktischsten.

Hier die Zusammenfassung der benotigten Hardware:

\- Raspberry Pi 2  
\- 5V Netzteil (und ggf. ein Kabel mit microUSB Stecker)  
\- microSD Karte mit 4GB Kapazitat (oder mehr, wird aber nicht benotigt)  
\- USB WLAN Dongle (optional)  
\- HiFiBerry DAC+

Der Aufbau der Hardware ist simpel: HifiBerry DAC+ Karte draufstecken (die beiliegenden Plastikabstandshalter nicht vergessen), LAN Kabel (und falls vorhanden WLAN Stick) einstecken. Fur das Gehause reichen ein paar LEGO Bausteine. Das Netzteil wird spater angeschlossen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_42.jpg)

Abbildung 8: HiFiBerryDAC mir RaspberryPi in bekannten Bauklotzchen-Gehause

Wie ein Golem einen Zauberspruch auf magischem Papier in seinem Kopf brauchte, um zu leben, so muss auch die Hardware durch Software belebt werden. Nun, es gab fur die „Aktivierung" eines Golems eine Menge an Zauberspruchen, genauso gibt es recht viele Software-Losungen fur Netzwerkplayer. Die mehr oder weniger bekannten Namen der verschiedenen Software-Distributionen sind:

\- Pi MusicBox  
\- P Core Player  
\- Volumio  
\- Rune Audio

Daniel Matuschek, der Entwickler der HiFiBerry Platine, hat die Treiber-Software fur Linux gebaut. Diese Treiber haben es in die „Core"-Distribution von Raspberry Pi Linux geschafft. Damit wird die HiFiBerry Platine von fast jeder Software-Distribution „Out-Of-the-Box" unterstutzt.

Ich habe mich fur RuneAudio entschieden, da mir Volumio zurzeit nicht besonders gefallt. Aber wer weiß, da sich alle Software-Distributionen in permanenter Weiterentwicklung befinden, kann es in der Zukunft passieren, dass ich eine Andere nehme.

Nun ein wenig Magie, damit der Netzwerkplayer zum Leben erwacht. Bitte nimm jetzt die Tastatur und Computer-Maus, offne einen Internet Browser und tippe folgendes in die Adresszeile ein: [http://www.runeaudio.com](http://www.runeaudio.com/) Dann ein Klick oben rechts auf „Download". Die Software fur Raspberry Pi 2 mit Klick auf „Download latest version" wird die Datei auf den heimischen Rechner ubertragen, wenn Du auf „Speichern" klickst. Die Datei wird von sourceforge.net geladen.

Leider kommt die Datei in einem Format an, mit dem Windows mit den Boardmitteln nicht weiter kommt. Hier Hilft schnell das Werkzeug „7zip" weiter. Das kleine Werkzeug ist schnell installiert.

Anschließend machst Du den Explorer auf und gehst zu der RuneAudio-Datei. Dort wahlst Du mit einem „rechts" Klick auf Runeaudio-Datei „7zip" und dann „Dateien entpacken". Mit dem neuen 7zip Fenster lasst sich die Datei in ein Verzeichnis deiner Wahl entpacken.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_43.jpg)

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_44.jpg)

Nun brauchst Du noch ein Werkzeug um Runeaudio auf die microSD Karte zu installieren, denn ein einfaches Kopieren hilft hier nicht.

Die entpackte Datei ist ein Foto von den Daten der SD-Karte - nein, naturlich nicht! Es ist eine bitgenaue Abbildung der Daten auf der SD Karte. Damit die einzelnen Bits exakt an der vorgesehen Stelle wieder landen, wird ein Programm benotigt, der die Bits fein sauberlich an die richtigen Stellen kopiert. Das Programm ist „Win32 Disk Imager". Das Tool „Win32 Disk Imager" kannst Du am besten auf sourceforge.net herunterladen, dort ist immer die neueste Version zu haben. Dieses Programm muss nicht installiert werden, es reicht, es in ein Verzeichnis zu entpacken.

Die nachsten Schritte sind auch von Computer-Legastheniker zu bewerkstelligen. Als erstes steckst Du die MicroSD-Karte in passenden Slot (ggf. Adapter benutzen) am Computer. Den Dialog von Explorer / Windows kannst Du sofort schließen.

Jetzt startest Du das Programm „Win32DiskImager.exe" und klickst Du auf das blaue Symbol neben dem leeren Feld (unter „Image File"). Ein Datei-Auswahl-Fenster wird geoffnet und Du wahlst die zuvor entpackte RuneAudio-Datei.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_45.jpg)

Als nachstes wahlst Du unter „Device" die SD-Karte aus.  
**ACHTUNG!** Prufe nochmal im Explorer, ob du den richtigen Laufwerksbuchstaben ausgewahlt hast!

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_46.jpg)

Denn bevor Du auf den Knopf „Write" klickst, solltest Du uberpruft haben, ob Du wirklich die microSD Karte ausgewahlt hast. Beim Schreiben der Daten wird auf dem ausgewahlten Laufwerk **ALLES **uberschrieben. Die gleiche Frage, wird Dir auch „Win32 DiskImager" stellen.

Nachdem die Daten erfolgreich auf die microSD-Karte ubertragen worden sind, kannst Du erstmal im Windows unten rechts, den Punkt „Hardware sicher entfernen" ausfuhren, bevor Du die Karte rausnimmst.

Hier die Zusammenfassung der benotigten Software und Tools:

\- RuneAudio Image Datei

\- 7zip

\- Win32 DiskImager

Jetzt bitte den Erweckungs-Zauber, nee, die beschriebene microSD Karte in Raspberry Pi mit HiFiBerry DAC einstecken. Vergiss bitte nicht. den Rasberry Pi 2 mit einem LAN Kabel an deinen Router anzuschließen. Nun darfst Du die Stromversorgung anschließen und dem Blinken der LED's auf dem Raspberry Pi eine Weile zusehen. Nach ein paar Minuten gehst Du zu deinem Rechner und offnest einen Internet-Browser deiner Wahl (Internet Explorer, Chrome oder Firefox oder …)

Die Browser haben oben ein Adressfeld. In diese Adresszeile tippst Du http://runeaudio ein. WICHTIG! Hinter runeaudio darf nichts stehen (weder ein „.com" noch was anderes)   
Jetzt druckst Du auf „Enter". Wenn alles geklappt hat offnet sich diese Seite:

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_47.jpg)

Falls es nicht auf Anhieb geklappt hat, nicht verzagen. Oft klappt die Namensauflosung nicht richtig. In diesem Fall musst Du die IP Adresse von deinem Runeaudio auf deinem Router (SpeedPort, Easybox, Fritzbox usw.) nachschlagen. Dann gibst Du statt http://runeaudio z.B. http://192.168.1.123 ein (Beispiel aus meinem Heimnetzwerk, dein Runeaudio hat eine andere IP-Adresse!).

Bevor Du Musik horen kannst (Cinch-Kabel schon angeschlossen?) musst Du noch ein wenig Konfigurationsarbeit leisten. Aber auch das ist sehr einfach!

Oben, in der rechten Ecke ist der Knopf fur das Menu. Wenn Du drauf klickst, bekommst Du diese Auswahl zu sehen:

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_48.jpg)

Mein erster Schritt ist der Punkt „Sources". Hier stellst Du ein, dass der HiFiBerry DAC das Ausgabemedium („Audio Output") ist. Einfach aus der Liste den HiFiBerryDAC auswahlen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_49.jpg)

Wenn Du die Lautstarke uber dein Handy/Tablet/PC steuern mochtest und einen HiFiBerryDac+ hast, dann kannst Du hier „hardware" auswahlen. Ansonsten lass es auf „disabled" stehen.

Danach scrollst Du im Fenster einige Eintrage weiter runter. Meine Erfahrung ist, dass bei der Nutzung von WLAN es zu Aussetzern kommen kann. Hier hilft ein großer Daten-Buffer. Die Werte, die ich verwende, siehst Du auf dem Screenshot.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_50.jpg)

Zum Schluss nicht vergessen, auf „Save and apply" zu drucken.

Mein nachster Schritt im Menu ist der Punkt „Settings". Hier befinden sich die wichtigen Schalter, wenn Du deine Musik auf dem Tablet oder Smartphone hast. Wenn du ein „angebissener Apfel" Smartphone hast, solltest Du den Schalter „AirPlay" auf „ON" stellen. Du kannst dann mit deinem Gerat die Musik uber die HiFi Beere abspielen.  
Wenn Du ein Gerat mit Android hast, dann ist der Schalter UPnP/DLNA auf on zu stellen. Allerdings brauchst Du auf deinem mobilen Gerat noch eine passende Abspiel-App, die UPnP kann.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_51.jpg)

Die anderen Schalter kannst Du wie auf dem Bild belassen. Zu den Spotify oder Last.fm Einstellungen kann ich nichts schreiben, da ich diese Dienste nicht benutze. Das konnen damit Erfahrene hier leicht durch passende Kommentare unter diesem Artikel erganzen.

Der nachste Punkt auf der Arbeitsliste ist die Einrichtung von WLAN (falls gewunscht und vorhanden). Das WLAN hat einen weiteren „audiophilen" Aspekt. Wie Daniel Matuschek durch Messungen festgestellt hat, bringt das LAN Kabel etwas Sauerei in das Ausgangssignal. Also wech damit! Im Menu den Eintrag „Network" auswahlen und wenn ein USB-WLAN Adapter eingesteckt ist, erscheint unterhalb von „ETH0" Balken (LAN-Kabel) ein „WLAN0" Balken.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_52.jpg)

Ein Klick auf den „WLAN0" Balken startet die Suche nach verfugbaren WLAN Netzwerken. Das kann gut eine Tasse Kaffee dauern.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_53.jpg)

Irgendwann kommt die Liste der verfugbaren WLAN Netzwerke, jetzt wahlst Du das Eigene mit einem Klick auf den Namen aus.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_54.jpg)

Das WLAN Passwort eingeben (WPS geht hier nicht) und auf „Save Profile" klicken.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_55.jpg)

Nun hast Du auch WLAN eingerichtet. Das LAN Kabel kannst Du aber noch nicht abziehen! Das WLAN wird erst nach einem Neustart OHNE LAN-Kabel aktiv.

Wenn Du mochtest, kannst Du jetzt direkt einen USB Stick mit Musik oder eine USB-Festplatte mit eigener Stromversorgung (eigenes Netzteil) anschließen. Je nach Große der der Musiksammlung dauert es eine gewisse Zeit, bis unten links die Schaltflache „Library" zur Verfugung steht. Deine Musik findest Du uber die große Schaltflache „USB storage (1)"

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_56.jpg)

Du siehst auf der rechten Seite jeder Zeile drei kurze Balken. Wenn Du darauf klickst, kannst gu den Inhalt einer Zeile (ein Lied oder einen Ordner) zu der Playlist hinzufugen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_57.jpg)

Die USB Sticks fassen große Mengen Musik. Doch richtig viel Platz gibt es nach wie vor auf Festplatten. Die aktuellen Router verfugen meistens uber mindestens eine USB Buchse oft sind es mehr. Du kannst eine USB Festplatte dann an deinem Router anschließen und auf den Inhalt uber das Heimnetzwerk zugreifen oder vielleicht hast Du eine NAS Kiste. Dann schau dir die nachsten Schritte an, um zu lernen, wie Du die Musik von NAS in den Netzwerkplayer einbinden kannst.

Im Menu oben rechts wahlst Du „Sources", dann kommst Du auf die nachfolgende Seite. Da ich schon ein paar Verzeichnisse von meinem NAS eingebunden habe , siehst Du direkt, wie ich meine Musik-Sammlung organisiert habe.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_58.jpg)

Um ein neues Musikverzeichnis hinzuzufugen, klickst Du bitte auf „ADD NEW MOUNT". Es wird dir ein Formular zur Einrichtung angezeigt. Fur „Source name" kannst Du irgendwas eintragen, doch ist es praktischer, wenn im Verzeichnis hauptsachlich Rock-Bands sind, den Mount z.B. „Rockiges" zu nennen. Das „Fileshare protocol" solltest Du belassen, wie es ist. Unter „IP adress" tragst Du die Adresse von deinem NAS ein (wenn Du nicht weißt, welche Adresse es hat, dann musst Du das auf deinem Router nachsehen).

In „Remote directory" tragst Du den Netzwerkpfad zu deinem Musikverzeichnis (z.B. MusiksammlungRock) ein  
Den Schalter „Guest access" stellst Du auf „ON" wenn Du keine Benutzer auf dem NAS eingerichtet hast und jeder in deinem Heimnetzwerk auf alle Daten zugreifen kann. Falls nicht, musst Du unter „Username" und „Password" entsprechend den richtigen Benutzer eintragen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_59.jpg)

Wenn Du mit der Eingabe fertig bist, klickst Du bitte auf „SAVE MOUNT". Jetzt musst Du nur noch warten, bis die HiFi Beere die Bibliothek erstellt hat, danach kannst Du aus deiner Sammlung was zum Abspielen auswahlen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_60.jpg)

Die paar Stunden Zeit fur die Frickelei haben sich doch gelohnt: dein Audio-Netzwerkplayer muss sich nicht vor seinen kommerziellen Freunden verstecken. Du hast mit einem uberschaubaren Aufwand einen Player gebaut, der im Laden um ein paar Faktoren teurer ist. Dein Player hat noch einem Vorteil: Wenn Dir das Bedienungskonzept oder Farben nicht mehr gefallen, eine zweite microSD zum Spielen kostet fast nix und es gibt noch andere Software…

Peter Gawrych  
aka Rincewind

  
![Musikstreamer mit Hifiberry selbst gebaut](https://www.lautsprecherbau.de/design/stories/Artikel/2015/September2015/Hifiberry/362-hifiberry_raspberry_pi_bild_36.jpg)

# HiFi-Beere selbstgebaut

Ich bin ein Vertreter der 70er Generation, daher habe ich den Wandel der Tontrager erlebt und mitgemacht. Von den Vinyl-Scheiben in meiner Kindheit angefangen, habe ich mich als heranwachsender Teenager mit der "compact cassette" angefreundet und mit der CD als das Musik-Medium lange glucklich gelebt. Und wenn ich kein Album komplett horen wollte, dann kam das Band in der Kassette zum Einsatz. Ja, genau Mix Tapes also sowas wie eine Playlist, nur mit viel mehr Liebe und Sorgfalt zusammengestellt.

Irgendwann kam die Musik im MP3 Format und plotzlich war es egal, ob MixTape 90 oder 60 Minuten dauerte oder die verflixte CD 72 Minuten Spielzeit hatte…

Heute sind MP3 Dateien DAS Tontragermedium fur den digitalen Alltag, man kann es mitnehmen oder sich auf sein Gerat streamen lassen. Wer seine Musik moglichst nah am Original genießen mochte, wird ein anderes Datenformat bevorzugen, das ohne Verlust beim Komprimieren auskommt (wie z.B. FLAC).

Nun, der Haken an der Sache ist, dass die digitale Dateien-Sammlung schneller wachst als das Vinyl-Archiv oder die Silberling-Sammlung. Dazu noch die verschiedenen Formate der Musik-Dateien und neuerdings die „High Resolution Files", die alle moglichst sehr gut wiedergegeben werden sollen.

Eine Eierliegende Wollmilchsau muss her, um der digitalen Musik-Flut Herr zu werden. Das dafur notwendige Stuck Technik kannst Du fertig kaufen. Doch kann es mit dem USB Stick, der externen Festplatte und dem heimischen Datei-Server oder mit gestreamten Inhalten von Windows Phone, Eifone und Android zurecht kommen? Und auch fur weniger als 100 Euro? Der audiophil veranlagte Horer verlangt dazu noch eine sehr gute Qualitat der Wandlung der digitalen Daten in analoge Signale.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_35.jpg)

Abbildung 1 : Netzwerkplayer (HiFiBerry) im Heimnetzwerk

Naturlich bietet die Industrie eine recht große Anzahl von Geraten an, die sich leider immer wieder als einsame Inseln der proprietaren Technik entpuppen, um dann vom Hersteller nach zwei oder drei Jahren „vergessen" zu werden. Dann klappt es plotzlich nicht mehr mit der Steuerungsapp oder das neue Musikformat wird nicht unterstutzt. Denn es gibt keine Software-Updates mehr.

Nun, warum nicht einen audiophilen Musik-Netzwerk-Player mal selbst frickeln? Die Hardware kostet nicht die Welt und nach zwei oder drei Nachmittagen ist es fertig. Da ist manchmal das Kleben von Lautsprecherboxen schwieriger (vor allen wenn man die Locher selber machen muss).

**Also los! Hier die Anleitung.**

Ähm. Stop. Ich schreibe noch ein paar Wort zur Auswahl der Komponenten. Falls es Dich nicht interessiert, kannst Du bis zur Anleitung weiter scrollen.

Fur die Auswahl der Komponenten fur den DIY Network-Player ist es mir wichtig, dass diese zu Mainstream gehoren. Exotische Teile haben (vielleicht) etwas, was sie besonders oder irgendwie besser macht. Doch am Ende ist es mit Ihnen, wie mit den proprietaren Inseln der Industrie. Das Interesse des Entwicklers erlahmt und es wird nicht mehr gepflegt und verschwindet in dem Meer der Vergessenheit.

Eine der einfachsten und daher weit verbreiteten Plattformen ist Raspberry Pi. Diesen Einplatinen-Computer gibt es mittlerweile in mehreren erfolgreichen Zuchtungen, Sorten …. Ne, Varianten: A und B, A+ und B+, die neuste Kreation ist die 2

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_36.jpg)

Abbildung 2: Raspberry Pi A (Quelle Wikipedia, Urheber SparkFun Electronics)

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_37.jpg)

Abbildung 3: Raspberry Pi B, Quelle Wikipedia, Urherber Philipp Bohk

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_38.jpg)

Abbildung 4: Raspberry Pi B+, Quelle Wikipadia, Urherber Lucasbosch

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_39.jpg)

Abbildung 5: Raspberry Pi 2, Quelle Wikipedia, Urherber Multicherry

Im Prinzip reichen die ersten Versionen A oder B um Musik abzuspielen. Da der Raspberry Pi 2 derzeit am einfachsten zu beschaffen ist, wird er fur den Netzwerkplayer verwendet.

Naturlich braucht der kleine Computer etwas Strom, nicht viel, mit einem 5 V Steckernetzteil mit einem mikroUSB-Anschluss (wie fur viele Smartphones) kann es schon versorgt werden. Ich wahle lieber ein etwas kraftigeres Modell, dass wirklich 1,5A bis 2A dauerhaft liefern kann, ohne dabei heiß zu werden. Denn die Hersteller der Stecker-Netzteile haben es in der Regel nicht vorgesehen, dass das Ding in 24x7 Betrieb lauft. Meistens geben die Hersteller der Steckernetzteile eh nur den kurzfristig verfugbaren Spitzenstrom an. Damit ist kein stabiler Dauerbetrieb moglich. Und saubere Spannung konnen die besseren Steckernetzteile auch.

Der Raspi hat eine Netzwerkbuchse aber keinen WLAN Adapter an Bord. Willst Du einen Raspi am WLAN haben, musst Du einen WLAN Stick kaufen. Aber Vorsicht! Nicht jeder USB-WLAN-Stick vertragt sich mit dem Raspi. Da hilft nur eins: deine bevorzugte Suchmaschine anwerfen und nach einem WLAN Adapter suchen, der sich mit Raspberry Pi 2 vertragt. Auch wenn der Raspi spater nur uber WLAN laufen soll, fur den ersten Start muss er mit einem LAN Kabel am Netzwerk schnorcheln.

Da jederComputer ein Betriebssystem braucht, das auf einem Datentrager gespeichert ist, nimmt der Raspi 2 eine microSD Karte als Festplattenersatz. Da das verwendete Betriebssystem nicht viel Platz beansprucht, kommt man bereits mit 4GB bestens zurecht. Da der Raspi 2 einiges an Geschwindigkeit zugelegt hat (verglichen mit fruheren Modellen) lohnt sich sogar die Investition in eine schnelle microSD Karte (Class 10). Zum Dank bootet der Raspi 2 schneller.

Da das Ziel ein gut klingender Player ist, wird noch eine Art Soundkarte benotigt. Denn der Kopfhorer-Ausgang eignet sich allerhochstens um System-Sounds auszugeben (in schlechter Qualitat). Die Soundkarte beim Raspi wird als DAC bezeichnet (Digital Analog Converter). Auch wenn der Raspberry Pi uber USB Ports verfugt, ist ein USB DAC nicht geeignet. Die Ursache liegt in der internen Anbindung des USB Busses. Hier kommt es ofters zu Datenstau und damit zu Aussetzern beim Abspielen.

Da es bei den verfugbaren DACs fur den Raspberry Pi 2 eine nahezu undurchsichtige Vielfalt gibt, ist meine Wahl auf eine Platine aus der Schweiz gefallen. Die HiFiBerry DAC+ Platine ist einer der bekanntesten DACs und wird von fast jeder Software fur den Raspi unterstutzt. Die Platine hat Daniel Matuschek entwickelt, der bereits fruher mit seiner ausgezeichneten DIY Phono-Vorstufe fur Aufsehen sorgte.

Die DAC Platine selbst ist sehr ubersichtlich. Dennoch ist es Daniel gelungen, durch intelligente Beschaltung des Bausteins das Maximum an Klang raus zu holen. Klar gibt es bessere DACs, diese sind jedoch erheblich teurer.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_40.jpg)

Abbildung 6: HiFiBerry DAC fur Raspberry Pi A und B (Quelle: HiFiBerry)

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_41.jpg)

Abbildung 7: HiFiBerry DAC fur Raspberry Pi A+, B+ und 2 (Quelle: HiFiBerry)

Die HiFiBerry DAC+ Platine gibt es wahlweise mit CINCH Anschlussen, ohne Anschlusse nur mit Lotpads oder mit 3,5mm Stereo Buchse zu kaufen. Fur mich ist die Cinch Ausfuhrung am praktischsten.

Hier die Zusammenfassung der benotigten Hardware:

\- Raspberry Pi 2  
\- 5V Netzteil (und ggf. ein Kabel mit microUSB Stecker)  
\- microSD Karte mit 4GB Kapazitat (oder mehr, wird aber nicht benotigt)  
\- USB WLAN Dongle (optional)  
\- HiFiBerry DAC+

Der Aufbau der Hardware ist simpel: HifiBerry DAC+ Karte draufstecken (die beiliegenden Plastikabstandshalter nicht vergessen), LAN Kabel (und falls vorhanden WLAN Stick) einstecken. Fur das Gehause reichen ein paar LEGO Bausteine. Das Netzteil wird spater angeschlossen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_42.jpg)

Abbildung 8: HiFiBerryDAC mir RaspberryPi in bekannten Bauklotzchen-Gehause

Wie ein Golem einen Zauberspruch auf magischem Papier in seinem Kopf brauchte, um zu leben, so muss auch die Hardware durch Software belebt werden. Nun, es gab fur die „Aktivierung" eines Golems eine Menge an Zauberspruchen, genauso gibt es recht viele Software-Losungen fur Netzwerkplayer. Die mehr oder weniger bekannten Namen der verschiedenen Software-Distributionen sind:

\- Pi MusicBox  
\- P Core Player  
\- Volumio  
\- Rune Audio

Daniel Matuschek, der Entwickler der HiFiBerry Platine, hat die Treiber-Software fur Linux gebaut. Diese Treiber haben es in die „Core"-Distribution von Raspberry Pi Linux geschafft. Damit wird die HiFiBerry Platine von fast jeder Software-Distribution „Out-Of-the-Box" unterstutzt.

Ich habe mich fur RuneAudio entschieden, da mir Volumio zurzeit nicht besonders gefallt. Aber wer weiß, da sich alle Software-Distributionen in permanenter Weiterentwicklung befinden, kann es in der Zukunft passieren, dass ich eine Andere nehme.

Nun ein wenig Magie, damit der Netzwerkplayer zum Leben erwacht. Bitte nimm jetzt die Tastatur und Computer-Maus, offne einen Internet Browser und tippe folgendes in die Adresszeile ein: [http://www.runeaudio.com](http://www.runeaudio.com/) Dann ein Klick oben rechts auf „Download". Die Software fur Raspberry Pi 2 mit Klick auf „Download latest version" wird die Datei auf den heimischen Rechner ubertragen, wenn Du auf „Speichern" klickst. Die Datei wird von sourceforge.net geladen.

Leider kommt die Datei in einem Format an, mit dem Windows mit den Boardmitteln nicht weiter kommt. Hier Hilft schnell das Werkzeug „7zip" weiter. Das kleine Werkzeug ist schnell installiert.

Anschließend machst Du den Explorer auf und gehst zu der RuneAudio-Datei. Dort wahlst Du mit einem „rechts" Klick auf Runeaudio-Datei „7zip" und dann „Dateien entpacken". Mit dem neuen 7zip Fenster lasst sich die Datei in ein Verzeichnis deiner Wahl entpacken.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_43.jpg)

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_44.jpg)

Nun brauchst Du noch ein Werkzeug um Runeaudio auf die microSD Karte zu installieren, denn ein einfaches Kopieren hilft hier nicht.

Die entpackte Datei ist ein Foto von den Daten der SD-Karte - nein, naturlich nicht! Es ist eine bitgenaue Abbildung der Daten auf der SD Karte. Damit die einzelnen Bits exakt an der vorgesehen Stelle wieder landen, wird ein Programm benotigt, der die Bits fein sauberlich an die richtigen Stellen kopiert. Das Programm ist „Win32 Disk Imager". Das Tool „Win32 Disk Imager" kannst Du am besten auf sourceforge.net herunterladen, dort ist immer die neueste Version zu haben. Dieses Programm muss nicht installiert werden, es reicht, es in ein Verzeichnis zu entpacken.

Die nachsten Schritte sind auch von Computer-Legastheniker zu bewerkstelligen. Als erstes steckst Du die MicroSD-Karte in passenden Slot (ggf. Adapter benutzen) am Computer. Den Dialog von Explorer / Windows kannst Du sofort schließen.

Jetzt startest Du das Programm „Win32DiskImager.exe" und klickst Du auf das blaue Symbol neben dem leeren Feld (unter „Image File"). Ein Datei-Auswahl-Fenster wird geoffnet und Du wahlst die zuvor entpackte RuneAudio-Datei.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_45.jpg)

Als nachstes wahlst Du unter „Device" die SD-Karte aus.  
**ACHTUNG!** Prufe nochmal im Explorer, ob du den richtigen Laufwerksbuchstaben ausgewahlt hast!

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_46.jpg)

Denn bevor Du auf den Knopf „Write" klickst, solltest Du uberpruft haben, ob Du wirklich die microSD Karte ausgewahlt hast. Beim Schreiben der Daten wird auf dem ausgewahlten Laufwerk **ALLES **uberschrieben. Die gleiche Frage, wird Dir auch „Win32 DiskImager" stellen.

Nachdem die Daten erfolgreich auf die microSD-Karte ubertragen worden sind, kannst Du erstmal im Windows unten rechts, den Punkt „Hardware sicher entfernen" ausfuhren, bevor Du die Karte rausnimmst.

Hier die Zusammenfassung der benotigten Software und Tools:

\- RuneAudio Image Datei

\- 7zip

\- Win32 DiskImager

Jetzt bitte den Erweckungs-Zauber, nee, die beschriebene microSD Karte in Raspberry Pi mit HiFiBerry DAC einstecken. Vergiss bitte nicht. den Rasberry Pi 2 mit einem LAN Kabel an deinen Router anzuschließen. Nun darfst Du die Stromversorgung anschließen und dem Blinken der LED's auf dem Raspberry Pi eine Weile zusehen. Nach ein paar Minuten gehst Du zu deinem Rechner und offnest einen Internet-Browser deiner Wahl (Internet Explorer, Chrome oder Firefox oder …)

Die Browser haben oben ein Adressfeld. In diese Adresszeile tippst Du http://runeaudio ein. WICHTIG! Hinter runeaudio darf nichts stehen (weder ein „.com" noch was anderes)   
Jetzt druckst Du auf „Enter". Wenn alles geklappt hat offnet sich diese Seite:

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_47.jpg)

Falls es nicht auf Anhieb geklappt hat, nicht verzagen. Oft klappt die Namensauflosung nicht richtig. In diesem Fall musst Du die IP Adresse von deinem Runeaudio auf deinem Router (SpeedPort, Easybox, Fritzbox usw.) nachschlagen. Dann gibst Du statt http://runeaudio z.B. http://192.168.1.123 ein (Beispiel aus meinem Heimnetzwerk, dein Runeaudio hat eine andere IP-Adresse!).

Bevor Du Musik horen kannst (Cinch-Kabel schon angeschlossen?) musst Du noch ein wenig Konfigurationsarbeit leisten. Aber auch das ist sehr einfach!

Oben, in der rechten Ecke ist der Knopf fur das Menu. Wenn Du drauf klickst, bekommst Du diese Auswahl zu sehen:

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_48.jpg)

Mein erster Schritt ist der Punkt „Sources". Hier stellst Du ein, dass der HiFiBerry DAC das Ausgabemedium („Audio Output") ist. Einfach aus der Liste den HiFiBerryDAC auswahlen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_49.jpg)

Wenn Du die Lautstarke uber dein Handy/Tablet/PC steuern mochtest und einen HiFiBerryDac+ hast, dann kannst Du hier „hardware" auswahlen. Ansonsten lass es auf „disabled" stehen.

Danach scrollst Du im Fenster einige Eintrage weiter runter. Meine Erfahrung ist, dass bei der Nutzung von WLAN es zu Aussetzern kommen kann. Hier hilft ein großer Daten-Buffer. Die Werte, die ich verwende, siehst Du auf dem Screenshot.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_50.jpg)

Zum Schluss nicht vergessen, auf „Save and apply" zu drucken.

Mein nachster Schritt im Menu ist der Punkt „Settings". Hier befinden sich die wichtigen Schalter, wenn Du deine Musik auf dem Tablet oder Smartphone hast. Wenn du ein „angebissener Apfel" Smartphone hast, solltest Du den Schalter „AirPlay" auf „ON" stellen. Du kannst dann mit deinem Gerat die Musik uber die HiFi Beere abspielen.  
Wenn Du ein Gerat mit Android hast, dann ist der Schalter UPnP/DLNA auf on zu stellen. Allerdings brauchst Du auf deinem mobilen Gerat noch eine passende Abspiel-App, die UPnP kann.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_51.jpg)

Die anderen Schalter kannst Du wie auf dem Bild belassen. Zu den Spotify oder Last.fm Einstellungen kann ich nichts schreiben, da ich diese Dienste nicht benutze. Das konnen damit Erfahrene hier leicht durch passende Kommentare unter diesem Artikel erganzen.

Der nachste Punkt auf der Arbeitsliste ist die Einrichtung von WLAN (falls gewunscht und vorhanden). Das WLAN hat einen weiteren „audiophilen" Aspekt. Wie Daniel Matuschek durch Messungen festgestellt hat, bringt das LAN Kabel etwas Sauerei in das Ausgangssignal. Also wech damit! Im Menu den Eintrag „Network" auswahlen und wenn ein USB-WLAN Adapter eingesteckt ist, erscheint unterhalb von „ETH0" Balken (LAN-Kabel) ein „WLAN0" Balken.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_52.jpg)

Ein Klick auf den „WLAN0" Balken startet die Suche nach verfugbaren WLAN Netzwerken. Das kann gut eine Tasse Kaffee dauern.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_53.jpg)

Irgendwann kommt die Liste der verfugbaren WLAN Netzwerke, jetzt wahlst Du das Eigene mit einem Klick auf den Namen aus.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_54.jpg)

Das WLAN Passwort eingeben (WPS geht hier nicht) und auf „Save Profile" klicken.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_55.jpg)

Nun hast Du auch WLAN eingerichtet. Das LAN Kabel kannst Du aber noch nicht abziehen! Das WLAN wird erst nach einem Neustart OHNE LAN-Kabel aktiv.

Wenn Du mochtest, kannst Du jetzt direkt einen USB Stick mit Musik oder eine USB-Festplatte mit eigener Stromversorgung (eigenes Netzteil) anschließen. Je nach Große der der Musiksammlung dauert es eine gewisse Zeit, bis unten links die Schaltflache „Library" zur Verfugung steht. Deine Musik findest Du uber die große Schaltflache „USB storage (1)"

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_56.jpg)

Du siehst auf der rechten Seite jeder Zeile drei kurze Balken. Wenn Du darauf klickst, kannst gu den Inhalt einer Zeile (ein Lied oder einen Ordner) zu der Playlist hinzufugen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_57.jpg)

Die USB Sticks fassen große Mengen Musik. Doch richtig viel Platz gibt es nach wie vor auf Festplatten. Die aktuellen Router verfugen meistens uber mindestens eine USB Buchse oft sind es mehr. Du kannst eine USB Festplatte dann an deinem Router anschließen und auf den Inhalt uber das Heimnetzwerk zugreifen oder vielleicht hast Du eine NAS Kiste. Dann schau dir die nachsten Schritte an, um zu lernen, wie Du die Musik von NAS in den Netzwerkplayer einbinden kannst.

Im Menu oben rechts wahlst Du „Sources", dann kommst Du auf die nachfolgende Seite. Da ich schon ein paar Verzeichnisse von meinem NAS eingebunden habe , siehst Du direkt, wie ich meine Musik-Sammlung organisiert habe.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_58.jpg)

Um ein neues Musikverzeichnis hinzuzufugen, klickst Du bitte auf „ADD NEW MOUNT". Es wird dir ein Formular zur Einrichtung angezeigt. Fur „Source name" kannst Du irgendwas eintragen, doch ist es praktischer, wenn im Verzeichnis hauptsachlich Rock-Bands sind, den Mount z.B. „Rockiges" zu nennen. Das „Fileshare protocol" solltest Du belassen, wie es ist. Unter „IP adress" tragst Du die Adresse von deinem NAS ein (wenn Du nicht weißt, welche Adresse es hat, dann musst Du das auf deinem Router nachsehen).

In „Remote directory" tragst Du den Netzwerkpfad zu deinem Musikverzeichnis (z.B. MusiksammlungRock) ein  
Den Schalter „Guest access" stellst Du auf „ON" wenn Du keine Benutzer auf dem NAS eingerichtet hast und jeder in deinem Heimnetzwerk auf alle Daten zugreifen kann. Falls nicht, musst Du unter „Username" und „Password" entsprechend den richtigen Benutzer eintragen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_59.jpg)

Wenn Du mit der Eingabe fertig bist, klickst Du bitte auf „SAVE MOUNT". Jetzt musst Du nur noch warten, bis die HiFi Beere die Bibliothek erstellt hat, danach kannst Du aus deiner Sammlung was zum Abspielen auswahlen.

![](https://www.lautsprecherbau.de/user/design/stories/Artikel/2015/September2015/Hifiberry/hifiberry_raspberry_pi_bild_60.jpg)

Die paar Stunden Zeit fur die Frickelei haben sich doch gelohnt: dein Audio-Netzwerkplayer muss sich nicht vor seinen kommerziellen Freunden verstecken. Du hast mit einem uberschaubaren Aufwand einen Player gebaut, der im Laden um ein paar Faktoren teurer ist. Dein Player hat noch einem Vorteil: Wenn Dir das Bedienungskonzept oder Farben nicht mehr gefallen, eine zweite microSD zum Spielen kostet fast nix und es gibt noch andere Software…

Peter Gawrych  
aka Rincewind
