# Headless-Konfiguration für den Raspberry Pi

_Captured: 2015-12-20 at 14:12 from [www.raspberry-pi-geek.de](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi)_

![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/headless-konfiguration-fuer-den-raspberry-pi/aa_123rf-19563382_konstantynov_headless-tablet_resized.jpg/11209-1-ger-DE/AA_123rf-19563382_konstantynov_headless-tablet_resized.jpg_large.jpg)

> _(C) konstantynov, 123RF_

Mit den hier vorgestellten Werkzeugen aus der SSH-Familie verwalten Sie Ihren Raspberry Pi problemlos aus der Ferne und ersparen sich dadurch die Anschaffung eines zusatzlichen Monitors und einer Tastatur. Der Konfigurationsaufwand fur eine solche Headless-Losung halt sich in erfreulich uberschaubaren Grenzen.

Viele Projekte fur den Raspberry Pi setzen einen "Headless"-Betrieb voraus, bei dem der Mini-Rechner ohne Monitor, Tastatur und Maus lauft. Oft zwingen schon Platzgrunde dazu, den fur viele Verwendungszwecke pradestinieren den Pi gerade seine geringen Abmaße. Als angenehmer Nebeneffekt bleibt der Low-Cost-Rechner im Headless-Betrieb auch ein solcher - fur Tastatur, Maus und Monitor kommen schnell 150 Euro oder mehr zusammen. Egal, warum sie den RasPi headless betreiben: Fur den Zugriff auf das Gerat mussen Sie in diesem Szenario eine Verbindung via Secure Shell (SSH) aufbauen [[1]](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi/\(offset\)/6).

SSH bietet einen sicheren, weil verschlusselten Weg, um sich auf einem entfernten Rechner anzubieten. Das Paket OpenSSH, das praktisch jede Linux-Distribution mitbringt, umfasst einen ganzen Werkzeugkasten an entsprechenden Tools, die ursprunglich vom OpenBSD-Projekt entwickelt wurden. SSH ubernimmt dabei die Rolle von Telnet oder Rlogin, Secure Copy (`scp`) ersetzt Remote Copy (`rcp`), Secure FTP (`sftp`) das unsichere FTP (`ftp`), und Ähnliches mehr.

Verwenden Sie auf dem RasPi eine halbwegs aktuelle Distribution wie Raspbian "Wheezy", steht SSH bereits einsatzfertig parat. Auf alteren Versionen war es dagegen in der Vorgabe deaktiviert. Haben Sie noch Tastatur und Monitor am Raspberry Pi hangen, prufen Sie mit dem Befehl `service sshd status` recht einfach, ob der SSH-Daemon bereits lauft. Falls ja, erhalten Sie eine Ausgabe wie in [Listing 1](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi).

Listing 1
    
    
    $ service sshd status
    Redirecting to /bin/systemctl status  sshd.service
    sshd.service - OpenSSH server daemon
              Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled)
              Active: active (running) since Wed 2013-02-13 13:06:40 EST; 28min ago
             Process: 273 ExecStartPre=/usr/sbin/sshd-keygen (code=exited, status=0/SUCCESS)
            Main PID: 280 (sshd)
              CGroup: name=systemd:/system/sshd.service
                      280 /usr/sbin/sshd -D

Um den Dienst gegebenenfalls zu installieren, benutzen Sie den Paketmanager der verwendeten RasPi-Distribution. Die entsprechenden Befehle fur Raspbian und Pidora zeigt das [Listing 2](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi). Nach dem Einrichten starten Sie den Daemon mittels des Befehls `sudo sshd start`.

#### IP-Adresse finden

Um Verbindung zum Raspberry Pi aufnehmen zu konnen, mussen Sie dessen IP-Adresse kennen - kein Problem, solange Sie ihn noch mit Tastatur und Monitor betreiben: Dann genugt ein schlichtes `ip addr` auf der Kommandozeile, um die Adresse herauszufinden. Was aber, wenn der Hund das HDMI-Kabel gefressen hat?

In diesem Fall verbinden Sie den Raspberry Pi mit dem Netzwerk und stecken dann die Stromversorgung ein, um ihn zu booten. Das geht headless allerdings auch nicht schneller als mit Tastatur und Monitor, nur sehen Sie diesmal nicht, was gerade vorgeht. Immerhin vermitteln Ihnen aber die Status-LEDs der RasPi (siehe [Tabelle "Funktion der Status-LEDs"](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi)) einen guten Eindruck davon, wie reibungslos der Vorgang ablauft. Bleiben einzelne LEDs dunkel, mussen Sie die entsprechende Fehlerquelle erst beseitigen, bevor Sie weitermachen konnen.

Funktion der Status-LEDs

Nummer

Aufschrift

Farbe

Funktion

D5

`ACT`

Grun

Zugriff auf SD-Karte

D6

`PWR`

Rot

Betriebsspannung

D7

`FDX`

Grun

Netzwerk (Full Duplex)

D8

`LNK`

Grun

Netzwerk (Verbindung/Aktivitat)

D9

`100`

Gelb

100-Mbit/s-LAN

Bei den ersten RasPis (Rev 1.0) sind D5 und D9 abweichend beschriftet.

Hat der Mini-Rechner erst einmal gebootet, finden Sie uber das Verwaltungsinterface des Routers in Ihrem Netzwerk die Adresse des Raspberry Pi schnell heraus. Suchen Sie dort nach einem Gerat namens `raspi` oder `raspberrypi` und notieren Sie dessen IP. Hilft gar nichts anderes weiter, mussen Sie schweres Geschutz in Form des Netzwerkscanners Nmap [[2]](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi/\(offset\)/6) auffahren. Wie das funktioniert, lesen Sie bei Bedarf im [Kasten "RasPi-Jagd per Nmap"](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi) nach. Dieser Overkill durfte aber nur in absoluten Ausnahmefall notwendig werden.

RasPi-Jagd per Nmap

Der Netzwerkscanner Nmap spurt zuverlassig jedes Gerat im Netzwerk auf und liefert bei Bedarf eine Fulle von Zusatzinformationen dazu. Auf einem Linux-Client richten Sie ihn ein, indem Sie das Paket _nmap_ uber den Paketmanager des Systems installieren, unter Debian und dessen Derivaten beispielsweise mittels `sudo apt-get install nmap`.

Um alle Gerate im Netzwerk aufzuspuren, verwenden Sie den Befehl `sudo nmap 192.168.0.0/24`, wobei Sie 192.168.0.0 durch die Adresse Ihres LANs ersetzen. In der Ausgabe von Nmap finden Sie eine Sequenz wie die in [Listing 2](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi) gezeigte, bei der an einer MAC-Adresse der Suffix `(Raspberry Pi Foundation)` anhangt. Die erste Zeile der Sequenz zeigt die IP-Adresse des Raspberry Pi, in [Listing 2](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi) ist es die 192.168.0.115.

Listing 2
    
    
    $ sudo nmap 192.168.0.0/24
    ...
    Nmap scan report for 192.168.0.115
    Host is up (0.0074s latency).
    Not shown: 999 closed ports
    PORT   STATE SERVICE
    22/tcp open  ssh
    MAC Address: B4:23:BF:DF:29:55 (Raspberry Pi Foundation)
    ...

#### Verbindungsaufnahme

Sobald Sie die IP-Adresse des Raspberry Pi kennen, nehmen Sie mithilfe des Befehls `ssh _user_@_IP_` Kontakt zu ihm auf. Als Benutzername `_user_` verwenden Sie entweder einen Account, den Sie dafur eigens auf dem RasPi eingerichtet haben, oder das bereits vorhandene Standard-Benutzerkonto der auf dem Pi eingesetzten Distribution. Die [Tabelle "Standard-Benutzerkonten"](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi) fuhrt die entsprechenden Logins und Passworter fur die gangigsten Varianten auf. Verwenden Sie auf dem RasPi eine dort nicht aufgefuhrte Distribution, hilft eventuell eine ahnliche Tabelle bei Elinux.org weiter [[3]](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi/\(offset\)/6).

In den folgenden Beispielen verwenden wir durchgangig 192.168.0.115 als IP und _fedora_ als Benutzerkonto. Diese mussen Sie jeweils durch die fur Ihre Installation gultigen Werte ersetzen.

Distribution

Benutzer

Passwort

Arch Linux ARM

root

`root`

OpenELEC

root

`openelec`

Pidora

root

`raspberrypi`

Raspbian Wheezy und Derivate

pi

`raspberry`

Melden Sie sich das erste Mal auf einer entfernten Maschine an, pruft Ihr Client die Datei `.rhosts` dahingehend, ob es sich um einen bereits bekannten Rechner handelt. Dies soll sicherstellen, dass Sie sich auch mit dem richtigen Rechner verbinden. Ist der Rechner dagegen bislang unbekannt, generiert SSH fur diesen einen Schlussel, an dem es ihn in Zukunft erkennen kann, und fragt dann sicherheitshalber noch einmal nach, ob Sie auch wirklich Kontakt aufnehmen wollen. Bejahen Sie das, beginnt die eigentliche Anmeldeprozedur. Ein Beispiel dieses Ablaufs zeigt [Listing 3](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi).

Listing 3
    
    
    $ ssh fedora@192.168.0.115
    The authenticity of host '192.168.0.115 (192.168.0.115)' can't be established.
    RSA key fingerprint is 83:d7:be:fe:5e:91:98:90:ff:eb:87:0b:88:d2:e9:e9.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added '192.168.0.115' (RSA) to the list of known hosts.
    fedora@192.168.0.115's password:

  


#### Root loswerden

Nach der Anmeldung auf einem RasPi-System, das lediglich uber einen Root-Account verfugt, sollten Sie aus Sicherheitsgrunden als erstes fur kunftige Anmeldungen ein normales Benutzerkonto anlegen. (Wie das funktioniert, beschreibt ein eigener Artikel ab Seite 28 in diesem Heft.) Als nachstes unterbinden Sie dann kunftige SSH-Logins durch _root_. Dazu tippen Sie:
    
    
    $ vi /etc/ssh/sshd_config

Der Editor Vi starten mit der Konfigurationsdatei fur SSH, in der Sie die Zeile `# PermitRootLogin yes` suchen. Hier entfernen Sie das Kommentarzeichen `#` vor dem Eintrag und andern das `yes` in ein `no` ([Abbildung 1](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi/\(offset\)/2)).

[ ![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/headless-konfiguration-fuer-den-raspberry-pi/abbildung-13/2808-1-ger-DE/Abbildung-11_large.png) ](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/headless-konfiguration-fuer-den-raspberry-pi/abbildung-13/2808-1-ger-DE/Abbildung-11_lightbox.png)

> _Abbildung 1: In der Datei sshd_config setzen Sie den Eintrag PermitRootLogin auf den Wert no._

Alle Benutzer, die via SSH auf den Raspberry Pi zugreifen durfen, tragen Sie nun mit in die Datei ein. Dazu erganzen Sie am Dateiende eine Zeile mit einer Liste der entsprechenden Benutzerkonten:
    
    
    AllowUsers hinz kunz

Damit die Änderungen greifen, starten Sie anschließend den SSH-Daemon mittels des Befehls `service sshd restart` neu. Zu guter Letzt beenden Sie die laufende SSH-Session mit `exit` und konnen sich anschließend als einer der neu eingetragenen Benutzer wieder anmelden.

#### Distribution konfigurieren

Lauft auf dem RasPi Pidora, dann startet dieses bei der ersten Benutzung normalerweise ein Konfigurationsskript, in dem Sie unter anderem ein Root-Passwort festlegen und ein Benutzerkonto einrichten konnen. Allerdings startet dieses Skript nur, wenn das Betriebssystem das Vorhandensein von Eingabegeraten feststellt. Booten Sie Pidora headless, konfiguriert es lediglich via DHCP die Netzwerkschnittstelle des RasPi, sodass Sie sich zumindest per SSH anmelden und dann die Konfiguration modifizieren konnen.

Booten Sie eine unter Raspbian "Wheezy" laufenden Raspberry Pi das erste Mal im Headless-Modus, erscheint eine Meldung, die Sie zum Start des Konfigurationstools Raspi-Config auffordert. Bei einer lokalen Erstanmeldung startet dieses automatisch, bei einer SSH-Verbindung mussen Sie es selbst aufrufen.

  


#### Schlussel generieren

Wahrscheinlich haben Sie schon einmal Public-Key-Verschlusselung genutzt, etwa fur E-Mails. Sie benotigen dazu einen offentlichen Key zum Verschlusseln und einen privaten Key zum Entschlusseln. Dabei dient der offentliche Schlussel quasi als Schloss, das sich mit dem privaten Schlussel wieder offnen lasst. Um die Sicherheit zu erhohen, sollten Sie den privaten Schlussel beim Erzeugen stets mit einer Passphrase absichern.

@:Dieser Mechanismus lasst sich auch fur SSH-Verbindungen einsetzen, wo er neben der Sicherheit auch den Komfort erhoht, indem er die Passworteingabe uberflussig macht. Dabei konnen Sie fur Benutzerkonten auf verschiedenen Maschinen auch unterschiedliche Schlusselpaare generieren.

Zunachst einmal erstellen Sie mithilfe des Befehls `ssh-keygen` ein neues Schlusselpaar. Das Tool fragt Sie zunachst nach einem Verzeichnis, in dem es die Schlussel ablegen soll, sowie nach einer Passphrase ([Listing 4](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi/\(offset\)/4)). Letztere darf neben Buchstaben und Leerzeichen auch Sonderzeichen [[4]](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi/\(offset\)/6). Den frisch erzeugten Public Key kopieren Sie nun auf den RasPi:
    
    
    $ ssh-copy-id fedora@192.168.0.115

Listing 4
    
    
    $ ssh-keygen
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/fedora/.ssh/id_rsa): [Eingabe]
    Created directory '/home/fedora/.ssh'.
    Enter passphrase (empty for no passphrase): Meine_Neue_Passphrase
    Enter same passphrase again: Meine_Neue_Passphrase
    Your identification has been saved in /home/fedora/.ssh/id_rsa.
    Your public key has been saved in /home/fedora/.ssh/id_rsa.pub.
    The key fingerprint is:
    3f:9e:8d:65:1b:0f:45:f7:22:a7:69:b3:c4:4d:8d:de fedora@raspi.local
    The key's randomart image is:
    +--[ RSA 2048]----+
    |                 |
    |                 |
    |              . .|
    |             . +.|
    |        S   . * o|
    |         . . X o |
    |          o % o E|
    |         . X B   |
    |          + + .  |
    +-----------------+

Anschließend melden Sie sich per SSH auf dem RasPi an - diesmal blitzschnell und ohne Angabe eines Passworts - und prufen, ob in der Datei `~/.ssh/authorized_keys` nicht etwa außer dem neu generierten Key auch andere, so nicht beabsichtigte Schlussel lagern.

Um auch anderen Benutzer diese Art der komfortablen SSH-Anmeldung zu ermoglichen, mussen Sie fur diese gesondert eigene Schlusselpaare erstellen.

#### Dateien ubertragen

Das OpenSSH-Paket bringt auch zwei von Werkzeuge mit, um Dateien sicher auf den Raspberry Pi zu ubertragen: `scp` ("secure copy") und `sftp` ("secure file transfer protocol"). Wahrend Scp sich vornehmlich dazu eignet, ad hoc eine kleinere Anzahl von Dateien zu transferieren, offnet Sftp eine dauerhafte Verbindung, uber die Sie eine ganze Reihe von Interaktionen vornehmen konnen.

Um Scp zu nutzen, mussen Sie sich nicht erst per SSH am RasPi anmelden. Die grundlegende Syntax des Kommandos folgt folgendem Schema:
    
    
    $ scp _Datei_ _user_@_IP_:/_Pfad_/_zum_/_Ziel_/

Mochten Sie etwa in unserer Beispielinstallation die Datei `raspi.html` aus dem aktuellen Verzeichnis in das Webserver-Verzeichnis auf dem RasPi ubertragen, verwenden Sie dazu den folgenden Befehl:
    
    
    $ scp opensource.odt fedora@192.168.0.115:/var/www/html/

Sie konnen auf diesem Weg auch komplette Verzeichnisse (in folgenden Beispiel den Ordner `foss/`) mitsamt Inhalt auf den RasPi kopieren. Dazu erganzen Sie den Scp-Befehl um die Option `-r` fur das rekursive Durchlaufen der Quelle:
    
    
    $ scp foss fedora@192.168.0.115:.

Hier steht anstelle der Angabe eines Verzeichnisses als Ziel lediglich ein Punkt. Das sorgt dafur, dass `foss/` und seine Inhalte im Home-Verzeichnis des Benutzers _fedora_ landen.

Bei Sftp handelt es sich um eine via SSH-Protokoll laufende sichere Version des klassischen FTP. Hier verbinden Sie sich wie von SSH selbst gewohnt, nur dass Sie als Kommando statt `ssh` diesmal `sftp` verwenden:
    
    
    $ sftp fedora@192.168.0.115

Dies offnet eine SFTP-Sitzung, in der Sie eine Vielzahl von Befehlen nutzen konnen. Beispiele fur die gangigsten davon zeigt das [Listing 5](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi/\(offset\)/4), das (kommentiert) den Ablauf einer kompletten Session darstellt.

Listing 5
    
    
    $ sftp fedora@192.168.0.115                        # via SFTP mit dem Raspberry verbinden
    fedora@192.168.0.115's password: _Passwort_
    Connected to 192.168.0.115
    sftp> pwd                                        # aktuelles entferntes Verzeichnis
    Remote working directory: /home/fedora
    sftp> lpwd                                        # aktuelles lokales Verzeichnis
    Local working directory: /home/rsuehle
    sftp> ls                                        # Inhalt des entfernten Verzeichnisses
    Desktop Docs  Downloads Music Pics  Public
    sftp> cd Docs                                        # entferntes Verzeichnis wechseln
    sftp> lls                                        # Inhalt des lokalen Verzeichnisses
    fedora.png
    sftp> put fedora.png                                # kopiert Datei ins entfernte Verzeichnis
    Uploading fedora.png to /home/fedora/Docs/fedora.png
    fedora.png                     100%
    556KB 556.1KB/s   00:01
    sftp> get opensource.odt                        # kopiert Datei aus dem entfernten Verzeichnis
    Fetching /home/fedora/Docs/opensource.odt to opensource.odt
    /home/fedora/Docs/opensource.odt
    100%  556KB 556.1KB/s   00:00
    sftp> lls                                        # Inhalt des lokalen Verzeichnisses
    fedora.png
    opensource.odt
    sftp> exit                                        # SFTP-Sitzung beenden

  


#### Grafische Programme

Benutzen Sie die grafische Oberflache eines Linux-Rechners, dann erfolgen alle Interaktionen uber das X Window System, kurz auch gern schlicht als X bezeichnet. Um via SSH eine grafische Anwendung starten zu konnen, mussen Sie dem Anmeldebefehl den Parameter `-X` hinzufugen. Er aktiviert das sogenannte X-Forwarding:
    
    
    $ ssh -X fedora@192.168.0.115

Das klappt jedoch nur, sofern in der bereits erwahnten SSH-Konfigurationsdatei `/etc/ssh/sshd_config` die Einstellung `X11Forwarding` auf `yes` gesetzt ist ([Abbildung 2](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi/\(offset\)/6)). Dies voraus gesetzt, konnen Sie nach der Anmeldung auch grafische Programme auf dem Raspberry Pi aus der Ferne nutzen. Um etwa den schlanken Webbrowser Midori zu starten, den die meisten RasPi-Distributionen bereits vorinstallieren, tippen Sie auf der Kommandozeile einfach `midori` ein ([Abbildung 3](http://www.raspberry-pi-geek.de/Magazin/2013/05/Headless-Konfiguration-fuer-den-Raspberry-Pi/\(offset\)/6)).

[ ![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/headless-konfiguration-fuer-den-raspberry-pi/abbildung-23/2811-1-ger-DE/Abbildung-21_large.png) ](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/headless-konfiguration-fuer-den-raspberry-pi/abbildung-23/2811-1-ger-DE/Abbildung-21_lightbox.png)

> _Abbildung 2: Um grafische Programme via SSH betreiben zu konnen, mussen Sie in /etc/ssh/sshd_config die Einstellung X11Forwarding auf yes setzen._

[ ![](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/headless-konfiguration-fuer-den-raspberry-pi/abbildung-33/2814-1-ger-DE/Abbildung-31_large.png) ](http://www.raspberry-pi-geek.de/var/rpg/storage/images/magazin/2013/05/headless-konfiguration-fuer-den-raspberry-pi/abbildung-33/2814-1-ger-DE/Abbildung-31_lightbox.png)

> _Abbildung 3: Ob das Aufrufen grafischer Programme via SSH klappt, testen Sie am einfachsten durch einen Aufruf des Webbrowsers Midori._

#### Fazit

Mit den hier vorgestellten Werkzeugen aus der SSH-Familie verwalten Sie Ihren Raspberry Pi problemlos aus der Ferne und ersparen sich dadurch die Anschaffung eines zusatzlichen Monitors und einer Tastatur. Der Konfigurationsaufwand fur eine solche Headless-Losung halt sich in erfreulich uberschaubaren Grenzen.

Ruth Suehle arbeitet fur Red Hat in der "Open Source and Standards Group", leitet das Marketing-Team des Fedora-Projekts und ist Ko-Autor des demnachst bei O'Reilly erscheinenden Buchs "Raspberry Pi Hacks". Fruher betatigte sie sich als Redakteur fur das "Red Hat Magazine", heute moderiert sie auf Opensource.com Diskussionen uber die Prinzipien freier Software. Auf GeekMom.com schildert sie außerdem das Abenteuer der Mutterschaft im Spannungsfeld rund um Technologie und Science Fiction.
