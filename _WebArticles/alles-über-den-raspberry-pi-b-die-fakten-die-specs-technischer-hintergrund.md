# Alles über den raspberry pi 3b+ - die fakten, die specs, technischer Hintergrund 

_Captured: 2018-03-16 at 20:59 from [buyzero.de](https://buyzero.de/blogs/news/raspberry-pi-3b-alle-fakten?contactID=597763cf47fbc0f7fccab6d8&emailID=5aabfcec597ed757414f7328&utm_campaign=Newsletter+16.03.18_5aabfcec597ed757414f7328&utm_medium=email&utm_source=newsletter)_

![Alles über den Raspberry Pi 3B+ - die Fakten, die Specs, technischer Hintergrund - bei uns jetzt kaufen!](https://cdn.shopify.com/s/files/1/1560/1473/articles/raspberry-pi-3-model-b-plus.jpg?v=1521044714)

# Raspberry Pi 3B+ - von Maximilian Batz / pi3g.com

Seit dem Start 2012 wurden uber 19 Millionen Raspberry Pi's verkauft. Davon alleine 9 Millionen Pi 3s! Grund genug, dem beliebtesten aller Single Board Computer mit dem Raspberry Pi 3 Model B+ ein Upgrade zu verpassen. Und ja, ein langgehegter Wunsch der Raspberry Pi Community geht endlich in Erfullung: GBit Ethernet. Über USB 2.0 - was das bedeutet schreibe ich hier noch. Das wirkliche Highlight fur mich ist allerdings das neue WLAN Modul des Raspbery Pi 3B+! Doch alles der Reihe nach.

[Hier kann man den Pi 3B+ ubrigens bei uns ab sofort kaufen - ohne Mengenbeschrankung!](https://buyzero.de/products/raspberry-pi-3b-plus?variant=6471085359131)

## Überblick: was ist neu?

Der neue Raspberry Pi 3B+ wurde, genauso wie Pi Zero W, von Roger Thornton designed.

Er hat die gleiche CPU wie beim Pi 3B, allerdings jetzt mit 1,4 GHz getaktet, mit deutlich verbessertem Abwarme-Management.

Ebenfalls gleich geblieben sind der Form-Faktor: die gleichen vier USB-Ports, die anderen Anschlusse und die PWR und ACT LEDs sind am von Pi 3 Model B gewohnten Platz. Auch der RAM bleibt bei 1 GB. Damit ist der neue Pi mit den meisten Gehausen (wir haben z.B. das TEK-BERRY 3 bereits erfolgreich testen konnen) und naturlich HATs und anderem Raspberry Pi Zubehor voll kompatibel!

Dank des neuen Funk-Moduls mit Metall-Abschirmung und prominentem Raspberry Pi Logo kann man die beiden Modelle allerdings auf Anhieb leicht auseinanderhalten. Der neue Pi 3B+ funkt jetzt auch im 5GHz Band und unterstutzt WLAN IEEE 802.11ac. Fur Bluetooth wird mit 4.2 eine neuere Version unterstutzt. Ich gehe in diesem Artikel naturlich noch ausfuhrlich auf die Funk-Neuerungen ein.

Neu sind außerdem der GBit LAN Port (mit maximal ca. 300 Mbit/s Durchsatz), Power over Ethernet-Unterstutzung, und massiv verbesserter PXE Netzwerk-Boot.

![Raspberry Pi 3 Model B+ bei buyzero.de jetzt verfügbar - Ihr Raspberry Pi Partner!](https://cdn.shopify.com/s/files/1/1560/1473/files/raspberry-pi-3-model-b_grande.jpg?v=1521043269)

# BCM2837B0 Die neue CPU

Auch das "Herz" des Raspberry Pi's hat jetzt einen Metall-Look. Darf ich vorstellen? **BCM2837B0**, der neue SoC.

Wie der Name schon verrat hat sich gegenuber dem BCM2837 intern nicht genug getan, um einen Major Versionssprung zu rechtfertigen:

Es sind auch weiterhin vier ARMv8-A Cortex-A53 64-bit Prozessor-Kerne verbaut. Der Grund fur das hartnackige RAM-Limit auf 1 GB ist ebenfalls im SoC-Design zu suchen. Der VideoCore IV - der GPU und Video-Kern des Raspberry Pi in allen bisherigen Modellen ab dem Pi 1B an - unterstutzt namlich maximal 1 GB RAM.

Durch den eingebauten Warmeverteiler (heat spreader), sowie einige weitere Optimierungen ("verbesserte Power-Integritat") konnte die Taktfrequenz der CPU-Kerne auf 1,4 GHz gesteigert werden. **Das ist im Vergleich zum Pi 3 Model B ein Plus von rund 16 %!**

**Der wirkliche Clou ist jedoch, dass diese Leistung unter Last deutlich langer konsistent aufrechterhalten werden kann.**

Die Raspberry Pi Foundation hat dazu die Stromversorgung des Einplatinencomputers von Grund auf uberarbeitet. Mit dem dafur eingesetzten **MxL7704** PMIC (Power management integrated circuit) schaut das Board zudem viel aufgeraumter aus. Es wurden bisher diskrete Stromversorgungen (sogenannte Bucks und LDOs) fur verschiedene Komponenten auf der Platine in diesem einen PMIC zusammengefasst. Der MxL7704 liefert jetzt die verschiedenen benotigten Spannungen (3,3 V / 1,8 V / etc), mit deutlich hoherer Stabilitat und feinerer Justierungsmoglichkeit. So kann der Kern (SoC) mit etwas weniger oder mehr Spannung versorgt werden, woruber die Performance und Abwarme beeinflusst werden kann.

Unter 70° C interner BCM2837B0 Temperatur wird die CPU-Frequenz dank der Verbesserungen auf 1,4 GHz angehoben. Der Pi versucht so lange wie moglich mit maximaler Leistung zu laufen, reguliert ab 70°C jedoch auf 1,2 GHz herunter. Über den MxL7704 wird die Core Voltage gesenkt - dadurch kann die CPU moglichst lange weiter auf noch hoher Leistung betrieben werden bis bei 80° C abreguliert werden muss. Durch den eingebauten Warme-Verteiler, den man als metallene Oberflache sieht, wird das ganze naturlich bestens unterstutzt. In vielen Anwendungsfallen sollte die CPU nie mehr die 80°C erreichen, also die Performance nie drosseln!

Im Vergleich zum Pi 3B kann der neue Pi dadurch also wesentlich langer hoher getaktet laufen, was sich z.B. beim Webbrowsen, Retro-Gaming, und Multimedia-Bereich sehr positiv außern sollte.

Das alles hat naturlich auch seinen Preis. Wir reden hier nicht vom Preis des Boards - der bleibt auch weiterhin bei 35 $ (exklusive Mehrwertsteuer) - sondern uber das Netzteil. Der Pi 3B+ zieht deutlich mehr Leistung als sein Vorganger, daher wird ein hochwertiges 2,5 A Netzteil von den Designern dringend empfohlen. Mit dem offiziellen Netzteil der Raspberry Pi Foundation ist man auf jeden Fall auf der sicheren Seite! Wir haben es aus diesem Grund auch in unserem Sortiment (im Original Zubehor Kit und in dem Deluxe Complete Kit), und empfehlen im Zweifel fur kritische Anwendungen immer dessen Kauf.

# Microchip LAN7515: oder wie bringe ich dem Pi GBit Ethernet bei?

Auch der Pi 3 B+ hat das weithin bekannte Bottleneck, nur einen USB 2.0 Port (480 Mbit/s brutto Datenrate) auf dem SoC. Der wird uns weiterhin begleiten, bis der SoC fur den Raspberry Pi 4 komplett neu designed wird.

Der Microchip LAN7515 holt jedoch aus diesem Bottleneck fur uns das wirklich maximal mogliche heraus.

Wir erhalten auf dem Pi 3 Model B+ neben den bekannten und allseits beliebten vier USB 2.0 Ports einen (physikalischen) GBit LAN Anschluss, der mit 300 Mbit/s reellem Durchsatz immerhin dreifache Durchsatzsteigerung gegenuber dem Pi 3B bietet! Also "nicht ganz" GBit, aber es wird uns die Wartezeit bis zum Pi 4 gut uberbrucken.

Die Performance im "echten Leben" wird bspw. bei Streamen von Videos von einer angeschlossenen USB Festplatte niedriger sein - da alle Daten (USB Ports und LAN) trotzdem durch den SoC und den einen USB 2.0 Port laufen mussen.

Der neue LAN Port bietet jedoch noch mehr:

Der PXE Boot (Netzwerkboot ohne microSD Karte) wurde massiv verbessert. Alle bekannten Probleme vom Pi3 B mit dem Netzwerkboot wurden von Gordon Hollingworth in das Boot ROM vom BCM2837B0 des neuen Modells eingebaut. Es sollte jetzt super-stabil sein.

Ein weiteres Highlight ist das neue, in Kurze verfugbare PoE HAT. Das PoE HAT macht aus 48 V die bei Power over Ethernet (PoE) zusatzlich zu Daten auf den Netzwerkkabeln anliegen die vom Pi benotigten 5 V. Der Pi 3 Model B+ fuhrt dazu uber einen neuen vier PIN Header die benotigten Leitungen von der LAN-Buchse direkt fur HATs heraus.

Der Pi 3 kann also zukunftig dank PoE und PXE einfach uber ein einziges (PoE)-Netzwerkkabel angeschlossen werden, und bootet ohne zusatzliche SD Karte oder microUSB Netzteil!

Das ist vor allem fur industrielle Anwendungen, Schulen / Universitaten, Digital Signage und Point of Sale Anwendungen interessant. Dank des auf dem PoE HAT integrierten Lufters wird außerdem sichergestellt dass der Pi 3B+ nicht uberhitzt. Hier hat die Foundation das Feedback aus dem Markt wunderbar verarbeitet, und tolle neue Moglichkeiten geschaffen!

Fur alle die lieber mit USB Sticks arbeiten: booten uber USB ist beim Pi3B+ naturlich ebenfalls moglich.

Als auf den Raspberry Pi von der ersten Stunde an spezialisierte Firma beraten wir Sie naturlich gerne ausfuhrlich rund um Ihre industriellen Projekte auf Raspberry Pi Pi 3 Model B+ Basis. [Kontaktieren Sie uns noch heute fur ein unverbindliches Erstgesprach - es lohnt sich.](https://buyzero.de/kontakt)

![](https://cdn.shopify.com/s/files/1/1560/1473/files/raspi3b__und_poe_hat_raspberry_pi_foundation_grande.jpg?v=1521043645)

# CYW43455: das große WLAN & Bluetooth Upgrade fur den Raspberry Pi

![Raspberry Pi 3 Model B+ WLAN Chip CYW43455 ](https://cdn.shopify.com/s/files/1/1560/1473/files/Rpi3b__wlan_closeup_look_wlan-chip-CYW43455_grande.jpg?v=1521043840)

Der neue silberne, mit Raspberry Pi Logo versehene Chip ist markant und unubersehbar. Er wird fortan fur hervorragende WLAN & Bluetooth Verbindungen stehen!

Das hier verwendete Chipset Cypress CYW43455 (ehemals BCM43455) wird von Linux - und damit Raspbian selbstverstandlich unterstutzt. Dank Hardware-Offloading fur AES und das altere TKIP werden die vier ARM Cores des Pi 3B+ entlastet und konnen sich auf ihre Aufgaben konzetrieren. CYW43455 bietet WLAN nach dem IEEE 802.11ac Standard, sowie volle Abwartskompatibilitat zu 802.11 a/b/g/n. Es funkt im 5 GHz und 2,4 GHz Bereich.

**Warum ist das wirklich wunderbar?**

Das 2,4 GHz Band (ISM - steht fur Industrial, Scientific and Medical) ist dank seiner weltweiten Verfugbarkeit mit sehr vielen Anwendern gesattigt. Von der Mikrowelle in der Kuche (ja, die funkt auch, vor allem wenn deren Tur nicht mehr ganz dicht ist!) uber DECT fur tragbare Telefone bis hin zu Garagenturoffnern, Babyphonen und Bluetooth tummeln sich hier einfach zu viele potentielle andere Storquellen. Das 5 GHz Band - ebenfalls weltweit verfugbar - bietet hier eine hervorragende Alternative. Es bietet sogar physikalisch bedingt hohere Geschwindigkeiten - allerdings dafur eine kurzere Reichweite: die 5 GHz Signale kommen nicht so gut durch Wande und Decken wie 2,4 GHz. Nicht alle Router (bspw. altere Fritz!Boxen) unterstutzen allerdings den neuen 802.11 ac 5 GHz Standard. Vielleicht zieht also mit dem neuen Pi auch bald ein neuer Router in Ihr zu Hause?

Aber genug um den heißen Brei geredet. **Was der Leser hier sicherlich vor allem wissen will ist die tatsachliche maximal mogliche Funk-Durchsatzrate.** Dazu zunachst einige theoretische Ausfuhrungen:

Der CYW43455 unterstutzt einen single spatial stream (1x1) fur eine Datenrate von bis zu 433,3 Mbps (PHY brutto Datenrate), bei Einsatz von WLAN 802.11ac. Er unterstutzt dabei 20/40/80 MHz WLAN-Funk-Kanale mit optionaler SGI (short guard interval).

80 MHz Kanale wurden im 802.11ac Standard neu eingefuhrt. Hier gilt: je mehr Breite des Kanals, desto mehr Durchsatz. Theoretisch unterstutzt 802.11ac bis zu 160 MHz Kanalbreite, jedoch gibt es noch kaum Gerate dafur am Markt, und der RPi konnte davon sowieso nicht profitieren.

Das Guard Interval dient dazu, damit nicht mehrere unabhangige Sender sich gegenseitig storen - bei SGI wird, wie der Name schon sagt, weniger lang auf andere Sender gewartet, und damit konnen mehr Bits pro millisekunde ubertragen werden.

Die WLAN Standards bieten, bereits ab 802.11 n die Moglichkeit mehrere raumlich getrennte Antennen (spatial streams) zu verwenden, und dadurch vom selben Gerat mehrere Datenstrome gleichzeitig zum Empfanger zu schicken, der das wiederum mit seinen Antennen gleichzeitig empfangen kann. Auch hier kann der Pi nicht davon profitieren, da "nur" eine Antenne verbaut wurde.

**Auf der Chip Seite konnen wir also bis zu 433,3 Mbps schnell funken.**

Der CYW43455 ist nun aber uber SDIO (den im SoC verbauten Arasan eMMC Controller) an den Pi 3 B+ SoC angebunden (der zweite, Broadcom SD Controller, unterstutzt SDIO nicht und wird daher fur die microSD Karte genutzt). Der Arasan Controller unterstutzt nach Spezifikation das SDIO v3.0 interface. Allerdings ist nicht sicher, besser gesagt eher unwahrscheinlich ob die vom CYW43455 angebotenen Übertragungsformate DDR50 (mit bis zu 400 Mbit/s Durchsatz - dual data rate bei 50 MHz), sowie SDR104 ( mit bis zu 432 Mbit/s Durchsatz) ebenfalls unterstutzt werden. Der Arasan eMMC SDIO lauft normalerweise (auf dem Pi 3B) mit 41,6 MHz. Bei einer Übertragung von 4 bits gleichzeitig erzielt man damit (brutto) 166,4 Mbit/s. Falls DDR unterstutzt wird, dann 332,8 Mbit/s.

Anscheinend ist es (aufgrund von Clock-Settings / Dividern etc.) nicht moglich den Arasan mit 50 MHz zu takten. Der nachstmogliche - und vermutlich letzte stabile, wenn uberhaupt - Sprung ist auf 62,5 MHz. Damit erhalten wir bei 4 bit Breite 250 Mbit/s, und bei DDR 500 Mbit/s.

**Mein educated guess ist dass wir bei ca. 166,4 Mbit/s Durchsatz mit dem Pi 3B+ am Limit sind.** Das ist die Brutto-Datenrate! Protokoll-Overhead, Checksummen, etc. werden diesen Durchsatz absenken. Vielleicht konnen einige Pis auf bis zu 250 Mbit/s Durchsatz gepusht werden. Gegenuber dem Pi 3 Model B (72,2 Mbit/s WLAN Durchsatz nach 802.11n brutto maximum) ist das auf jeden Fall bereits eine Verdoppelung der Datenrate. Mit dem weniger dicht "besiedelten" 5 GHz Band kann diese Datenrate zudem auch besser ausgeschopft werden.

Der große Vorteil dieser Anbindung uber den SDIO ist dass der WLAN - Teil des Pi 3B+ vom USB Port unabhangig ist. Damit kann fur Selbstbau-Router-Projekte, etc. mehr Bandbreite ausgeschopt werden. Auch unsere Anonymebox (Tor basierende Plug & Play Anonymisierungslosung) profitiert davon.

Im echten Leben konnen wir wohl mit bis zu 102 Mbit/s netto Durchsatz im 5 GHz Band rechnen (Zahlen von Milhouse, dem [LibreELEC ](https://libreelec.tv/)Entwickler). Das spricht fur den Arasan SDIO Port als Bottleneck.

Interessanterweise wurde wie beim[ Pi Zero W ](https://buyzero.de/products/raspberry-pi-zero-w?variant=38399156114)auch eine Proant PCB Antenne verbaut. Dadurch soll ebenso eine etwas bessere Performance (Durchsatz + Reichweite) im 2,4 GHz Bereich erreicht werden als beim Pi 3.

## Vor-zertifiziertes WLAN-Modul fur eigene Produkte

Weniger interessant fur Hobby-Maker, dafur allerdings sehr (!) interessant fur Unternehmen, Startups und die Geschaftswelt ist das vor-zertifizierte WLAN-Modul. Zusammen mit dem Compute Module 3 kann das Modul zukunftig in eigene Projekte eindesigned werden. Durch die Abschirmung (mit dem Raspberry Pi Logo) konnte es als modulare Losung zertifiziert werden.

Dank dieser bereits durch die Foundation erfolgten Zertifizierung - die Unmengen an Geld und Zeit verschlungen hat - konnen andere Unternehmen jetzt Produkte auf Basis der Raspberry Pi Plattform herausbringen. Die Raspberry Pi Plattform steht naturlich nicht nur fur hervorragenden Software Support, sondern auch fur solides Engineering, und gute Langzeitverfugbarkeit.

Damit konnen Unternehmen also eigene WLAN und Bluetooth-fahige Losungen - fur moderne Gerate in unserer vernetzten IoT Welt unverzichtbar - gemaß Eben Upton 10 x gunstiger und schneller auf den Markt bringen. In den meisten Fallen wird nur eine Zertifizierung der nicht-Funk Teile erforderlich sein. Das Modul ist dank der Raspberry Pi Foundation weltweit zertifiziert und einsetzbar.

## Bluetooth 4.2

Der Pi 3 B unterstutzte noch Bluetooth 4.1; Mit dem CYW43455 unterstutzt der Pi 3B+ jetzt auch Bluetooth 4.2, und damit naturlich weiterhin "Bluetooth Classic" und Bluetooth LE (Low Energy).

Kleiner Versionssprung - große, tolle neue Features fur Ihre IoT Gerate!

Bluetooth 4.2 verbessert fur Bluetooth LE die Geschwindigkeit, den Datenschutz und die Datensicherheit. (Stichworte: LE Privacy 1.2, LE Secure Connections, LE Data Length Extension).

Die Bluetooth LE Daten-Pakete konnen zukunftig 2,5 x schneller verschickt werden, und die Pakete konnen jetzt bis zu 10 x mehr Daten enthalten, im Vergleich zur vorigen Version.

Bluetooth 4.1 sieht bereits vor, dass Smart Devices leichter miteinander reden konnen, ohne einen Hub wie bspw. einen Computer oder ein Telefon nutzen zu mussen.

**Bluetooth 4.2 bringt das jedoch auf eine komplett neue Ebene:**

Mit dem IPSP unterstutzten 6LoWPAN (Internet Protocol Support Profile / Low Power Wireless Personal Area Networks) soll das Internet Protokoll (IP) auf kleinen und leistungsschwachen Geraten unterstutzt werden um am Internet der Dinge (Internet of Things) teilhaben zu konnen. Leistungsschwache Gerate? Sensoren, Aktoren, vernetztes Haus, IoT-Gerate, ... - Dinge wo man normalerweise keinen Bildschirm hat um ein WLAN Passwort einzugeben. Dazu werden IPv6 Pakete fur den direkten Internetzugriff genutzt.

Bluetooth Smart Internet Gateways (GATT) ist eine weitere Funktionalitat, die einen Gateway ins Internet bereitstellt. Beispielsweise kann so ein Bluetooth 4.2 Sensor durch den Pi 3B+ als Gateway device Nachrichten schicken und empfangen.

Zum Thema Datenschutz: Bluetooth Beacons die versuchen Ihr Gerat zu tracken mussen ab v4.2 erst explizit eine Erlaubnis von Ihnen bekommen.

LE Secure Connections ist ein neuer Algorithmus fur besonders sicheres Pairing von Bluetooth Geraten, der erst ab Bluetooth 4.2 verfugbar ist. Dadurch konnen zukunftig beispielsweise auch sicherheitskritischere Anwendungen, wie automatisches Aufmachen der Wohnungstur durch den Raspberry Pi, besser abgesichert werden.

Die aktuellste Version ist ubrigens Bluetooth 5, das 2016 vorgestellt wurde - diese wird vom neuen Pi noch nicht unterstutzt.

WLAN und Bluetooth sind auf dem CYW43455 in unabhangigen Hardwareeinheiten implementiert. Der Chip sorgt durch interne Verbindungen und "Absprache untereinander", sowie optimierte Empfangs-Algorithmen allerdings fur eine friedliche und produktive Koexistenz.

![Raspberry Pi 3B+ mit GBit Ethernet Port, WLAN 802.11ac, Bluetooth 4.2, und 1,4 GHz Taktfrequenz](https://cdn.shopify.com/s/files/1/1560/1473/files/rasp-3bplus-gbit-port_grande.jpg?v=1521044598)

# Performance Tests

Wir haben fur diesen Artikel nur mit einem pre-release Image testen konnen, bei dem WLAN noch nicht aktiviert war, **und die CPU mit 1,2 GHz getaktet wurde**. Einen Test mit dem neuen Software-Image reichen wir demnachst nach, und erwarten naturlich deutlich bessere Performance fur den Pi 3B+. Hier sind dennoch unsere Resultate als eine Orientierung:

**Raspberry Pi 3 B**

**Raspberry Pi 3 B+**

**Kommentar**

**Spezifikationen**

SOC

Broadcom BCM2837

Broadcom BCM2837B0

jew. 4 x Cortex-A53

CPU

Cortex-A53 @ 1,2 GHz

Cortex-A53 @ 1,4 GHz

**Pi 3 B+ mit 1,2 GHz getestet!**

RAM

1024 MB LPDDR2

1024 MB LPDDR2

LAN

10/100 Mbit

1000 Mbit

uber USB 2.0

Power

5 V, 2.5 A

5 V, 2.5 A

via microUSB

**Sysbench**

Sysbench - CPU (sec)  
(Total Time)   
3 repeats 4 threads

93,0516 sec

92,8582 sec

kurzer ist besser

Sysbench - CPU (sec)   
(Total Time by event execution)   
3 repeats 4 threads

372,0941 sec

371,3438 sec

kurzer ist besser

**Speicher: ****_MBW - RAM (MiB/s)_**

Memcpy

694,796 MiB/s

785,585 MiB/s

mehr ist besser

Dumb

721,429 MiB/s

807,196 MiB/s

mehr ist besser

Mcblock

1086,907 MiB/s

1287,237 MiB/s

mehr ist besser

**Netzwerk (LAN)**

Iperf - Ethernet (Mbits/s)  
3 repeats

94,2 Mbit/s

319 Mbit/s

mehr ist besser

**Hdparm (SD Karte)**

Cached

601,79 MB / s

599,96 MB / s

mehr ist besser

Disk Reads

21,61 MB / s

21,66 MB / s

mehr ist besser

**Stromverbrauch (Watt)**

Idle

4,2 W

7,6 W

Sysbench Power Consumption  
(3 repeats, 4 threads)

11,7 W

14,0 W

Verbrauch wahrend dem Sysbench Test.

Es ist fur den Betrieb des neuen Raspberry Pi's 3B Plus[ auf jeden Fall neue Software erforderlich](https://www.raspberrypi.org/downloads/noobs/) \- er wird mit NOOBS vor der Version 2.7.0, die am 14.03.2018 erschienen ist nicht booten. Fur Raspbian Jessie wird die Firmware ebenfalls zur Verfugung gestellt (werden). Es wird vermutlich eine Weile dauern, bis andere Distributionen, wie bspw. LibreELEC, RetroPie etc. nachgezogen haben - mit den neuen Features des neuen Pis durfte das Resultat dann aber fur sich sprechen, die Geduld wird reichlich belohnt werden!

Alle Fans des 40 Pin GPIO Headers konenn aufatmen - alles ist wie gehabt, alle heißgeliebten Erweiterungs-HATs werden unterstutzt. Wie beim Pi 3B und Pi Zero W ist Bluetooth jedoch uber den "guten" UART angebunden (den PL011). Nutzer des UARTs uber den GPIO Header sollten die bekannten Einschrankungen des hier zur Verfugung stehenden miniUARTs beachten, bzw. per Overlay die zwei UARTs tauschen oder Bluetooth deaktivieren. Ich verweise hier auf meinen Artikel uber den Pi3 B in der entsprechenden Raspberry Pi Geek Ausgabe.

Der RUN Header hatte vorher zwei Pins. Einer davon war Ground - beim Verbinden des "RUN" Pins an GND wurde die CPU zuruckgesetzt. Der Header konnte also verwendet werden um einen Reset-Taster einzubauen. Dabei blieb jedoch die Stromzufuhr komplett eingeschaltet, auch bei kontinuierlichem Halten des RUN Pins an GND war die CPU zwar praktisch gesehen aus, aber es wurde trotzdem Strom verbraucht.

Im Pi 3B+ wurde der GND Pin aus diesem Header entfernt, und ein neuer Pin "PEN" hinzugefugt. PEN steht dabei fur Power ENable. Beim Verbinden des PEN Pins an GND wird dem Board der Strom komplett entzogen - es geht damit in den niedrigsten Stromverbrauchszustand in den es gehen kann. Sicherlich sinnvoll fur batteriebetriebene Losungen, die das Board dann aus dem Tiefschlaf mit einem kleinen Mikrocontroller aufwecken konnen.

Wo GND holen, wenn nicht stehlen? Auf dem GPIO Port stehen jede Menge GND Pins zur Verfugung, auch ist die außere Hulle der USB Ports auf Ground. Eine Buroklammer ist vermutlich lang genug. Just saying.

# Resumee und zusammenfassung

Der Raspberry Pi 3 B+ ist, wie der Name schon sagt, kein Pi 4. Liebevoll entwickelt, bietet er aber noch etwas mehr Leistung als sein Vorganger in fast jeder "Disziplin" eines Single Board Computers. Ähnlich wie Pi 1B+ vs. 1B, handelt es sich hier um kontinuierliche Weiterentwicklung und Liebe zum Detail statt Quantensprung.

Wie bereits erwahnt ist das Limit auf 1 GB RAM durch den VideoCore IV bedingt, der deutlich fester in einem BCM283x verbacken ist, als die ARM Cores; Uns liegen keine Informationen zu einer hoheren Taktung des VideoCore IV, oder anderen Veranderungen daran vor. Aus der Erfahrung mit dem Pi 3B wissen wir, dass auch H.265 Video in vielen Fallen flussig abspielbar sein sollte - in Software hardwarebeschleunigt dekodiert.

Der Pi 4 wird vermutlich ein großeres Redesign auch dieser bislang unberuhrten Teile des SoCs werden. Das wird uns sicher neue Moglichkeiten und zukunftige Upgrade-Pfade eroffnen - mehr RAM, dedizierte USB Ports (USB 3 ware schick, liebe Foundation!), volle 1000 Mbit/s GBit LAN, usw. usf. Dieses Redesign braucht naturlich Zeit, die die Foundation durch den Release des Pi 3B+ fur uns uberbrucken mochte.

Der Pi 3 B+ wird hergestellt werden bis zum Januar 2023. Die Foundation versichert uns, dass auch die anderen Modelle (Pi 1B+, 2, 3) bei entsprechender Nachfrage weiter hergestellt werden. Wir konnen uns demnachst eventuell auf eine Pi 3A+ Variante (ohne LAN und mit nur einem USB Port), sowie ein Compute Module 3+ freuen.

Wir bieten ihn auf [buyzero.de zum Start am 14.3.2018 fur 34,50 € an, inklusive Mehrwertsteuer](https://buyzero.de/products/raspberry-pi-3b-plus?variant=6471085359131) (Preis konnte in der Zwischenzeit steigen - schnell sein, und [gleich bestellen!](https://buyzero.de/products/raspberry-pi-3b-plus?variant=6471085359131)). Den Pi 3B+ [bieten wir ohne jegliche Mengenbeschrankungen an](https://buyzero.de/products/raspberry-pi-3b-plus?variant=6471085359131) \- Mengen ab 1000 Stuck bitten wir jedoch u[ber unseren Support anzufragen](https://buyzero.de/pages/kontakt), um die Logistik und Lieferzeiten klaren zu konnen.

Shortlink: der Raspberry Pi 3B+ ist unter folgender URL - in beliebiger Menge - erhaltlich:

Hier ist auch ein Konfigurator hinterlegt, mit dem man gleich d**as optimale Zubehor konfigurieren**, oder ein Einsteiger-Set kaufen kann. Wir empfehlen das [Deluxe Complete Kit mit original Raspberry Pi Foundation Zubehor](https://buyzero.de/products/raspberry-pi-3b-plus?variant=6471085522971) (Netzteil & Gehause).

Ab 75 € bieten wir versandkostenfreien Versand per DHL innerhalb Deutschlands an!

# Über pi3g

Seit 2012 sind wir ausschließlich auf den Raspberry Pi fokussiert, und haben viel Erfahrung mit dem beruhmten Singleboardcomputer sammeln konnen. pi3g ist im DACH Raum (Deutschland, Österreich, Schweiz) approved Raspberry Pi Reseller der Raspberry Pi Foundation, sowie offizieller Pi Zero & Pi Zero W Distributor.

Wir sind neben der Raspberry Pi Foundation mit vielen weiteren Partnerschaften rund um den kleinen Einplatinenrechner aufgestellt - vom Gehause uber Software bis zur Platinenentwicklung konnen wir Ihnen alles aus einer Hand bieten.

[Wir sind damit eine hervorragende Anlaufquelle fur Consulting & Realisation rund um Ihre Raspberry Pi basierenden embedded-Projekte, Industrie-Steuerungen, Industrie-Projekte aller Art, fur Sortimentserweiterungen Ihres Online-Shops rund um den Raspberry Pi, und fur Sourcing von Raspberry Pi Komponenten.](https://buyzero.de/pages/kontakt)
