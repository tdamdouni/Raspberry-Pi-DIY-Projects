#!/bin/bash
cd "$(dirname "$0")"

# this example will visualize a web radio
mpg123 -s --no-seekbuffer -m -r 44100 http://icecast.djazz.se:8000/gnr | sudo ../unicorn-fft

