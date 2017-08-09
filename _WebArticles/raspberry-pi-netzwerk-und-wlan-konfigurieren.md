# Raspberry PI – Netzwerk und Wlan konfigurieren

_Captured: 2017-05-06 at 16:55 from [www.welzels.de](http://www.welzels.de/blog/2012/12/raspberry-pi-netzwerk-und-wlan-konfigurieren/)_

Wie bereits in vorangegangenen [Kapitel](http://www.welzels.de/blog/projekte/raspberry-pi/raspberry-pi-die-erste-installation/) erwahnt, habe ich weder Monitor noch Tastatur an meinem Raspberry PI angeschlossen und auch keine Lust im Schneidersitz mit Tastatur auf dem Schoß, vor dem Fernseher sitzend die weitere Konfiguration durchzufuhren. Daher erfolgt der Zugriff auf den PI mittels SSH.

Um dies zu realisieren, muss der Raspberry PI erst einmal in das Netzwerk eingebunden werden. Den Raspberry PI uber ein Netzwerkkable mit dem Rooter oder einem Switch verbinden und die Spannungsversorgung uber micro USB des Raspberry PI anschließen. Als Spannungsversorgung verwende ich mein iPhone Ladegerat, der USB-Port des Rooters, sofern er einen solchen besitzt, sollte auch ausreichen. Als nachstes benotigt man noch die IP-Adresse des Raspberry PI. Er ist so eingestellt, dass ihm eine Adresse per DHCP zugewiesen wird. Diese muss nun erst einmal ermittelt werden. In der Regel, wird diese im Web-Frontend des Routers unter Heimnetz angezeigt. Ist dies nicht der Fall, kann diese zum Beispiel aus einem Terminal uber Befehl „nmap" ermittelt werden:

Hier bei ist 192.168.178.1 die IP-Adresse meines Routers. Hat man einen andern Adressbereich muss dieser angegeben werden.

Es wird nun das gesamte Netzwerk gescannt werden. Beim Rasperry PI ist nur der Port 22 offen und er hat noch keinen Namen. Bei mir ist es also der folgende Eintrag:

Die Adresse ist also 192.168.178.26. Ist die Adresse bekannt, ein Terminal offnen und per SSH mit dem Raspberry PI verbinden:

Nun sind wir auf dem Raspberry PI im Text Modus. Dieser reicht fur die weitere Konfiguration aus.

Bevor nun weitere Konfigurationen vorgenommen werden, sollte an dieser Stelle erst einmal das System auf den neusten Stand gebracht werden. Zuerst die Datenbank des Paketmanagers updaten:

Wurden die Paketquellen aktualisiert, sollten eventuell veraltete Pakete durch neue ersetzt werden:

Wenn alles aktualisiert wurde konnen wir uns wieder der Konfiguration widmen. Es empfehlenswert, in regelmaßigen Abstanden, diese beiden Schritte durchzufuhren.

## Den Namen des Raspberry PI andern

Ich habe und mochte mehrere Raspberries in meinem Netzwerk betreiben, die die unterschiedlichsten Aufgaben erfullen sollen. Zum einen, sollten innerhalb eines Netzwerkes keine Gerate mit dem gleichen Namen auftreten, da der Nameserver ansonsten keine Beziehung zwischen IP-Adresse und Namen knupfen kann. Des weiteren ist es naturlich auch sinnvoll den Namen des Raspberry PI dessen Anwendung zuzuordnen. Wer nur einen Verwenden mochte und wem der Name egal ist kann diesen Anschnitt uberspringen.

Zuerst muss die Datei „hostsname" geandert werden:

In der Datei steht einfach nur der aktuelle Name „raspberry". Diesen nun einfach loschen und einen beliebigen Namen eintragen, in meinem Fall ist dies „knuts-raspi". Der Name darf keine Sonder-, Leer- oder mathematische Zeichen enthalten, Zahlen sind erlaubt. Durch drucken der Tastenkombination [CTRL]+[x] wird Nano beendet. Da die Datei verandert wurde muss noch zusatzlich [y] eingegebne werden um das Speichern der Änderung zu bestatigen.

Als nachstes muss der alte Name aus der Datei „hosts" durch den neuen Namen erstzt werden:

So dass die Datei danach wie folgt aussieht (naturlich nicht mit meinem Namen):

Damit die Änderungen auch wirksamwerden empfiehlt sich ein Neustart des Systems:

**Tipp:**  
Einige Router besitzen keinen Name Server oder es funktioniert nicht immer, der Name muss/kann dort manuell eingetragen werden. Hierzu das Web-Frontend des Routers offnen und das Heimnetz wahlen. Auf bearbeiten des Eintrags mit der IP-Adress des Raspberry PI klicken. Hier besteht in der Regel die Moglichkeit einen Name einzutragen, also der den man zuvor vergeben hat. Danach kann der Raspberry PI anstelle durch die IP-Adresse auch mit dem Namen innerhalb des Netzwerkes angesprochen werden.  
Die SSH-Verbindung kann nun wie folgt aufgebaut werden:

## Wireless Adapter konfigurieren

Die meisten werden den Raspberry PI uber Wlan in das Netzwerk einbinden und wahrscheinlich auch hierfur auch einen EDIMAX EW-7811UN oder baugleichen USB-Wlan Adapter verwenden. Dieser kleinen USB Sticks basieren in der Regel auf einem Realtek RTL8188 Chip.

Die kabelgebundene Netzwerkverbindung sollte noch bestehen. Um herauszufinden, welchen Stick man verwendet, per SSH mit dem Raspberry PI verbinden und den folgenden Befehl eingeben:

Der letzte Eintrag ist der Wlan USB-Stick. Nun muss die Firmware fur den Stick installiert werden. Im Falle des Realtek Chips ist dise im Packet „[firmware-realtek](http://wiki.debian.org/rtl819x#Wheezy)" enthalten. Um sicherzustellen, dass das Packet existiert, kann der Cache durchsucht werden:

Nun mussen noch alle fur Wireless LAN notwendigen Pakete installiert werden. Bei mir war schon alles installiert, aber noch einmal zur Vollstandigkeit. Pakete die bereits installiert sind werden nicht neu installiert.

Ist alles installiert, sollte man sich erst einmal die verfugbaren Wireless Netzwerke anzeigen lassen:

Es werden alle in Reichweite befindlichen Netzwerke angezeigt. Hierbei ist es naturlich wichtig, dass das eigene Netz gefunden wurde.

Da ein Wlan nur verschlusselt betrieben werden soll, muss der Schlussel dem Raspberry PI bekannt sein. Dieser sollte jedoch nicht im Klartext hinterlegt werden. Daher Verschlusseln wird den Schlussel. MY_ESSID stellt im folgenden den Namen des Wlans und MY_WPA_KEY den WPA-Schlussel dar. Schlussel erzeugen:

Den psk Eintrag (aebd5…) nun merken, abschreiben oder kopieren und die Datei „interfaces" offnen:

Die Datei dann wie folgt modifizieren:

Den Editor mit [CTRL]+[x]" schließen und das speichern mit [y] bestatigen. Die Datei sollte, trotz Verschlusselung, nur von root lesbar sein:

Nun das Wlan mit dem folgenden Befehl stoppen:

Und wieder starten:

Die letzte Adresse, in meinem Fall die 192.168.178.35, ist die IP-Adresse des Raspery PI. Unbedingt merken oder besser noch aufschreiben!

Den Raspberry PI mit sudo poweroff ausschalten und die kabelgebundene Netzwerkverbindung trennen. Beim nachsten Start wird automatisch die Wlan Verbindung hergestellt. Da die Namens IP Bindung nun noch an der Adresse der Kabelverbindung hangt muss, sofern der Router dies nicht automatisch tut, die Namenszuordnung erneut durchgefuhrt werden.
