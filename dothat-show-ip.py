#!/usr/bin/env python

# http://forums.pimoroni.com/t/dothat-ip-address-at-boot/3308/3

import fcntl
import socket
import struct

import dothat.lcd as lcd


def get_addr(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])
    except IOError:
        return 'Not Found!'

wlan0 = get_addr('wlan0')
eth0 = get_addr('eth0')
host = socket.gethostname()

lcd.clear()

lcd.set_cursor_position(0,0)
lcd.write('{}'.format(host))

lcd.set_cursor_position(0,1)
if eth0 != 'Not Found!':
    lcd.write(eth0)
else:
    lcd.write('eth0 {}'.format(eth0))

lcd.set_cursor_position(0,2)
if wlan0 != 'Not Found!':
    lcd.write(wlan0)
else:
    lcd.write('wlan0 {}'.format(wlan0))
