# PI-NAS – DLNA/UPnP Media Server

_Captured: 2017-05-06 at 16:41 from [www.welzels.de](http://www.welzels.de/blog/projekte/raspberry-pi/low-budget-nas-mit-einem-raspberry-pi/pi-nas-media-server/)_

Welchen DLAN/UPnP Server man nun installiert bleibt jedem selbst uberlassen. Hier eine Auswahl, von der nur einer installiert sein muss bzw. sein sollte.

## Twonky Media Server

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/twonky-150x150.png)

TwonkyServer ist ein _Digital Living Network Alliance _(DLNA) fahiger UPnP-AV-Server, der sowohl Musik als auch Filme Streamen kann. Das Heißt Gerate, die das DLNA-Protokoll unterstutzen, wie PlayStaion, smartTVs und gewohnliche PCs, konnen von diesem Server Musik und Filme empfangen. Mittlerweile auch iPhone und iPad uber Twonky Beam, die dann auch Musik und Filme auf ein Apple TV uber AirPlay streamen konnen. Jedoch kostet Twonky Server, nach einer Testphase von 30 Tagen, rund 15€, was nicht in das Konzept fur ein Low Budget NAS passt. Dennoch hier die Installation, beginnend mit dem Laden und Entpacken der Dateien:

Damit Twonky auch beim Systemstart geladen wird muss noch das Init-Skript „twonky.sh" in das Verzeichnis "/etc/init.d/" verlinkt werden:

Nun muss noch ein Fehler in der Datei beseitigt werden:

Und den hervorgehobenen Eintrag einfugen:

Dann die Services erzeugen:

12345678 
pi@pi-nas ~ $ sudo insserv twonkyserver pi@pi-nas ~ $ sudo find /etc/rc* -name *twonkyserver/etc/rc0.d/K01twonkyserver/etc/rc1.d/K01twonkyserver/etc/rc2.d/K01twonkyserver/etc/rc3.d/S01twonkyserver/etc/rc5.d/S01twonkyserver/etc/rc6.d/K01twonkyserver

Den Raspberry PI neu booten oder mit pi@pi-nas ~ $ sudo service twonkyserver start starten. Nach dem Neustart die Konfigurationsseite <http://pi-nas:9000> aufrufen. Auf der Twonky Seite auf „Sharing" drucken, das Verzeichnis „/share/Multimedia" wahlen und die Änderungen Speichern.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/twonky_web01-300x229.png)

Auf „Advanced" drucken und den Server neu starten. Er beginnt dann mit Durchsuchen der Mediathek.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/twonky_web02-300x229.png)

Nun konnen noch weitere Einstellungen getroffen werden und, sofern man diesen hat, der Lizenzschlussel eingegeben werden.

Mit den Navigationsschaltflachen Video, Photo oder Musik gelangt man dann in die Mediathek:

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/twonky_web03-300x229.png)

Über die Apps Twonky und Twonky Beam lasst sich dann bequem auf die Mediathek zugreifen und auch an einen Apple TV, uber AirPlay stramen.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/Twonky-200x300.png)

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/twonky-Beam-300x225.png)

(Dear Twonky, I do not understand why the server costs, during the Apps are free in App Store or Google Play? The other way that would make more sense!)

## TVMOBiLi

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/tvmobili-150x150.png)

Ein weiterer DLNA fahiger UPnP-AV-Server mit ahnlichen Funktionen wie Twonky Server. Er ist „fast" kostenlos. Nach 30 Tagen, wird das monatliche Streaming Volumen auf 10GB/Monat begrenzt. Ein unbegrenztes Volumen kostet dann 26€ einmalig oder monatlich 1,30€. Dennoch auch hier die Installation; Laden, entpacken und in das Verzeichnis „/opt" kopieren:

Da hier mehrere Glibc Versionen existieren, muss ein Link auf das entsprechende Binary erzeugt werden:

Danach die Konfigurationsdatei kopieren und anpassen:

Und die markierten Zeilen entsprechend anpassen:

Sowie in dem Init-Skript unter „INSTALLROOT" den Pfad angeben:

Damit TVMOBiLi nach dem Booten automatisch startet mussen noch die Startskripte kopiert und bearbeitet werden.

Von dem Init-Skript Service erzeugt, aber zuvor muss dem Init-Skript noch ein LSB-Header verpasste werden:

Nun den Service erzeugen:

123456789 
pi@pi-nas / $ sudo insserv tvmobilisvcdpi@pi-nas / $ sudo find /etc/rc* -name *tvmobilisvcd/etc/rc0.d/K01tvmobilisvcd/etc/rc1.d/K01tvmobilisvcd/etc/rc2.d/S02tvmobilisvcd/etc/rc3.d/S02tvmobilisvcd/etc/rc4.d/S02tvmobilisvcd/etc/rc5.d/S02tvmobilisvcd/etc/rc6.d/K01tvmobilisvcd

Den Raspberry PI neu starten, damit sichergestellt ist das alles funktioniert. Nach dem der Server gestartet ist gelangt man durch die Eingabe der Adresse <http://pi-nas:30888/__index> in ein Web-Browser zur weiteren Konfiguration.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/TVMOBiLi-Web01-300x229.png)

Next drucken und die Medien-Ordner „/share/Multimedia" hinzufugen.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/TVMOBiLi-Web02-300x229.png)

Dann mit Next zum nachsten Dialog gehen. Hier muss ein Account angelegt bzw. eine Registrierung durchgefuhrt werden.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/TVMOBiLi-Web03-300x224.png)

Eine Emailadresse, Password und Benutzername reichen, es kommt auch keine Mail zuruck. Nach dem die Eingaben durchgefuhrt wurden, kann die Konfiguration abgeschlossen werden.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/TVMOBiLi-Web04-300x229.png)

Danach ist der Server funktionsbereit:

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/TVMOBiLi-Web05-300x229.png)

Mit Twonky Beam lasst sich auch auf diesen TVMOBiLi zugreifen.

## MediaTomb

MediaTomb ist ein weiterer UPnP MediaServer, der allerdings kostenlos und bereits in der Raspbian Paketquelle vorhanden ist. Daher lasst er sich installieren uber:

Mediatomb wird unter den Benutzernamen _mediatomb_ ausgefuhrt. Dieser keinen Berechtigung in das Verzeichnis „/share/Multimedia" zu schreiben, er soll dort aber seine Datenbank anlegen. Daher mussen ihm die Rechte erteilt werden:

Die Konfigurationsdatei offnen:

Und als Home-Verzeichnis „/share/Multimedia" eintragen:

Mediatomb neu starten:

Und das Web-Interface uber <http://pi-nas:49152> aufrufen.

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/mediatomb01-300x220.png)

> _Dort auf die Scan-Einstellungen klicken (roter Pfeil) und die folgenden Einstellungen vornehmen:_

![](http://www.welzels.de/blog/wp-content/uploads/2012/12/mediatomb02-300x220.png)

Alternativ kann der Multimedia Ordner auch uber „Filesystem" eingebunden werden.

Sowohl die iOS App (vermutlich auch Android) Twonky und Twonky Beam konnen auf Mediatomb zugreifen und Musik bzw. Videos verteilen. Cover-Bilder werden nicht angezeigt, vermutlich fehlt noch irgend etwas oder er kann die ID3-Tags nicht lesen. Konnte daran liegen, dass die aktuelle Version 2010 veroffentlicht wurde.

## MiniDLAN

MiniDLAN stellt ein UPnP in bescheidener Form zur Verfugung und ist ebenfalls Bestandteil der Raspbian Paketquelle, lasst sich also direkt installieren:

Nach der Installation mussen die folgenden Einstellungen in der Datei „/etc/minidlna.conf" vorgenommen werden:

Dein Eintrag fur das Medienverzeichnis media_dir=/var/lib/minidlna ersetzen durch:

Der Namen des Server wird wie folgt festgelegt:

Über die Option „inotify" kann festgelegt werden ob automatisch nach neuen Dateien gesucht wird:

Um die Änderungen zu ubernehmen, den Service neu starten:

Über <http://pi-nas:8200> lasst sich eine Statistik aufrufen, eine Web-Administration oder -Medienubersicht gibt es nicht. Dafur kann auch wieder mit Twonky und Twonky Beam auf den Server zugegriffen werden, sogar mit Cover-Bildern.

## Fazit der DLNA/UPnP Media Server

Erste Wahl wahre eigentlich Twonky Server. Er ist recht einfach zu installieren, die Konfiguration uber das Web-Interface ist intuitiv, mehrsprachig und bietet viele Moglichkeiten. Auch die Medienubersicht ist sehr gut gelost. Aber brauche ich das? Eigentlich nicht oder nur ein mal zur Konfiguration und diese kann, wie bei miniDLAN, einfach nach der Installation in der Konsole geschehen. Und das schone Web-Frontend? Es viel bequemer ist mit XBMC oder Twonky Beam auf den Media-Server zuzugreifen.

An dieser Stelle verstehe ich Twonkys Geschaftsmodell nicht, die App ist sowohl kostenlos im [App Store](https://itunes.apple.com/de/app/twonky-beam/id445754456?mt=8) als auch unter [Google Play](https://play.google.com/store/apps/details?id=com.pv.twonkybeam&feature=search_result#?t=W251bGwsMSwyLDEsImNvbS5wdi50d29ua3liZWFtIl0.) erhaltlich, wahrend der Server 15€ kostet. Wo lasst sich wohl der bessere Umsatz machen, auch wenn die App nur einen Euro kosten wurde? Welcher „Bastler" ist bereit einen Media Server zu kaufen, wenn er auch einen kostenlosen bekommt?

TVMOBiLi … eher suspekt und ich frage mich die ganze Zeit wie ich meine Registrierung wieder ruckgangig machen kann. Abgesehen davon mochte ich mich nicht immer kurz vor Monatsende daruber wundern warum ich nicht mehr auf den Server komme.

Somit ist meine Wahl miniDLAN, er bietet alles was ich benotige. Ich kann per iPhone und iPad drauf zugreifen und es auf mein Apple TV streamen (Danke Twonky). Der Zugriff uber PS3 und XBMC ist ebenfalls problemlos moglich.

Mediatomb ware zwar auch kostenlos gewesen und hatte ein Web-Interface, was jedoch weder von der Optik ansprechende, noch intuitiv bedienbar ist. Außerdem scheint die Entwicklung 2010 geendet zuhaben. Daher keine Alternative.

Das ist aber nur meine subjektive Meinung. Mag sein, dass der ein oder andere dennoch die 15€ ausgibt oder einen ganz anderen Server bevorzugt.

iTunes kann nicht auf ein DLAN/UPnP-Server zugreifen, somit fehlt noch etwas fur den Mac. Das folgt dann im nachsten Kapitel.

_Dieses Dokument ist ein Teil von „[Low Budget NAS mit einem Raspberry PI](http://www.welzels.de/blog/projekte/raspberry-pi/low-budget-nas-mit-einem-raspberry-pi/)" und setzt die vorangegangenen Schritte voraus!_
