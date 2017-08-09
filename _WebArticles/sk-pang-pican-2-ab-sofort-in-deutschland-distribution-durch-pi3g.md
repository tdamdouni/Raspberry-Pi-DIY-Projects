# SK Pang PiCan 2 ab sofort in Deutschland – Distribution durch pi3g

_Captured: 2017-05-11 at 22:43 from [pi3g.com](https://pi3g.com/2016/05/22/sk-pang-pican-2-ab-sofort-in-deutschland-distribution-durch-pi3g/)_

Der PiCan, jetzt in der zweiten Auflage, dient dazu den Raspberry Pi mit dem CAN Bus zu verbinden. Der PiCan wird von der britischen Firma [SK Pang](http://skpang.co.uk/catalog/pican2-canbus-board-for-raspberry-pi-2-p-1475.html) hergestellt.

Sie konnen den PiCan 2 [hier ](https://pi3g.com/produkt-kategorie/raspberry-pi-accessories/raspberry-pi-accessories-camera-gpio/)bestellen.

## **Stop: ich weiß was ein Raspberry Pi ist, aber was ist ein CAN Bus?**

Der CAN Bus wurde 1983 von Bosch fur die Vernetzung von Steuergeraten in Autos entwickelt. Ein interessanter Zufall: Ich wurde ubrigens ebenfalls 1983 geboren.

Der Bus arbeitet mit zwei verdrillten Adern, CAN_HIGH und CAN_LOW. CAN_GND als Masse und dritte Ader ist optional, jedoch auch auf dem PiCan 2 Adapter Board vorhanden.

Es gibt einen Highspeed und einen Lowspeed-Bus. Bei dem Highspeed-Bus betragt die maximale Datenubertragungsrate 1 Mbit/s, bei Lowspeed 125 kbit/s.

Außer in Autos wird der Bus auch in der Automatisierungstechnik, Medizintechnik, Raumfahrttechnik und in vielen weiteren Bereichen eingesetzt. So sind neben AUDIs, VWs und BMWs auch Computertomographen, Elektro-Rollstuhle, Herz-Lungen-Maschinen und Seenotrettungskreuzer mit dem CAN-Bus ausgestattet.

Mit CANopen gibt es auch ein auf CAN aufbauendes Kommunikationsprotokoll das hauptsachlich in der Automatisierungstechnik eingesetzt wird. Fur CANopen steht mit CanFestival nach Kompilierung auch fur den Raspberry Pi ein CANopen Stack zur Verfugung.

## **Und warum ist das spannend?**

Man kann mit dem Raspberry Pi 3 und dieser Platine, dem PiCan 2 mit dem Bordelektronik im Auto sprechen. In Europa wurde ab 1.1.2000 fur Benzin-Autos, und ab 1.1.2003 fur Diesel und Gasautos verpflichtend eine sogenannte OBD II Buchse eingefuhrt. OBD steht dabei fur on-board Diagnostik.

Mit dem PiCan 2 Board kann man uber zwei der Pins des OBD II den CAN Bus des Autos ansteuern und die Nachrichten mitlesen. Dabei werden je nach Auto beispielsweise Nachrichten wie Tur offen, Blinker gesetzt, Position des Lenkrades, oder Handbremse angezogen uber den CAN Bus ubermittelt. Manche Autos schweigen sich auf dem CAN Bus dagegen erstmal aus, bis die Bordelektronik explizit nach Informationen gefragt wird.

Auf blafusel.de gibt es eine Liste mit uber 3000 Eintragen von Auto-Modellen die uber verschiedene Methoden erfolgreich angesteuert wurden. In den Kommentaren finden sich auch weitere wertvolle Hinweise, zum Beispiel wo der Stecker genau verbaut wurde.

## **Wo kann ich die Hardware kaufen?**

Ab sofort ubernehmen wir innerhalb Deutschlands fur SK Pang die Distribution von dem Pi Can 2.

Bei Interesse an dem Pi Can 2 konnen Sie ihn [direkt hier ](https://pi3g.com/produkt-kategorie/raspberry-pi-accessories/raspberry-pi-accessories-camera-gpio/)bestellen.

Wir werden die Ware außerdem Handlern direkt anbieten, und die Handler die sie im Sortiment haben dann hier auflisten.
