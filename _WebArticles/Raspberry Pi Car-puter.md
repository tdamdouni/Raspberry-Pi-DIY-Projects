# Raspberry Pi Car-puter 

_Captured: 2016-01-11 at 11:33 from [nikrooz.co.uk](http://nikrooz.co.uk/raspberry-pi-car-puter/)_

## The problem

We down-graded but up-sized our car, to a Vauxhall / Opel Zafira. It's only a 2002 model but does come with cruise control, air con and all electric windows, mirrors, etc. However, unlike our old Peugeot 307, it doesn't tell you what you've set the cruise control to. Or, in fact, a very accurate speed reading. And the built-in trip computer only shows one piece of information at a time; you have to scroll all the way round 7 options to get from average MPG to instant, for example.

![Zafira-display](data:image/jpeg;base64,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)

> _The stock display (not mine)_

## The Solution - A Raspberry Pi, of course!

![PiPuter](http://i1.wp.com/www.nikrooz.co.uk/wp-content/upLoads/2013/09/wpid-DSC_1443.jpg?resize=350%2C197)

> _Car Raspberry Pi computer_

I got myself an OBD II bluetooth interface off ebay for about £7\. The OBD port on the Zafira sits just underneath the handbrake lever, and gets you connected to the engine ECU, as well as the ABS and power steering ECUs.

I started experimenting with some android apps to start with. Most of these use the open PIDS available [here on Wikipedia](http://en.wikipedia.org/wiki/OBD-II_PIDs). The Mode 1 PIDS give you a fair amount of information - officially. But on my car, they didn't. I could get RPM, speed and water temperature, but not much else. To replace my OEM display, I'd need at least to get hold of the Miles Per Gallon and as many other readings as I could. So, I found a couple of Opel-specific apps that gave some other bits of information - MAF flow rate, injection fuel quantity, fuel temperature, and lots of other goodies. That's enough to work out MPG! If only I could get my hands on these manufacturer-specific PIDs, I'd be able to get the same readings on my Pi and display them nicely.

#### Hacking the bluetooth comms

At this point I had Xbian running on the R-pi, and had installed a bluetooth dongle and got comms established between the Pi and the scanner. See this page on how TODO!. I tried looking for ways to snoop the serial comms between my android phone and the scanner. Apparently, eavesdropping on bluetooth comms is extremely difficult, since it channel-hops constantly and you won't know which channel it about to hop to unless you were there and on the right channel at the start of the conversation. Suffice to say, a standard £1 bluetooth dongle won't let you eavesdrop on communications.

## The OBD comms

So, how do I find out what to send to my ECU to get the needed telemetry?

#### Strace!

Strace is a linux command that helps you debug processes. Importantly for us, it logs writes to the serial port. So, run it on android as root and it'll tell you what your processes are talking about.

Below is a snippet of what I got back from strace after attaching it to the right process. I had to root my phone, copy in an strace binary, run it as root, and point it to the right Process ID.

If you're familiar with AT commands at all, you may recognize some of the command sent. Either way, the [ELM327 AT commands sheet](http://elmelectronics.com/ELM327/AT_Commands.pdf) has them all listed. Of course, my £7 dongle is not an official ELM327 based device, it's a Chinese copy! But they did keep the AT commands the same for compatibility.

So, here's how one piece of software initializes the bus:

`atz #reset``ete0 #echo off``ATL0 #linefeeds off``ATAL #allow long messages &gt;7``ATSP5 #Set protocol ISO 14230-4 (KWP FAST)``ATH1 #headers on``ATSTFF #timeout big (ST32 is good)``ATSH8111F1 #header 8111F1`

I already know from research that my Bosch EDC15M ECU communicates over KWP, but what's really interesting here is the header, 8111F1. Thanks to a Russian site with an explanation of KWP, I could work out what this header means (see below). The communications continue:

`3E #tester present``1A80 #ECU ID table``1A81``1800FF00 &nbsp; #Mode 18 request for DTCs``3E``82``ATZ``ATSH8128F1 #28 is the ABS``3E``3E``3E``82``ATZ``ATSH8131F1 #31 is the EPS``3E``1A80``1A81``2101``2101``2101`

#### KWP

The KeyWord Protocol, KWP2000 is not very well documented as far as I can find. One amazingly helpful resource was a Russian site with a [document detailing one Russian ECU manufacturer's implementation of KW](http://avto-chiptuning.siteedit.ru/page4)P. Of course, their implementation is not exactly the same as Opel/Vauxhall's, but it gives an insight into ISO 14230, which otherwise is inaccessible to those not willing to pay tens of thousands for access to the standard. It's worth a read - open the page in Chrome if you do want a look, and it'll translate it into English-ish for you.

Here's my notes on it:

Header: Format - Target - Source - [Len]  
Rest of message: Sld Data (63bytes)[255] Checksum

So, the header 81 11 F1 means: Format 81 (Start Comms, as per below) --- TO 11 (as above, 28 refers to the ABS in this car and 31 is the EPS controller) --- FROM F1 (I think this is abritrary, as long as it's no used on the bus)
    
    
    Format name                 Answer (id always 7f; bit 6=1)
    81     startComms           c1
    82     stopComms            c2
    01     readDataByPID
    10     startDiagnosticSess 50
    20     stopDiags           60
    11     ecuReset            51
    12     freezeframeData
    14     clearDTC            54
    18     readDTCs            58
    1A     readECUID           5A
    21     readDatabyLocID     61
    22     readDatabyCommonID + 2 bytes
    23     readMembyAddr       63
    25     StopRepeatedDatatrans
    26     SetDataRate
    27     SecurityAccess
    28     DisableNormComms
    2C     DefineLocalID
    2E     WriteDatabyCommonID
    2F     IOcontrolByCommonID
    30     ioControlByLocID    70
    3B     writeDataByLocID    7B Corresponding to 21
    3E     testerPresent       7E Apparently send this every 2.5s
    GMLAN-specific:
    A2     ReportProgrammingState
    A5     EnterProgramming
    A9     CheckCodes
    AA     ReadDPID
    AE     DeviceControl

So those are the header types, now for the query payload:
    
    
    10 startDiagnosticSess packet can be followed with 81 (diagnostic mode pls) and baud rate (0A, normal:26, high:39, enhanced)
    	To stop send a 20 (should get 60 back. 7F is bad news)
    3E Testerpresent followed by 01 (reponse pls) or 02 (its ok don't reply)
    11 ecuReset followed by 01 for power on
    1A ecuID  followed by 1 byte:
    	80 - complete table. 
    	1A 80 response:
    		5a 80 [3-21]VIN [22-37]ECUhardwareno [38-57]sysSupplierECUSW [58-72]Engine [73-79]repairshopCode [80-89]progDate [90-97]vehManECUID
    		5A		90			91					92						93				94						98			9f
    1A A0 possibly ODO reading?
    1A 90 VIN
    
    14 clearDTC followed by 0000 Pwertrain or FF00 All systems. 54 reply contains same 2 bytes
    
    18 ReadDTCs complicated
    
    21 readDatabylocID:
    	01 - AftersalesServiceRecord (->128b)
    	02 - endOfAssemblyLine (->128)
    	03 - factoryTest (->128)
    	A0 - immobilizerRecord (2)
    	A1 - Body serial No (7)
    	A2 - Engine Serial No (7)
    	A3 - Manufacture date (10)
    		A1 for example gives 61 A1 +7 bytes returned
    	C3 - Possibly TRANS
    	C4 - Aircon request at byte 1
    	D3 - Cruise control switches??
    
    21 A0 Immobilizer record
    21 30 IO control
    21 30 IObelow Param state 
    IOs:
    01	injector1OutputControl	This setting informs the control unit, the tester prompts direct control of the nozzle 1.	I1OC
    02	injector2OutputControl	This setting informs the control unit, the tester prompts direct control nozzle 2.	I2OC
    03	injector3OutputControl	This setting informs the control unit, the tester prompts direct control of the nozzle 3.	I3OC
    04	injector4OutputControl	This setting informs the control unit, the tester prompts direct control nozzle 4.	I4OC
    05	ignition1OutputControl	This setting informs the control unit, the tester prompts direct control of the ignition coil 1 and 4 cylinders.	IGN1OC
    06	ignition2OutputControl	This setting informs the control unit, the tester prompts direct control of the ignition coil 2 and 3 cylinders.	IGN2OC
    09	fuelPumpRelayOutputControl	This setting informs the control unit, the tester prompts direct control of the fuel pump relay.	FPROC
    0A	coolingSytemFanRelayOutputControl	This setting informs the control unit, the tester prompts direct control of the cooling fan relay motor.	CSFROC
    0B	airConditionRelayOutputControl	This setting informs the control unit, the tester prompts direct control relay unit.	ACROC
    0C	malfunctionIndicationLampOutputControl	This setting informs the control unit, the tester prompts direct control of the MIL.	MILOC
    0 D	canisterPurgeValve OutputControl	This setting informs the control unit, the tester prompts direct control canister purge valve.	CPV OC
    41	idleStepMotorPositionAdjustment	This setting informs the control unit, the tester prompts direct position control idle speed regulator.	ISMPA
    42	idleEngineSpeedAdjustment	This setting informs the control unit, the tester prompts direct control idle speed.	IESA
    
    Params: 00 returntoECU. 01 reportState. 02 reportIOconditions. 03 reportIOscaling. 04 resetDefault. 05 freezeCurr. 06 executeControlOption. 07 shortTermAdjust. 08 longTermAdjust. 09 reportIOcalibration
    ---------------
    ---------------
    23 Read mem by address
    23 MemType=0 AddrMSB AddrLSB Memsize
    Response 63 xx xx xx xx
    -----
    3B Write Data by LocID
    90 - VIN
    98 - RepairShopCode
    A1 bodySerNum
    A2 engineSerNum
    A3 manufactDate
    
    Eg. 3B 90 + 19 ASCII chars
    3B 90 xx xx xx xx -> Wait for flow control??? 30 00 00
    Response 7B 90 or 7F 3B errCode
    
    ------------
    27 Security
    27 subFunct
    01	SeedRequest
    02	KeyResponse
    03	SeedAnother
    04	ResponseAnother.....

#### Bored yet?

I won't go on too much more about KWP, suffice to say sending a header 8111F1 and payload 2101 gives the "AftersalesServiceRecord", which contains all the data we need:

2101: 80 F1 11 4C 61 01 00 00 00 00 00 00 00 00 0C 0C 00 00 0B C1 00 00 02 4C 00 00 00 00 03 E3 00 00 00 00 32 C8 03 E7 04 29 03 38 E5 62 00 00 00 00 03 84 00 00 00 00 09 3D 00 00 0C 09 A0 00 01 90 00 00 A9 00 00 20 00 00 01 BD 0C 2F 03 E8 00 02 9D

The response starts 80 F1 11 (Response, TO F1, from 11 (ECU)

Then 4C = Error (OK) code, and:
    
    
    21 01 Responses:
    # 1	Positive response readDataByLocalIdentifier	61	no
    # 2	afterSalesServiceRecordLocalIdentifier	01	no
    # 3	Word of equipment 1	08	no
    # 4	Word of picking 2	35	no
    # 5	The word mode 1	XX	no
    # 6	Word of mode 2	XX	no
    # 7	Memory word current faults 1	XX	no
    # 8	Memory word current faults 2	XX	no
    # 9	Memory word current faults 3	XX		no	
    # 10	Memory word fault current 4	XX	no

Then things get interesting. The following pairs of bytes (WORDs) give all sorts of info: Throttle position, coolant, air and oil temperature, desired & actual RPM, desired & actual boost pressure, EGR pulse ratio, road speed, cruise control set speed, battery voltage, brake pedal position, MAF flow rate, air pressure and others.

#### Which byte is which?

Sorry, I'm not going to tell you that! It took ages of getting sensor readings under different conditions - different temperatures, different load conditions, lots of throttle blipping to figure out which reading is the 'desired' value and which is the 'actual' value for many of the values. Oh, and things like the temperatures being measured in Kelvin instead of degrees (free clue!)

EDIT:

That wasn't very nice, sorry. The info is all in the Github project [XBMC-rpi-service.skin.OBD](https://github.com/anikrooz/XBMC-rpi-service.skin.OBD) and some explanation is in my followup post [here](http://nikrooz.co.uk/raspberry-pi-carputer-2-xbmc-skins/)

[Excel PID working out](http://nikrooz.co.uk/wp-content/upLoads/2015/08/2010-on.xlsx) - This .xlsx file has my workings out of how I figured out which byte of the 2101 response was which. It's not nicely formatted but scroll to the right to see my formulae and adjusted values

[2101-on.txt](http://nikrooz.co.uk/wp-content/upLoads/2013/09/2101-on.txt) has the original values used to create the above spreadsheet

I seem to have lost the original python code used to generate that .txt file, but it's pretty straightforward: I just kept sending 2101 requests after setting the header ATSH8111F1. Once I figured out that the values came in byte pairs, I used excel to translate these to numbers, and a knowledge of how the engine works to figure out which data should trend which way.

## Back to the Pi

#### So, how does the Pi work?

The Raspberry Pi is running the Xbian build of XBMC - it's the fastest by far, and has most bits you'll need pre-installed.

One thing that got missed out for some reason is libtiff. If you get error messages like the below in your logs (/home/xbian/.xbmc/temp/xbmc.log), you'll need to install libtiff4.
    
    
    15:46:20 T:2913350720   DEBUG: Loading: /usr/local/lib/xbmc/system/ImageLib-arm.so
    15:46:20 T:2913350720   ERROR: Unable to load /usr/local/lib/xbmc/system/ImageLib-arm.so, reason: libtiff.so.4: cannot open shared object file: No such file or directory
    15:46:20 T:2837853248   DEBUG: SECTION:LoadDLL(special://xbmcbin/system/ImageLib-arm.so)
    15:46:20 T:2837853248   DEBUG: Loading: /usr/local/lib/xbmc/system/ImageLib-arm.so
    15:46:20 T:2837853248   ERROR: Unable to load /usr/local/lib/xbmc/system/ImageLib-arm.so, reason: libtiff.so.4: cannot open shared object file: No such file or directory
    ^C
    root@AntCar:/home/xbian# apt-get install libtiff4

I did a lot of work on getting the GPIO working in and out straight from the XBMC skin. I'll cover that in a separate post.

#### Bluetooth

Here's what I did to get bluetooth connecting to the ELM327 scanner:

`root@AntCar:``/home/xbian``# apt-get install bluez``root@AntCar:``/home/xbian``# hcitool scan``Scanning ...``00:01:E3:8B:AE:43       Mark``00:01:E3:8E:F4:E9       Ant Dect``00:0D:18:27:FA:E6       Vgate``root@AntCar:``/home/xbian``# cat /etc/bluetooth/rfcomm.conf``#``# RFCOMM configuration file.``#``rfcomm99 {``bind ``yes``;``device 00:0D:18:27:FA:E6;``channel 1;``comment ``"ELM327 based OBD II test tool"``;``}``root@AntCar:~``# cat /etc/udev/rules.d/99-custom.rules ``KERNEL==``"rfcomm99"``, ATTR{address}==``"00:0d:18:27:fa:e6"``, ATTR{channel}==``"1"``, OWNER=``"xbian"``, GROUP=``"dialout"``, SYMLINK+=``"elm327"``cat` `/etc/init``.d``/elm327``#!/bin/bash``DevNum=99       ``# DevNum is depending on the rfcom settings /etc/bluetooth/rfcom.cfg``case` `$1 ``in``start)``rfcomm bind $DevNum``;;``stop)``rfcomm release $DevNum``;;``status)``rfcomm show $DevNum``;;``*)``cat``&amp;lt;`

And some testing:
    
    
    apt-get install python-serial
    
    screen /dev/rfcomm99 38400
    
    python to start Python.
    import serial
    ser = serial.Serial('/dev/rfcomm99', 38400, timeout=1)
    Nser.write("01 0D \r")
    speed_hex = ser.readline().split(' ')
    speed = float(int('0x'+speed_hex[3], 0 ))
    print 'Speed: ', speed, 'km/h'
    
    
    

See my [followup post](http://nikrooz.co.uk/raspberry-pi-carputer-2/) for more info and links to github projects
