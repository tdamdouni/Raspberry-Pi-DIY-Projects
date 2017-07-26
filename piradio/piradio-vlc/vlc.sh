#!/usr/bin/env bash
killall vlc > /dev/null 2>&1
/usr/bin/cvlc --quiet --intf rc --rc-fake-tty --rc-host 0.0.0.0:9294 --extraintf http --http-password vlcremote playlist.m3u > /dev/null & 2>&1
sleep 0.5
/bin/pidof vlc