# HowTo: Homebridge Plugins installieren

_Captured: 2017-05-06 at 10:09 from [timobihlmaier.de](https://timobihlmaier.de/homebridge-plugins-installieren/)_

In meinem letzten Blogeintrag habe ich euch bereits gezeigt, wie Homebridge auf dem Raspberry Pi installiert werden kann, um dadurch Fremdgerate mit Siri fernzusteuern. Falls ihr das Video bzw. den Artikel dazu verpasst habt, solltet ihr diesen unbedingt vorher [hier](https://timobihlmaier.de/homebridge-auf-einem-raspberry-pi-installieren/) ansehen.

Hier wird euch nun gezeigt, wir ihr Plugins installieren und anschließend mit Siri verwenden konnt. Bitte beachtet, dass der Artikel nur als Erganzung zu meinem YouTube-Video gedacht ist.

## Homebridge Plugins aussuchen

Es gibt eine Vielzahl an Plugins, die fur Homebridge geschrieben worden sind und damit euer Fremdgerat mit Apples HomeKit verknupfen.

Eine Übersicht uber samtliche kompatible Plugins findet ihr **[hier](https://timobihlmaier.de/?r=https://www.npmjs.com/browse/keyword/homebridge-plugin)**.

In diesem Beispiel mochte ich das Plugin _homebridge-wakeonlan _installieren. Also wahlt ihr das Plugin entsprechend aus und erhaltet eine kurze Beschreibung des Plugins, eine Installationsanleitung und eine Beispielkonfiguration.

## Plugins installieren

Um ein zuvor ausgesuchtes Plugin zu installieren, muss am Raspberry Pi (am besten per SSH) folgender Befehl eingegeben werden:
    
    
    sudo npm install -g _Pluginname
    _

wobei hierbei _Pluginname _mit dem richtigen Name des Plugins ersetzt wird. In diesem Beispiel also _homebridge-wakeonlan_.

## Konfiguration auslesen

Als nachsten musst ihr in der config.json das jeweilige Plugin konfigurieren.

[alert style="blue"]Da die folgenden Schritte etwas schwer zu beschreiben sind, lege ich euch mein [YouTube-Video](https://youtu.be/Mig0x5MUloI) dazu ans Herz, durch das die Schritte um einiges verstandlicher sind.[/alert]

Zunachst zeigen wir den kompletten Inhalt der aktuellen config.json mit folgenden Befehl an
    
    
    cat .homebridge/config.json
    

und kopieren den gesamten Inhalt der Datei in die Zwischenablage (also den Inhalt markieren und mit STRG+C kopieren).

Zur Vermeidung von Fehlern empfehle ich, den kopierten Inhalt in einen [JSON Formatter](https://timobihlmaier.de/?r=https://jsonformatter.curiousconcept.com/) zu kopieren, um Syntax-Fehler zu vermeiden.

## Konfiguration anpassen

Jetzt kopiert ihr den Inhalt, den ihr auf der Pluginseite unter Configuration findet, in den bereits zuvor eingefugten config.json Inhalt auf der JSON Formatter ein.

Dabei ist die Position wichtig. Hier unterscheiden wir zwischen zwei Arten:

  * Accessories: sind die Plugins, bei denen die Configuration mit _„accessories": [_ beginnt
  * Platforms: sind die Plugins, bei denen die Configuration mit _„platforms": [_ beginnt

Je nachdem, wie die Datei beginnt, musst ihr den Inhalt der Configuration ab der ersten geoffneten geschweiften Klammer (also { ) bis zur letzten geschlossenen geschweiften Klammer kopieren. Danach entsprechend under Accessories oder Platforms einfugen.

Wichtig ist aber, dass jedes Plugin nach der letzten geschlossenen geschweiften Klammer ein Komma hat, bis auf das letzte.

Wenn ihr also nur ein Plugin verwendet, muss kein Komma folgen. Sofern ihr aber z.B. drei verwendet, muss auf das erste und zweite Plugin ein Komma folgen. Nur nicht auf das dritte, da dies das letzte Plugin ist.

Solltet ihr dies nicht richtig verstanden haben, solltet ihr mein Video dazu ansehen, das es eindeutiger macht.

Zuletzt pruft ihr, ob die Konfiguration korrekt ist und keine Syntaxfehler enthalt. Dazu klicken wir auf _Validate _im JSON Formatter. Sofern alles richtig ist, erscheint keine Fehlermeldung und der Text kann in die Zwischenablage kopiert werden.

## Konfiguration einfugen

Nachdem ihr nun die config.json richtig mit den neuen Plugins konfiguriert habt, musst ihr die Konfiguration noch abspeichern.

Die beste Methode dazu ist, zuerst die config.json zu loschen. Dies geht mit
    
    
    sudo rm .homebridge/config.json
    

Nun ist die Datei geloscht und wir erstellen sie erneut mit dem neuen Inhalt. Dazu geben wir
    
    
    sudo nano .homebridge/config.json
    

ein und fugen die im JSON Formatter erstelle Konfiguration ein. Dies geht entweder mit STRG+V oder je nach Programm auch mit einem einfachen Rechtsklick.  
Anschließend kann die Konfiguration mit STRG+O abgespeichert und mit STRG+X geschlossen werden.

## Homebridge starten

Im letzten Schritt konnt ihr nun Homebridge startet. Um auf mogliche Fehler hingewiesen zu werden, geben wir dazu zunachst
    
    
    sudo homebridge
    

ein. So konnt ihr direkt sehen, ob eure Plugins auch wirklich erfolgreich geladen worden sind (dann seht ihr _plugin loaded: Pluginname_ ). Falls Fehler erscheinen solltet und ihr diese nicht selbst beheben konnt, konnt ihr diese gerne in den Kommentaren posten, damit ich euch weiterhelfen kann. Normalerweise sollte aber alles direkt funktionieren.

Dann beenden wir wieder mit STRG+C und starten uber das Autostart-Skript den Server mit
    
    
    sudo /etc/init.d/homebridge start
    

## Homebridge mit Siri verknupfen

Jetzt habt ihr erfolgreich euer eigenes HomeKit eingerichtet, das ihr nur noch mit der Home-App von Apple auswahlen und mit Siri verknupfen musst.

Da dies deutlich einfach durch ein Video beschrieben wird, verweise ich euch hier erneut auf mein YouTube-Video.

Sofern ihr nun noch Fragen oder Anregungen habt, konnt ihr dies gerne in den Kommentaren fragen. Auch wurde ich mich uber Vorschlage zu neuen Anleitungen sehr freuen.
