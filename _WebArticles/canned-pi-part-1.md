# CANned Pi: (Part1)

_Captured: 2017-05-11 at 22:44 from [www.cowfishstudios.com](http://www.cowfishstudios.com/blog/canned-pi-part1)_

In this tutorial you will learn how to gain access to a vehicle's internal network using a Raspberry Pi and CAN-Bus Board!

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/6115565_orig.jpg)

## **_Hardware Required:_**  


![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/4354074_orig.jpg)

## **_Introduction to CAN (Controller Area Network)_**  


At its simplest level CAN (Controller Area Network) can be thought of as a means of linking all of the electronic systems within a car together to allow them to communicate with each other.

The CAN (Controller Area Network) network protocol was developed by Robert Bosch GmbH initially for vehicle systems, but is used in many different fields, the bulk of which are:

  * Machine Control
  * Medical Equipment and devices
  * Factory Automation
  * And more….  


## _**CAN Topology**_  


The CAN bus is commonly implemented using two twisted differential wires, CAN high and CAN low, with two termination resistors of 120 ohm each. The bus has a maximum signaling rate of 1 Mbps with a bus length of 40 m with a maximum of 30 nodes.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/7081046_orig.png)

## _**OSI Model for CAN**_  


You may recall learning about the OSI Model (Open Systems Interconnection model) in one of your engineering classes. The OSI Model is a theoretical, seven-layered model of how networks work.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/326569.png?572)

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/5714255.png?572)

The Physical Layer defines the physical transmission of a frame between two nodes. It also standardizes the bus electrical characteristics.

The Data Link Layer allows all modules to transmit and receive data on the bus.

The Data Link Layer is also subdivided into two layers: Medium Access Control and Logical Link Control.

The LLC (Logical Link Control) layer will accept messages by the filtering process, overloading notification and recovery management tasks will be taken care of this layer.

The MAC (Medium Access Control) layer will do the data encapsulation; frame coding, media access management, error detection, signaling and acknowledgment tasks.

The model below explains the transfer of data between two nodes.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/4860939_orig.png)

The Physical Layer ensures the physical connection between the nodes in the network. The Data Link Layer contains frames and information to identify the frames and errors. It also has information to determine the bus access.

## _**Types of CAN**_  


There are two types of CAN implementations depending in the size of the identifier field.

  1. STANDARD: 11-bit wide identifier field  

  2. EXTENDED: 29-bit wide identifier field
![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/8786236_orig.png)

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/7145005_orig.jpg)

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/960772_orig.png)

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/660065_orig.jpg)

## _**How is OBD-II related to CAN?**_  


As you learned in the previous [tutorial](http://www.cowfishstudios.com/blog/obd-pi-raspberry-pi-displaying-car-diagnostics-obd-ii-data-on-an-aftermarket-head-unit) OBD stands for On-Board Diagnostics, and this standard connector has been mandated in the US since 1996. Now you can think of OBD-II as an on-board computer system that is responsible for monitoring your vehicle's engine, transmission, and emissions control components.

Vehicles that comply with the OBD-II standards will have a data connector within about two feet of the steering wheel. The OBD connector is officially called a SAE J1962 Diagnostic Connector, but is also known by DLC, OBD Port, or OBD connector. OBD-II defines a 16-bit connector, and looks like this.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/1447573_orig.png)

There are five different protocols defined on the OBD-II connector, we are only going to focus on ISO 15765, which is CAN for vehicles. All vehicles 2008 and up support CAN.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/7726237_orig.png)

Pin 6 and 14 will be our ticket into the world of CAN!

## _**SocketCAN?**_  


The [socketcan](https://www.kernel.org/doc/Documentation/networking/can.txt) package is an implementation of CAN protocols (Controller Area Network) for Linux. While there have been other CAN implementations for Linux based on character devices, SocketCAN uses the Berkeley socket API, the Linux network stack and implements the CAN device drivers as network interfaces. The CAN socket API has been designed as similar as possible to the TCP/IP protocols to allow programmers, familiar with network programming, to easily learn how to use CAN sockets.

## _**Hardware Setup**_  


The hardware setup is quite simple.

1\. Take your 20 gauge wire and cut it into two pieces. Strip both ends of the wire about 1/4" from the end.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/2229438.jpg?396)

NOTE: The wire length will vary depending on where you would like your Raspberry Pi to sit in the vehicle.

2\. Your OBD-II Connector Shell will come with four pins, we will only be utilizing two (CAN_L & CAN_H). Crimp a pin on one side of each wire. Locate Slot 6 and 14 on your OBD-II connector shell and insert the two pins.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/4804680.jpg?508)

3\. Locate the screw terminal on your PICAN board. The wire from Slot 6 will connect to the CAN_H terminal. The wire from Slot 14 will connect to the CAN_L terminal.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/5122362.jpg?403)

## _**Software Installation**_  


Before you start you will need a fresh install of [Raspbian 3.12.28+](http://downloads.raspberrypi.org/raspbian/images/raspbian-2014-09-12/) with network access.

We'll be doing this from a console cable connection, but you can just as easily do it from the direct HDMI/TV console or by SSH'ing in. Whatever gets you to a shell will work!

Note: For the following command line instructions, do not type the '$', that is only to indicate that it is a command to enter.

Before proceeding, run:

Note: Please login as root when entering the rest of the commands.

First, copy the tar archive to your Raspberry Pi:

# /etc/modules: kernel modules to load at boot time.  
#  
# This file contains the names of kernel modules that should be loaded  
# at boot time, one per line. Lines beginning with "#" are ignored.  
# Parameters can be specified after the module name.

snd-bcm2835  
spi_bcm2708

# MCP2515 configuration for PICAN module  
spi-config devices=\  
bus=0:cs=0:modalias=mcp2515:speed=10000000:gpioirq=25:pd=20:pds32-0=16000000:pdu32-4=0x2002:force_release

# load the module  
mcp251x

## _**Device Configuration**_  


Now its time to connect your Raspberry Pi to the OBD-II port and begin to dump some data!

First, we need to configure the device and determine the bitrate. The [bitrate](http://www.techterms.com/definition/bitrate) describes the rate at which bits are transferred from one location to another.

How do you figure out the vehicles target bus bitrate? The simplest way is to guess (unless you have an oscilloscope).

The most common ones are 33,333 bps, 50 Kbps, 83,333 bps, 100 Kbps, 125 Kbps, 250 Kbps, 500 Kbps, 800 Kpbs, and 1,000 Kbps.

The standard command to configure a CAN bus interface is:

Now its time to bring up the interface and start dumping frames:

pi@raspberrypi:~$ candump -cae any,0:0,#FFFFFFFF  
can0 120 [8] 00 00 00 00 10 10 04 4D '........'  
can0 038 [8] C0 00 08 00 00 00 00 07 'P.......'  
can0 244 [8] 10 00 00 00 00 00 00 5E '@.......'  
can0 3C9 [8] 03 FF 21 02 A7 03 31 D4 '.....m..'  
can0 4C7 [8] 08 00 01 00 00 00 00 00 '........'  
can0 442 [8] 00 2D 00 34 77 77 77 F3 '........'  
can0 321 [8] 01 F8 01 F8 00 00 00 1C '........'  
can0 453 [8] 42 01 00 00 00 00 00 00 '........'  
can0 433 [8] 20 00 30 00 00 40 00 80 '...@....'  
can0 448 [8] 30 02 40 00 00 00 00 00 '@.......'  
...

Note: If you receive an error bring the interface down, and try a different bitrate.

## _socketCAN Tools_  


Now that you are up and running let's take some time to understand the frame format and learn in more detail about the tools provided by socketCAN.

At this point you are probably wondering how the frames are formatted? The figure below will give you a better understanding.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/854449_orig.png)

Next let's discuss candump. The candump command dumps traffic on a CAN network.

The following commandcandump -cae any,0:0,#FFFFFFFF (which you entered earlier) is showing you everything that is happening on the bus, including errors.

candump also has the ability to dump data with a specific ID (identifier), here is an example for 0x3cd:

pi@raspberrypi:~$ candump -cae can0,3cd:7ff  
can0 3CD [5] 00 00 00 DD B2 '........'  
can0 3CD [5] 00 00 00 DD B2 '........'  
can0 3CD [5] 00 00 00 DD B2 '........'  
can0 3CD [5] 00 00 00 DD B2 '........'  
can0 3CD [5] 00 00 00 DD B2 '........'  
...

Another useful feature is the ability to save all the received packets for offline analysis.

This is the command to save all the received packets into a logged file:

$ head -n5 candump-2014-09-21_204243.log  
(1411332163.747563) can0 038#C0000800000007  
(1411332163.747683) can0 244#100000000000005E  
(1411332163.748935) can0 039#35020F83  
(1411332163.749096) can0 262#00010069  
(1411332163.749638) can0 030#84000000002000DC

Note: The head command reads the first few lines of any text given to it as an input and writes them to standard output.

socketCAN also have the ability to replay the logged file on a virtual interface for realtime analysis. This will be extremely helpful when we begin to reverse engineer CAN bus frames.

Enter the following commands to bring up the virtual interface:

Next, run canplayer which will feed in the original dump:

If successful you should see packets flowing with the same timing of the original recording.

The final command we will learn is cansniffer. This will group the messages by ID's (identifiers).This is also a great tool to get an overview of the traffic.

Run:

/ time __ID data ... < cansniffer can0 # l=2 h=10 t=50 >  
0.205252 22 01 F8 01 F8 00 00 00 1C '........'  
0.157026 23 02 01 01 FF 00 00 2D 12 '........'  
0.205252 25 00 2D 00 34 77 77 77 F3 '........'

Note: Try opening a door or turning on a light. See what happens!

Please stay tuned for part 2 of the series. The second part of this tutorial will cover reverse engineering of CAN bus frames and show you how to write a test application using C programing to print the frames/data gathered in a readable format.
