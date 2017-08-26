#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import signal

import scrollphathd
import misaki_gothic

print("""
Scroll pHAT HD: Unicode scroll text

Scrolls japanese chars across the screen
in a 7x7 pixel large font.

Press Ctrl+C to exit!

""")

if len(sys.argv) > 1:
	string = u"　" + unicode(sys.argv[1], 'utf-8')
else:
	string = u"　かいぞくロボにんじゃさる"

scrollphathd.rotate(180)

scrollphathd.write_string(string, x=0, y=0, font=misaki_gothic, brightness=0.5)

while True:
    scrollphathd.show()
    scrollphathd.scroll(1)
    time.sleep(0.05)

