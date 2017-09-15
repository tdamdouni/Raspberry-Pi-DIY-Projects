# Raspberry Pi: Relais-Schalter per GPIO steuern

_Captured: 2017-09-03 at 13:11 from [tutorials-raspberrypi.de](https://tutorials-raspberrypi.de/raspberry-pi-relais-schalter-steuern/)_

![Raspberry Pi Relais Schalter](https://tutorials-raspberrypi.de/wp-content/uploads/2015/08/51UIh5JWRoL.jpg)

Oftmals will man auch Module mit hoheren Spannung mit dem Raspberry Pi steuern. Fur diesen Zweck konnen am Raspberry Pi Relais verwendet werden: Mittels eines niederspannigen Impulses wird der Relais-„Schalter" umgelegt. Da der Pi nur maximal 5V (die GPIOs sogar nur 3.3V) vertragt bleibt ohne Relais das Risiko vorhanden, den Pi durchbrennen zu lassen. Hat man jedoch zwei voneinander getrennte Stromkreise kann das nicht passieren.

Wie man ein Relais mit dem Raspberry Pi steuert und was dabei beachtet werden muss zeige ich in diesem Tutorial.

## Zubehor

  * Female - Female [Jumper Kabel](http://www.ebay.de/sch/i.html?_from=R40&_sacat=0&_nkw=female+female-jumper+kabel&rt=nc&LH_PrefLoc=1)
  * externer Stromkreis (z.B. [Batterien](http://www.amazon.de/mn/search/?_encoding=UTF8&linkCode=ur2&camp=1634&creative=19450&tag=754-21&field-keywords=Batterien)) und eine Anwendung (bspw. Motoren)

Die Relais gibt es als [2er](http://www.amazon.de/gp/product/B00PIMRGN4?ie=UTF8&linkCode=as2&camp=1634&creative=6738&tag=754-21&creativeASIN=B00PIMRGN4), [4er](http://www.amazon.de/gp/product/B00HWPDASA?ie=UTF8&linkCode=as2&camp=1634&creative=6738&tag=754-21&creativeASIN=B00HWPDASA), [8er](http://www.amazon.de/gp/product/B00SV22T8K?ie=UTF8&linkCode=as2&camp=1634&creative=6738&tag=754-21&creativeASIN=B00SV22T8K) und sogar als [16er](http://www.amazon.de/gp/product/B005WR747I?ie=UTF8&linkCode=as2&camp=1634&creative=6738&tag=754-21&creativeASIN=B005WR747I) Module, je nachdem was man braucht. Um nicht zu viele GPIOs auf dem Pi zu „verschwenden" lohnt sich bei mehr als 4 Kanalen die Anschaffung eines [GPIO Port Expander](https://tutorials-raspberrypi.de/gpio/gpios-mittels-i2c-port-expander-erweitern/).

## Aufbau

Der Aufbau ist sehr simpel, da alle Pins beschriftet sind. Links (GND) kommt an Pin 6 des Pi's (GND), der rechte Pin (VCC) kommt an 3V3 (Pin 1) des Pis. Je nachdem wie viele der Relais du steuern willst, musst du entsprechend viele GPIOs mit den IN Pins verbinden. Es empfiehlt sich ein kleiner Widerstand zwischen Pi und Relais zu setzen, ist aber bei 3V3 nicht unbedingt notig.  
Solltest du 5V statt 3.3V an VCC setzen, solltest du auf jeden Fall jeweils einen Widerstand (~1kΩ) zwischen die GPIOs und die IN Pins setzen.

Auf der anderen Seite sind an jedem Relais 3 Verbindungen (siehe Bild unten): Je nachdem ob am IN-Pin eine LOW (0V) oder HIGH (3.3V bzw. 5V) anliegt wird entweder der Schalter zwischen der Mitte und Rechts, bzw. Mitte und Links geoffnet. Falls du alle 3 Pins verbindest kannst du das Relais quasi als Switch verwenden, lasst du rechts oder links frei hat es einfach die Wirkung eines On/Off Schalters. Wo dabei VCC bzw. Ground angeschlossen werden (Mitte bzw. Rechts/Links) spielt keine Rolle.

![Raspberry Pi Relais: Entweder Mitte-Links oder Mitte-Rechts wird verbunden/](https://tutorials-raspberrypi.de/wp-content/uploads/20150831_122651.jpg)

> _Entweder Mitte-Links oder Mitte-Rechts wird verbunden / „geoffnet"._

**Solltest du Gerate mit hohen Spannungen anschließen wollen, solltest du entweder genaustens wissen was du tust oder einen Elektriker fragen! 230V sind lebensgefahrlich. Achte zusatzlich auf die Spezifikationen des Relais und nimm moglichst keine zwielichtigen China-Teile (das ist im Niedrigstrom-Bereich zwar egal, bei hoheren Spannungen sollte man aber der Sicherheit zu Liebe den Euro mehr ausgeben und geprufte Ware nehmen). Ich ubernehme keine Haftung fur Schaden!**

## Raspberry Pi Relais Steuerung

Auch die Steuerung ist nicht sonderlich schwierig, da nur GPIOs geschaltet werden mussen. Du kannst dafur C++ ([wiringPi](https://tutorials-raspberrypi.de/gpio/wiringpi-installieren-pinbelegung/)) oder Python verwenden. Ich verwende Python und habe GPIO 17 (Pin 11) verwendet.
    
    
    sudo python

1234567 
import RPi.GPIO as GPIOGPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board NummernRELAIS_1_GPIO = 17GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisenGPIO.output(RELAIS_1_GPIO, GPIO.LOW) # ausGPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # an

Liegen 0V am Relais Pin an, leuchtet die entsprechende LED, bei einem HIGH Pegel erlischt die LED. Mochtest du, dass bei einem HIGH Pegel das Relais offnet musst du also den mittleren und linken Pin mit dem Stromkreis verbinden. Dabei ist die LED aus. Soll das Relais offnen, wenn die LED auch brennt werden mittlerer und rechter OUT Pin verbunden.

Das war es auch schon. Mich wurde interessieren, in welchen Anwendungen die Raspberry Pi Relais bei euch Benutzung finden?

  
![](https://tutorials-raspberrypi.de/wp-content/uploads/2014/03/20140330_1445092.jpg)

Im zweiten Teil des[Tutorials](http://tutorials-raspberrypi.de/gpio/gpios-mittels-i2c-port-expander-erweitern/) wird gezeigt, wie man mittels eines Skripts die GPIO Pins des I2C auslesen kann und Signale sendet. Außerdem wird ein Skript gezeigt, dass auf einfache User Interaktionen reagiert.

## Python Skript zur Ein- und Ausgabe

Also erstellen wir ein Skript
    
    
    sudo nano i2c_input_output.py

mit folgendem Inhalt:

1234567891011121314151617181920212223242526272829303132333435363738394041 
import smbusimport time#bus = smbus.SMBus(0) # Rev 1 Pibus = smbus.SMBus(1) # Rev 2 PiDEVICE = 0x20 # Device Adresse (A0-A2)IODIRA = 0x00 # Pin Register fuer die RichtungIODIRB = 0x01 # Pin Register fuer die RichtungOLATB = 0x15 # Register fuer Ausgabe (GPB)GPIOA = 0x12 # Register fuer Eingabe (GPA)# Definiere GPA Pin 7 als Input (10000000 = 0x80)# Binaer: 0 bedeutet Output, 1 bedeutet Inputbus.write_byte_data(DEVICE,IODIRA,0x80)# Definiere alle GPB Pins als Output (00000000 = 0x00)bus.write_byte_data(DEVICE,IODIRB,0x00)# Setze alle 7 Output bits auf 0bus.write_byte_data(DEVICE,OLATB,0)#Funktion, die alle LEDs aufleuchten laesst.def aufleuchten():for MyData in range(1,8):# Zaehle von 1 bis 8, was binaer# von 001 bis 111 ist.bus.write_byte_data(DEVICE,OLATB,MyData)print "Zahl:", MyData, "Binaer:", '{0:08b}'.format(MyData)time.sleep(1)# Setze wieder alle Pins auf 0bus.write_byte_data(DEVICE,OLATB,0)#Endlosschleife, die auf Tastendruck wartetwhile True:# Status von GPIOA Register auslesenTaster = bus.read_byte_data(DEVICE,GPIOA)if Taster & 0b10000000 == 0b10000000:print "Taster gedrueckt"aufleuchten()

Mit STRG + O und STRG + X speichern und beenden.

Um das Skript nun zu starten, geben wir
    
    
    sudo python i2c_input_output.py

ein. Sobald du den Taster druckst fangen die LEDs an zu leuchten. Mit STRG + C kannst du das Skript abbrechen und zur Konsole zuruckkehren.

Wie du siehst ist die Benutzung recht einfach und damit hat man sich weitere 16 GPIO Pins geschaffen.
