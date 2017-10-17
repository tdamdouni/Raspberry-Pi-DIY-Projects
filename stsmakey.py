#!/usr/bin/env python
"""
You will need:
* Explorer HAT Pro
* Makey Makey
* STS-Pi
* A USB battery

Note: You will probably need to grab the latest pyusb from GitHub to make this work:

git clone https://github.com/walac/pyusb
cd pyusb
sudo ./setup.py install
"""

import usb.core
import usb.util
import explorerhat
import time
import sys

explorerhat.light.red.on()

USB_VENDOR  = 0x1b4f
USB_PRODUCT = 0x2b75

USB_IF      = 0 # Interface
USB_TIMEOUT = 5 # Timeout in MS

BTN_LEFT  = 79
BTN_RIGHT = 80
BTN_DOWN  = 81
BTN_UP    = 82

dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT)
endpoint = dev[0][(2,0)][0]

for cfg in dev:
    for intf in cfg:
        if dev.is_kernel_driver_active(intf.bInterfaceNumber):
            dev.detach_kernel_driver(intf.bInterfaceNumber)

dev.set_configuration()
usb.util.claim_interface(dev, USB_IF)

explorerhat.light.red.off()
explorerhat.light.green.on()

while True:
    control = None
    try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        print(control)
    except:
        pass

    if control is not None:
        if BTN_DOWN in control:
            explorerhat.motor.backwards()

        elif BTN_UP in control:
            explorerhat.motor.forwards()

        elif BTN_LEFT in control:
            explorerhat.motor.two.forwards()
            explorerhat.motor.one.backwards()

        elif BTN_RIGHT in control:
            explorerhat.motor.two.backwards()
            explorerhat.motor.one.forwards()

        else:
            explorerhat.motor.stop()

    time.sleep(0.02)