# Kleiner Datei-Server (NAS) selbst gebaut

_Captured: 2015-12-15 at 11:54 from [www.pcwelt.de](http://www.pcwelt.de/tipps/Kleiner-Datei-Server-_NAS_-selbst-gebaut-7916711.html)_

![Mit unserer Anleitung machen Sie aus dem Platinen-Computer einen Datei-Server für USB-Festplatten.](http://bilder.pcwelt.de/3212697_620x310.jpg)

> _Mit unserer Anleitung machen Sie aus dem Platinen-Computer einen Datei-Server fur USB-Festplatten._

** Der scheckkartengroße Platinen-Computer Raspberry Pi ist sehr schnell popular geworden. Kein Wunder - bei einem Preis von nur knapp 50 Euro. Er eignet sich nicht nur wunderbar zum Experimentieren, sondern auch als kleiner Heim-Server. In diesem Tipp zeigen wir Ihnen, wie Sie aus dem Raspberry Pi in Verbindung mit einer USB-Festplatte einen sehr flexiblen Datei-Server (NAS) machen. **

**Schritt 2** : Stecken Sie die SD-Karte mit Raspbian wheezy darauf in den Raspberry Pi. Schließen Sie im Anschluss daran die Stromversorgung an die Micro-USB-Buchse an sowie eine Tastatur an die eine und die Festplatte an die andere USB-Buchse.

Falls Sie auch eine Maus benutzen mochten, brauchen Sie einen USB-Hub. Den Monitor verbinden Sie per HDMI. Vergessen Sie aber nicht, das Netzwerkkabel ebenfalls einzustecken.

**Schritt 3:** Zur Anmeldung verwenden Sie den Benutzernamen „pi" sowie das Passwort „raspberry". Im Konfigurationsdialog „Raspi-config" stellen Sie dann bei „configure_keyboard" ein deutsches Tastatur-Layout ein. Bei „change_ locale" wahlen Sie „de_DE.UTF8 UTF8", und bei „change_timezone" stellen Sie „Europe" und „Berlin" ein. Mittels „change_password" andern Sie das Passwort des Standardbenutzers „pi". Sie mussen das Passwort zweimal eingeben - es wird dabei nicht auf dem Bildschirm angezeigt.

Aktivieren Sie außerdem unter „ssh" den SSH-Server. Sie benotigen ihn, wenn Sie das System fernwarten mochten (> Schritt 5). Bei „boot_behavior" stellen Sie „Yes" ein, damit das System gleich mit einer grafischen Oberflache startet.

Wenn Sie eine SD-Karte mit vier GB oder mehr Kapazitat verwenden, gehen Sie auf „expand_rootfs" und folgen dann den Anweisungen auf dem Bildschirm. Daraufhin nutzt das System den gesamten verfugbaren Platz aus. Zum Abschluss gehen Sie noch auf „Finish" und bestatigen den Neustart mit „Yes".

**Schritt 4:** Um Raspbian mit Datei-Server-Funktionen auszustatten, mussen Sie einige zusatzliche Tools installieren und die Konfiguration andern. Klicken Sie im Menu links unten auf „Zubehor > Root Terminal". Fuhren Sie im Anschluss daran auf der Kommandozeile die beiden Zeilen

aus. Die beiden Samba-Pakete richten den Server fur Windows-Freigaben ein, ntfs-3g ist fur den Schreibzugriff auf NTFS-formatierte USB-Gerate erforderlich. Hinter mc verbirgt sich der Dateimanager Midnight Commander, der auch einen kleinen Texteditor mitbringt.

Als Nachstes legen Sie mit dem Befehl

ein Passwort fur den Zugriff auf die freigegebenen Ordner fest. Sie tippen das Passwort zweimal blind ein und bestatigen dann jeweils mit der Enter-Taste.

Öffnen Sie nun mithilfe des Befehls

die Samba-Konfigurationsdatei. Erstellen Sie am Ende der Datei folgende Zeilen

Dadurch geben Sie unter dem Namen [public] den Linux-Pfad „/media" frei, unter dem Raspbian die USB-Laufwerke einhangt.

Als Nachstes sollten Sie in der Samba-Konfigurationsdatei noch den Eintrag hinter „workgroup" so anpassen, dass er dem Namen der in [Windows](http://www.pcwelt.de/handover/451) definierten Arbeitsgruppen-Bezeichnung entspricht. Falls Sie sich nicht sicher sind, schlagen Sie die Bezeichnung in Windows unter „Systemsteuerung > System" nach. Drucken Sie die F2-Taste, um die Datei zu speichern. Mit F10 beenden Sie den Editor. Geben Sie zum Abschluss

ein, um den Dienst fur die Dateifreigaben neu zu starten. Im Windows-Explorer geben Sie in die Adresszeile

ein und bestatigen mit Enter. Dann melden Sie sich als Benutzer „pi" mit dem uber „smbpasswd" vergebenen Passwort an. Wenn der Zugriff uber den Namen „raspberrypi" nicht moglich sein sollte, verwenden Sie stattdessen die IP-Nummer. Diese bekommen Sie im Terminal-Fenster des Raspberry-Systems uber den Befehl

heraus.

**Schritt 5:** Ihr Raspberry-NAS konnen Sie nach der Erstkonfiguration ohne Monitor und Tastatur betreiben. Falls Sie allerdings doch mal etwas an den Einstellungen andern mochten, konnen Sie das fortan auch von einem anderen Rechner aus uber das Netzwerk tun.

Unter Windows nutzen Sie beispielsweise den SSH-Client Putty. Geben Sie dazu in Putty den Host-Namen oder die IP-Adresse des Raspberry Pi ein und klicken Sie auf „Open". Loggen Sie sich als Benutzer „pi" mit dem Passwort ein, das Sie unter > Schritt 3 vergeben haben.

Mussen Sie Befehle oder Anwendungen als Administrator („root") ausfuhren, stellen Sie dem Befehl einfach ein „sudo" voran, also beispielsweise
