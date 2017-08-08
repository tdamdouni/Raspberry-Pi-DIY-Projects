# Audi CanBus – Raspberry Pi

_Captured: 2017-05-11 at 22:07 from [www.janssuuh.nl](http://www.janssuuh.nl/de/category/pican/)_

In der Beschreibung der PiCan Installation lesen Sie, dass Sie den Canbus manuell aktivieren mussen.

Zum Gluck enthalt Raspbian einen Datei / das beim starten angesprochen wird.. Diese Datei heißt::  
[nano /etc/rc.local]

Am Ende dieser Datei (knapp uber 'exit 0') rufe Ich eine Python-Datei auf (python_can.py):  
sudo python /home/pi/python_can.py

![Knipsel](http://www.janssuuh.nl/wp-content/uploads/2016/03/Knipsel-2.png)

> _Und in dieser python_can.py gibts den folgenden code ein:_

import os

#os.system("sudo ip link set can0 up type can bitrate 100000 restart-ms 100 loopback on")  
os.system("ip link set can0 up type can bitrate 100000 restart-ms 100")  
os.system("kodi")

Dies automatisch beim Ihre Raspberry Pi 'Ip Link Set'-Befehl starten.

Die erste Zeile ist passiv (#). Hier ist der gleiche Befehl, aber mit dem Zusatz "gehen zuruck auf". Dieser Zusatz macht das den Canbus nicht werklich funktioniert, aber echo't auf sich selbst. Fur Testzwecke ist dies eine praktische Erganzung. Betrachten Sie es als 'Localhost' Prinzip.  
Wenn ich also testen mochten, dann bewegen Ich die (#) auf die zweite Zeile.
