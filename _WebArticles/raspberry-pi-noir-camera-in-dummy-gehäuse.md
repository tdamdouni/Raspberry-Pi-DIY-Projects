# Raspberry Pi – NoIR Camera in Dummy-Gehäuse

_Captured: 2017-05-23 at 18:50 from [mathias-biedert.de](http://mathias-biedert.de/2015/11/13/raspberry-pi-noir-camera-in-dummy-gehaeuse/)_

![](http://mathias-biedert.de/wp-content/uploads/2015/11/20151122_1630291.png)

Mir Kamm die Idee meine Raspberry Pi NoIR Cam mit dem IR-Ring in eine Kamera Attrappe einzubauen.  
Gesagt getan

**Folgende Material wird benotigt:**

- [Wasserdichte Kamera Attrappe](http://www.amazon.de/gp/product/B0058QSFCG/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B0058QSFCG&linkCode=as2&tag=m09da-21)  
- [Infrarot-Baugruppe mit 36 IR-Leds](http://www.amazon.de/gp/product/B008X0OEOC/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B008X0OEOC&linkCode=as2&tag=m09da-21)  
- [Raspberry Pi NoIR Kamera-Modul](http://www.amazon.de/gp/product/B00G9AZ79O/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B00G9AZ79O&linkCode=as2&tag=m09da-21)  
- [Raspberry Pi 2 Model B](http://www.amazon.de/gp/product/B00T2U7R7I/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B00T2U7R7I&linkCode=as2&tag=m09da-21)  
- [MicoSD 8GB](http://www.amazon.de/gp/product/B00MWXUKDK/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B00MWXUKDK&linkCode=as2&tag=m09da-21)  
- [MT3608 DC-DC Step Up Power Modul](http://www.ebay.de/itm/272029531535?_trksid=p2057872.m2749.l2649&ssPageName=STRK%3AMEBIDX%3AIT)  
- [MicoUSB Verlangerung](http://www.amazon.de/gp/product/B0052L7F3M/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B0052L7F3M&linkCode=as2&tag=m09da-21) oder Netzteil direkt verloten  
- [MicoUSB Netzteil 5V 2000mA](http://www.amazon.de/gp/product/B00GM0305Y/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B00GM0305Y&linkCode=as2&tag=m09da-21)  
- [Netzwerkleitung Slim 10m](http://www.amazon.de/gp/product/B004WCQFGU/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B004WCQFGU&linkCode=as2&tag=m09da-21) alternativ [WLAN-Stick](http://www.amazon.de/gp/product/B003MTTJOY/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1638&creative=6742&creativeASIN=B003MTTJOY&linkCode=as2&tag=m09da-21)  
- [Litzenkabel 0,14mm²](http://www.ebay.de/itm/Litzenkabel-0-14mm-10m-5m-3m-Rollen-in-schwarz-rot-blau-und-grun-wahlbar-/351525469693?var=&hash=item51d88cfdfd:m:mjL_BbiSG-hERoRXWQZ_vew)

**Verwendetes Werkzeug:**

![20151113_092731---Kopie](http://mathias-biedert.de/wp-content/uploads/2015/11/20151113_092731-Kopie1.png)

Als Erstes habe ich das Ganze Gehause auseinandergenommen. Die IR-Attrappe einfach entnehmen dazu die Schrauben losen.  
Dann habe ich mir den Infrarot-Baugruppe genommen und die Rander mit einem Seitenschneider gekurzt, bis sie in den schwarzen Ring passen. Vorsicht nicht die Leiterbahnen beschadigen.  
Dann habe ich das NoIR Kameramodul mit Heißkleber die Kamera mittig in den Infrarot-Baugruppering geklebt. Dann habe ich mir von der Attrappe das Objektiv genommen und auf 2 cm gekurzt habe dazu die Puksage genommen. Die Fakelinse einfach mit dem Fingerrausdrucken. Dann die Objektiv-Hulse mittig auf die Kamera mit Heißkleber drucken. Dann das Ganze wider verschrauben. Sollte da so aussehen:

![20151113_111729](http://mathias-biedert.de/wp-content/uploads/2015/11/20151113_111729.jpg)

Als nachstes Sagen wir die Ruckblende an damit wir das Netzteilkabel und das Netzteilkabel durchstecken konnen.  
Oder wir scheiden den Stecker vom Netzteil ab und benutzen einen WLAN-Stick dann konnen wir uns das sparen.

![20151113_111732](http://mathias-biedert.de/wp-content/uploads/2015/11/20151113_111732.jpg)

So jetzt mussen wir nur noch alles Zusammenloten. Ich habe hier mal Anschlussplan erstellt.

![Anschlussplan RaspberryPi Cam Dummy](http://mathias-biedert.de/wp-content/uploads/2015/11/Anschlussplan-RaspberryPi-Cam-Dummy.png)

Dann mussen wir nur noch das Image fur die Kamerasoftware [hier](https://github.com/ccrisan/motionPie/releases) herunterladen und auf die MicoSD-Karte schreiben.  
Zum Schluss wieder alles zusammen Bauen und testen Hier meine Kamera im Einsatz:

![](http://mathias-biedert.de/wp-content/uploads/2015/11/20151122_162436-150x150.jpg)

Hier die nachtraglich von Euch gewunschte Testbilder:

~ lg. Mathias ~
