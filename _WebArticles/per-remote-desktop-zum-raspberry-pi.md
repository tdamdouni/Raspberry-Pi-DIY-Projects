# Per Remote Desktop zum Raspberry PI

_Captured: 2017-05-06 at 16:54 from [www.welzels.de](http://www.welzels.de/blog/2013/03/per-remote-desktop-zum-raspberry-pi/)_

Der Raspberry PI verfugt uber einen HDMI Anschluss und zwei USB Ports. An diese Anschlusse den Monitor, eine Tastatur und Maus angeschlossen, schnell noch LXDE installieren und man hat einen kleinen grafischen Rechner.

Aber wer macht das schon…

Ich zum Beispiel besitze uberhaupt keinen Monitor. Das heißt der Monitor den ich besitze, ist in meinem iMac verbaut und da kann ich den PI gar nicht anschließen, zumindest wusste eich nicht wie. Musste mir also erst einmal einen zweiten Monitor anschaffen. Jedoch mochte ich uberhaupt keinen zwein Monitor auf meinem Schreibtisch haben. Des weiteren benotigte ich ja auch noch eine zweite Maus und eine zweite Tastatur!

Die Losung wahre, die Bildschirmausgabe uber das Netzwerk auf meinen Rechner zu ubertragen. So zusagen ein AirPlay Mirroring. Also jene moderne Technologie, wie sie beim einem Tablets und ahnlichen Geraten zum Einsatz kommt.

Ist aber gar nicht modern, beherrschen UNIX Systeme schon seit mehr als 20 Jahren. Und dar der PI ja unter Linux lauft, also einem UNIX Derivat, kann er das auch. Zugegeben es ist eine andere Technologie, als jene die beim AirPlay Mirroring zum Einsatz kommt. Aber es geht ja um das Resultat und nicht um die Technologie.

![RDVs](http://www.welzels.de/blog/wp-content/uploads/2013/03/RDVs-300x187.png)

Die Linux Variante der „Bildschirmfreigabe" setzt einen XServer auf dem Host Computer voraussetzt. Fur Linux und Mac OS X kein Problem, fur Windows ohne schon, von iOS und Android mal ganz abgesehen. Eine alternative ist das Remote Desktop Protocol (RDP). Auch wenn ursprunglich von Microsoft entwickelt, gibt es einen Server-Dienst fur Linux und Client-Anwendungen fur so ziemlich jedes Betriebssystem.

## RDP auf dem PI installieren

Zunachst benotigt man eine SD-Karte mit Raspbian, wie ich es bereits in [Raspberry PI - Die Installation](http://www.welzels.de/blog/2012/12/raspberry-pi-die-installation/) beschrieben habe. Egal ob die Installation wie in der Beschreibung erlautert durchgefuhrt oder eine bestehende Installation verwendet wird, sollte zu erst das System auf den aktuellen Stand gebracht werden:

Ist die Aktualisierung beendet, muss erst einmal sichergestellt werden, dass das grafische System auf dem Raspberry PI nach dem booten auch gestartet wird. Dies kann uber den Raspberry PI Konfigurator geschehen:

Dort den Eintrag _boot_behaviour - Start desktop on boot?_ wahlen:

![Raspi-config01](http://www.welzels.de/blog/wp-content/uploads/2013/03/Raspi-config01-300x219.png)

_Should we boot straight to desktop?_ mit Ja bestatigen und das System neu starten:

![Raspi-config02](http://www.welzels.de/blog/wp-content/uploads/2013/03/Raspi-config02-300x219.png)

Zum Schluss nur noch der eigentliche Server installieren:

Dann kann uber eine Remote Desktop Verbindung auf den Raspberry PI zugegriffen werden.

## Remote Desktop Verbindung zum PI herstellen

### Remote Desktop Verbindung unter Windows

Unter Windows ist der Client bereits installiert und kann uber „Programme -> Zubehor -> Remote Desktop Verbindung" geoffnet werden.

![RDVWin](http://www.welzels.de/blog/wp-content/uploads/2013/03/RDVWin-300x187.png)

### Remote Desktop Verbindung unter Mac OS X

Fur Mac OS X stehen verschiedene Clients zu verfugen. Hat man MS Office fur Mac, ist unter „Programme -> Remotedesktopverbindung" der Microsoft Client bereits vorhanden. Andernfalls kann er unter <https://www.microsoft.com/germany/mac/remote-desktop-client> geladen werden.

![RDVMAC](http://www.welzels.de/blog/wp-content/uploads/2013/03/RDVMAC-300x187.png)

Mochte man den Microsoft Client nicht verwenden, gibt es alternativ im App Store bzw. im Netz.

### Remote Desktop Verbindung unter Linux

Unter Linux benotigt man das Packet „rdesktop" und ggf. noch ein GUI fur Gnome „gnome-rdp" oder fur KDE „krdc".

![RDVLinux](http://www.welzels.de/blog/wp-content/uploads/2013/03/RDVLinux-300x187.png)

### Remote Desktop Verbindung unter iOS

Es lasst sich so auch eine Verbindung mit dem iPhone oder dem iPad herstellen. Im App Store findet man etliche kostenlose und kostenpflichtige Apps. Ich habe es mal mit dem „[Kostenlos Remote-Desktop](https://itunes.apple.com/de/app/kostenlose-remote-desktop/id394062949?mt=8)" versucht und es hat problemlos funktioniert.

![RDViOS](http://www.welzels.de/blog/wp-content/uploads/2013/03/RDViOS-300x225.png)

Sollte also auch unter Android funktionieren, da ich uber kein Android Gerat verfuge, kann ich das nicht mit Bestimmtheit sagen. Einfach mal in [Google Play](https://play.google.com/store/search?q=remote+desktop&c=apps) schauen und testen.

### Weitere Einstellungen

Nun konnen noch einige erweiterte Einstellungen, wie Bildschirmauflosung, Farbe, lokale Ressourcen etc. getroffen werden:

  * Unter Windows lassen sich die einzelnen Einstellungen mit „Optionen" aufrufen.
  * Unter Mac OS X gelangt man dort hin, uber die Menuleiste „RDV -> Einstellungen".
  * Unter Linux, bzw. mit Gnome RDP, muss zuerst eine neue Session erstellt werden, bei der dann die Einstellungen festgelegt werden konnen.

### Verbindung aufbauen

Nach starten des Remote Desktop Client, muss die IP Adresse des Raspberry PI angegeben werden. Der Raspberry PI kann auch uber den Host-Namen angesprochen werden, dazu mussen Samba und Winbind installiert und konfiguriert sein.

![rdv01](http://www.welzels.de/blog/wp-content/uploads/2013/03/rdv01-300x134.png)

Nach dem „Verbinden" gedruckt wurde erscheint dann der Anmeldebildschirm des Raspberry PI.

![rdv02](http://www.welzels.de/blog/wp-content/uploads/2013/03/rdv02-300x238.png)

Als Modul sesman-XVNC wahlen, Benutzername, Passwort eingeben und auf OK drucken. Danach wird der grafische Desktop des Raspberry PI angezeigt.

![rdv03](http://www.welzels.de/blog/wp-content/uploads/2013/03/rdv03-300x238.png)

Nun kann bequem, ohne zusatzliche Hardware oder großere Umbaumaßnahmen am Raspberry PI gearbeitet werden. Voraussetzung ist eine einigermaßen schnelle Netzwerkverbindung zwischen PI und dem Host vorhanden, bemerkt man den unterschied zwischen direkter Hardware- und indirekter Netzwerkanbindung nicht.
