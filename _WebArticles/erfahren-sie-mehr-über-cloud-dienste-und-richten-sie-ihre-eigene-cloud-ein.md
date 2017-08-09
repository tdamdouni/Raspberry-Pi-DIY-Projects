# Erfahren Sie mehr über Cloud-Dienste und richten Sie Ihre eigene Cloud ein.

_Captured: 2017-05-06 at 16:45 from [eigene-cloud-einrichten.de](https://eigene-cloud-einrichten.de/)_

Willkommen auf Eigene-Cloud-einrichten.de, einem der fuhrenden deutschen Portale zur Information uber eine eigene, private Cloud.

Es gibt ganz unterschiedliche Wege, wie Sie zu Ihrer eigenen Cloud kommen konnen:

  1. **Cloud fur unter 100 € zu Hause:** Sie folgen der Anleitung auf dieser Seite und wir zeigen Ihnen Schritt fur Schritt wie Sie mit technischem Grundwissen einen Raspberry Pi als Cloud-Server einrichten - mit der Cloud-Software Ihrer Wahl (z.B. [Nextcloud](https://eigene-cloud-einrichten.de/nextcloud-der-owncloud-fork-vorgestellt))  

  2. **Fertig eingerichteter Cloud-Server fur zu Hause:** Sie wollen gerne einen kleinen Cloud-Server fur zu Hause ohne Einrichtungsaufwand? Erfahren Sie mehr uber [alternative Cloud-Hardware](https://eigene-cloud-einrichten.de/cloud-server-im-ueberblick)  

  3. **Dropbox Alternativen/Cloud-Hoster:** Der Cloud-Server soll lieber nicht zu Hause stehen? Verschaffen Sie sich einen Überblick uber [Cloud-Hoster](https://eigene-cloud-einrichten.de/cloud-dienste), bei denen ein monatlicher Betrag fallig wird  

  4. **Losungen fur Unternehmen:** Es soll keine private Cloud werden? [Professionelle Cloud-Hoster fur Unternehmen](https://eigene-cloud-einrichten.de/business-cloud) haben wir auch fur Sie zusammengestellt

Sie haben sich also fur die **private Cloud** entschieden? In diesem ausfuhrlichen Artikel werden wir uns intensiv mit der Einrichtung eines kleinen Servers beschaftigen, sodass Sie schon bald Ihren eigenen Cloud-Server zu Hause stehen haben konnen. Naturlich reden wir auch uber die Vor- und Nachteile einer eigenen, privaten Cloud.

Haufig gestellte Fragen rund um eine eigene Cloud und die entsprechenden Antworten finden Sie in unserer [FAQ](https://eigene-cloud-einrichten.de/haeufig-gestellte-fragen-rund-um-die-eigene-cloud-faq).

### Inhaltsubersicht

  1. Einrichtung einer eigenen Losung 

### 1\. Was ist eine Cloud?

![](https://eigene-cloud-einrichten.de/img/artikel/cloud-personen-julia-timm-fotolia.png)

> _Was meint man eigentlich, wenn man von "Cloud" spricht? Foto: Julia Timm - Fotolia.com_

Womoglich wissen Sie noch gar nicht, was eine Cloud uberhaupt ist. Deshalb mochte ich Ihnen das zuerst erklaren.

Der Begriff "Cloud" steht fur eine Abkurzung des sogenannten Cloud Computing, das sich in den letzten Jahren immer großerer Beliebtheit erfreut.

Die Cloud kann zahlreiche unterschiedliche Dienstleistungen beherbergen. Hierbei handelt es sich um abstrakte Struktur, schließlich ist dem Nutzer nicht bekannt (und ist es fur ihn auch nicht relevant) wie viele Server in dieser Wolke fur ihn arbeiten. Wenn Sie etwas in der "Cloud" speichern, verwenden Sie einen Service, der mit den Servern Ihres Anbieters kommuniziert und die Daten dort ablegt. Mehr erfahren Sie in dem Artikel: [Was ist eine Cloud?](https://eigene-cloud-einrichten.de/was-ist-eine-cloud-cloud-computing-erklaert)

Auf dieser Seite sprechen wir haufig von Ihrer eigenen Cloud. Es soll dabei nicht darum gehen, selbst ein großes Server-Netzwerk aufzubauen, um verschiedene Prozesse durchzufuhren. Wenn Sie sich dieses Tutorial durchlesen, sollte Ihr Wunsch sein, einen eigenen kleinen Server einzurichten, sodass Sie ihre **Daten darauf bequem speichern und synchronisieren** konnen. Es geht uns also nur den Speicherplatz in einer Cloud.

### 2\. Vor- und Nachteile einer eigenen Cloud

Die großen Anbieter, wie z.B. Dropbox, Google Drive, iCloud & Co., verfugen uber zahlreiche Server und beherbergen die Dateien von Millionen von Nutzern. Doch damit entstehen auch einige Probleme.

_**Wie** konnen Sie sicher sein, dass Ihre Dateien dort nicht von anderen eingesehen werden? **Wie** konnen Sie den Zugriff von Geheimdiensten auf Ihre sensiblen Dokumente verhindern, wenn Sie keine Kontrolle uber die Server haben?_

Die kurze Antwort auf diese Fragen lautet: Leider (fast) gar nicht. Sie mussen sich auf diese Anbieter verlassen. Das fallt schwer. Insbesondere dann, wenn Google, Dropbox & Co. Ihre Server in den USA oder als US-amerikanisches Unternehmen betreiben.

Die Bevolkerung ist sensibler im Umgang mit Ihren Daten geworden, seit bekannt wurde, dass US-Behorden etwa durch das sog. [PRISM-Programm](https://de.wikipedia.org/wiki/PRISM_%28%C3%9Cberwachungsprogramm%29) auf die Server von großen IT-Unternehmen, die in den USA angesiedelt sind, zugreifen konnen. Viele der großeren Cloud-Anbieter sitzen in den USA: Google mit [Google Drive](https://drive.google.com/), die [Dropbox](https://www.dropbox.com/), Microsoft mit [SkyDrive](http://windows.microsoft.com/de-de/skydrive/download), Apple mit [iCloud](https://www.icloud.com/) und viele weitere. Dort abgelegte Dateien sind haufig nicht verschlusselt.

Vieles auf dieser Welt hat seinen Wert und **seinen Preis**. Daher sollten Sie sich auch immer fragen, wie ein Cloud-Dienst die gigantischen IT-Infrastrukturen finanzieren kann. Es mag - auch US-amerikanische - Dienste geben, die Ihre Daten schutzen und die ab einer gewissen Speichermenge kostenpflichtige Tarife anbieten. Es gibt aber genau so Dienste, die sich fur Ihre Daten interessieren - das konnen sowohl Cloud-Dienstleister als auch Geheimdienste sein.

Mal angenommen, Sie speichern in Ihrem Cloud-Account **private Bilder, Erinnerungen und Dokumente**, die Sie zur Ausfuhrung Ihrer Arbeit benotigen. Mochten Sie es wirklich hinnehmen, dass ein Cloud-Dienst oder ein Geheimdienst auf diese Daten zugreifen kann? Fuhlt es sich nicht besser an, wenn Sie wissen, dass Ihre Daten auch physikalisch bei Ihnen im eigenen Haus lagern? Sollte es nicht so sein, dass Sie die volle Kontrolle uber Ihre eigenen Daten haben?

Wenn Ihr eigener Cloud-Service Sie Hunderte von Euro kosten _wurde_, dann ware er wohl keine ernsthafte Alternative. Doch dem ist nicht so. Mit einer der hier vorgestellten eigenen, privaten Cloud konnen Sie sogar **Geld sparen** gegenuber Online Cloud Dienstleistern.

Ich habe einmal alle **Vorteile dieser Losung** fur Sie zusammengetragen:

  * **Ihre Daten liegen bei Ihnen**  
Der kleine Rechner, den wir Ihnen im Laufe des Artikels vorstellen werden, kann bei Ihnen zu Hause aufgestellt werden. Ihre Daten liegen also wirklich bei Ihnen. Wenn ein Geheimdienst an Ihre Daten wollte, musste er schon in das System oder in Ihr Haus einbrechen.  

  * **Sie sind unabhangig**  
Sie sind nicht mehr langer abhangig von US-amerikanischen Cloud-Dienstleistern. Es spielt fur Sie keine Rolle mehr, ob sich die Preise eines Accounts bei einem dieser Anbieter erhohen, denn Sie bezahlen nur, wie gewohnt, fur Ihren Zugang zu Internet, die Stromkosten und einmalig den Einkaufspreis fur einen kleinen Server.  

  * **Sie haben die volle Kontrolle**  
Den Speicherplatz, den Sie zur Verfugung haben, konnen Sie auch auf verschiedene Benutzer verteilen. So konnen auch andere Mitglieder Ihrer Familie in den Genuss Ihres eigenen Cloud-Servers kommen.  

  * **Sie bezahlen fur etwas Materielles**  
Bei der monatlichen oder jahrlichen Gebuhr eines Cloud-Anbieters bekommen Sie fur diesen Zeitraum den Speicherplatz zur Verfugung gestellt. Endet der Vertrag, so haben Sie auch keinen Zugriff mehr auf den Speicherplatz.  
  
Fur Ihre eigene Cloud mussen Sie nur einmal (abgesehen von Gebuhren wie dem Internetanschluss, siehe "Gebuhren") bezahlen und halten anschließend etwas in der Hand. Wenn Sie die Cloud nicht mehr verwenden mochten, konnen Sie die dafur bestellten Gerate auch anderweitig verwenden. Zum Beispiel fur Ihren [eigenen MediaServer](https://raspberry.tips/raspi-media-center/raspberry-pi-als-media-server-mit-minidlna-einrichten/).  

  * **Sie sparen oft Geld**  
Wenn Sie uber 5 oder 10 GigaByte benotigen, mussen Sie in vielen Fallen bereits bei den Cloud-Dienstleistern bezahlen. So ist Ihre eigene Cloud auf Dauer gunstiger.

### Nachteile einer eigenen Cloud

Doch sollten Sie auch der Nachteile bewusst sein, die eine eigene Cloud bietet:

  * **Einrichtung benotigt etwas Zeit & Wissen**  
Um die eigene Cloud einzurichten, benotigen Sie etwas Zeit. Ich bin bemuht, Ihnen mit dieser Anleitung alles notige Wissen fur die Einrichtung zu vermitteln. Wenn Sie diesem Artikel also Schritt fur Schritt folgen, konnen Sie die Cloud nach dieser Anleitung und innerhalb von einigen Minuten bis Stunden einrichten. Ein gewisses technisches Grundverstandnis sollte jedoch vorhanden sein.  
  
Außerdem mussen Sie selbst regelmaßig Updates der Software durchfuhren.  

  * **Sie sind fur Ihre Daten verantwortlich**  
Die oben angesprochene Kontrolle ist auch ein Nachteil. Sie sollten sich bewusst sein, dass die in Ihrer Cloud abgelegte Daten nur auf dem Speicher des kleinen Rechners abgelegt sind. Sollte also bei Ihnen eingebrochen werden oder sollten Teile des eigenen Servers vernichtet werden, sind diese Daten aus Ihrer Cloud unwiderruflich geloscht.  
  
Die hier empfohlenen Systeme bieten einen Grundschutz gegen Hackerangriffe. Doch genau so wie es nicht unmoglich ist, einen Account bei einem Cloud-Anbieter zu knacken, so kann dies auch bei Ihrer eigenen Cloud geschehen und Sie sind dafur verantwortlich. Da Ihre Cloud eben nicht so bekannt ist wie Dropbox & Co. schwimmt sie unter dem Radar und ist fur Hacker in der Regel nicht so interessant.  

  * **Geschwindigkeitseinbußen moglich**  
Nehmen wir an, Sie haben einen Internettarif, der Ihnen 16 MBit/s (Download) und etwa 2 MBit/s (Upload) garantiert. Wenn Sie also Daten zu einem der oben angesprochenen Daten hochladen, zum Beispiel der Dropbox, konnen Sie diese mit maximal 2 MBit/s hochladen. Auch bei Ihrer eigenen Cloud konnen Sie mit maximal 2 MBit/s (etwa 0,25 MegaByte pro Sekunde) hochladen, wahrend die Cloud gleichzeitig theoretisch bis zu 8-mal so viel (16 MBit/s) herunterladen, also empfangen konnte.  
  
Nach dieser Rechnung spielt es fur die Geschwindigkeit keine Rolle, ob Sie auf eine eigene Cloud oder einen Cloud-Anbieter zuruckgreifen, jedoch ist der kleine Rechner, der Ihnen als Server dienen wird, und die darauf installierte Software nicht so leistungsfahig wie die Hard- und Software eines Cloud-Anbieters. Das Synchronisieren mit Ihrer eigenen Cloud (z.B. auf dem Handy oder auf dem PC) kann daher etwa langsamer von statten gehen. Nach meinen Erfahrungen geschieht dies dennoch in einem akzeptablen Tempo.  

  * **Teilen schwierig**  
Wenn Sie intensiv Inhalte mit Freunden uber die Cloud teilen mochten, sollten Sie auf einen leistungsstarken Server setzen. Dazu finden Sie mehr Information in dem [Artikel uber Cloud-Hardware](https://eigene-cloud-einrichten.de/cloud-server-im-ueberblick).

Sie sind von den Vorteilen Ihrer eigenen Cloud uberzeugt oder zumindest neugierig? Dann will ich Ihnen jetzt zeigen, wie Sie Ihre eigene Cloud aufbauen konnen, und was Sie dafur benotigen.

### 3.1 Die Voraussetzungen

Folgende Voraussetzungen mussen erfullt sein:

  * Sie benotigen einen **Internetanschluss**, der rund um die Uhr aktiv ist, und einen Router mit LAN-Anschluss. Das wird bei Ihnen in der Regel gegeben sein.  

  * Sie mussen uber **grundlegende PC-Kenntnisse** verfugen, wenn Sie dieser Anleitung folgen.  

  * Sie mussen einmalig in ein Server-System **investieren**. Die entsprechenden Produkte finden Sie ebenfalls auf dieser Seite.

### 3.2 Einmalig benotigt

Egal fur welches Server-System Sie sich entscheiden, Sie brauchen fur die Konfiguration und Einrichtung **einmalig** und fur nur einige Minuten die folgenden Dinge:

  * Eine Tastatur - nach Moglichkeit ein Kabeltastatur, da diese weniger Strom benotigt. Ein Beispiel dafur ist diese [Logitech Tastatur](https://eigene-cloud-einrichten.de/link/10)*.  

  * Ein HDMI-Kabel und einen HDMI-Monitor. Ein handelsublicher Fernseher mit HDMI-Anschluss und Kabel ist ausreichend.  

  * microSD-Karten-Leser. In der Regel ist ein handelsublicher SD-Karten-Leser mit microSD-Adapter ausreichend.

### 3.3 Raspberry Pi als Cloud-Server verwenden

Bei dem [Raspberry Pi](http://www.amazon.de/gp/product/B01CCOXV34/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B01CCOXV34&linkCode=as2&tag=wwco-21)* handelt es sich um einen kleinen und minimalistischen Computer. Er ist zwar langst nicht so leistungsstark wie ein handelsublicher Rechner, kostet aber weniger als 50 Euro und reicht als einfacher Cloud-Server vollkommen aus. Zusammen mit dem anderen Zubehor kommen Sie auf etwa 100 Euro.

Im Folgenden finden Sie eine Übersicht, der Produkte, die Sie benotigen werden. Per Klick auf den Kaufen-Button konnen Sie diese Produkte bei Amazon.de erwerben.

In jedem Fall werden Sie den **Raspberry Pi**, ein **passendes Gehause** und das entsprechende **Netzteil** benotigen:

Naturlich benotigen Sie auch noch etwas Speicher fur Ihre Cloud. Das Raspberry Pi-Betriebssystem benotigt etwa 8 GB. Um die notwendige Speicherkarten-Große zu berechnen, gilt folgendes: 8 GB + Ihr gewunschter Cloud-Speicher = Speicher-Karten-Große.

Benotigen Sie mehr als 55 GB Cloud-Speicher, sollten Sie auf eine externe Festplatte - mit eigenem Lade-Kabel - setzen. Dann benotigen Sie nur eine 8 GB microSD-Karte. Legen Sie dann bei der Installation der Cloud-Software statt _/var/www/cloud_ ein Verzeichnis auf dieser Festplatte, z.B. _/media/festplatte/cloud_, fest. Eine Anleitung dazu finden Sie beispielsweise [hier](http://jankarres.de/2013/01/raspberry-pi-usb-stick-und-usb-festplatte-einbinden/) (auch optionalen Schritt 6 ausfuhren und am Ende mit den Befehlen chown und chmod die Rechte - wie unter [3.3.5](https://eigene-cloud-einrichten.de/) setzen).

Bei der microSD-Karte gilt: Je hoher die Schreib- und Lesegeschwindigkeit ist, desto schneller kann Ihre Cloud Dateien verarbeiten.

Falls Sie keine **microSD-Karte** in der entsprechenden Große haben, sollten Sie sich eine bestellen. Außerdem wird ein **LAN-Kabel** benotigt. Hier zwei Vorschlage, falls Sie eines der beiden Produkte noch nicht haben:

Die bestellten Artikel sind da? Gut, dann kann es los gehen.

### 3.3.1 Betriebssystem kopieren

Rufen Sie [diese Internetseite](http://www.raspberrypi.org/downloads) auf. Wahlen Sie **Raspbian** und anschließend **Raspbian Jessie Lite** aus. Per Klick auf "Download ZIP" downloaden Sie die Datei.

Verbinden Sie das SD-Karten-Lesegerat mit Ihrem PC und stecken Sie die bestellte SD-Karte in den entsprechenden Slot. Die Karte sollte nun von Ihrem PC erkannt werden.

Überprufen Sie das Dateisystem der SD-Karte. Unter Windows rufen Sie dafur "Computer" auf und klicken mit der rechten Maustaste auf "Wechseldatentrager" (wenn es mehrere Eintrage gibt, sollten Sie prufen, welcher mit dem Einstecken Ihrer SD-Karte hinzugekommen ist). Per Klick auf "Eigenschaften" werden Ihnen Informationen uber die Karte angezeigt. Wenn dort "Dateisystem: FAT32" steht, konnen Sie den nachsten Absatz ignorieren.

Sollte bei Ihnen ein anderes Dateisystem stehen, so schließen Sie das Fenster "Eigenschaften von Wechseldatentrager" und klicken Sie noch einmal mit der rechten Maustaste auf den Eintrag "Wechseldatentrager". Klicken Sie nun "Formatieren..." und wahlen Sie unter Dateisystem "FAT32". Mit Klick auf "Starten" wird mit der Formatierung begonnen. Sobald der Vorgang abgeschlossen ist, konnen Sie fortfahren.

![Screenshot: Image Writer für Windows](https://eigene-cloud-einrichten.de/img/artikel/image_writer_windows.png)

Laden und entpacken Sie den [Image Writer for Windows](https://www.heise.de/download/product/win32-disk-imager-92033/download). Starten Sie die .exe Datei per Doppelklick. Nun offnet sich das Programm Fenster. Klicken Sie auf den mit "1."-gekennzeichneten Button, und wahlen Sie die in Schritt 1 heruntergeladene Datei aus. Geben Sie unter "2." den Laufwerkbuchstaben Ihrer SD-Karte an und klicken Sie anschließend auf "Write" ("3.").

Das Betriebssystem wird nun auf die SD-Karte geschrieben. Das kann eine Weile dauern. Sollten Sie vorher noch einen Hinweis zu sehen bekommen, so bestatigen Sie und fahren Sie fort.

Wenn Sie einen Mac verwenden, lauft es etwas anders ab. Dieses auf Youtube veroffentlichte [Video-Tutorial](http://www.youtube.com/watch?v=MMtV15B0PAE) zeigt Ihnen, wie Sie die SD-Karte formatieren konnen. Außerdem konnen Sie zum Beispiel [diesen Image Writer](http://download.cnet.com/Apple-ImageWriter/3000-2112_4-349.html) verwenden, um an Ihrem Mac die SD-Karte zu beschreiben.

### 3.3.2 Den Raspberry Pi einrichten

Wenn Sie die Hulle geoffnet haben, sollten Sie, wie [hier beschrieben](http://www.raspberrypi.org/quick-start-guide), zunachst die SD-Karte in den Schlitz auf der Unterseite einfuhren. Nun konnen Sie den Raspberry Pi vorsichtig in der Hullenunterseite verankern und die Oberseite der Hulle daruber stulpen.

Verbinden Sie das HDMI-Kabel mit dem Raspberry Pi und Ihrem HDMI-Monitor. Nutzen Sie außerdem einen der USB-Slots, um eine schnurgebundene Tastatur anzuschließen. Außerdem sollten Sie ein Ende des LAN-Kabels mit Ihrem Router (z.B. Fritz!Box) und das andere mit dem Raspberry Pi verbinden.

Wenn Sie das getan haben, kann es losgehen. Stecken Sie das Netzteil in die Steckdose und verbinden Sie das andere Ende mit dem dafur vorgesehenen Anschluss am Raspberry Pi. Dieser schaltet sich nun automatisch an.

![Raspberry Pi: Konfiguration und Inbetriebnahme anhand eines Screenshots](https://eigene-cloud-einrichten.de/img/artikel/raspi_config.png)

Nach einem kurzen Ladevorgang sollte die folgende Oberflache (siehe Abbildung) erscheinen. Hier konnen Sie nun einige Einstellungen vornehmen.

Zunachst sollten Sie die Sprache andern. Wahlen Sie dafur mit den Pfeiltasten **"Internationalisation Options"** aus und bestatigen Sie mit der Enter-Taste. Wahlen Sie zuerst "Change Locale". Eventuelle Nachfragen bestatigen Sie mit der Enter-Taste. Nutzen Sie die Pfeiltasten, um zu dem Eintrag "de_DE.UTF-8 UTF-8" zu scrollen und betatigen Sie die Leertaste um den Eintrag auszuwahlen. Mit Enter bestatigen Sie, eventuell mussen Sie zuvor noch die Tab-Taste drucken.

Die Menueintrage werden Ihnen eventuell jetzt schon auf Deutsch angezeigt. Beachten Sie daher die Zahlen links neben den Eintragen, wenn Sie dieser Anleitung folgen. Wahlen Sie nun erneut Eintrag 4 aus und anschließend I2. Dort wahlen Sie durch scrollen ebenfalls die passenden Eintrage aus und bestatigen jeweils mit Enter.

Nun mussen Sie noch das **Tastatur Layout** anpassen. Rufen Sie dafur erneut Menu 4 auf und dieses Mal I3. Nach einigen Sekunden gelangen Sie wieder in das Hauptmenu.

Wahlen Sie als Nachstes mittels der Pfeiltasten den Eintrag 1 aus und bestatigen Sie mit der Enter-Taste. Warten Sie nun einige Zeit.

Ist der Vorgang abgeschlossen, konnen Sie das **Benutzer-Passwort andern**. Wahlen Sie Eintrag 2 aus und drucken Sie 2x Enter. Sie werden nun nach einem neuen Passwort gefragt. Denken Sie sich ein sicheres Passwort aus oder nutzen Sie einen [Passwort Generator](https://60tools.com/de/tool/password-generator). Geben Sie Ihr Passwort ein (moglichst ohne Umlaute, z und y). Lassen Sie sich nicht davon irritieren, dass wahrend der Eingabe nichts passiert. Wenn Sie fertig sind bestatigen Sie mit Enter, geben das Passwort erneut ein und bestatigen nochmals mit Enter. Beim Anzeigen der Meldung drucken Sie noch einmal die Enter-Taste.

Wahlen Sie nun den Menupunkt Nummer 4 aus. Bei der darauf folgenden Abfrage nutzen Sie die Pfeiltasten um den Eintrag "No" zu markieren und bestatigen mit Enter.

Starten Sie jetzt die "Advanced Options" und rufen Sie anschließend den Menupunkt **"SSH"** auf. Wenn "Enable" hervorgehoben wurde, konnen Sie mit Enter bestatigen, nutzen Sie ansonsten die Pfeiltasten. Um die nachfolgende Meldung zu schließen verwenden Sie die Enter-Taste. In dem "Advanced Options"-Menu sollten Sie außerdem den dritten Eintrag (**"Memory Split"**) auswahlen. Geben Sie anschließend 16 ein.

Navigieren Sie mit den Pfeil-Tasten so, dass der Eintrag "Finish" hinterlegt ist und bestatigen Sie mit Enter. Geben Sie das folgende Kommando ein, um den Pi neu zu starten:
    
    
    sudo shutdown -r

Nach dem Booten werden Sie nach dem Benutzernamen ("pi") und Ihrem neuen Passwort gefragt. Geben Sie zuerst den Benutzernamen ein, bestatigen Sie mit Enter und machen Sie schließlich das gleiche bei der Eingabe des Passworts.

Zunachst wollen wir den Raspberry Pi auf den neuesten Stand bringen, geben Sie dafur das Kommando ein:
    
    
    sudo apt-get update

und wenn der Vorgang abgeschlossen ist:
    
    
    sudo apt-get upgrade

Sollten Sie auf Englisch gefragt werden, ob Sie fortfahren wollen, so drucken Sie einfach Enter. Moglicherweise mussen Sie sich nun eine Weile gedulden.

### 3.3.3 Webserver einrichten

Damit Ihr Raspberry Pi und damit auch Ihre Cloud PHP-Skripte ausfuhren kann und uber das Internet erreichbar ist, mussen Sie zunachst einen Webserver einrichten. Wir verwenden hierfur [nginx](http://nginx.org/en/).
    
    
    sudo apt-get install nginx php5-fpm php5-mysql mysql-server

Sobald Sie gefragt werden, ob Sie fortfahren mochten, bestatigen Sie durch Drucken der Enter-Taste. Wahrend der Installation wird ein blaues Fenster erscheinen und Sie zur Eingabe eines Passworts auffordern. Geben Sie ein sicheres Passwort ein und notieren Sie es. Falls notwendig, geben Sie es anschließend erneut ein. Weiter geht es dann mit der (Tab und) Enter-Taste.

Anschließend installieren Sie durch Eingabe dieses Befehls noch einige benotigte Pakete. Darunter ist auch der Editor vim, mit dem Sie Dateien bearbeiten konnen. Wenn erforderlich, bestatigen Sie auch hier eventuelle Nachfragen mit Hilfe der Enter-Taste.
    
    
    sudo apt-get install php-pear php-xml-parser php5-cli php5-gd php5-intl php5-curl vim openssl

Öffnen Sie die PHP-Konfigurationsdatei mit dem folgenden Befehl:
    
    
    sudo vi /etc/php5/fpm/pool.d/www.conf

Sie sollten einen "listen"-Zeile _ohne_ ";" davor finden. Ändern Sie die Zeile gegebenenfalls ab (zB von "listen = /var/run/php5-fpm.sock"), sodass sie wie folgt aussieht:
    
    
    listen = 127.0.0.1:9000
    

Durch [Einfg] konnen Sie die Zeile entsprechend bearbeiten. Drucken Sie anschließend [Esc], geben Sie ":wq" ein und drucken Sie [Enter] um die Datei zu speichern.

### 3.3.4 Port-Freigabe & Dynamisches DNS

Damit sichergestellt ist, dass Sie von außen auf Ihren Server zugreifen konnen, mussen Sie in Ihrem Router eine sogenannte **Port-Freigabe** einrichten. Dies unterscheidet sich von Router zu Router. Zunachst mussen Sie jedoch Ihre IP-Adresse kennen. Geben Sie dafur auf dem Raspberry Pi folgendes ein:
    
    
    ifconfig

Irgendwo in der Ausgabe wird so ein ahnlicher Eintrag zu finden sein: "inet Adresse:_192.168.178.47_". Das Unterstrichene, in Ihrem Fall sieht das vermutlich anders aus, ist Ihre lokale IP-Adresse.

Richten Sie jetzt auf Ihrem Router eine (HTTPS)-Port-Freigabe (TCP) fur den Eingangsport 443, Ausgangsport 443 und den Rechner mit Ihrer lokalen IP-Adresse ein. Je nach Router-Modell ist dies unterschiedlich, hier Anleitungen fur einige Router:

  * Andere Modelle: Suchen Sie nach "Port-Freigabe" und dem Namen Ihres Routers, um eine passende Anleitung zu finden

In der Regel werden Sie eine dynamische IP-Adresse haben. Ihre IP wird sich also regelmaßig andern. Deshalb mussen Sie einen sogenannten dynamischen DNS-Anbieter auswahlen. Wahlen Sie einfach einen von diesen Anbietern aus:

Melden Sie sich nun bei einer dieser Seiten fur einen kostenlosen Tarif an. Dort werden Sie einen sogenannten **Hostnamen** anlegen, z.B. "muellercloud.twodns.de". Über diesen Namen ist Ihre Cloud spater erreichbar. Auf der Seite des dynamischen DNS-Anbieters werden Sie haufig auch Informationen vorfinden, um diesen **Anbieter in Ihrem Router einzurichten**.

Dort stehen keine Informationen dazu? Dann probieren Sie es mal uber das Administrationsmenu Ihres Routers (bei der Fritz!Box "fritz.box" im Browser eingeben) und suchen dort nach "Dynamisches DNS". Haben Sie einen solchen Menupunkt gefunden, geben Sie dort ggf. Ihre Login-Daten und Ihren Host-Namen ein.

Sobald Sie sich sowohl bei einem Anbieter registriert als auch diesen korrekt in Ihrem Router eingerichtet haben, konnen wir mit dem nachsten Schritt fortfahren.

### 3.3.5 SSL-Verbindung einrichten

Nun sind Sie fast am Ende dieses Tutorials angekommen. Nach den nachsten zwei Schritten werden Sie einen korrekt konfigurierten, kleinen Server eingerichtet haben. Zunachst aber mussen wir noch dafur sorgen, dass Sie Ihre Dateien via SSL verschlusselt synchronisieren konnen.

Fuhren Sie den folgenden Befehl aus, um ein neues Verzeichnis anzulegen und in dieses zu wechseln:
    
    
    sudo mkdir -p /var/www/{ssl,cloud} && sudo chown -R www-data:pi /var/www && cd /var/www/ssl

Damit auch der Benutzer Pi spater Zugriff auf die Dateien hat, legen wir eine neue Gruppe an, fugen Pi hinzu und andern die Rechte an den Dateien:
    
    
    sudo addgroup pi
    
    
    
    sudo usermod -aG pi pi && sudo chmod -R 775 /var/www/cloud

Mit dem folgenden Befehle erstellen Sie nun ein **SSL-Zertfikat**, welches Sie selbst signieren:
    
    
    sudo openssl req -x509 -nodes -days 9999 -newkey rsa:2048 -keyout cloudssl.key -out cloudssl.crt

Bei Nachfragen bezuglich eines "Challenge-Passwords", Ihres Unternehmens oder etwas anderem, geben Sie einfach die entsprechenden Daten ein und bestatigen Sie mit Enter.

Anschließend nehmen wir die richtige Konfiguration fur PHP vor, um sicherzustellen, dass auch große Dateien problemlos hochgeladen werden konnen. Fuhren Sie dafur den folgenden Befehl aus, der eine fur Sie vorbereitete Datei von unserer Website zu Ihnen herunterladt:
    
    
    sudo wget -q -O /etc/php5/fpm/conf.d/user.ini - https://eigene-cloud-einrichten.de/getPHPINI

Starten Sie nun den Webserver und PHP neu:
    
    
    sudo service nginx restart && sudo service php5-fpm restart

### 3.3.6 MySQL-Datenbank einrichten

Wir werden nun noch eine **MySQL-Datenbank einrichten**. Geben Sie in der Kommando-Zeile Ihres Raspberry Pis den nachfolgenden Befehl ein, und setzen Sie an Stelle der eckigen Klammern das von Ihnen zuvor festgelegte MySQL-Passwort ein. _Wichtig: Die eckigen Klammern bitte in allen folgenden Beispielen auch ersetzen bzw. entfernen!_
    
    
    mysql --user=root --password=[IHR MYSQL-PASSWORT] mysql

Sie sollten jetzt ein "mysql>" sehen konnen. Zunachst erstellen wir eine neue MySQL-Datenbank, den Namen konnen Sie aus Buchstaben, Zahlen und Unterstrichen beliebig wahlen, merken Sie ihn sich jedoch. Folgender Befehl ist dazu notwendig, bestatigt wird mit [Enter]:
    
    
    CREATE database [DATENBANK-NAME, z.B. cloud_db];
    

Anschließend erstellen wir einen neuen MySQL-Benutzer und gewahren ihm alle Rechte auf die Datenbank. Dafur mussen Sie sich einen Benutzernamen und ein MySQL-Benutzer-Passwort ausdenken. Erganzen Sie diese in dem Kommando:
    
    
    GRANT ALL PRIVILEGES ON [DATENBANK-NAME, WIE IM KOMMANDO ZUVOR FESTGELEGT].* TO '[MYSQL-BENUTZER-NAME]'@'localhost'
    

[Enter] drucken und anschließend folgendes eingeben und mit [Enter] bestatigen:
    
    
    IDENTIFIED BY '[MYSQL-BENUTZER-Passwort]';

Kommt jetzt die Meldung "Query OK" haben Sie die MySQL-Datenbank und den Benutzer korrekt eingerichtet. Bitte merken Sie sich alle Daten, da Sie sie spater noch einmal benotigen werden.

In unregelmaßigen Abstanden, sollten Sie Ihren **[Raspberry Pi aktualisieren**](https://eigene-cloud-einrichten.de/haeufig-gestellte-fragen-rund-um-die-eigene-cloud-faq#software-update).

Jetzt sind wir mit dem **ersten Teil des Tutorials fertig...**

### 3.3.7 Cloud-Software

**...fehlt nur noch die Installation einer Cloud-Software**. Dafur haben wir verschiedene [Programme zusammengetragen](https://eigene-cloud-einrichten.de/cloud-software). Rufen Sie den Link auf, um sich dort fur ein Programm zu entscheiden. Per Klick auf "Tutorial" bei der jeweiligen Software finden Sie eine Anleitung, wie diese Software einzurichten ist.

Sie wissen nicht fur welche Cloud-Software Sie sich entscheiden sollen? Dann empfehle ich Ihnen die [Installationsanleitung fur die Owncloud](https://eigene-cloud-einrichten.de/so-installieren-sie-die-owncloud-und-richten-sie-ein), die direkt auf diesem Tutorial aufbaut.

Ähnlich aufgebaut ist ein Owncloud-Ableger, die Nextcloud. Folgen Sie [unserem Nextcloud Tutorial](https://eigene-cloud-einrichten.de/nextcloud-installieren-und-einrichten-so-gehts), um stattdessen die Software zu installieren.

### 3.4 Alternativen

Sollten Sie sich gegen einen Raspberry Pi entschieden haben, etwa weil Sie einen Cloud-Server mit noch besserer Performance benotigen, habe ich hier ein paar **Alternativen** fur Sie zusammengestellt.

**1\. Fertige Cloud-Server**

Fertig eingerichtete Losungen richten sich in der Regel auch an Techniklaien und sind mit deutlich weniger Zeitaufwand eingerichtet. Ein besonderes beliebtes Cloud-System - fur das Sie allerdings zusatzlich eine Festplatte kaufen mussen - sehen Sie rechts.

Mehr uber NAS-Systeme und fertige Server Hardware fur Ihre Cloud gibt es in [dem Server Hardware Vergleich](https://eigene-cloud-einrichten.de/cloud-server-im-ueberblick). Dort finden Sie eine Vielzahl von Geraten im Vergleich.

**2\. Online Cloud-Hoster**

Sie mochten keinen eigenen Server zu Hause stehen haben, der rund um die Uhr laufen soll? Dann ist vermutlich eine Online-Losung das richtige. Dropbox & Co. sind jedoch amerikanische Unternehmen und ermoglichen Ihnen außerdem nur begrenzt Einstellungen an Ihrer Cloud vorzunehmen. Aus diesen Grunden konnen Sie auch eine recht kostengunstige Losung wahlen: einen **Cloud-Hoster**.

Suchen Sie dazu aus dieser [Cloud-Hoster-Übersicht](https://eigene-cloud-einrichten.de/cloud-dienste) einen Hoster aus. Nach der Einrichtung Ihrer eigenen Cloud konnen Sie diese in der Regel uber einen deutschen Webserver nutzen. Der Webserver steht nicht bei Ihnen zu Hause, dafur verlangt der Hoster jedoch geringe Gebuhren fur den Webspace.

### 4\. Fazit zur eigenen Cloud

Wie Sie sehen gibt es mehrere Moglichkeiten eine eigene Cloud einzurichten. Sie konnen dafur einen eigenen, kleinen Server wie etwa den [Raspberry Pi](http://www.amazon.de/gp/product/B01CCOXV34/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B01CCOXV34&linkCode=as2&tag=wwco-21)* oder eine andere Hardware kaufen. Mit der hier veroffentlichten Anleitung ist es auch nicht allzu schwer, so eine Cloud einzurichten.

Eine andere Moglichkeit ist das Verwenden eines Cloud-Hosters. Sie kaufen quasi Speicherplatz im Web und richten dort dann Ihre Cloud ein. Haufig wird Ihnen die Einrichtung dort abgenommen.

Letztendlich entscheiden jedoch Sie, wie Sie Ihre eigene Cloud einrichten wollen.
