#!/bin/sh
export DISPLAY=:0
tvservice -p
fbset -depth 8; fbset -depth 16; xrefresh