#!/bin/bash

sudo /usr/bin/fbi -cachemem 0 --noverbose --noreadahead -T 1 -device /dev/fb0 -a --list filelist -t 5 --blend 1000 2> /dev/null 1> /dev/null
