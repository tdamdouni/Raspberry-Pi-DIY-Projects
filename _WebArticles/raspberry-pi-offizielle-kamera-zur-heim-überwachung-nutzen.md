# Raspberry Pi: Offizielle Kamera zur Heim-Überwachung nutzen

_Captured: 2017-05-01 at 17:36 from [www.google.de](https://www.google.de/amp/s/amp.pcwelt.de/article/9821023)_

** Das offizielle Kameramodul fur den Raspberry ist klein und bietet andererseits eine genugend hohe Auflosung, um als unauffallige Überwachungseinheit zu arbeiten. Der Artikel erklart Schritt fur Schritt, wie das funktioniert. **

![Heimüberwachung mit der Software MotionPie auf dem Raspberry Pi](http://bilder.pcwelt.de/3984145_620x310.jpg)

> _Heimuberwachung mit der Software MotionPie auf dem Raspberry Pi_

[Central Monitoring Software - Download Now](http://www.pcwelt.de/aclk?sa=l&ai=Ck1R20VUHWdniN8_UpgPZvYywCK3Z2OdIyYL-9aUFwI23ARABIMj83AlgyQagAZn8rf8DyAEBqQJf0MLLKUmyPqgDAcgDwwSqBLsBT9DauVBSNnDpdnnd5Kj3zhbjfIxDSjS6oGrvpW5VvqEgma9-7Bsy39BKRI7jFluUn9X7PJZpItxZuCxXMoo3yAWiGLDSLsWKHA_DRo2UmJBGFQVfpkIQpzqXOD2A6UvRDB_ZoAmIRtfjBHr6YJ-68u0br46CzFE1OoJjGI6M5wHRADOuWWKvMV8SKO-oAasgNZ_u4ZYXbo8gOXMN9nHL6q16C4OiCH4_800Z_DjzppSP45dYmonRxU0bs6AGUYAHz4NSqAemvhvYBwHSCAUIgGEQAbEJyS9NVIeQ12_YEwI&num=1&sig=AOD64_09Trqkw_-SROPjZrrzSffOYjadcA&client=ca-pub-3393096715879124&adurl=http://www.go1984.de/)

[Powerful security camera software. Try it for Free - Install Now!](http://www.pcwelt.de/aclk?sa=l&ai=Ck1R20VUHWdniN8_UpgPZvYywCK3Z2OdIyYL-9aUFwI23ARABIMj83AlgyQagAZn8rf8DyAEBqQJf0MLLKUmyPqgDAcgDwwSqBLsBT9DauVBSNnDpdnnd5Kj3zhbjfIxDSjS6oGrvpW5VvqEgma9-7Bsy39BKRI7jFluUn9X7PJZpItxZuCxXMoo3yAWiGLDSLsWKHA_DRo2UmJBGFQVfpkIQpzqXOD2A6UvRDB_ZoAmIRtfjBHr6YJ-68u0br46CzFE1OoJjGI6M5wHRADOuWWKvMV8SKO-oAasgNZ_u4ZYXbo8gOXMN9nHL6q16C4OiCH4_800Z_DjzppSP45dYmonRxU0bs6AGUYAHz4NSqAemvhvYBwHSCAUIgGEQAbEJyS9NVIeQ12_YEwI&num=1&sig=AOD64_09Trqkw_-SROPjZrrzSffOYjadcA&client=ca-pub-3393096715879124&adurl=http://www.go1984.de/) [Gehe zu go1984.de](http://www.pcwelt.de/aclk?sa=l&ai=Ck1R20VUHWdniN8_UpgPZvYywCK3Z2OdIyYL-9aUFwI23ARABIMj83AlgyQagAZn8rf8DyAEBqQJf0MLLKUmyPqgDAcgDwwSqBLsBT9DauVBSNnDpdnnd5Kj3zhbjfIxDSjS6oGrvpW5VvqEgma9-7Bsy39BKRI7jFluUn9X7PJZpItxZuCxXMoo3yAWiGLDSLsWKHA_DRo2UmJBGFQVfpkIQpzqXOD2A6UvRDB_ZoAmIRtfjBHr6YJ-68u0br46CzFE1OoJjGI6M5wHRADOuWWKvMV8SKO-oAasgNZ_u4ZYXbo8gOXMN9nHL6q16C4OiCH4_800Z_DjzppSP45dYmonRxU0bs6AGUYAHz4NSqAemvhvYBwHSCAUIgGEQAbEJyS9NVIeQ12_YEwI&num=1&sig=AOD64_09Trqkw_-SROPjZrrzSffOYjadcA&client=ca-pub-3393096715879124&adurl=http://www.go1984.de/)

Das kleine Kameramodul fur den [Raspberry Pi](http://www.pcwelt.de/ratgeber/Raspberry-Pi-2-Neue-Hardware-zum-gleich-Preis-Test-9653684.html) kann in der beachtlichen Auflosung von 2592 x 1944 Pixeln aufnehmen. Linse und Raspberry selbst sind ausreichend kompakt, um versteckt im Haus das Geschehen zu uberwachen. Sie passen aber auch problemlos in wetterfeste Gehause, um eine Überwachung von Außenanlagen zu ermoglichen. Auf den nachsten Seiten lesen Sie, wie Sie sich eine personliche Überwachungsanlage zusammenbauen.

## Konzept und Zutaten fur die gunstige Heim-Überwachung

Sofern Sie bereits einen [Raspberry Pi](http://www.pcwelt.de/handover/685) der ersten oder zweiten Generation besitzen, benotigen Sie lediglich zusatzlich das Kameramodul. Um die 30 Euro mussen Sie bei den einschlagigen Elektronikversendern dafur einrechnen (etwa [bei Amazon](http://www.pcwelt.de/handover/426?redirect=http%3A%2F%2Fwww.amazon.de%2FKamera-Modul-f%25C3%25BCr-Raspberry-Pi%2Fdp%2FB00E1GGE40%3F%2Fref%3Das_li_ss_tl%3F_encoding%3DUTF8%26camp%3D1638%26creative%3D19454%26linkCode%3Dur2%26site-redirect%3Dde%26tag%3Dpcwelt.de-21) ). Damit die Kameraeinheit moglichst unauffallig im Haus genutzt werden kann, sollten Sie dem Board außerdem ein WLAN-Modul spendieren. [Ein Wi-Fi-Dongle fur die USB-Schnittstelle](http://www.pcwelt.de/ratgeber/Raspberry_Pi_mit_WLAN_ausstatten_-_so_geht_s-Raspberry_Pi-9020385.html) kostet noch einmal maximal zehn Euro. Das Kameramodul selbst besteht nur aus dem Sensor, der auf einer kleinen Platine untergebracht ist, sowie einem fest damit verbundenen Datenkabel. Sie benotigen also zusatzlich ein Gehause fur die Kamera, die dann auch gleichzeitig den Sensor halt. Wenn Sie mit der Überwachungskamera erst in die Welt des Raspberry einsteigen wollen, kaufen Sie zusatzlich die Platine selbst (am besten Modell 2), eine SD-Speicherkarte (Micro- SD-Speicherkarte fur das Modell 2) und ein Netzteil fur den Micro-USB-Anschluss. Zusatzlich ist noch ein Gehause fur den Raspberry zu empfehlen. Oder Sie packen alles zusammen in ein im Handel erhaltliches Kameragehause fur den Außeneinsatz.

Damit die Kamera ihre Arbeit verrichten kann, muss ein Betriebssystem auf dem Raspberry laufen. Es gibt verschiedene Ansatze, um das System als Überwachungseinheit zu nutzen. Eine klassische Kombination ist [Raspbian als Betriebssystem](http://www.pcwelt.de/ratgeber/Raspberry_Pi_als_Desktop_und_Netbook_nutzen-Mobiler_Eigen-PC-8674813.html) und die Software [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion) als Steuerung fur das Kameramodul. Allerdings ist Motion selbst nicht so weit, um die Raspberry-Kamera direkt zu unterstutzen. Damit diese Kombination funktioniert, muss eine speziell angepasste Version eingesetzt und installiert werden, die wiederum einige Abhangigkeiten besitzt.

![Auf dem Board des Raspberry Pi 2 ist der Anschluss für die Kamera vorbildlich beschriftet und liegt neben der HDMI-Buchse.](http://bilder.pcwelt.de/3912959_620x310.jpg)

> _Vergroßern Auf dem Board des Raspberry Pi 2 ist der Anschluss fur die Kamera vorbildlich beschriftet und liegt neben der HDMI-Buchse._

Ein zweiter Ansatz nutzt ein bereits spezialisiertes Betriebssystem, dessen einzige Aufgabe in der Steuerung der Kamera besteht. Der Vorteil: Einrichtung und Nutzung sind technisch wesentlich einfacher. Der Nachteil: Der Raspberry dient ausschließlich als Surveillance Station und kann keine weiteren Aufgaben erfullen. Die Frage ist indes, ob zusatzliche Aufgaben fur eine Platine, die sich in einem Kameragehause außen am Haus befindet, uberhaupt noch realistisch sind? Dieser Workshop entscheidet sich deshalb fur ein noch recht junges Projekt, das die Raspberry-Hardware zur monofunktionalen Überwachungsstation macht.

## Kameramodul und Raspberry verbinden

![](http://api-img.billiger.de/dynimg/G2m52F2NeJmIoGSIovbPLe6s9Q8qlEczXDrU21LmKOZAF4c0q9hDHWuSsXjV1t2OeqWi6SxwZgXsXLqeBEtxtTpZMXnIhdEQNqzEB0MKfUo/810200821.jpg)

Die Kamera ist zwar klein und empfindlich, der Zusammenbau von Kameramodul und Raspberry dennoch nicht besonders schwierig. Sie erhalten das Modul in einer Versandhulle, welche statische Ladung verhindert. Bevor Sie sich an den Zusammenbau machen, sollten Sie sich unbedingt erden, um eine Beschadigung des Bauteils zu vermeiden. Fassen Sie dazu etwa kurz den Heizkorper an. Wenn Sie ganz sicher gehen wollen, besorgen Sie sich aus dem Fachhandel ein Antistatikarmband. Je nach Modell finden Sie die Anschlusse auf dem Board an verschiedenen Stellen.

**Raspberry 2:** Nutzen Sie bereits den Raspberry Pi 2, befindet sich der Anschluss fur die Kamera zwischen HDMI-Port und Audioausgang. Ziehen Sie die kleine weiße Klemme vorsichtig nach oben, und fuhren Sie das Datenkabel nun in den kleinen Schlitz ein. Die Kontakte zeigen in Richtung HDMI-Anschluss. Schieben Sie danach die Klemme vorsichtig nach unten. Damit ist die Verbindung hergestellt.

**Raspberry 1:** Auf dem Board der ersten Generation befindet sich der Anschluss zwischen HMDI- und Ethernet-Buchse. Die Vorgehensweise ist identisch. Die blaue Seite des Datenkabels muss in Richtung Ethernet-Anschluss zeigen.

![Der Anschlusstyp ist beim ersten Raspberry Pi identisch. Hier klemmen Sie das Datenkabel aber zwischen Ethernet-Port und HDMI-Buchse.](http://bilder.pcwelt.de/3912957_620x310.jpg)

> _Vergroßern Der Anschlusstyp ist beim ersten Raspberry Pi identisch. Hier klemmen Sie das Datenkabel aber zwischen Ethernet-Port und HDMI-Buchse._

## Die Software Motion Pie auf dem Raspberry Pi installieren

Laden Sie sich zuerst das Image von Motion Pie auf Ihren Linux-Rechner. Dazu besuchen Sie [Github](https://github.com/ccrisan/motionPie/releases) und wahlen dort die Datei, die zu Ihrem Raspberry passt (Modell 1 oder 2). Nach der Übertragung klicken Sie doppelt auf die Datei. Mit Klicken und Ziehen entpacken Sie das im Archiv gespeicherte Image in ein Verzeichnis Ihrer Wahl. Wenn Sie bereits mit dem Raspberry und Image-Dateien gearbeitet haben, kennen Sie die Prozedur: Damit das System starten kann, wird die Datei zunachst auf die Speicherkarte ubertragen. Der Entwickler stellt [im Wiki zum Projekt](https://github.com/ccrisan/motionpie/wiki/Installation) ein kleines Script zur Verfugung, das unerfahrenen Anwendern alle Arbeiten abnehmen soll. Klicken Sie mit der rechten Maustaste auf „writeimage.sh", und speichern Sie die Datei auf Ihrem Linux-System.

Im Dateimanager (etwa Nautilus oder Nemo) klicken Sie mit der rechten Maustaste auf den Download und nutzen das Kommando „Eigenschaften". Hier kennzeichnen Sie die Datei als ausfuhrbar.

[Weitere innovative Projekte rund um den Raspberry Pi](http://www.pcwelt.de/ratgeber/Innovative_Projekte_rund_um_den_Raspberry_Pi-Heisse_Himbeeren-8999803.html)

Im nachsten Schritt ermitteln Sie, unter welchem Geratenamen die Speicherkarte zu erreichen ist. Diese Info benotigen Sie in jedem Fall, gleich ob Sie das Script nutzen oder den konventionellen Weg zur Installation beschreiten. Legen Sie die Karte also in das Lesegerat ein. lsblk listet alle vorhandenen Datentrager auf; anhand der angezeigten Große sollte die Karte eindeutig zu identifizieren sein. Um das Script fur die Installation zu benutzen, offnen Sie ein Terminal, wechseln in das Verzeichnis, in dem das Script liegt, und verwenden diesen Befehl:

Statt „[x]" verwenden Sie die ermittelte Laufwerkskennung. Das Script erledigt nun alle weiteren Schritte, ohne dass Sie eingreifen mussten. Alternativ nutzen Sie das bewahrte Kommando „dd":

Nach der Kopie entnehmen Sie die Speicherkarte und setzen diese in den Raspberry ein. Verbinden Sie das Gerat mit der Stromversorgung. Nachdem das System gestartet ist, konnen Sie es erstmals per Browser aufrufen. Dazu geben Sie in dessen Adresszeile die IP-Adresse des Raspberry ein, die Sie am schnellsten uber den Router ermitteln.

Motion Pie zeigt bereits auf der Startseite das aktuelle Bild. Um die Optionen zu erreichen, klicken Sie auf den Schlussel am oberen Rand. Als Benutzernamen geben Sie admin ein. Unmittelbar nach der Installation ist noch kein Passwort vergeben. Holen Sie dies am besten sofort nach. Motion Pie kennt zwei Benutzerkonten. Einmal den Administrator, der Änderungen am System vornehmen kann. Zum anderen aber auch einen einfachen Benutzer, der Zugriff auf die Bilder bekommt. Beide Benutzerkonten mussen also nicht notwendigerweise identisch sein. Ändern Sie die Namen und Passworter nach Wunsch, und bestatigen Sie mit „Apply".

![Bei intensivem Gebrauch wird auf der SD-Karte des Raspberry Pi schnell der Speicher knapp. Richten Sie dann etwa eine Verbindung zu einem NAS-Server ein.](http://bilder.pcwelt.de/3912956_620x310.jpg)

> _Vergroßern Bei intensivem Gebrauch wird auf der SD-Karte des Raspberry Pi schnell der Speicher knapp. Richten Sie dann etwa eine Verbindung zu einem NAS-Server ein._

## Das Funknetz des Raspberry Pi aktivieren

Um den Zugriff per WLAN zu ermoglichen, loggen Sie sich als Administrator in das System ein und wahlen die Option „Show Advanced Settings". Damit wird der Abschnitt „Network" sichtbar. Hier konnen Sie dem System eine feste IP-Adresse zuweisen und noch wichtiger: Dort aktivieren Sie den Zugriff per WLAN. Klicken Sie den betreffenden Schalter an, und geben Sie den Namen des Netzwerks (SSID) und das Kennwort ein. Als Verschlusselung wird WPA und WPA2 unterstutzt. Der Netzwerkname sollte keine Leerzeichen enthalten. Mit einem Klick auf „Apply" ubernehmen Sie die Änderungen. Danach verbinden Sie sich mit einem Mobilgerat per WLAN mit dem Raspberry. Ist dieser erfolgreich, entfernen Sie das Ethernet-Kabel. Ihre Überwachungseinheit ist damit einsatzbereit. Sie konnen die Komponenten in einem Kameragehause verbauen und die Einheit an den finalen Ort bringen.

## Vielfaltige Moglichkeiten

Die erweiterten Einstellungen bieten vielseitige Moglichkeiten, die Überwachung im Detail zu steuern:

**Tipp 1:** Je nach Aufnahmeintervall wird das Dateivolumen der Bilder schnell die Speicherkapazitat der SD-Karte ubersteigen. Wenn Sie Bilder und Videos auf einem Server speichern wollen, hinterlegen Sie dessen Angaben unter „File Storage". Unter „Storage Device" entscheiden Sie sich fur „Network Share". Damit offnen sich die weiteren Optionsfelder. Weniger erfahrene Anwender orientieren sich bei den Angaben am besten an den Eigenschaften einer funktionierenden Netzwerkfreigabe, die sie uber den Linux-Dateimanager einsehen konnen. Die Abbildung oben zeigt ein Beispiel fur eine korrekt ausgefullte Netzwerkressource. Bei der Eingabe der Daten sollten Sie sorgfaltig arbeiten. Falsche Angaben fuhren dazu, dass die Kamera nicht mehr aufnimmt.

**Tipp 2:** Zur diskreten Überwachung stort das deutlich sichtbare Licht des Kameramoduls. Dieses schalten Sie unter den „Expert Settings" im Punkt „Enable CSI Camera Led" aus.

**Tipp 3:** Sofern Sie keine Änderungen vornehmen, nimmt die Kamera das Bild permanent auf und zeigt es im Back-End an. Unter „Video Streaming" konnen Sie sich die URL des Streams in die Zwischenablage kopieren. Damit laden Sie die Übertragung auf Wunsch in ein Programm wie etwa den VLC-Player.

![Die Konfigurationsoberfläche zeigt die URLs für das aktuelle Bild. Damit binden Sie dieses auf einer Webseite ein oder betrachten den Stream in einem Player.](http://bilder.pcwelt.de/3912958_620x310.jpg)

> _Vergroßern Die Konfigurationsoberflache zeigt die URLs fur das aktuelle Bild. Damit binden Sie dieses auf einer Webseite ein oder betrachten den Stream in einem Player._

**Tipp 4:** Ihnen genugen Standbilder? Dann aktivieren Sie „Still images". In den Optionen legen Sie die Bildqualitat fest und definieren das Aufnahmeintervall. Im Listenfeld entscheiden Sie sich fur ein zeitgesteuertes Intervall und legen es anschließend in Sekunden fest.

**Tipp 5:** Es gibt auch die Option, dass die Kamera nur dann fotografiert, wenn sich etwas bewegt. In diesem Fall aktivieren Sie „Motion Triggered". Danach mussen Sie aber auch die nachfolgende Option aktivieren: „Motion Detection". Die dort vorgegebenen Werte sind sinnvoll ausgewahlt. Über den Schieberegler legen Sie die Empfindlichkeit fest.

Je geringer der Wert, umso empfindlicher ist die Einstellung. Das kann aber auch zu einer Menge an Falschaufzeichnungen fuhren. Am besten experimentieren Sie empirisch, bis Sie zufrieden sind. Wenn Sie die Bewegungserkennung aktiviert haben, ist auch der Bereich „Motion Movies" auswahlbar. Damit nehmen Sie Bewegtbilder auf. Über die maximale Dauer (voreingestellt ist der Wert 0, was keine Beschrankung bedeutet), die Qualitat sowie die Aufbewahrungszeit (Preserve Movies) steuern Sie, wie viel Speicherplatz benotigt wird.

**Tipp 6:** Damit Sie nicht rund um die Uhr aufnehmen, stellen Sie unter „Working Schedule" einen Zeitplan auf. Markieren Sie die Wochentage, und tragen Sie jeweils einen Zeitraum ein. Über das Listenfeld am unteren Rand steuern Sie, ob innerhalb oder außerhalb dieser Zeit auf Bewegungen geachtet wird.

  
![Windows-Reparatur: System ohne Neuinstallation retten](http://bilder.pcwelt.de/4016707_620x310.jpg)

> _[Windows 7, 8 und 10 sind stabile Systeme und bieten obendrein ein ganzes Arsenal an Reparaturfunktionen, wenn Windows mal stottert.](http://www.pcwelt.de/ratgeber/Windows-Reparatur-ohne-Neuinstallation-so-geht-s-Im-Notfall-9596385.html)_

!['PC schneller machen: Windows, RAM & Festplatten ](http://bilder.pcwelt.de/3965249_300x150.jpg)

!['Großer Test: Die besten Windows-Tablets](http://bilder.pcwelt.de/3975240_300x150.jpg)

!['Windows per USB-Stick installieren - so geht's](http://bilder.pcwelt.de/4045751_300x150.jpg)

!['Virtualisierung – Hyper-V in Windows 10](http://bilder.pcwelt.de/3898105_300x150.jpg)

!['So fährt Windows in nur 3 Sekunden hoch](http://bilder.pcwelt.de/3894244_300x150.jpg)

!['Zurück zu Windows 7: So downgraden Sie Windows 10](http://bilder.pcwelt.de/4045188_300x150.jpg)

!['Win 7 wohl doch noch erhältlich - dank Ausnahme](http://bilder.pcwelt.de/4038475_300x150.jpg)

!['Windows-Explorer stürzt ab: So lösen Sie das Problem](http://bilder.pcwelt.de/3965038_300x150.jpg)

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

!['Microsoft-Tool erspart Ihnen viel Update-Stress](http://bilder.pcwelt.de/3862587_300x150.jpg)

!['Windows 8 ohne Datenverlust zurücksetzen - so geht's](http://bilder.pcwelt.de/3890300_300x150.jpg)

  
![Windows-Reparatur: System ohne Neuinstallation retten](http://bilder.pcwelt.de/4016707_620x310.jpg)

> _[Windows 7, 8 und 10 sind stabile Systeme und bieten obendrein ein ganzes Arsenal an Reparaturfunktionen, wenn Windows mal stottert.](http://www.pcwelt.de/ratgeber/Windows-Reparatur-ohne-Neuinstallation-so-geht-s-Im-Notfall-9596385.html)_

!['PC schneller machen: Windows, RAM & Festplatten ](http://bilder.pcwelt.de/3965249_300x150.jpg)

!['Windows per USB-Stick installieren - so geht's](http://bilder.pcwelt.de/4045751_300x150.jpg)

!['So fährt Windows in nur 3 Sekunden hoch](http://bilder.pcwelt.de/3894244_300x150.jpg)

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

!['Microsoft-Tool erspart Ihnen viel Update-Stress](http://bilder.pcwelt.de/3862587_300x150.jpg)

!['7 geniale Tuning-Tipps für Windows 7](http://bilder.pcwelt.de/3496297_300x150.jpg)

!['Windows 7 & 8: Zehn Tipps zum System-Tuning](http://bilder.pcwelt.de/3671436_300x150.jpg)

!['Geheime Bord-Tools von Windows effektiv nutzen](http://bilder.pcwelt.de/3567594_300x150.jpg)

!['Top 15: Diese Tipps machen Ihr Windows 7 perfekt](http://bilder.pcwelt.de/3460918_300x150.jpg)

!['Animierte Desktop-Hintergründe in Windows 7](http://bilder.pcwelt.de/3206593_300x150.jpg)
