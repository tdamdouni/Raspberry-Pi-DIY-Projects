# Raspberry Pi als AirPlay Client [Update]

_Captured: 2017-05-06 at 16:56 from [www.welzels.de](http://www.welzels.de/blog/2014/12/raspberry-pi-als-airplay-client-update/)_

Seit dem letzen Beitrag „[Rasspberry Pi als AirPlay Client](http://www.welzels.de/blog/projekte/raspberry-pi/raspberry-pi-als-airplay-client/)" ist schon etwas Zeit vergangen, und jetzt einfach uberall Update reinzuschreiben, wo es Änderungen gegeben hat macht auch kein Sinn. Auch stimmt die Rechnung, ob ein Apple TV nun gunstiger ist, nicht mehr. Zwar wird fur den analogen Audioausgang noch immer ein pulsweiten moduliertes Signal (PWM), anstelle eines Digital-Analog-Wandlers (DAC) verwendet, aber wen das stort, muss eben eine USB-Soundkarte anschließen. Ich mochte gar nicht lange um audiophile Philosophien herumreden, in erster Linie geht es ja um den Spaß.

## Vorbereitung

Zunachst benotigt man einen einen Raspberry Pi. Es ist egal, ob nun die Version B oder [B+](http://www.amazon.de/gp/product/B00LPM6U06/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00LPM6U06&linkCode=as2&tag=wwwwelzelsde-21&linkId=F54KSHUSGZCK7X5B) eingesetzt wird, die Version des [Raspberry Pi A+](http://www.amazon.de/gp/product/B00Q8MM4PI/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00Q8MM4PI&linkCode=as2&tag=wwwwelzelsde-21&linkId=LDO4GYZ4XX7ZIKTA) ist zwar ebenfalls in der Lage die Aufgabe zu ubernehmen, allerdings ist aufgrund der fehlenden Netzwerkschnittstelle die Installation etwas schwieriger. Ein Moglich ist naturlich alles auf einem B+ zu installieren und die [SD-Karte](http://www.amazon.de/gp/product/B002NTW99G/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B002NTW99G&linkCode=as2&tag=wwwwelzelsde-21&linkId=JEJCKZZMYJ6MCP5M) spater in einen A+ zu stecken. Ein weitere Moglichkeit ist die Installation uber einen UART zu USB Konverter (FTDI TTL-232R-3V3) und einem Wlan Adapter.

Egal fur welches System man sich entscheidet, die installierte Distribution muss Raspbian (Debian in der Version Wheezy) sein. Das Download und die Installationsanleitung fur das Betriebssystem finden sich auf den Projektseite <http://www.raspberrypi.org/downloads/>.

### Der erste Start

Nach dem das Betriebssystem auf das Board ubertragen wurde mussen zunachst einige Einstellungen durchgefuhrt werden.

#### Starten des RPI

Der Raspberry Pi (RPI) besitzt zwar ein root Account, jedoch ohne Passwort. Daher mussen wir uns zunachst als „pi" einloggen:

  * ssh pi@raspberrypi
  * Passwort: raspberry

Nach dem ersten Login sollten nun die Grundeinstellungen vorgenommen werden. Dazu gibt man den folgenden Befehl ein:

![Raspi-config01](http://www.welzels.de/blog/wp-content/uploads/2013/03/Raspi-config01-300x219.png)

  1. In dem Textmenu den ersten Eintrag wahlen um die SD-Karte vollstandig nutzen zu konnen.
  2. Das Passwort fur den Benutzer „pi", in dein beliebiges Passwort andern.
  3. Wir benotigen keinen grafischen Desktop, „Console Text console" ist die voreingestellte Option, daher muss hier auch nichts geandert werden.
  4. Die Sprach- und Landeseinstellungen: 
    1. Change Locale, sollte in Englisch belassen werden, denn sollte es mal zu einem Problem kommen, findet man mit der englischsprachigen Fehlermeldung meist einfacher die Losung als mit der deutschsprachigen.
    2. Die Zeitzone sollte auf den entsprechenden Standort eingestellt werden.
    3. Da wir uns nur remote auf dem RPI anmelden ist die Tastatureinstellung nicht notwendig.
  5. Kamera verwenden wir nicht.
  6. Rastrack muss jeder fur sich selbst entscheiden, ob er dort teilnehmen mochte.
  7. Das Overclocking ist hier nicht notwendig.
  8. Erweiterte Optionen (Advanced Options): 
    1. Overscan: Da kein Display angeschlossen ist wird diese Option nicht benotigt.
    2. Hostname: Nennen wir ihn mal „air-pi"
    3. Memory Split: Der RPI verfugt uber keinen gesonderten Speicher fur die GPU. Da keine grafische Ausgabe genutzt wird, kann der Wert auf 16 verkleinert werden.
    4. SSH: Ist bereits aktiviert und muss auch aktiviert bleiben, da wir sonst nicht mehr auf den RPI kommen.
    5. SPI: Benotigen wir nicht.
    6. I2C: Benotigen wir nicht.
    7. Serial: Wird zwar nicht benotigt (außer bei A+), kann aber nicht schaden es eingeschaltet zu lassen.
    8. Audio: Die Option 1, „Force 3.5mm (‚headphone') jack" wahlen,
    9. Update: Fuhrt den Konsolen Befehl „apt-get update" aus, das fuhren wir spater in der Konsole aus.

Nach dem die Einstellungen vorgenommen wurden, mit „finish" die Konfiguration beenden. Damit die Einstellungen ubernommen werden muss das System neugestartet werden. In der Regel wird man nach dem Verlassen dazu aufgefordert, ansonsten kann man dies mit dem folgenden Befehl durchfuhren:

Einigen Minuten warten, bis der RPI wieder gestartet ist und wieder einloggen. Je nachdem, wie schnell nun der Router registriert, das wir den Namen des RPI geandert haben mussen wir uns nun mit dem neuen oder alten Namen einloggen. Ggf. verwendet man nun erst einmal die IP-Adresse. Irgendwann taucht der richtige Name im Netzwerk auf.

### Weitere Grundeinstellungen

Erst einmal das System auf den neuesten Stand bringen:

Da das heruntergeladenen Raspbian Image mehr beinhaltet, als wir tatsachlich benotigen entfernen wir nun erst einmal den uberflussigen Ballast. Das heiß, alles was mit X zutun hat wird geloscht:

Damit sind alle X11, Xorg, LXDE etc. Pakete deinstalliert. Um nun noch die Konfigurationen zu entferne fuhren wir noch die nachfolgenden Befehle aus:

Es werden zwar auch Pakete geloscht, die wir im nachfolgenden wieder benotigen, jedoch ist es einfacher die paar Pakete spater neu zu installieren, als jedes Paket im einzelnen zu behandeln.

## Shairport installieren

Leider ist Shairport nicht in den Raspbian Paketquellen enthalten, daher mussen wir es selbst kompilieren. Zunachst benotigen wir die Quelle:

Des weitern werden noch einige Entwicklungsbibliotheken benotigt:

Nach dem alles geladen und installiert ist, wechseln wir in das Source-Verzeichnis von Shairport und fuhren das Konfigurationsskript aus:

Die Ausgabe sollte wie oben dargestellt lauten. Danach kompilieren wir Shairport und installieren es, wenn alles funktioniert hat:

Zwar ist nun alles installiert, da es sich aber um eine allgemeine Installation handelt, fehlen noch die Konfigurationsskripte fur Debian. Diese befinden sich im Verzeichnis „scripts/debian", und mussen einfach in das Verzeichnis „etc" kopiert werden:

Bevor Shairport nun gestartet werden kann muss noch ein Benutzer „shairport" angelegt werden, der Mittglied in der Gruppe „audio" ist. Da sich der Benutzer nicht anmelden muss und ein Teil des Systems steuert, legen wir ihn wie folgt an:

Bevor wir Shairport nun starten, nehmen wir noch ein paar Einstellungen vor. Konfigurationsdatei offnen:

Und wie folgt modifizieren:

Nun kann Shairport mit folgendem Befehl gestartet werden (nicht ausfuhren!):

Allerdings wird Shairport so nur manuell gestarte. Um Shairport beim Booten zu starten muss das init-Skript noch registriert werden:

Nach einem Reboot des Raspberry Pi oder dem Start des Services:

Kann uber iTunes, iPad, iPhone und iPod Touch auf dem AirPi Musik abgespielt werden. Naturlich geht das auch mit Android, davon habe ich aber keine Ahnung, deshalb einfach mal in Google Play nachschauen.

![airpi01](http://www.welzels.de/blog/wp-content/uploads/2014/12/airpi01.png)

![airpi02](http://www.welzels.de/blog/wp-content/uploads/2014/12/airpi02.png)

![airpi03](http://www.welzels.de/blog/wp-content/uploads/2014/12/airpi03-300x225.png)

Fur richtiges AirPlay fehlt noch Wlan. Da ich die Installation bereits in einem alteren Artikel beschreiben und bislang keine bessere oder einfachere Moglichkeit gefunden habe, verweise ich dafur auf [Wireless Adapter konfigurieren](http://www.welzels.de/blog/2012/12/raspberry-pi-netzwerk-und-wlan-konfigurieren/#Wireless_Adapter_konfigurieren).
