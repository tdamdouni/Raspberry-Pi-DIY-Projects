#! /bin/sh

case "$1" in
    halt) sudo python -c 'import unicornhat; unicornhat.clear()';;
    poweroff) sudo python -c 'import unicornhat; unicornhat.clear()';;
    reboot) sudo python -c 'import unicornhat; unicornhat.clear()';;
esac