# Raspberry Pi als Server im Dauerbetrieb (24/7, headless)

_Captured: 2017-05-06 at 15:18 from [www.elektronik-kompendium.de](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002251.htm)_

Fur die meisten Server-Aufgaben war der ursprungliche Raspberry Pi vollig ungeeignet. Das Problem war dessen geringe CPU- und I/O-Geschwindigkeit, sowie der kleine Arbeitsspeicher. Diese drei Komponenten reduzierten die Moglichkeiten. Mit dem Raspberry Pi 2 B hat sich das geandert. Sowohl die CPU-Geschwindigkeit als auch der Arbeitsspeicher sind fur typische Server-Aufgaben optimal. Gleichzeitig ist der Stromverbrauch so gering, dass er durch den Dauerbetrieb keine Rolle spielt.

Allerdings gibt es eine Einschrankung. Die Anbindung der Netzwerk-Schnittstelle ist nicht optimal. Sie hangt am internen USB. Wenn man noch weitere USB-Gerate anschließt, dann begrenzt man damit auch die Geschwindigkeit der Netzwerk-Schnittstelle.

  * [Raspberry Pi: USB - Universal Serial Bus](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002181.htm)

Wenn man den Raspberry Pi als Server, Gateway oder Router dauerhaft (24/7) betreiben mochte, dann muss man ein paar Dinge beachten. Einiges gilt besonders fur den Raspberry Pi. Anderes gilt generelle fur den Dauerbetrieb, auch fur andere Systeme, die als Server, Gateway oder Router fungieren.  
Die folgenden Hinweise und Maßnahmen beziehen sich auf Optimierungsmoglichkeiten fur den Raspberry Pi und die Verbesserung der Sicherheit. Bei der Optimierung geht es hauptsachlich um Stabilitat und rudimentare Leistungssteigerungen. Bei der Sicherheit geht es darum, den Dauerbetrieb sicherer zu gestalten. Das ist deshalb notwendig, weil der Raspberry Pi, abhangig von der eingesetzten Linux-Distribution, nicht sicher genug konfiguriert ist.

Alle Maßnahmen bezuglich Optimierung und Sicherheit sind optional. Das heißt, keine der Maßnahmen mussen zwangslaufig erfolgen. Man sollte sich nur daruber im Klaren sein, welche Konsequenzen das Unterlassen der einen oder anderen Maßnahme zur Folge haben kann.  
Wer einen Raspberry Pi dauerhaft betreibt, ubernimmt auch die Verantwortung fur Schaden und Folgen. Auch dann, wenn der Raspberry Pi unbeaufsichtigt lauft.

### Schritt fur Schritt: Raspberry Pi als Server einrichten

Wenn man den Raspberry Pi als Server einrichten will, um ihn anschließend im Headless-Betrieb einzusetzen, dann sind je nach individuellen Vorlieben einige Konfigurationsschritte vorzunehmen.

### Übersicht: Raspberry Pi als Server

  * Ausstattung fur den Dauerbetrieb
  * Optimierung fur den Dauerbetrieb
  * Server-Sicherheit im Dauerbetrieb

### Übersicht: Ausstattung fur den Dauerbetrieb

Im Dauerbetrieb geht es hauptsachlich darum, dass der Raspberry Pi stabil lauft. Nichts ist argerlicher als wenn der Raspberry Pi wegen auftretender Fehler seinen Betrieb einstellt oder Aussetzer hat. In so einem Fall kann die Fehlersuche eine nervtotende Angelegenheit sein. Nicht selten kommt es vor, dass man bei der Fehlerursache nichts herausbekommt, deshalb den Fehler nicht nachstellen und deshalb auch keine Losung erarbeiten kann.  
Um genau das zu vermeiden, hier ein paar Empfehlungen bezuglich der Ausstattung des Raspberry Pi.

Grundsatzlich sollte man ein gutes Netzteil verwenden. Es gibt immer wieder Berichte in diversen Foren, dass ein Raspberry Pi nicht richtig funktioniert oder instabil ist. In den allermeisten Fallen ist das Netzteil schuld. Deshalb nicht am Netzteil sparen, wenn der Raspberry Pi als Server im Dauerbetrieb laufen soll.

  * [Das richtige Netzteil](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002021.htm)

SD-Speicherkarten sind extrem gunstig. Wie sich jeder denken kann, ist hier die Qualitat weit gefachert. Dabei muss man wissen, dass SD-Speicherkarten eigentlich fur den Betrieb in Digitalkameras und anderen mobilen Geraten gedacht sind. Hierbei treten so gut wie keine Komplikationen auf, weil hier Schreib- und Lesezugriffe selten und in geringem Umfang auftreten.  
Ganz anders als Datenspeicher fur den Raspberry Pi. Das darauf laufende Betriebssystem schreibt immer mal wieder, wenn auch in geringem Umfang, Daten auf die SD-Karte, was naturlich die Speicherzellen mehr beansprucht, als wenn nur ab und zu eine Fotodatei in einer Digitalkamera gespeichert wird. Mehr Schreibzugriffe fuhren auch zu einer schnelleren Abnutzung und somit schneller zum Ausfall. Im Dauerbetrieb wird das noch viel schneller eintreten. Aus diesem Grund sollte man auch nicht die billigste und kleinste SD-Card nehmen, sondern ein besseres Modell eines Markenherstellers und mit großzugig dimensionierter Speicherkapazitat wahlen.

  * [Die richtige SD-Card](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002011.htm)

### Übersicht: Optimierung fur den Dauerbetrieb (Headless-Konfiguration)

Der Raspberry Pi als Server im Dauerbetrieb lauft in der Regel ohne Bildschirm, Tastatur und Maus. Man bezeichnet das als "headless", respektive Headless-Betrieb, weshalb sich eine spezielle Headless-Konfiguration lohnt. Hauptsachlich in Bezug auf Stabilitat und Leistungssteigerung.

  * Daten auslagern oder sichern
  * Speicherverteilung optimieren
  * Nicht benotigte Dienste abschalten
  * Swapping deaktivieren

Ansonsten kann man zur Minimierung von Schreibzugriffen Log-Dateien und andere temporare Dateien ins RAM auslagern und auf den Eintrag der Zugriffszeiten je Datei verzichten (noatime).

### Optimierung: Daten auslagern oder sichern

Weil SD-Speicherkarten alles andere als zuverlassig sind, eignen sie sich in einem Raspberry Pi nicht, um darauf Daten dauerhaft zu speichern, die regelmaßig erzeugt werden. Außerdem gibt es Falle, bei denen eine mangelhafte Stromversorgung des Raspberry Pi zu Konflikten im Dateisystem und damit zu Datenverlusten fuhren. Im Prinzip muss man beim dauerhaften Betrieb eines Raspberry Pi immer damit rechnen, dass es zum Datenverlust kommen kann. Deshalb sollten Daten auf einem meist zuverlassigeren USB-Stick, ubers Netzwerk auf einem NAS oder in die Cloud gespeichert werden.

  * [USB-Stick automatisch einbinden](https://www.elektronik-kompendium.de/sites/raspberry-pi/1911271.htm)

Ein Mittelweg ist, wenn man die Daten auf der SD-Karte speichert und zusatzlich einmal am Tag automatisch ein Backup der Daten auf einen USB-Stick macht. Dadurch verlangert man die Lebensdauer der SD-Karte nicht, aber hat zumindest eine Datensicherung, wenn die SD-Karte irgendwann Probleme macht.

  * [Backup von Daten erstellen](https://www.elektronik-kompendium.de/sites/raspberry-pi/1911281.htm)

### Optimierung: Speicherverteilung

Das SDRAM auf dem Raspberry Pi ist ein sogenanntes "shared memory". Das heißt, ein großer Teil wird fur den Arbeitsspeicher der CPU verwendet und nur ein kleiner Teil wird fur den Grafikspeicher der GPU genutzt. Standardmaßig ist fur den GPU-Speicher eine Große von 64 MByte festgelegt. Weil man den grafischen Fenster-Manager im Server- bzw. Headless-Betrieb nicht braucht, kann man die Speicherverteilung zu Gunsten des Arbeitsspeichers optimieren.

  * [Speicherverteilung/Memory Split optimieren](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002121.htm)

### Optimierung: Nicht benotigte Dienste abschalten

Im Zuge der Performance- und Speicher-Optimierung geht es auch darum, nicht benotigte Dienste, die aktiviert sind zu identifizieren und ggf. abzuschalten. Das kann Prozessorleistung und Arbeitsspeicher sparen.

  * [Dienste verwalten](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002211.htm)

### Optimierung: Swapping deaktivieren

Wenn man die Speicherverteilung des Raspberry Pi optimiert hat, dann kann man sich uberlegen, ob man das Swapping abschaltet.  
Auf einem Server kann Swapping nutzlich, aber auch unnutz sein. Speziell beim Raspberry Pi ist Swapping eigentlich kontraproduktiv. Swapping erhoht die Anzahl der Schreibzugriffe auf das Speichermedium, auf dem sich der Swap-Speicher befindet. Das Betriebssystem und der Swap-Speicher befindet sich beim Raspberry Pi auf einer SD-Speicherkarte, die nur eine begrenzte Anzahl an Schreibzugriffen vertragt. Damit verkurzt sich die Lebensdauer der SD-Karte. SD-Karten eignen sich deshalb uberhaupt nicht zum Swapping. Vor allem dann nicht, wenn der Raspberry Pi dauerhaft und eine moglichst lange Zeit storungsfrei laufen soll. Ein weiterer Grund auf Swapping zu verzichten ist die begrenzte Geschwindigkeit der SD-Speicherkarten. Das macht das Swapping auf dem Raspberry Pi langsam. Man kann also unter Umstanden auf Swapping verzichten.

  * [Swapping deaktivieren](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002131.htm)

### Übersicht: Server-Sicherheit

Eine Standard-Installation eines Raspberry Pi mit Raspbian in einem lokalen Netzwerk ist von außen gesehen einigermaßen sicher. Allerdings muss man immer davon ausgehen, dass sich ein Angreifer im eigenen lokalen Netzwerk befindet oder Zugriff bekommen kann. Insbesonders dann, wenn man ein WLAN betreibt. Das Problem dabei sind nicht die ungebetenen Gaste, die sich einhacken wollen, sondern Freunde, die ihre unsicheren Clients mitbringen. Wer weiß schon, welche Trojaner und Wurmer da drauf sind und Locher in die Firewall reißen.

Die hier dargestellten Sicherheitsprobleme sind in ihrer Schwere in gewisser Weise Ansichtssache. Deshalb muss man den Losungen hier nicht zwangslaufig folgen. Es gibt allerdings Konstellationen, bei denen man die beschriebenen Sicherheitsprobleme nicht ignorieren darf. Insbesondere dann nicht, wenn man den Raspberry Pi dauerhaft betreibt und er auch noch aus dem Internet erreichbar ist. Aber auch dann, wenn der Raspberry Pi nur im lokalen Netz erreichbar ist, sollte man sich um eine hohere Sicherheit bemuhen, weil man davon ausgehen muss, dass sich ein Angreifer Zugang zum lokalen Netz verschaffen kann oder im schlimmsten Fall schon verschafft hat.

  * Root-Zugriff
  * Standard-Benutzer und -Passworter
  * Nicht benotigte Software
  * Aktualisierung vornehmen
  * SSH-Zugang

Hinweis: Nicht alle hier dargestellten Sicherheitsprobleme stellen ein echtes Problem dar. Und auch nicht alle Maßnahmen machen in jedem Fall Sinn. Und die Losungen und Vorschlage sind auch nicht in Stein gemeißelt. Man muss schon nach der Verhaltnismaßigkeit schauen. Manche Maßnahmen konnen auch dazu fuhren, dass man sich aussperrt, dass man sich ein bereits funktionierendes und konfiguriertes System zerschießt, was auch nicht die Losung sein kann.  
Es ist nicht notwendig, einen Raspberry Pi in einen Hochsicherheitsbereich zu verwandeln. Es reicht in der Regel aus, ein paar Abwehr- oder Sicherheitsmaßnahmen einzurichten, um den Aufwand fur Eindringlinge zu erhohen und den Server unattraktiv zu machen. In der Regel setzen Eindringlinge ihre Ressourcen dann bei einfacher anzugreifenden Opfern ein.

### Sicherheitsproblem: Root-Zugriff

Der Benutzer "root" ist ein Standard-Benutzer, der sich in jedem Linux-System befindet. Dieser Benutzername ist nicht nur bekannt, sondern auch noch mit uneingeschrankten Rechten ausgestattet. Jetzt braucht man nur noch das Passwort, was sich mit ausreichend Zeit, auch automatisiert, herausfinden lasst.

Was Root-Zugriffe auf ein System angeht, kann man geteilter Meinung sein. Es gibt die Ansicht, dass man einen Server als kompromittiert ansehen muss, wenn ein Eindringling mit einer beliebigen Identitat Root-Zugriff erlangen kann.  
Bei einem Raspbian ist es so, dass der Standard-Benutzer "pi" jederzeit Root-Rechte per "sudo" erhalten kann. Und das ohne Eingabe des Root-Passworts. Es kann sinnvoll sein dieser Konstellation einen Riegel vorzuschieben. Der Benutzer, aber auch der Angreifer, brauchen dann zwei Passworter. Einmal das des Benutzers und dann noch das Passwort von "root", sofern er Root-Rechte haben will.

  * [Root-Zugriff einschranken](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002231.htm)

### Sicherheitsproblem: Standard-Benutzer und Standard-Passworter

Die standardmaßig angelegten Benutzer und dazugehorigen Standard-Passworter in Linux-Distributionen sind aus Sicht eines Angreifers eine feine Sache. Sie erleichtern den Zugriff. Da Standard-Benutzer- und -Passworter dokumentiert sind, stellen sie ein erhebliches Sicherheitsrisiko dar.  
Bei Raspbian ist fur den Benutzer "root" kein Passwort festgelegt und damit kein Zugang moglich, es sei denn, man hat das nachtraglich geandert. Fur den Benutzer "pi" ist "raspberry" als Standard-Passwort festgelegt. Generell wird empfohlen bei der Erstkonfiguration fur den Benutzer "pi" ein neues Passwort zu vergeben. Wenn man das nicht macht, dann riskiert man, dass es ein Angreifer schafft, mit dem Benutzer "pi" und dem Standard-Passwort "raspberry", Zugriff zu erhalten.

Man muss das nicht als ernsthaftes Problem sehen. Es kommt auf die Nutzung des Raspberry Pi an. Nur soviel sei erwahnt, dass es einige Tutorials gibt, die den Raspberry Pi zum VPN-Gateway oder WLAN-Access-Point machen. Man sollte sich daruber im Klaren sein, dass der Raspberry Pi dabei unter Umstanden per SSH von extern erreichbar ist. Dabei reißt man sich mit SSH eine Sicherheitslucke ins Netzwerk, wenn ein standardmaßig angelegter Benutzer ein Standard-Passwort aufweist. Insbesondere der Benutzer "pi" ist gefahrdet, weil der immer vorhanden ist.

Standard-Benutzernamen mit Standard-Passwortern sind typische Sicherheitslucken. Schlimmer sind nur noch Passworter, die man nicht andern kann.

  * [Standard-Benutzername und Passwort andern](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002241.htm)

### Sicherheitsproblem: Nicht benotigte Software

Der sichere Betrieb eines Raspberry Pi als Server bedingt, dass darauf nur die Anwendungen installiert sind, die fur den Betrieb notig sind. Eine Standard-Distribution, wie zum Beispiel Raspbian, bildet fur den Betrieb eines Servers eigentlich keine gute Basis, weil hier schon so viel vorinstalliert ist, von dem man im Detail nichts weiß und was man nicht unter Kontrolle hat.  
Allerdings stellen die ungenutzten Anwendungen erst einmal kein Sicherheitsproblem dar. Allerdings kann man nicht ausschließen, dass ein Angreifer nicht doch einen Weg findet, uber eine ungenutzte Anwendung eine Sicherheitslucke auszumachen und auszunutzen. Deswegen scheidet eine Standard-Distribution als Server-Betriebssystem eigentlich aus.  
Empfehlenswert ist eine spezielle Server-Distribution oder ein Minimal-Image einer Linux-Distribution.

  * [Minimal-Raspbian installieren](https://www.elektronik-kompendium.de/sites/raspberry-pi/1907011.htm)

Ein Server sollte in der Regel nur genau die Software enthalten, die er zur Erfullung seiner Aufgabe benotigt, jedes weitere Paket stellt ein potenzielles Sicherheits- oder Performancerisiko dar.  
Alle Komponenten, die nicht gebraucht werden, sollten abgeschaltet, besser deinstalliert werden, um Eindringlingen moglichst wenig Angriffsflache zu bieten.

  * [Minimal-Raspbian erzeugen](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002111.htm)

### Sicherheitsproblem: Veraltete Software

Wenn ein Angreifer uber die ublichen Authentifizierungswege nicht in ein System reinkommt, dann wird er die Implementierung auf Schwachstellen abklopfen. Beispielsweise in dem er sich uber aktuelle Sicherheitslucken in der Version der Implementierung informiert. Neue Versionen werden generell mit Bug-Fixes zu beschriebenen Sicherheitslucken veroffentlicht. Angreifer nutzen diese Informationen, um im Internet nach Servern und Software zu suchen, die diese Lucken aufweisen.  
Deshalb sei angeraten regelmaßig neue Aktualisierungen einzuspielen. Es mag dann zwar sein, dass die neue Version auch Sicherheitslucken enthalt, aber das ist ja dann noch nicht bekannt. Wenn dann welche bekannt werden, kommt in der Regel zeitnah eine neue Aktualisierung heraus, die das Problem lost. Wenn man standig seine eingesetzte Software auf den neusten Stand hat, hat man Software-seitig ein ziemlich sicheres System.  
Wer sein System nicht laufend aktuell halt, dem muss klar sein, dass er sein System mit Sicherheitslucken betreibt.

Bei jedem Update besteht naturlich auch immer die Gefahr, dass man sich Funktionsstorungen einhandelt. Vor allem bei wichtigen Systemen mochte man das vermeiden. Die Frage ist, wie viel Aufwand zieht es nach sich, wenn ein Eindringling Schaden verursacht hat.  
Ein Mittelweg mag sein, dass man keine automatischen Updates macht, sondern regelmaßige Termine fur die manuelle Auslosung setzt und dabei berucksichtigt, dass man zum anschließenden Prufen und Beseitigen von Problemen noch etwas Zeit einplant.

  * [Betriebssystem und Software aktualiseren](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002041.htm)

Alternativ kann man zumindest Sicherheitsupdates automatisch einspielen lassen.

Dann sollte man noch einen kritischen Blick auf die Paketquellen werfen.

  * [Paketquellen prufen und andern](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002201.htm)

### Sicherheitsproblem: SSH-Zugang

Standardmaßig ist auf einer Linux-Distribution fur den Raspberry Pi, wie zum Beispiel Raspbian, ein SSH-Server aktiv. Der ermoglicht es, dass man sich mit einem SSH-Client von einem anderen System uber das Netzwerk auf den Raspberry Pi per SSH einloggt, ohne direkt mit Tastatur und Bildschirm am Raspberry Pi zu sitzen.

Dieser Remote-Zugriff auf den Raspberry Pi ist standardmaßig aber alles andere als sicher. Auch wenn SSH (Secure Shell) das anders suggeriert. Es kommt auch auf eine sichere Konfiguration an. Die ist in der Standard-Installation komfortabel eingerichtet, allerdings nicht darauf ausgelegt, dass der Raspberry Pi als Server, Gateway oder Router Kontakt zur Außenwelt hat.

Wenn ein Raspberry Pi als Server, Gateway oder Router vom Internet aus erreichbar ist, dann sollte man sich um zusatzliche Sicherungsmaßnahmen fur den SSH-Zugang kummern. Das ist wichtig und dringend. Ein als Server, Gateway oder Router betriebener Raspberry Pi mit einem Standard-Raspbian ist nicht sicher.

  * [SSH-Server auf dem Raspberry Pi absichern](https://www.elektronik-kompendium.de/sites/raspberry-pi/2006101.htm)

### Sicherheitshinweis zum Schluss

Ein Server, Gateway oder Router ist nur so sicher, wie der PC, von dem er administriert wird. Ein Trojaner auf diesem PC kann ein Einfallstor fur den gut geschutzten Server sein.

### Erweiterung: Fernwartung und Remote-Service

### Weitere verwandte Themen:

### Produktempfehlungen
