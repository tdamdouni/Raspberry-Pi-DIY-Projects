# SSH auf dem Raspberry Pi aktivieren (jetzt unter Raspian nötig)

_Captured: 2017-05-06 at 10:15 from [linuxundich.de](https://linuxundich.de/raspberry-pi/ssh-auf-dem-raspberry-pi-aktivieren-jetzt-unter-raspian-noetig)_

![](https://linuxundich.de/wp-content/uploads/2016/11/SSH-Raspberry-Pi-aktivieren-1021x580.png)

Im Gegensatz zu einem klassischen [Linux](https://linuxundich.de/tag/linux/) auf einem Computer, installiert man den [Raspberry Pi](https://linuxundich.de/go/rpi) immer uber eine Image-Datei. Dadurch ergibt sich eine Sicherheitslucke: Jedes Image ist identisch, daher lautet der im System angelegte User immer „pi" mit dem Passwort „raspberry". Dieses lasst sich uber das Kommando `passwd` schnell andern, doch viele RasPi-User machen davon keinen Gebrauch. Betreibt man den [Raspberry Pi](https://linuxundich.de/go/rpi) in einem offentlich zuganglichen Netz, ist es von daher fur einen Angreifer kein großes Problem den RasPi zu finden und sich einzuloggen. Zumal der RasPi seine Dasein uber einen ARP-Scan bereitwillig mitteilt.
    
    
    $ sudo arp-scan --localnet | grep Raspberry
    192.168.0.100  b8:27:eb:76:1e:16  [Raspberry Pi](https://linuxundich.de/category/raspberry-pi/) Foundation
    192.168.0.101  b8:27:eb:e4:e1:30  [Raspberry Pi](https://linuxundich.de/category/raspberry-pi/) Foundation

Bislang war auf den Raspian-Images der SSH-[Server](https://linuxundich.de/tag/server/) von Haus aus aktiv. Somit ließ sich der Raspberry Pi „headless" aufsetzen. Man brauchte also weder Maus, Tastatur oder einen Monitor um das System des RasPis einzurichten, was die Installation eines RasPi-Servers ungemein vereinfacht. In Anbetracht der IT-Sicherheits-GAUs der letzten Tage und Wochen, macht die Raspberry Pi Foundation [mit dieser Praxis nun Schluss](https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/): Seit Raspbian 2016-11-25 muss man den SSH-[Server](https://linuxundich.de/tag/server/) aktivieren. Kann man den RasPi direkt bedienen, ist das schnell geschehen, einen Headless-RasPi muss man jedoch gezielt vorbereiten.

## SSH auf dem Raspberry Pi aktivieren

Wer auf seinen Raspberry Pi direkt zugreifen kann, weil neben Tastatur/Maus auch noch ein Monitor an dem Minirechner angeschlossen sind, muss zum Aktivieren von SSH keine großen Klimmzuge machen. In der Anwendung _Preferences_ | _Raspberry Pi Configuration_ findet sich im Reiter _Interfaces_ ein Schalter zum Aktivieren des SSH-Servers. Diesen ist weiter von Haus aus installiert, man muss hier nun lediglich den Schalter auf _Enabled_ stellen und den Dialog mit _OK_ beenden.

Alternativ ruft man das konsolenbasierte Raspberry-Pi-Konfigurationswerkzeug mittels `sudo raspi-config` in einem Terminal auf und schaltet dort unter dem Eintrag _7 Advanced Options_ | _A4 SSH_ die entsprechende Option ein. Dies funktioniert dann selbstverstandlich auch mit dem Light-Image von Raspbian, das auf eine grafische Desktopumgebung verzichtet. Einen Neustart danach braucht es nicht zwingend, man kann man sich sofort wieder per SSH einloggen.

Dabei findet man gleich eine weitere Neuerung. Solange man das Passwort des Standardnutzers „pi" nicht abandert, es also bei „raspberry" belasst, bekommt man bei jedem Einloggen einen Hinweis auf den Schirm, dass man dieses doch bitte schnellstmoglichst tun solle. Dazu genugt es sich ganz normal einzuloggen und dann mit dem Kommando `passwd` das Kennwort abzuandern. [Linux](https://linuxundich.de/tag/linux/)-typisch zeigt das System bei dieser Aktion keinerlei Sternchen oder andere Platzhalter an. Alternativ funktioniert das Ändern des Passworts auch uber RasPi-Config.

## SSH auf einem Headless-RasPi

Mochte man nun aber gar nicht erst einen Monitor und Eingabegerate an den Raspberry Pi anschließen, dann steht man mit dem neusten Raspbian vor verschlossenen Turen: Konnte man sich fruher per SSH direkt auf dem RasPi einloggen, heißt es jetzt nur noch `ssh: connect to host 192.168.111.100 port 22: Connection refused` und nichts geht mehr. Nun beißt sich die Katze naturlich in den Schwanz: Ohne SSH kein SSH. Doch auch fur diesen Fall haben die Entwickler von Raspbian eine Losung erdacht.

Damit Raspbian von Haus aus SSH aktiviert, schreibt man die Image-Datei wie gewohnt auf die SD-Karte. Nach Abschluss der Aktion nehmt ihr die Karte nun nicht sofort aus dem Kartenleser, sondern offnet die `/boot`-Partition des Raspbian-Systems in einem Dateimanager eurer Wahl und erstellt dort eine leere Datei mit dem Namen `ssh`. Da mit dem FAT-Dateisystem formatiert wurde, funktioniert dies mit allen gangigen Betriebssystem, also mit Linux, MacOS X und auch mit dem Windows Explorer unter Microsoft Windows.

Ich personlich mache es mir unter Linux ein wenig leichter: Anstatt einen Dateimanager zu bemuhen, schreibe ich das Rapbian-Image wie gewohnt mit dd auf die Speicherkarte (Achtung: Bitte Namen und bei Bedarf Pfad der Image-Datei anpassen, sowie den Pfad `/dev/sdd` zur Speicherkarte andern) und lege die Datei dann mit `touch` an. Wobei man auch hier wieder den Pfad zum Mountpunkt der `/boot`-Partition anpassen muss. Arch bindet externe Medien unter /run/media/benutzername ein. Das `$(whoami)` sorgt dafur, dass dieser automatisch aufgelost wird.
    
    
    $ sudo dd if=2016-11-25-raspbian-jessie.img of=/dev/sdd bs=512; sync
    $ touch /run/media/$(whoami)/boot/ssh

In Zukunft wird es also ein klein wenig komplizierter einen Raspberry Pi ohne Monitor und Tastatur entsprechend aufzusetzen. Das Plus an Sicherheit ist es in meinen Augen jedoch wert, ich mochte nicht von einem „Raspberry-Pi-Botnet" aus der Presse erfahren. Zahlreiche RasPi-User wussten wahrscheinlich gar nicht, dass das System aus dem Netz heraus uber SSH zu erreichen war. Wurde dann nicht einmal das Standard-Passwort geandert, war das RasPi-System offen wie ein Scheunentor.
