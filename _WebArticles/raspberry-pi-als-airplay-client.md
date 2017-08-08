# Raspberry PI als AirPlay Client

_Captured: 2017-05-06 at 16:58 from [www.welzels.de](http://www.welzels.de/blog/projekte/raspberry-pi/raspberry-pi-als-airplay-client/)_

Dieser Artikel ist nicht mehr aktuell, ich empfehle den folgenden Artikel: [Raspberry Pi als AirPlay Client [Update]](http://www.welzels.de/blog/2014/12/raspberry-pi-als-airplay-client-update/)

Der Raspberry PI eignet sich auch als AirPlay Empfanger, einfach ein paar alte aktiv Lautsprecher anschließen fertig. Aber ist das gunstiger und besser als ein kommerziell erhaltliches Gerat zu kaufen? Dazu spater erst einmal die Installation.

Bevor neu Pakete installiert werden sollte die Paketdatenbank auf den neusten Stand gebracht werden:

Anschließend mussen die folgenden Pakete installieren werden:

Benotigt wird noch das Perl Modul NET::SDP:

Ggf. muss die Installation zweimal durchgefuhrt werden, da _cpan_ beim ersten mal sagt: _„Warning: Cannot install NET::SDP, don't know what it is."_

Shairport existiert nicht als Raspbian Packet, das Quell-Paket kann aber von GIT geladen werden:

Nach dem Shairport geladen wurde, muss es noch kompilieren werden:

Da Shairport nicht aus der Raspbian Repository stammt, installiere ich es in das Verzeichnis „/opt":

Dies erleichtert die Wartung des System und es kann, wenn es nicht mehr benotigt wird, einfach geloscht werden.

Shairport installiert nicht automatisch ein Startskript, hat aber eines im Installationsverzeichnis. Dieses wird in das Verzeichnis „/opt/shairport/etc" kopiert:

Innerhalb des Init-Skriptes mussen noch die Zeilen 20 und 22 angepasst werden. Zeile 20 ist notwendig, da es nicht im Wurzelverzeichnis sonder in „/opt/shairport" liegt. In Zeile 22 wird mit „$HOSTNAME" festgelegt unter welcher Name der Raspberry PI spater, als AirPlay Gerat, erreichbar ist. Es kann hier auch ein anderer Name angegeben werden.

Zum Schluss muss noch der Dienst erzeugt werden, damit Shairport nach dem Booten automatisch gestartet wird:

Den Dienst dann uber sudo service shairport start starten oder den Raspberry PI neu booten. Danach kann die Musik uber iTunes, iPhone oder iPad an den Raspberry PI gesendet werden.

![AirPi-iPhone](http://www.welzels.de/blog/wp-content/uploads/2013/01/AirPi-iPhone-200x300.png)

![AirPi-iTunes](http://www.welzels.de/blog/wp-content/uploads/2013/01/AirPi-iTunes-300x200.png)

Durch Eingabe des folgenden Befehls konnen die Kanale, der internen Sound-Karte ausgewahlt werden:

Die moglichen Optionen fur die Autioausgabe sind:

  * Auto: 0
  * Kopfhorer (3,5 Klinke): 1
  * HDMI: 2

Leider hat die analoge Ausgabe eine sehr schlechte Qualitat. Das Audio-Signal wird nicht mittels DAC gewandelt, sonder es handelt sich um ein PWM Signal.

Um die analoge Audio-Ausgabe zu verbessern wird dann schon eine externer USB Sound-Karte benotigt. Damit diese funktioniert musste habe ich die Alsa Konfigurationsdatei folgendermaßen angepasst:

**Mein Fazit bezuglich dieser Anwendung des Raspberry PI:**

Ein Apple TV kostet rund 100€ und eine AirPort Express Basisstation ca. 90€, das sind die Gerate mit denen sich der, ich nenne ihn mal AirPi, messen lassen muss. Nun der Raspberry PI kostet rund 33€ (RS-Online). Aber das sind ja noch nicht alle Kosten. Also rechne ich mal zusammen:

[Raspberry PI](http://raspberrypi.rsdelivers.com/default.aspx?cl=1)
32,88 €

[Gehause](http://raspberrypi.rsdelivers.com/product/rs/raspberry-pi-type-b-case-white/casewht.aspx)
6,07 €

[4GB SD Card](http://www.amazon.de/SanDisk-Capacity-Speicherkarte-original-Handelsverpackung/dp/B000WQKOQM/ref=sr_1_2?m=A3JWKAKR8XB7XF&s=ce-de&ie=UTF8&qid=1357245745&sr=1-2)
8,36 €

[USB 2.0 HUB mit Netzteil](http://www.amazon.de/LogiLink-4-Port-Hub-Netzteil-schwarz/dp/B003ECC6O4/ref=sr_1_4?m=A3JWKAKR8XB7XF&s=ce-de&ie=UTF8&qid=1357246190&sr=1-4)
11,78 €

[Micro USB Kabel](http://www.amazon.de/AmazonBasics-2-0-Kabel-A-Stecker-Micro-B-Stecker-Meter/dp/B003ES5ZSW/ref=sr_1_2?s=ce-de&ie=UTF8&qid=1357246285&sr=1-2)
5,99 €

[Wireless LAN USB Adapter](http://www.amazon.de/EDIMAX-EW-7811UN-Wireless-Adapter-IEEE802-11b/dp/B003MTTJOY/ref=pd_bxgy_computers_img_y)
12,95 €

[USB Sound Karte](http://www.amazon.de/Creative-Soundblaster-Play-Soundkarte-extern/dp/B0028RZ23I/ref=sr_1_1?s=computers&ie=UTF8&qid=1357247403&sr=1-1)
19,25 €

Summe
97,28 €

Somit hatte man auch gleich ein AppleTV oder die gunstigere AirPort Express Basisstation kaufen konnen. Was noch hinzukommt, es ist ein ziemlicher Kabelsalat, da das ganze aus zwei Geraten besteht, USB-Hub und Raspberry PI. Ein Steckernetzteil versorgt den USB-Hub, ein microUSB Kabel geht vom USB-Hub zum Raspberry PI, um diesen mit Spannung zu versorgen. Der Wireless LAN Adapter kann direkt am PI angeschlossen werden, allerdings nicht die USB-Soundkarte. Zieht dann zuviel Strom, sie muss am USB-Hub angeschlossen werden. Das heißt von dem zweiten USB-Anschluss des PI muss ein weiters Kabel zu dem USB-Hub gezogen werden. Das ganze nur weil ein 2€ DAC fehlt, schade.

Anders sieht es aus, wenn der HDMI-Ausgang als Schnittstelle zum Verstarker genutzt werden kann. Es sind dann lediglich 60,26€, hinzu kommen dann noch ca. 5€ fur ein Netzteil, also rund 65€ und es ist nur ein Gerat ohne Kabelsalat. Jedoch stellt sich dann die Frage ob nicht RaspBMC die Richtige Anwendung ist. Das ist aber ein Thema, dem ich mich ein andermal widmen werde.

Damit hier kein falscher Eindruck entsteht! Ich finde den Raspberry PI sehr gelungen und mochte ihn auf keinen Fall schlecht machen. Aber fur diese Anwendungen gibt es bessere, bereits fertige, kommerzielle Losungen.
