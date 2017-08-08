# Mit dem Raspberry Pi die Wohnung überwachen

_Captured: 2017-03-04 at 23:24 from [www.pcwelt.de](http://www.pcwelt.de/ratgeber/Mit_dem_Raspberry_Pi_die_Wohnung_ueberwachen-Sicherheit-8638548.html)_

![Mit Motion können Sie Ihr Haus über Bilder oder einen Videostream überwachen.](http://bilder.pcwelt.de/4006740_620x310.jpg)

> _Mit Motion konnen Sie Ihr Haus uber Bilder oder einen Videostream uberwachen._

** Ein Raspberry Pi ist vielseitig. Setzen Sie das hauseigene Betriebssystem Raspbian ein, dann lasst sich aus dieser Kombination sehr einfach ein Überwachungssystem basteln. Sie brauchen dazu noch eine Kamera und die Software Motion. **

[IP Camera Software](http://www.googleadservices.com/pagead/aclk?sa=L&ai=CvmXqYT67WP-ADYeWBZ3YiIAN4rTWgUbEw4aRqgLAjbcBEAEgyPzcCWDJjsaN9KTQGaABmfyt_wPIAQGpAnFlacCP0rE-qAMByAPLBKoEwgFP0PEQaJA-NdROmDGHbYklrzu6j8axAXySGRhpggvtTpVUozulOoJaEPsruxatwIB9-ZsZcpE2Kpr_HU6P015pA5uMQcHtbQafKGGMA-OF9-4wUUF2rc2RExXpBeExmZ-kntm8vrWOtC1_roBYvLJJjGkop_c4HgkX3PELFvIfmgAwQis-AmUNEF7owSfevQFjLhXVNz-JGYgvlLLvANJiW0pv96xp2RAH9YqEbjD8Bp9oewlRH_jxybH5xadzESJnI4AHz4NSqAemvhvYBwHSCAUIgGEQAQ&num=1&cid=CAASEuRomYQnSQHRON_UgSq_5QuYyA&sig=AOD64_1Ozmu9sG1nXZIEZGn4lZld6exx3g&client=ca-pub-3393096715879124&adurl=http://www.go1984.de/)

[Easy-to-use surveillance software. Try it for Free - Install Now!](http://www.googleadservices.com/pagead/aclk?sa=L&ai=CvmXqYT67WP-ADYeWBZ3YiIAN4rTWgUbEw4aRqgLAjbcBEAEgyPzcCWDJjsaN9KTQGaABmfyt_wPIAQGpAnFlacCP0rE-qAMByAPLBKoEwgFP0PEQaJA-NdROmDGHbYklrzu6j8axAXySGRhpggvtTpVUozulOoJaEPsruxatwIB9-ZsZcpE2Kpr_HU6P015pA5uMQcHtbQafKGGMA-OF9-4wUUF2rc2RExXpBeExmZ-kntm8vrWOtC1_roBYvLJJjGkop_c4HgkX3PELFvIfmgAwQis-AmUNEF7owSfevQFjLhXVNz-JGYgvlLLvANJiW0pv96xp2RAH9YqEbjD8Bp9oewlRH_jxybH5xadzESJnI4AHz4NSqAemvhvYBwHSCAUIgGEQAQ&num=1&cid=CAASEuRomYQnSQHRON_UgSq_5QuYyA&sig=AOD64_1Ozmu9sG1nXZIEZGn4lZld6exx3g&client=ca-pub-3393096715879124&adurl=http://www.go1984.de/) [Gehe zu go1984.de](http://www.googleadservices.com/pagead/aclk?sa=L&ai=CvmXqYT67WP-ADYeWBZ3YiIAN4rTWgUbEw4aRqgLAjbcBEAEgyPzcCWDJjsaN9KTQGaABmfyt_wPIAQGpAnFlacCP0rE-qAMByAPLBKoEwgFP0PEQaJA-NdROmDGHbYklrzu6j8axAXySGRhpggvtTpVUozulOoJaEPsruxatwIB9-ZsZcpE2Kpr_HU6P015pA5uMQcHtbQafKGGMA-OF9-4wUUF2rc2RExXpBeExmZ-kntm8vrWOtC1_roBYvLJJjGkop_c4HgkX3PELFvIfmgAwQis-AmUNEF7owSfevQFjLhXVNz-JGYgvlLLvANJiW0pv96xp2RAH9YqEbjD8Bp9oewlRH_jxybH5xadzESJnI4AHz4NSqAemvhvYBwHSCAUIgGEQAQ&num=1&cid=CAASEuRomYQnSQHRON_UgSq_5QuYyA&sig=AOD64_1Ozmu9sG1nXZIEZGn4lZld6exx3g&client=ca-pub-3393096715879124&adurl=http://www.go1984.de/)

In diesem Beitrag zeigen wir Ihnen, wie Sie mit wenig Geld ein Überwachungssystem selbst basteln. Dazu brauchen Sie einen [Raspberry Pi](http://www.pcwelt.de/handover/685), eine Kamera und die Software Motion. Letztere befindet sich in den Repositories der Linux-Distribution Raspbian.

Wir haben das Szenario mit der neuesten Raspian-Version getestet. Es basiert auf Debian GNU/Linux 8 Jessie. Das Betriebssystem wurde vollstandig aktualisiert und befindet sich auf dem Stand Anfang Juli 2016. Als Überwachungskamera wurde ein Kamera-Modul fur den Raspberry Pi verwendet.

## Welcher Raspberry Pi sich am besten eignet

Bevor wir mit Motion in die Vollen gehen, mussen wir uns zunachst etwas mit der Hardware beschaftigen. Die Raspberry-Pi-Familie ist im Laufe der letzten Jahre gewachsen. Welchen Raspberry Pi Sie als Fundament fur das Überwachungssystem einsetzen, hangt ein bisschen von Ihren Anspruchen ab.

![](http://api-img.billiger.de/dynimg/z2McYCsv8zqS5B9lbePzeJan7Ej-H1pTXDrU21LmKOZAF4c0q9hDHWLF6fHi997Baxqk09jAJ_VhKroKKIWdEElyFALK2qq0DDsJnHNbwCV/630686309.jpg)

Den [geringsten Stromverbrauch](https://www.bitblokes.de/2015/11/stromverbrauch-des-raspberry-pi-zero-gemessen/) weisen die Modelle Raspberry Pi A+ und Raspberry Pi Zero auf. Diese sind zwar weniger leistungsstark als ein Raspberry Pi 2 oder 3, aber fur Motion reichen sie allemal. Auf dem System muss keine grafische Oberflache oder kein GUI laufen. Ein weiterer Vorteil der Modelle A+ oder Zero ist die Große. Da die beiden deutlich kleiner sind, lassen sie sich einfacher verbauen oder verstecken.

Wollen Sie einen Raspberry Pi Zero einsetzen, brauchen Sie dafur die neueste Revision oder v1.3 oder hoher. Alles darunter bietet keine Schnittstelle fur das Kamera-Modul. Bei der zweiten Revision benotigen Sie ein spezielles Adapter-Kabel. Außerdem ist zu beachten, dass der Pi Zero keine USB-Schnittstelle mitbringt. Wollen Sie eine normale Webcam als Überwachungskamera anschließen, ist fur die Benutzung eines herkommlichen USB-Anschlusses ein weiteres Adapter-Kabel notwendig. Dann haben Sie aber ein Problem, wenn Sie eine WLAN-Karte einsetzen mochten, weil dann ein USB-Hub notwendig ware.

Ein [Raspberry Pi 3](http://www.pcwelt.de/handover/733?redirect=https%3A%2F%2Fwww.amazon.de%2FRaspberry-Pi-3-Model-B%2Fdp%2FB01CEFWQFA%2Fref%3Dsr_1_1%3Fs%3Dcomputers%26ie%3DUTF8%26qid%3D1468395851%26sr%3D1-1%26keywords%3Draspberry%2Bpi%2Bzero%26tag%3Dpcwelt.de-21) hat WLAN und Bluetooth bereits an Bord. Allerdings braucht diese Version den meisten Strom und wird auch am warmsten. Das sollten Sie bedenken, wenn Sie den SBC (Single Board Computer) irgendwo verbauen mochten.

Der beste Kompromiss zwischen Große und Funktionalitat ist wohl der Raspberry Pi A+. Der Winzling besitzt eine Schnittstelle fur ein Kamera-Modul und hat einen USB-Steckplatz, an dem sich eine WLAN-Karte anschließen lasst.

Sie konnen aber im Prinzip jede Raspberry-Pi-Variante verwenden.

![Für ein Überwachungssystem mit Motion ist der Raspberry Pi A+ schnell genug. Es ist wohl die beste Kompromisslösung, da trotz geringer Größe Kameraschnittstelle und USB-Port vorhanden sind.](http://bilder.pcwelt.de/4004500_620x310.jpg)

## WLAN ist wichtig

Moglicherweise fragen Sie sich zu diesem Zeitpunkt, ob eine WLAN-Verbindung unbedingt notwendig ist. Das ist sie nicht, denn Motion wurde die Bilder auch auf dem lokalen Speicher ablegen. Wollen Sie allerdings an die Aufnahmen, mussen Sie die SD-Karte entnehmen.

Ist eine drahtlose Netzwerkverbindung vorhanden, konnen Sie die Bilder auf ein externes Storage kopieren lassen. Weiterhin ist Motion in der Lage, bei erkannter Bewegung zum Beispiel eine E-Mail zu senden. Deswegen halten wir WLAN fur eine essenzielle Komponente bei diesem Konstrukt.

## Die richtige Kamera wahlen

Die Software Motion funktioniert mit jeder Kamera, die den V4L-Treiber (Video for Linux) verwendet. Das Gerat taucht damit in der Form _/dev/videoX_ auf. Die erste Kamera am System ware _/dev/video0_ , die zweite _/dev/video1_ und so weiter. V4L unterstutzt eigentlich jede handelsubliche Webcam, die via [USB](http://www.pcwelt.de/handover/601) angeschlossen wird.

In den Anfangszeiten des Raspberry Pi und des entsprechenden Kamera-Moduls gab es keine offizielle Unterstutzung fur V4L. Aus diesem Grund war der Einsatz des Kamera-Moduls problematisch. Mithilfe einiger Hacks hat die Geschichte funktioniert, aber als trivial darf die Einrichtung nicht bezeichnet werden. In der Zwischenzeit ist das wesentlich einfacher geworden, und wir empfehlen den Einsatz des Kamera-Moduls.

Sollten Sie unserer Empfehlung folgen, haben Sie zwei Optionen. Es gibt eine normale Kamera und auch eine [NoIR-Version](http://www.pcwelt.de/ratgeber/So-steuern-Sie-mit-Raspberry-Pi-eine-Infrarotkamera-9885564.html) . Letztere hat keinen Infrarotfilter. Wahrend des Tages sehen die Bilder etwas eigenartig aus. Allerdings eignet sich diese Kamera fur Nachtsicht, sollten Sie eine Infrarotbeleuchtung oder einige Infrarot-LEDs im Einsatz haben.

## Raspbian richtig konfigurieren

Bevor wir uns der Einrichtung des Kamera-Moduls widmen, erst einmal einige Tipps fur die richtige Konfiguration von Raspbian.   
Verwenden Sie eine USB-WLAN-Netzwerkkarte, dann konfigurieren Sie diese am besten im GUI. Selbst wenn Sie spater die grafische Oberflache deaktivieren, um Ressourcen zu sparen, wird sich das Raspberry Pi weiterhin mit dem gewahlten WLAN verbinden. Das ist die einfachste Art, das WLAN zu konfigurieren.

Startet bei Ihnen die grafische Schnittstelle, dann stellen Sie das um. Klicken Sie auf _Menu Einstellungen Raspberry-Pi-Konfiguration_ . Nun offnet sich ein Fenster. Unter _System Boot_ setzen Sie den Haken bei _Zum CLI_ .

Fur Motion ist kein GUI notwendig, also verschwenden wir die Ressourcen auch nicht.

Ebenso schadet es nicht, das Passwort zu andern. Das gilt vor allen Dingen dann, wenn der Raspberry Pi aus dem Netzwerk erreichbar ist. Die Standard-Anmeldedaten p _i_ / _raspberry_ sind in der Zwischenzeit sehr bekannt. Eine automatische Anmeldung ist ebenfalls nicht notwendig, da sich Motion auch so starten lasst.

![Passwort ändern, GUI deaktivieren und automatische Anmeldung deaktivieren.](http://bilder.pcwelt.de/4004506_620x310.jpg)

> _Passwort andern, GUI deaktivieren und automatische Anmeldung deaktivieren._

Wollen Sie spater entfernt (remote) auf den Raspberry Pi zugreifen, muss der SSH-Server aktiviert sein. Wenn Sie die Raspberry-Pi-Konfiguration sowieso offen haben, konnen Sie das im Reiter Schnittstellen uberprufen. Eine Konfiguration ist spater uber das Kommandozeilen-Tool _raspi-config_ ebenfalls moglich.

![Überprüfen Sie gleich, ob der SSH-Server läuft oder nicht.](http://bilder.pcwelt.de/4004510_620x310.jpg)

> _Überprufen Sie gleich, ob der SSH-Server lauft oder nicht._

Weiterhin benotigen Sie die IP-Adresse des Raspberry Pi. Am besten ist, das Gerat besitzt eine feste IP-Adresse. In modernen Routern ist es moglich, eine IP-Adresse immer der gleichen Mac-Adresse zuweisen zu lassen. Das ist die einfachste Art, eine fixe IP-Adresse zu vergeben.

Wollen Sie die momentan zugewiesene IP-Adresse des Raspberry Pi herausfinden, dann dient dafur der Kommandozeilenbefehl _ifconfig_ . Damit kommen Sie auch an die Mac- oder Hardware-Adresse.

![Die Hardware-Adresse brauchen Sie eventuell, um dem Raspberry Pi eine fixe IP-Adresse zu spendieren.](http://bilder.pcwelt.de/4004502_620x310.jpg)

> _Die Hardware-Adresse brauchen Sie eventuell, um dem Raspberry Pi eine fixe IP-Adresse zu spendieren._

Mit fester IP-Adresse und SSH-Server konnen Sie den Winzling im sogenannten Headless-Modus, also ohne Bildschirm, betreiben und konfigurieren. Ein Zugriff unter Linux und Mac OS X ist uber ein Terminal per Standard moglich. Bei [Windows](http://www.pcwelt.de/handover/451) brauchen Sie zusatzliche Software wie den kostenlosen SSH-Client [putty](http://www.putty.org/) .

![Richtig konfiguriert, lässt sich der Raspberry Pi im Headless-Modus betreiben und konfigurieren.](http://bilder.pcwelt.de/4004512_620x310.jpg)

> _Richtig konfiguriert, lasst sich der Raspberry Pi im Headless-Modus betreiben und konfigurieren._

## Das Kamera-Modul fur Motion fit machen

Nachdem das System nun ganz auf unsere Bedurfnisse zugeschnitten und optimiert ist, kummern wir uns um das Kamera-Modul an sich. Zunachst einmal aktivieren wir es. Rufen Sie dazu auf der Kommandozeile das Konfigurationsprogramm mit dem Befehl _raspi-config_ auf. Über den Punkt 6 konnen Sie das Kamera-Modul aktivieren.

![Das Englisch-Deutsch-Kauderwelsch übersehen wir ganz lässig und aktivieren das Kamera-Modul.](http://bilder.pcwelt.de/4004504_620x310.jpg)

> _Das Englisch-Deutsch-Kauderwelsch ubersehen wir ganz lassig und aktivieren das Kamera-Modul._

Nun ist das Kamera-Modul aktiv, aber es ist noch nicht via V4L-Treiber ansprechbar. Dafur fuhren Sie auf der Kommandozeile den Befehl

aus. Sollte es hier zu einer Fehlermeldung kommen, ist vorher ein weiterer Befehl notwendig. Er lautet

Laufen die Befehle ohne Fehlermeldung durch, haben Sie nun ein Gerat _/dev/video0_ . Sie konnen den Umstand uberprufen, indem Sie den Befehl _ls /dev/vi*_ aufrufen.

![Nachdem der oder die Treiber geladen sind, überprüfen Sie das Gerät /dev/video0.](http://bilder.pcwelt.de/4004503_620x310.jpg)

> _Nachdem der oder die Treiber geladen sind, uberprufen Sie das Gerat /dev/video0._

Der Treiber ist zu diesem Zeitpunkt geladen, wurde aber einen Neustart nicht uberstehen. Diese Prozedur konnen Sie allerdings automatisieren. Fugen Sie dafur in der Datei _/etc/modules_ die Zeile _bcm2835-v4l2_ ein. Das konnte inklusive eines Kommentars so aussehen:

![So startet der richtige Treiber bei Systemstart automatisch.](http://bilder.pcwelt.de/4004509_620x310.jpg)

> _So startet der richtige Treiber bei Systemstart automatisch._

**Tipp fur Experten:** Der Befehl _lsmod_ gibt ebenfalls Aufschluss uber die geladenen Treiber.

![Experten sehen sehr schnell, ob die gewünschten Treiber richtig geladen sind.](http://bilder.pcwelt.de/4004508_620x310.jpg)

> _Experten sehen sehr schnell, ob die gewunschten Treiber richtig geladen sind._

## Die Bewegungserkennungs-Software Motion installieren

Die Open-Source-Software Motion klinkt sich direkt in das Gerat _/dev/videoX_ ein und wertet den Video-Stream aus. Sollte sich die Anzahl der vorher festgelegten Pixel andern, wertet die Software diesen Zustand als Bewegung. Je nach Konfiguration fuhrt das Programm dann bestimmte Aktionen aus.   
An dieser Stelle ist das System nun perfekt fur Motion konfiguriert. Die Software zu installieren, ist ein Kinderspiel. Dafur rufen Sie den Befehl

auf. Bestatigen Sie die Frage mit der Taste _J_ und lehnen Sie sich zuruck. Die Installation dauert nur wenige Momente.

![Die Installation der Überwachungs-Software ist ein Einzeiler.](http://bilder.pcwelt.de/4004507_620x310.jpg)

> _Die Installation der Überwachungs-Software ist ein Einzeiler._

Eine Installation bedeutet allerdings noch nicht, dass Motion automatisch startet. Mochten Sie das, dann editieren Sie die Datei _/etc/default/motion_ . Darin finden Sie nur zwei Zeilen, und eine davon ist ein Kommentar. Wenn Sie die zweite Zeile von _start_motion_daemon=no_ andern auf

lauft die Software zur Erkennung von Bewegung bei jedem Systemstart automatisch.

Wir kummern uns vor dem Start des Daemons aber zunachst um die Konfiguration.

Fur einen kurzen Check konnen Sie die Software manuell starten. So wissen Sie, dass alles funktioniert.

## Erste Schritte mit Motion

Starten Sie die Software mit diesem Befehl handisch:

Das _sudo_ ist in diesem Fall notig, damit lediglich der Benutzer _root_ die Standardkonfigurationsdatei lesen darf. Legen Sie eine conf-Datei in Ihrem Home-Verzeichnis an, dann lasst sich Motion auch mit einem anderen Nutzer starten. Klappt das ohne Fehlermeldung, wissen wir, dass unsere Hardware funktioniert.

![Für eine schnelle Überprüfung ist ein manueller Start gar nicht verkehrt.](http://bilder.pcwelt.de/4004528_620x310.jpg)

> _Fur eine schnelle Überprufung ist ein manueller Start gar nicht verkehrt._

Es gibt noch eine andere Art der Überprufung, die wir mit dem Browser durchfuhren konnen. Damit lasst sich das Bild sehen, das die Kamera gerade einfangt. Allerdings ist die Überwachungs-Software so konfiguriert, dass nur der lokale Rechner Zugriff auf den Stream hat. Stoppen Sie Motion daher:

Öffnen Sie im Anschluss die Standardkonfigurationsdatei _/etc/motion/motion.conf_ . Dazu nehmen Sie zum Beispiel _nano_ :

Die Datei ist ein ziemliches [Monster](http://www.monster.de), und wir passen sie spater noch an. Fur den Moment suchen Sie nach der Zeile _stream_localhost on_ und andern sie in _stream_localhost off_ . Der Parameter befindet sich in der Sektion _# Live Stream Server_ .

Starten Sie Motion abermals und geben Sie in einen Browser im selben Netzwerk _http://<IP-Adresse Raspberry Pi>:8081_ ein. In unserem Fall ist das _http://192.168.100.52:8081_ .

Haben Sie zum Beispiel VLC installiert, konnen Sie damit den Stream ebenfalls offnen. Klicken Sie dazu auf _Medien Netzwerkstream offnen_ und geben im entsprechenden Feld die URL ein.   
Dieser Punkt ist auch dann wichtig, wenn Sie den Raspberry Pi ohne Monitor als Überwachungskamera einrichten mochten. Sie wollen die Kamera schließlich so positionieren, dass ein optimaler Bereich uberwacht wird.

![Sie können auch mit VLC überprüfen, ob die Hardware richtig funktioniert.](http://bilder.pcwelt.de/4004526_620x310.jpg)

> _Sie konnen auch mit VLC uberprufen, ob die Hardware richtig funktioniert._

![Mit VLC können Sie den Stream von motion abgreifen. Somit ist sogar eine Live-Überwachung möglich.](http://bilder.pcwelt.de/4004529_620x310.jpg)

> _Mit VLC konnen Sie den Stream von motion abgreifen. Somit ist sogar eine Live-Überwachung moglich._

## Das Wichtigste der Konfigurationsdatei

In diesem Abschnitt kummern wir uns um die wichtigsten Parameter der Konfigurationsdatei. Sie werden diese Datei im Laufe der Zeit zu Zwecken der Feinabstimmung des ofteren anpassen. Alles zu erklaren wurde den Rahmen dieses Artikels sprengen. Allerdings sind einige Parameter sehr wichtig, und diese mochten wir Ihnen kurz erklaren.

Relativ am Anfang finden Sie die Zeile _videodevice /dev/video0_ . Sollte nur eine Kamera am Raspberry Pi hangen, ist das so in Ordnung. Motion kann aber auch mit mehr als einer Kamera umgehen. Dafur wurden Sie unterschiedliche Konfigurationsdateien verwenden und Motion mithilfe des Schalters _-c_ den Pfad der Konfigurationsdatei mitteilen:

Etwas weiter unten finden Sie die beiden Zeilen _width 320_ und _height 240_ . Das sind Breite und Hohe des Bildes, das Motion ausgibt und entsprechend speichert. Sie sollten die maximalen Werte der eingesetzten Kamera kennen und die Werte aus diesem Grund nicht uberschreiten. Passen Sie außerdem auf, dass die Bilder nicht zu groß werden, sonst geht Ihnen bei viel Bewegung irgendwann der Speicher auf dem Datentrager aus. Wir empfehlen, klein anzufangen und die Großen in kleinen Schritten anzupassen.

Direkt darunter finden Sie _framerate 2_ . Die Zahl ist die maximale Bildanzahl, die pro Sekunde aufgenommen wird. Je hoher die Zahl, desto mehr Bilder gibt es und desto mehr Speicher benotigt das System. Auch hier sollten Sie vorsichtiges Finetuning walten lassen.

Der Parameter _auto_brightness_ steht per Standard auf _off_ . Billige Webcams bringen keine automatische Justierung der Helligkeit mit sich. Sollten Sie deswegen Probleme haben, konnen Sie Motion diese Einstellung uberlassen. Direkt darunter finden Sie die Parameter _brightness_ , _contrast_ , _saturation_ und _hue_ . Diese Parameter dienen zur weiteren optimalen Abstimmung der Bildqualitat.

![Die rot markierten Parameter helfen, die Bildqualität optimal für Ihr Szenario anzupassen.](http://bilder.pcwelt.de/4004527_620x310.jpg)

> _Die rot markierten Parameter helfen, die Bildqualitat optimal fur Ihr Szenario anzupassen._

## Bewegung erkennen

Sehr wichtig in der Konfigurationsdatei ist die Sektion _# Motion Detection Settings_ . Der erste Parameter, _threshold_ , bestimmt, wie viele Pixel sich in einem Bild andern mussen, um als Bewegung wahrgenommen zu werden. Per Standard steht das auf 1500. Behalten Sie im Hinterkopf, dass bei Änderung der Breite und Hohe die Gesamtzahl der Pixel wachst.

Bei den Standard-Einstellungen haben wir 76800 Pixel pro Bild (320 x 240). Setzen Sie das zum Beispiel auf 640 und 480, waren das 307200 Pixel. Eine Änderung ist fur die Software aber weiterhin 1500 Pixel. Die Sache wird also wesentlich sensibler.

![Diese Sektion ist das Herzstück der Bewegungs-Erkennung. Hier legen Sie fest, wie viele Pixel sich ändern müssen, damit Motion dies als Bewegung deklariert.](http://bilder.pcwelt.de/4004530_620x310.jpg)

> _Vergroßern Diese Sektion ist das Herzstuck der Bewegungs-Erkennung. Hier legen Sie fest, wie viele Pixel sich andern mussen, damit Motion dies als Bewegung deklariert._

Sobald Motion eine Bewegung erkennt, speichert sie Dateien per Standard im jpg-Format. Zusatzlich wird nach jeder Bewegungssequenz per Standard eine swf-Datei als kleiner Film kreiert. Wo diese Dateien hinterlegt werden, konfigurieren Sie uber den Parameter _target_dir_ . Per Standard ist das der Ordner _/var/lib/motion_ . Sie sollten das Verzeichnis Ihren Anforderungen entsprechend andern. Ein zweiter oder externer Datentrager ist nicht die schlechteste Losung, da Ihnen in diesem Fall das Dateisystem nicht voll laufen kann.

Direkt darunter finden Sie _snapshot_filename_ . Damit legen Sie den Dateinamen fest. Die Standard-Einstellung ist aber bereits sehr gut, da die Dateien anhand eines Zeitstempels abgelegt werden.

Sie finden weiter unten in der Konfigurationsdatei eine Sektion, die mit _# External Commands, Warnings and Logging_ beginnt. Dort konnten Sie bei Erkennung einer Bewegung, sowohl bei Start als auch Ende, bestimmte Befehle ausfuhren lassen. Denkbar ist zum Beispiel das Senden einer E-Mail oder das Abspielen eines Klangs.

## Motion alternativ automatisch starten

In den meisten Fallen sollte ein automatischer Start als Daemon ausreichen. Wie das funktioniert, haben wir in diesem Beitrag bereits behandelt. Nun konnte es aber sein, dass Sie zwei Kameras am Raspberry Pi angeschlossen haben, und beide sollen eigene Konfigurationsdateien erhalten.

Als Vorbereitung uberprufen Sie die jeweilige Konfigurationsdatei und suchen nach der Zeile _daemon=on_ . Diese befindet sich ziemlich am Anfang. Per Standard steht der Parameter auf _on_ und das bewirkt, dass beim handischen Start von Motion das Terminal wieder freigegeben wird.

Sie konnen Scripte unter Raspbian _Jessie_ weiterhin mithilfe der Datei _/etc/init.d/rc.local_ laufen lassen. Das ist einfacher als mit systemd zu hantieren. Dort hinterlegen Sie Befehle, wie Sie diese im Terminal ausfuhren wurden. Ein guter Rat ist allerdings, die vollstandigen Pfade anzugeben. Bei Motion ware das /usr/bin/motion. Wo sich eine ausfuhrbare Datei befindet, fragen Sie mithilfe des Befehls which ab:

Somit sind Sie nun in der Lage, mehrere Motion-Instanzen mit verschiedenen Konfigurationsdateien auszufuhren.

![Bei Raspbian Jessie funktioniert die Datei /etc/rc.local weiterhin wie gehabt.](http://bilder.pcwelt.de/4004501_620x310.jpg)

> _Bei Raspbian Jessie funktioniert die Datei /etc/rc.local weiterhin wie gehabt._

**Tipp fur Experten:** Wollen Sie Motion zum Beispiel nur nachts laufen lassen oder ab einer bestimmten [Uhrzeit](http://www.uhrzeit.org), konnen Sie die entsprechenden Befehle naturlich auch mithilfe eines Cronjobs zeitsteuern.

  
![Windows per USB-Stick installieren - so geht's](http://bilder.pcwelt.de/4045751_620x310.jpg)

> _[Mit Tipps und Tools lassen sich Windows 7, 8.1 und 10 auch von einem speziell vorbereiteten USB-Stick aus installieren.](http://www.pcwelt.de/ratgeber/Windows-per-USB-Stick-installieren-so-geht-s-421524.html)_

!['Virtualisierung – Hyper-V in Windows 10](http://bilder.pcwelt.de/3898105_300x150.jpg)

!['So fährt Windows in nur 3 Sekunden hoch](http://bilder.pcwelt.de/3894244_300x150.jpg)

!['Windows-Reparatur: System ohne Neuinstallation retten](http://bilder.pcwelt.de/4016707_300x150.jpg)

!['PC schneller machen: Windows, RAM & Festplatten ](http://bilder.pcwelt.de/3965249_300x150.jpg)

!['Zurück zu Windows 7: So downgraden Sie Windows 10](http://bilder.pcwelt.de/4045188_300x150.jpg)

!['Win 7 wohl doch noch erhältlich - dank Ausnahme](http://bilder.pcwelt.de/4038475_300x150.jpg)

!['Windows-Explorer stürzt ab: So lösen Sie das Problem](http://bilder.pcwelt.de/3965038_300x150.jpg)

!['Großer Test: Die besten Windows-Tablets](http://bilder.pcwelt.de/3975240_300x150.jpg)

!['11 coole Windows-Features, die Microsoft versteckt hat](http://bilder.pcwelt.de/3985544_300x150.jpg)

!['Video-Tutorial: Windows-Start beschleunigen - so geht's](http://bilder.pcwelt.de/3998642_300x150.jpg)

!['Versteckte Benutzerkonten in Windows anlegen  ](http://bilder.pcwelt.de/3956152_300x150.jpg)

!['Verknüpfungen tarnen: So entfernen Sie den Icon-Pfeil](http://bilder.pcwelt.de/3956136_300x150.jpg)

!['Alle Apps in Windows 8 und 10 auf einen Blick](http://bilder.pcwelt.de/3951236_300x150.jpg)

!['So erstellen Sie eine Verknüpfung in der Taskleiste](http://bilder.pcwelt.de/3939976_300x150.jpg)

!['Windows 8: Boot-Menü beim Hochfahren aufrufen](http://bilder.pcwelt.de/3915657_300x150.jpg)

!['Windows 8: So deaktiveren Sie den Sperrbildschirm](http://bilder.pcwelt.de/3927487_300x150.jpg)

!['Mehr Power durch Windows-Frühjahrsputz](http://bilder.pcwelt.de/3867993_300x150.jpg)

!['Virtueller PC: Gratis & ohne Zusatz-Programm](http://bilder.pcwelt.de/3879215_300x150.jpg)

!['Virtualbox vs. Vmware - vier Virtualisierer im Vergleich](http://bilder.pcwelt.de/3878133_300x150.jpg)

!['Windows-10-Passwort vergessen? Kein Problem!](http://bilder.pcwelt.de/3895665_300x150.jpg)

  
![Windows per USB-Stick installieren - so geht's](http://bilder.pcwelt.de/4045751_620x310.jpg)

> _[Mit Tipps und Tools lassen sich Windows 7, 8.1 und 10 auch von einem speziell vorbereiteten USB-Stick aus installieren.](http://www.pcwelt.de/ratgeber/Windows-per-USB-Stick-installieren-so-geht-s-421524.html)_

!['So fährt Windows in nur 3 Sekunden hoch](http://bilder.pcwelt.de/3894244_300x150.jpg)

!['Windows-Reparatur: System ohne Neuinstallation retten](http://bilder.pcwelt.de/4016707_300x150.jpg)

!['PC schneller machen: Windows, RAM & Festplatten ](http://bilder.pcwelt.de/3965249_300x150.jpg)

!['Zurück zu Windows 7: So downgraden Sie Windows 10](http://bilder.pcwelt.de/4045188_300x150.jpg)

!['Windows-Explorer stürzt ab: So lösen Sie das Problem](http://bilder.pcwelt.de/3965038_300x150.jpg)

!['Windows bootet nicht? So retten Sie es!](http://bilder.pcwelt.de/3974209_300x150.jpg)

!['11 coole Windows-Features, die Microsoft versteckt hat](http://bilder.pcwelt.de/3985544_300x150.jpg)

!['Video-Tutorial: Windows-Start beschleunigen - so geht's](http://bilder.pcwelt.de/3998642_300x150.jpg)

!['Windows 7 mit Win-10-Funktionen aufrüsten](http://bilder.pcwelt.de/3992716_300x150.jpg)

!['So lässt sich USB 3.0 unter Windows 7 nutzen ](http://bilder.pcwelt.de/3985131_300x150.jpg)

!['Versteckte Benutzerkonten in Windows anlegen  ](http://bilder.pcwelt.de/3956152_300x150.jpg)

!['Verknüpfungen tarnen: So entfernen Sie den Icon-Pfeil](http://bilder.pcwelt.de/3956136_300x150.jpg)

!['So erstellen Sie eine Verknüpfung in der Taskleiste](http://bilder.pcwelt.de/3939976_300x150.jpg)

!['Windows XP unter Windows 7 in der VM nutzen](http://bilder.pcwelt.de/3924790_300x150.jpg)

!['Windows-10-Passwort vergessen? Kein Problem!](http://bilder.pcwelt.de/3895665_300x150.jpg)

!['Microsoft-Tool erspart Ihnen viel Update-Stress](http://bilder.pcwelt.de/3862587_300x150.jpg)

!['7 geniale Tuning-Tipps für Windows 7](http://bilder.pcwelt.de/3496297_300x150.jpg)

!['Windows 7 & 8: Zehn Tipps zum System-Tuning](http://bilder.pcwelt.de/3671436_300x150.jpg)

!['Geheime Bord-Tools von Windows effektiv nutzen](http://bilder.pcwelt.de/3567594_300x150.jpg)

!['Top 15: Diese Tipps machen Ihr Windows 7 perfekt](http://bilder.pcwelt.de/3460918_300x150.jpg)
