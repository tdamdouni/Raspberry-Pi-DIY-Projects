# Raspberry Pi mit Solaranlage betreiben – Teil 2

_Captured: 2017-05-19 at 11:35 from [developer-blog.net](https://developer-blog.net/raspberry-pi-mit-sonnenenergie-betreiben-teil-2/)_

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
