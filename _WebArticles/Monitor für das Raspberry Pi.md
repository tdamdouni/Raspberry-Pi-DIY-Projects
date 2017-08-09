# Monitor für das Raspberry Pi

_Captured: 2016-11-07 at 10:59 from [kampis-elektroecke.de](http://kampis-elektroecke.de/?page_id=2631)_

![Raspberry Pi](http://kampis-elektroecke.de/wp-content/uploads/2013/07/Raspberry-Pi-klein.jpg)

In diesem Artikel zeige ich euch wie ihr einen kleinen 3,5″ Monitor als Display fur euer Raspberry Pi verwenden konnt.  
Bei dem Monitor handelt es sich um den einer Einparkhilfe und er wird mit Hilfe des AV-Anschlusses von dem Raspberry Pi angesteuert.  
Ihr konnt ihn fur etwa 17€ bei Ebay ersteigern:

-> [Monitor](http://www.ebay.de/itm/300664239676;jsessionid=ABD69B709098B60135F14444C2F81B25?ru=http%3A%2F%2Fwww.ebay.de%2Fsch%2Fi.html%3F_from%3DR40%26_sacat%3D0%26_nkw%3D300664239676%26_rdc%3D1#ht_2638wt_940)

Zusatzlich benotigt ihr noch eine 12V Spannungsquelle (ich zeige euch auch noch wie ihr ihn mit 5V betreiben konnt), sowie ein AV-Kabel mit zwei Steckern.  
Ausgepackt sieht der Monitor so aus:

![Monitor\(1\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Monitor1.jpg)

### **-> Anschluss an das Raspberry Pi:**

Als erstes verbindet ihr den Bildschirm mit eurer Spannungsquelle und dem Raspberry Pi:

![Monitor\(2\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Monitor2.jpg)

![Monitor\(3\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Monitor3.jpg)

Die Spannungsquelle stellt ihr anschließend auf 12V ein.  
Sobald euer Pi bootet sollte folgendes auf dem Monitor erscheinen:

![Monitor\(4\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Monitor4.jpg)

Naturlich ist die Schrift noch etwas klein.  
Diese konnt ihr mittels:

andern. Hierfur wahlt ihr als erstes wahlt ihr _UTF-8_ aus:

![Monitor\(5\)](http://kampis-elektroecke.de/wp-content/uploads/2013/07/Monitor5.png)

Anschließend wahlt ihr _Guess optimal character set_ und danach _VGA_:

![Monitor\(7\)](http://kampis-elektroecke.de/wp-content/uploads/2013/07/Monitor7.jpg)

Als letztes musst ihr dann _16×28 (framebuffer only)_ auswahlen:

![Monitor\(8\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Monitor8.jpg)

Nach einer kurzen Wartezeit sollte das Bild anschließend so aussehen:

![Monitor\(9\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Monitor9.jpg)

### **-> Umbau des Monitors:**

Hier zeige ich euch wie ihr den Monitor so umbaut, dass er mit einer Versorgungsspannung von 5V auskommt.  
Dadurch ist es moglich den Monitor direkt am USB-Port des Raspberry Pi zu betreiben.  
Diese Option funktioniert allerdings nur bei der Version 2 vom Raspberry Pi ohne zusatzlichen Aufwand, da diese Version keinen Überlastschutz am USB-Port mehr besitzt (bei der Version 1 ist dies F1 und F2 direkt neben dem USB-Port).  
Als erstes musst ihr den Monitor offnen.  
Dies macht ihr indem ihr die vier Schrauben auf der Ruckseite entfernt:

![Umbau Monitor\(1\)](http://kampis-elektroecke.de/wp-content/uploads/2013/07/Umbau_Monitor1.jpg)

Jetzt konnt ihr den Monitordeckel abnehmen.  
Der nachste Schritt besteht darin, ein IC (Typ XL1509) zu entfernen und die rote Leitung des Kabels an den Pin 2 des ausgeloteten ICs (hier bei mir an dem 4-pol Stecker) anzuloten. Dies konnt ihr machen ohne die Platine losen zu mussen, indem ihr die Platine an der Ecke mit dem Stecker vorsichtig mit einem Schraubendreher anhebt.  
Fertig umgebaut sieht die Leiterkarte dann so aus (die Stellen die ihr andern musst habe ich markiert):

![Umbau Monitor\(2\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Umbau_Monitor2.jpg)

Die Umbauarbeiten am Kabel sehen so aus:

![Umbau Monitor\(3\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Umbau_Monitor3.jpg)

Das Kabel bekommt ihr aus dem Stecker, indem ihr den Stecker raus zieht und die kleine Nase des Anschlusses, auf der Ruckseite des Steckers, vorsichtig mit einer Pinzette nach oben biegt.  
Den Crimpkontakt schneidet ihr anschließend mit einem Seitenschneider ab.  
Damit sind die Umbauarbeiten am Monitor abgeschlossen und ihr konnt diesen wieder zuschrauben.  
Jetzt kommt das Monitorkabel dran.  
Hierfur habe ich mir so einen USB-Stecker samt Gehause bestellt:

![Umbau Monitor\(4\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Umbau_Monitor4.jpg)

Die beiden Litzen fur die Spannungsversorgung werden an die beiden außersten Anschlusse des Steckereinsatzes gelotet (vorher die Haube fur den USB-Stecker uber das Kabel ziehen ;)).  
Hierbei solltet ihr auf die Anschlussbelegung eines USB-Steckers achten.  
Diese seht ihr hier:

![USB Wikipedia](http://kampis-elektroecke.de/wp-content/uploads/2013/07/USB.jpg)

Quelle: [Wikipedia](http://de.wikipedia.org/wiki/Universal_Serial_Bus)

Fertig sieht dies dann so aus:

![Umbau Monitor\(5\)](http://kampis-elektroecke.de/wp-content/uploads/2013/07/Umbau_Monitor5.jpg)

Danach kann der Einsatz zusammen gebaut werden und in das Steckergehause geschoben werden…

![Umbau Monitor\(6\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Umbau_Monitor6.jpg)

Jetzt konnt ihr die Klappe vom Metallgehause drauf setzen und die Kabelfuhrung zusammenquetschen…

![Umbau Monitor\(7\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Umbau_Monitor7.jpg)

Als letztes musst ihr dann nur noch die Haube uber den Stecker ziehen.  
Hier seht ihr den kompletten Stecker und das komplette Kabel:

![Umbau Monitor\(8\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Umbau_Monitor8.jpg)

![Umbau Monitor\(9\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Umbau_Monitor9.jpg)

Bei der 256MB Version des Raspberry Pi musst ihr noch den Überlastschutz F2 und F3 entfernen und uberbrucken.  
Entweder ihr verbinden die beiden Pads, welche direkt neben dem USB-Port liegen, mit einem Stuck Draht oder ihr verwendet 0 Ohm Widerstande. ich habe mich fur die zweite Losung entschieden:

![Umbau Monitor\(10\)](http://kampis-elektroecke.de/wp-content/uploads/2014/06/Umbau_Monitor10.jpg)

Der komplette Aufbau sieht dann so aus:

![Umbau Monitor\(11\)](http://kampis-elektroecke.de/wp-content/uploads/2013/07/Umbau_Monitor11.jpg)

![Umbau Monitor\(12\)](http://kampis-elektroecke.de/wp-content/uploads/2013/07/Umbau_Monitor12.jpg)

**Dokumentation:**

-> [Zuruck zu den Basteleien mit dem Raspberry Pi](http://kampis-elektroecke.de/?page_id=1648)
