# Raspberry Pi mit Solar Panel betreiben – Teil 3

_Captured: 2017-05-19 at 11:35 from [developer-blog.net](https://developer-blog.net/raspberry-pi-mit-sonnenenergie-betreiben-teil-3/)_

Nach der Theorie zum Thema Raspberry Pi und Sonnenenergie und eine Aufstellung moglicher Konfigurationen mochte ich nun meine Losung prasentieren. Meine Grundidee war das best Mogliche herauszuholen, dafur jedoch moglichst wenig dafur zu zahlen. Man muss naturlich immer in Betracht ziehen, das es sicher noch billiger geht, aber die Qualitat soll ja nicht darunter leiden. Ziel ist den Raspberry Pi moglichst lange und ohne Ausfalle autonom nur mit Sonnenenergie zu betreiben. Dafur habe folgende Hardware gefunden.

![Raspberry Pi Solar Panel](https://developer-blog.net/wp-content/uploads/2013/09/IMG_2555.jpg)

> _[Raspberry Pi Solar](http://developer-blog.net/wp-content/uploads/2013/09/IMG_2555.jpg)_

## Das Solar Panel

Als Solar Panel verwende ich das [EasyAcc Solar Ladegerat](http://www.amazon.de/gp/product/B00C3A6KKO/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00C3A6KKO&linkCode=as2&tag=developerblog-21), welches nach meiner Recherche vom Preis/Leistungsverhaltnis das beste verfugbare war. Vor allem der attraktive Preis war bei mir der Kaufgrund. Das Solar Ladegerat hat einen USB Port und liefert bei direkter Sonneneinstrahlung genug Energie um den Raspberry Pi zu betrieben. Die Verpackung ist zwar etwas billig, auch ist gar keine Anleitung dabei, jedoch funktioniert das Solar Panel direkt ohne Probleme. Die Zellen sind in eine stabile und wetterfeste Tasche eingenaht und dort auch wasserdicht verpackt. Diese Tasche lasst sich einfach zusammenfalten und mitnehmen.

## Der Stutzakku

Als Stutzakku habe ich mich fur einen der selben Firma entschieden: [EasyAcc 10000mAh PowerBank](http://www.amazon.de/gp/product/B00BJCHH36/ref=as_li_ss_tl?ie=UTF8&camp=1638&creative=19454&creativeASIN=B00BJCHH36&linkCode=as2&tag=developerblog-21). Das ist aber zufallig und ich will hier auf keinen Fall die Firma EasyAcc besonders erwahnen. Wichtig war fur mich, dass der Akku mit 10000mAh genug Leistung mitbringt um meine Handy und auch mein iPad zu laden. Außerdem hat er genug Leistung um den Raspberry Pi sicher uber den Tag mit Strom zu versorgen.

Die PowerBank zeigt auch sehr schon den Ladezustand an, so kann ich im schlimmsten Fall, sollte er uber den Tag zuwenig geladen haben auch schnell ein Netzteil anstecken. Dieses ist zwar im Lieferumfang nicht dabei, aber normalerweise hat man als Smartphone Besitzer sowieso ein Micro USB Ladegerat zuhause herumliegen.

## Mobilitat

Insgesamt gefallt mir meine Zusammenstellung sehr gut. Der Akku kann auch alleine als Stutzakku fur meine anderen mobilen Gerate verwendet werden, Der Raspberry Pi wird mit diesem Akku selber zu einem mobilen Gerat und kann endlich uberall hin mitgenommen werden. Das Solar Panel ladt mir entweder den Akku, oder versorgt mir den Raspberry Pi direkt mit Strom. Damit bin ich nun sehr flexibel unterwegs.

![Raspberry Pi Solar2](https://developer-blog.net/wp-content/uploads/2013/09/IMG_2556.jpg)

> _[Raspberry Pi Solar2](http://developer-blog.net/wp-content/uploads/2013/09/IMG_2556.jpg)_

## Test

Beim ersten Test funktionierte alles wunderbar. Das Solar Panel liefert genug Strom um den Pi zu versorgen. Auch den Akku kann es laden, wobei ich annehme, dass es um einiges langsamer geht als uber die Steckdose. In den nachsten Wochen werde ich den Dauerbetrieb testen und auch daruber berichten.

  


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
