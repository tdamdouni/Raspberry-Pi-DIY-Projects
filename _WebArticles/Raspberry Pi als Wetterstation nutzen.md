# Raspberry Pi als Wetterstation nutzen 

_Captured: 2015-12-25 at 10:06 from [www.tecchannel.de](http://www.tecchannel.de/pc_mobile/peripherie/2064103/raspberry_pi_als_wetterstation_nutzen/)_

Im Elektrohandel und in Baumarkten konnen Sie zwischen einer ganzen Reihe von Wetterstationen der unterschiedlichsten Auspragungen wahlen. Die verschiedenen Modelle arbeiten alle nach dem gleichen Funktionsprinzip. Eine Reihe von Sensoren ubertragen die Messergebnisse drahtlos an die Basisstation. Diese zeigt dann automatisiert die Ergebnisse der verschiedenen Sensoren und meist auch die jeweils gemessenen Maximal- und Minimalwerte. Üblicherweise ist das dann auch bereits der gesamte Funktionsumfang.

Wer die Wetterdaten uber einen langeren Zeitraum auswerten mochte, hat nur selten die Moglichkeit dazu. Aufpassen mussen Sie beim Kauf auch, wenn Sie an mehreren Orten Daten erheben wollen. Denn zusatzliche Empfanger sind haufig ubermaßig teuer. Apropos Empfanger: Temperatur und Luftfeuchte gehoren zum Standard. Die Messung der Windgeschwindigkeit oder auch Niederschlagsmenge sind dann wieder den teureren Stationen vorbehalten. Der Raspberry Pi bringt alle Voraussetzungen fur die Kernkomponente einer Wetterstation mit.

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2525465/522x294.png)

> _Raspberry Pi in der Praxis_

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2518726/522x294.png)

Das Projekt[ Air Pi](http://airpi.es/) hat gleich aus mehreren Grunden fur einiges Aufsehen gesorgt. Zum Einen, weil es einigen britischen Schulern initiiert wurde. Zum Zweiten, weil die Grundausstattung zuerst fur knapp 78 Euro ohne den Raspberry angeboten wurde, auch wenn dieser Preis inzwischen nicht mehr gehalten werden kann. Vor allen Dingen aber deshalb, weil die vorgestellte Losung nahezu alle Daten der Atmosphare messen und protokollieren kann.

Eine Liste der erforderlichen Komponenten inklusive Bauanleitung und Bezugsquellen finden Sie ebenfalls auf der Homepage. Demnachst soll auch ein kompletter Bausatz uber die Website angeboten werden. Zur Zeit werden hier aber nur Vorbestellungen entgegengenommen. Der Preis fur alle Komponenten zusammen soll bei umgerechnet etwa 110 Euro liegen. Dazu kommen dan noch die Kosten fur den Raspberry Pi von etwa 35 Euro.

Um Air Pi zu nutzen und zusammenzubauen, sollten Sie sich selbst als fortgeschrittener Bastler einstufen. Außerdem brauchen Sie auch eine Portion Geduld. Denn bis Sie alle notwendigen Teile besorgt haben, dauert es schon ein paar Tage.

Und Sie mussen in der Lage sein, Schaltplane lesen zu konnen, und auch der Umgang mit dem Lotkolben darf Ihnen keine besonderen Schwierigkeiten bereiten.

Air Pi misst bei Nutzung aller Boards und angeschlossenen Sensoren nicht nur die Lufttemperatur, sondern auch die Luftfeuchtigkeit, den Anteil an CO2 und Stickstoff in der Luft sowie die UV-Strahlung. Gerade diese vielen unterschiedlichen Parameter, die gemessen und protokolliert werden, erweitern das Einsatzgebiet uber eine Wetterstation hinaus. Denn die Daten lassen auch Ruckschlusse uber das Raumklima in den eigenen vier Wanden zu.

Air Pi verwendet den Raspberry Pi als zentrales Element. Die einzelnen Sensoren ubermitteln die Messwerte unmittelbar an das Gerat. Zusatzliche Platinen mussen mit der zentralen Einheit verbunden werden, dabei soll das System aber trotzdem klein und handlich bleiben. Deutlich einfacher wird es, wenn der Ein-Platinen-Rechner lediglich als Datensammler und fur die Auswertungen genutzt wird, die Daten selbst aber von einzelnen Empfangern erhoben und dann drahtlos an eine Steuereinheit ubermittelt werden. Wer mochte, kann seine Messergebnisse auch in Echtzeit auf [http://airpi.es](http://airpi.es/) veroffentlichen.

### USB-Wetterdaten-Empfanger nutzen

In Elektronikmarkten und auch deren Online-Shops finden Sie Funkempfanger, die sich per USB-Anschluss mit einem PC verbinden lassen (> Kasten "Mehr Infos zu den Wetterstationen"). Die Empfanger erhalten die Daten per Funk von Sensoren und ubermitteln diese dann an den PC.

Nehmen Sie die Sensoren und den Empfanger entsprechend der mitgelieferten Dokumentationen in Betrieb. Verbinden Sie dann den Empfanger per USB-Kabel mit dem Raspberry Pi. Versorgen Sie den kleinen Computer anschließend mit Strom, und lassen Sie das Betriebssystem starten. Die nachfolgenden Kommandos beziehen sich auf Raspbian, das alle Grundlagen fur den Betrieb mitbringt.

Loggen Sie sich per SSH auf dem Raspberry ein oder schließen einen Monitor an, damit Sie sich als Benutzer auf dem Rechner anmelden konnen. Öffnen Sie eine Konsole, und geben Sie dort das Kommando ein:

`sudo dmesg`

Sie erhalten damit eine Ruckmeldung der Gerate, die am USB-Port ermittelt worden sind. Suchen Sie dort nach einem Eintrag, der auf den angeschlossenen Funkempfanger hindeutet, zum Beispiel "Wetterdatenempfanger" oder den Herstellernamen. Falls Sie hier keinen Eintrag finden, unterbrechen Sie die Verbindung erneut und stopseln das Gerat erneut an, um zu sehen, ob es dann zu einer Meldung kommt. Schauen Sie auf den Seiten des Herstellers nach, ob es dort Hinweise gibt oder vielleicht sogar einen Treiber. Allerdings sollten tiefergehende Probleme eher die Ausnahme sein, da rein technisch ein solcher Empfanger recht einfach konstruiert ist.

Sofern das Kommando zeigt, dass die Verbindung mit dem Raspberry funktioniert, brauchen Sie ein Programm, das in der Lage ist, die ubertragenen Daten auszulesen. Hier bietet sich [Socat](http://www.dest-unreach.org/socat) an. Es fragt die Schnittstellen ab und gibt auf der Konsole die Ergebnisse aus. Installieren Sie die Software mit:

`sudo apt-get install socat`

Um an die Messwerte zu gelangen, mussen Sie die Schnittstelle abfragen:

`sudo socat /dev/ttyUSB1,b9600 STDOUT`

In diesem Beispiel ist der Empfanger mit der Schnittstelle USB1 verbunden. Als Ruckmeldung erhalten Sie zum Beispiel:

`$1;1;;;- 0,9;;;17,6;;;;;75;;;59;;;;;;;;;0`

Wenn auf den ersten Blick zunachst nichts zu passieren scheint, ist das kein Grund zur Besorgnis. Das Abfragen per Schnittstelle kann bis zur ersten Übertragung durchaus ein paar Minuten dauern. Das Ergebnis sieht auf den ersten Blick wenig aufregend aus, liefert aber die Grundlage fur die weiteren Schritte. In Abhangigkeit der Software, mit der Sie die Daten auswerten oder aufbereiten wollen (> Kasten), wird der Funktionsaufruf in ein Script gepackt oder die Ausgabe in eine andere Datei umgeleitet, die sich dann automatisiert importieren lasst.

### Mehr Infos zu den Wetterstationen

Viele Anwender haben gute Erfahrungen mit dem Funkempfanger aus dem Hause ELV gemacht (USB-Wetterdaten-Empfanger USB-WDE1). Die Grundeinheit kostet weniger als 30 Euro, Außen- und Innensensoren liegen zwischen 30 und 50 Euro. Damit ist die gesamte Station dann teurer als Air Pi, aber auch viel schneller einsatzbereit.

**Alles auf einen Blick:** Mit dem Raspberry Pi erfasste Daten werden fur eine Langzeitaufzeichnung in eine Datenbankdatei geschrieben. Sie lassen sich dann mit einem Programm wie Rrdtool grafisch aufbereiten.

Eine Moglichkeit, aus den ubermittelten Daten grafische Auswertungen zu schaffen, ist der Einsatz von [Rrdtool](http://www.mrtg.org/rrdtool). Fur Debian wird ein Binarpaket angeboten, das Sie also schnell installieren konnen. Auf der Seite des Projekts finden Sie eine Reihe von Tutorials, mit deren Hilfe Sie Schritt fur Schritt lernen, wie Sie eine Datenbank anlegen und die Messwerte in regelmaßigen Abstanden abfragen.

Zur Auswertung der Messungen mit Air Pi und zur Steuerung benotigen Sie eine spezielle Software. Deren Quellcode wurde auf Github veroffentlicht und kann uber <https://github.com/tomhartley/AirPi> eingesehen und heruntergeladen werden. (hal)
