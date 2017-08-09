# Raspberry Pi als Mediacenter einrichten 

_Captured: 2016-11-07 at 11:10 from [www.tecchannel.de](http://www.tecchannel.de/a/raspberry-pi-als-mediacenter-einrichten,2059184)_

Bei Open ELEC handelt sich um eine kleine Linux-Distribution mit der Mediacenter-Software XBMC. Open Elec ist fur PCs, einige Multimedia-Gerate wie beispielsweise Apple TV und auch fur den Raspberry Pi verfugbar. Eine Kombination aus Raspberry Pi, Open Elec und Maraschino ergibt eine perfekte und fernsteuerbare Multimedia-Station. Das Prinzip wurde auch mit jedem anderen System funktionieren, auf dem XBMC lauft. Dazu gehort unter anderem Raspbmc, das sich via [Noobs](http://www.raspberrypi.org/downloads) installieren lasst. [Open Elec](http://openelec.tv/) bringt allerdings ein separates und speziell entwickeltes Menu mit sich, das die Konfiguration angenehmer macht.

  1. **[Raspberry Pi als Arcade-Automat**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468)  
Der Raspberry Pi lasst als Arcade-Automat im Miniaturformat vergangene Zeiten aufleben. Ein kleiner Bildschirm zeigt dabei die Retro-Spiele an, wahrend ein Analogstick samt Buttons fur die Steuerung zur Verfugung steht.
  2. **[Raspberry Pi als Notebook**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,2)  
Die eigentlich fur das Smartphone Motorola Atrix gedachte Docking-Station verwandelt den Raspberry Pi in einen Laptop mit Bildschirm, Tastatur und Touchpad. Die Erweiterungen sind bereits ab 70 Euro auf Ebay erhaltlich.
  3. **[WLAN-Schnittstelle fur kleines Geld**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,3)  
Der Raspberry Pi bietet keinen WLAN-Zugang. Ein entsprechendes Modul kann jedoch fur kleines Geld nachgerustet werden.
  4. **[Raspberry Pi als VPN-Server**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,4)  
Als permanent laufender VPN-Server kann der Raspberry Pi jederzeit fur eine abhorsichere Verbindung sorgen.
  5. **[Raspberry Pi als TOR-Zugang**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,5)  
Über das TOR-Netzwerk kann der Raspberry Pi fur eine anonyme Internetverbindung sorgen, indem der Datenverkehr uber ein weltweites Rechnernetz umgeleitet wird.
  6. **[Bastelanleitung fur Raspberry Pi Gehause**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,6)  
Ein gunstiges Gehause fur die Platine des Raspberry Pi lasst sich uber diese Schablone basteln, die nach dem Ausdrucken nur noch gefaltet werden muss.
  7. **[Raspberry Pi als gunstige Alternative zu Apples Time Capsule**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,7)  
Apples Backup-Losung Time Capsule schlagt mit uber 200 Euro zu Buche. Mit dem Raspberry Pi lasst sich die Datensicherung auf dem Mac auch deutlich gunstiger realisieren.
  8. **[Gut verpackt fur die lange Reise**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,8)  
Die großen Temperaturanderungen auf dem Weg nach oben zwangen die Forscher dazu, den Raspberry Pi gut einzupacken.
  9. **[Der Raspberry Pi als Supercomputer**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,9)  
Aus dem Verbund von 64 Mini-PCs entstand an der Universitat von Southampton ein Supercomputer. Als Gehause wurden Lego-Steine verwendet.
  10. **[Der Raspberry Pi als Turoffner**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,10)  
Eine praktische Bastlerlosung: Per iPhone und Siri lasst sich das Garagentor offnen. Fur die Technik im Hintergrund ist ein Raspberry Pi zustandig.
  11. **[Der Raspberry Pi im Weltraum**](http://www.tecchannel.de/g/die-besten-verwendungsmoeglichkeiten-fuer-raspberry-pi,108468,11)  
Sogar im Weltraum war der kleine Rechner bereits. Per Ballon ging es in eine Hohe von 30 Kilometern. Von hier sendete das System Live-Bilder an die Erde.

Laden Sie zunachst das neueste Abbild von der[ Open-Elec](http://openelec.tv/)-Website herunter, oder benutzen Sie die Datei auf der Heft-DVD. Diese enthalt die notigen Dateien fur die Installation unter Windows und Linux. Sollte dies nicht die allerneueste Version sein, konnen Sie Open Elec spater automatisch aktualisieren lassen. Fur die Installation macht die Version keinen Unterschied. In diesem Beitrag zeigen wir Ihnen, wie Sie Open Elec unter Windows auf eine SD-Karte ubertragen. Wie es unter Linux geht, konnen Sie[ in diesem Wiki](http://wiki.openelec.tv/index.php?title=Installing_OpenELEC_on_Raspberry_Pi) nachlesen. Die Installation lasst sich auch auf einem Raspberry Pi mit laufendem Raspbian durchfuhren. Da dieser allerdings nur einen Steckplatz fur eine SD-Karte hat und darauf das Betriebssystem lauft, brauchen Sie zusatzlich einen USB-Kartenleser.

Die Anleitung fur eine weitere Installationsvariante finden Sie [auf dieser Webseite](http://wiki.openelec.tv/index.php?title=Installing_OpenELEC_on_Raspberry_Pi). Im Open-Elec-Wiki wird beschrieben, wie Sie einen zusatzlichen USB-Stick am Raspberry Pi als Datenspeicher einrichten. Mit dieser Maßnahme lasst sich die Geschwindigkeit des Systems steigern.

**Hinweis: Sicherheitsrisiko SSH-Server **

SSH ist bei Open Elec nicht besonders sicher konfiguriert. Der Standardbenutzername ist "root" und das Passwort "openelec". Mit diesem Wissen kann sich jeder Anwender in Ihrem Netzwerk Zugriff auf die Open-Elec-Box verschaffen. Da sich der Rasperry Pi aber in Ihrem Heimnetz wahrscheinlich hinter einer Firewall befindet, kann von außen niemand das Gerat erreichen. Das SSH-Passwort lasst derzeit nicht sehr einfach andern. Es befindet sich in einem nur lesbaren Dateisystem. Fur eine Passwortanderung mussten Sie Open Elec aus den Quellen selbst bauen. Dieser Umstand soll sich irgendwann in der Zukunft andern.

**Installation durchfuhren:**Entpacken Sie das Archiv auf die Festplatte. Fur die Installation unter Windows entpacken Sie auch die enthaltene Datei "OpenELEC-RPi.arm- 3.2.4.img.zip". Die TAR-Datei dient der Installation unter Linux. Laden Sie sich außerdem das Tool [Win 32 Disk Imager](http://sourceforge.net/projects/win32diskimager/) herunter.

Stecken Sie die SD-Karte in den Kartenleser. Fur Open Elec muss die Karte mindestens eine Kapazitat von 1 GB haben. Sichern Sie alle darauf befindlichen Dateien, denn die Karte wird im nachsten Schritt uberschrieben.

![XBMC-Server hinzufügen: Bevor Sie Maraschino mit Open Elec nutzen können, müssen Sie die entsprechenden Einstellungen hinterlegen.](http://images.cio.de/images/computerwoche/bdb/2516784/840x473.jpg)

> _XBMC-Server hinzufugen: Bevor Sie Maraschino mit Open Elec nutzen konnen, mussen Sie die entsprechenden Einstellungen hinterlegen._

Starten Sie Win 32 Disk Imager. Wahlen Sie auf der rechten Seite des Fensters den Laufwerksbuchstaben der SD-Karte aus. Prufen Sie diese Angabe genau, denn das Tool zeigt beispielsweise auch USB-Festplatten an. Wenn Sie das falsche Laufwerk wahlen, gehen alle Daten darauf verloren. Über die Schaltflache neben dem Feld unter "Image File" wahlen Sie die zuvor entpackte "Datei OpenELEC-RPi.arm- 3.2.4.img" aus. Klicken Sie dann auf die Schaltflache "Write", und bestatigen Sie mit "Yes". Nachdem der Vorgang abgeschlossen ist, schließen Sie Win 32 Disk Imager uber die Schaltflache "Exit". Melden Sie den Kartenleser beim System ab und nehmen die SD-Karte aus dem Kartenleser.

**Hinweis:** Sollte es bei der Verwendung von Win 32 Disk Imager Probleme auftreten, formatieren Sie die Karte vorher uber das Tool [SD Formatter](http://www.pcwelt.de/downloads/SD_Formatter-SD-Card-Tool-8412440.html). Stellen Sie dabei uber "Option" den Parameter "Format Size Adjustment" auf "On".

  


Stecken Sie die SD-Karte nun in den Raspberry Pi, und schließen Sie das Netzteil an. Fur die Einrichtung benotigen Sie wenigstens eine Tastatur. Die Steuerung erfolgt uber die Cursortasten. Beim ersten Start des Systems erscheint automatisch ein Assistent, in dem Sie die Sprache fur die Benutzeroberflache auswahlen, beispielsweise "Deutsch". Der zweite Schritt ist, den Rechner zu taufen. Dies ist fur spatere Netzwerkzugriffe notwendig. Wir haben es bei der Standardeinstellung Open Elec gelassen. Wenn Sie einen WLAN-Stick am Raspberry Pi nutzen, sucht das System im nachsten Schritt nach verfugbaren WLANs, und Sie konnen sich mit einem verbinden. Weiterhin durfen Sie im Einrichtungsassistenten bestimmen, welche Fernzugriffe erlaubt sind. Hier stehen SSH und Samba zur Auswahl. Wenn der Raspberry Pi spater auch "headless", also beispielsweise als reine Musikstation ohne Bildschirm laufen soll, ist SSH fur die Remote-Administration empfehlenswert. Wollen Sie diese Einstellungen spater andern, finden Sie auf der XBMC-Oberflache ganz rechts ein Menu "System" mit dem Untermenu "OpenELEC". Hier andern Sie auch die Tastatureinstellung, die trotz zuvor gewahlter Sprache "Deutsch" auf "us" gesetzt ist.

![Maraschino konfigurieren: Über das Rädchen links oben aktivieren Sie den Modus, über den Sie Module hinzufügen können. Rechts oben konfigurieren Sie die Hosts.](http://images.cio.de/images/computerwoche/bdb/2516785/840x473.jpg)

> _Maraschino konfigurieren: Über das Radchen links oben aktivieren Sie den Modus, uber den Sie Module hinzufugen konnen. Rechts oben konfigurieren Sie die Hosts._

Netzwerk, Zerofconf oder Avahi: Gerade fur den Betrieb ohne Bildschirm ist es wichtig, den Raspberry Pi uber das Netzwerk erreichen zu konnen. Eine Moglichkeit ist, Open Elec mit einer festen IP-Adresse zu konfigurieren. Sie konnen das uber die Open-Elec-Einstellungen realisieren. Gut zu wissen ist, dass Open Elec per Standard Avahi oder Zeroconf aktiviert hat. Die meisten Linux-Installationen bringen einen entsprechenden Client mit sich. Unter Windows mussen Sie[ die Bonjour-Dienste](http://www.apple.com/de/support/bonjour) nachinstallieren. Das Gute dabei ist, dass Sie die IP-Adresse nicht wissen mussen. Sie konnen das Gerat in unserem Fall unter "OpenELEC. local" erreichen. Der Name vor ".local" hangt davon ab, wie Sie die Installation benannt haben. Ändern Sie den Namen uber die Open- Elec-Einstellungen, ist ein Neustart des Systems notwendig.

  


Fur die Fernsteuerung von Open Elec beziehungsweise XBMC gibt es gleich mehrere Moglichkeiten. Unter anderem ist ein Webinterface in XBMC eingebaut, das allerdings nicht besonders viele Funktionen bietet. Wollen Sie es dennoch benutzen, mussen Sie uber "System > Einstellungen > Dienste > Webserver" die Option "Steuerung uber HTTP zulassen" aktivieren. Wir zeigen Ihnen Alternativen mit Android und Maraschino. Letzteres bietet eine Weboberflache, uber die Sie XBMC fernsteuern konnen. Wir haben die Installation unter Ubuntu getestet. Dafur gilt auch die folgende Beschreibung. Im Prinzip wurde Maraschino auch unter Windows funktionieren. Die Installation ist hier jedoch relativ aufwendig, weil Sie den Webserver Apache und Python installieren und manuell konfigurieren mussen. Deshalb raten wir davon ab und empfehlen fur Windows-Nutzer die Ubuntu-Installation in einer virtuellen Maschine. Am besten nutzen Sie dafur die kostenlose Virtualisierungs-Software [Virtualbox](http://www.pcwelt.de/downloads/System-Software-VirtualBox-Windows-582647.html).

Auch fur die Benutzung von Maraschino mussen Sie die Steuerung uber HTTP zulassen. Wollen Sie Android als Fernbedienung einsetzen, mussen Sie in den "Einstellungen" außerdem unter "Dienste > Fernsteuerung" die Option "Steuerung uber entfernte Programme zulassen" aktivieren.

![Musik kontrollieren: Mit Hilfe von Maraschino haben Sie XBMC im Griff. Sie können unter anderem Musik auswählen, die auf dem Raspberry Pi abgespielt werden soll.](http://images.cio.de/images/computerwoche/bdb/2516786/840x473.jpg)

> _Musik kontrollieren: Mit Hilfe von Maraschino haben Sie XBMC im Griff. Sie konnen unter anderem Musik auswahlen, die auf dem Raspberry Pi abgespielt werden soll._

**Maraschino vorbereiten:**Die Software befindet sich in aktiver Entwicklung. Deswegen kann es noch zu einigen Unstimmigkeiten kommen. Es gibt allerdings ein Maraschino-Forum auf [www.maraschinoproject.com](http://www.maraschinoproject.com/), in dem Sie Hilfe finden. Unter Linux lasst sich Maraschino sehr bequem zum Laufen bringen, vorausgesetzt Git und Python sind vorhanden. Git installieren Sie uber die Paketverwaltung nach, Python ist bei den meisten Distributionen standardmaßig installiert. Sind diese Voraussetzungen erfullt, fuhren Sie folgenden Befehl auf der Kommandozeile aus (eine Zeile):

sudo git clone https://github.com/mrkipling/maraschino.git /opt/maraschino

Im Anschluss kopieren Sie das Init-Script und die Konfigurationsdatei mit den beiden Zeilen

sudo cp /opt/maraschino/initd /etc/init.d/maraschino   
sudo cp /opt/maraschino/default /etc/default/maraschino

Mit der Standardeinstellung lauft Maraschino auf Port 7000. Das konnen Sie bei Bedarf in der Konfigurationsdatei "/etc/default/mara schino" andern. Mochten Sie Maraschino in einen anderen Pfad und nicht unter "/opt" legen, passen Sie in der Konfigurationsdatei den Parameter "APP_PATH" an.

Im Anschluss machen Sie die Datei "maraschino" ausfuhrbar:

sudo chmod a+x /etc/init.d/ maraschino

Den Server konnen Sie nun mit folgendem Befehl starten:

sudo /etc/init.d/maraschino start

Optional konnen Sie den Dienst automatisch starten lassen. In unserem Beispiel funktioniert das mit Hilfe des Befehls:

update-rc.d maraschino defaults

![XBMC und Android: Links sehen Sie das offizielle XBMC Remote und rechts Yatse. Welche App Sie bevorzugen, ist unter anderem Geschmackssache.](http://images.cio.de/images/computerwoche/bdb/2516787/840x473.jpg)

> _XBMC und Android: Links sehen Sie das offizielle XBMC Remote und rechts Yatse. Welche App Sie bevorzugen, ist unter anderem Geschmackssache._

**Server hinzufugen:** Sobald der Server gestartet ist, erreichen Sie die Oberflache unter http://localhost:7000 im Browser. Nun konnen Sie den Raspberry Pi als Server hinzufugen. Achten Sie darauf, beim Feld "Hostname / IP address" kein "http://" zu verwenden. Tragen Sie als Host-Namen beispielsweise openelec. local und hinter "Port" den Wert 80 ein. Hinter "Username" genugt xbmc, wenn Sie in Open Elec nichts anderes konfiguriert haben. Klicken Sie nun auf "Save", scheint sich nichts getan zu haben. Maraschino hat den Server allerdings gespeichert. Sie konnen das verifizieren, indem Sie mit der Maus in die rechte obere Ecke des Browser-Fensters fahren. Dort haben Sie außerdem die Moglichkeit, uber "XBMC servers > Add server" mehr als einen XBMC-Server zu hinterlegen.

  


Bewegen Sie die Maus in die linke obere Ecke, konnen Sie auf das Radchen klicken und den Konfigurationsmodus fur die Module aktivieren. Fugen Sie einfach ein entsprechendes Modul, wie zum Beispiel die "XBMC Library", hinzu. Hier kann es sein, dass Maraschino wenig aussagekraftige Fehlermeldungen ausgibt wie : "There was a problem connecting to the XBMC server".

![Anwendername und Passwort: Damit nicht jeder auf Ihre Maraschino-Implementierung zugreifen kann, sollten Sie diese mit einem Passwort schützen.](http://images.cio.de/images/computerwoche/bdb/2516788/840x473.jpg)

> _Anwendername und Passwort: Damit nicht jeder auf Ihre Maraschino-Implementierung zugreifen kann, sollten Sie diese mit einem Passwort schutzen._

Der Grund hierfur ist, dass die Bibliothek nicht aktualisiert ist. Gehen Sie den Weg uber "Files", finden Sie alle in Open Elec eingebundenen Quellen und Ordner. Rufen Sie eine Musikdatei auf, spielt sich diese auf dem Raspberry Pi und nicht im Browser ab. Deswegen empfehlen wir Ihnen die Installation des Add-ons "XBMC Library Auto Update". Sie finden es via "System > Einstellungen > Add-ons > Weitere Addons > XBMC.org Add-ons > Programm Addons". Ist es dort nicht gelistet, klicken Sie mit der rechten Maustaste auf "XBMC.org Addons" und dann auf "Aktualisierung erzwingen". Hierfur und fur die Installation ist eine Internetverbindung notwendig. Weiterhin sollten Sie in den Einstellungen unter "Musik a Datenbank" die Option "Aktualisiere Datenbank bei Start" aktivieren. Haben Sie eine sehr große Bibliothek, kann das den Start sehr verzogern. In diesem Fall sollten Sie "XBMC Library Auto Update" so konfigurieren, dass die Aufgabe nachts lauft.

**Tipp:** Sind Sie im Besitz eines Synology-NAS, dann konnen Sie Maraschino uber [die Pakete der Synocommunity](http://www.synocommunity.com/packages) installieren.

  


Open Elec beziehungsweise XBMC lassen sich auch mit Hilfe diverser Android-Apps fernsteuern. Android beherrscht aber derzeit noch kein Zeroconf. Deswegen mussen Sie die IP-Adresse der XBMC-Station kennen. In diesem Fall empfehlen wir Ihnen, der Open-Elec-Installation eine feste IP-Adresse zu spendieren.

In Sachen Fernbedienung funktioniert das offizielle [XBMC Remote](http://www.pcwelt.de/a54c) ganz brauchbar. Sie konfigurieren in der Maske einen frei wahlbaren Namen, IP-Adresse, API-Port, Anmeldenamen und Passwort. Die drei letzteren sind mit den Webserver-Einstellungen in Open Elec abzugleichen.

Eine praktische Alternative zu XBMC Remote ist die App [Yatse](http://www.pcwelt.de/85pg). Vielerorts wird dieses Programm besser bewertet. Die Konfiguration lauft aquivalent zu XBMC Remote. Yatse bietet unter anderem eine Offline- Bibliothek. Weiterhin konnen Sie mit Yatse Medien via UPnP zu XBMC senden und von XBMC streamen. Fur diese Funktionen mussen Sie allerdings den Yatse Unlocker auf Google Play kaufen, der mit 3,49 Euro zu Buche schlagt. Sollte sich das Raspberry Pi in einem anderen Raum befinden, konnen Sie Ihr Android- Gerat als Player verwenden. Somit ist eine doppelte Verwaltung der Musiksammlung nicht notwendig

## Infrarot-Fernbedienung verwenden

Wenn Sie ihren Raspberry Pi als Mediacenter am TV-Gerat betreiben wollen, bietet eine herkommliche Infrarot-Fernbedienung den meisten Komfort. Bei neueren TV-Geraten benotigen Sie keine Extra-Fernbedienung. Sie mussen hier nur HDMI-CEC aktivieren und konnen dann den Raspberry Pi mit der TV-Fernbedienung steuern.

Weitere Infos dazu finden Sie [hier](http://www.pcwelt.de/8n6z). Sollte das nicht funktionieren, verwenden Sie eine Extra-Fernbedienung mit eigenem USB-Infrarot-Empfanger. Eine Liste der unterstutzten Modelle finden Sie uber [diese Webseite](http://www.pcwelt.de/bcly). (hal)

Dieser Artikel basiert auf einem Beitrag unserer Schwesterpublikation [PC-Welt](http://www.pcwelt.de/ratgeber/Raspberry_Pi_als_Mediacenter_einrichten-Schritt_fuer_Schritt-8632892.html?redirect=1).
