# Github-Projekt shaircast: Raspberry Pi als Multiroom-AirPlay-Server

_Captured: 2016-01-09 at 19:38 from [www.ifun.de](http://www.ifun.de/github-projekt-shaircast-raspberry-pi-als-multiroom-airplay-server-86934/)_

Falls ihr mehrere AirPlay-Lautsprecher im Haus und zufallig noch einen Raspberry Pi rumliegen habt, wollt ihr euch vielleicht an folgendem Bastelprojekt versuchen: Mit [shaircast](https://github.com/nguyer/shaircast) konnt ihr die Beschrankung aushebeln, dass sich von einem iOS-Gerat aus nicht mehrere AirPlay-Lautsprecher zugleich ansprechen lassen. Apple lasst dies nur beim Audiostreaming von iTunes aus zu.

![raspberry-pi-2-500](http://images.ifun.de/wp-content/uploads/2015/02/raspberry-pi-2-500.jpg)

shaircast baut auf die Open-Source-Plattform [node.js](https://nodejs.org/en/) und bringt die beiden unabhangig von einander existierenden Projekte [NodeTunes](https://github.com/stephen/nodetunes) und [Node-AirTunes](https://github.com/lperrin/node_airtunes) unter einen Hut. NodeTunes macht dabei den Raspberry Pi zum AirPlay-Empfanger und Node-AirTunes kummert sich um die Ausgabe an alle verfugbaren AirPlay-Lautsprecher.

Auf diese Weise konnt ihr euch ein von iOS-Gerats aus bespielbares AirPlay-Multiroom-System zusammenhacken. Allerdings werden stets alle Lautsprecher gemeinsam angesprochen. (Danke David)
