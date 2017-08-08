# Multiroom Wlan Lautsprecher im Eigenbau

_Captured: 2017-05-01 at 17:03 from [blog.johjoh.de](http://blog.johjoh.de/multiroom-wlan-lautsprecher-im-eigenbau/)_

![](https://i0.wp.com/blog.johjoh.de/wp-content/uploads/2015/12/2376-eva1-e1453481961413.jpg?resize=634%2C372)

> _Anleitungen, Artikel, Multiroom Audio, Raspberry PI, Squeeze Clients_

Beiden Multiroom System ist Bewegung in den Markt gekommen. Immer mehr Hersteller ([siehe Artikel Multiroom System](http://blog.johjoh.de/multiroom-system/)) kommen auf dem Markt. Leider sind die Preise immer noch unverschamt hoch und die Qualitat ist mehr Mittelmassig oder das System ist in sich so weit geschlossen, das man keinerlei Flexibilitat hat. Auch das Handling ist nicht immer wie man so schon sagt, Benutzer orientiert ausgelegt.

Lidl hat im aktuellen Prospekt 05.12.2015 die Serie von SilverCrest mit 4 Varianten im Angebot. Von 60 € bis 130 € je Lautsprecher sind das schon sehr gunstige Preise. Die Leistung erstreckt sich von 18W bis 35W. Da stellt sich nur die Frage wie lange diese im Markt verfugbar sind. Wenn man sein System erweitern mochte, sollte man darauf achten , dass das System auch langfristiger verfugbar ist.

So ist eine Opensource System wie hier beschrieben, langfristig gesehen, die bessere Wahl und die Qualitat des Klangs kann man selber bestimmen.

Fur manche mag Multiroom neu sein, aber da man von einem Zentralen Instanz an X Ausgabe Gerate, Videos oder Audio senden kann ist nicht neu. Logitech hat dieses bereits 2001 mit der Squeeze Serie sehr gut umgesetzt ([siehe Wikipedia](https://de.wikipedia.org/wiki/Squeezebox)). Neben Software gab es eine Reihe von Hardware Player, Boxen etc. die alle getrennt oder auch als ein Verbundsystem (Multiroom) laufen konnten. Das ganze zentral gesteuert, per APP, oder Web Interface. Auch andere Dienste wie Napster, Spotify, WebRadio konnten mit eingebunden werden.

2012 wurde die Serie von Logitech komplett eingestellt. Die Software wurde als Opensource zur Verfugung gestellt. Die hat nun die freie Gemeinde von Entwicklern auf die Idee gebracht das ganze weiter zu entwickeln. Unter anderen gibt es auch viele SoftClient wie der Squeezelite, der unter anderen auf dem Raspberry lauft. Diese habe ich jetzt schon mehrfach im Einsatz, hatte er immer die Herausforderung wie die Musik ausgegeben wird.

Im Artikel [HDMI Audio Ausgabe fur den Raspberry-PI ](http://blog.johjoh.de/hdmi-audio-ausgabe-fuer-den-raspberry-pi/)bin ich schon auf einige Moglichkeiten eingegangen. Aber das Thema Verstarker und Lautsprecher war immer nur Semiprofessionell umgesetzt… aber Funktional.

Mit dem HiFiBerry AMP+ bietet sich da neue Moglichkeiten, ein LAN oder auch W-Lan Lautsprecher umzusetzen fur wenig Geld.

Zum Einsatz kommt der neue HiFiBerry AMP+ fur den Raspberri B oder B+. Das Modul wird huckepack auf dem Erweiterungs-Steckplatz des Raspberry gesteckt und bietet folgende Leistungs-Merkmale:

**HiFiBerry AMP+ Daten:**

  * ![](https://i2.wp.com/blog.johjoh.de/wp-content/uploads/2015/12/HifiBerry.jpg?resize=248%2C300)

DA-Wandlung mit Sample-Raten 44,1/48 kHz
  * Integrierter DAC
  * Voll digitale Audioverarbeitung
  * Leistungsfahiger Spannungsregler, versorgt auch den Raspberry Pi mit, so benotigt man nur ein Netzteil (12-18 V DC) fur beide Boards
  * GPIO-Modul zum direkten Aufsetzen auf den Raspberry Pi
  * Mit den Raspberry Pi Versionen A+, B+ und 2 B kompatibel
  * Class-D-Digitalverstarker, max. 25 W an 4 Ω bzw. max. 17 W an 8 Ω

Die 25 W bzw. 17 W horen sich nicht viel an, aber mit dem hohen Wirkungsgrad eines Klass D Verstarkers, reicht das um einen Raum gut auszufullen. Kombiniert mit einem Subwoofer solle das ausreichend sein.

Der Weitere Vorteil ist das der Raspberrry uber den Hifiberry mit Strom versorgt wird und kein zweites Netzteil benotigt wird.

![20151203_174247](https://i2.wp.com/blog.johjoh.de/wp-content/uploads/2016/01/20151203_174247.jpg?resize=300%2C169)

Zu den Kosten:

1 Raspberry 27 € ([Amazon](http://www.amazon.de/gp/product/B00T2U7R7I/ref=as_li_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B00T2U7R7I&linkCode=as2&tag=johjoh-21))

1 Hifiberry AMP+ 79 € ([Amazon](http://www.amazon.de/gp/product/B00UTV03G6/ref=as_li_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B00UTV03G6&linkCode=as2&tag=johjoh-21))

8 10mm M3 Abstandshalter+4 M3 Muttern 0,30€

Netzteil 12V 60W ca 20.00€

Lautsprecher 50 € ([Amazon](http://www.amazon.de/gp/product/B00W7DMF6U/ref=as_li_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B00W7DMF6U&linkCode=as2&tag=johjoh-21))

**Gesamt ca.: 177 € **(etwas teurer als bei Silvercraft, aber die Lautsprecher haben da den besseren Klang)

Bei Sonos geht es erst bei 300 € los und nach oben sind keine grenzen gesetzt. Das Modul habe ich mit Abstandshalter (10mm M3) fur 30 Cent auf den Raspberry geschraubt damit die beiden Platinen eine

![20151203_174425](https://i2.wp.com/blog.johjoh.de/wp-content/uploads/2016/01/20151203_174425.jpg?resize=300%2C169)

stabile Verbindung haben und die Mechanische Belastung am Pfostenstecker nicht so groß ist. Der kleine Doppeldecker wird dann im Lautsprecher Platz finden. Dazu habe ich die Kunststoff Abdeckung bzw Halterung der Lautsprecher Klemmen ausgebaut und ein Loch hinein geschnitten. Der Profi bekommt jetzt bestimmt eine Krise da der Lautsprecher jetzt nicht mehr in sich geschlossen ist. Ich habe da aber fur mich keinen Unterschied horen konnen. Durch die Fugen kommt Luft durch, aber das kann man auch gut als Beluftung fur den PI dann gebrauchen. Der Raspberry wurde uber die Abstandshaltern und M3 Schrauben auf 2 Kunstoffschienen geschraubt. Diese wurden dann an die Halterung geklebt. Wenn man naturlich an den PI oder am die Flash Karte mochte fuhrt kein anderer Weg vorbei als die Lautsprecher Klemmen Abdeckung mitsamt dem Raspberry auszubauen.

Dann habe ich noch eine Buchse fur die Stromversorgung eingebaut und dies mit dem HifiBerry uber die Schraubanschlussen verbunden. Alternativ stellt der HififBerry auch einen Standard Anschlussbuchse zur Verfugung. Das Interne Lautsprecherkabel wird direkt an den HifiBerry angeschlossen. Der zweite Kanal geht wie auf dem Bild unten zu sehen ist nach aussen. Von dort aus kann das Kabel zum 2. Lautsprecher gelegt werden.

![20151203_182057](https://i1.wp.com/blog.johjoh.de/wp-content/uploads/2016/01/20151203_182057.jpg?resize=300%2C169)

Jetzt noch das Ganze in den Lautsprecher eingebaut und fertig. Als Image habe ich mir wie immer [Raspbian Wheezy](https://www.raspberrypi.org/downloads/raspbian/) genommen. Dann muss noch der HifiBerry eingerichtet werden. Dazu sind einige Schritte notig, unter anderen auch die Firmware zu aktualisieren. Alternativ wenn kein LAN Anschluss vorhanden ist, kann auch ein W-Lan Stick genommen werden. Je nach Empfang sollte aber ein Stick mit externer Antenne genommen werden. D

amit wird dann nur noch ein Strom Anschluss benotigt.

![Lautsprecher mit eingebauten W-Lan](https://i1.wp.com/blog.johjoh.de/wp-content/uploads/2016/01/20151203_182625.jpg?resize=300%2C169)

> _Lautsprecher mit eingebauten W-Lan_

Dann erst mal den Squeezelite Client installiert ([siehe hier](http://blog.johjoh.de/squeezelite-auf-den-raspberry-installieren/)).

Danach werden wir den HifiBerry AMP + einrichten. In der Datei /etc/modules folgende Zeile auskommentieren. _sudo nano /etc/modules_
    
    
    snd_bcm2835

in
    
    
    #snd_bcm2835

Danach folgendes am Ende der Datei /boot/config.txt eintragen. _sudo nano /boot/config.txt_
    
    
    dtoverlay=hifiberry-amp

Um die Klangqualitat noch zu verbessern empfehle ich einen Equalizer zu installieren.
    
    
    sudo apt-get install -y libasound2-plugin-equal
    sudo nano -c /etc/asound.conf
    
    
    ctl.equal {
      type equal;
      controls "/home/pi/.alsaequal.bin"
    }
    pcm.plugequal {
      type equal;
      slave.pcm "_**plughw:0,0**_";
      controls "/home/pi/.alsaequal.bin"
    }
      pcm.equal {
      type plug;
      slave.pcm plugequal;
    }

Im start Script vom Squeezlite dann die Soundkarte umstellen auf:

`SL_SOUNDCARD=``"equal"`

Fur alle die wegen dem Stromverbrauch sich Sorgen machen konnen beruhigt sein. Der Raspberry verbraucht im Leerlauf gerade mal 1 W….
