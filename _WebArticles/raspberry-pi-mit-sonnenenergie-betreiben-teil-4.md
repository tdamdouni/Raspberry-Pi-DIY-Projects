# Raspberry Pi mit Sonnenenergie betreiben – Teil 4

_Captured: 2017-05-19 at 11:36 from [developer-blog.net](https://developer-blog.net/raspberry-pi-mit-sonnenenergie-betreiben-teil-4/)_

In den letzten Teilen dieser Artikelserie um das Thema [Raspberry Pi und Sonnenenergie](https://developer-blog.net/raspberry-pi-mit-sonnenenergie-betreiben/) habe ich bereits die Theorie dazu vorgestellt und auch eine mogliche Losung beschrieben. Im letzten Teil habe ich sogar meine personliche Losung vorgestellt. Seit dem Artikel sind nun einige Tage vergangen und ich hatte Zeit, einige Tests durchzufuhren. Ich zeige euch nun wie lange mein **Raspberry Pi Akku** lauft und wie gut diese Losung ist.

![Raspberry Pi Akku](https://developer-blog.net/wp-content/uploads/2013/09/IMG_2559.jpg)

> _[Raspberry Pi Versuchsaufbau](http://developer-blog.net/wp-content/uploads/2013/09/IMG_2559.jpg)_

## Der tatsachliche Verbrauch (Raspberry Pi Akku)

In Foren werden offensichtlich einige Mythen rund um den tatsachlichen Stromverbraucht verbreitet und die Herstellerangaben sind wie immer mit Vorsicht zu genießen. Aus diesem Grund will ich mir mit einem einfachen Test selbst ein Bild machen. Dazu habe ich folgende Versuchsanordnung erstellt.

### Versuchsanordnung

  1. Test unter voller Last  
Im ersten Test soll herausgefunden werden, wie lange der Raspberry Pi mit einem Akku (mein Raspberry Pi Akku) betrieben lauft. Zusatzlich wird der Raspberry Pi moglichst stark ausgelastet. Ziel ist, herauszufinden wieviel Ampere der Pi unter hoher CPU Auslastung benotigt.  
Zu diesem Zweck habe ich den neuen Akku ([EasyAcc 10000mAh PowerBank](http://www.amazon.de/gp/product/B00BJCHH36/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00BJCHH36&linkCode=as2&tag=developerblog-21)) voll geladen, den Pi angesteckt und unter voller Last laufen lassen. Mit einem Skript habe ich die Laufzeit protokolliert.
  2. Test unter Leerlauf  
Das Ziel des zweiten Test ist herauszufinden, ob es eine Änderung in der Laufzeit bei geringer bis keiner Last gibt.

### Ergebnis

Das Ergebnis ist uberraschend! Nach zwei Tagen habe ich nun folgende Werte herausgefunden:

  1. Test unter voller Last  
Laut dem Protokoll wurde der Test am 11.09.2013 um 16:39 Uhr gestartet. Im Log war ersichtlich, dass der letzte Einrag vom 12.09.2013 um 10:03 Uhr stammte. Das bedeutet, der Raspberry Pi ist 17 Stunden und 24 Minuten gelaufen. Bei einer Akkuladung von 10000mAh ergibt das eine benotigte Stromstarke von 571 mA. Bei dieser Rechnung wird angenommen, dass die Spannung konstant 5V war.
  2. Test unter Leerlauf  
Bei diesem Test gab es geringfugig andere Werte. Gestartet wurde am 13.09.2013 um 8:50 Uhr und der letzte Log Eintrag stammte vom 14.09.2013 um 4:05 Uhr. Folglich lief der Raspberry Pi 19 Stunden und 25 Minuten. Wie erwartet langer als im ersten Testlauf, jedoch nur 2 Stunden langer. Mit diesen Werten ergibt sich eine errechnete Stromstarke von 519 mA. Wieder mit den konstanten 5V.

### Informationen

Um den Test nachzuvollziehen hier einige Informationen. Der Testaufbau ist im Bild demonstriert. Der Raspberry Pi hangt uber USB am Akku und hat lediglich einen Micro WLAN Stick angeschlossen. Dieser wird fur eine [SSH Verbindung](https://developer-blog.net/ssh-zugriff-auf-den-raspberry-pi/) benotigt um folgende Skripts zu starten:

  * Protokollierung  
Um im nachhinein festzustellen, wann dem Raspberry Pi der Strom ausgegangen ist habe ich folgendes kurzes Skript laufen gehabt, welches alle 60 Sekunden die aktuelle Uhrzeit in eine Logdatei schreibt. Die Differenz aus erster und letzter Uhrzeit ist die Laufzeit:  


123456789101112
#!/bin/bashlog(){message="$@"echo $messageecho $message >>minutes_log.log}while truedolog $(date +"%d.%m.%Y %T")sleep 60done

## Zusammenfassung

Mit diesem Test wollte ich feststellen wie lange der Raspberry Pi lauft, wenn er lediglich mit einem Akku betrieben wird. Diese Information war leider nicht eindeutig im Internet zu finden. Nach zwei Versuchsanordnungen, eine unter voller Last, die andere im Leerlauf, ergab sich ein minimaler unterschied von 2 Stunden. Im Leerlauf war der Raspberry Pi fast 19,5 Stunden online. Das mit einem 10000mAh Raspberry Pi Akku.

Viele Leser werden vermutlich nun enttauscht sein. Auch mit enttauscht dieser Wert. Zum einen habe ich es nicht geschafft den Pi mehr als 24 Stunden online zu halten, zum anderen ist der Unterschied zwischen voller Last und Leerlauf kaum nennenswert.

Fur eine Solaranlage ergibt sich nun folgendes Bild: sie muss mindestens einmal den Raspberry Pi Akku am Tag komplett laden und nebenbei auch den Raspberry Pi am laufen halten. Es ergibt sich somit folgende Regel: fur den Pi der immer 5V benotigt sollte an einem Tag bis zu 20A zur Verfugung stehen. Es ergibt sich somit ein taglicher Stromverbrauch von 5V * 20A = 100 Watt (das ist kein genauer Wert, dieser reicht aber fur den Betrieb eines Raspberry Pis).

  


In diesem Teil geht es um die Berechnung mit welchen Kosten wir fur dieses Projekt rechnen mussen. Sonnenenergie ist toll, da sie gratis ist, jedoch ist die Anschaffung der Hardware fur die Nutzung der Sonnenenergie heute noch relativ teuer und rentiert sich erst uber mehrere Jahre. Nimmt man dazu noch Wartungskosten erst uber Jahrzehnte. Zahlt es sich also nun aus den Raspberry Pi mit Sonnenenergie zu betreiben? Schließlich braucht er ja kaum Energie. Ein netter Artikel zur Umsetzung dieser Losung ist [hier](http://www.rustynailworkshop.com/archives/6) zu finden.

## Rechenbeispiele zur Solaranlage

Bei meinen Rechenbeispielen gehe ich von 2 unterschiedlichen Annahmen aus. Zum einen ist da der Rapberry Pi der mit seinen 3,5 Watt betrieben wird und das auf Dauer. Das bedeutet er musste standig unter voller Last stehen und die großte mogliche Leistung erzielen. Zum anderen nehme ich den normalen Fall, ein Raspberry Pi der auch im Dauerbetrieb ist, jedoch nur selten eine Auslastung hat und lange im low power Modus operiert.

### Best Case Scenario

Der Raspberry Pi lauft. Er ist rund um die Uhr erreichbar, fuhrt aber nur gelegentlich Aufgaben aus. Hier ein Backup, da eine Webseite anzeigen, Daten speichern oder Werte ausgeben. Die meiste Zeit verbringt er mit einer Auslastung bei nur wenigen Prozent. Vom Power USB Kabel nimmt er nur so viel Energie, soviel er eben gerade benotigt, meistens das Minimum.

Es ist Sommer, die Sonne scheint 10 Stunden am Tag und es ist gerade Mittag, keine Wolke am Himmel.

### Losung

Fur diesen Fall benotigen wir lediglich eine kleine Solaranlage. Eine Eingangsspannung von 5 V und ca. 200 - 300 mA sollten ausreichen um den Pi optimal mit Energie zu versorgen. Dafur reicht uns:

  * eine kleine [10 Watt Solaranlage](http://www.amazon.de/gp/product/B007HAZY8Y/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B007HAZY8Y&linkCode=as2&tag=developerblog-21)  
dieses Solarpanel liefert laut Herstellerangabe bis zu 600 mA und auch im Schatten mindestens 200 mA.
  * ein [Laderegler fur die Solarzelle](http://www.amazon.de/gp/product/B002R00V8W/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B002R00V8W&linkCode=as2&tag=developerblog-21)  
diesen benotigen wir, damit es zu keinen Überspannungen kommt und unser Pi Schaden erleidet.

Mit dieser Investition sollte der Raspberry Pi bei genug Sonneneinstrahlung autonom damit betrieben werden konnen.

### Worst Case Scenario

Im schlimmsten Fall lauft unser Pi also unter voller Last und hat somit den maximalen Verbrauch. Aufgaben sind dafur meistens Berechnungen. Anwendungsbeispiele sind unter anderem Bitcoin mining, Videos de-/komprimieren, Berechnungen durchfuhren, Video streamen usw. all jene Aufgaben bei der der Prozessor zu 100% ausgelastet ist und auch moglichst viele angesteckte Gerate oder Interfaces angesprochen werden. Fur diese Arbeit wird Energie benotigt. Der Pi nimmt sich also vom Power USB Kabel so viel er kann.

Um das ganze spannende zu machen ist gerade Nacht und es ist tiefer Winter. Den Tag uber war es bedeckt und neblig.

### Losung

In diesem Fall sind wir auf einen Akku angewiesen und mussen hoffen, dass die Leistung der Solarzelle ausreicht um ihn am Tag soweit zu laden, dass wir mit dem Raspberry Pi uber die Nacht kommen. Fur wenig direkte Sonneneinstrahlung sind großere und Leistungsfahigere Solarzellen notwendig:

  * eine leistungsfahige [200 Watt Solaranlage](http://www.amazon.de/gp/product/B00821AED2/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00821AED2&linkCode=as2&tag=developerblog-21)  
diese Anlage ist gegenuber der ersten um einiges teurer. Hier ist jedoch im Preis bereits ein Laderegler enthalten.
  * einen Laderegler  
dieser ist bei der Solaranlage bereits enthalten.
  * einen [Blei-Akku](http://www.amazon.de/gp/product/B005N97ZQU/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B005N97ZQU&linkCode=as2&tag=developerblog-21)  
dieser Akku ist mit seinen 33 Ah stark genug um den Pi 2 Tage lang selber zu versorgen.

Bei diesem Szenario muss man aber bedenken, dass irgendwann einfach zu wenig Strom uber die Solaranlage kommt und man irgendwann den Akku ans Stromnetz anschließen sollte. Dafur muss man laufend uber den Ladezustand des Akkus informiert werden.

Bei all den Zahlen und Fakten ist naturlich Vorsicht geboten. Das Thema Sonnenenergie ist komplex und nicht einfach. Allein schon die korrekte Positionierung einer Solaranlage kann massive Unterschiede bewirken. Als Beispiel dazu sagt dieses Diagramm eigentlich alles aus:

![Solaranlage Ausrichtung](https://developer-blog.net/wp-content/uploads/2013/09/SolarertragNachAusrichtung.png)

> _[Solaranlage Ausrichtung](http://developer-blog.net/wp-content/uploads/2013/09/SolarertragNachAusrichtung.png)_

Ich hoffe mit diesen Beispielen wird die Problematik bei dem Solarbetrieb deutlich. Im nachsten Teil zeige ich meine Losung.
