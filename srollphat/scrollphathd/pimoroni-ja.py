#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import signal

import scrollphathd
import misaki_gothic

print("""
Scroll pHAT HD: Hello World

Scrolls "かいぞくロボにんじゃさる" across the screen
in a 7x7 pixel large font.

Press Ctrl+C to exit!

""")

scrollphathd.rotate(180)

scrollphathd.write_string(u"　かいぞくロボにんじゃさる", x=0, y=0, font=misaki_gothic, brightness=0.5)

while True:
    scrollphathd.show()
    scrollphathd.scroll(1)
    time.sleep(0.05)

