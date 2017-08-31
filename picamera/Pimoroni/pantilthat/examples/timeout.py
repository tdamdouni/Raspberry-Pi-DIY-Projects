#!/usr/bin/env python

import time

import pantilthat

pantilthat.idle_timeout(0.5)

while True:
    pantilthat.pan(-90)
    time.sleep(3)
    pantilthat.pan(0)
    time.sleep(3)
    pantilthat.pan(90)
    time.sleep(3)
    pantilthat.pan(0)
    time.sleep(3)
