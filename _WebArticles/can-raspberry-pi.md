# CAN + Raspberry Pi

_Captured: 2017-05-11 at 22:05 from [lnxpps.de](http://lnxpps.de/rpie/)_

If you are searching for a cheap, fast and reliable CAN interface with Ethernet connection consider using [CAN-CAN Interface](http://lnxpps.de/openwrt/wr841/indexe.html)  
or the [Banana Pi with integrated CAN-Controller](http://lnxpps.de/bpie/index.html) Please have a look at [Raspberry Forum](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=44&t=7027&start=284)

## Summary

Efforts connecting a MCP2515 CAN controller to Raspberry Pi. Please note: This is not ment to be a description for Linux beginners.  
The combination of RPi and MCP2515 isn't perfect - you need some time to get a reliable setup working.

## Wiring
    
    
    P1-01 3V3    -> MCP2515 VCC
    P1-02 5V     -> MCP2551 VCC
    P1-06 GND    -> MCP25xx GND
    P1-19 GPIO10 -> MOSI
    P1-21 GPIO9  -> MISO
    P1-22 GPIO25 -> MCP2515 INT
    P1-23 GPIO11 -> SCK
    P1-24 GPIO8  -> CS0
    

![](http://lnxpps.de/rpie/rpi_mcp2515.png)

Rasperry Pi GPIOs use 3V3 as the MCP2515 does. The tranceiver uses 5V - the R1/R2 combination is a voltage divider.

## Improved Design

I've seen commercial products based on the schematic above. Strange, because these days you should use a MCP2562 instead of the (not recommend for new designs) MCP2551. The MCP2562 can operate with two supply voltages (e.g. 3V3 IO / 5V CANBUS) which avoids the two resistors R1/R2 and is more reliable. Here the new design:

![](http://lnxpps.de/rpie/RPi-MCP2515_new.png)

If you want to try this design: [ +-10 PCBs from Dirtypcbs.com](http://dirtypcbs.com/store/designer/details/GBert/1553/rpi-mcp2515-v1-0-zip)

![](http://dirtypcbs.com/files/thumb/500x400/aolg/top.png)

## CAN test

Make sure that you have all necessary modules installed #
    
    
    spi-bcm2708
    can
    can-dev
    can-raw
    mcp251x
    
    # Maerklin Gleisbox (60112 and 60113) uses 250000
    # loopback mode for testing
    ip link set can0 up type can bitrate 125000 loopback on
    
    root@raspberrypi ~ # dmesg
    [  394.151290] bcm2708_spi bcm2708_spi.0: SPI Controller at 0x20204000 (irq 80)
    [  465.325599] can: controller area network core (rev 20090105 abi 8)
    [  465.325968] NET: Registered protocol family 29
    [  523.007604] CAN device driver interface
    [  560.310129] can: raw protocol (rev 20090105)
    [  565.070666] can: broadcast manager protocol (rev 20090105 t)
    [  593.259813] mcp251x spi0.0: CANSTAT 0x80 CANCTRL 0x07
    [  593.266881] mcp251x spi0.0: probed
    [  638.710821] mcp251x spi0.0: CNF: 0x03 0xb5 0x01
    
    # on second terminal
    root@raspberrypi ~ # candump any,0:0,#FFFFFFFF
      can0  123  [4] DE AD BE EF
      can0  123  [4] DE AD BE EF
      can0  123  [4] DE AD BE EF
      can0  123  [4] DE AD BE EF
    
    root@raspberrypi ~ # cansend can0 123#deadbeef
    root@raspberrypi ~ # cansend can0 123#deadbeef
    
    root@raspberrypi ~ # ip -s -d link show can0
    3: can0: <NOARP,UP,LOWER_UP,ECHO> mtu 16 qdisc pfifo_fast state UNKNOWN mode DEFAULT qlen 10
        link/can 
        can <LOOPBACK> state ERROR-ACTIVE restart-ms 0 
        bitrate 125000 sample-point 0.875 
        tq 500 prop-seg 6 phase-seg1 7 phase-seg2 2 sjw 1
        mcp251x: tseg1 3..16 tseg2 2..8 sjw 1..4 brp 1..64 brp-inc 1
        clock 8000000
        re-started bus-errors arbit-lost error-warn error-pass bus-off
        0          0          0          0          0          0         
        RX: bytes  packets  errors  dropped overrun mcast   
        8          2        0       0       0       0      
        TX: bytes  packets  errors  dropped carrier collsns 
        8          2        0       0       0       0      
    
    root@raspberrypi ~# cat /proc/interrupts
               CPU0       
      3:     192391   ARMCTRL  BCM2708 Timer Tick
     52:          2   ARMCTRL  BCM2708 GPIO catchall handler
     65:          2   ARMCTRL  ARM Mailbox IRQ
     66:          1   ARMCTRL  VCHIQ doorbell
     75:   14889016   ARMCTRL  dwc_otg, dwc_otg_hcd:usb1
     77:      11994   ARMCTRL  bcm2708_sdhci (dma)
     80:         58   ARMCTRL  bcm2708_spi.0
     83:         22   ARMCTRL  uart-pl011
     84:      21565   ARMCTRL  mmc0
    110:          2      GPIO  mcp251x
    Err:          0
    
    

## Misc

[Alternative MCP2515 module](http://clientes.netvisao.pt/anbadeol/mcp2515.html)  
[Faster?!](http://lnxpps.de/can2udpe/smallest-rocrail-server-ever/#mcp2515_module)  
Slightly modified:  
Look at:[mcp2515.c](http://lnxpps.de/rpie/mcp2515_mod.c) Reduced to the max

Impressum:
