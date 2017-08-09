# Raspberry Pi überwacht Datenverkehr im Netzwerk 

_Captured: 2015-12-25 at 10:39 from [www.tecchannel.de](http://www.tecchannel.de/pc_mobile/peripherie/2067920/raspberry_pi_ueberwacht_datenverkehr_im_netzwerk/index.html)_

Einige Spionageprogramme auf dem PC konnen sich erstaunlich gut vor Antiviren-Tools schutzen. So war etwa eines der ersten Rootkits fur [Windows XP](http://www.tecchannel.de/produkte/pc-mobil/betriebssystem/microsoft-windows-xp/) uber ein Jahr aktiv, bis es von den Antivirenherstellern entdeckt wurde. Darum kann es hilfreich sein, den Netzwerkverkehr von einem anderen PC aus zu belauschen.

Wer keinen zweiten PC fur diesen Zweck hat, kann dazu auch den Minirechner Raspberry Pi nutzen, den es fur deutlich unter 50 Euro inklusive Zubehor gibt. Als System kommt [Kali Linux](http://www.kali.org/) zum Einsatz, das von Sicherheitsexperten zum Testen der Sicherheit in Netzwerken verwendet wird. Wir zeigen die ersten Schritte fur Kali Linux auf dem Raspberry Pi.

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2525465/522x294.png)

> _Raspberry Pi in der Praxis_

  * ![](http://images.tecchannel.de/images/tecchannel/bdb/2518726/522x294.png)

**Kali Linux installieren:** Wenn Sie mit dem Raspberry Pi noch nicht vertraut sind,[ finden hier eine ausfuhrliche Beschreibung des Minirechners](http://www.pcwelt.de/ratgeber/Raspberry_Pi_-_So_richten_Sie_den_Mini-PC_ein-Phaenomenale_Platine-8600657.html). Wie beim Raspberry Pi ublich, geschieht die "Installation" eines System, indem Sie sein Image auf die SD-Karte fur den Minirechner packen. Das notige ISO-Image von [Kali Linux fur Raspberry Pi finden Sie hier](http://www.offensive-security.com/kali-linux-vmware-arm-image-download/). Zum Entpacken auf die SD-Karte konnen Sie unter [Windows](http://www.tecchannel.de/pc_mobile/windows/) das Tool [Win 32 Disk Imager](http://sourceforge.net/projects/win32diskimager/) verwenden. Wahlen Sie unter "Image File" den Pfad zum Image von Kali Linux mit Namen Kali Linux-1.0.6a-rpi.img. Stecken Sie die SD-Karte fur den Minirechner an Ihrem PC ein, und wahlen Sie Ihren Laufwerksbuchstaben in Win 32 Disk Imager unter "_Device_" aus. Vorsicht: Es werden alle Daten auf der SD-Karte geloscht. Mit "_Write_" starten Sie den Vorgang.

Stecken Sie die fertige SD-Karte in den Raspberry Pi und schalten Sie ihn ein, indem Sie die Stromversorgung einstecken. Der Bootvorgang dauert einige Zeit. Schließlich loggen Sie sich mit Konto _root_ und dem Kennwort _toor_ in Kali Linux ein und erhalten so Adminzugriff. Nun starten Sie uber den Befehl _startx_ die grafische Bedienerfuhrung.

Kali Linux hat den Leitspruch: Je leiser du bist, desto mehr wirst du horen. Deshalb startet Kali ohne Netzwerkdienste. Wenn Sie nun etwa das in Kali Linux enthaltene Tool Metasploit zum Testen von Schwachstellen in Ihrem [Netzwerk](http://www.tecchannel.de/netzwerk/) nutzen mochten, mussen Sie die notigen Dienste zunachst im Terminal mit diesen zwei Befehl starten:

`service postgresql start`
`service metasploit start`

`msfconsole`

[Metasploit](http://de.wikipedia.org/wiki/Metasploit) ist in der Bedienung anspruchsvoll. Es darf zudem nur in Ihrem eigenen [Netzwerk](http://www.tecchannel.de/netzwerk/) genutzt werden. Fremde Netze sind tabu. Hilfe fur den Einsatz zu Metasploit finden Sie [deutschsprachig hier](http://de.docs.kali.org/) oder [englischsprachig hier](http://help.metasploit.com/), außerdem kurz und knapp uber [www.pcwelt.de/dma6](http://www.pcwelt.de/dma6). Ein Demovideo bekommen Sie uber <https://www.youtube.com/watch?v=cUDJ9kf4oIQ>.
