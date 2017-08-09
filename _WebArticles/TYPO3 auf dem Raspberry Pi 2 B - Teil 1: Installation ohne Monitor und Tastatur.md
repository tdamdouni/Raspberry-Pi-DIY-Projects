# TYPO3 auf dem Raspberry Pi 2 B - Teil 1: Installation ohne Monitor und Tastatur

_Captured: 2015-12-20 at 14:18 from [www.co-operate.net](http://www.co-operate.net/artikel/article/typo3-auf-dem-raspberry-pi-2-b-teil-1-installation-ohne-monitor-und-tastatur.html)_

Der neue Raspberry Pi 2 B war heute endlich in der Post! Lang genug hat's ja gedauert. Spontane Idee: Die Rechenpower konnte fur einen kleinen TYPO3-Entwicklungsserver reichen...? Aber gerade heute ist kein HDMI-Kabel zurm Ausprobieren da. Na, dann installiere ich Raspbian eben "headless" - ohne Monitor, Tastatur und Maus!

## Die Zutatenliste

  * Micro-SD-Karte (SDHC mit min. 4 GB, besser 16 GB ) 
  * Netzteil und Netzwerkkabel fur den Raspberry Pi.
  * Einen zweiten Rechner (PC, Mac, Linux,...) mit SD-Card-Reader ein und Micro-SD-Adapter.

  * Das aktuelle [NOOBS](http://www.raspberrypi.org/downloads/) (News Out Of the Box Software) mit Raspbian. Kann man von der offiziellen RapsberryPi-Seite herunterladen.
  * Und naturlich den Raspberry Pi 2 B selbst :-)

## Vorbereitungen am PC

Nach dem Entpacken des NOOBS erklart die Datei INSTRUCTIONS-README.txt, wie man die Software auf die Micro-SD-Karte bekommt. Das ist einfach:

Abweichend vom Standard noch ein paar Änderungen an der Installationsroutine, damit die Installation "headless" und vollautomatisch funktioniert. Mangels Tastatur und Monitor (siehe oben) muss ja alles ohne Benutzerinteraktion ablaufen. Dafur:

  * Im Rootverzeichnis der SD-Karte die Datei /recovery.cmdline mit einem Texteditor offnen und die (einzige) Zeile um ein "silentinstall" erweitern: 
    
        runinstaller quiet vt.cur_default=1 elevator=deadline silentinstall

  * Im Verzeichnis os auf der SD-Karte alle Unterverzeichnisse mit Ausnahme von Raspbian loschen.
  * Die Datei os/Raspbian/flavours.json auf der SD-Karte mit einem Texteditor offnen und alle "Flavours" bis auf eine loschen, so dass in der Datei nur Folgendes ubrigbleibt (die supported_hex_revisions konnen naturlich abweichen):  

    
          "flavours": [
    
            {
    
              "name": "Raspbian",
    
              "description": "A Debian wheezy port, optimised for the Raspberry Pi",
    
              "supported_hex_revisions": "2,3,4,5,6,7,8,9,d,e,f,10,11,12,14,19,1040,1041"
    
            }
    
          ]
    
        }

## Weiter am Raspberry Pi

Jetzt die Micro-SD-Karte in den Raspberry Pi stecken, Netzwerkkabel und Stromkabel einstopseln und ca. 20 Minuten warten. So lange dauert namlich die Installation, egal ob "silent", "headless", "unattended" oder anders.

Danach geht es per SSH weiter:

  * Erstmal die IP-Adresse des neuen Raspberry Pi 2 B herausfinden. Gar nicht so einfach ohne Monitor :-) Also doch wieder ein Netzwerk-Scan vom PC aus. Ich nutze dafur den kostenlosen [Angry IP Scanner](http://angryip.org/download/), den gibt's fur alle gangigen Betriebssysteme.
  * Der Login funktioniert ab jetzt per SSH mit: ssh pi@ip.adr.es.se und "raspberry" (dem Standardpasswort).

Feierabend! Morgen geht's weiter mit 'nem Apache Webserver auf dem Raspberry Pi...

## Nachtrag

Wer, wie ich, gerade nur eine eigentlich zu kleine 4GB Speicherkarte hat, kann mit einer Deinstallation der X11-Desktop-Pakete freien Platz schaffen. Der Raspberry Pi soll ja ohnehin ohne Monitor betrieben werden:
    
    
    sudo apt-get remove --purge x11-common
    
    
    sudo apt-get autoremove

Vorsicht: Das ist eine ziemlich radikale Losung. Ggf. werden dabei auch Pakete deinstalliert, die spater doch wieder benotigt werden. Eine großere SD-Karte (oder ein zusatzlicher USB-Stick) waren vielleicht die bessere Wahl...
