# Firmware- und Kernel-Update mit rpi-update beim Raspberry Pi

_Captured: 2017-05-06 at 15:47 from [www.elektronik-kompendium.de](https://www.elektronik-kompendium.de/sites/raspberry-pi/2006061.htm)_

"rpi-update" ist ein Tool, mit dem man ein Firmware- und Kernel-Update auf dem Raspberry Pi durchfuhren kann. "rpi-update" ist ein eigenstandiges Script, das von Github die aktuelle GPU-Firmware, den Bootloader, den Linux-Kernel mit verschiedenen Modulen und die Userspace-Bibliotheken fur VideoCoreIV und ARMv6 herunterladt.

### Was man uber rpi-update wissen muss!

Achtung! Es gibt es nur wenige Situationen, bei der das Ausfuhren von "rpi-update" notwendig ware. Vor allem wenn man nicht weiß warum. Es gibt so gut wie keinen Grund an einem laufenden System ein Firmware- und Kernel-Update mit "rpi-update" durchzufuhren. Die Gefahr ist viel zu groß, dass danach das eine oder andere System nicht mehr richtig funktioniert.  
Ein Update uber "rpi-update" kann "unstable" sein. Das heißt, dass daran noch entwickelt wird und dass es vielleicht fehlerhaft ist. Sobald Firmware, Bootloader, der Kernel und die Bibliotheken "stable" sind, werden sie uber "apt-get upgrade" verfugbar gemacht und sind dann offiziell installierbar.  
Deshalb generell die Empfehlung, Finger weg von "rpi-update". Es sei denn man weiß, warum man das tut.

### Firmware- und Kernel-Update durchfuhren (empfohlen)
    
    
    sudo apt-get update
    sudo apt-get upgrade

Ein Firmware- und Kernel-Update kommt beispielsweise mit dem Paket "raspberrypi-bootloader" und bringt in der Regel eine neue Firmware, einen neuen Kernel und verschiedene aktualisierte Module und Bibliotheken mit.

  * [Betriebssystem und Software des Raspberry Pi aktualisieren](https://www.elektronik-kompendium.de/sites/raspberry-pi/2002041.htm)

### Firmware- und Kernel-Update durchfuhren (nicht empfohlen)

Finger weg von "rpi-update". Es sei denn man weiß, warum man das tut.
    
    
    sudo rpi-udpate

Nach einem Kernel-Update ist immer ein Reboot fallig.
    
    
    sudo reboot

Viel Gluck!

Hat man versehentlich ein "rpi-update" gemacht, und festgestellt, dass das eine oder andere nicht mehr funktioniert, dann muss man warten, bis uber "apt-get upgrade" ein stabiles und fehlerfreies Upgrade angeboten wird. Oder man fuhrt ein Downgrade durch.

### Wenn nach einem „rpi-update" nichts mehr geht

  1. Wenn ein Raspberry Pi nach einem "rpi-update" nicht mehr richtig startet, kann es helfen, wenn man mit Strg + Alt + F2 oder F3 oder F4 in eine Konsole wechselt. Eventuell hat man dann eine Chance, einen Downgrade bzw. ein Rollback durchzufuhren.
  2. Eventuell kann man auch mit einem geeigneten System in der Datei "/boot/config.txt" die Zeile "start_x=0" eintragen und danach prufen, ob der Raspberry Pi mit der Kommandozeile startet.

Erst wenn auch das nicht mehr geht, dann hat man verloren. Dann muss man ein funktionierendes Image auf die Speicherkarte spielen.

### Firmware-Update ruckgangig machen (Downgrade/Rollback)

Soviel sei gesagt, ein Firmware- und Kernel-Update kann man nicht einfach so ruckgangig machen. Es gibt keine "Undo"-Funktion. Allerdings hat man die Moglichkeit, eine altere und stabile Version der Firmware und des Kernels einzuspielen, sofern das System uberhaupt noch lauft.  
Dazu muss man wissen, auf welche Version man zuruck will. Deshalb schaut man sich zuerst einmal alle Commits an, die ein Kernel-Update liefert.

  * <https://github.com/Hexxeh/rpi-firmware/commits/master>

Doch welcher davon ist der richtige? Am besten schaut man nach "kernel: Bump to {Versionsnummer}". Hier achtet man auf eine Versionsnummer, die mit einer geraden Zahl endet. Die Wahrscheinlichkeit, dass es sich um eine stabile Kernel-Version handelt ist sehr hoch. Wenn das System anschließend stabil lauft kann man mit "apt-get upgrade" auf den aktuellen Stable-Kernel upgraden.

Was wir jetzt noch brauchen ist die vollstandige Commit-Nummer. Das ist eine ewig lange Zahl in der hexadezimalen Schreibweise (0..9A..F). Die bekommt man, wenn man rechts auf die Kurzdarstellung der hexadezimalen Zahl klickt.

Anschließend fuhrt man ein Firmware- und Kernel-Update mit dieser Commit-Nummer durch.
    
    
    sudo rpi-update {Commit-Nummer}

Nach erfolgreichem Kernel-Update ist ein Neustart notwendig.
    
    
    sudo reboot

Viel Gluck!

Sofern verfugbar kann man danach versuchen, per "apt-get upgrade" die neuste lauffahige Firmware- und Kernel-Version einzuspielen.

### Weitere verwandte Themen:

### Produktempfehlungen
