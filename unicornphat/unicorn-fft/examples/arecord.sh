#!/bin/bash
cd "$(dirname "$0")"

# this example takes a live audio input (works great on the pi zero in uac2 gadget mode!)
# arecord will downmix to mono (plug)
arecord -f cd -c 1 | sudo ../unicorn-fft
