# LibreELEC 8 ist ausgegeben – einfach auf dem Raspberry Pi 3 installieren

_Captured: 2017-05-19 at 11:25 from [www.bitblokes.de](https://www.bitblokes.de/2017/02/libreelec-8-ist-ausgegeben-einfach-auf-dem-raspberry-pi-3-installieren/)_

LibreELEC 8 wurde nach zehn Alpha- und drei Beta-Versionen als stabil deklariert. Genau genommen ist es LibreELEC 8.0.0. Ich haben die Alpha- und Beta-Versionen (7.9.x) schon langer auf einem Raspberry Pi 3 verwendet und es ist bisher schon sehr gut gelaufen. LibreELEC 8.0 basiert bekanntlich auf dem Multimediasystem Kodi 17 _Krypton_, das viele Verbesserungen und Änderungen mit sich bringt.

### Änderungen in LibreELEC 8 seit der letzten Beta-Version

Die Entwickler haben diverse Fixes eingepflegt und in den entsprechenden Abbildern auf die Kernel linux-amlogic 3.10 (arm) und 3.14 (aarch64) aktualisiert. Weiterhin gibt es ein Applet, das fur das Übertakten eines Odroid-C2 notwendig ist. Wie erwartet gab es keine großartigen Neuerungen mehr.

Das Abbild von LibreELEC 8 fur herkommliche x86_64-Hardware ist 216 MByte groß. Das liegt unter dem Boot-Großen-Limit von 230 MByte mit Blick auf altere OpenELEC-Installationen. Somit musst Du fur ein Upgrade die Partitionen nicht andern oder komplett neu installieren.

Anwender von Community Builds fur Odroid-C2, WeTek Hub und Play 2 (aarch64 Kernel mit 32-Bit Userspace), die nun offizielle Versionen einsetzen mochten, mussen vor einem Update die 32-Bit-Binar-Add-ons entfernen. Ebenso ist ein `touch /storage/.update/.nocompat` notwendig, um die Überprufung der Architektur zu uberschreiben. Wer die offiziellen Builds verwendet, soll einfach aktualisieren wie gehabt.

### Bugs und Fixes

Die Entwickler bedanken sich fur das umfangreiche Feedback, das von den Alpha- und Beta-Versionen zuruckgeflossen ist. Sie glauben, dass sich keine großen Fehler in LibreELEC 8 eingeschlichen haben. In zirka zwei Wochen soll aber bereits Version 8.0.1 ausgegeben werden und sich um Probleme kummern, die nun aufkommen. Es gibt zum Beispiel auch ein bekanntes Problem mit iMX6. Hier startet Audio erst ungefahr 90 Sekunden nach dem Start.

### Installation von LibreELEC 8

Am einfachsten installierst Du LibreELEC 8, indem Du den LibreELEC USB-SD Creator verwendest. Den gibt es fur Linux, macOS und Windows gleichermaßen.

Unter Linux machst Du die Datei ausfuhrbar und startest sie danach. Damit das Programm auf die SD-Karte schreiben darf, braucht sie root-Zugriff. Du konntest sie zum Beispiel so uber das Terminal starten, wenn Du Dich im gleichen Ordner befindest:
    
    
    sudo ./LibreELEC.USB-SD.Creator.Linux-64bit.bin

Im Anschluss sieht das so aus:

![LibreELEC 8 installiert sich am einfachsten über den LibreELEC USB-SD-Creator](https://www.bitblokes.de/wp-content/uploads/2017/02/libreelec-8.png)

> _LibreELEC 8 installiert sich am einfachsten uber den LibreELEC USB-SD Creator_

Hast Du einen Raspberry Pi 2 oder 3, dann wahlst diese Architektur einfach aus uns rechts daneben die Version von LibreELEC.

Ich musste meinen Raspberry Pi 3 nur aktualisieren und nicht neu installieren, da mir der Pfad auf LibreELEC 8.0 automatisch angeboten wurde.

Die Entwickler bieten aber auch _img.gz_-Dateien an. Das sind die Abbilder, die Du mithilfe der ublichen Verdachtigen auf Datentrager schreiben kannst. [Etcher](https://www.bitblokes.de/2016/11/raspbian-oder-andere-abbilder-sehr-einfach-mit-etcher-auf-eine-sd-karte-schreiben/) ware da ein Kandidat. Links zu diesen Abbildern findest Du in der [offiziellen Ankundigung](https://libreelec.tv/2017/02/libreelec-krypton-v8-0-0-release/) zu LibreELEC 8.

### Kurzes Wort zu Kodi 17 _Krypton_

Kodi 17 Krypton hat mit _Estuary_ und _Estouchy _zwei neue Tapeten bekommen. Sie sind schick und sehen modern aus.

![LibreELEC und Estuary: Serien](https://www.bitblokes.de/wp-content/uploads/2016/12/serien.jpg)

> _LibreELEC und Estuary: Serien_

Hier ein Screenshot von Kodi 17 auf einem Nexus 7 2013. Das verwendete Skin ist Estouchy.

![Kodi 17 mit Estouchy auf einem Nexus 7](https://www.bitblokes.de/wp-content/uploads/2017/02/estouchy.jpg)

> _Kodi 17 mit Estouchy auf einem Nexus 7_

Weiterhin sind die Sektionen logischer unterteilt und Du als Anwender findest Dich besser zurecht.

![LibreELEC: Dienste](https://www.bitblokes.de/wp-content/uploads/2016/12/dienste.jpg)

> _Kodi 17: Dienste_

Als Standard WebUI ist Chorus 2 eingestellt. Ein Browser wird damit ohne Zusatze zur Fernbedienung. Unter Android sparst Du Dir damit fast [Kore](https://www.bitblokes.de/2015/12/kore-2-0-0-ist-da-kodi-fernbedienung-fuer-android/), die offizielle Fernbedienung von Kodi. Musik lasst sich ubrigens schon zum Browser streamen, mit Videos geht das noch nicht.

![Kodi 17 mit Chorus 2 bedienen](https://www.bitblokes.de/wp-content/uploads/2017/02/chorus-2.jpg)

> _Kodi 17 mit Chorus 2 bedienen_

Was DU alles fur Dein eigenes Multimediacenter mit LibreELEC und Raspberry Pi benotigst, findest Du in [diesem Beitrag](https://www.bitblokes.de/2015/11/raspberry-pi-2-als-multimedia-center-mit-kodi-was-man-dafuer-braucht/).

## Nette Pi-Konstellation

**Du kannst gerne Deinen Senf zu diesem Beitrag geben: [Hier geht es zu den Kommentaren](https://www.bitblokes.de/2017/02/libreelec-8-ist-ausgegeben-einfach-auf-dem-raspberry-pi-3-installieren/)**
