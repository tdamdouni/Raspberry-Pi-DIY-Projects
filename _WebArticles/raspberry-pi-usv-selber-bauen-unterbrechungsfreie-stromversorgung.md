# Raspberry Pi – USV selber bauen (Unterbrechungsfreie Stromversorgung)

_Captured: 2017-09-03 at 13:10 from [tutorials-raspberrypi.de](https://tutorials-raspberrypi.de/raspberry-pi-usv-selber-bauen-unterbrechungsfreie-stromversorgung/)_

In einigen Anwendungen ist es wichtig, dass der Pi auch bei einem Stromausfall weiter mit Strom versorgt wird. Wird im Moment der Stromunterbrechung auf der SD Karte geschrieben ist es moglich, dass das Image korrupt und damit unbrauchbar wird.  
Eine USV (Unterbrechungsfreie Stromversorgung) stellt sicher, dass bei einer Stromunterbrechung ein Akku / andere Stromquelle einspringt, ohne dass das Gerat beeintrachtigt wird.

Eine solche USV kann sehr einfach mit ein paar Bauteilen erstellt werden und im Notfall kann mittels eines Skripts darauf reagiert werden und der Pi ordnungsgemaß heruntergefahren werden.

## Zubehor

  * [Powerbank](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=intenso 10000 powerbank) mit 2.1A Output (wichtig: muss gleichzeitig auf- und entladbar sein)
  * [USB Hub](http://www.amazon.de/gp/product/B00Y211AFM?ie=UTF8&linkCode=as2&camp=1634&creative=6738&tag=754-21&creativeASIN=B00Y211AFM) (andernfalls musste ein Kabel aufgeschnitten werden)
  * [Relais](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=5V Relais)
  * 10kΩ Widerstand
  * 2 Micro USB Kabel

Zwar gibt es bereits fertige USV fur den Raspberry Pi zu kaufen, aber diese sind entweder recht teuer ([Link](http://www.amazon.de/gp/product/B00P16T13A/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00P16T13A&linkCode=as2&tag=modules-21)) oder nicht sehr gut bewertet ([Link](http://www.amazon.de/gp/product/B00HY8XY40/ref=as_li_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00HY8XY40&linkCode=as2&tag=modules-21)). Eine andere [Variante](http://www.ramser-elektro.at/shop/bausaetze-und-platinen/bausatz-usb-redundanzmodul-fuer-raspberry/) (die allerdings Lot- und Elektronikkentnisse voraussetzt), ware die Speisung zweier Stromquellen - zum einen uber die Steckdose und zum anderen uber die [Powerbank](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=intenso 10000 powerbank).

## Aufbau

![](https://tutorials-raspberrypi.de/wp-content/uploads/2015/09/usv_Steckplatine1-1024x480.png)

Es werden zwei USB Ports des Hubs benotigt. An den ersten wird die Powerbank angeschlossen, die wiederum dem Pi als Stromquelle dient. Der zweite USB Anschluss wird als An/Aus Schalter des Relais verwendet. Ich habe die Kabel, die das Relais steuern, einfach unter die Halterungen geklemmt. Auf der rechten Seite siehst du wo 5V und GND an einer USB Buchse liegen.

Der mittlere OUT Pin des Relais kommt an GPIO27 (Pin 13) des Pi's. Der rechte OUT Pin uber einen 10kΩ Widerstand an Pin 2 (5V) des Pi's, der rechte an Pin 6 (GND).

## Software

Angenommen es kommt nun zu einem Stromausfall. Zum einen wurde der Pi noch einige Stunden (je nach Powerbank Modell) laufen. Danach ware aber Schluss. Damit der Pi nun mitgeteilt bekommt, dass er grade auf „Notstrom" lauft, schaltet das Relais um und an GPIO23 liegen nun 0V an. Davor gab es einen HIGH Pegel, da durch die USB Hub Stromversorgung auch das Relais geoffnet war.

In meinem Beispiel mochte ich zeigen, wie man auf die Änderung reagiert und den Pi sachgemaß herunter fahrt. Naturlich konnen auch andere Aktionen ausgefuhrt werden (Email versenden, Daten speichern, erst nach einer Weile herunter fahren, usw.).

Fur dieses Beispiel musst du [wiringPi](https://tutorials-raspberrypi.de/gpio/wiringpi-installieren-pinbelegung/) installiert haben (eine ahnliche Umsetzung mit Python sollte sicher auch moglich sein). Der wiringPi Pin 2 entspricht GPIO27 (siehe wiringPi Pin Belegung).

Wir erstellen eine neue Datei
    
    
    sudo nano /usr/local/etc/USV.sh

mit folgendem Inhalt:

123456789101112131415161718 
#!/bin/bashgpio mode 2 inwhile truedoresult="$( gpio read 2 )"if [ "$result" = "1" ]; then# Custom Code# in 60 min herunterfahrensudo shutdown -h 60 &amp;# Custom Code Endefisleep 1done

Statt meinem Code kann auch jeder beliebige andere Shell-Befehl eingetragen werden.

Damit das Skript nun bei jedem Reboot auch mitstartet, tragen wir es noch als crontab ein:
    
    
    sudo crontab -e

Am Ende der Datei wird nun folgende Zeile eingefugt:
    
    
    @reboot bash /usr/local/etc/USV.sh &

Das von mir verwendete Powerbank Modell schaltet seine Aufladung ab, sobald es voll ist. Bei Interesse kann ich auch noch eine Schaltung prasentieren, womit man alle X Stunden die Powerbank aufladen lasst (was im Grunde nur ein zusatzliches Relais ist). Dazu kannst du auch ggf. [diesen Artikel](https://tutorials-raspberrypi.de/gpio/relais-schalter-mit-dem-raspberry-pi-steuern/) lesen.
