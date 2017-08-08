# Homematic: CCU2 auf einen Raspberry Pi auslagern – RaspberryMatic

_Captured: 2017-05-19 at 11:13 from [www.technikkram.net](https://www.technikkram.net/2016/12/homematic-ccu2-auf-einen-raspberry-pi-auslagern-raspberrymatic)_

Wer Homematic schon etwas langer im Einsatz hat, weiß, dass die CCU2 nicht die schnellste Hardware beherbergt. Gerade wer mehr Programme und Gerate nutzt, kennt die doch langer werdenden Wartezeiten zwischen den Aktionen. eQ-3 hat schon vor langerer Zeit angekundigt, dass der Code hierfur offen gelegt werden soll, damit Entwickler diesen nutzen konnen.

![](https://www.technikkram.net/wp-content/uploads/2016/12/RaspyMatic-Pi-700x411.jpg)

Ich verfolge das Geschehen schon etwas langer, war aber bisher einfach zu faul, mich darum zu kummern. Da die Installation aber sehr einfach geworden ist, es steht ein Image-File zur Verfugung, habe ich mich dem Thema erneut gewidmet. Doch bevor wir mit der Installation loslegen, mochte ich Euch hierzu ein paar Hintergrunde erklaren.

**Motivation - Warum einen Raspberry Pi nutzen?**

Wie schon eingangs erlautert, ist die [CCU2](http://amzn.to/2irDOxo) nicht gerade ein hoch performantes System, dass man sich fur diesen Zweck vorstellen kann. Bei einer großeren Anzahl an Datenpunkten mach das Gerat sehr schnell die Gratsche und verlangsamt die Arbeit ungemein. Das liegt einfach an der Hardware. Diese ist schon etwas in die Tage gekommen. Jeder Raspberry ist hier mit wesentlich mehr Leistung und Arbeitsspeicher ausgestattet, sodass sich der kleine Computer dafur ideal anbietet.

![](https://www.technikkram.net/wp-content/uploads/2016/12/RaspyMatic-Pi-Modul-gestekt_compressed.jpg)

Die Entwickler haben sich zum Ziel erklart, den gesamten Funktionsumfang der [CCU2](http://amzn.to/2irDOxo) auf den Raspberry Pi zu ubertragen. Aktuell lauft das System auf dem Raspberry Pi2 und mit ein paar Einschrankungen auch auf dem Raspberry Pi3

Leider lauft aktuell kein Homematic IP auf dem Raspberry Pi3. Ansonsten sieht das System nach der einfachen Installation genauso aus, wie Ihr es von Eurer [CCU2](http://amzn.to/2irDOxo) kennt.

**Fur wen ist RaspberryMatic geeignet? **

Klar, fur jeden der gerne Bastelt, der Aufwand hierbei ist aber wie schon gesagt recht gering, es muss kein Code in schwarze Fenster gehackt werden, um den Pi zum Laufen zu bringen. Wer gerne viel ausprobiert und die langen Wartezeiten von der [CCU2](http://amzn.to/2irDOxo) satt hat, fur den konnte das Projekt sehr interessant sein.

Der Vorteil ist, dass die Daten der [CCU2](http://amzn.to/2irDOxo) ubernommen werden konnen, sodass Ihr nicht bei 0 anfangen musst. Alle Gerate, Programme und Verknupfungen konnen von der [CCU2](http://amzn.to/2irDOxo) ubernommen werden.

**Was brauche ich dafur?**

**Bezeichnung**
**Amazon**
**ELV-Shop**
**ELV-Bausatz**

**4 GB SD-Karte**
[Link](http://amzn.to/2fZ9ZC3)
[Link](https://ad.zanox.com/ppc/?40296118C39719437&ULP=%5b%5bhttp://ad.dyntracker.de/set.aspx?trackid=D6B8B9F5EA6894958591B212CBEF4F40&dt_subid1=&dt_subid2=&dt_keywords=&dt_freetext=&dt_url=http://www.elv.de/intenso-microsd-karte-class-10-mit-sd-adapter-4-gb.html?refid=zanox%5d%5d)
nicht verfugbar

**Funkmodul Raspberry Pi**
nicht verfugbar
nicht verfugbar
[Bausatz](https://ad.zanox.com/ppc/?40296118C39719437&ULP=\[\[http://ad.dyntracker.de/set.aspx?trackid=D6B8B9F5EA6894958591B212CBEF4F40&dt_subid1=&dt_subid2=&dt_keywords=&dt_freetext=&dt_url=http://www.elv.de/homematic-funkmodul-fuer-raspberry-pi-bausatz.html?refid=zanox\]\])

**Raspberry Pi 2**
[Link](http://amzn.to/2hpmQOj)
[Link](https://ad.zanox.com/ppc/?40296118C39719437&ULP=\[\[http://ad.dyntracker.de/set.aspx?trackid=D6B8B9F5EA6894958591B212CBEF4F40&dt_subid1=&dt_subid2=&dt_keywords=&dt_freetext=&dt_url=http://www.elv.de/raspberry-pi-2-b-1-gb.html?refid=zanox\]\])
nicht verfugbar

**Raspberry Pi3**
[Link](http://amzn.to/2hOiT6P)
[Link](https://ad.zanox.com/ppc/?40296118C39719437&ULP=\[\[http://ad.dyntracker.de/set.aspx?trackid=D6B8B9F5EA6894958591B212CBEF4F40&dt_subid1=&dt_subid2=&dt_keywords=&dt_freetext=&dt_url=http://www.elv.de/raspberry-pi-3-1-gb.html?refid=zanox\]\])
nicht verfugbar

Fur die Software benotigen wir eine schnelle microSD Karte. Ich habe mir dazu einen [4 GB Karte](http://amzn.to/2hOnpSS) bestellt. Die Karte darf naturlich auch großer sein!

Ein [Netzteil mit 2,5A](http://amzn.to/2eM1JVP) sorgt fur den stabilen Betrieb. Ein [Gehause ](http://amzn.to/2es6PFL)und ein Netzwerkkabel werden auch benotigt.

**Bausatz:**

Der Bausatz besteht auf einer handvoll Teile, die in kurzer Zeit zusammengelotet sind. Solltet Ihr keinen Lotkolben haben, oder einfach keine Lust haben, zu loten, dann schreibt mich einfach an. Ich helfe Euch hier gerne.

![raspymatic-pi-modul](https://www.technikkram.net/wp-content/uploads/2016/12/RaspyMatic-Pi-Modul-e1492633562570.jpg)

> _Mit einem geeigneten Lotkolben sind die Teile in wenigen Minuten verbunden. Die Sockelleiste wird nun noch auf den Raspberry Pi gesteckt (wie im 2. Bild zu sehen)._

**Update 21.01.2017: Hier noch ein paar weitere Bilder + Tipps fur den Zusammenbau:**

![](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Funkmodul-Aufbau-e1492633578360.jpg)

![](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Funkmodul-Aufbau2-e1492633589986.jpg)

![](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Funkmodul-Aufbau3-e1492633598807.jpg)

![](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Funkmodul-Aufbau4-e1492633610427.jpg)

![](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Funkmodul-Aufbau5-e1492633620959.jpg)

![](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Funkmodul-Aufbau6-e1488291098174.jpg)

![](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Funkmodul-Aufbau7-e1492633634108.jpg)

Ihr sollte zuerst die beiden Platinen aneinander loten, dann habt Ihr es einfacher. Als provisorischen Unterlage konnt Ihr die Stiftleiste verwenden, die im nachsten Schritt angelotet werden muss. Achtet auch darauf, dass genugen Hitze an den Lotpunkten ankommt, damit keine kalten Lotstellen entstehen. Zum Schluss empfiehlt es sich, den beiliegenden Ferritkern noch zu verwenden. Das Ende vom Kabel (USB-Netzteil) wickelt ihr 3-4x um den Kern. So konnen Storungen, die sich negativ auf die Antennenleistung auswirken konnen, gefiltert.

Das waren die Schritte, die wird bei der Hardware-Installation bewaltigen mussten. Nun konnen wir zur Software ubergehen.

**Installation:**

Zuerst mussen wir die aktuelle Version von RaspberryMatic herunterladen. Das Image bekommen wir hier her: <https://github.com/jens-maus/RaspberryMatic/releases/latest>

Das Image ist fur den [Pi2](http://amzn.to/2hOrN4f) und [Pi3](http://amzn.to/2iikCVy) geeignet!

Um das gerade heruntergeladene Image auf unsere SD-Karte zu bekommen, verwenden wir die Software [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/) (Windows) oder [ApplePi-Baker](http://www.tweaking4all.com/hardware/raspberry-pi/macosx-apple-pi-baker/) (MacOS).

![homematic-raspymatic-installation](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-RaspyMatic-Installation.png)

Nun starten wir Win32 Disk Imager. Falls dabei Probleme auftreten sollten, bitte als Administrator ausfuhren!

Bei Device wahlen wir unsere microSD-Karte aus und mit dem Ordnersymbol navigieren wir zum Image. Über die Schaltflache „Write" wird der Vorgang gestartet.

![raspberry-pi-homematic](https://www.technikkram.net/wp-content/uploads/2016/12/Raspberry-Pi-Homematic.png)

Nachdem die Karte geschrieben wurde, konnen wir diese in den Pi einsetzen. Jetzt solltet Ihr zuerst das Netzwerkkabel einstecken und dann den Stecker fur die Spannungsversorgung.

Ihr braucht dazu keinen angeschlossenen Monitor und auch keine Tastatur. Der Bootvorgang dauert wenige Sekunden.

Danach konnt Ihr den Pi entweder uber http://IP-ADRESSE-DES-PIS/ oder aber uber <http://homematic-raspi/> im Netzwerk erreichen.

**Übernahme der Daten aus der CCU2:**

Zuerst musst Ihr Euch auf Eurer bestehenden CCU2 einloggen. Die Firmware-Version der CCU2 darf dabei aber nicht hoher sein als die der RaspberryMatic.

Um ein Backup der CCU2 zu erstellen navigiert Ihr zu Einstellungen -> Systemsteuerung -> Sicherheit -> Backup

Dort klickt Ihr auf den Menupunkt „Backup erstellen". Dieser Vorgang dauert wenige Minuten. Dieses Backup legen wir an einem sicheren Ort ab, um es spater wieder in die CCU2 einspielen zu konnen. Hier sind auch alle zusatzlich installierten Programme wie z.B. CUx-Deamon enthalten.

Da diese zusatzlichen Module leider von der RaspberryMatic aus dem Backup nicht verarbeitet werden konnen, mussen wir nun ein 2. Backup anlegen, das wir spater in den Pi einspielen konnen. Das neue Backup muss frei von zusatzlichen Modulen sein. Daher mussen diese vorher geloscht werden.

Darum gehen wir nun unter: Einstellungen->Systemsteuerung->Zusatzsoftware

Hier deinstallieren wir alle Pakete, die vorhanden sind. Keine Angst, diese konnen spater durch unser 1. Backup wieder vollstandig hergestellt werden.

Nun erstellen wir unser 2. Backup fur den Raspberry Pi.

Einstellungen -> Systemsteuerung -> Sicherheit -> Backup

Das 2. Backup nennen wir anders als das Erste, damit wir dieses beim Speichern nicht uberschreiben.

![homematic-backup](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Backup.png)

Die CCU2 nehmen wir nun vom Strom, da zeitgleich nur eine Zentrale laufen darf. Im nachsten Schritt spielen wir nun das 2. Backup, das wir soeben erstellt haben, in unseren Pi ein.

Dazu offnen wir die Weboberflache von RaspberryMatic uber den Link <http://homematic-raspi/>

Dort navigieren wir dann zu dem Punkt Einstellungen -> Systemsteuerung -> Sicherheit -> Backup und wahlen hier den Button „Backup einspielen" aus. Wir wahlen nun das 2. Backup aus. Der Vorgang lauft wesentlich kurzer als auf der CCU2 ;-)

Nun konnt Ihr (bei Bedarf) die zuvor geloschten zusatzlichen Module installieren.

Testet die Performance einfach mal, ich finde, dass der Unterschied wie Tag und Nacht ist. Gerade bei den Programmen merkt man den Unterschied sehr erheblich! Viel Spaß beim Testen.

**Empfang verbessern:**

Durch den Raspberry Pi habe ich mir leider wieder das leidige Thema mit dem schlechten Empfang eingehandelt. Bei meiner [CCU2](http://amzn.to/2irDOxo) hatte ich eine [externe Antenne](http://amzn.to/2hOqwtN) montiert, um das Problem zu beheben.

![rp_Homematic-CCU2-mit-neuer-Antenne-700x394.jpg](https://www.technikkram.net/wp-content/uploads/2016/07/Homematic-CCU2-mit-neuer-Antenne-700x394-1.jpg)

Da es sich bei dem Bausatz von ELV um das gleiche [Funkmodul](https://ad.zanox.com/ppc/?40296118C39719437&ULP=\[\[http://ad.dyntracker.de/set.aspx?trackid=D6B8B9F5EA6894958591B212CBEF4F40&dt_subid1=&dt_subid2=&dt_keywords=&dt_freetext=&dt_url=http://www.elv.de/homematic-funkmodul-fuer-raspberry-pi-bausatz.html?refid=zanox\]\]) handelt, wie es auch in der CCU2 verbaut ist, kann auch bei dem Pi eine externe Antenne angebracht werden. Damit ist dann auch beim Raspberry das Problem mit dem schlechten Empfang behoben. Eine ausfuhrliche Anleitung zum Umbau der CCU2 findet Ihr [hier](https://www.technikkram.net/2016/07/homematic-empfang-der-ccu2-deutlich-verbessern-mit-externer-antenne).

![](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Pi-Umbau-Antenne-e1492633668507.jpg)

Das gleiche habe ich auch erfolgreich an meinem Pi durchgefuhrt. Auch diese Schritte will ich Euch naturlich nicht vorenthalten. Daher habe ich auch [hierzu einen Artikel](https://www.technikkram.net/2017/01/externe-antenne-fuer-den-raspberry-pi-mit-rasberrymatic) geschrieben.

![](https://www.technikkram.net/wp-content/uploads/2016/12/Homematic-Pi-mit-Antenne_compressed.jpg)
