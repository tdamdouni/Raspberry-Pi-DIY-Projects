# Raspberry Pi – DropBox benutzen

_Captured: 2017-05-06 at 16:29 from [technik.blogbasis.net](https://technik.blogbasis.net/raspberry-pi-dropbox-benutzen-10-03-2013)_

DropBox ist ein Dateisynchronisationsdienst den bestimmt jeder schon mal genutzt bzw. davon gehort hat. Diesen kann man uber Umwege auch auf dem Rasperry Pi nutzen.

## Die versuchte Installation

Zunachst versuchte ich den Sourcecode des DropBox-Clients zu kompilieren. Das funktionierte auch einwandfrei. Wer dies nachmachen mochte:
    
    
    mkdir ~/dropbox
    cd ~/dropbox
    sudo apt-get install libnautilus-extension-dev python2.7-dev python-gobject-2-dev python-gtk2 python-docutils
    wget "https://www.dropbox.com/download?dl=packages/nautilus-dropbox-1.4.0.tar.bz2"
    tar xfv [Datei]
    cd nautilus-dropbox-1.4.0/
    ./configure
    make
    sudo make install

Danach konnt ihr zwar „dropbox" aufrufen, aber um es benutzen zu konnen, muss man erst den DropBox-Daemon installieren. Hier ist der Knackpunkt: Der Daemon ist proprietar und steht fur ARM-Systeme leider nicht zur Verfugung, sodass ein Aufruf von „dropbox start -i" mit der Fehlermeldung scheitert:
    
    
    Error: Platform not supported

DropBoxl lasst sich uber diesen Weg nicht nutzen. In diesem Fall mussen wir warten, bis DropBox einen Daemon fur die entsprechende Architektur bereitstellt.

## Der Losungsweg uber die API

DropBox bietet eine API an, sodass man auf gewisse Funktionen des Dienstes zugreifen kann. Ein schlauer Kopf hat damit einen [Bash DropBox Client](https://github.com/andreafabrizi/Dropbox-Uploader) geschrieben. Damit kann man zwar nur grundlegende Funktionen, wie z.B. das Hochladen, Herunterladen, Loschen von einzelnen Dateien nutzen, doch das kann bereits ausreichen.

### Installation und Konfiguration des DropBox Uploaders

Wir erstellen uns einen Ordner, klonen das Repository und fuhren das Script aus:
    
    
    mkdir ~/dropbox
    cd ~/dropbox
    rm -rf *
    git clone git@github.com:andreafabrizi/Dropbox-Uploader.git
    ./dropbox_uploader.sh

Nun mussen wir nur noch den Zugriff einrichten. Die Schritte dazu werden vom Script deutlich erklart. Zusammengefasst musst ihr auf die App-Developer Seite von Dropbox, um eine neue App zu erstellen. Die generierten Schlussel mussen dann eingegeben werden. Zuletzt muss man noch den Oauth-Link bestatigen. Damit sollte die Konfiguration abgeschlossen werden.

### Die Nutzung des DropBox Uploaders

Einmal den DropBox Uploader ausgefuhrt und man sieht, was man alles machen kann:
    
    
    pi@raspberrypi ~/dropbox  ./dropbox_uploader.sh
    Andrea Fabrizi - andrea.fabrizi@gmail.com
    Usage: ./dropbox_uploader.sh COMMAND [PARAMETERS]...
    Commands:
    	 upload   [LOCAL_FILE]  <REMOTE_FILE>
    	 download [REMOTE_FILE] <LOCAL_FILE>
    	 delete   [REMOTE_FILE/REMOTE_DIR]
    	 mkdir    [REMOTE_DIR]
    	 list     <REMOTE_DIR>
    	 share    [REMOTE_FILE]
    	 info
    	 unlink
    
    For more info and examples, please see the README file.
    

Demnach kann man nur einzelne Dateien hoch- bzw. herunterladen. Ein Upload von Ordnern konnte man jedoch rekursiv durchfuhren. Man sollte jedoch beachten, dass in den Developer-ToS, welchen man zugestimmt hat, folgendes steht (1.3):

> (b) We may limit the number of calls accepted by the API if we believe that the number of calls to the Dropbox API may negatively impact the Dropbox API or Dropbox service.

Demnach sollte man nicht zu viele API Aufrufe in einer geringen Zeit durchfuhren. Fur die Synchronisation von einigen wichtigen Dateien reicht das Script jedoch vollkommen aus.

~Sebastian
