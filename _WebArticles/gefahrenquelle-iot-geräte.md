# Gefahrenquelle IoT Geräte

_Captured: 2017-05-19 at 11:38 from [developer-blog.net](https://developer-blog.net/gefahrenquelle-iot-geraete/)_

**IoT Gerate** sind eine Gefahrenquelle die lange Zeit unbeachtet blieb. Ende letzter Woche gab es einen **großen DDoS Angriff**, worauf zahlreiche Bekannte Webdienste ausgefallen sind. Laut ersten Analysen spielten IoT Gerate dabei eine zentrale Rolle. Ich habe dazu recherchiert und herausgefunden, warum der Raspberry Pi ein gutes IoT Gerat ist.

![Gefahrenquelle IoT Geraete](https://developer-blog.net/wp-content/uploads/2016/10/gefahrenquelle-iot-geraete.jpg)

## Gefahrenquelle IoT Gerate

Drucker, Babyphones und Kameras haben am Freitag zu hundert tausenden gemeinsam das **DynDNS Service** mit laufenden Anfragen blockiert. Dieser DDoS Angriff hatte es darauf angelegt zahlreiche beliebte Webdienste zu blockieren. Twitter, Paypal, Spotify und einige andere auch wurden zeitweise lahmgelegt. Das ging deshalb, das diese Dienste DynDNS Services nutzen.

### Warum IoT?

In einem Artikel uber die [Sicherheitslucke IoT](https://technology-blog.net/sicherheitsluecke-iot/) wird das Problem sehr schon in dem Ausdruck „**Internet of unpatchable Things**" ausgedruckt. Das beschreibt das Problem voll und ganz. IoT Gerate werden verkauft und genutzt, bestehen aber wie jeder Laptop oder jedes Smartphone immer aus Hardware und Software. Bei einem Laptop wurde der Kaufer in den letzten Jahren zusehends darauf trainiert die Updates laufend einzuspielen. Manche Systeme wie Windows spielen diese automatisch ein, sofern man das nicht manuell unterbindet. Durch laufende Sicherheitsupdates bleibt eine Software zumindest auf einem hohen Level sicher. Angreifer haben es so recht schwer bekannte Sicherheitslucken auszunutzen. Der Aufwand fur einen Hack ist hoch. **Maleware** kann eigentlich nur durch die Dummheit des Benutzers eindringen (Download Link im Mail, manuelles Herunterladen von Schadhafter Software).

### Keine Updates

IoT Gerate werden nie aktualisiert. Das ist eine Tatsache, wer mir nicht glaubt sollte sich die Frage stellen: „Wann hast du zuletzt die Firmware deines Druckers, Fernsehers oder Kamera aktualisiert?". Es ist nicht so, dass es keine Updates gabe. Man kann ein beliebiges Modell eines Druckers nehmen und auf der offiziellen Webseite des Herstellers nach Firmware Updates suchen. Bestimmt findet man dort Versionen die hoher sind als die aktuelle Software auf dem eigenen Gerat ist. Dieses Problem wird in Zukunft sogar noch schlimmer: wer wurde manuell fur jede einzelne Gluhbirne ein Softwareupdate einspielen? Tatsachlich ist es sowohl dem Verkaufer als auch dem Kunden egal, ob das IoT Gerat infiziert ist oder nicht. Solange es korrekt funktioniert. Aufregen wird sich der Kunde erst, wenn sein Webservice nicht funktioniert. Selbst dann, wenn seine eigenen Gerate an der Storung schuld sind!

Es sind aber nicht nur die fehlenden Updates die problematisch sind. Meist ist der Hersteller schlampig und verwendet Standardpassworter fur eine komplette Gerateserie. Wer kommt schon auf die Idee bei einem Babyphone oder einer Kamera das Master Passwort zu andern?

### Problemlosung

Im Artikel wird behauptet es gebe zu diesem Problem aktuell keine Losung. Das stimmt. Ein Losungsansatz ware aber der **Raspberry Pi**. IoT Gerate die auf dem Raspberry Pi basieren konnten durch automatische Updates sicher gehalten werden. **Linux** ist das Betriebssystem fur Server und hat demnach die großte Erfahrung wenn es heißt sicher vor Angriffen zu sein, schließlich steht jeder Server 24 Stunden am Tag als Angriffsziel parat. Genau das wird bei einem mit dem Internet verbundenem IoT Gerat der Fall sein. Es bleibt abzuwarten ob der Angriff am Wochenende zu Reaktionen der Hersteller oder Seitens der Politik kommen wird. Das Gefahrenpotential durch IoT Gerate steigt mit jedem verkauften Gerat. Der Raspberry Pi mit Linux als Basis ware ein Schritt zu mehr Sicherheit.

## Fazit

IoT Gerate lassen sich offenbar recht einfach durch Maleware infizieren und in ein **großes Botnetz** zusammenzufuhren. Ein Gefahrenpotential das leider viel zu lange unterschatzt wurde. Der Raspberry Pi konnte ein Losungsansatz sein.

Was denkt ihr daruber? Wer hat von euch spielt regelmaßig Firmware Updates ein?
