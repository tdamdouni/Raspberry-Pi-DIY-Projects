# Raspberry Pi: SPI-Schnittstelle

_Captured: 2017-05-19 at 11:14 from [www.netzmafia.de](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_SPI.html)_

## Grundlagen

Der Raspberry Pi kann uber den digitalen GPIO-Port nicht nur per I2C, UART oder bitweise kommunizieren, sondern hat auch eine SPI-Schnittstelle. Beim Modell B/B+ und folgende sind die SPI-Pins auf der GPIO-Steckerleiste uber folgende Pins erreichbar:
    
    
    SPI MOSI – PIN 19, GPIO 10
    SPI MISO – PIN 21, GPIO 9
    SPI SCLK – PIN 23, GPIO 11
    SPI CS0  – PIN 24, GPIO 8
    SPI CS1  – PIN 26, GPIO 7
    

Das Serial Peripheral Interface (kurz SPI, oder SPI-Bus) ist ein synchrones Datenbus-System, das von Motorola (heute Freescale) entwickelt wurde, und mit dem digitale Schaltungen nach dem Master-Slave-Prinzip miteinander kommunizieren konnen. Der Bus wird fur kurze Distanzen verwendet und arbeitet prinzipiell wie ein Schieberegister. Er hat vier logische Signale:

  * SCLK : Serial Clock (output from master). 
  * MOSI : Master Output, Slave Input (DO, output from master). 
  * MISO : Master Input, Slave Output (DI, output from slave). 
  * CS : Chip Select (active low, output from master). 

Der Mikrocontroller unterstutzt intern drei Chip-Select-Leitungen, es sind aber nur zwei (CS0, CS1) auf die Steckerleiste herausgefuhrt. Es lassen sich also direkt uber den Treiber nur zwei Gerate ansprechen. Manuell konnte man aber auch andere GPIO-Pins fur das CS-Signal weiterer SPI-Devices generieren, nur das muss dan auch im Programm "von Hand" erledigt werden.

![](http://www.netzmafia.de/skripten/hardware/RasPi/SPI-Schema.gif)

Die Datenubertragung erfolgt zwischen den beiden Busteilnehmern also seriell und synchron uber die Leitungen MISO und MOSI, wobei der Master die Kommunikation steuert und den Takt uber SCLK-Leitung (Serial-Clock) vorgibt.

Der Zugriff im Betriebssystem Raspbian erfolgt uber die Geratedateien /dev/spidev0.0 (Gerat an CS0) und /dev/spidev0.1 (Gerat an CS1), in die man direkt schreiben und aus denen man auch direkt lesen kann. Das Freischalten der Treiber wurde schon in der [Installationsanleitung](http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_Install.html) vorgenommen und ist dort beschrieben. Mit dem Befehl sudo modprobe spi-bcm2708 konnen Sie uberprufen, ob das Treibermodul geladen wurde.

Ab Kernelversion 3.18 ist der Eintrag dtparam=spi=on in der Datei /boot/config.txt notwendig. Die Zeile kann mit raspi-config eingetragen werden. Ausserdem scheint es einen neueren Treiber zu geben, spi_bcm2835 statt des spi_bcm2708. Sie konnen das einfach ausprobieren, indem Sie den Treiber manuell laden. Wenn es beim spi_bcm2708 schief geht, nemen Sie den spi_bcm2835:
    
    
    modprobe spi_bcm2708
    modprobe: ERROR: could not insert 'spi_bcm2708': No such device
    modprobe spi_bcm2835
    

Der Treiber unterstutzt folgende Geschwindigkeiten:
    
    
      cdiv     speed          cdiv     speed
        2    125.0 MHz          4     62.5 MHz
        8     31.2 MHz         16     15.6 MHz
       32      7.8 MHz         64      3.9 MHz
      128     1953 kHz        256      976 kHz
      512      488 kHz       1024      244 kHz
     2048      122 kHz       4096       61 kHz
     8192     30.5 kHz      16384     15.2 kHz
    32768     7629 Hz
    

Es werden folgende Modi unterstutzt (Mode bits):

  * SPI_CPOL - Clock polarity 
  * SPI_CPHA - Clock phase 
  * SPI_CS_HIGH - Chip Select active high 
  * SPI_NO_CS - 1 dev/bus, no chipselect 

Fur die Datenubertragung konnen 8-Bit-Worte (Normalfall) oder auch 9-Bit-Worte bei LoSSI-Modus) verwendet werden.

Fur eine ersten Test konnen Sie den Loopbacktest verwenden. Dazu werden die Pins MOSI und MISO miteinadner verbunden. Laden Sie sich die aktuelle Version des Testprogramms auf den Raspberry und compilieren Sie es:
    
    
    wget https://raw.githubusercontent.com/torvalds/linux/master/tools/spi/spidev_test.c
    gcc -o spidev_test spidev_test.c
    

Danach starten Sie das Programm
    
    
    ./spidev_test -D /dev/spidev0.0
    

Das Programm bietet zahlreiche Kommandozeilenoptionen:
    
    
      -D --device   device to use (default /dev/spidev1.1)
      -s --speed    max speed (Hz)
      -d --delay    delay (usec)
      -b --bpw      bits per word 
      -l --loop     loopback
      -H --cpha     clock phase
      -O --cpol     clock polarity
      -L --lsb      least significant bit first
      -C --cs-high  chip select active high
      -3 --3wire    SI/SO signals shared
      -v --verbose  Verbose (show tx buffer)
      -p            Send data (z.B. 1234\xde\xad)
      -N --no-cs    no chip select
      -R --ready    slave pulls low to pause
      -2 --dual     dual transfer
      -4 --quad     quad transfer);
    

Das Senden von Daten an die Schnittstell funktioniert auch auf der Kommandozeile z. B.:
    
    
    echo -ne "\x01\x02\x03" > /dev/spidev0.0
    

Das gleiche Programm finden Sie auch unter der Adresse .

Es gibt vier verschiedene SPI-Modes fur den Takt, der Raspi benutzt nur Mode 0,0, was bedeutet:

  * CLK = Low im Ruhezustand 
  * Übernahme der Datenbits mit der positiven Flanke 
  * Die Default-Taktfrequenz des RasPi betragt 500 kHz 

Das Senden und Empfangen geschieht immer gleichzeitig, bei jedem Takt wird ein Bit vom MOSI des Masters versendet und uber MISO ein Bit des Slaves empfangen. Schickt also der Master ein Kommando an den Slave, erhalt er die Antwort auf die vorherige Anforderung.

Sie konnen aber auch dauerhaft dafur sorgen, dass die Zugriffsrechte beim Bootvorgang von System festgelegt werden. Hier stutzt man sich auf das udev-Subsystem. Normalerweise erstellt es fur jedes neue Gerat eine Geratedatei im Verzeichnis /dev. Man kann aber auch weitere Regeln angeben, indem man im Verzeichnis /etc/udev/rules.d eine Steuerdatei anlegt. Der numerische Prafix des Dateinamens regelt dabei die Reihenfolge der Abarbeitung der Dateien. Fur SPI legen Sie im o. g. Verzeichnis die Datei 51-i2c.rules an und tragen darin die folgende Regel ein:
    
    
    SUBSYSTEM=="spidev", GROUP="users", MODE="0660"
    

Damit sind die entsprechenden Devices fur die Gruppe "users" mit Lese- und Schreibrecht versehen. Jetzt mussen Sie nur noch den udev-Daemon von den Änderungen wissen lassen (beim nachsten Reboot passiert das dann automatisch):
    
    
    sudo service udev restart
    

### Programmierung mit C

Wenn Sie den SPI-Bus in C ansprechen wollen, brauchen Sie auf jeden Fall die folgenden Headerdateien:
    
    
    #include <fcntl.h>                // Needed for SPI port
    #include <sys/ioctl.h>            // Needed for SPI port
    #include <linux/spi/spidev.h>     // Needed for SPI port
    

Der Zugriff unter C hat recht klassische Programmierweise. Nach dem Öffnen des Devices werden die Parameter eingestellt und danach ist das System bereit fur den Datentransfer. Bei dem folgenden Programmfragment wird neben dem Setzen der Parameter auch gezeigt, wie man die Parameter wieder abfragen kann:
    
    
    static const char *device = "/dev/spidev0.0";
    static uint8_t mode;
    static uint8_t bits = 8;
    static uint32_t speed = 500000;
    static uint16_t delay;
    int ret, fd;
    
    /* Device oeffen */
    if ((fd = open(device, O_RDWR)) < 0)
      {
      perror("Fehler Open Device");
      exit(1);
      }
    /* Mode setzen */
    ret = ioctl(fd, SPI_IOC_WR_MODE, &mode);
    if (ret < 0)
      {
      perror("Fehler Set SPI-Modus");
      exit(1);
      }
    
    /* Mode abfragen */
    ret = ioctl(fd, SPI_IOC_RD_MODE, &mode);
    if (ret < 0)
      {
      perror("Fehler Get SPI-Modus");
      exit(1);
      }
    
    /* Wortlaenge setzen */
    ret = ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, &bits);
    if (ret < 0)
      {
      perror("Fehler Set Wortlaenge");
      exit(1);
      }
    
    /* Wortlaenge abfragen */
    ret = ioctl(fd, SPI_IOC_RD_BITS_PER_WORD, &bits);
    if (ret < 0)
      {
      perror("Fehler Get Wortlaenge");
      exit(1);
      }
    
    /* Datenrate setzen */
    ret = ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, &speed);
    if (ret < 0)
      {
      perror("Fehler Set Speed");
      exit(1);
      }
       
    /* Datenrate abfragen */
    ret = ioctl(fd, SPI_IOC_RD_MAX_SPEED_HZ, &speed);
    if (ret < 0)
      {
      perror("Fehler Get Speed");
      exit(1);
      }
    
    /* Kontrollausgabe */
    printf("SPI-Device.....: %s\n", device);
    printf("SPI-Mode.......: %d\n", mode);
    printf("Wortlaenge.....: %d\n", bits);
    printf("Geschwindigkeit: %d Hz (%d kHz)\n", speed, speed/1000);
    

Fur das Schreiben und gleichzeitige Lesen von Daten reicht eine einzige Funktion. Der Puffer-Parameter data enthalt die zu sendenden Daten und er wird mit den Empfangsdaten uberschrieben. Er verhalt sich damit wie in an MOSI und MISO angeschlossenes Schieberegister.
    
    
    int SpiWriteRead (int fd, unsigned char *data, int length)
    /* Schreiben und Lesen auf SPI. Parameter:
     * fd        Devicehandle
     * data      Puffer mit Sendedaten, wird mit Empfangsdaten überschrieben
     * length    Länge des Puffers
    */
    
      {
    	struct spi_ioc_transfer spi[length]; /* Bibliotheksstruktur fuer Schreiben/Lesen */
      uint8_t bits = 8;                    /* Datenlaenge */
      uint32_t speed = 500000;             /* Datenrate */
    	int i, ret;                          /* Zaehler, Returnwert */
    
      /* Wortlaenge abfragen */
      ret = ioctl(fd, SPI_IOC_RD_BITS_PER_WORD, &bits);
      if (ret < 0)
        {
        perror("Fehler Get Wortlaenge");
        exit(1);
        }
    
      /* Datenrate abfragen */
      ret = ioctl(fd, SPI_IOC_RD_MAX_SPEED_HZ, &speed);
      if (ret < 0)
        {
        perror("Fehler Get Speed");
        exit(1);
        }
    
      /* Daten uebergeben */
    	for (i = 0; i < length; i++)
    	  {
    		spi[i].tx_buf        = (unsigned long)(data + i); // transmit from "data"
    		spi[i].rx_buf        = (unsigned long)(data + i); // receive into "data"
    		spi[i].len           = sizeof(*(data + i));
    		spi[i].delay_usecs   = 0;
    		spi[i].speed_hz      = speed;
    		spi[i].bits_per_word = bits;
    		spi[i].cs_change     = 0;
    	  }
    
    	ret = ioctl(fd, SPI_IOC_MESSAGE(length), &spi) ;
    	if(ret < 0)
        {
    		perror("Fehler beim Senden/Empfangen - ioctl");
    		exit(1);
        }
    	return ret;
      }
    

Die andernorts schon besprochene Bibliothek WiringPi bietet zur Losung der meisten Probleme, die sich beim Öffnen von SPI-Geraten und dem Senden und Empfangen von Bytes ergeben. Der Code der Bibliothek ist recht ubersichtlich und so sollten Sie in der Lage, diesen als Grundlage fur Ihren eigenen Code verwenden.

Das folgende Beispiel zeigt exemplarisch das Auslesen eines 3-Achsen-Beschleunigungssensors ADXL 362 mit der Bibliothek. Der anfangliche Vorspann setzt wieder die Busparameter (in diesem Fall alle auf den Default). Danach erfolgen dann erst die Initialisierung des Sensors und dann das Auslesen der Daten. Die gesendeten Befehle muss man sich aus dem [Datenblatt](http://www.netzmafia.de/skripten/hardware/RasPi/ADXL362.pdf) herausfischen. Je nach Sensor oder Device ist hier oftmals Versuch und Irrtum angesagt, bis man zu Ziel gelangt.
    
    
    #include <bcm2835.h>
    #include <stdio.h>
    /* ggf. weiter includes */
    
    int main(int argc, char **argv)
      {
      char buf [10];
    
      if (!bcm2835_init()) return 1;   /* Bibliothek initialisieren */
        
      /* Schnittstenneparameter setzen */
      bcm2835_spi_begin();
      bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);      /* default */
      bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);                   /* default */
      bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_65536); /* default */
      bcm2835_spi_chipSelect(BCM2835_SPI_CS0);                      /* default */
      bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW);      /* default */
    
      /* Device-ID abfragen */
      buf[0] = 0x0B; buf[1] = 0x00; buf[2] = 0x00;
      bcm2835_spi_transfern(buf, 3);
      /* buf enthaelt die gelesenen Daten */
      printf("Device ID: %02X \n", buf[2]);
        
      /* Soft-Reset des Sensors */
      buf[0] = 0x0A; buf[1] = 0x1F; buf[2] = 0x52;
      bcm2835_spi_transfern(buf, 3);
      delay(1000);
    
      /* Setup for Measure */
      buf[0] = 0x0A; buf[1] = 0x2D; buf[2] = 0x02;
      bcm2835_spi_transfern(buf, 3);
      delay(1000);
    
      /* X-Achse auslesen */
      buf[0] = 0x0B; buf[1] = 0x0E; buf[2] = 0x00; buf[3] = 0x00;
      bcm2835_spi_transfern(buf, 4);
      printf("X-Achse: %02X %02X \n", buf[3], buf[2]);
      delay(1000);
      bcm2835_spi_end();
      return 0;
      }
    

### Programmierung mit Python

Auch wenn Python schon standardmaßig in der Raspbian-Distribution installiert ist, wird SPI leider noch nicht gleich mit unterstutzt. Man also den passenden die SPI-Library fur Python nachinstallieren. Inzwischen gibt es da auch zwei Wege. Wenn man wirklich nur die eine Bibliothek braucht, fuhrt man im Terminal folgendes aus:
    
    
    sudo su
    apt-get install python-dev
    mkdir python-spi
    cd python-spi
    wget https://github.com/JoBergs/RaspiContent/raw/master/spidev/setup.py
    wget https://github.com/JoBergs/RaspiContent/raw/master/spidev/spidev_module.c
    python setup.py install
    

Wenn Sie aber schon wissenn, dass Sie ofter mit Python arbeiten werden und auch sicher ofter mal etwas nachinstallieren mussen, ist es gunstiger, sich den Installer fur Python-Software einmal zu installieren. Das Laden und Installieren von Bibliotheken etc. ist damit dann wesentlich einfacher, denn erledigt das Herunterladen und Installieren in einem Aufwasch:
    
    
    sudo su
    apt-get install git-core python-dev
    apt-get install python-pip
    pip install spidev
    

Zum Testen, ob alles geklappt hat, kann man nun Python mit Root-Rechten starten ( und interaktiv die Spidev-Library testen:
    
    
    import spidev
    

Wenn eine Fehlermeldung kommt, sollten Sie auf prufen, ob der Treiber freigegeben ist (). Die Geratedateien listet das Kommando . Damit kann man prufen, ob zwei SPI-Gerate gefunden werden (je eines pro CS-Signal). Es sollte sich also ergeben:
    
    
    /dev/spidev0.0
    /dev/spidev0.1
    

Das folgente Demoprogramm offnet die SPI-Schnittstelle und schreibt zehn mal pro Sekunde ein byte (0xAA): import spidev import time spi = spidev.SpiDev() # create spi object spi.open(0, 1) # open spi port 0, device (CS) 1 try: while True: resp = spi.xfer2([0xAA]) # transfer one byte time.sleep(0.1) # sleep for 0.1 seconds #end while except KeyboardInterrupt: # Ctrl+C pressed spi.close() # close the port before exit #end try

#### Liste der Spidev-Properties

PropertyFunktion

bits_per_word
Setzen/Lesen der Wortlange (8..16)

cshigh
Lesen/Setzen CS auf active high

lsbfirst
Lesen ob das LSB zuerst oder zuletzt gesendet wird

max_speed_hz
Lesen/Setze Datenrate

mode
Lesen/Setzen des SPI-Mode (Taktpolaritat CPOL, Phase CPHA) (0b00..0b11)

threewire
Lesen/Setzen "I/SO signals shared" -> nur eine Datenleitung (nur bei manchen Devices moglich)

#### Liste der Spidev-Methoden

MethodeFunktion

spi.open(0,0)
Öffnet den SPI-Bus 0 mit CS0

spi.open(0,1)
Öffnet den SPI-Bus 0 mit CS1

spi.close()
Schliesst den SPI-Bus

spi.readbytes(len)
Liest len Bytes vom SPI-Slave

spi.writebytes([array of bytes])
Sendet ein Byte-Array zum SPI-Slave

spi.xfer([array of bytes])
Sendet ein Byte-Array, CEx wird vor jedem Byte aktiv und dann wieder inaktiv

spi.xfer2([array of bytes])
Sendet ein Byte-Array, dabei bleibt CEx dauerhaft aktiv

Als Beispiel soll der Port-Expander MCP23S17 dienen, der unter anderem zwei 8-Bit-Ports bietet. Das IC wird per SPI an RasPi angeschlossen und ist recht einfach zu programmieren. Gegebenefalls hilft ein Blick ins [Datenblatt](http://www.netzmafia.de/skripten/hardware/RasPi/MCP23S17.pdf) weiter:
    
    
    #!/usr/bin/python
    import spidev
    import time
    
    spi = spidev.SpiDev()
    spi.open(0,0)
    
    while True:
      spi.xfer([0,0,0])      # turn all LEDs off
      time.sleep(1)
      spi.xfer([1,255,255])  # turn all LEDs on
      time.sleep(1)
    # end while
    

Neben dem Portexpander ist wohl der [A/D-Wandler MCP3008](http://www.netzmafia.de/skripten/hardware/RasPi/MCP3004_3008.pdf) einer der beliebtesten SPI-Bausteine. Der Raspberry Pi hat von Haus aus keine analogen Ein- und Ausgange. Der MCP3008 wandelt analoge Spannungen an seinen acht Eingangen in binare Daten um und ubertragt sie per SPI zum Raspberry Pi. Der MCP3008 hat eine Auflosung von 10 Bit. Die zu messende, analoge Spannung wird in 1024 Schritte unterteilt. Die kleinstmogliche Einheit errechnet sich damit zu _Step = VRef/1024_. Bei einer Referenzspannung von 3,3 V ergibt sich: _Step = 3,3/1024 = 0,003222_, also ca. 3,22 mV. Das folgende Bild zeigt die Konfigurationsbits zum Ansprechen der einzelnen Kanale und den Ablauf der Kommunikation:

![](http://www.netzmafia.de/skripten/hardware/RasPi/mcp3008_conf.gif)

Dazu ein Beispiel fur Kanal 0. Zuerst muss das CS-Signal auf Low gezogen werden um den Chip anzusprechen, was die Methoden xfer() oder xfer2() automatisch erledigen. Nun senden wir zuerst das Startbit (1) und anschliessend das SGL/DIFF Bit (1). Die nachsten drei Bits bestimmen den Kanal (0 0 0). Alle darauffolgend gesendeten Bits sind "don't care". Zuletzt muss ein Dummybyte (0x00) gesendet werden. Daraus ergibt sich der folgende Python-Aufruf: spi.xfer([0x01, 0x80,0x00]) . Ein komplettes Python-Programm konnte folgendermassen aussehen:
    
    
    #!/usr/bin/python
    
    import spidev
    import time
    
    spi = spidev.SpiDev()
    spi.open(0,1)
    
    while True:
      antwort = spi.xfer([1,128,0])
      time.sleep(0.01)               # Wandlung abwarten
      wert = ((antwort[1] * 256) + antwort[2]) * 0.00322
      print wert ," V"
      time.sleep(1)
    # end while
    

Durch die Muliplikation mit 0.00322 wird der Dezimalwert in die ensprechende Spannung umgerechnet.

Das folgende Bild zeigt den "kleine Bruder", den MCP3004 mit nur vier Eingangen als komplette Schaltung. Ausgangsseitig ist das IC direkt mit dem SPI-Interface des Raspberry verbunden. Die Schaltung kann man gut auf einer Lochrasterplatine aufbauen. Der MCP3004 arbeitet mit 3,3 V.

![](http://www.netzmafia.de/skripten/hardware/RasPi/mcp3004.gif)

Man darf nur keine zu großen Spannungen anschließen. Deshalb sind an allen vier Eingangen Spannungsteiler vorgesehen, mit denen das Eingangssignal abgeschwacht werden kann. versehen. Bei Kanal 1 sind dies R1 und R2. Das Eingangssignal wird daher abgeschwacht: _Vout = R2/(R1 +R2) * Vin_. Fur einen Messbereich von 0 bis 5 V nehmen Sie R1 = R2 = 10 kΩ. Das ergibt dann eine Spannung am ADC-Eingang von 0 bis 2,5 V. Fur einen Messbereich von 0 bis 10 V konnen Sie R1 = 10 kΩ und R2 = 22 kΩ, was am ADC-Eingang maximal 3,125 V ergibt. Fur einen Messbereich von 0 bis 3,3 V nehmen Sie fur R1 = 1 kΩ, R2 entfallt. Um Signalstorungen zu reduzieren, konnen Sie noch je einen kleinen Kondensator von 1 bis 10 nF fur C1 bis C4 bestucken. Wer ganz sicher sein will, dass dem IC nichts geschieht, kann fur ZD1 bis ZD4 noch Z-Dioden mit einer Nennspannung von 3,6 V als Überspannungsschutz bestucken.

Das Programm zum Auslesen ist kurz und ubersichtlich. Da der Wandler 10 Bit Auflosung hat, werden zwei Bytes gelesen, wobei vom MSB nur die unteren zwei Bit verwendet werden. Der Wert setzt sich dann zusammen, indem das MSB mit 3 und-verknupft und mit 256 multipliziert [(rcv[1] & 3) << 8] und dazu das LSB addiert wird. Das Beispiel zeigt das Lesen von Kanal 1, bei den anderen Kanalen funktioniert es auf die gleiche Weise.
    
    
    #!/usr/bin/python
    import spidev
    import time
    
    # SPI-Instance erzeugen und den Bus oeffen
    spi = spidev.SpiDev()
    spi.open(0,0)
    
    # Einleseschleife
    while True:
      # Lese ADC-Kanal 1
      rcv = spi.xfer2 ([1, 8 << 4, 0])
      adcval = ((rcv[1] & 3) << 8) + rcv[2]
      # Wert ausgeben 
      Print "ADC = ", adcval
      # etwas warten
      time.sleep(1)
    # Ende Schleife
    

Wenn Sie sehen wollen, wie die Bausteine ohne Spilib angesprochen werden konne, sehen Sie sich die beiden folgenden Links mal an:

  * [ Der Port-Expander MCP23S17](http://erik-bartmann.de/component/attachments/download/23.html)
  * [ Der A/D-Wandler MCP3008](http://erik-bartmann.de/component/attachments/download/21.html)

_Copyright (C) Hochschule Munchen, FK 04, Prof. Jurgen Plate_
