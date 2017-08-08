# HomeBridge auf Raspberry Pi installieren

_Captured: 2017-05-06 at 10:00 from [alexbloggt.com](https://alexbloggt.com/homebridge-installieren/)_

![](https://alexbloggt.com/wp-content/uploads/2016/02/Artikelbild_HomeBridge-700x329.jpg)

Da [RaZberry](https://alexbloggt.com/geraete-ueber-den-raspberry-pi-und-homekit-steuern/) mittlerweile seine HomeKit-Funktionalitat entfernt hat, habe ich mich nach einer geeigneten Alternative fur einen HomeKit-Server auf meinem Raspberry Pi umgesehen und bin dabei bei dem Projekt „[HomeBridge](https://github.com/nfarina/homebridge)" gelandet. Dieser Server basiert auf NodeJS und lasst sich dank zahlreich vorhandener Plugins einfach erweitern, sodass man damit bequem uber die HomeKit API seine Sensoren und Aktoren ansteuern kann.

In diesem Artikel geht es um die Grundinstallation von HomeBridge auf einem Raspberry Pi. Wie man diese Installation fur sein eigenes vorhandenes Setup (z.B. Funksteckdosen, Temperatur- / Luftfeuchtigkeitssensoren, Infrarot-Gerate etc.) mit Hilfe bereits existierender Plugins erweitern kann, folgt in einem separaten Artikel.

Bevor ihr mit der weiteren Installation beginnt, solltet ihr uber

eure Paketquellen und Pakete auf den aktuellsten Stand bringen, um etwaige Probleme mit Abhangigkeiten von Paketen zu umgehen.

# 1\. Update des C++-Compilers

_**Hinweis**: Dieser Schritt ist nur notwendig fur Nutzer, die noch Raspbian Wheezy einsetzen. Unter Jessie solltet ihr die aktuelle Version des Compilers bereits installiert haben. Ihr konnt das uberprufen mit g++-4.9 -v. Erhaltet ihr in der letzten Zeile gcc version 4.9.x,so konnt ihr diesen Schritt uberspringen. Das gilt naturlich auch fur Wheezy-Installationen, bei denen ihr den Compiler schon aktualisiert habt._

Um die neueste Version des Compilers fur Raspbian zu installieren, musst ihr zunachst eure Paketquellen (temporar) andern. Bearbeitet dazu die Paketquellen, z.B. via sudo nano /etc/apt/sources.list und ersetzt „_wheezy_" jeweils mit „_jessie_". Speichert die Änderungen und fuhrt ein sudo apt-get update aus, um die Änderungen an den Paketquellen durchzufuhren. Anschließend konnt ihr mit sudo apt-get install gcc-4.9 g++-4.9 die benotigte Version des Compilers installieren. Ihr konnt (und solltet) dann die Änderungen an den Paketquellen wieder ruckgangig machen, indem ihr diese wieder bearbeitet via sudo nano /etc/apt/sources.list und „jessie" wieder durch „wheezy" ersetzt. Ein anschließendes sudo apt-get update bringt eure Quellen wieder auf den Ursprungszustand.

Um die Standardcompilerversion noch der neu installierten Version anzupassen, reichen diese beiden Befehle, die ihr einfach nacheinander aufrufen konnt:

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 60 --slave /usr/bin/g++ g++ /usr/bin/g++-4.9sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.6 40 --slave /usr/bin/g++ g++ /usr/bin/g++-4.7

Gebt ihr nun g++ -v ein, sollte in der letzten ausgegebenen Zeile

stehen.

# 2\. Installation von NodeJS

_**Hinweis**: Bei der Installation wird zwischen Raspberry 1 (Raspberry A, Raspberry B, Raspberry B+, Raspberry Zero) und Raspberry 2 (Raspberry Pi B2) unterschieden. Bitte achtet darauf, die richtige Version zu installieren! Falls ihr nicht wisst, welche Version ihr habt, konnt ihr dies an den technischen Daten erkennen. Handelt es sich um ein Modell mit 1GB RAM, so ist es ein Raspberry 2, hat euer Raspberry 512MB oder weniger, so ist es ein Raspberry 1._

**Update** 03.03.2016: Mittlerweile gibt es einen neuen Raspberry Pi - den Raspberry Pi 3. Auch auf diesem lasst sich HomeBridge installieren. Bei der NodeJS-Version sollte auch hier die ARMv7-Version wie beim Raspberry Pi 2 laufen.

Wechselt zur Installation am Besten uber „cd" erst einmal in euer Home-Verzeichnis. Anschließend schaut ihr auf [dieser Seite](https://nodejs.org/en/download/), welche Version von NodeJS in der LTS-Version aktuell „stable" ist. Zur Zeit der Artikelerstellung war das 4.3.0.

Ladet euch die Version auf euren Raspberry Pi herunter, entpackt sie und wechselt in das erstellte Verzeichnis:

  * Raspberry 1:  

  * Raspberry 2:  


Anschließend kopiert ihr den Inhalt des Verzeichnisses nach „_/usr/local_":

Um die erfolgreiche Installation zu prufen, fuhrt ihr ein node -vaus, bei dem ihr als Ausgabe nun „_v4.3.0_" erhalten solltet (bzw. aktueller).

Hat das soweit geklappt, konnt ihr die heruntergeladene Datei sowie den entpackten Ordner loschen:

# 3\. Installation weiterer Pakete

Ein paar weitere Pakete werden fur Avahi noch benotigt. Diese konnen einfach uber apt installiert werden:

# 4\. Installation von HomeBridge

Die Installation von HomeBridge selbst ist nun denkbar einfach. Ein einfaches

sollte euch HomeBridge in der aktuellsten Version uber npm laden und installieren lassen. Das dauert etwas, sollte aber in einigen Minuten (zumindest beim Raspberry 1) abgeschlossen sein.

Ihr konnt anschließend eure Installation prufen, indem ihr HomeBridge ganz einfach uber homebridge im Terminal startet. Es kommen jetzt noch Meldungen, dass keine Plugins und keine Konfigurationsdatei gefunden wurden, das ist in der Grundinstallation normal. Wie ihr eure Gerate einbindet uber die Plugins und passende Konfigurationsdateien erstellt, werde ich im nachfolgenden Blogbeitrag beschreiben.

# 5\. Autostart von HomeBridge

Der Autostart von HomeBridge ist naturlich nur dann sinnvoll, wenn ihr den Service soweit samt Plugins und Konfiguration auf eurem Raspberry Pi eingerichtet habt. Der Vollstandigkeit halber, beschreibe ich diesen Schritt aber auch noch in diesem Artikel.

Hier wird unterschieden, zwischen 2 Moglichkeiten: Einmal via init.d (Wheezy und alter) und uber systemd (Jessie und neuer). Da ich selbst auf meinem Raspberry Pi noch Wheezy nutze, gehe ich hier nur auf die Methode via init.d ein. Wer systemd nutzen mochte, findet [hier](https://gist.github.com/johannrichard/0ad0de1feb6adb9eb61a/) eine ausfuhrliche Beschreibung dazu.

## 5.1 Autostart uber init.d

Erstellt zunachst eine neue Datei unter „_/etc/init.d/_" uber sudo nano/etc/init.d/homebridge, welche ihr mit folgendem Inhalt fullt:

```
#!/bin/sh
### BEGIN INIT INFO
# Provides: homebridge
# Required-Start:    $network $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO
dir="/home/pi"
cmd="DEBUG=* /usr/local/bin/homebridge"
user="pi"
name=`basename $0`
pid_file="/var/run/$name.pid"
stdout_log="/var/log/$name.log"
stderr_log="/var/log/$name.err"
get_pid() {
    cat "$pid_file"
}
is_running() {
    [ -f "$pid_file" ] && ps `get_pid` > /dev/null 2>&1
}
case "$1" in
    start)
    if is_running; then
        echo "Already started"
    else
        echo "Starting $name"
        cd "$dir"
        if [ -z "$user" ]; then
            sudo $cmd >> "$stdout_log" 2>> "$stderr_log" &
        else
            sudo -u "$user" $cmd >> "$stdout_log" 2>> "$stderr_log" &
        fi
        echo $! > "$pid_file"
        if ! is_running; then
            echo "Unable to start, see $stdout_log and $stderr_log"
            exit 1
        fi
    fi
    ;;
    stop)
    if is_running; then
        echo -n "Stopping $name.."
        kill `get_pid`
        for i in {1..10}
        do
            if ! is_running; then
                break
            fi
            echo -n "."
            sleep 1
        done
        echo
        if is_running; then
            echo "Not stopped; may still be shutting down or shutdown may have failed"
            exit 1
        else
            echo "Stopped"
            if [ -f "$pid_file" ]; then
                rm "$pid_file"
            fi
        fi
    else
        echo "Not running"
    fi
    ;;
    restart)
    $0 stop
    if is_running; then
        echo "Unable to stop, will not attempt to start"
        exit 1
    fi
    $0 start
    ;;
    status)
    if is_running; then
        echo "Running"
    else
        echo "Stopped"
        exit 1
    fi
    ;;
    *)
    echo "Usage: $0 {start|stop|restart|status}"
    exit 1
    ;;
esac
exit 0
```

Anschließend andert ihr noch die Benutzerrechte und installiert das erstellte Script:

Ihr konnt nun HomeBridge ganz einfach uber sudo /etc/init.d/homebridge start starten. Beim Systemstart sollte HomeBridge zudem nun automatisch gestartet werden. Die Ausgaben von HomeBridge findet ihr nun ubrigens unter „_/var/log/homebridge.log_" bzw. "_/var/log/homebridge.err_".

Damit ist die Grundinstallation vom HomeKit abgeschlossen. Im nachsten Artikel geht es dann um die Konfiguration und Erweiterung der Installation. Dabei werde ich insbesondere auf das Steuern von Funksteckdosen uber Raspberry-Remote eingehen und zeigen, wie sich Sensoren einbinden lassen.

_**Tipp**: Ihr konnt die Push-Benachrichtigung eures Browsers verwenden, um uber neue Artikel benachrichtigt zu werden. Akzeptiert dazu einfach die Meldung eures Browsers beim Aufruf dieser Seite und ihr werdet automatisch benachrichtigt. Das Abo konnt ihr naturlich jederzeit beenden._
