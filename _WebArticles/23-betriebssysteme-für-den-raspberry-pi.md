# 23 Betriebssysteme für den Raspberry Pi

_Captured: 2017-05-19 at 11:43 from [www.elektronikpraxis.vogel.de](http://www.elektronikpraxis.vogel.de/single-board-computer/raspberry-pi/articles/488934/)_

![Die Standarddistribution: Von Beginn an ist das Debian-basierte Raspbian das empfohlene Einsteiger-Betriebssystem für alle Varianten des Raspberry Pi. Die aktuelle Version, Raspbian ](http://images.vogel.de/vogelonline/bdb/1004400/1004411/24.jpg)

> _[Die Standarddistribution: Von Beginn an ist das Debian-basierte Raspbian das empfohlene Einsteiger-Betriebssystem fur alle Varianten des Raspberry Pi. Die aktuelle Version, Raspbian "Jessie", wurde im Marz 2016 auf Kernel-Version 4.1 aktualisiert. Fur Einsteiger, Fortgeschrittene oder Experimentierfreudige existiert allerdins noch eine breite Anzahl an Betriebssystem-Alternativen fur den Einplatinenrechner.](http://www.elektronikpraxis.vogel.de/index.cfm?pid=11180&pk=1004411&type=article&fk=488934)_

(Bild: Screenshot / Raspberry Pi Foundation)

Neueinsteiger greifen zur Standarddistribution Raspbian, Microsoft mochte Windows 10 auf den Einplatinenrechner pushen. Allerdings gibt es fur das Raspberry Pi noch viele weitere OS-Alternativen. Hier ist fur fast jeden Geschmack ein Betriebssystem dabei - ob schlankes Maker-System, handliches Media Center, Netzwerk-bootbares Multiuser-OS oder obskure Unix-Variante.

In erster Linie als Linux-System fur Einsteiger in die Programmierung und Bastler fur IoT-Anwendungen bekannt, erlangt der Minicomputer [Raspberry Pi auch zunehmend fur industrielle Losungen](http://www.elektronikpraxis.vogel.de/hf/articles/526402/) Aufmerksamkeit . Hatte sich der Einplatinenrechner bis Oktober 2015 weltweit bereits uber 7 Millionen Mal verkauft, durfte diese Zahl nach dem Erscheinen der 5-Dollar-Variante [Raspberry Pi Zero](http://www.elektronikpraxis.vogel.de/embedded-computing/articles/514099/) und dem derzeitigen Spitzenmodell [Raspberry Pi 3](http://www.elektronikpraxis.vogel.de/embedded-computing/articles/523253/) noch einmal gewaltig gewachsen sein (Sehen Sie hierzu auch unsere Übersichtstabelle [Alle Raspberry-Pi-Modelle im Überblick](https://www.elektronikpraxis.vogel.de/index.cfm?pid=14967)).

_(Anmerkung: Bei diesem Beitrag handelt es sich um ein Update des ursprunglichen Artikels vom 11. Mai 2015)._

[ Fotostrecke starten: Klicken Sie auf ein Bild (22 Bilder) ](http://www.elektronikpraxis.vogel.de/index.cfm?pid=7525&pk=488934&fk=1004414&type=article)

Fur den ersten Start empfiehlt die Raspberry Pi Foundation, die Programmsammlung NOOBS (New Out Of the Box Software) zu verwenden. Der NOOBS-Installer stellt einem in der aktuellen Version 1.9 beim ersten Systemstart funf empfohlene Betriebssysteme zur Auswahl. Neben dem Standard-OS Raspbian sind das derzeit die Mediacenter-Systeme OpenELEC und OSMC, RISC OS sowie Microsofts Windows 10 IoT Core.

Damit sind die Moglichkeiten aber noch lange nicht erschopft: Fur den Raspberry Pi existieren noch zahlreiche unterschiedliche Linux-Varianten, die sich an unterschiedliche Geschmacker richten und verschiedene Spezialitaten oder Anwendungsmoglichkeiten mit sich bringen. Selbst abseits des weit verbreiteten, freien OS haben sich zahlreiche Entwickler bemuht, auch andere Betriebssysteme auf den Einplatinenrechner zu portieren. Neben dem Standard-OS Raspbian mochten wir daher an dieser Stelle 20 Betriebssysteme vorstellen, die Sie als Alternative auf Ihrem Raspberry Pi einsetzen konnen.

  


### Weitere Linux-Beispiele: Fedberry, Kali und OpenSUSE

![Wer früher gerne Pidora auf dem Raspberry Pi eingesetzt hat oder generell Fedora gegenüber Debian \(und dem Debian-Derivat Raspbian\) bevorzugt, kann inzwischen zu Fedberry greifen. Die für das Raspberry Pi 2 optimierte Linux-Distribution ist ein Remix des aktuellen Fedora 23 und kann auf dessen App-Repository zurückgreifen.](http://images.vogel.de/vogelonline/bdb/1004400/1004418/4.jpg)

> _Wer fruher gerne Pidora auf dem Raspberry Pi eingesetzt hat oder generell Fedora gegenuber Debian (und dem Debian-Derivat Raspbian) bevorzugt, kann inzwischen zu Fedberry greifen. Die fur das Raspberry Pi 2 optimierte Linux-Distribution ist ein Remix des aktuellen Fedora 23 und kann auf dessen App-Repository zuruckgreifen._

(Bild: Fedberry.org) 

Eine lange Zeit ebenfalls weit verbreitete Alternative, die lange Zeit auch im NOOBS-Installer integriert war, war die Fedora-basierte Linux-Distribution [Pidora](http://pidora.ca/). Diese Linux-Variante war ab 2014 auf die in den Raspberry-Pi-1-Modellen verwendete ARMv6-Architektur zugeschnitten. Allerdings wird Pidora bereits seit geraumer Zeit nicht mehr weiterentwickelt, so dass sich das OS bereits auf dem Raspberry Pi 2 nicht mehr vernunftig einsetzen ließ.

Dafur springt hier der Fedora 23 Remix [Fedberry](http://fedberry.org/) in die Bresche. Dieses OS lauft auch auf den Modellen Raspberry Pi 2 sowie 2B und bietet Zugriff auf das umfangreiche Angebot an vorgefertigten Packages der aktuellen Fedora-23-Fassung. Im Vergleich zu Arch Linux - und, je nach Anwendung, auch zu Raspbian - hat Fedberry allerdings immer noch gelegentlich mit Geschwindigkeitsproblemen zu kampfen. Anfanger oder Linux-Nutzer, die Fedora gegenuber Debian bevorzugen, sollten allerdings gut mit diesem Betriebssystem zurechtkommen. Grundsatzlich ist es zwar moglich, Fedora 23 auch direkt auf einem Raspberry Pi 3 Model B zu installieren. Allerdings ist hierbei mit deutlichen Leistungseinschrankungen zu rechnen, da - ahnlich wie bei Arch Linux - die zugrunde liegende ARMv8-Prozessorarchitektur noch nicht voll unterstutzt wird.

[ Fotostrecke starten: Klicken Sie auf ein Bild (22 Bilder) ](http://www.elektronikpraxis.vogel.de/index.cfm?pid=7525&pk=488934&fk=1004414&type=article)

Eine vergleichsweise junge Linux-Distribution, um die sich aber schnell eine große Fangemeinde gebildet hat, ist [Kali Linux](https://www.kali.org). Das 2013 erstmals veroffentlichte Betriebssystem basiert ursprunglich auf Debian und ist speziell auf Sicheheitstests und -anwendungen optimiert. Kali Linux wurde schnell auf diverse Prozessorarchitekturen angepasst und unterstutzt seit Version 1.0.9 (August 2014) auch das Raspberry Pi B+. [Version 2.1.2 von Kali](http://docs.kali.org/kali-on-arm/kali-linux-raspberry-pi2) lasst sich auch auf dem Raspberry Pi 2 und dem Raspberry Pi 3 installieren.

Neben den hier genannten haben auch andere Linux-Varianten auf die eine oder andere Art ihren Weg auf den Einplatinenrechner gefunden. So unterstutzt etwa auch OPENSuse, fruher weit verbreitet und in Deutschland noch mit einer treuen Fangemeinde, die ARM-Prozessorarchitektur und [lasst sich auch fur den Einsatz auf dem Raspberry Pi 2](https://en.opensuse.org/HCL:Raspberry_Pi2) anpassen. Allerdings ist das OS nicht optimal auf die Hardware des RasPi zurechtgeschnitten, so dass die Installation von OpenSUSE auf dem Einplatinenrechner nur wirklich eingefleischten Fans zu empfehlen ist.

Auch andere Linix-Distributionen haben einen Weg auf den Einplatinenrechner gefunden, so etwa gentoo. Ähnlich wie auch OpenSUSE sind diese aber in der Regel nicht fur einen idealen Einsatz auf dem Raspberry Pi ausgereift.
