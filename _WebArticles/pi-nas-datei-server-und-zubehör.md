# PI-NAS – Datei-Server und Zubehör

_Captured: 2017-05-06 at 16:50 from [www.welzels.de](http://www.welzels.de/blog/projekte/raspberry-pi/low-budget-nas-mit-einem-raspberry-pi/pi-nas-datei-server-und-zubehor/)_

## Samba Server

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/Finder_smb-300x209.png)

Samba implementiert das SMB/CIFS-Protokoll unter Unix, so dass Dateien und Drucker mit Microsoft Windows, OS X und anderen Unix-Systemen geteilt werden konnen.

Die Konfiguration des Servers kann entweder in der Datei „/etc/samba/smb.conf" vorgenommen werden oder uber das Web-Administations-Tool SWAT. Ich verzichte an dieser Stelle auf eine ausfuhrliche Anleitung zur Konfiguration, da dies vermutlich den Rahmen sprengen wurde und bereits sehr gute Anleitungen, auch in deutscher Sprache, existieren. Ich empfehle einfach mal bei den Kollegen von [ubunuusers](http://ubuntuusers.de) vorbeizuschauen, in deren [wiki gibt es ausfuhrliche Informationen bezuglich Samba](http://wiki.ubuntuusers.de/Samba).

Hier die Änderungen die ich an der „/etc/samba/smb.conf" vorgenommen habe:

Ein Samba User kann anlegen mit (pi ist der User pi):

SWAT lasst sich uber einen Web-Browser durch die Eingabe von <http://pi-nas:901> aufrufen. Als root angemeldet lassen sich dort die notwendigen Konfigurationen vornehmen.

## Netatalk

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/Finder-300x210.png)

Netatalk ist eine frei verfugbare Open-Source-AFP-Fileserver. Somit konnen mehren Macintosh-Clients gleichzeitig auf das PI-NAS zugreifen.

Nach der Installation ist er noch nicht lauffahig und wird auch noch nicht im Finder angezeigt. Die Konfigurationsdatei „afpd.conf" offnen.

Und die folgende Zeile einfugen:

Innerhalb der „afpd.conf" ist nichts aktiv, daher ist es egal wohin die Zeile kopiert wird.  
Anschließend die Datei „AppleVolumes.default" offnen:

Unter Zeile 177 die folgenden Eintragungen einfugen:

### Avahi fur Netatalk aktivieren

Damit Avahi Netatalk publiziert, muss die Datei "afpd.service" erstellt werden:

In die Datei den folgenden Inhalt einfugen und speichern:

Danach mussen beide Dienste neu gestartet werden:

Wer nicht das Xserve Symbol im Finder angezeigt bekommen mochte, kann die Variable _Xserve_ durch eine der hier aufgefuhrten ersetzen:

![Mac](http://www.welzels.de/blog/wp-content/uploads/2013/01/default.png)

![AirPort](http://www.welzels.de/blog/wp-content/uploads/2013/01/AirPort.png)

![AppleTV1,1](http://www.welzels.de/blog/wp-content/uploads/2013/01/AppleTV11.png)

![iMac](http://www.welzels.de/blog/wp-content/uploads/2013/01/iMac.png)

![MacBook](http://www.welzels.de/blog/wp-content/uploads/2013/01/MacBook.png)

![MacBookPro](http://www.welzels.de/blog/wp-content/uploads/2013/01/MacBookPro.png)

![Macmini](http://www.welzels.de/blog/wp-content/uploads/2013/01/Macmini.png)

![MacPro](http://www.welzels.de/blog/wp-content/uploads/2013/01/MacPro.png)

![PowerBook](http://www.welzels.de/blog/wp-content/uploads/2013/01/PowerBook.png)

![PowerMac](http://www.welzels.de/blog/wp-content/uploads/2013/01/PowerMac.png)

## NFS Server

NFS (Network File System) ursprunglich von SUN entwickelt ist ein Netzwerk-Protokoll um Dateien uber das lokale Netzwerk auszutauschen. Linux und UNIX System konnen sehr einfach auf diese zentrale Dateisystem zugreifen. Somit ist es ideal geeignet andere im netzbefindliche Rasperry PIs mit einem Netzlaufwerk auszustatten.

Fur den Server muss zunachst das folgende Paket installiert werden:

Anschließend werden die gewunschten Freigaben in die Datei „/etc/exports" eingetragen:

Es sollten nicht die Verzeichnisse der Benutzer im Netzwerk freigegeben werden, da hierfur eine einheitliche netzweite numerische UID benotigt wird. Was eigentlich nur mittels LDAP oder NIS-Server sichergestellt werden kann. Daher beschranke ich mich hier auf das Public und Multimedia Verzeichnis:

Der Adressbereich muss entsprechend auf das eigene Netzwerk angepasste werden.

Nun muss noch der IPv6-Betrieb in der Datei „/etc/netconfig" deaktiviert werden, da der Raspberry PI diesen nicht unterstutzt.

Hier fur mussen die Zeilen 16 und 17 deaktiviert werden (# voranstellen):

Abschließend mussen die Freigaben exportiert und der NFS-Kernel-Server sowie der RPCBIND Service gestartet werden:

Leider starten die Dienste nach einem Neustart des Raspberry PI nicht automatisch. Bei alle bislang installierten Services wurden RC-Scripte zum starten und beenden des Service installiert, beim NFS-Server existieren lediglich Skripte zum stoppen. Um diese hinzuzufugen mussen erst einmal die vorhandenen entfernt werden. Die Befehle eingeben, bis kein Skript mehr gefunden wird:

Die drei letzten Befehle, im Beispiel oben, durfen keine Ruckgabe liefern. Die Ruckgaben mussen geloscht werden. Erst danach konnen die neuen Skripte erstellt werden:

Nach dem Reboot starten sollten die Dienste gestartet sein.

## FTP Server

Es gibt eine verschiedene FTP Server innerhalb der Debian Repository, ich habe einfach mal das Paket _proftpd_ gewahlt. Der Pro FTP Server kann einfach uber die Paketquelle installiert werden:

Wahrend der Installation kann ausgewahlt erden, ob dieser als _standalone_ oder als _inetd_ betrieben werden soll. Keine permanenten Zugriffe zu erwarten sind sollte inetd gewahlt werden, dies ist ressourcenschonender:

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/proftpd-300x215.png)

Im nachsten Schritt die Konfigurationsdatei offnen:

Und die folgenden Änderungen vornehmen. In Zeile 11 den IPv6 Unterstutzung ausschalten:

In Zeile 15 den Namen des Servers festlegen:

In Zeile 34 legen wir noch fest, dass der Benutzer nur Zugriff auf sein Home-Verzeichnis haben soll und nicht in die untere Ebene wechseln kann:

Den Server neu starten:

Soll der zugriff auch uber Secure FTP (SFPT) moglich sein, so muss am Ende der Datei noch folgende hinzugefugt werden und danach neu starten:

Auf den anonymen Zugang verzichte ich. Aber wie aus der Konfigurationsdatei ersichtlich, kann dieser einfach durch das entfernen der Rauten im unteren Teil aktiviert werden.

_Dieses Dokument ist ein Teil von „[Low Budget NAS mit einem Raspberry PI](http://www.welzels.de/blog/projekte/raspberry-pi/low-budget-nas-mit-einem-raspberry-pi/)" und setzt die vorangegangenen Schritte voraus!_
